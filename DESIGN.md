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
- **Variants**: freshness strip, next-check timeline, chain graph, density matrix support.
- **States**: loading/error handled by the parent page; hover/focus through links or clickable SVG groups.
- **Accessibility**: each SVG has a localized heading/description nearby and per-mark `<title>` tooltips.

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
