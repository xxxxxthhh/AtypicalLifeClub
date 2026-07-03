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

    function formatPercent(value) {
        if (typeof value !== 'number' || !Number.isFinite(value)) return '—';
        const rounded = Math.abs(value) < 0.05 ? 0 : value;
        return `${rounded > 0 ? '+' : ''}${rounded.toFixed(1)}%`;
    }

    window.ResearchTracking = {
        RERUN_AGE_DAYS,
        RERUN_DRIFT_PCT,
        buildRerunItem,
        formatPercent
    };
}());
