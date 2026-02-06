const REPORTS_URL = '/invest/research/data/reports.json';
const CURRENCY_URL = '/invest/currency/data/historical.json';
const LANG_QUERY_KEY = 'lang';
const LANG_STORAGE_KEY = 'invest_home_lang';
const SUPPORTED_LANGS = ['zh', 'en'];

const I18N = {
    zh: {
        brandSubtitle: '研究 + 追踪工作区',
        navBack: '返回 Blog',
        navInvest: 'Invest',
        navResearch: 'Research',
        navCurrency: 'Currency',
        switchAriaLabel: '语言切换',
        heroTitle: '统一投资工作台',
        heroSubtitle: '研报与追踪模块统一入口。',
        statReports: '研报总数',
        statCoverage: '覆盖标的',
        statDays: '汇率样本天数',
        statUpdated: '最近数据更新',
        currentModulesTitle: '当前模块',
        currentModulesDesc: '先聚焦研究与汇率两条主线。',
        moduleResearchTitle: 'Research',
        moduleResearchDesc: '研报列表、标签筛选、双语详情切换。',
        moduleResearchButton: '进入 Research',
        moduleCurrencyTitle: 'Currency',
        moduleCurrencyDesc: '货币对走势、区间统计、偏离监控、自动日更。',
        moduleCurrencyButton: '进入 Currency',
        badgeOnline: '已上线',
        roadmapTitle: '规划中的扩展',
        roadmapDesc: '新模块按同一壳接入。',
        roadmapPreciousTitle: '贵金属追踪',
        roadmapPreciousDesc: '金银价格与区间统计。',
        roadmapPortfolioTitle: '组合观察台',
        roadmapPortfolioDesc: '持仓、风险暴露、事件日历。',
        roadmapLabTitle: '小项目并入',
        roadmapLabDesc: '统一入口，模块化接入。',
        footerNote: '仅为个人研究与记录，不构成投资建议。',
        documentTitle: 'Invest | Atypical Life Club'
    },
    en: {
        brandSubtitle: 'Research + Tracking Workspace',
        navBack: 'Back to Blog',
        navInvest: 'Invest',
        navResearch: 'Research',
        navCurrency: 'Currency',
        switchAriaLabel: 'Language switch',
        heroTitle: 'Unified Invest Workspace',
        heroSubtitle: 'A single entry for research and tracking modules.',
        statReports: 'Research Reports',
        statCoverage: 'Covered Tickers',
        statDays: 'FX Sample Days',
        statUpdated: 'Latest Data Update',
        currentModulesTitle: 'Current Modules',
        currentModulesDesc: 'Focused on research and currency tracking first.',
        moduleResearchTitle: 'Research',
        moduleResearchDesc: 'Report list, tag filters, and bilingual detail view.',
        moduleResearchButton: 'Open Research',
        moduleCurrencyTitle: 'Currency',
        moduleCurrencyDesc: 'Pair trends, range stats, deviation monitor, and daily auto updates.',
        moduleCurrencyButton: 'Open Currency',
        badgeOnline: 'Live',
        roadmapTitle: 'Planned Expansions',
        roadmapDesc: 'New modules plug into the same shell.',
        roadmapPreciousTitle: 'Precious Metals Tracker',
        roadmapPreciousDesc: 'Gold/Silver prices and range statistics.',
        roadmapPortfolioTitle: 'Portfolio Console',
        roadmapPortfolioDesc: 'Positions, risk exposure, and event calendar.',
        roadmapLabTitle: 'Side Project Hub',
        roadmapLabDesc: 'One entry point with modular onboarding.',
        footerNote: 'For personal research records only, not investment advice.',
        documentTitle: 'Invest Workspace | Atypical Life Club'
    }
};

const statsState = {
    reportCount: '--',
    coverageCount: '--',
    currencyDays: '--',
    lastUpdatedRaw: null
};

let currentLang = 'zh';

function setText(id, value) {
    const el = document.getElementById(id);
    if (el) {
        el.textContent = value;
    }
}

function getMessages() {
    return I18N[currentLang] || I18N.zh;
}

function normalizeLanguage(value) {
    const lang = String(value || '').toLowerCase();
    return SUPPORTED_LANGS.includes(lang) ? lang : '';
}

function readSavedLanguage() {
    try {
        return normalizeLanguage(window.localStorage.getItem(LANG_STORAGE_KEY));
    } catch (error) {
        return '';
    }
}

function saveLanguage(lang) {
    try {
        window.localStorage.setItem(LANG_STORAGE_KEY, lang);
    } catch (error) {
        // Ignore localStorage failures in private mode / restricted env.
    }
}

function chooseInitialLanguage() {
    const params = new URLSearchParams(window.location.search);
    const fromQuery = normalizeLanguage(params.get(LANG_QUERY_KEY));
    if (fromQuery) return fromQuery;

    const fromStorage = readSavedLanguage();
    if (fromStorage) return fromStorage;

    return 'zh';
}

function syncLanguageQuery() {
    const params = new URLSearchParams(window.location.search);
    params.set(LANG_QUERY_KEY, currentLang);
    const nextUrl = `${window.location.pathname}?${params.toString()}`;
    window.history.replaceState({}, '', nextUrl);
}

function renderLanguageSwitch() {
    const root = document.getElementById('languageSwitch');
    if (!root) return;

    root.querySelectorAll('.lang-btn').forEach((button) => {
        button.classList.toggle('active', button.dataset.lang === currentLang);
        button.setAttribute('aria-pressed', button.dataset.lang === currentLang ? 'true' : 'false');
    });
}

function applyTranslations() {
    const messages = getMessages();
    document.querySelectorAll('[data-i18n]').forEach((el) => {
        const key = el.dataset.i18n;
        if (messages[key]) {
            el.textContent = messages[key];
        }
    });

    const switchRoot = document.getElementById('languageSwitch');
    if (switchRoot) {
        switchRoot.setAttribute('aria-label', messages.switchAriaLabel);
    }

    document.documentElement.lang = currentLang === 'zh' ? 'zh-CN' : 'en';
    document.title = messages.documentTitle;
    renderLanguageSwitch();
    syncLanguageQuery();
}

function bindLanguageSwitch() {
    const root = document.getElementById('languageSwitch');
    if (!root) return;

    root.querySelectorAll('.lang-btn').forEach((button) => {
        button.addEventListener('click', () => {
            const targetLang = normalizeLanguage(button.dataset.lang);
            if (!targetLang || targetLang === currentLang) {
                return;
            }
            currentLang = targetLang;
            saveLanguage(currentLang);
            applyTranslations();
            renderStats();
        });
    });
}

function formatDateTime(value) {
    if (!value) return '--';
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return value;
    return date.toLocaleString(currentLang === 'en' ? 'en-US' : 'zh-CN');
}

function renderStats() {
    setText('reportCount', statsState.reportCount);
    setText('coverageCount', statsState.coverageCount);
    setText('currencyDays', statsState.currencyDays);
    setText('lastUpdated', formatDateTime(statsState.lastUpdatedRaw));
}

async function loadResearchStats() {
    try {
        const response = await fetch(REPORTS_URL, { cache: 'no-store' });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const reports = await response.json();
        if (!Array.isArray(reports)) throw new Error('invalid reports data');

        statsState.reportCount = String(reports.length);
        statsState.coverageCount = String(new Set(reports.map((r) => r.ticker)).size);
    } catch (error) {
        console.error('Failed to load research stats:', error);
        statsState.reportCount = '--';
        statsState.coverageCount = '--';
    }
    renderStats();
}

async function loadCurrencyStats() {
    try {
        const response = await fetch(CURRENCY_URL, { cache: 'no-store' });
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const payload = await response.json();

        const days = payload?.metadata?.total_days;
        const updated = payload?.metadata?.last_updated;

        statsState.currencyDays = Number.isFinite(days) ? String(days) : '--';
        statsState.lastUpdatedRaw = updated || null;
    } catch (error) {
        console.error('Failed to load currency stats:', error);
        statsState.currencyDays = '--';
        statsState.lastUpdatedRaw = null;
    }
    renderStats();
}

document.addEventListener('DOMContentLoaded', async () => {
    currentLang = chooseInitialLanguage();
    applyTranslations();
    bindLanguageSwitch();
    await Promise.all([loadResearchStats(), loadCurrencyStats()]);
});
