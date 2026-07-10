export const HEADING_COMMENT_V1 = 'heading-comment-v1';

export const REPORT_MODULES = [
    {
        id: 'overview', labels: { zh: '摘要与当前判断', en: 'Summary & Current View' },
        keywords: {
            zh: ['执行摘要', '摘要', '更新', '重跑', '最新事实', '事实基础', '当前判断'],
            en: ['executive summary', 'summary', 'update', 'rerun', 'fact base', 'current view'],
        },
    },
    {
        id: 'business', labels: { zh: '业务概览', en: 'Business Overview' },
        keywords: {
            zh: ['业务概览', '业务画像', '商业模式', '分部', '做什么', '产品', '平台供应商'],
            en: ['business overview', 'business model', 'segment', 'what', 'product', 'platform supplier'],
        },
    },
    {
        id: 'competition', labels: { zh: '行业与竞争位置', en: 'Industry & Competition' },
        keywords: {
            zh: ['行业', '竞争', '护城河', '市场份额', '生态', '供应链', 'tam', '对手'],
            en: ['industry', 'competition', 'competitive', 'competitor', 'moat', 'market share', 'ecosystem', 'supply chain', 'tam'],
        },
    },
    {
        id: 'financial', labels: { zh: '财务健康度', en: 'Financial Health' },
        keywords: {
            zh: ['财务', '现金流', '资产负债', '营收', '利润', '毛利率', '红旗', '结果'],
            en: ['financial', 'cash flow', 'balance sheet', 'revenue', 'earnings', 'margin', 'red flag', 'results'],
        },
    },
    {
        id: 'management', labels: { zh: '管理层评估', en: 'Management Assessment' },
        keywords: {
            zh: ['管理层', '治理', '高管', '领导', 'ceo', '执行质量'],
            en: ['management', 'governance', 'executive', 'ceo', 'execution quality'],
        },
    },
    {
        id: 'bullBear', labels: { zh: '牛熊论点', en: 'Bull & Bear Cases' },
        keywords: {
            zh: ['牛市', '熊市', '乐观', '悲观', '上行', '下行', '看涨', '看空'],
            en: ['bull', 'bear', 'upside', 'downside', 'positive case', 'negative case', 'steel-manned'],
        },
    },
    {
        id: 'uncertainties', labels: { zh: '关键不确定性', en: 'Key Uncertainties' },
        keywords: {
            zh: ['不确定性', '论点失效', '失效条件', '风险边界'],
            en: ['uncertainty', 'uncertainties', 'thesis-breaking', 'failure condition', 'risk boundary'],
        },
    },
    {
        id: 'valuation', labels: { zh: '估值分析', en: 'Valuation' },
        keywords: {
            zh: ['估值', '倍数', '目标价', '公允价值', '定价'],
            en: ['valuation', 'multiple', 'target price', 'fair value', 'pricing'],
        },
    },
    {
        id: 'catalysts', labels: { zh: '催化剂与监控', en: 'Catalysts & Monitoring' },
        keywords: {
            zh: ['催化', '监测', '监控', '时间线', '指标', '清单'],
            en: ['catalyst', 'monitoring', 'watchlist', 'timeline', 'checklist'],
        },
    },
    {
        id: 'conclusion', labels: { zh: '结论与复盘', en: 'Conclusion & Review' },
        keywords: {
            zh: ['结论', '建议', '复盘', '综合'],
            en: ['conclusion', 'recommendation', 'review', 'synthesis'],
        },
    },
    {
        id: 'appendix', labels: { zh: '附录与来源', en: 'Appendix & Sources' },
        keywords: {
            zh: ['附录', '资料来源', '数据来源', '来源', '假设', '术语'],
            en: ['appendix', 'sources', 'data source', 'assumption', 'glossary'],
        },
    },
];

const MODULE_IDS = new Set(REPORT_MODULES.map((module) => module.id));
const EXPLICIT_HEADING_RE = /^(##\s+)(.+?)\s+<!-- report-module:([A-Za-z][A-Za-z0-9-]*) -->\s*$/;

export class ReportModuleContractError extends Error {
    constructor(reason, lineNumber) {
        super(`line ${lineNumber}: ${reason}`);
        this.name = 'ReportModuleContractError';
        this.lineNumber = lineNumber;
    }
}

function stripMarkdownCover(markdown) {
    const normalized = String(markdown || '').replace(/^\uFEFF?/, '').replace(/\r\n/g, '\n');
    const titleMatch = normalized.match(/^#\s+.*(?:\n+|$)/);
    const withoutTitle = titleMatch ? normalized.slice(titleMatch[0].length) : normalized;
    let lineOffset = titleMatch ? (titleMatch[0].match(/\n/g) || []).length : 0;
    const coverMatch = withoutTitle.match(/^([\s\S]*?)\n---\s*\n+/);
    if (!coverMatch) return { body: withoutTitle, lineOffset };

    const coverLines = coverMatch[1].split('\n').map((line) => line.trim()).filter(Boolean);
    const coverKeys = [
        '标的收录日期', '最近更新日期', '代码', '免责声明',
        'Coverage date', 'Last updated', 'Ticker', 'Disclaimer',
    ];
    const isCoverMetadata = coverLines.length > 0
        && coverLines.length <= 8
        && coverLines.every((line) => coverKeys.some((key) => (
            line.startsWith(`${key}：`) || line.startsWith(`${key}:`)
        )));
    if (!isCoverMetadata) return { body: withoutTitle, lineOffset };
    lineOffset += (coverMatch[0].match(/\n/g) || []).length;
    return { body: withoutTitle.slice(coverMatch[0].length), lineOffset };
}

function resolveModuleKey(title, lang) {
    const text = String(title || '').toLowerCase();
    for (const moduleDef of REPORT_MODULES) {
        const keywords = moduleDef.keywords[lang] || moduleDef.keywords.en || [];
        if (keywords.some((keyword) => text.includes(String(keyword).toLowerCase()))) {
            return moduleDef.id;
        }
    }
    return null;
}

function parseExplicitH2(line, lineNumber) {
    const markerCount = line.split('report-module').length - 1;
    if (markerCount === 0) {
        throw new ReportModuleContractError('missing report-module marker', lineNumber);
    }
    if (markerCount > 1) {
        throw new ReportModuleContractError('duplicate report-module markers', lineNumber);
    }
    const markerMatch = line.match(EXPLICIT_HEADING_RE);
    if (!markerMatch) {
        throw new ReportModuleContractError(
            'malformed report-module marker; expected <!-- report-module:<id> --> at the end of the H2',
            lineNumber,
        );
    }
    const moduleKey = markerMatch[3];
    if (!MODULE_IDS.has(moduleKey)) {
        throw new ReportModuleContractError(`unknown report module id "${moduleKey}"`, lineNumber);
    }
    return { title: markerMatch[2].trim(), moduleKey };
}

function splitMarkdownSections(markdown, lang, moduleContract) {
    if (moduleContract !== null && moduleContract !== undefined && moduleContract !== HEADING_COMMENT_V1) {
        throw new Error(`Unsupported report module contract: ${moduleContract}`);
    }
    const explicit = moduleContract === HEADING_COMMENT_V1;
    const stripped = stripMarkdownCover(markdown);
    const lines = stripped.body.split('\n');
    const sections = [];
    let currentSection = null;
    let parentModuleKey = 'overview';
    const introBuffer = [];
    const bodyBuffer = [];
    let sectionIndex = 0;

    const commitIntro = () => {
        const content = introBuffer.join('\n').trim();
        if (content) {
            sections.push({
                id: `intro-${sectionIndex}`, title: lang === 'en' ? 'Introduction' : '基础信息',
                level: 0, moduleKey: 'overview', content, isIntro: true,
            });
            sectionIndex += 1;
        }
        introBuffer.length = 0;
    };
    const commitCurrent = () => {
        if (!currentSection) return;
        const content = bodyBuffer.join('\n').trim();
        if (content) sections.push({ ...currentSection, content });
        currentSection = null;
        bodyBuffer.length = 0;
    };

    lines.forEach((line, index) => {
        const headingMatch = line.match(/^(#{2,3})\s+(.*)$/);
        if (!headingMatch) {
            if (explicit && line.includes('report-module')) {
                throw new ReportModuleContractError(
                    'malformed report-module marker; markers belong on H2 headings',
                    stripped.lineOffset + index + 1,
                );
            }
            if (currentSection) bodyBuffer.push(line);
            else if (line.trim()) introBuffer.push(line);
            return;
        }

        const isH2 = headingMatch[1] === '##';
        if (explicit && !isH2 && line.includes('report-module')) {
            throw new ReportModuleContractError(
                'malformed report-module marker; markers belong on H2 headings',
                stripped.lineOffset + index + 1,
            );
        }
        commitCurrent();
        commitIntro();

        const explicitHeading = explicit && isH2
            ? parseExplicitH2(line, stripped.lineOffset + index + 1)
            : null;
        const title = explicitHeading ? explicitHeading.title : headingMatch[2].trim();
        const ownModuleKey = explicitHeading ? explicitHeading.moduleKey : resolveModuleKey(title, lang);
        if (isH2) parentModuleKey = ownModuleKey || 'overview';
        const moduleKey = isH2
            ? (ownModuleKey || 'overview')
            : (explicit ? parentModuleKey : (
                parentModuleKey && parentModuleKey !== 'overview'
                    ? parentModuleKey
                    : (ownModuleKey || parentModuleKey || 'overview')
            ));
        currentSection = {
            id: `section-${sectionIndex}`, title, moduleKey, level: isH2 ? 2 : 3, content: '',
        };
        sectionIndex += 1;
    });

    commitCurrent();
    commitIntro();
    return sections;
}

export function buildReportModules(markdown, lang, moduleContract = null) {
    const moduleMap = new Map(REPORT_MODULES.map((moduleDef, index) => [
        moduleDef.id,
        { ...moduleDef, number: String(index + 1).padStart(2, '0'), sections: [], hasContent: false },
    ]));
    splitMarkdownSections(markdown, lang, moduleContract).forEach((section) => {
        moduleMap.get(MODULE_IDS.has(section.moduleKey) ? section.moduleKey : 'overview').sections.push(section);
    });
    return REPORT_MODULES.map((moduleDef) => {
        const module = moduleMap.get(moduleDef.id);
        module.hasContent = module.sections.some((section) => Boolean(section.content && section.content.trim()));
        return module;
    });
}

function normalizeModuleContent(module) {
    if (!module || !module.hasContent) return '';
    return module.sections
        .map((section) => `${section.title}\n${section.content}`)
        .join('\n\n').replace(/\r/g, '').replace(/\s+/g, ' ').trim().toLowerCase();
}

export function buildModuleDiff(currentMarkdown, previousMarkdown, options = {}) {
    const lang = options.lang || 'en';
    const currentModules = buildReportModules(currentMarkdown, lang, options.currentContract);
    const previousModules = buildReportModules(previousMarkdown, lang, options.previousContract);
    const previousMap = new Map(previousModules.map((module) => [module.id, module]));
    const counts = { added: 0, modified: 0, removed: 0, unchanged: 0 };
    const modules = currentModules.map((currentModule) => {
        const previousModule = previousMap.get(currentModule.id);
        let status = 'empty';
        if (currentModule.hasContent && (!previousModule || !previousModule.hasContent)) status = 'added';
        else if (!currentModule.hasContent && previousModule && previousModule.hasContent) status = 'removed';
        else if (currentModule.hasContent && previousModule && previousModule.hasContent) {
            status = normalizeModuleContent(currentModule) === normalizeModuleContent(previousModule)
                ? 'unchanged' : 'modified';
        }
        if (status !== 'empty') counts[status] += 1;
        return {
            ...currentModule, current: currentModule, previous: previousModule, status,
            hasContent: currentModule.hasContent || Boolean(previousModule && previousModule.hasContent),
        };
    });
    return { modules, counts };
}
