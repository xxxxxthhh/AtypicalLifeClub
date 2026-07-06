// 汇率监控 Dashboard - 主逻辑
// 全局变量
let historicalData = null;
let currentChart = null;
let selectedBaseCurrency = 'SGD';
let selectedTargetCurrency = 'CNY';
let selectedTimeRange = 365;
let currentLang = chooseInitialLanguage();

const CURRENCIES = ['USD', 'CNY', 'SGD', 'JPY', 'AUD'];
const TIME_RANGE_OPTIONS = [30, 90, 180, 365, 730];

const I18N = {
    zh: {
        documentTitle: 'Invest Currency | Atypical Life Club',
        shellSubtitle: '汇率追踪与偏离监控',
        navBack: '返回 Invest',
        heroTitle: '汇率追踪',
        heroSubtitle: '跟踪关键货币对走势、偏离区间和阶段波动，数据由 Action 自动日更。',
        cardsTitle: '核心监控卡片',
        cardsIntro: '自动展示当前基准货币下的全部对手货币表现。',
        controlsTitle: '参数与图表',
        controlsIntro: '切换基准货币、目标货币和时间窗口，图表会同步更新。',
        baseCurrency: '基础货币',
        targetCurrency: '目标货币',
        timeRange: '时间范围',
        statsTitle: '统计摘要',
        statsIntro: '当前货币对的区间统计与偏离参考。',
        lastUpdated: '最后更新',
        dataSource: '数据来源：fawazahmed0 Currency API',
        disclaimer: '仅供个人研究，不构成投资建议。',
        dataLoadError: '数据加载失败，请刷新页面重试',
        deviation: '偏差',
        mean: '均值',
        upperBand1: '均值 + 1σ',
        lowerBand1: '均值 - 1σ',
        upperBand2: '均值 + 2σ',
        lowerBand2: '均值 - 2σ',
        dateAxis: '日期',
        rateAxis: '汇率',
        pair: '货币对',
        currentRate: '当前汇率',
        average: '平均值',
        stdDev: '标准差',
        max: '最高值',
        min: '最低值',
        currencyLabels: {
            USD: 'USD (美元)',
            CNY: 'CNY (人民币)',
            SGD: 'SGD (新加坡元)',
            JPY: 'JPY (日元)',
            AUD: 'AUD (澳元)'
        },
        rangeLabels: {
            30: '30天',
            90: '90天',
            180: '180天',
            365: '1年',
            730: '2年'
        },
        dateLocale: 'zh-CN'
    },
    en: {
        documentTitle: 'Invest Currency | Atypical Life Club',
        shellSubtitle: 'FX Tracking & Deviation Monitor',
        navBack: 'Back to Invest',
        heroTitle: 'Currency Tracker',
        heroSubtitle: 'Track key FX pairs, deviation bands, and period volatility. Data refreshes automatically.',
        cardsTitle: 'Core Monitor Cards',
        cardsIntro: 'Shows every counter-currency under the selected base currency.',
        controlsTitle: 'Controls & Chart',
        controlsIntro: 'Change the base currency, target currency, and time window to update the chart.',
        baseCurrency: 'Base Currency',
        targetCurrency: 'Target Currency',
        timeRange: 'Time Range',
        statsTitle: 'Statistical Summary',
        statsIntro: 'Period statistics and deviation reference for the selected pair.',
        lastUpdated: 'Last updated',
        dataSource: 'Data source: fawazahmed0 Currency API',
        disclaimer: 'For personal research only. Not investment advice.',
        dataLoadError: 'Data failed to load. Please refresh and try again.',
        deviation: 'Deviation',
        mean: 'Mean',
        upperBand1: 'Mean + 1σ',
        lowerBand1: 'Mean - 1σ',
        upperBand2: 'Mean + 2σ',
        lowerBand2: 'Mean - 2σ',
        dateAxis: 'Date',
        rateAxis: 'Exchange rate',
        pair: 'Pair',
        currentRate: 'Current rate',
        average: 'Average',
        stdDev: 'Standard deviation',
        max: 'High',
        min: 'Low',
        currencyLabels: {
            USD: 'USD (US dollar)',
            CNY: 'CNY (Chinese yuan)',
            SGD: 'SGD (Singapore dollar)',
            JPY: 'JPY (Japanese yen)',
            AUD: 'AUD (Australian dollar)'
        },
        rangeLabels: {
            30: '30 days',
            90: '90 days',
            180: '180 days',
            365: '1 year',
            730: '2 years'
        },
        dateLocale: 'en-US'
    }
};

// 初始化
document.addEventListener('DOMContentLoaded', async () => {
    console.log('Dashboard 初始化...');
    bindLanguageSwitch();
    applyStaticTranslations();

    // 加载数据
    await loadData();

    // 设置事件监听
    setupEventListeners();

    // 初始化目标货币选项（确保与基础货币一致）
    updateTargetCurrencyOptions();

    // 初始化显示
    updateDashboard();
});

// 加载数据
async function loadData() {
    try {
        const response = await fetch('/invest/currency/data/historical.json');
        if (!response.ok) {
            throw new Error('数据加载失败');
        }
        historicalData = await response.json();
        console.log('数据加载成功:', historicalData.metadata);
    } catch (error) {
        console.error('加载数据失败:', error);
        alert(t('dataLoadError'));
    }
}

// 设置事件监听
function setupEventListeners() {
    document.getElementById('base-currency-select').addEventListener('change', (e) => {
        selectedBaseCurrency = e.target.value;
        updateTargetCurrencyOptions();
        updateDashboard();
    });

    document.getElementById('currency-select').addEventListener('change', (e) => {
        selectedTargetCurrency = e.target.value;
        updateDashboard();
    });

    document.getElementById('timerange-select').addEventListener('change', (e) => {
        selectedTimeRange = parseInt(e.target.value);
        updateDashboard();
    });
}

// 更新目标货币选项（排除基础货币）
function updateTargetCurrencyOptions() {
    const targetSelect = document.getElementById('currency-select');
    const currentValue = targetSelect.value;

    // 清空选项
    targetSelect.innerHTML = '';

    // 添加除基础货币外的所有货币
    CURRENCIES.forEach(curr => {
        if (curr !== selectedBaseCurrency) {
            const option = document.createElement('option');
            option.value = curr;
            option.textContent = getCurrencyLabel(curr);
            targetSelect.appendChild(option);
        }
    });

    // 尝试保持之前的选择，如果不可用则选择第一个
    if (currentValue !== selectedBaseCurrency && CURRENCIES.includes(currentValue)) {
        targetSelect.value = currentValue;
        selectedTargetCurrency = currentValue;
    } else {
        selectedTargetCurrency = targetSelect.value;
    }
}

// 获取货币标签
function getCurrencyLabel(currency) {
    return labels().currencyLabels[currency] || currency;
}

// 计算货币对汇率（支持任意基础货币）
function getExchangeRate(baseRate, targetRate, base, target) {
    // 如果基础货币是 USD，直接返回目标货币汇率
    if (base === 'USD') {
        return targetRate;
    }
    // 如果目标货币是 USD，返回基础货币汇率的倒数
    if (target === 'USD') {
        return 1 / baseRate;
    }
    // 其他情况：通过 USD 作为中间货币转换
    // 例如：SGD/CNY = (USD/CNY) / (USD/SGD)
    return targetRate / baseRate;
}

// 更新整个Dashboard
function updateDashboard() {
    if (!historicalData) return;

    updateStatCards();
    updateChart();
    updateStatistics();
    updateLastUpdateTime();
}

// 更新统计卡片
function updateStatCards() {
    // 获取所有可能的货币对
    const pairs = CURRENCIES.filter(c => c !== selectedBaseCurrency);

    pairs.forEach((targetCurr, index) => {
        const stats = calculateStats(selectedBaseCurrency, targetCurr);
        const cardId = `stat-card-${index}`;

        // 更新或创建卡片
        let card = document.getElementById(cardId);
        if (!card) {
            // 如果卡片不存在，创建新的
            const grid = document.querySelector('.stats-grid');
            card = document.createElement('div');
            card.id = cardId;
            card.className = 'stat-card';
            grid.appendChild(card);
        }

        const pairName = `${selectedBaseCurrency}/${targetCurr}`;
        const changePercent = ((stats.current - stats.previous) / stats.previous * 100).toFixed(2);
        const changeSymbol = changePercent >= 0 ? '↑' : '↓';
        const deviation = Math.abs((stats.current - stats.mean) / stats.stdDev);

        // 设置卡片样式
        card.className = 'stat-card';
        if (deviation >= 2) {
            card.classList.add('alert');
        } else if (deviation >= 1.5) {
            card.classList.add('warning');
        }

        card.innerHTML = `
            <div class="stat-label">${pairName}</div>
            <div class="stat-value">${stats.current.toFixed(4)}</div>
            <div class="stat-change">${changeSymbol} ${Math.abs(changePercent)}%</div>
            <div class="stat-deviation">${t('deviation')}: ${deviation.toFixed(2)}σ</div>
        `;
    });

    // 移除多余的卡片
    const grid = document.querySelector('.stats-grid');
    const allCards = grid.querySelectorAll('.stat-card');
    allCards.forEach((card, index) => {
        if (index >= pairs.length) {
            card.remove();
        }
    });
}

// 计算统计数据（支持任意货币对）
function calculateStats(baseCurr, targetCurr) {
    const data = historicalData.historical
        .slice(-selectedTimeRange)
        .map(d => {
            const baseRate = d.rates[baseCurr] || 1; // USD 的汇率是 1
            const targetRate = d.rates[targetCurr] || 1;
            return getExchangeRate(baseRate, targetRate, baseCurr, targetCurr);
        })
        .filter(v => v !== undefined && !isNaN(v));

    if (data.length === 0) {
        return { current: 0, previous: 0, mean: 0, stdDev: 0, min: 0, max: 0 };
    }

    const current = data[data.length - 1];
    const previous = data.length > 1 ? data[data.length - 2] : current;
    const mean = data.reduce((a, b) => a + b, 0) / data.length;
    const variance = data.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / data.length;
    const stdDev = Math.sqrt(variance);
    const min = Math.min(...data);
    const max = Math.max(...data);

    return { current, previous, mean, stdDev, min, max };
}

// 更新图表
function updateChart() {
    const chartData = prepareChartData(selectedBaseCurrency, selectedTargetCurrency);

    if (currentChart) {
        currentChart.destroy();
    }

    const ctx = document.getElementById('mainChart').getContext('2d');
    const pairName = `${selectedBaseCurrency}/${selectedTargetCurrency}`;

    currentChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: chartData.labels,
            datasets: [
                {
                    label: pairName,
                    data: chartData.values,
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.4
                },
                {
                    label: t('mean'),
                    data: chartData.mean,
                    borderColor: '#48bb78',
                    borderWidth: 2,
                    borderDash: [5, 5],
                    fill: false,
                    pointRadius: 0
                },
                {
                    label: t('upperBand1'),
                    data: chartData.upperBand1,
                    borderColor: '#f6ad55',
                    borderWidth: 1,
                    borderDash: [3, 3],
                    fill: false,
                    pointRadius: 0
                },
                {
                    label: t('lowerBand1'),
                    data: chartData.lowerBand1,
                    borderColor: '#f6ad55',
                    borderWidth: 1,
                    borderDash: [3, 3],
                    fill: false,
                    pointRadius: 0
                },
                {
                    label: t('upperBand2'),
                    data: chartData.upperBand2,
                    borderColor: '#fc8181',
                    borderWidth: 1,
                    borderDash: [2, 2],
                    fill: false,
                    pointRadius: 0
                },
                {
                    label: t('lowerBand2'),
                    data: chartData.lowerBand2,
                    borderColor: '#fc8181',
                    borderWidth: 1,
                    borderDash: [2, 2],
                    fill: false,
                    pointRadius: 0
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            aspectRatio: window.innerWidth < 768 ? 1.2 : 2,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                    labels: {
                        boxWidth: window.innerWidth < 768 ? 10 : 15,
                        font: {
                            size: window.innerWidth < 768 ? 10 : 12
                        }
                    }
                },
                tooltip: {
                    mode: 'index',
                    intersect: false
                }
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: t('dateAxis')
                    },
                    ticks: {
                        maxRotation: 45,
                        minRotation: 45,
                        font: {
                            size: window.innerWidth < 768 ? 9 : 11
                        }
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: t('rateAxis')
                    },
                    ticks: {
                        font: {
                            size: window.innerWidth < 768 ? 9 : 11
                        }
                    }
                }
            }
        }
    });
}

// 准备图表数据
function prepareChartData(baseCurr, targetCurr) {
    const stats = calculateStats(baseCurr, targetCurr);
    const data = historicalData.historical.slice(-selectedTimeRange);

    const labels = data.map(d => d.date);
    const values = data.map(d => {
        const baseRate = d.rates[baseCurr] || 1;
        const targetRate = d.rates[targetCurr] || 1;
        return getExchangeRate(baseRate, targetRate, baseCurr, targetCurr);
    });

    const mean = Array(values.length).fill(stats.mean);
    const upperBand1 = Array(values.length).fill(stats.mean + stats.stdDev);
    const lowerBand1 = Array(values.length).fill(stats.mean - stats.stdDev);
    const upperBand2 = Array(values.length).fill(stats.mean + 2 * stats.stdDev);
    const lowerBand2 = Array(values.length).fill(stats.mean - 2 * stats.stdDev);

    return {
        labels,
        values,
        mean,
        upperBand1,
        lowerBand1,
        upperBand2,
        lowerBand2
    };
}

// 更新统计信息
function updateStatistics() {
    const stats = calculateStats(selectedBaseCurrency, selectedTargetCurrency);
    const pairName = `${selectedBaseCurrency}/${selectedTargetCurrency}`;

    const statsHtml = `
        <div class="stat-item">
            <div class="stat-item-label">${t('pair')}</div>
            <div class="stat-item-value">${pairName}</div>
        </div>
        <div class="stat-item">
            <div class="stat-item-label">${t('currentRate')}</div>
            <div class="stat-item-value">${stats.current.toFixed(4)}</div>
        </div>
        <div class="stat-item">
            <div class="stat-item-label">${t('average')}</div>
            <div class="stat-item-value">${stats.mean.toFixed(4)}</div>
        </div>
        <div class="stat-item">
            <div class="stat-item-label">${t('stdDev')}</div>
            <div class="stat-item-value">${stats.stdDev.toFixed(4)}</div>
        </div>
        <div class="stat-item">
            <div class="stat-item-label">${t('max')}</div>
            <div class="stat-item-value">${stats.max.toFixed(4)}</div>
        </div>
        <div class="stat-item">
            <div class="stat-item-label">${t('min')}</div>
            <div class="stat-item-value">${stats.min.toFixed(4)}</div>
        </div>
    `;

    document.getElementById('statistics').innerHTML = statsHtml;
}

// 更新最后更新时间
function updateLastUpdateTime() {
    if (historicalData && historicalData.metadata) {
        const lastUpdate = historicalData.metadata.last_updated;
        const date = new Date(lastUpdate);
        document.getElementById('last-update').textContent = date.toLocaleString(labels().dateLocale);
    }
}

function labels() {
    return I18N[currentLang] || I18N.en;
}

function t(key) {
    return labels()[key] || key;
}

function applyStaticTranslations() {
    const activeLabels = labels();
    document.documentElement.lang = currentLang === 'zh' ? 'zh-CN' : 'en';
    document.title = activeLabels.documentTitle;
    renderLanguageSwitchUI(currentLang);
    syncLanguageQuery(currentLang);

    document.querySelectorAll('[data-i18n]').forEach((el) => {
        const value = activeLabels[el.dataset.i18n];
        if (value !== undefined) el.textContent = value;
    });
    refreshCurrencySelectLabels();
    refreshTimeRangeLabels();
}

function refreshCurrencySelectLabels() {
    document.querySelectorAll('#base-currency-select option, #currency-select option').forEach((option) => {
        option.textContent = getCurrencyLabel(option.value);
    });
}

function refreshTimeRangeLabels() {
    const select = document.getElementById('timerange-select');
    if (!select) return;
    TIME_RANGE_OPTIONS.forEach((value) => {
        const option = select.querySelector(`option[value="${value}"]`);
        if (option) option.textContent = labels().rangeLabels[value] || String(value);
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
            updateTargetCurrencyOptions();
            updateDashboard();
        });
    });
}
