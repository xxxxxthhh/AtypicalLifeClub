// Editorial preview entries are explicit publication records, not inferred from
// lastUpdate or financial-number diffs. Historical dates are never relabelled today.
const TEXT = {
    zh: {
        title: '研究更新', kicker: 'RESEARCH JOURNAL',
        intro: '今天的研究，与此前相比改变了什么。',
        preview: '历史内容预览 · 使用 11 月 10 日与 11 月 2 日的真实研究更新，保留原日期；尚未接入自动日更。',
        date: '更新日期', all: '全部类型', facts: '事实与事件', stance: '判断调整',
        change: '改了什么', meaning: '如何影响判断', next: '接下来关注',
        report: '阅读报告', evidence: '查看证据记录', evidenceDate: '证据日期',
        empty: '这一天没有符合筛选条件的更新。',
        error: '研究更新暂时无法加载，请稍后重试。',
        count: n => `${n} 项研究更新`,
    },
    en: {
        title: 'Research updates', kicker: 'RESEARCH JOURNAL',
        intro: 'What changed in the research, and what it means.',
        preview: 'Historical preview · Real updates from November 10 and November 2, with original dates. Automatic daily publishing is not connected yet.',
        date: 'Publication date', all: 'All types', facts: 'Facts & events', stance: 'Stance changes',
        change: 'What changed', meaning: 'Why it matters', next: 'What to watch',
        report: 'Read report', evidence: 'View evidence', evidenceDate: 'Evidence date',
        empty: 'No updates match this date and filter.',
        error: 'Research updates could not be loaded. Please try again later.',
        count: n => `${n} research update${n === 1 ? '' : 's'}`,
    },
};
const esc = value => String(value).replace(/[&<>"']/g, char => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
})[char]);

function isDate(value) {
    return typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value)
        && Number.isFinite(Date.parse(`${value}T00:00:00Z`))
        && new Date(`${value}T00:00:00Z`).toISOString().slice(0, 10) === value;
}

export function validateUpdates(payload, reports, signals) {
    if (payload?.schemaVersion !== 1 || payload.mode !== 'historical-preview' || !Array.isArray(payload.entries)) {
        throw new Error('Invalid daily-updates payload');
    }
    const reportIds = new Set(reports.map(report => report.id));
    const signalMap = new Map(signals.map(signal => [signal.id, signal]));
    const ids = new Set();
    for (const entry of payload.entries) {
        if (!entry.id || ids.has(entry.id)) throw new Error('Duplicate or missing update id');
        ids.add(entry.id);
        if (!isDate(entry.publishedDate) || !isDate(entry.evidenceDate) || entry.evidenceDate > entry.publishedDate) {
            throw new Error(`Invalid dates: ${entry.id}`);
        }
        const signal = signalMap.get(entry.signalId);
        if (!reportIds.has(entry.reportId) || !signal?.reportIds?.includes(entry.reportId)
            || signal.date !== entry.evidenceDate) throw new Error(`Invalid source reference: ${entry.id}`);
        if (!['facts', 'stance'].includes(entry.type)) throw new Error(`Invalid type: ${entry.id}`);
        for (const field of ['company', 'ticker']) {
            if (typeof entry[field] !== 'string' || !entry[field].trim()) throw new Error(`Missing ${field}`);
        }
        for (const field of ['title', 'change', 'meaning', 'next']) {
            for (const lang of ['zh', 'en']) {
                if (typeof entry[field]?.[lang] !== 'string' || !entry[field][lang].trim()) {
                    throw new Error(`Missing ${field}.${lang}`);
                }
            }
        }
    }
    return payload.entries;
}

export function selectUpdates(entries, date, type = 'all') {
    return entries.filter(entry => entry.publishedDate === date && (type === 'all' || entry.type === type));
}

export function renderUpdates(entries, state) {
    const lang = state.lang === 'zh' ? 'zh' : 'en';
    const text = TEXT[lang];
    const dates = [...new Set(entries.map(entry => entry.publishedDate))].sort().reverse();
    const date = dates.includes(state.date) ? state.date : dates[0];
    const selected = selectUpdates(entries, date, state.type);
    const card = entry => {
        // Both destinations are built from validated IDs, never arbitrary URLs.
        const reportUrl = `/invest/research/reports/view.html?id=${encodeURIComponent(entry.reportId)}&lang=${lang}`;
        const evidenceUrl = `/invest/research/monitoring-dashboard.html?lang=${lang}#signal-${encodeURIComponent(entry.signalId)}`;
        return `<article class="journal-card" data-update-id="${esc(entry.id)}">
            <div class="journal-meta"><span>${esc(entry.ticker)}</span><span>${esc(entry.company)}</span><span class="journal-tag">${text[entry.type]}</span></div>
            <h3>${esc(entry.title[lang])}</h3>
            <dl>${['change', 'meaning', 'next'].map(field => `<div><dt>${text[field]}</dt><dd>${esc(entry[field][lang])}</dd></div>`).join('')}</dl>
            <footer><div><a href="${esc(reportUrl)}">${text.report} ↗</a><a href="${esc(evidenceUrl)}">${text.evidence} ↗</a></div><span>${text.evidenceDate} ${esc(entry.evidenceDate)}</span></footer>
        </article>`;
    };
    return `<div class="journal-heading"><div><p class="journal-kicker">${text.kicker}</p><h2 id="daily-updates-title">${text.title}</h2><p>${text.intro}</p></div><span class="journal-count" role="status" aria-live="polite">${text.count(selected.length)}</span></div>
        <p class="journal-preview">${text.preview}</p>
        <div class="journal-controls"><label>${text.date}<select data-journal-date>${dates.map(day => `<option value="${esc(day)}"${day === date ? ' selected' : ''}>${esc(day)}</option>`).join('')}</select></label>
        <div role="group" aria-label="${lang === 'zh' ? '更新类型' : 'Update type'}">${['all', 'facts', 'stance'].map(type => `<button type="button" data-journal-type="${type}" aria-pressed="${state.type === type}">${text[type]}</button>`).join('')}</div></div>
        <div class="journal-cards">${selected.length ? selected.map(card).join('') : `<p role="status">${text.empty}</p>`}</div>`;
}

export async function mountUpdates(root) {
    const language = () => document.documentElement.lang.startsWith('zh') ? 'zh' : 'en';
    const state = { lang: language(), date: '', type: 'all' };
    let entries;
    const draw = () => { root.innerHTML = renderUpdates(entries, state); };
    try {
        const paths = ['daily-updates', 'reports', 'signals'];
        const data = await Promise.all(paths.map(async name => {
            const response = await fetch(`/invest/research/data/${name}.json`, { cache: 'no-store' });
            if (!response.ok) throw new Error(`${name}: HTTP ${response.status}`);
            return response.json();
        }));
        entries = validateUpdates(...data);
        state.date = [...new Set(entries.map(entry => entry.publishedDate))].sort().reverse()[0] || '';
        state.lang = language();
        draw();
    } catch (error) {
        console.error('Daily research updates:', error);
        const showError = () => {
            const text = TEXT[language()];
            root.innerHTML = `<h2 id="daily-updates-title">${esc(text.title)}</h2><p role="status">${esc(text.error)}</p>`;
        };
        showError();
        new MutationObserver(showError).observe(document.documentElement, { attributes: true, attributeFilter: ['lang'] });
        return;
    }
    root.addEventListener('change', event => {
        if (event.target.matches('[data-journal-date]')) {
            state.date = event.target.value;
            draw();
            root.querySelector('[data-journal-date]').focus();
        }
    });
    root.addEventListener('click', event => {
        const button = event.target.closest('[data-journal-type]');
        if (!button) return;
        state.type = button.dataset.journalType;
        draw();
        root.querySelector(`[data-journal-type="${state.type}"]`).focus();
    });
    new MutationObserver(() => {
        const lang = language();
        if (state.lang !== lang) { state.lang = lang; draw(); }
    }).observe(document.documentElement, { attributes: true, attributeFilter: ['lang'] });
}

if (typeof document !== 'undefined') {
    const root = document.getElementById('daily-updates');
    if (root) void mountUpdates(root);
}
