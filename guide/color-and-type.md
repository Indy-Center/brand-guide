# Color and type

> **Building an app?** Get these colors, roles and fonts from
> `@indy-center/centerline-tokens`, part of Indy Centerline, our design
> system, instead of copying them. Its rules are on
> [tech.flyindycenter.com/design](https://tech.flyindycenter.com/design/)
> and its components on [centerline.flyindycenter.com](https://centerline.flyindycenter.com).

## Colors

Indy Center comes in two **color schemes**, light and dark, with a
sky-blue accent in both. Every Indy Center app offers both, and picks one
in this order:

1. The member's own choice, if they've made one.
2. Otherwise, their device's light or dark setting.
3. Otherwise, light.

Members who had an account before the light scheme arrived start in dark,
so nothing changes for them until they choose. They're told once that light
exists and where to choose it.

### Light is framed

The **header and footer use the dark colors in both schemes**, and so does
the home page's hero. In light, only the content between them turns light.
The dark frame keeps the two schemes looking like one brand.

### Brand colors

These never change between schemes.

| Name | Hex | Used for |
| --- | --- | --- |
| Night | `#070F13` | The "black" of the black logo and mark; avatar and link-preview backgrounds |
| Sky | `#0369A1` | The accent: main buttons, the current page number, links on light backgrounds |
| White | `#FFFFFF` | The white logo and mark; text on Sky |

> **Buttons have changed.** Main buttons are now `#0369A1`, with
> `#075985` on hover. This page used to give `#0284C7` for buttons and
> `#0369A1` for hover. If you copied those, update both.

### Roles

A role is what a color is for. Its value depends on the scheme.

| Role | Used for | Light | Dark |
| --- | --- | --- | --- |
| `background` | Page background | `#F1F5F9` | `#111827` |
| `card` | Cards and panels | `#FFFFFF` | `#1E293B` |
| `muted` | Raised areas, input fills, table heads | `#E2E8F0` | `#334155` |
| `border` | Lines around cards and tables | `#E2E8F0` | `#334155` |
| `input` | Input borders | `#64748B` | `#64748B` |
| `foreground` | Headings | `#0F172A` | `#FFFFFF` |
| `foreground-soft` | Body text | `#334155` | `#D1D5DB` |
| `muted-foreground` | Captions and fine print | `#475569` | `#9CA3AF` |
| `placeholder` | Placeholder text in inputs | `#475569` | `#D1D5DB` |
| `primary` | Main buttons, the current page number | `#0369A1` | `#0369A1` |
| `primary-hover` | Main buttons on hover | `#075985` | `#075985` |
| `primary-foreground` | Text on main buttons | `#FFFFFF` | `#FFFFFF` |
| `link` | Links | `#0369A1` | `#38BDF8` |
| `ring` | Focus outlines | `#0284C7` | `#0EA5E9` |
| `destructive` | Errors and actions that delete | `#B91C1C` | `#F87171` |
| `success` | Success | `#15803D` | `#4ADE80` |
| `warning` | Warnings | `#A16207` | `#FACC15` |
| `info` | Information and notices | `#0369A1` | `#38BDF8` |

The header, footer and home page hero always use the **Dark** column.

Status badges sit on a 10% tint of their color. In light, the tint is
Tailwind's `-600` step and the text its `-800`; in dark, the tint is `-500`
and the text `-300`.

### Contrast

Text and controls meet **WCAG 2.2 AA**, the web's standard level of
accessibility, in both schemes: at least 4.5:1 for
text, 3:1 for large text and for the edges of controls such as input
borders and focus outlines. The values above pass on `background` and
`card`, with one exception: in light, set `warning` text on a card, not
straight on the page background, where it falls just short (4.49:1).

Colors and contrast are rules: change them only with the brand owner's OK
(the ATM, at [atm@flyindycenter.com](mailto:atm@flyindycenter.com)).

### The logo on each scheme

The logo and mark stay **white or black** whatever the colors around them:
white on the dark header and footer, black on light content. See
[Marks](marks.md).

## Type

The same type rules apply to the apps and to graphics, posts and banners.

### Fonts

| Text | Font | Weight |
| --- | --- | --- |
| Headings, including panel and card titles | Source Sans 3, the logo's font | Semibold or Bold |
| Everything else: body text, buttons, forms, tables | The system font, each device's own sans-serif | Regular; Medium or Semibold for emphasis |
| VATSIM IDs (CIDs) and ratings | The system monospaced font | Regular |

Source Sans 3 is free from [Google Fonts](https://fonts.google.com/specimen/Source+Sans+3).
The system font is San Francisco on Apple devices, Segoe UI on Windows and
Roboto on Android. In a graphic, where there's no device to follow, use
one of those, or Arial or Helvetica.

On graphics and banners, a big title can also be Source Sans 3 Black, the
weight of "Indy" in the logo.

Small section labels are set in **capitals with wide letter spacing**,
Semibold.

Monospaced CIDs and ratings line up in tables, and a 0 never looks like an
O.

### Sizes

The apps use [Tailwind's default sizes](https://tailwindcss.com/docs/font-size),
so a size class means the same in every app.

| Tailwind class | Size | Used for |
| --- | --- | --- |
| `text-xs` | 12px | Fine print, badges |
| `text-sm` | 14px | Captions, table text, labels |
| `text-base` | 16px | Body text |
| `text-lg` to `text-2xl` | 18–24px | Section and panel headings |
| `text-3xl` | 30px | Page titles |
| `text-4xl` to `text-6xl` | 36–60px | Hero and banner titles |

On phones, form fields are at least 16px, or iOS zooms in when they're
tapped.

### For developers

`@indy-center/centerline-tokens` already holds these font stacks and the
self-hosted Source Sans 3. If you're not using the package:

```css
--font-heading: 'Source Sans 3', ui-sans-serif, system-ui, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
--font-sans: ui-sans-serif, system-ui, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;
```

Self-host Source Sans 3 as one WOFF2 file: the variable font's Latin
subset, which holds every weight in about 29 KB. Upright only; no italic
file is needed. Load it with `font-display: swap`, so text shows in the
system font until it arrives. The system font costs nothing to load. Add
`font-variant-numeric: tabular-nums` to `font-mono`.

### The logo's name

The logo's name is drawn as part of the logo. Use the logo file; don't
retype it. See [Marks](marks.md).

### Type is a rule

Fonts and sizes are rules, like colors: change them only with the brand
owner's OK (the ATM, at [atm@flyindycenter.com](mailto:atm@flyindycenter.com)).
