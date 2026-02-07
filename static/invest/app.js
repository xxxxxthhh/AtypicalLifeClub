const REPORTS_URL = "/invest/research/data/reports.json";
const CURRENCY_URL = "/invest/currency/data/historical.json";
const METALS_URL = "/invest/metals/data/historical.json";
const LANG_QUERY_KEY = "lang";
const LANG_STORAGE_KEY = "invest_home_lang";
const SUPPORTED_LANGS = ["zh", "en"];

const I18N = {
  zh: {
    navBack: "返回 Blog",
    navInvest: "投资",
    navResearch: "企业调研",
    navCurrency: "汇率追踪",
    switchAriaLabel: "语言切换",
    heroTitle: "总览",
    statReports: "研报总数",
    statCoverage: "覆盖标的",
    statDays: "汇率样本天数",
    statUpdated: "最近数据更新",
    currentModulesTitle: "当前模块",
    moduleResearchTitle: "企业调研",
    moduleResearchButton: "打开 Research",
    moduleCurrencyTitle: "汇率追踪",
    moduleCurrencyButton: "打开 Currency",
    moduleMetalsTitle: "金属追踪",
    moduleMetalsButton: "打开 Metals",
    metricAssets: "追踪标的",
    metricReports: "研报数量",
    metricCoverage: "覆盖标的",
    metricDays: "样本天数",
    metricUpdated: "最近更新",
    metricStatus: "数据状态",
    metricStatusValue: "自动日更",
    documentTitle: "Invest | Atypical Life Club",
  },
  en: {
    navBack: "Back to Blog",
    navInvest: "Invest",
    navResearch: "Research",
    navCurrency: "Currency",
    switchAriaLabel: "Language switch",
    heroTitle: "Overview",
    statReports: "Research Reports",
    statCoverage: "Covered Tickers",
    statDays: "FX Sample Days",
    statUpdated: "Latest Data Update",
    currentModulesTitle: "Current Modules",
    moduleResearchTitle: "Research",
    moduleResearchButton: "Open Research",
    moduleCurrencyTitle: "Currency",
    moduleCurrencyButton: "Open Currency",
    moduleMetalsTitle: "Metals",
    moduleMetalsButton: "Open Metals",
    metricAssets: "Assets",
    metricReports: "Reports",
    metricCoverage: "Coverage",
    metricDays: "Sample Days",
    metricUpdated: "Updated",
    metricStatus: "Data Status",
    metricStatusValue: "Daily Refresh",
    documentTitle: "Invest Workspace | Atypical Life Club",
  },
};

const statsState = {
  reportCount: "--",
  coverageCount: "--",
  currencyDays: "--",
  metalsAssets: "--",
  researchUpdatedRaw: null,
  currencyUpdatedRaw: null,
  metalsUpdatedRaw: null,
};

let currentLang = "zh";

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function getMessages() {
  return I18N[currentLang] || I18N.zh;
}

function normalizeLanguage(value) {
  const lang = String(value || "").toLowerCase();
  return SUPPORTED_LANGS.includes(lang) ? lang : "";
}
