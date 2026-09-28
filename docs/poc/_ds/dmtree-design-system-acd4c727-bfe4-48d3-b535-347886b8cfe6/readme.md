# DMTree Design System

**Brand:** DMTree Wellness and Healing Arts (full name: Divine Medicine Tree Wellness and Healing Arts)  
**Website:** [dmtree.live](https://dmtree.live)  
**Location:** 1919 Grass Valley Hwy #190, Auburn, CA 95603  
**Phone:** 1(916)-913-6873

---

## About the Brand

DMTree Wellness and Healing Arts is a holistic wellness center offering a wide spectrum of healing modalities — from massage and bodywork to sound therapy, breathwork, astrology, lunar ceremonies, and an apothecary. The brand is rooted in the belief that the body holds its own divine medicine, with the guiding philosophy: **"Activate the divine medicine within you."**

The center's full name — **Divine Medicine Tree** — is encoded in the logo initialism DMT + REE. The brand occupies the intersection of ancient wisdom traditions, somatic healing, and community ritual.

**Services offered:**
Massage · Vibration & Sound Therapy · BodyWork · Breathwork · Stress Reduction · Movement · Courses & Workshops · Meditation · Apothecary · Lunar Ceremony · Astrology · Ayurveda · Aura Reading · Free Spirit Bar & Lounge · Sensory Deprivation Chamber · Autism Support · Brain Tap Therapy · Ionic Foot Bath

---

## Sources

- **Website:** https://dmtree.live (GoDaddy Website Builder, live)
- **Uploaded logos:** `uploads/tree_logo.svg`, `uploads/gold_text_logo.svg` (copied to `assets/`)
- **Brand colors specified by owner:** Gold `#D9B13B`, Dark Green `#0f260f`

No Figma file or codebase repo was provided.

---

## Content Fundamentals

### Tone & Voice
- **Reverent but accessible.** Copy reads like a wise guide speaking warmly to a curious seeker — not clinical, not overly casual.
- **Invitational, never pushy.** Calls to action invite rather than demand: "Book Now," "See Events," "Come Visit."
- **Poetic & evocative.** Service descriptions use metaphor and feeling: "Let go into Deep Relaxation," "Healing Through Ancient Wisdom," "Unlock Hidden Abilities."
- **Short, resonant phrases.** Headlines are often 3–6 words. No padding, no jargon.
- **First person ("we") for the center; second person ("you") for the client.** "We listen to our clients… Our goal is to provide our clients with tools to live a beautiful, pain free, and emotionally balanced life."

### Casing
- **Section headings:** Title Case for navigation; Sentence case or all-caps for hero statements.
- **Service names:** lowercase with occasional all-caps for emphasis (e.g. "AURA READER," "FREE SPIRIT BAR AND LOUNGE").
- **Taglines:** Sentence case, evocative — "Open the Possibilities."

### Emoji & Symbols
- **No emoji** in core brand copy. The brand relies on visual metaphor and imagery rather than emoji.
- **Decorative dividers** (thin gold lines) are used in the logo — this motif can extend to section separators.

### Copy Examples
- Hero: *"Open the Possibilities"*
- Sub-hero: *"Activate the divine medicine within you"*
- Welcome: *"Thank you for being here"*
- Service: *"Let go into Deep Relaxation"*, *"Healing Through Ancient Wisdom"*, *"Clear Stress and Emotional Blocks"*
- Tagline: *"Wellness and Healing Arts"*
- About: *"We listen to our clients, their body and their energy. We take our time, give our full attention, a full heart and understanding of the science behind our practice."*

---

## Visual Foundations

### Color System
- **Dark Forest Green `#0f260f`** — primary background for hero sections, navigation, overlays. Conveys earth, depth, rootedness.
- **Gold `#D9B13B`** — primary accent, display text on dark backgrounds, CTA fills, logo color. Conveys warmth, sacredness, vitality.
- **Cream `#f8f4e8`** — light section backgrounds, warm off-white. Feels like parchment, natural.
- **Parchment `#f2ecda`** — slightly deeper cream for alternating sections.
- Neutrals range from warm ink `#1a1610` through bark, taupe, stone to cream.

### Typography
- **Primary font: EB Garamond** (Google Fonts) — substituting for Times New Roman used in the SVG logo. Classical serif with organic letterforms; carries sacred, timeless energy.
- **Secondary font: Lato** — clean, humanist sans-serif for labels, navigation, small UI text.
- Display headings are large, airy, letter-spaced. Body copy is generous in line-height.
- *Note: The original logo uses Times New Roman. If pixel-perfect logo reproduction is needed, license or embed the original font file.*

### Backgrounds
- **Hero/Header:** Full-bleed dark green `#0f260f`, often with the tree logo or healing imagery.
- **Content sections:** Alternating cream `#f8f4e8` and parchment `#f2ecda`.
- **Cards:** White or warm white, with a subtle gold border or none.
- No aggressive gradients — if used, a very gentle cream-to-white or dark-green-to-black fade.
- Nature photography (hands, forest, light through trees) is used as full-bleed imagery.

### Spacing & Layout
- Generous vertical rhythm — sections breathe with `6rem` (96px) top/bottom padding.
- Content width capped at `1200px`, centered.
- Service grids typically 3-column on desktop, 1-2 on mobile.
- Cards are modestly padded (`2rem`) with enough whitespace to feel uncluttered.

### Cards
- White or cream background.
- 4–8px corner radius (subtle, not pill-shaped).
- No harsh drop shadow — use `0 4px 16px rgba(15,38,15,0.12)` (warm green-tinted shadow).
- Optional thin gold border `rgba(217,177,59,0.35)` for elevated cards.
- Service cards often have an image zone on top and a title + tagline below.

### Buttons
- **Primary:** Gold fill `#D9B13B`, dark green text `#0f260f`, 4px radius. On hover: slightly brighter gold, subtle gold glow shadow.
- **Secondary/Outline:** Transparent fill, gold border, gold text. On hover: gold fill.
- **Ghost:** No border, gold text. On hover: gold underline or slight background tint.

### Borders & Dividers
- Thin double-line dividers in gold (from the logo motif) — `1px` lines spaced `4px` apart.
- Section separators are decorative and minimal.
- Card borders use `rgba(217,177,59,0.35)`.

### Shadows & Elevation
- All shadows are warm green-tinted (not cool gray).
- Gold glow shadows `rgba(217,177,59,0.30)` for CTAs and highlighted elements.
- Elevation is subtle — this brand doesn't use heavy drop shadows.

### Animations & Motion
- **Slow, gentle fades** — `450ms ease` for appears, overlays.
- **No bouncy animations.** The brand is grounding, not playful.
- Hover states: opacity fade (0.85) or color shift over `280ms ease`.
- Press states: very slight scale-down `scale(0.97)` over `150ms`.

### Hover & Interaction States
- Links/buttons on dark bg: gold text brightens to `#e8cc72`.
- Cards: lift shadow slightly + very subtle upward translate `translateY(-2px)`.
- Navigation items: gold underline animate from center out.

### Imagery
- **Color palette of imagery:** warm, earthy — golden hour light, forest greens, skin tones, candle glow.
- **Grain/texture:** slight warmth and softness, not overly polished.
- **NOT:** cool-toned, blue-filtered, stark high-contrast.

### Corner Radii
- Buttons: `4px`
- Cards: `8px`
- Badges/tags: `9999px` (pill)
- Modals/drawers: `12px`
- Inputs: `4px`

### Iconography
See the Iconography section below.

---

## Asset Shortcut Reference

Semantic names for every SVG in `assets/` — reference these tags directly in design requests instead of describing the file each time.

**Lookup table — description → shortcut:**

| If you say... | Use shortcut | File |
|---|---|---|
| "the tree logo" / "tree emblem" / "circular seal" | `@tree-logo` | `assets/tree_logo.svg` |
| "the DMTree logo" / "gold wordmark" / "horizontal logo" | `@dmtree-logo` | `assets/gold_text_logo.svg` |
| "the Divine Medicine Tree logo" / "full name lockup" / "formal title" | `@divine-medicine-logo` | `assets/divine-medicine-lockup.svg` |
| "the crow" / "bird silhouette" | `@crow` | `assets/crow.svg` |
| "corner ornament" / "corner flourish" / "filigree corner" | `@corner-ornament` | `assets/filigree-corner.svg` |
| "flower of life" / "flower pattern" / "sacred geometry bloom" | `@flower-of-life` | `assets/flower-of-life.svg` |
| "metatron" / "metatron's cube" / "sacred lattice" | `@metatron` | `assets/metatron.svg` |

**Full details:**

| Shortcut | File | What it is | Typical use |
|---|---|---|---|
| `@tree-logo` | `assets/tree_logo.svg` | Circular emblem: dark-green disc, gold tree of life illustration, crescent moon phases arcing overhead, "Divine Medicine Tree Wellness & Healing Arts" wordmark + tagline set inside the circle | Primary logo mark — favicons, seals, title-page medallions, stamps |
| `@dmtree-logo` | `assets/gold_text_logo.svg` | Horizontal gold serif wordmark "DMTree Wellness and Healing Arts" with tagline "Activate the divine medicine within you," underline rule beneath "DMTree" | Headers, letterheads, flat lockups where a circular emblem won't fit |
| `@divine-medicine-logo` | `assets/divine-medicine-lockup.svg` | Stacked gold serif text lockup: full name "Divine Medicine Tree" / "Wellness and Healing Arts" / tagline "Activate the divine medicine within you," double gold rule beneath the first line | Title pages, formal letterheads, or anywhere the full unabbreviated business name is called for |
| `@crow` | `assets/crow.svg` | Solid black crow/bird silhouette (traced illustration) | Accent motif for pages, dividers, or symbolic flourishes — flat black, recolor via CSS `fill` if placed inline as `<svg>` |
| `@corner-ornament` | `assets/filigree-corner.svg` | Single gold scrollwork corner flourish (flourish + dot, hand-drawn line quality) | Page/card corners — rotate/flip via CSS transform to cover all 4 corners of a frame |
| `@flower-of-life` | `assets/flower-of-life.svg` | Flower-of-Life sacred geometry — overlapping circles in a hexagonal bloom, thin gold line art | Full-bleed faint background wash (~8–15% opacity) behind hero sections or report covers |
| `@metatron` | `assets/metatron.svg` | Tree-of-Life / seed-pattern lattice — 10 small circles connected in a hexagonal/triangular grid, thin gold line art | Secondary background wash (pair with or alternate against `@flower-of-life`); works well small/tiled too |

Reference these by shortcut name in design requests, e.g. "put `@flower-of-life` behind the hero at 10% opacity" or "use `@corner-ornament` on all four corners of the card." A visual specimen card lives in the Design System tab under Brand → "Asset Reference."

## Iconography

The brand does not use a standard icon library. The primary iconographic element is the **tree logo** — a detailed botanical illustration in gold on dark green, rendered as SVG.

- **Primary icon asset:** `assets/tree_logo.svg` — the circular tree emblem.
- **Text logo:** `assets/gold_text_logo.svg` — "DMTREE / Wellness and Healing Arts" in gold serif.
- **No icon font** is used on the website (GoDaddy builder may include its own).
- **Recommended icon set for UI:** [Phosphor Icons](https://phosphoricons.com/) (CDN available) — Regular weight, nature-friendly glyph set with icons for wellness, nature, body, and spirit.
- **Usage:** Icons are decorative/supportive, not navigational. They appear at `24px` in UI context, `32–48px` in service cards.
- **Style:** Line icons, 1.5px stroke weight, rounded caps, gold `#D9B13B` on dark surfaces, dark green `#0f260f` on light surfaces.

---

## File Index

```
styles.css                  ← Design system entry point (link this)
tokens/
  colors.css                ← Color custom properties
  typography.css            ← Font imports + type scale
  spacing.css               ← Space/radius scale
  shadows.css               ← Shadows, transitions, z-index
assets/
  tree_logo.svg             ← Primary circular tree emblem
  gold_text_logo.svg        ← Gold wordmark
guidelines/                 ← Foundation specimen cards (@dsCard)
components/core/            ← Reusable React UI components
ui_kits/website/            ← DMTree website hi-fi recreation
readme.md                   ← This file
SKILL.md                    ← Agent skill definition
```

### Components
- **Button** — Primary, secondary, ghost variants; sm/md/lg sizes.
- **ServiceCard** — Image + title + tagline tile for the service grid.
- **Badge** — Small status/category pill.
- **GoldDivider** — Branded double-line gold divider.
- **SectionHeading** — Styled h2/h3 with optional gold underline accent.

### UI Kits
- **website/** — DMTree homepage recreation: hero, navigation, services grid, contact section.

---

## Caveats

- The original logo font is **Times New Roman** (not web-licensed). **EB Garamond** is used as the nearest free substitute. Supply the original TTF/OTF if exact reproduction is required.
- No Figma source file was provided. Visual recreation is based on the live website and uploaded SVGs.
- Photography/imagery is referenced but not bundled — the OG image URL is from GoDaddy's CDN and not redistributable.
