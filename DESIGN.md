# Atypical Life Club Design System

## 1. Atmosphere & Identity

A quiet research command center: information-dense, bilingual, and deliberately neutral. The signature is factual layering: cards, chips, rows, and SVG views use the same restrained surfaces so structure and position carry meaning instead of status colors.

## 2. Color

### Palette

| Role | Token | Light | Dark | Usage |
|------|-------|-------|------|-------|
| Surface/page | `--theme` | `rgb(255, 255, 255)` | `rgb(29, 30, 32)` | Page background |
| Surface/card | `--entry` | `rgb(255, 255, 255)` | `rgb(46, 46, 51)` | Cards, panels, SVG background |
| Surface/soft blue | `--surface-2` | `rgba(47, 111, 237, 0.04)` | `rgba(121, 164, 255, 0.12)` | Soft panel gradients and chart bands |
| Surface/soft teal | `--surface-3` | `rgba(15, 157, 140, 0.08)` | `rgba(89, 200, 185, 0.12)` | Secondary soft gradients |
| Text/primary | `--primary` | `rgb(30, 30, 30)` | `rgb(218, 218, 219)` | Headings |
| Text/body | `--content` | `rgb(31, 31, 31)` | `rgb(196, 196, 197)` | Body copy and table values |
| Text/secondary | `--secondary` | `rgb(108, 108, 108)` | `rgb(155, 156, 157)` | Captions, metadata, axes |
| Text/tertiary | `--tertiary` | `rgb(214, 214, 214)` | `rgb(65, 66, 68)` | Muted dividers and dashed empty states |
| Border/default | `--border` | `rgb(238, 238, 238)` | `rgb(51, 51, 51)` | Panels, rows, graph lanes |
| Accent/primary | `--accent` | `#2f6fed` | `#79a4ff` | Links, focus, structural highlights |
| Accent/soft | `--accent-soft` | `rgba(47, 111, 237, 0.12)` | `rgba(121, 164, 255, 0.22)` | Active controls, selected chips |
| Accent/secondary | `--accent-alt` | `#0f9d8c` | `#59c8b9` | Rare secondary structural accent |

### Coverage Map Handoff Tokens

The `coverage-map.html` reference uses a tighter standalone research canvas. Page-scoped coverage tokens may override the shared shell on that route:

| Role | Token | Light | Dark | Usage |
|------|-------|-------|------|-------|
| Coverage/page | `--coverage-bg` | `#f5f6f9` | `#0d0f13` | Coverage map background |
| Coverage/panel | `--coverage-panel` | `#ffffff` | `#161a20` | Header, hero, lanes, cards |
| Coverage/raised panel | `--coverage-panel-2` | `#fbfcfe` | `#1b2027` | Node cards and secondary card bodies |
| Coverage/ink | `--coverage-ink` | `#14171c` | `#eceef1` | Primary titles on the coverage route |
| Coverage/body | `--coverage-ink-2` | `#3b4048` | `#c3c7ce` | Dense card copy on the coverage route |
| Coverage/muted | `--coverage-muted` | `#6b7079` | `#8a8f98` | Metadata, captions, inactive controls |
| Coverage/faint | `--coverage-faint` | `#a7abb3` | `#565b63` | Breadcrumb separators and lane indices |
| Coverage/line | `--coverage-line` | `#e7e9ee` | `#272c34` | Handoff-style dividers and panel borders |
| Coverage/grid | `--coverage-grid` | `rgba(20, 24, 32, 0.045)` | `rgba(255, 255, 255, 0.04)` | 26px hero grid overlay |

### Rules

- Do not encode investment judgment with red, green, amber, or stance-colored visuals.
- Use `--accent` only for links, focus, active controls, and structural callouts.
- New chart or graph marks use existing neutral/accent tokens through `color-mix()`.

## 3. Typography

### Scale

| Level | Size | Weight | Line Height | Tracking | Usage |
|-------|------|--------|-------------|----------|-------|
| Page title | inherited theme scale | 700 | tight | 0 | Hero/page title |
| Section title | `1rem` to `1.1rem` | 650 | 1.35 | 0 | Dashboard and map panels |
| Card title | `0.92rem` to `1rem` | 650 | 1.35 | 0 | Report cards, layer titles |
| Body | `0.84rem` to `0.9rem` | 400 | 1.45-1.6 | 0 | Summaries and table cells |
| Metadata | `0.72rem` to `0.78rem` | 650 | 1.35 | 0 | Chips, labels, axis text |

### Font Stack

- Primary: inherited system sans stack from the site theme.
- Mono: inherited site monospace stack where numbers or code require it.

### Rules

- Data-heavy numbers should use tabular figures when displayed in charts or dense tables.
- Labels and captions stay compact, but visible text must remain at least `0.72rem`.

## 4. Spacing & Layout

### Base Unit

All spacing is based on the existing 4px rhythm.

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | `0.25rem` | Tight inline spacing |
| `--space-2` | `0.5rem` | Chip and cell gaps |
| `--space-3` | `0.75rem` | Compact panel padding |
| `--space-4` | `1rem` | Section-to-body gap |
| `--space-6` | `1.5rem` | Wider panel rhythm |

### Grid

- Content follows the current Hugo shell/container.
- Dashboard panels use CSS grid, not percentage-heavy flex math.
- Mobile breakpoint for dense visuals is `760px`; graph-only views can hide below it when the card/list fallback remains.

### Rules

- Keep cards at 10-12px radius and compact row spacing.
- Dense operational views should be scannable before decorative.

## 5. Components

### Neutral Chip

- **Structure**: inline-flex span with border, rounded pill, compact padding.
- **Variants**: stance, count, theme, role.
- **States**: chips are informational unless used inside a button group.
- **Accessibility**: do not rely on chip color alone; text carries the datum.

### Research Panel

- **Structure**: bordered article with header and body region.
- **Variants**: layer panel, verdict layer, criteria group, graph/timeline module.
- **Spacing**: `--space-3` internal padding, `--space-4` panel gap.
- **Depth**: border plus tonal background only.

### Inline SVG Data View

- **Structure**: one SVG in a named module container with text fallback/loading state.
- **Variants**: freshness strip, next-check timeline, density matrix support.
- **States**: loading/error handled by the parent page; hover/focus through links or clickable SVG groups.
- **Accessibility**: each SVG has a localized heading/description nearby and per-mark `<title>` tooltips.

### Coverage Chain Board

- **Structure**: horizontally scrolling lane board with 180px layer lanes, mono lane index, layer code, node cards, and a compact role legend.
- **Variants**: current report node, planned gap node, dimmed non-matching role node.
- **States**: role filter preserves all lane positions while lowering opacity on non-matching nodes; links keep hover/focus affordance.
- **Accessibility**: board uses real DOM links and list semantics, not a rasterized graph or screenshot.

### Research Command Hero

- **Structure**: bordered hero panel with a mono kicker, title, explanatory copy, and a compact stat grid.
- **Surface**: tonal panel with a faint 26px grid overlay using `--surface-2`, `--surface-3`, and `--border`.
- **Variants**: research index, coverage map, monitoring dashboard, report detail.
- **States**: loading stats use `--` placeholders; no stance colors or market-signal colors in the hero.
- **Accessibility**: stats are plain text, not icons; hero text must remain readable with Chinese and English copy.

### Research Role Filter

- **Structure**: inline button group above chain/map views.
- **Variants**: all, common constraint, risk anchor, architecture check, dashboard.
- **States**: active uses `--accent-soft` and `--accent`; inactive uses bordered neutral chips; focus rings are visible.
- **Behavior**: filtering may dim graph nodes and reduce card lists, but should not imply positive/negative investment judgment.

### Research Reading Path

- **Structure**: three sibling anchor panels that state a reader task, its scope, and the destination: understand the chain, browse companies, or inspect recent changes.
- **Surface**: default border and tonal background only; the arrow and focus treatment use `--accent` without encoding investment judgment.
- **States**: hover and keyboard focus use the existing micro-motion and focus-ring rules; internal list navigation stays on the current language state.
- **Accessibility**: each panel is one descriptive link with a localized task title and supporting sentence; the group has a localized navigation label.

### Research Collection Filter

- **Structure**: an exclusive button group for all, chain book, research library, and review candidates, composed with category, ticker-initial, and search controls.
- **Semantics**: `chain` means a current report with `chainLayer`; reports without `chainLayer`, including benchmark-only ETF research, belong to `library`; `review` is determined by the shared rerun rule.
- **States**: active buttons use `--accent-soft` and `--accent`; every button exposes `aria-pressed`, and the localized visible-result count updates through a polite status region.
- **Accessibility**: controls remain native buttons, keep visible focus, and never reset another active filter when composed.

### Module Reader Shell

- **Structure**: sticky left module navigation, segmented reading-mode controls, one bordered report panel, and module sections.
- **Variants**: module view, full report, previous archive, diff comparison.
- **States**: active module uses accent-soft tonal fill; missing modules remain visible but muted.
- **Accessibility**: module buttons update the URL query and remain keyboard operable.

## 6. Motion & Interaction

| Type | Duration | Easing | Usage |
|------|----------|--------|-------|
| Micro | 160-200ms | ease | Hover and focus transitions |
| Standard | 200-260ms | ease | Card lift, control active state |

### Rules

- Animate only `transform`, `opacity`, `border-color`, and tonal color changes.
- Anchor navigation uses smooth scrolling where supported.
- Every clickable control must have hover and visible focus states.

## 7. Depth & Surface

### Strategy

Mixed, but restrained: borders and tonal shifts are the default; shadows are subtle and only on hover or focus.

| Level | Value | Usage |
|-------|-------|-------|
| Border | `1px solid var(--border)` | Panels, tables, graph lanes |
| Tonal panel | `color-mix(in srgb, var(--entry) 94%, var(--surface-2))` | Secondary panels |
| Hover shadow | `0 10px 26px -20px color-mix(in srgb, var(--accent) 65%, transparent)` | Report card lift |

### Rules

- Do not nest decorative cards inside decorative cards.
- SVG charts should sit in one module panel and avoid extra framed sub-cards.
