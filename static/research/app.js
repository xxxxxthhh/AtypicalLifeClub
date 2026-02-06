let reports = [];
const REPORTS_DATA_URL = '/research/data/reports.json';

document.addEventListener('DOMContentLoaded', async () => {
    await loadReportsData();
    setupFilters();
    loadReports();
    updateStats();
});

async function loadReportsData() {
    try {
        const response = await fetch(REPORTS_DATA_URL, { cache: 'no-store' });
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        if (!Array.isArray(data)) {
            throw new Error('reports.json must be an array');
        }

        reports = data;
    } catch (error) {
        console.error('Failed to load report metadata:', error);
        reports = [];
        renderEmptyState('研报元数据加载失败，请稍后重试。');
    }
}

function loadReports(filter = 'all') {
    const grid = document.getElementById('reportsGrid');
    const filteredReports = filter === 'all'
        ? reports
        : reports.filter((r) => r.category === filter);

    if (!filteredReports.length) {
        renderEmptyState('当前筛选条件下暂无研报。');
        return;
    }

    grid.innerHTML = filteredReports.map((report) => `
        <div class="report-card" onclick="window.location.href='${report.file}'">
            <div class="report-header">
                <div class="report-company">${report.company} ${report.ticker}</div>
                <h3 class="report-title">${report.title}</h3>
                <div class="report-meta">
                    <span>📅 ${report.date}</span>
                    <span>🔄 ${report.lastUpdate}</span>
                </div>
            </div>
            <div class="report-body">
                <p class="report-summary">${report.summary}</p>
                <div class="report-tags">
                    ${(report.tags || []).map((tag) => `<span class="tag">${tag}</span>`).join('')}
                </div>
                ${report.highlights ? `
                    <div class="report-highlights">
                        <strong>核心要点：</strong>
                        <ul style="margin-top: 0.5rem; padding-left: 1.5rem; color: var(--text-secondary); font-size: 0.875rem;">
                            ${report.highlights.map((h) => `<li>${h}</li>`).join('')}
                        </ul>
                    </div>
                ` : ''}
            </div>
            <div class="report-footer">
                <a href="${report.file}" class="read-more">
                    阅读完整报告 →
                </a>
                <span class="update-badge">最近更新: ${report.lastUpdate}</span>
            </div>
        </div>
    `).join('');
}

function renderEmptyState(message) {
    const grid = document.getElementById('reportsGrid');
    if (!grid) return;
    grid.innerHTML = `<p style="padding: 1rem; color: var(--secondary);">${message}</p>`;
}

function setupFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach((btn) => {
        btn.addEventListener('click', () => {
            filterButtons.forEach((b) => b.classList.remove('active'));
            btn.classList.add('active');
            loadReports(btn.dataset.filter);
        });
    });
}

function updateStats() {
    const reportCountEl = document.getElementById('reportCount');
    const companyCountEl = document.getElementById('companyCount');
    const updateDateEl = document.getElementById('updateDate');

    reportCountEl.textContent = reports.length;
    companyCountEl.textContent = new Set(reports.map((r) => r.company)).size;

    if (!reports.length) {
        updateDateEl.textContent = '--';
        return;
    }

    const latestDate = reports.reduce((latest, r) => {
        return new Date(r.lastUpdate) > new Date(latest) ? r.lastUpdate : latest;
    }, reports[0].lastUpdate);

    updateDateEl.textContent = latestDate;
}
