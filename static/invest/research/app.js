let reports = [];
let pricesByReportId = new Map();
const REPORTS_DATA_URL = '/invest/research/data/reports.json';
const PRICES_DATA_URL = '/invest/research/data/prices.json';
const CURRENCY_DATA_URL = '/invest/currency/data/historical.json';
const METALS_DATA_URL = '/invest/metals/data/historical.json';
const SIGNALS_DATA_URL = '/invest/research/data/signals.json';

const CATEGORY_LABELS = {
    all: '全部',
    nuclear: '核能',
    tech: '科技',
    energy: '能源'
};

const filterState = {
    category: 'all',
    letter: 'all',
    query: ''
};

document.addEventListener('DOMContentLoaded', async () => {
    await Promise.all([loadReportsData(), loadPricesData()]);
    setupFilters();
    setupSearch();
    buildLetterStrip();
    renderReports();
    updateStats();
    await loadMarketContext();
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

        reports = sortReportsByLatestUpdate(data.filter(isCurrentReport));
    } catch (error) {
        console.error('Failed to load report metadata:', error);
        reports = [];
        renderEmptyState('研报元数据加载失败，请稍后重试。');
    }
}

async function loadPricesData() {
    try {
        const response = await fetch(PRICES_DATA_URL, { cache: 'no-store' });
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        const entries = Array.isArray(data?.entries) ? data.entries : [];
        pricesByReportId = new Map(entries
            .filter((entry) => entry && typeof entry.reportId === 'string')
            .map((entry) => [entry.reportId, entry]));
    } catch (error) {
        console.warn('Failed to load research prices:', error);
        pricesByReportId = new Map();
    }
}

function tickerLetter(report) {
    const raw = String(report.ticker || '').trim();
    const symbol = raw.includes(':') ? raw.split(':').slice(1).join(':') : raw;
    const first = (symbol.trim() || String(report.company || '').trim()).charAt(0).toUpperCase();
    return /[A-Z]/.test(first) ? first : '#';
}

async function loadMarketContext() {
    const root = document.getElementById('marketContextStrip');
    if (!root) return;

    try {
        const [currencyResponse, metalsResponse, signalsResponse] = await Promise.all([
            fetch(CURRENCY_DATA_URL, { cache: 'no-store' }),
            fetch(METALS_DATA_URL, { cache: 'no-store' }),
            fetch(SIGNALS_DATA_URL, { cache: 'no-store' })
        ]);
        if (!currencyResponse.ok || !metalsResponse.ok || !signalsResponse.ok) {
            throw new Error('market context fetch failed');
        }

        const [currency, metals, signals] = await Promise.all([
            currencyResponse.json(),
            metalsResponse.json(),
            signalsResponse.json()
        ]);
        const cny = currency?.current?.rates?.CNY;
        const gold = metals?.current?.['GC=F']?.price;
        const copper = metals?.current?.['HG=F']?.price;
        const newestSignal = (Array.isArray(signals) ? signals : [])
            .slice()
            .sort((a, b) => parseReportDate(b.date) - parseReportDate(a.date))[0];
        if (![cny, gold, copper].every((value) => typeof value === 'number' && Number.isFinite(value)) || !newestSignal) {
            throw new Error('market context data incomplete');
        }

        root.innerHTML = `
            <a class="market-context-item" href="/invest/currency/">USD/CNY ${formatNumber(cny, 4)}</a>
            <a class="market-context-item" href="/invest/metals/">Gold ${formatNumber(gold, 1)} · Copper ${formatNumber(copper, 3)}</a>
            <a class="market-context-item" href="/invest/research/monitoring-dashboard.html#${escapeHtml(signalAnchor(newestSignal))}">最新信号 ${escapeHtml(newestSignal.date || '')} · ${escapeHtml(localizeSignal(newestSignal.title))}</a>
        `;
        root.hidden = false;
    } catch (error) {
        console.warn('Failed to load market context:', error);
        root.hidden = true;
        root.innerHTML = '';
    }
}

function formatNumber(value, fractionDigits) {
    return Number(value).toLocaleString(undefined, {
        minimumFractionDigits: fractionDigits,
        maximumFractionDigits: fractionDigits
    });
}

function signalAnchor(signal) {
    return `signal-${String(signal?.id || '').replace(/[^A-Za-z0-9_-]/g, '-')}`;
}

function localizeSignal(value) {
    if (!value) return '';
    if (typeof value === 'string') return value;
    return value.zh || value.en || '';
}

function applyFilters() {
    const query = filterState.query.trim().toLowerCase();
    let list = reports.filter((report) => {
        if (filterState.category !== 'all' && report.category !== filterState.category) return false;
        if (filterState.letter !== 'all' && tickerLetter(report) !== filterState.letter) return false;
        if (query) {
            const haystack = [report.ticker, report.company, report.title, report.titleEn, report.id];
            if (!haystack.some((value) => String(value || '').toLowerCase().includes(query))) return false;
        }
        return true;
    });

    if (filterState.letter !== 'all') {
        list = [...list].sort((a, b) => String(a.ticker || '').localeCompare(String(b.ticker || '')));
    }
    return list;
}

function renderReports() {
    const grid = document.getElementById('reportsGrid');
    const filteredReports = applyFilters();

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
                ${renderTrackingChips(report)}
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

function renderTrackingChips(report) {
    const chips = [renderPriceChip(report), renderRerunChip(report)].filter(Boolean);
    if (!chips.length) return '';
    return `<div class="report-price-row">${chips.join('')}</div>`;
}

function renderPriceChip(report) {
    const entry = pricesByReportId.get(report.id);
    if (!entry) return '';
    if (entry.status === 'missing') {
        return `<span class="tag price-chip price-chip-muted">无价格数据</span>`;
    }

    if (typeof entry.changePct !== 'number' || !entry.baseDate) return '';
    const staleSuffix = entry.status === 'carried-forward' && entry.lastDate
        ? ` · 数据截至 ${entry.lastDate}`
        : '';
    return `<span class="tag price-chip">自报告 ${formatPercent(entry.changePct)}（基准 ${escapeHtml(entry.baseDate)}）${escapeHtml(staleSuffix)}</span>`;
}

function renderRerunChip(report) {
    if (!report.chainLayer || !window.ResearchTracking) return '';
    const item = window.ResearchTracking.buildRerunItem(report, pricesByReportId.get(report.id));
    if (!item || !item.isCandidate) return '';
    return '<span class="tag price-chip rerun-chip">复核候选 / rerun candidate</span>';
}

function formatPercent(value) {
    if (window.ResearchTracking) return window.ResearchTracking.formatPercent(value);
    if (typeof value !== 'number' || !Number.isFinite(value)) return '—';
    const rounded = Math.abs(value) < 0.05 ? 0 : value;
    return `${rounded > 0 ? '+' : ''}${rounded.toFixed(1)}%`;
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
            filterState.category = btn.dataset.filter;
            renderReports();
        });
    });
}

function setupSearch() {
    const input = document.getElementById('reportSearch');
    if (!input) return;
    input.addEventListener('input', () => {
        filterState.query = input.value;
        renderReports();
    });
}

function buildLetterStrip() {
    const strip = document.getElementById('letterStrip');
    if (!strip) return;

    const present = new Set(reports.map(tickerLetter));
    const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
    if (present.has('#')) letters.push('#');

    strip.innerHTML = [
        `<button class="letter-btn active" type="button" data-letter="all">全部</button>`,
        ...letters.map((letter) =>
            `<button class="letter-btn" type="button" data-letter="${letter}" ${present.has(letter) ? '' : 'disabled'}>${letter}</button>`)
    ].join('');

    strip.querySelectorAll('.letter-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            filterState.letter = btn.dataset.letter;
            strip.querySelectorAll('.letter-btn').forEach((b) => b.classList.toggle('active', b === btn));
            renderReports();
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
