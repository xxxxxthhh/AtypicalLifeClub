let reports = [];
let pricesByReportId = new Map();
let currentLang = chooseInitialLanguage();
const REPORTS_DATA_URL = '/invest/research/data/reports.json';
const PRICES_DATA_URL = '/invest/research/data/prices.json';
const CURRENCY_DATA_URL = '/invest/currency/data/historical.json';
const METALS_DATA_URL = '/invest/metals/data/historical.json';
const SIGNALS_DATA_URL = '/invest/research/data/signals.json';

const CATEGORY_LABELS = {
    zh: {
        all: '全部',
        nuclear: '核能',
        tech: '科技',
        energy: '能源',
        other: '其他'
    },
    en: {
        all: 'All',
        nuclear: 'Nuclear',
        tech: 'Technology',
        energy: 'Energy',
        other: 'Other'
    }
};

const COVERAGE_TIER_LABELS = {
    zh: {
        seed: '初览 / Seed',
        lite: '精简 / Lite',
        full: '完整 / Full'
    },
    en: {
        seed: 'Seed',
        lite: 'Lite',
        full: 'Full'
    }
};

const I18N = {
    zh: {
        documentTitle: 'Invest Research | Atypical Life Club',
        shellSubtitle: '公司研究与深度跟踪',
        navBack: '返回 Invest',
        heroTitle: '研报中心',
        heroSubtitle: '统一展示公司研究，按主题筛选，详情页采用统一模板渲染 Markdown。',
        coverageLink: 'AI 基建覆盖地图 / 研究思路',
        monitoringLink: '全书监控仪表盘',
        reviewsLink: '半年度复盘',
        rssLink: 'RSS 订阅',
        statReports: '研报数量',
        statCompanies: '覆盖公司',
        statUpdated: '最近更新',
        listTitle: '报告列表',
        filterAria: '研报分类筛选',
        filterAll: '全部',
        filterNuclear: '核能',
        filterTech: '科技',
        filterEnergy: '能源',
        searchPlaceholder: '搜索代码 / 公司 / 标题',
        searchAria: '搜索研报',
        letterAria: '按代码首字母筛选',
        loadError: '研报元数据加载失败，请稍后重试。',
        emptyFiltered: '当前筛选条件下暂无研报。',
        reportFallbackTitle: '研究报告',
        reportDate: '报告日期',
        updated: '更新',
        readReport: '阅读完整报告',
        noPriceData: '无价格数据',
        priceDataAsOf: (date) => `数据截至 ${date}`,
        sinceReport: (change, date) => `自报告 ${change}（基准 ${date}）`,
        rerunCandidate: '复核候选 / rerun candidate',
        latestSignal: '最新信号'
    },
    en: {
        documentTitle: 'Invest Research | Atypical Life Club',
        shellSubtitle: 'Company Notes & Deep Dives',
        navBack: 'Back to Invest',
        heroTitle: 'Research Center',
        heroSubtitle: 'Browse company research by theme. Report detail pages render Markdown through one shared reader.',
        coverageLink: 'AI Infrastructure Coverage Map',
        monitoringLink: 'Book-Level Monitoring Dashboard',
        reviewsLink: 'Semiannual Reviews',
        rssLink: 'RSS Feed',
        statReports: 'Reports',
        statCompanies: 'Companies',
        statUpdated: 'Latest Update',
        listTitle: 'Report List',
        filterAria: 'Research category filter',
        filterAll: 'All',
        filterNuclear: 'Nuclear',
        filterTech: 'Technology',
        filterEnergy: 'Energy',
        searchPlaceholder: 'Search ticker / company / title',
        searchAria: 'Search reports',
        letterAria: 'Filter by ticker initial',
        loadError: 'Report metadata failed to load. Please try again later.',
        emptyFiltered: 'No reports match the current filters.',
        reportFallbackTitle: 'Research Report',
        reportDate: 'Report date',
        updated: 'Updated',
        readReport: 'Read full report',
        noPriceData: 'No price data',
        priceDataAsOf: (date) => `Data as of ${date}`,
        sinceReport: (change, date) => `${change} since report (basis ${date})`,
        rerunCandidate: 'Rerun candidate',
        latestSignal: 'Latest signal'
    }
};

const filterState = {
    category: 'all',
    letter: 'all',
    query: ''
};

document.addEventListener('DOMContentLoaded', async () => {
    bindLanguageSwitch();
    applyStaticTranslations();
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
        renderEmptyState(t('loadError'));
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
            <a class="market-context-item" href="${escapeHtml(withLang('/invest/currency/'))}">USD/CNY ${formatNumber(cny, 4)}</a>
            <a class="market-context-item" href="${escapeHtml(withLang('/invest/metals/'))}">Gold ${formatNumber(gold, 1)} · Copper ${formatNumber(copper, 3)}</a>
            <a class="market-context-item" href="${escapeHtml(withLang(`/invest/research/monitoring-dashboard.html#${signalAnchor(newestSignal)}`))}">${escapeHtml(t('latestSignal'))} ${escapeHtml(newestSignal.date || '')} · ${escapeHtml(localizeSignal(newestSignal.title))}</a>
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
    if (currentLang === 'en') return value.en || '';
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
        renderEmptyState(t('emptyFiltered'));
        return;
    }

    grid.innerHTML = filteredReports.map((report) => {
        const highlights = reportHighlights(report);
        const reportHref = escapeHtml(reportUrl(report));
        const reportTitle = escapeHtml(reportTitleText(report));
        const summary = escapeHtml(reportSummaryText(report));
        return `
        <article class="report-card report-card-clickable" data-href="${reportHref}" tabindex="0" role="link" aria-label="${reportTitle}">
            <div class="report-main">
                <div class="report-headline">
                    <div class="report-company">${escapeHtml(reportCompanyText(report))} (${escapeHtml(report.ticker)})</div>
                    <span class="report-category">${escapeHtml(categoryLabel(report.category))}</span>
                </div>
                <h3 class="report-title">${reportTitle}</h3>
                <p class="report-summary">${summary}</p>
                <div class="report-meta">
                    <span>${escapeHtml(t('reportDate'))} ${escapeHtml(report.date)}</span>
                    <span>${escapeHtml(t('updated'))} ${escapeHtml(report.lastUpdate)}</span>
                </div>
                ${renderTrackingChips(report)}
                <div class="report-tags">
                    ${reportTags(report).map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join('')}
                </div>
                ${highlights.length ? `
                <ul class="report-highlights">
                    ${highlights.map((h) => `<li>${escapeHtml(h)}</li>`).join('')}
                </ul>
                ` : ''}
            </div>
            <div class="report-footer">
                <a href="${reportHref}" class="read-more">${escapeHtml(t('readReport'))}</a>
                <span class="update-badge">ID: ${escapeHtml(report.id)}</span>
            </div>
        </article>
    `;
    }).join('');

    bindCardNavigation();
}

function renderTrackingChips(report) {
    const chips = [renderTierChip(report), renderPriceChip(report), renderRerunChip(report)].filter(Boolean);
    if (!chips.length) return '';
    return `<div class="report-price-row">${chips.join('')}</div>`;
}

function renderTierChip(report) {
    if (!report.chainLayer || !report.coverageTier) return '';
    const label = tierLabel(report.coverageTier);
    if (!label) return '';
    return `<span class="tag price-chip tier-chip">${escapeHtml(label)}</span>`;
}

function renderPriceChip(report) {
    const entry = pricesByReportId.get(report.id);
    if (!entry) return '';
    if (entry.status === 'missing') {
        return `<span class="tag price-chip price-chip-muted">${escapeHtml(t('noPriceData'))}</span>`;
    }

    if (typeof entry.changePct !== 'number' || !entry.baseDate) return '';
    const staleSuffix = entry.status === 'carried-forward' && entry.lastDate
        ? ` · ${t('priceDataAsOf', entry.lastDate)}`
        : '';
    return `<span class="tag price-chip">${escapeHtml(t('sinceReport', formatPercent(entry.changePct), entry.baseDate))}${escapeHtml(staleSuffix)}</span>`;
}

function renderRerunChip(report) {
    if (!report.chainLayer || !window.ResearchTracking) return '';
    const item = window.ResearchTracking.buildRerunItem(report, pricesByReportId.get(report.id));
    if (!item || !item.isCandidate) return '';
    return `<span class="tag price-chip rerun-chip">${escapeHtml(t('rerunCandidate'))}</span>`;
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
        `<button class="letter-btn${filterState.letter === 'all' ? ' active' : ''}" type="button" data-letter="all">${escapeHtml(categoryLabel('all'))}</button>`,
        ...letters.map((letter) =>
            `<button class="letter-btn${filterState.letter === letter ? ' active' : ''}" type="button" data-letter="${letter}" ${present.has(letter) ? '' : 'disabled'}>${letter}</button>`)
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

function labels() {
    return I18N[currentLang] || I18N.en;
}

function t(key, ...args) {
    const value = labels()[key];
    return typeof value === 'function' ? value(...args) : value || key;
}

function categoryLabel(category) {
    return CATEGORY_LABELS[currentLang]?.[category] || CATEGORY_LABELS.en[category] || category || CATEGORY_LABELS[currentLang].other;
}

function tierLabel(tier) {
    return COVERAGE_TIER_LABELS[currentLang]?.[tier] || COVERAGE_TIER_LABELS.en[tier] || tier;
}

function reportTitleText(report) {
    if (currentLang === 'en') {
        return report.titleEn || reportCompanyText(report) || t('reportFallbackTitle');
    }
    return report.title || report.titleEn || report.company || t('reportFallbackTitle');
}

function reportCompanyText(report) {
    const company = report.company || report.id || '';
    if (currentLang !== 'en' || !containsCjk(company)) return company;
    const title = report.titleEn || '';
    const derived = title.split(' Deep Research Report')[0].trim();
    return derived || report.ticker || report.id || company;
}

function reportSummaryText(report) {
    if (currentLang === 'en') {
        return report.summaryEn || '';
    }
    return report.summary || report.summaryEn || '';
}

function reportTags(report) {
    if (currentLang === 'en') {
        return Array.isArray(report.tagsEn) ? report.tagsEn : [];
    }
    return Array.isArray(report.tags) ? report.tags : [];
}

function reportHighlights(report) {
    if (currentLang === 'en') {
        return Array.isArray(report.highlightsEn) ? report.highlightsEn.slice(0, 3) : [];
    }
    return Array.isArray(report.highlights) ? report.highlights.slice(0, 3) : [];
}

function containsCjk(value) {
    return /[\u3400-\u9fff]/u.test(String(value || ''));
}

function reportUrl(report) {
    return withLang(report.file || `/invest/research/reports/view.html?id=${report.id}`);
}

function withLang(url) {
    const [baseAndQuery, hash = ''] = String(url || '').split('#');
    const joiner = baseAndQuery.includes('?') ? '&' : '?';
    const href = `${baseAndQuery}${joiner}lang=${currentLang}`;
    return hash ? `${href}#${hash}` : href;
}

function applyStaticTranslations() {
    const activeLabels = labels();
    document.documentElement.lang = currentLang === 'zh' ? 'zh-CN' : 'en';
    document.title = activeLabels.documentTitle;
    renderLanguageSwitchUI(currentLang);
    syncLanguageQuery(currentLang);

    document.querySelectorAll('[data-i18n]').forEach((el) => {
        const key = el.dataset.i18n;
        const value = activeLabels[key];
        if (!key || value === undefined) return;
        if (el.classList.contains('hero-link')) {
            el.innerHTML = `${escapeHtml(value)} <span class="hero-link-arrow" aria-hidden="true">→</span>`;
        } else {
            el.textContent = value;
        }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach((el) => {
        const value = activeLabels[el.dataset.i18nPlaceholder];
        if (value !== undefined) el.setAttribute('placeholder', value);
    });

    document.querySelectorAll('[data-i18n-aria-label]').forEach((el) => {
        const value = activeLabels[el.dataset.i18nAriaLabel];
        if (value !== undefined) el.setAttribute('aria-label', value);
    });
}

function bindLanguageSwitch() {
    const root = document.getElementById('languageSwitch');
    if (!root) return;
    root.querySelectorAll('.lang-opt').forEach((button) => {
        button.addEventListener('click', () => {
            const nextLang = normalizeLanguage(button.dataset.lang);
            if (!nextLang || nextLang === currentLang) return;
            currentLang = nextLang;
            saveLanguage(currentLang);
            applyStaticTranslations();
            buildLetterStrip();
            renderReports();
            updateStats();
            loadMarketContext();
        });
    });
}
