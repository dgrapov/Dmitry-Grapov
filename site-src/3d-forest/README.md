# Digital Food Forest — Dmitry Grapov portfolio scene

An interactive 3D voxel forest. Five things in the scene are clickable; each opens a panel with
copy and links. Ambient creatures (squirrel, frog, lizard, scorpion, snake) enter one at a time,
visit one of the clickable forms — triggering its plasma/geometry flare — and leave. A crow is both
a resident animation and one of the five clickable items.

## Files

| File | What it is |
|---|---|
| `Dmitry Grapov Forest.dc.html` | **The source you edit.** Markup + logic in one file. |
| `dist/index.html` | Self-contained build (no dependencies) — this is what you deploy. |
| `Dmitry Grapov Portfolio Pixel.dc.html` | Earlier variation: chunky pixel hologram tree, orbitable. |
| `Dmitry Grapov Portfolio.dc.html` | Earliest variation: scroll-through tunnel of nodes. |
| `support.js`, `_ds/` | Runtime + design-system assets used by the `.dc.html` sources. |
| `sections.yml` | Editable content template (generated) — see [Editing via `sections.yml`](#editing-via-sectionsyml-recommended). |
| `scripts/` | `sync-sections.sh export`/`apply` and their Node/Python helpers, for round-tripping `sections.yml` ⇄ the `.dc.html` source. |

## Editing the content

All copy lives in ONE place: the `sections` array near the top of the logic block in
`Dmitry Grapov Forest.dc.html`. Order matters — index 0…4 maps to a specific object in the scene:

| Index | Scene object | Currently |
|---|---|---|
| 0 | mushroom ring (front left) | Origin / about |
| 1 | hollow in the right redwood | Code & science |
| 2 | slime mold on the floor | Teaching |
| 3 | the crow (perched, flies between branches) | Writing & art |
| 4 | the spring pool (right) | Contact |

Each entry:

```js
{
  kicker: 'MUSHROOM RING // ORIGIN',       // small all-caps label
  title:  'Cultivating signal from noise', // headline
  body:   "One or two paragraphs…",        // prose
  chips:  ['MetaMapR','networkly'],        // optional tag pills; [] to hide
  links:  [{ label: 'GitHub', url: 'https://github.com/dgrapov' }],
}
```

Notes
- Keep `body` to roughly 40–90 words; the panel is fixed-width and long copy pushes the links down.
- `chips` are for project/tool names. An empty array removes the row entirely.
- `links` render as bordered buttons in order; 1–3 works best. `mailto:` links are fine.
- Don't rename the keys, and keep exactly five entries unless you also change the scene (below).

### Editing via `sections.yml` (recommended)

Instead of hand-editing the one-line-per-section JS array above, edit a plain YAML template:

```bash
cd site-src/3d-forest
scripts/sync-sections.sh export   # html -> sections.yml (pulls the current copy)
$EDITOR sections.yml              # edit kicker / title / body / chips / links
scripts/sync-sections.sh apply    # sections.yml -> html (writes the array back)
```

`sections.yml` holds the same five entries, one YAML doc each, with `body` as a
readable block of text and `links` as a `label`/`url` list — no JS quoting/escaping
to worry about. `index`/`scene` fields in the file are just labels for orientation;
order in the file (not the `index` value) is what gets written back, and it must stay
five entries. `apply` requires Node (`node`) and Python 3 with PyYAML (`pyyaml`).

As always: after `apply`, re-export/rebuild `docs/index.html` (below) and actually
load it in a browser before merging.

## Changing which objects are clickable

Each object is registered with one `addHotspot(cells, accentColor, lightPosition, motif)` call inside
`setup()`, in the same order as `sections`. To retire an object, delete its `addHotspot` call **and**
its `sections` entry. To add one, build its voxel cells with the existing helpers
(`mushroom`, `blob`, `line`, `slime`, `ring`, `frond`, `tuft`, `column`) and add a matching
`sections` entry. Two constraints:

- `canVisit` (just above the animation loop) lists which creatures may visit which index —
  index 1 is up a trunk, so only climbers are allowed there. Update it if indices change.
- Outline-only shapes (like the hollow arch) have no solid surface to click, so they pass
  `{ proxyPick: true }` to use an invisible box instead. Solid shapes don't need it.

## Tweaks

The four exposed props: `seed`, `pixelSize`, `accentA`, `accentB`.
`seed` regenerates the whole layout — mushroom count and placement, slime-mold branching,
lichen patches, which sacred-geometry motif belongs to which object. `0` means "random each load";
set a specific number to lock a layout you like. `pixelSize` raises/lowers render resolution
(1 = sharpest, higher = chunkier and faster).

## Deploying to GitHub Pages

Free GitHub Pages serves static files only — which is all this is.

1. Copy `dist/index.html` to the root of your Pages repo (or into `/docs`).
2. Settings → Pages → deploy from branch, root or `/docs`.
3. Done. No build step, no server. The scene is one file, ~570 KB, works offline.

Re-export after any content edit: the build in `dist/` is a snapshot, not a live link to the source.

## Performance notes

WebGL is required. The scene is a few thousand instanced cubes plus particle systems — fine on
laptops and modern phones. If you need it lighter, raise `pixelSize` to 2–3; that alone roughly
halves fill cost. There is intentionally no reduced-motion fallback.
