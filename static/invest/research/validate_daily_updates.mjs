#!/usr/bin/env node
// Read-only validation. --root is a research directory containing data/.
import { readFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateUpdates } from './daily-updates.mjs';

try {
    const args = process.argv.slice(2);
    if (args.length && (args.length !== 2 || args[0] !== '--root' || !args[1] || args[1].startsWith('--'))) {
        throw new Error('Usage: node validate_daily_updates.mjs [--root <research-directory>]');
    }
    const root = args.length ? resolve(args[1]) : dirname(fileURLToPath(import.meta.url));
    const [payload, reports, signals] = await Promise.all(
        ['daily-updates', 'reports', 'signals'].map(async name => {
            const path = resolve(root, 'data', `${name}.json`);
            return JSON.parse(await readFile(path, 'utf8'));
        }),
    );
    const entries = validateUpdates(payload, reports, signals);
    console.log(`Daily updates valid: ${entries.length} entries (${payload.mode}, schema v${payload.schemaVersion}).`);
} catch (error) {
    console.error(`Daily updates invalid: ${error.message}`);
    process.exitCode = 1;
}
