# Color and type

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

- The websites use each device's **system font** (the default sans-serif).
- Headings are set **bold or semibold**; small section labels in **capitals
  with wide letter spacing**.
- VATSIM IDs (CIDs) and ratings are set in a **monospaced** font.
- The logo's name is drawn as part of the logo. Don't retype it.

The logo's name is set in **Source Sans 3**: "Indy" in Black, "Center" in
Light. It's free from [Google Fonts](https://fonts.google.com/specimen/Source+Sans+3).
For graphics where you choose the font, use it: Bold or Black for headings,
Regular or Light for text.
