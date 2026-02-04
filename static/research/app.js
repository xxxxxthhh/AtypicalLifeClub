// Reports data
const reports = [
    {
        id: 'jinpan-2026',
        company: '金盘科技',
        ticker: '688676.SH',
        title: '金盘科技深度研究报告 - AI数据中心电源设备龙头',
        summary: '干式变压器细分市场龙头，全球市场份额25.5%。AIDC业务爆发式增长，数据中心订单同比增长603.68%。前瞻布局固态变压器，已送样英伟达。',
        tags: ['电力设备', 'AI数据中心', '固态变压器', '科创板'],
        category: 'tech',
        date: '2026-02-03',
        lastUpdate: '2026-02-03',
        file: '/research/reports/jinpan-2026.html',
        highlights: [
            '全球干式变压器市场份额25.5%',
            'AIDC订单增长603.68%',
            '固态变压器已送样英伟达',
            '国家级制造业单项冠军'
        ]
    },
    {
        id: 'paypal-2026',
        company: 'PayPal Holdings Inc.',
        ticker: 'NASDAQ: PYPL',
        title: 'PayPal 深度调研报告 - 2025-2026年度分析',
        summary: '数字支付巨头面临转型挑战，Q4财报未达预期导致股价暴跌16%。CEO更换、裁员7%、技术基础设施重组，市场份额受Stripe和Apple Pay威胁。',
        tags: ['金融科技', '数字支付', '企业转型', '竞争分析'],
        category: 'tech',
        date: '2026-02-03',
        lastUpdate: '2026-02-03',
        file: '/research/reports/paypal-2026.html',
        highlights: [
            'Q4财报未达预期，股价暴跌16.26%',
            'CEO更换：Enrique Lores接任',
            '裁员7%，技术基础设施重组',
            '面临Stripe和Apple Pay激烈竞争'
        ]
    },
    {
        id: 'oklo-2026',
        company: 'Oklo Inc.',
        ticker: 'NYSE: OKLO',
        title: 'OKLO 详尽调研报告 - 2026年发展前景分析',
        summary: '小型模块化核反应堆开发商，与Meta签署1.2 GW合作项目。2026年将是关键年，监管进展和项目执行将直接影响长期前景。',
        tags: ['核能', 'SMR', '清洁能源', 'AI基础设施'],
        category: 'nuclear',
        date: '2026-02-03',
        lastUpdate: '2026-02-03',
        file: '/research/reports/oklo-2026.html',
        highlights: [
            '市值115亿美元，前收入阶段公司',
            'Meta 1.2 GW核能园区合作',
            '2027-2028年首个反应堆投运',
            'NRC监管审查关键年'
        ]
    }
];

// Load reports on page load
document.addEventListener('DOMContentLoaded', () => {
    loadReports();
    setupFilters();
    updateStats();
});

function loadReports(filter = 'all') {
    const grid = document.getElementById('reportsGrid');
    const filteredReports = filter === 'all'
        ? reports
        : reports.filter(r => r.category === filter);

    grid.innerHTML = filteredReports.map(report => `
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
                    ${report.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                </div>
                ${report.highlights ? `
                    <div class="report-highlights">
                        <strong>核心要点：</strong>
                        <ul style="margin-top: 0.5rem; padding-left: 1.5rem; color: var(--text-secondary); font-size: 0.875rem;">
                            ${report.highlights.map(h => `<li>${h}</li>`).join('')}
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

function setupFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.dataset.filter;
            loadReports(filter);
        });
    });
}

function updateStats() {
    document.getElementById('reportCount').textContent = reports.length;

    const uniqueCompanies = new Set(reports.map(r => r.company));
    document.getElementById('companyCount').textContent = uniqueCompanies.size;

    const latestDate = reports.reduce((latest, r) => {
        return new Date(r.lastUpdate) > new Date(latest) ? r.lastUpdate : latest;
    }, reports[0].lastUpdate);
    document.getElementById('updateDate').textContent = latestDate;
}
