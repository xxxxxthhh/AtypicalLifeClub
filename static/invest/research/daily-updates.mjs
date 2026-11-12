// Publication records come from approved research reviews, never frontend diffs.
// Historical publication dates and IDs are preserved in both supported modes.
const TEXT = {
    zh: {
        title: '研究更新', kicker: 'RESEARCH JOURNAL',
        intro: '今天的研究，与此前相比改变了什么。',
        preview: '历史内容预览 · 展示已有研究更新，保留原始发布日期。',
        date: '更新日期', all: '全部类型', facts: '事实与事件', stance: '判断调整',
        change: '改了什么', meaning: '如何影响判断', next: '接下来关注',
        report: '阅读报告', evidence: '查看证据记录', evidenceDate: '证据日期',
        live: '已审核发布的研究更新 · 按上海时间（UTC+8）的发布日期查看。',
        unpublished: '这一天尚无已发布的研究更新。',
        empty: '这一天没有符合筛选条件的更新。',
        error: '研究更新暂时无法加载，请稍后重试。',
        count: n => `${n} 项研究更新`,
    },
    en: {
        title: 'Research updates', kicker: 'RESEARCH JOURNAL',
        intro: 'What changed in the research, and what it means.',
        preview: 'Historical preview · Existing research updates with their original publication dates.',
        date: 'Publication date', all: 'All types', facts: 'Facts & events', stance: 'Stance changes',
        change: 'What changed', meaning: 'Why it matters', next: 'What to watch',
        report: 'Read report', evidence: 'View evidence', evidenceDate: 'Evidence date',
        live: 'Reviewed and published research updates · Publication dates use Shanghai time (UTC+8).',
        unpublished: 'No research updates have been published for this day.',
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

const isRecord = value => value !== null && typeof value === 'object' && !Array.isArray(value);
const isId = value => typeof value === 'string' && /^[A-Za-z0-9][A-Za-z0-9_-]*$/.test(value);

export function validateUpdates(payload, reports, signals) {
    if (!isRecord(payload) || payload.schemaVersion !== 1
        || !['historical-preview', 'live'].includes(payload.mode) || !Array.isArray(payload.entries)) {
        throw new Error('Invalid daily-updates payload');
    }
    if (!Array.isArray(reports) || !Array.isArray(signals)
        || reports.some(report => !isRecord(report) || !isId(report.id))
        || signals.some(signal => !isRecord(signal) || !isId(signal.id))) {
        throw new Error('Invalid source catalogs');
    }
    const reportIds = new Set(reports.map(report => report.id));
    const signalMap = new Map(signals.map(signal => [signal.id, signal]));
    if (reportIds.size !== reports.length || signalMap.size !== signals.length) {
        throw new Error('Duplicate source id');
    }
    const ids = new Set();
    for (const entry of payload.entries) {
        if (!isRecord(entry) || !isId(entry.id) || ids.has(entry.id)) {
            throw new Error('Invalid or duplicate update id');
        }
        ids.add(entry.id);
        if (!isId(entry.reportId) || !isId(entry.signalId)) {
            throw new Error(`Invalid source id: ${entry.id}`);
        }
        if (!isDate(entry.publishedDate) || !isDate(entry.evidenceDate) || entry.evidenceDate > entry.publishedDate) {
            throw new Error(`Invalid dates: ${entry.id}`);
        }
        const signal = signalMap.get(entry.signalId);
        if (!reportIds.has(entry.reportId) || !Array.isArray(signal?.reportIds)
            || !signal.reportIds.includes(entry.reportId)
            || signal.date !== entry.evidenceDate) throw new Error(`Invalid source reference: ${entry.id}`);
        if (!['facts', 'stance'].includes(entry.type)) throw new Error(`Invalid type: ${entry.id}`);
        for (const field of ['company', 'ticker']) {
            if (typeof entry[field] !== 'string' || !entry[field].trim()) throw new Error(`Missing ${field}`);
        }
        for (const field of ['title', 'change', 'meaning', 'next']) {
            for (const lang of ['zh', 'en']) {
                if (!isRecord(entry[field]) || typeof entry[field][lang] !== 'string' || !entry[field][lang].trim()) {
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

export function shanghaiDate(now = new Date()) {
    const parts = new Intl.DateTimeFormat('en', {
        timeZone: 'Asia/Shanghai', year: 'numeric', month: '2-digit', day: '2-digit',
    }).formatToParts(now);
    const part = type => parts.find(item => item.type === type).value;
    return `${part('year')}-${part('month')}-${part('day')}`;
}

export function renderUpdates(entries, state) {
    const lang = state.lang === 'zh' ? 'zh' : 'en';
    const text = TEXT[lang];
    const live = state.mode === 'live';
    const today = live ? shanghaiDate(state.now) : '';
    const dates = [...new Set([...entries.map(entry => entry.publishedDate), ...(live ? [today] : [])])].sort().reverse();
    const date = dates.includes(state.date) ? state.date : live ? today : dates[0];
    const selected = selectUpdates(entries, date, state.type);
    const empty = live && !selectUpdates(entries, date).length ? text.unpublished : text.empty;
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
        <p class="journal-preview">${live ? text.live : text.preview}</p>
        <div class="journal-controls"><label>${text.date}<select data-journal-date>${dates.map(day => `<option value="${esc(day)}"${day === date ? ' selected' : ''}>${esc(day)}</option>`).join('')}</select></label>
        <div role="group" aria-label="${lang === 'zh' ? '更新类型' : 'Update type'}">${['all', 'facts', 'stance'].map(type => `<button type="button" data-journal-type="${type}" aria-pressed="${state.type === type}">${text[type]}</button>`).join('')}</div></div>
        <div class="journal-cards">${selected.length ? selected.map(card).join('') : `<p role="status">${empty}</p>`}</div>`;
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
        state.mode = data[0].mode;
        state.date = state.mode === 'live' ? '' : [...new Set(entries.map(entry => entry.publishedDate))].sort().reverse()[0] || '';
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
