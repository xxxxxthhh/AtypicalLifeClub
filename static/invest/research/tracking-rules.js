(function () {
    const RERUN_AGE_DAYS = 60;
    const RERUN_DRIFT_PCT = 25;

    function currentUtcDay() {
        const now = new Date();
        return new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate()));
    }

    function dateFromYmd(value) {
        const match = String(value || '').match(/^(\d{4})-(0[1-9]|1[0-2])-([0-2][0-9]|3[01])$/);
        if (!match) return null;
        return new Date(Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3])));
    }

    function ageDays(value, today = currentUtcDay()) {
        const date = dateFromYmd(value);
        if (!date) return null;
        return Math.max(0, Math.floor((today.getTime() - date.getTime()) / 86400000));
    }

    function usablePriceEntry(entry) {
        return Boolean(
            entry
            && entry.status !== 'missing'
            && typeof entry.changePct === 'number'
            && Number.isFinite(entry.changePct)
        );
    }

    function buildRerunItem(report, priceEntry, today = currentUtcDay()) {
        const age = ageDays(report.priceAsOf, today);
        if (age === null) return null;

        const hasPrice = usablePriceEntry(priceEntry);
        const driftPct = hasPrice ? Math.abs(priceEntry.changePct) : null;
        const untracked = !hasPrice;
        const ageTerm = age / RERUN_AGE_DAYS;
        const driftTerm = hasPrice ? driftPct / RERUN_DRIFT_PCT : null;
        const isCandidate = age > RERUN_AGE_DAYS || (hasPrice && driftPct >= RERUN_DRIFT_PCT);
        const shouldList = isCandidate || untracked;

        return {
            report,
            priceEntry,
            ageDays: age,
            driftPct,
            untracked,
            ageTerm,
            driftTerm,
            score: ageTerm + (driftTerm || 0),
            isCandidate,
            shouldList
        };
    }

    function isRerunCandidate(report, priceEntry, today = currentUtcDay()) {
        if (!report || !report.chainLayer) return false;
        return Boolean(buildRerunItem(report, priceEntry, today)?.isCandidate);
    }

    // v6 Track 2 (docs/research-hub-v6-plan.md §3.3): a published trigger that fired
    // while the stance stayed put. Two conditions only, per spec:
    //   1. a monitoring item LINKED from stanceTriggers (the union of the upgrade and
    //      downgrade monitoringIds — not every item in monitoring[]) reads "breached";
    //   2. the stance has not changed since that item's readingAsOf.
    // The stance date is the last stanceHistory[] entry (reports.json is authoritative;
    // verdicts.json is regenerated daily). Same-day boundary: a stance dated exactly on
    // readingAsOf counts as "not changed since" and still produces a row — only a stance
    // dated strictly after the grade clears it.
    function linkedMonitoringIds(report) {
        const triggers = report && report.stanceTriggers;
        const ids = new Set();
        if (!triggers || typeof triggers !== 'object') return ids;
        ['upgrade', 'downgrade'].forEach((side) => {
            const value = triggers[side];
            const list = value && Array.isArray(value.monitoringIds) ? value.monitoringIds : [];
            list.forEach((id) => ids.add(id));
        });
        return ids;
    }

    function currentStanceDate(report) {
        const history = report && Array.isArray(report.stanceHistory) ? report.stanceHistory : [];
        if (!history.length) return null;
        return history[history.length - 1].date || null;
    }

    function buildTriggerWatchRows(reports, today = currentUtcDay()) {
        const rows = [];
        (Array.isArray(reports) ? reports : []).forEach((report) => {
            if (!report || !report.chainLayer || report.isCurrent === false) return;
            const linked = linkedMonitoringIds(report);
            if (!linked.size) return;
            const stanceDate = currentStanceDate(report);
            const breached = (Array.isArray(report.monitoring) ? report.monitoring : []).filter((item) => (
                item
                && item.reading === 'breached'
                && linked.has(item.id)
                && dateFromYmd(item.readingAsOf)
                && (!stanceDate || stanceDate <= item.readingAsOf)
            ));
            if (!breached.length) return;
            // The longest-standing breach dates the row.
            const oldest = breached.slice().sort((a, b) => a.readingAsOf.localeCompare(b.readingAsOf))[0];
            rows.push({
                report,
                reportId: report.id,
                stance: report.stance,
                conviction: report.conviction,
                stanceDate,
                items: breached,
                readingAsOf: oldest.readingAsOf,
                daysSinceBreach: ageDays(oldest.readingAsOf, today)
            });
        });
        return rows.sort((a, b) => (
            b.daysSinceBreach - a.daysSinceBreach
            || String(a.reportId).localeCompare(String(b.reportId))
        ));
    }

    function formatPercent(value) {
        if (typeof value !== 'number' || !Number.isFinite(value)) return '—';
        const rounded = Math.abs(value) < 0.05 ? 0 : value;
        return `${rounded > 0 ? '+' : ''}${rounded.toFixed(1)}%`;
    }

    window.ResearchTracking = {
        RERUN_AGE_DAYS,
        RERUN_DRIFT_PCT,
        buildRerunItem,
        isRerunCandidate,
        buildTriggerWatchRows,
        formatPercent
    };
}());
