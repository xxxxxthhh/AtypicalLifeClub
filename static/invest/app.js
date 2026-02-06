const REPORTS_URL = '/invest/research/data/reports.json';
const CURRENCY_URL = '/invest/currency/data/historical.json';

function setText(id, value) {
    const el = document.getElementById(id);
    if (el) {
        el.textContent = value;
    }
}

function formatDateTime(value) {
    if (!value) return '--';
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return value;
    return date.toLocaleString('zh-CN');
}

async function loadResearchStats() {
    try {
        const response = await fetch(REPORTS_URL, { cache: 'no-store' });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const reports = await response.json();
        if (!Array.isArray(reports)) throw new Error('invalid reports data');

        setText('reportCount', String(reports.length));
        setText('coverageCount', String(new Set(reports.map((r) => r.ticker)).size));
    } catch (error) {
        console.error('Failed to load research stats:', error);
        setText('reportCount', '--');
        setText('coverageCount', '--');
    }
}

async function loadCurrencyStats() {
    try {
        const response = await fetch(CURRENCY_URL, { cache: 'no-store' });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const payload = await response.json();

        const days = payload?.metadata?.total_days;
        const updated = payload?.metadata?.last_updated;

        setText('currencyDays', Number.isFinite(days) ? String(days) : '--');
        setText('lastUpdated', formatDateTime(updated));
    } catch (error) {
        console.error('Failed to load currency stats:', error);
        setText('currencyDays', '--');
        setText('lastUpdated', '--');
    }
}

document.addEventListener('DOMContentLoaded', async () => {
    await Promise.all([loadResearchStats(), loadCurrencyStats()]);
});
