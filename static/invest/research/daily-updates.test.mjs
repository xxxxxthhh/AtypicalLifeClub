import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { validateUpdates, selectUpdates, renderUpdates, mountUpdates } from './daily-updates.mjs';
const load = async name => JSON.parse(await readFile(new URL(`./data/${name}.json`, import.meta.url), 'utf8'));
const [payload, reports, signals] = await Promise.all(['daily-updates', 'reports', 'signals'].map(load));
const entries = validateUpdates(payload, reports, signals);

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
    assert.match(html, /尚未接入自动日更/);
    assert.match(html, /2026-11-09/);
    assert.equal((html.match(/<article /g) || []).length, 4);
    assert.doesNotMatch(html, /2026-11-12/);
});
test('English rendering has translated copy and preserves filter selection', () => {
    const html = renderUpdates(entries, {lang: 'en', date: '2026-11-02', type: 'stance'});
    assert.match(html, /A rebuilt valuation moves/);
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
