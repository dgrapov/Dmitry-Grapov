# Dmitry Grapov — Portfolio

Live at **https://dgrapov.github.io/Dmitry-Grapov/** via GitHub Pages (branch `master`, folder `/docs`).

## Structure

- **`docs/index.html`** — the deployed site. A self-contained, single-file interactive
  3D voxel scene ("Digital Food Forest") — no build step, no server, works offline.
  This is the only file GitHub Pages serves.
- **`site-src/3d-forest/`** — editable source for the scene above, plus two earlier
  design variations (pixel hologram tree, scroll tunnel). See
  [`site-src/3d-forest/README.md`](site-src/3d-forest/README.md) for how to edit
  content/links and re-export to `docs/index.html`.

The previous Hugo-based site (theme, R build scripts, old `docs/` output, and
its unrelated template placeholder content/testimonials) has been removed —
this is a clean, from-scratch build. It's still recoverable from git history
(the commit before this one) if ever needed.

## For developers

**Requirements**: any modern browser with WebGL2. No Node, no package
manager, no build tooling needed to *run* the site.

**Local preview** — three options, no deployment required:
1. Open `docs/index.html` directly in a browser (`file://` works — the
   README for `site-src/3d-forest/` documents this too).
2. Serve it locally: `python3 -m http.server` from the repo root, then visit
   `http://localhost:8000/docs/`.
3. Headless, for scripted checks (what was used to verify this repo's own
   changes): [Playwright](https://playwright.dev/python/) against the
   `file://` URL, asserting no `pageerror`/console errors and that
   `document.querySelector('#__bundler_err')` is empty. A GPU-capable
   headless Chromium is required for the WebGL canvas to actually paint,
   not just parse.

**Editing content** (links, bio, career details, which employers show up as
chips, etc.) — see [Editing content](#editing-content-links-bio-sections)
below; everything lives in one `sections` array.

**Editing the scene itself** (adding/removing clickable objects, changing
voxel geometry, ambient creature behavior, color themes) — see
[`site-src/3d-forest/README.md`](site-src/3d-forest/README.md), which covers
the `addHotspot` registration, the shared voxel-primitive helpers, and the
exposed `seed` / `pixelSize` / `accentA` / `accentB` props.

**Regenerating `docs/index.html` by hand** (rather than through the
authoring tool) — read [the sharp edge below](#a-sharp-edge-if-you-ever-hand-edit-docsindexhtml-directly)
first; it's a real, non-obvious way to silently corrupt the file.

**Contributing / deploying changes**: this repo treats `master` as the live
site — push feature branches and open a PR rather than committing straight
to `master`, and **actually render the result in a browser before merging**
(a JSON round-trip or regex check is not sufficient evidence the page works;
see the sharp edge above for why). Once merged, GitHub Pages picks it up
automatically.

## Editing content (links, bio, sections)

All copy — including links — lives in the `sections` array near the top of the
logic block in `site-src/3d-forest/Dmitry Grapov Forest.dc.html`. See that folder's
README for the full guide. After editing, re-export/rebuild to a self-contained file
and replace `docs/index.html`.

## Deploying

GitHub Pages is already configured (`master` / `/docs`). Merge changes to `master`
and the live site updates automatically — no CI/build step required.

## Artistic inspiration

The scene is a **food forest**, not a résumé with a 3D skin — the metaphor is
literal. Five career facets are grown as forest elements rather than listed as
sections:

| Forest element | Represents | Why |
|---|---|---|
| Mushroom ring | Origin / bio | Fungal "fairy rings" mark where a colony began — a starting point that keeps growing outward |
| Hollow redwood | Code & science | Where the structural, load-bearing work lives — the tools everything else stands on |
| Slime mold | Teaching | *Physarum* solves shortest-path problems with no brain, just distributed signal — knowledge spreading root to root, not top-down |
| The crow | Writing & art | Corvids are tool-users and pattern-recognizers that move between fixed points — carrying things across the canopy |
| Spring pool | Contact | Water as convergence point; the one place every path in a forest eventually leads |

Ambient creatures (squirrel, frog, lizard, scorpion, snake) wander the scene on
their own schedule, visit whichever hotspot they're allowed near, trigger a
brief flare, and move on — small unscripted life happening whether or not
anyone's watching, the way a real ecosystem doesn't pause for an audience.
It's a deliberate rhyme with the site owner's own off-the-clock life
(trail running, mountain biking, an off-grid farm) and with his actual field
(metabolomic **network** analysis, mycelium-like by nature) — the same
patience-and-feedback-loops relationship to systems, just rendered as biology
instead of biochemistry.

## Technology

`docs/index.html` is a **single self-contained file** (~570 KB) — no server,
no build step, no external requests at runtime, works offline straight off
disk or from any static host.

- **Rendering**: Three.js (r160), thousands of instanced `BoxGeometry` cubes
  (`THREE.InstancedMesh`) rather than individual meshes, so the whole voxel
  forest is a handful of draw calls.
- **Procedural generation**: a small deterministic seeded PRNG drives organic
  shape generators (`mushroom`, `blob`, `slime`, `frond`, `tuft`, `column`,
  `ring`) — mushroom placement, slime-mold dendritic growth, lichen patches,
  and which sacred-geometry motif belongs to which hotspot are all derived
  from one `seed` prop. `seed: 0` regenerates a new layout on every load;
  a fixed integer locks in a specific one.
  - `pixelSize` (1–5) trades render resolution for GPU cost — the single
    exposed performance knob. No reduced-motion fallback; WebGL is required.
- **UI/content layer**: React (UMD build), driving the hotspot panels —
  `Component.sections` is the single array holding every bit of copy and
  every link on the site (see [Editing content](#editing-content-links-bio-sections)).
- **Packaging**: everything — React, ReactDOM, Three.js, all fonts — is
  embedded as base64 (gzip-compressed where it helps) inside a
  `<script type="__bundler/manifest">` block. On load, a small bootstrap
  script decodes those into `blob:` URLs, substitutes them into an inlined
  HTML template, and swaps `document.documentElement` for the fully
  resolved document. This is *why* the file can be dropped anywhere
  (GitHub Pages, `file://`, any static host) with zero configuration.

### A sharp edge, if you ever hand-edit `docs/index.html` directly

The page's own markup — including its inline `<script>` tags — is stored as
one big **JSON-encoded string** inside
`<script type="__bundler/template">`. If you regenerate that block yourself
(rather than through the authoring tool — see `site-src/3d-forest/README.md`),
a plain `JSON.stringify`/`json.dumps` is **not enough**: any literal
`</script` substring inside the embedded page (which it has, since the page
contains its own scripts) will prematurely close the *outer* script tag when
the browser's HTML parser scans it — before your JavaScript ever gets to
`JSON.parse` it. Escape `</` as `<\/` in the serialized string (the bundler's
own code does exactly this elsewhere, e.g. around `resourceScript`). This
bit us once already in this repo's history — verify any hand patch by
actually loading the file in a browser (or headless Chromium via Playwright),
not just by re-parsing the JSON in a script.
