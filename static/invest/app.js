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
    moduleCurrencyTitle: "汇率追踪",
    moduleMetalsTitle: "金属追踪",
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
    moduleCurrencyTitle: "Currency",
    moduleMetalsTitle: "Metals",
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
  if (el) {
    el.textContent = value;
  }
}

function getMessages() {
  return I18N[currentLang] || I18N.zh;
}

function normalizeLanguage(value) {
  const lang = String(value || "").toLowerCase();
  return SUPPORTED_LANGS.includes(lang) ? lang : "";
}

function readSavedLanguage() {
  try {
    return normalizeLanguage(window.localStorage.getItem(LANG_STORAGE_KEY));
  } catch (error) {
    return "";
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

  return "zh";
}

function syncLanguageQuery() {
  const params = new URLSearchParams(window.location.search);
  params.set(LANG_QUERY_KEY, currentLang);
  const nextUrl = `${window.location.pathname}?${params.toString()}`;
  window.history.replaceState({}, "", nextUrl);
}

function renderLanguageSwitch() {
  const root = document.getElementById("languageSwitch");
  if (!root) return;

  root.querySelectorAll(".lang-opt").forEach((button) => {
    button.classList.toggle("active", button.dataset.lang === currentLang);
    button.setAttribute(
      "aria-pressed",
      button.dataset.lang === currentLang ? "true" : "false",
    );
  });
}

function applyTranslations() {
  const messages = getMessages();
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.dataset.i18n;
    if (messages[key]) {
      el.textContent = messages[key];
    }
  });

  const switchRoot = document.getElementById("languageSwitch");
  if (switchRoot) {
    switchRoot.setAttribute("aria-label", messages.switchAriaLabel);
  }

  document.documentElement.lang = currentLang === "zh" ? "zh-CN" : "en";
  document.title = messages.documentTitle;
  renderLanguageSwitch();
  syncLanguageQuery();
}

function bindLanguageSwitch() {
  const root = document.getElementById("languageSwitch");
  if (!root) return;

  root.querySelectorAll(".lang-opt").forEach((button) => {
    button.addEventListener("click", () => {
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
  if (!value) return "--";
  if (typeof value === "string" && /^\d{4}-\d{2}-\d{2}$/.test(value)) {
    const dateOnly = new Date(`${value}T00:00:00`);
    if (!Number.isNaN(dateOnly.getTime())) {
      return dateOnly.toLocaleDateString(
        currentLang === "en" ? "en-US" : "zh-CN",
      );
    }
  }
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleString(currentLang === "en" ? "en-US" : "zh-CN");
}

function pickMostRecent(values) {
  let latestValue = null;
  let latestTs = -Infinity;

  values.forEach((value) => {
    if (!value) return;
    const ts = new Date(value).getTime();
    if (Number.isNaN(ts)) return;
    if (ts > latestTs) {
      latestTs = ts;
      latestValue = value;
    }
  });

  if (latestValue) return latestValue;
  return values.find((value) => !!value) || null;
}

function renderStats() {
  const globalUpdated = pickMostRecent([
    statsState.researchUpdatedRaw,
    statsState.currencyUpdatedRaw,
    statsState.metalsUpdatedRaw,
  ]);

  setText("reportCount", statsState.reportCount);
  setText("coverageCount", statsState.coverageCount);
  setText("currencyDays", statsState.currencyDays);
  setText("lastUpdated", formatDateTime(globalUpdated));

  setText("moduleResearchReports", statsState.reportCount);
  setText("moduleResearchCoverage", statsState.coverageCount);
  setText(
    "moduleResearchUpdated",
    formatDateTime(statsState.researchUpdatedRaw),
  );

  setText("moduleCurrencyDays", statsState.currencyDays);
  setText(
    "moduleCurrencyUpdated",
    formatDateTime(statsState.currencyUpdatedRaw),
  );

  setText("moduleMetalsAssets", statsState.metalsAssets);
  setText("moduleMetalsUpdated", formatDateTime(statsState.metalsUpdatedRaw));
}

async function loadResearchStats() {
  try {
    const response = await fetch(REPORTS_URL, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const reports = await response.json();
    if (!Array.isArray(reports)) throw new Error("invalid reports data");

    statsState.reportCount = String(reports.length);
    statsState.coverageCount = String(
      new Set(reports.map((r) => r.ticker)).size,
    );
    statsState.researchUpdatedRaw = pickMostRecent(
      reports.map((r) => r.lastUpdate || r.date),
    );
  } catch (error) {
    console.error("Failed to load research stats:", error);
    statsState.reportCount = "--";
    statsState.coverageCount = "--";
    statsState.researchUpdatedRaw = null;
  }
  renderStats();
}

async function loadCurrencyStats() {
  try {
    const response = await fetch(CURRENCY_URL, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const payload = await response.json();

    const days = payload?.metadata?.total_days;
    const updated = payload?.metadata?.last_updated;

    statsState.currencyDays = Number.isFinite(days) ? String(days) : "--";
    statsState.currencyUpdatedRaw = updated || null;
  } catch (error) {
    console.error("Failed to load currency stats:", error);
    statsState.currencyDays = "--";
    statsState.currencyUpdatedRaw = null;
  }
  renderStats();
}

async function loadMetalsStats() {
  try {
    const response = await fetch(METALS_URL, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const payload = await response.json();

    const metadata = payload?.metadata || {};
    const totalMetals = metadata.total_metals;
    const totalEtfs = metadata.total_etfs;
    let assets = null;

    if (Number.isFinite(totalMetals) || Number.isFinite(totalEtfs)) {
      assets =
        (Number.isFinite(totalMetals) ? totalMetals : 0) +
        (Number.isFinite(totalEtfs) ? totalEtfs : 0);
    } else if (payload?.current && typeof payload.current === "object") {
      assets = Object.keys(payload.current).length;
    }

    statsState.metalsAssets = Number.isFinite(assets) ? String(assets) : "--";
    statsState.metalsUpdatedRaw = metadata.last_updated || null;
  } catch (error) {
    console.error("Failed to load metals stats:", error);
    statsState.metalsAssets = "--";
    statsState.metalsUpdatedRaw = null;
  }
  renderStats();
}

document.addEventListener("DOMContentLoaded", async () => {
  currentLang = chooseInitialLanguage();
  applyTranslations();
  bindLanguageSwitch();
  await Promise.all([loadResearchStats(), loadCurrencyStats(), loadMetalsStats()]);
});
