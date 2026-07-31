import test from 'node:test';
import assert from 'node:assert/strict';

globalThis.window = {};
await import('./tracking-rules.js');

const { isRerunCandidate, buildTriggerWatchRows } = window.ResearchTracking;
const today = new Date(Date.UTC(2026, 3, 15));

test('excludes a stale report without a chain layer from review candidates', () => {
    const report = { priceAsOf: '2026-01-01' };
    assert.equal(isRerunCandidate(report, null, today), false);
});

test('excludes a high-drift report without a chain layer from review candidates', () => {
    const report = { priceAsOf: '2026-04-01' };
    const priceEntry = { status: 'ok', changePct: 30 };
    assert.equal(isRerunCandidate(report, priceEntry, today), false);
});

test('includes a stale chain report in review candidates', () => {
    const report = { chainLayer: 'P2', priceAsOf: '2026-01-01' };
    assert.equal(isRerunCandidate(report, null, today), true);
});

// ─── v6 Track 2: trigger watch selection (spec §3.3) ───

function watchReport(overrides = {}) {
    return {
        id: 'fixture-2026',
        chainLayer: 'power',
        stance: 'constructive',
        conviction: 'medium',
        stanceHistory: [{ stance: 'constructive', conviction: 'medium', date: '2026-01-10', price: 10 }],
        stanceTriggers: {
            downgrade: { zh: 'zh', en: 'en', monitoringIds: ['linked-item'] }
        },
        monitoring: [
            { id: 'linked-item', metric: { zh: '指标', en: 'Metric' }, reading: 'breached', readingAsOf: '2026-04-08' }
        ],
        ...overrides
    };
}

test('breached linked item with an unchanged stance produces a row', () => {
    const rows = buildTriggerWatchRows([watchReport()], today);
    assert.equal(rows.length, 1);
    assert.equal(rows[0].reportId, 'fixture-2026');
    assert.equal(rows[0].stance, 'constructive');
    assert.equal(rows[0].items[0].id, 'linked-item');
    assert.equal(rows[0].readingAsOf, '2026-04-08');
    assert.equal(rows[0].daysSinceBreach, 7);
});

test('a stance changed after readingAsOf clears the row', () => {
    const report = watchReport({
        stanceHistory: [
            { stance: 'constructive', conviction: 'medium', date: '2026-01-10', price: 10 },
            { stance: 'cautious', conviction: 'medium', date: '2026-04-09', price: 9 }
        ],
        stance: 'cautious'
    });
    assert.deepEqual(buildTriggerWatchRows([report], today), []);
});

test('a stance dated exactly on readingAsOf still produces a row', () => {
    const report = watchReport({
        stanceHistory: [{ stance: 'constructive', conviction: 'medium', date: '2026-04-08', price: 10 }]
    });
    assert.equal(buildTriggerWatchRows([report], today).length, 1);
});

test('a breached item that no trigger links to is not watched', () => {
    const report = watchReport({
        stanceTriggers: { downgrade: { zh: 'zh', en: 'en', monitoringIds: ['other-item'] } },
        monitoring: [
            { id: 'other-item', metric: { zh: '其它', en: 'Other' } },
            { id: 'linked-item', metric: { zh: '指标', en: 'Metric' }, reading: 'breached', readingAsOf: '2026-04-08' }
        ]
    });
    assert.deepEqual(buildTriggerWatchRows([report], today), []);
});

test('within and ungraded readings never produce a row', () => {
    const within = watchReport({
        monitoring: [{ id: 'linked-item', metric: { en: 'Metric' }, reading: 'within', readingAsOf: '2026-04-08' }]
    });
    const ungraded = watchReport({ monitoring: [{ id: 'linked-item', metric: { en: 'Metric' } }] });
    assert.deepEqual(buildTriggerWatchRows([within, ungraded], today), []);
});

test('non-chain and archived reports are skipped', () => {
    const nonChain = watchReport({ id: 'non-chain', chainLayer: undefined });
    const archived = watchReport({ id: 'archived', isCurrent: false });
    assert.deepEqual(buildTriggerWatchRows([nonChain, archived], today), []);
});

test('rows sort by days since breach, longest standing first', () => {
    const older = watchReport({
        id: 'older-2026',
        monitoring: [{ id: 'linked-item', metric: { en: 'Metric' }, reading: 'breached', readingAsOf: '2026-03-01' }]
    });
    const newer = watchReport({ id: 'newer-2026' });
    assert.deepEqual(
        buildTriggerWatchRows([newer, older], today).map((row) => row.reportId),
        ['older-2026', 'newer-2026']
    );
});

test('the upgrade side also links a watched item', () => {
    const report = watchReport({
        stanceTriggers: {
            upgrade: { zh: 'zh', en: 'en', monitoringIds: ['linked-item'] },
            downgrade: { zh: 'zh', en: 'en', monitoringIds: ['other-item'] }
        },
        monitoring: [
            { id: 'other-item', metric: { en: 'Other' } },
            { id: 'linked-item', metric: { en: 'Metric' }, reading: 'breached', readingAsOf: '2026-04-08' }
        ]
    });
    assert.equal(buildTriggerWatchRows([report], today).length, 1);
});

test('the real book currently has no breached-and-unreviewed report', async () => {
    const { readFileSync } = await import('node:fs');
    const { fileURLToPath } = await import('node:url');
    const path = fileURLToPath(new URL('./data/reports.json', import.meta.url));
    const reports = JSON.parse(readFileSync(path, 'utf-8'));
    assert.deepEqual(buildTriggerWatchRows(reports), []);
});
