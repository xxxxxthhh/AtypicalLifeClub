let reports = [];
const REPORTS_DATA_URL = '/invest/research/data/reports.json';

const CATEGORY_LABELS = {
    all: '全部',
    nuclear: '核能',
    tech: '科技',
    energy: '能源'
};

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

    grid.innerHTML = filteredReports.map((report) => {
        const highlights = Array.isArray(report.highlights) ? report.highlights.slice(0, 3) : [];
        const reportHref = escapeHtml(report.file || '');
        const reportTitle = escapeHtml(report.title || report.company || '研究报告');
        return `
        <article class="report-card report-card-clickable" data-href="${reportHref}" tabindex="0" role="link" aria-label="${reportTitle}">
            <div class="report-main">
                <div class="report-headline">
                    <div class="report-company">${escapeHtml(report.company)} (${escapeHtml(report.ticker)})</div>
                    <span class="report-category">${escapeHtml(CATEGORY_LABELS[report.category] || report.category || '其他')}</span>
                </div>
                <h3 class="report-title">${escapeHtml(report.title)}</h3>
                <p class="report-summary">${escapeHtml(report.summary)}</p>
                <div class="report-meta">
                    <span>报告日期 ${escapeHtml(report.date)}</span>
                    <span>更新 ${escapeHtml(report.lastUpdate)}</span>
                </div>
                <div class="report-tags">
                    ${(report.tags || []).map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join('')}
                </div>
                ${highlights.length ? `
                <ul class="report-highlights">
                    ${highlights.map((h) => `<li>${escapeHtml(h)}</li>`).join('')}
                </ul>
                ` : ''}
            </div>
            <div class="report-footer">
                <a href="${reportHref}" class="read-more">阅读完整报告</a>
                <span class="update-badge">ID: ${escapeHtml(report.id)}</span>
            </div>
        </article>
    `;
    }).join('');

    bindCardNavigation();
}

function renderEmptyState(message) {
    const grid = document.getElementById('reportsGrid');
    if (!grid) return;
    grid.innerHTML = `<div class="empty-state">${escapeHtml(message)}</div>`;
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

function bindCardNavigation() {
    const cards = document.querySelectorAll('.report-card-clickable[data-href]');
    cards.forEach((card) => {
        const targetUrl = card.dataset.href;
        if (!targetUrl) return;

        card.addEventListener('click', (event) => {
            if (event.target.closest('a, button')) return;
            window.location.href = targetUrl;
        });

        card.addEventListener('keydown', (event) => {
            if (event.key !== 'Enter' && event.key !== ' ') return;
            event.preventDefault();
            window.location.href = targetUrl;
        });
    });
}

function updateStats() {
    const reportCountEl = document.getElementById('reportCount');
    const companyCountEl = document.getElementById('companyCount');
    const updateDateEl = document.getElementById('updateDate');

    reportCountEl.textContent = String(reports.length);
    companyCountEl.textContent = String(new Set(reports.map((r) => r.company)).size);

    if (!reports.length) {
        updateDateEl.textContent = '--';
        return;
    }

    const latestDate = reports.reduce((latest, r) => {
        return new Date(r.lastUpdate) > new Date(latest) ? r.lastUpdate : latest;
    }, reports[0].lastUpdate);

    updateDateEl.textContent = latestDate;
}

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}
