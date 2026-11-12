import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { validateUpdates, selectUpdates, renderUpdates, mountUpdates, shanghaiDate } from './daily-updates.mjs';
const load = async name => JSON.parse(await readFile(new URL(`./data/${name}.json`, import.meta.url), 'utf8'));
const [production, reports, signals] = await Promise.all(['daily-updates', 'reports', 'signals'].map(load));
// Frozen editorial preview fixture: publication growth must not change these UI expectations.
const payload = JSON.parse(await readFile(new URL('./daily-updates.test.fixture.json', import.meta.url), 'utf8'));
const entries = validateUpdates(payload, reports, signals);

test('production payload validates and preserves the five original historical records', () => {
    const published = validateUpdates(production, reports, signals);
    for (const historical of entries) {
        const actual = published.find(entry => entry.id === historical.id);
        assert.ok(actual, `Missing historical publication: ${historical.id}`);
        // Audit metadata may be added; every original core field must remain exact.
        assert.deepEqual(Object.fromEntries(Object.keys(historical).map(key => [key, actual[key]])), historical);
    }
});

test('live payload accepts legacy records and optional audit metadata without generating IDs or dates', () => {
    const copy = structuredClone(payload);
    copy.mode = 'live';
    copy.entries[0].approvedVersion = 'review-2';
    copy.entries[0].sourceFingerprint = 'sha256:example';
    const before = structuredClone(copy);
    assert.equal(validateUpdates(copy, reports, signals), copy.entries);
    assert.deepEqual(copy, before);
    assert.deepEqual(validateUpdates({...copy, entries: []}, reports, signals), []);
});
test('invalid core fields and unsafe IDs fail in both publication modes', () => {
    const mutations = [
        p => { p.entries[0] = null; },
        p => { p.entries[0].id = 12; },
        p => { p.entries[0].id = {}; },
        p => { p.entries[0].id = 'bad/id'; },
        p => { p.entries[0].id = ' bad-id'; },
        p => { p.entries[0].reportId = ['hims-2026']; },
        p => { p.entries[0].signalId = 'bad#anchor'; },
        p => { p.entries[0].publishedDate = '2026-02-30'; },
        p => { p.entries[0].publishedDate = '2026-11-08'; },
        p => { p.entries[0].evidenceDate = 20261109; },
        p => { p.entries[0].type = ['facts']; },
        p => { p.entries[0].company = 123; },
        p => { p.entries[0].ticker = ' '; },
        p => { p.entries[0].title = ['title']; },
        p => { p.entries[0].next.en = 42; },
    ];
    for (const mode of ['historical-preview', 'live']) {
        for (const mutate of mutations) {
            const copy = structuredClone(payload);
            copy.mode = mode;
            mutate(copy);
            assert.throws(() => validateUpdates(copy, reports, signals));
        }
    }
    for (const invalid of [null, [], {...payload, schemaVersion: '1'}, {...payload, mode: 'automatic'}, {...payload, entries: {}}]) {
        assert.throws(() => validateUpdates(invalid, reports, signals));
    }
});
test('invalid or ambiguous source catalogs fail closed', () => {
    for (const [r, s] of [[{}, signals], [reports, null], [[null], signals],
        [[...reports, reports[0]], signals], [reports, [...signals, signals[0]]],
        [reports, [{...signals[0], reportIds: signals[0].reportIds.join(',')}]]]) {
        assert.throws(() => validateUpdates(payload, r, s));
    }
});
test('Shanghai publication day crosses UTC midnight independently of device timezone', () => {
    assert.equal(shanghaiDate(new Date('2026-11-12T15:59:59Z')), '2026-11-12');
    assert.equal(shanghaiDate(new Date('2026-11-12T16:00:00Z')), '2026-11-13');
    assert.equal(shanghaiDate(new Date('2026-12-31T16:00:00Z')), '2027-01-01');
});
test('live defaults to Shanghai today with honest unpublished copy and historical choices', () => {
    for (const lang of ['zh', 'en']) {
        const html = renderUpdates(entries, {lang, mode: 'live', type: 'all', now: new Date('2026-11-12T16:00:00Z')});
        assert.match(html, /value="2026-11-13" selected/);
        assert.match(html, /value="2026-11-10"/);
        assert.match(html, /value="2026-11-02"/);
        assert.match(html, lang === 'zh' ? /尚无已发布/ : /No research updates have been published/);
        assert.match(html, lang === 'zh' ? /已审核发布/ : /Reviewed and published/);
        assert.doesNotMatch(html, /Historical preview|November 10|历史内容预览|尚未接入|<article /);
    }
});
test('live displays only explicitly published current-day records without rewriting history', () => {
    const current = {...structuredClone(entries[0]), id: 'hims-approved-20261113', publishedDate: '2026-11-13'};
    const copy = {...payload, mode: 'live', entries: [...entries, current]};
    const validated = validateUpdates(copy, reports, signals);
    const html = renderUpdates(validated, {lang: 'zh', mode: 'live', type: 'all', now: new Date('2026-11-12T16:00:00Z')});
    assert.equal((html.match(/<article /g) || []).length, 1);
    assert.match(html, /data-update-id="hims-approved-20261113"/);
    assert.match(html, /两条下调条件/);
    assert.doesNotMatch(html, /尚无已发布|历史内容预览/);
    assert.equal(entries[0].publishedDate, '2026-11-10');
});
test('live keeps historical selection and distinguishes an empty type filter', () => {
    const state = {lang: 'en', mode: 'live', date: '2026-11-10', type: 'all', now: new Date('2026-11-12T16:00:00Z')};
    assert.equal((renderUpdates(entries, state).match(/<article /g) || []).length, 4);
    const filtered = renderUpdates(entries, {...state, type: 'stance'});
    assert.match(filtered, /No updates match/);
    assert.doesNotMatch(filtered, /No research updates have been published/);
    assert.match(filtered, /value="2026-11-10" selected/);
});
test('empty live payload still offers today while preview defaults to latest historical day', () => {
    const now = new Date('2026-11-12T16:00:00Z');
    const empty = renderUpdates([], {lang: 'en', mode: 'live', type: 'all', now});
    assert.match(empty, /value="2026-11-13" selected/);
    assert.match(empty, /No research updates have been published/);
    const preview = renderUpdates(entries, {lang: 'en', type: 'all', now});
    assert.match(preview, /value="2026-11-10" selected/);
    assert.doesNotMatch(preview, /2026-11-13/);
});

test('all preview entries reference the actual report and dated signal', () => {
    assert.equal(entries.length, 5);
    assert.equal(selectUpdates(entries, '2026-11-10').length, 4);
    assert.equal(selectUpdates(entries, '2026-11-02', 'stance').length, 1);
});
test('date and type filters stay combined, including empty results', () => {
    assert.equal(selectUpdates(entries, '2026-11-10', 'stance').length, 0);
    assert.equal(selectUpdates(entries, '2026-11-02', 'facts').length, 0);
    assert.equal(selectUpdates(entries, '2026-11-12').length, 0);
});
test('historical dates remain explicit and no current data is inferred', () => {
    const html = renderUpdates(entries, {lang: 'zh', date: '2026-11-10', type: 'all'});
    assert.match(html, /历史内容预览/);
    assert.match(html, /保留原始发布日期/);
    assert.doesNotMatch(html, /尚未接入|自动日更/);
    assert.match(html, /2026-11-09/);
    assert.equal((html.match(/<article /g) || []).length, 4);
    assert.doesNotMatch(html, /2026-11-12/);
});
test('English rendering has translated copy and preserves filter selection', () => {
    const html = renderUpdates(entries, {lang: 'en', date: '2026-11-02', type: 'stance'});
    assert.match(html, /A rebuilt valuation moves/);
    assert.match(html, /Historical preview · Existing research updates with their original publication dates/);
    assert.doesNotMatch(html, /not connected|Automatic daily publishing/);
    assert.match(html, /value="2026-11-02" selected/);
    assert.match(html, /data-journal-type="stance" aria-pressed="true"/);
    assert.match(html, /id=axti-2026&amp;lang=en/);
});
test('rendered evidence anchors resolve to existing signals', () => {
    const html = renderUpdates(entries, {lang: 'en', date: '2026-11-10', type: 'all'});
    for (const entry of selectUpdates(entries, '2026-11-10')) {
        assert.ok(html.includes(`#signal-${entry.signalId}`));
    }
});
test('invalid source dates, duplicate ids and missing translations fail closed', () => {
    for (const mutate of [
        p => { p.entries[0].evidenceDate = '2026-02-30'; },
        p => { p.entries[0].signalId = 'missing'; },
        p => { p.entries[0].reportId = 'axti-2026'; },
        p => { p.entries.push(p.entries[0]); },
        p => { p.entries[0].change.en = ''; },
    ]) {
        const copy = structuredClone(payload);
        mutate(copy);
        assert.throws(() => validateUpdates(copy, reports, signals));
    }
});
test('editorial strings are escaped before rendering HTML', () => {
    const copy = structuredClone(entries);
    copy[0].title.zh = '<img src=x onerror="alert(1)">';
    const html = renderUpdates(copy, {lang: 'zh', date: '2026-11-10', type: 'all'});
    assert.doesNotMatch(html, /<img/);
    assert.match(html, /&lt;img/);
});
test('mount passes live mode through and keeps loading failures distinct from unpublished days', async () => {
    const saved = {document: globalThis.document, fetch: globalThis.fetch, MutationObserver: globalThis.MutationObserver};
    const savedError = console.error;
    const root = {innerHTML: '', addEventListener() {}};
    globalThis.document = {documentElement: {lang: 'en'}};
    globalThis.MutationObserver = class { observe() {} };
    globalThis.fetch = async path => ({ok: true, json: async () => path.includes('daily-updates') ? {...payload, mode: 'live', entries: []} : path.includes('reports') ? reports : signals});
    console.error = () => {};
    try {
        await mountUpdates(root);
        assert.ok(root.innerHTML.includes(`value="${shanghaiDate()}" selected`));
        assert.match(root.innerHTML, /No research updates have been published/);
        assert.doesNotMatch(root.innerHTML, /could not be loaded|Historical preview/);
        globalThis.fetch = async () => ({ok: true, json: async () => ({schemaVersion: 999})});
        await mountUpdates(root);
        assert.match(root.innerHTML, /could not be loaded/);
        assert.doesNotMatch(root.innerHTML, /No research updates have been published/);
    } finally {
        Object.assign(globalThis, saved);
        console.error = savedError;
    }
});

test('mount uses the current language when initialization changes it during fetch', async () => {
    const saved = {document: globalThis.document, fetch: globalThis.fetch, MutationObserver: globalThis.MutationObserver};
    let release;
    const gate = new Promise(resolve => { release = resolve; });
    const root = {innerHTML: '', addEventListener() {}};
    globalThis.document = {documentElement: {lang: 'en'}};
    globalThis.MutationObserver = class { observe() {} };
    globalThis.fetch = async path => {
        await gate;
        return {ok: true, json: async () => path.includes('daily-updates') ? payload : path.includes('reports') ? reports : signals};
    };
    try {
        const mounted = mountUpdates(root);
        document.documentElement.lang = 'zh-CN';
        release();
        await mounted;
        assert.match(root.innerHTML, /两条下调条件/);
        assert.match(root.innerHTML, /id=hims-2026&amp;lang=zh/);
        assert.doesNotMatch(root.innerHTML, /lang=en/);
    } finally { Object.assign(globalThis, saved); }
});
test('load errors preserve the named region and follow the current language', async () => {
    const saved = {document: globalThis.document, fetch: globalThis.fetch, MutationObserver: globalThis.MutationObserver};
    const savedError = console.error;
    const observers = [];
    const root = {innerHTML: ''};
    globalThis.document = {documentElement: {lang: 'en'}};
    globalThis.MutationObserver = class { constructor(fn) {observers.push(fn);} observe() {} };
    globalThis.fetch = async () => ({ok: false, status: 503});
    console.error = () => {};
    try {
        await mountUpdates(root);
        assert.match(root.innerHTML, /id="daily-updates-title">Research updates/);
        assert.match(root.innerHTML, /role="status"/);
        assert.match(root.innerHTML, /could not be loaded/);
        document.documentElement.lang = 'zh-CN';
        observers[0]();
        assert.match(root.innerHTML, /id="daily-updates-title">研究更新/);
        assert.match(root.innerHTML, /暂时无法加载/);
    } finally {
        Object.assign(globalThis, saved);
        console.error = savedError;
    }
});
test('mount handles date selection, type selection and language updates', async () => {
    const saved = {document: globalThis.document, fetch: globalThis.fetch, MutationObserver: globalThis.MutationObserver};
    const listeners = {};
    const observers = [];
    const root = {innerHTML: '', addEventListener: (name, fn) => {listeners[name] = fn;}, querySelector: () => ({focus() {}})};
    globalThis.document = {documentElement: {lang: 'zh-CN'}};
    globalThis.MutationObserver = class { constructor(fn) {observers.push(fn);} observe() {} };
    globalThis.fetch = async path => ({ok: true, json: async () => path.includes('daily-updates') ? payload : path.includes('reports') ? reports : signals});
    try {
        await mountUpdates(root);
        assert.match(root.innerHTML, /两条下调条件/);
        listeners.change({target: {matches: () => true, value: '2026-11-02'}});
        assert.match(root.innerHTML, /从谨慎调整为中性观察/);
        listeners.click({target: {closest: () => ({dataset: {journalType: 'facts'}})}});
        assert.match(root.innerHTML, /这一天没有符合筛选/);
        document.documentElement.lang = 'en';
        observers[0]();
        assert.match(root.innerHTML, /No updates match/);
        assert.match(root.innerHTML, /value="2026-11-02" selected/);
    } finally { Object.assign(globalThis, saved); }
});
