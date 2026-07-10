import test from 'node:test';
import assert from 'node:assert/strict';

globalThis.window = {};
await import('./tracking-rules.js');

const { isRerunCandidate } = window.ResearchTracking;
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
