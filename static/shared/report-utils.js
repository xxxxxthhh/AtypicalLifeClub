// Shared report-metadata helpers used by research/app.js and research/coverage-map.html
function isCurrentReport(report) {
    return report && report.isCurrent !== false;
}

function parseReportDate(value) {
    const timestamp = Date.parse(`${value}T00:00:00Z`);
    return Number.isNaN(timestamp) ? 0 : timestamp;
}

function sortReportsByLatestUpdate(list) {
    return [...list].sort((a, b) => {
        const updateDiff = parseReportDate(b.lastUpdate) - parseReportDate(a.lastUpdate);
        if (updateDiff !== 0) return updateDiff;

        const dateDiff = parseReportDate(b.date) - parseReportDate(a.date);
        if (dateDiff !== 0) return dateDiff;

        const leftKey = a.company || a.id || '';
        const rightKey = b.company || b.id || '';
        return leftKey.localeCompare(rightKey);
    });
}

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}
