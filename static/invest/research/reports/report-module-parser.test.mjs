import assert from 'node:assert/strict';
import test from 'node:test';

import {
    buildModuleDiff,
    buildReportModules,
    HEADING_COMMENT_V1,
} from './report-module-parser.mjs';


test('keeps legacy keyword mapping when no contract is selected', () => {
    // Given
    const markdown = [
        '# Legacy report',
        '',
        '## Executive Summary',
        'Summary body.',
        '',
        '## Business Overview',
        'Business body.',
        '',
        '### Industry context',
        'Nested body.',
    ].join('\n');

    // When
    const modules = buildReportModules(markdown, 'en');

    // Then
    const assignments = modules.filter((module) => module.hasContent).map((module) => [
            module.id,
            module.sections.map((section) => section.title),
        ]);
    assert.deepEqual(
        JSON.parse(JSON.stringify(assignments)),
        [
            ['overview', ['Executive Summary']],
            ['business', ['Business Overview', 'Industry context']],
        ],
    );
});


test('uses the explicit marker instead of heading keywords when opted in', () => {
    // Given
    const markdown = [
        '# Explicit report',
        '',
        '## Durable economics <!-- report-module:business -->',
        'Business body.',
    ].join('\n');

    // When
    const modules = buildReportModules(markdown, 'en', HEADING_COMMENT_V1);

    // Then
    const business = modules.find((module) => module.id === 'business');
    assert.equal(business.hasContent, true);
    assert.equal(business.sections[0].title, 'Durable economics');
});


test('makes opted-in H3 headings inherit the explicit H2 module', () => {
    // Given
    const markdown = [
        '# Explicit report',
        '',
        '## Durable economics <!-- report-module:business -->',
        'Business body.',
        '',
        '### Valuation vocabulary must not remap this child',
        'Nested body.',
    ].join('\n');

    // When
    const modules = buildReportModules(markdown, 'en', HEADING_COMMENT_V1);

    // Then
    const business = modules.find((module) => module.id === 'business');
    assert.deepEqual(
        business.sections.map((section) => section.title),
        ['Durable economics', 'Valuation vocabulary must not remap this child'],
    );
});


for (const fixture of [
    {
        name: 'missing marker',
        heading: '## Durable economics',
        message: /line 3.*missing/i,
    },
    {
        name: 'duplicate marker',
        heading: '## Durable economics <!-- report-module:business --> <!-- report-module:financial -->',
        message: /line 3.*duplicate/i,
    },
    {
        name: 'malformed marker',
        heading: '## Durable economics <!-- report-module: business -->',
        message: /line 3.*malformed/i,
    },
    {
        name: 'unknown marker',
        heading: '## Durable economics <!-- report-module:operations -->',
        message: /line 3.*unknown/i,
    },
]) {
    test(`rejects ${fixture.name} when opted in`, () => {
        // Given
        const markdown = ['# Explicit report', '', fixture.heading, 'Body.'].join('\n');

        // When / Then
        assert.throws(
            () => buildReportModules(markdown, 'en', HEADING_COMMENT_V1),
            fixture.message,
        );
    });
}


test('uses each report own contract in a mixed explicit-current legacy-previous diff', () => {
    // Given
    const currentMarkdown = [
        '# Current report',
        '',
        '## Durable economics <!-- report-module:business -->',
        'Current business body.',
    ].join('\n');
    const previousMarkdown = [
        '# Previous report',
        '',
        '## Business Overview',
        'Previous business body.',
    ].join('\n');

    // When
    const diff = buildModuleDiff(currentMarkdown, previousMarkdown, {
        lang: 'en',
        currentContract: HEADING_COMMENT_V1,
        previousContract: null,
    });

    // Then
    const business = diff.modules.find((module) => module.id === 'business');
    assert.equal(business.current.hasContent, true);
    assert.equal(business.previous.hasContent, true);
    assert.equal(business.status, 'modified');
});
