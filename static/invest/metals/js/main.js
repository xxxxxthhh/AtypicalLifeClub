/**
 * Metals Module - Main JavaScript
 * Pure vanilla JS, no dependencies except Chart.js (CDN)
 */

// === State ===
let DATA = null;
let priceChart = null;
let compareChart = null;
let selectedSymbol = "GC=F";
let compareSymbols = ["GC=F", "SI=F"];
let currentLang = chooseInitialLanguage();

const COLORS = [
  "#667eea", "#ed8936", "#38a169", "#e53e3e",
  "#9f7aea", "#3182ce", "#d69e2e", "#dd6b20",
];

const RANGE_OPTIONS = [30, 90, 180, 365, 730];
const COMPARE_RANGE_OPTIONS = [30, 90, 180, 365];

const I18N = {
  zh: {
    documentTitle: "Metals | Invest | Atypical Life Club",
    shellSubtitle: "贵金属与 ETF 跟踪",
    navBack: "返回 Invest",
    heroTitle: "金属追踪",
    heroSubtitle: "贵金属现货 & 金属相关 ETF · 数据由 Action 自动日更",
    metalsTitle: "贵金属现货",
    etfTitle: "金属 ETF",
    chartTitle: "价格走势",
    compareTitle: "对比模式",
    compareHint: "选择标的进行归一化对比（最多5个）",
    dataSource: "数据来源: Yahoo Finance",
    lastUpdated: "最后更新",
    disclaimer: "仅供个人研究参考，不构成投资建议。",
    preciousMetals: "贵金属",
    mean: "均值",
    target: "标的",
    current: "当前",
    stdDev: "标准差",
    high: "最高",
    low: "最低",
    normalized: "归一化 (起点=100)",
    rangeLabels: {
      30: "30天",
      90: "90天",
      180: "180天",
      365: "1年",
      730: "2年",
    },
  },
  en: {
    documentTitle: "Metals | Invest | Atypical Life Club",
    shellSubtitle: "Precious Metals & ETF Tracker",
    navBack: "Back to Invest",
    heroTitle: "Metals Tracker",
    heroSubtitle: "Precious metals spot prices & metal-related ETFs · Data refreshes automatically",
    metalsTitle: "Precious Metal Spot Prices",
    etfTitle: "Metal ETFs",
    chartTitle: "Price Trend",
    compareTitle: "Comparison Mode",
    compareHint: "Select assets for normalized comparison (up to 5)",
    dataSource: "Data source: Yahoo Finance",
    lastUpdated: "Last updated",
    disclaimer: "For personal research only. Not investment advice.",
    preciousMetals: "Precious Metals",
    mean: "Mean",
    target: "Asset",
    current: "Current",
    stdDev: "Standard deviation",
    high: "High",
    low: "Low",
    normalized: "Normalized (start = 100)",
    rangeLabels: {
      30: "30 days",
      90: "90 days",
      180: "180 days",
      365: "1 year",
      730: "2 years",
    },
  },
};

// === Init ===
async function init() {
  try {
    bindLanguageSwitch();
    applyStaticTranslations();
    const resp = await fetch("/invest/metals/data/historical.json");
    DATA = await resp.json();
    document.getElementById("lastUpdated").textContent =
      DATA.metadata.last_updated.split("T")[0];
    populateSymbolSelect();
    renderMetalsCards();
    renderEtfCards();
    renderCompareToggles();
    updateChart();
    updateCompareChart();
    bindEvents();
  } catch (e) {
    console.error("Failed to load data:", e);
  }
}

// === Helpers ===
function getAllSymbols() {
  const m = Object.keys(DATA.metadata.metals);
  const e = Object.keys(DATA.metadata.etfs);
  return [...m, ...e];
}

function getSymbolName(sym) {
  if (DATA.metadata.metals[sym]) return DATA.metadata.metals[sym].name;
  if (DATA.metadata.etfs[sym]) return DATA.metadata.etfs[sym].name;
  return sym;
}

function getHistory(sym) {
  return DATA.metals[sym] || DATA.etfs[sym] || [];
}

function formatPrice(val) {
  if (val >= 1000) return val.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  if (val >= 10) return val.toFixed(2);
  return val.toFixed(4);
}

function calcStats(history, days) {
  const slice = history.slice(-days);
  if (!slice.length) return null;
  const closes = slice.map(d => d.close);
  const mean = closes.reduce((a, b) => a + b, 0) / closes.length;
  const variance = closes.reduce((a, b) => a + (b - mean) ** 2, 0) / closes.length;
  const stdDev = Math.sqrt(variance);
  return {
    mean: mean,
    stdDev: stdDev,
    min: Math.min(...closes),
    max: Math.max(...closes),
    current: closes[closes.length - 1],
    sigma: stdDev > 0 ? (closes[closes.length - 1] - mean) / stdDev : 0,
  };
}

document.addEventListener("DOMContentLoaded", init);

// === Populate Symbol Select ===
function populateSymbolSelect() {
  const sel = document.getElementById("symbolSelect");
  sel.innerHTML = "";
  const metals = Object.keys(DATA.metadata.metals);
  const etfs = Object.keys(DATA.metadata.etfs);

  const grpM = document.createElement("optgroup");
  grpM.label = t("preciousMetals");
  metals.forEach(s => {
    const opt = document.createElement("option");
    opt.value = s;
    opt.textContent = getSymbolName(s);
    if (s === selectedSymbol) opt.selected = true;
    grpM.appendChild(opt);
  });
  sel.appendChild(grpM);

  const grpE = document.createElement("optgroup");
  grpE.label = "ETF";
  etfs.forEach(s => {
    const opt = document.createElement("option");
    opt.value = s;
    opt.textContent = `${s} - ${getSymbolName(s)}`;
    if (s === selectedSymbol) opt.selected = true;
    grpE.appendChild(opt);
  });
  sel.appendChild(grpE);
}

// === Render Cards ===
function renderCard(sym, container) {
  const cur = DATA.current[sym];
  if (!cur) return;
  const history = getHistory(sym);
  const stats = calcStats(history, 90);
  const sigma = stats ? stats.sigma : 0;
  const absSigma = Math.abs(sigma);

  let cls = "stat-card";
  if (sym === selectedSymbol) cls += " active";
  if (absSigma >= 2) cls += " alert";
  else if (absSigma >= 1.5) cls += " warning";

  const isUp = cur.changePct >= 0;
  const arrow = isUp ? "↑" : "↓";
  const changeCls = isUp ? "up" : "down";

  const card = document.createElement("div");
  card.className = cls;
  card.dataset.symbol = sym;
  card.innerHTML = `
    <div class="card-name">${getSymbolName(sym)}</div>
    <div class="card-price">${formatPrice(cur.price)}</div>
    <div class="card-change ${changeCls}">${arrow} ${cur.changePct.toFixed(2)}%</div>
    <div class="card-sigma">σ: ${sigma.toFixed(2)}</div>
  `;
  card.addEventListener("click", () => {
    selectedSymbol = sym;
    document.getElementById("symbolSelect").value = sym;
    renderMetalsCards();
    renderEtfCards();
    updateChart();
  });
  container.appendChild(card);
}

function renderMetalsCards() {
  const el = document.getElementById("metalsCards");
  el.innerHTML = "";
  Object.keys(DATA.metadata.metals).forEach(s => renderCard(s, el));
}

function renderEtfCards() {
  const el = document.getElementById("etfCards");
  el.innerHTML = "";
  Object.keys(DATA.metadata.etfs).forEach(s => renderCard(s, el));
}

// === Price Chart ===
function updateChart() {
  const days = parseInt(document.getElementById("rangeSelect").value);
  const history = getHistory(selectedSymbol).slice(-days);
  if (!history.length) return;

  const labels = history.map(d => d.date);
  const closes = history.map(d => d.close);
  const stats = calcStats(getHistory(selectedSymbol), days);

  const datasets = [
    {
      label: getSymbolName(selectedSymbol),
      data: closes,
      borderColor: "#667eea",
      backgroundColor: "rgba(102,126,234,0.08)",
      fill: true,
      tension: 0.3,
      pointRadius: 0,
      borderWidth: 2,
    },
  ];

  if (stats) {
    datasets.push({
      label: t("mean"),
      data: Array(closes.length).fill(stats.mean),
      borderColor: "#38a169",
      borderDash: [6, 3],
      pointRadius: 0,
      borderWidth: 1.5,
      fill: false,
    });
  }

  if (priceChart) priceChart.destroy();
  priceChart = new Chart(document.getElementById("priceChart"), {
    type: "line",
    data: { labels, datasets },
    options: chartOptions(),
  });

  updateStatsGrid(stats);
}

function chartOptions() {
  return {
    responsive: true,
    aspectRatio: window.innerWidth < 760 ? 1.2 : 2,
    interaction: { mode: "index", intersect: false },
    plugins: {
      legend: { position: "top", labels: { font: { size: 12 } } },
      tooltip: { mode: "index", intersect: false },
    },
    scales: {
      x: {
        ticks: { maxTicksLimit: 8, font: { size: 11 } },
        grid: { display: false },
      },
      y: {
        ticks: { font: { size: 11 } },
        grid: { color: "rgba(0,0,0,0.05)" },
      },
    },
  };
}

// === Stats Grid ===
function updateStatsGrid(stats) {
  const el = document.getElementById("statsGrid");
  if (!stats) { el.innerHTML = ""; return; }
  el.innerHTML = `
    <div class="stats-item">
      <div class="stats-label">${t("target")}</div>
      <div class="stats-value">${getSymbolName(selectedSymbol)}</div>
    </div>
    <div class="stats-item">
      <div class="stats-label">${t("current")}</div>
      <div class="stats-value">${formatPrice(stats.current)}</div>
    </div>
    <div class="stats-item">
      <div class="stats-label">${t("mean")}</div>
      <div class="stats-value">${formatPrice(stats.mean)}</div>
    </div>
    <div class="stats-item">
      <div class="stats-label">${t("stdDev")}</div>
      <div class="stats-value">${formatPrice(stats.stdDev)}</div>
    </div>
    <div class="stats-item">
      <div class="stats-label">${t("high")}</div>
      <div class="stats-value">${formatPrice(stats.max)}</div>
    </div>
    <div class="stats-item">
      <div class="stats-label">${t("low")}</div>
      <div class="stats-value">${formatPrice(stats.min)}</div>
    </div>
  `;
}

// === Compare Toggles ===
function renderCompareToggles() {
  const el = document.getElementById("compareToggles");
  el.innerHTML = "";
  getAllSymbols().forEach((sym, i) => {
    const btn = document.createElement("button");
    btn.className = "toggle-btn" + (compareSymbols.includes(sym) ? " active" : "");
    btn.textContent = DATA.metadata.metals[sym] ? getSymbolName(sym) : sym;
    btn.addEventListener("click", () => toggleCompare(sym));
    el.appendChild(btn);
  });
}

function toggleCompare(sym) {
  const idx = compareSymbols.indexOf(sym);
  if (idx >= 0) {
    if (compareSymbols.length <= 1) return;
    compareSymbols.splice(idx, 1);
  } else {
    if (compareSymbols.length >= 5) return;
    compareSymbols.push(sym);
  }
  renderCompareToggles();
  updateCompareChart();
}

// === Compare Chart ===
function updateCompareChart() {
  const days = parseInt(document.getElementById("compareRange").value);
  const datasets = [];

  compareSymbols.forEach((sym, i) => {
    const history = getHistory(sym).slice(-days);
    if (!history.length) return;
    const base = history[0].close;
    const normalized = history.map(d => (d.close / base) * 100);
    datasets.push({
      label: DATA.metadata.metals[sym] ? getSymbolName(sym) : sym,
      data: normalized,
      borderColor: COLORS[i % COLORS.length],
      pointRadius: 0,
      borderWidth: 2,
      tension: 0.3,
      fill: false,
    });
  });

  // Use longest series for labels
  let maxLen = 0;
  let labelsSource = [];
  compareSymbols.forEach(sym => {
    const h = getHistory(sym).slice(-days);
    if (h.length > maxLen) {
      maxLen = h.length;
      labelsSource = h.map(d => d.date);
    }
  });

  if (compareChart) compareChart.destroy();
  compareChart = new Chart(document.getElementById("compareChart"), {
    type: "line",
    data: { labels: labelsSource, datasets },
    options: compareChartOptions(),
  });
}

function compareChartOptions() {
  return {
    responsive: true,
    aspectRatio: window.innerWidth < 760 ? 1.2 : 2,
    interaction: { mode: "index", intersect: false },
    plugins: {
      legend: { position: "top", labels: { font: { size: 12 } } },
      tooltip: {
        mode: "index",
        intersect: false,
        callbacks: {
          label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y.toFixed(1)}`,
        },
      },
    },
    scales: {
      x: {
        ticks: { maxTicksLimit: 8, font: { size: 11 } },
        grid: { display: false },
      },
      y: {
        ticks: {
          font: { size: 11 },
          callback: (v) => v.toFixed(0),
        },
        grid: { color: "rgba(0,0,0,0.05)" },
        title: { display: true, text: t("normalized"), font: { size: 11 } },
      },
    },
  };
}

// === Event Bindings ===
function bindEvents() {
  document.getElementById("symbolSelect").addEventListener("change", (e) => {
    selectedSymbol = e.target.value;
    renderMetalsCards();
    renderEtfCards();
    updateChart();
  });

  document.getElementById("rangeSelect").addEventListener("change", () => {
    updateChart();
  });

  document.getElementById("compareRange").addEventListener("change", () => {
    updateCompareChart();
  });
}

function labels() {
  return I18N[currentLang] || I18N.en;
}

function t(key) {
  return labels()[key] || key;
}

function applyStaticTranslations() {
  const activeLabels = labels();
  document.documentElement.lang = currentLang === "zh" ? "zh-CN" : "en";
  document.title = activeLabels.documentTitle;
  renderLanguageSwitchUI(currentLang);
  syncLanguageQuery(currentLang);

  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const value = activeLabels[el.dataset.i18n];
    if (value !== undefined) el.textContent = value;
  });
  refreshRangeLabels("rangeSelect", RANGE_OPTIONS);
  refreshRangeLabels("compareRange", COMPARE_RANGE_OPTIONS);
}

function refreshRangeLabels(selectId, options) {
  const select = document.getElementById(selectId);
  if (!select) return;
  options.forEach((value) => {
    const option = select.querySelector(`option[value="${value}"]`);
    if (option) option.textContent = labels().rangeLabels[value] || String(value);
  });
}

function bindLanguageSwitch() {
  const root = document.getElementById("languageSwitch");
  if (!root) return;
  root.querySelectorAll(".lang-opt").forEach((button) => {
    button.addEventListener("click", () => {
      const nextLang = normalizeLanguage(button.dataset.lang);
      if (!nextLang || nextLang === currentLang) return;
      currentLang = nextLang;
      saveLanguage(currentLang);
      applyStaticTranslations();
      if (!DATA) return;
      populateSymbolSelect();
      renderMetalsCards();
      renderEtfCards();
      renderCompareToggles();
      updateChart();
      updateCompareChart();
    });
  });
}
