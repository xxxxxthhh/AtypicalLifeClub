import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, mkdir, readFile, writeFile, copyFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { basename, dirname, resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const cli = fileURLToPath(new URL('./validate_daily_updates.mjs', import.meta.url));
const names = ['daily-updates', 'reports', 'signals'];
// Keep CLI failure fixtures independent of the growing production publication log.
const data = await Promise.all(names.map(async name => JSON.parse(await readFile(
    new URL(name === 'daily-updates' ? './daily-updates.test.fixture.json' : `./data/${name}.json`, import.meta.url), 'utf8',
))));
const run = (args = [], options = {}) => spawnSync(process.execPath, [cli, ...args], {encoding: 'utf8', ...options});
async function fixture(t, values = data) {
    const root = await mkdtemp(join(tmpdir(), 'daily-updates-cli-'));
    t.after(async () => {
        // Only remove this test's own freshly allocated temporary directory.
        assert.equal(dirname(resolve(root)), resolve(tmpdir()));
        assert.ok(basename(root).startsWith('daily-updates-cli-'));
        await rm(root, {recursive: true});
    });
    await mkdir(join(root, 'data'));
    await Promise.all(names.map((name, index) => writeFile(join(root, 'data', `${name}.json`), JSON.stringify(values[index]))));
    return root;
}

test('fixed-argv CLI validates production publications from an unrelated working directory', () => {
    const result = run([], {cwd: tmpdir()});
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /^Daily updates valid: \d+ entries \((historical-preview|live), schema v1\)\.\n$/);
    assert.equal(result.stderr, '');
});
test('CLI validates live fixtures with optional audit metadata without changing files', async t => {
    const values = structuredClone(data);
    values[0].mode = 'live';
    values[0].entries[0].approvedVersion = 'review-2';
    values[0].entries[0].sourceFingerprint = 'sha256:example';
    const root = await fixture(t, values);
    const before = await Promise.all(names.map(name => readFile(join(root, 'data', `${name}.json`), 'utf8')));
    const result = run(['--root', root]);
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /5 entries \(live, schema v1\)/);
    const after = await Promise.all(names.map(name => readFile(join(root, 'data', `${name}.json`), 'utf8')));
    assert.deepEqual(after, before);
});
test('live six-record publication runs journal suites and fixed-argv CLI in an isolated tree',
    {skip: process.env.DAILY_UPDATES_LIVE_SUITE_CHILD === '1'}, async t => {
    const values = structuredClone(data);
    values[0].mode = 'live';
    // Synthetic approved-publication fixture only; never written into production data.
    values[0].entries.push({
        ...structuredClone(values[0].entries[0]),
        id: 'fixture-approved-hims-20261113-v2', publishedDate: '2026-11-13',
        approvedVersion: 'fixture-review-v2', sourceFingerprint: 'sha256:fixture-only',
        title: {zh: '测试夹具：已批准发布', en: 'Test fixture: approved publication'},
    });
    const root = await fixture(t, values);
    for (const name of ['daily-updates.mjs', 'daily-updates.test.mjs', 'daily-updates.test.fixture.json',
        'validate_daily_updates.mjs', 'validate_daily_updates.test.mjs']) {
        await copyFile(new URL(`./${name}`, import.meta.url), join(root, name));
    }
    // Skip only this orchestration case in the child to prevent recursive copies.
    const childEnv = {...process.env, DAILY_UPDATES_LIVE_SUITE_CHILD: '1'};
    delete childEnv.NODE_TEST_CONTEXT;
    const suite = spawnSync(process.execPath, ['--test', '--test-reporter=tap',
        join(root, 'daily-updates.test.mjs'), join(root, 'validate_daily_updates.test.mjs')],
    {encoding: 'utf8', cwd: root, env: childEnv, timeout: 10000});
    assert.equal(suite.status, 0, suite.stdout + suite.stderr);
    assert.match(suite.stdout, /# fail 0/);
    assert.match(suite.stdout, /ok \d+ - production payload validates and preserves the five original historical records/);
    assert.match(suite.stdout, /ok \d+ - fixed-argv CLI validates production publications/);
    const result = spawnSync(process.execPath, [join(root, 'validate_daily_updates.mjs')], {encoding: 'utf8', cwd: tmpdir()});
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /Daily updates valid: 6 entries \(live, schema v1\)/);
    const after = JSON.parse(await readFile(join(root, 'data', 'daily-updates.json'), 'utf8'));
    assert.deepEqual(after, values[0]);
});

test('CLI accepts an empty live publication day', async t => {
    const values = structuredClone(data);
    values[0] = {schemaVersion: 1, mode: 'live', entries: []};
    const result = run(['--root', await fixture(t, values)]);
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /0 entries \(live, schema v1\)/);
});
test('CLI rejects invalid IDs, dates, types and source references', async t => {
    for (const mutate of [
        p => { p.entries[0].id = 123; },
        p => { p.entries[0].id = 'unsafe/id'; },
        p => { p.entries[0].publishedDate = '2026-02-30'; },
        p => { p.entries[0].type = 'automatic'; },
        p => { p.entries[0].signalId = 'missing'; },
    ]) {
        const values = structuredClone(data);
        values[0].mode = 'live';
        mutate(values[0]);
        const result = run(['--root', await fixture(t, values)]);
        assert.equal(result.status, 1);
        assert.match(result.stderr, /Daily updates invalid:/);
        assert.equal(result.stdout, '');
    }
});
test('CLI reports malformed JSON and missing files as failures', async t => {
    const root = await fixture(t);
    await writeFile(join(root, 'data', 'daily-updates.json'), '{invalid');
    const malformed = run(['--root', root]);
    assert.equal(malformed.status, 1);
    assert.match(malformed.stderr, /Daily updates invalid:/);
    const missing = run(['--root', join(root, 'missing')]);
    assert.equal(missing.status, 1);
    assert.match(missing.stderr, /Daily updates invalid:.*ENOENT/);
});
test('CLI rejects unknown or incomplete arguments', () => {
    for (const args of [['--root'], ['--root', '--other'], ['--unknown'], ['--root', '.', 'extra']]) {
        const result = run(args);
        assert.equal(result.status, 1);
        assert.match(result.stderr, /Usage: node validate_daily_updates.mjs/);
    }
});
