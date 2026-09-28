# Roadmap — telling more of the story, keeping the forest

Goal: make the Digital Food Forest more engaging and tell more of Dmitry's story
**without** changing its look (dark CRT-green voxels, VT323/Plex Mono, glitch
transitions, sacred-geometry halos). Constraint: it must stay a static GitHub Pages
site with no server and no build step.

Two references on GitHub Pages (once merged to `master`):

| URL | What |
|---|---|
| `/Dmitry-Grapov/` | Live site, unchanged |
| `/Dmitry-Grapov/v1/` | Frozen snapshot of the live site before this work (`docs/v1/index.html`) |
| `/Dmitry-Grapov/poc/` | Working proof of concept (`docs/poc/`, a copy of `Dmitry Grapov Forest POC.dc.html`) |

Screenshots of the POC are in [`poc-screens/`](poc-screens/).

---

## The story model: present, past, (future)

The forest is the **present**: five clickable forms (origin, code, teaching, writing, contact).
The POC adds a second place to look.

- **◂ The past: a felled redwood stump** off to the left of the forest. Its top face
  shows **growth rings**, one band per career chapter (the outer ring is the most recent).
  The camera pans left to it with the existing glitch transition. A timeline panel
  lists the chapters, and selecting one lights up its ring in the wood. Tree rings are the
  forest's own way to record time, so the metaphor fits the rest of the site
  (mushroom ring = origin, slime mold = teaching…).
- **▸ The future (proposed, not built): a seed bank / nursery** to the right, holding
  what's growing next (current interests, open-to-work areas, side projects). It
  mirrors the stump, so the site reads as past ← present → future.

## What the POC already does (`docs/poc/`)

| # | Feature | Why |
|---|---|---|
| 1 | Subtitle under the name: *AI/ML · DATA · SYNTHETIC BIOLOGY* | First 5 seconds: who is this |
| 2 | Rotating hints (*click the glowing forms · ◂ look left into the past · keys 1–5*) | Tells visitors what they can do |
| 3 | **Beacon pulse** on forms you haven't found yet; `n/5 FOUND` counter | Discovery loop; the progress dashes now have a meaning |
| 4 | **Floating name tag** over the hovered form | Hover used to show only `◆` in a corner |
| 5 | **Camera glide** to the form before its panel opens | The transition most top Three.js portfolios use |
| 6 | **≡ INDEX** menu: a fast, non-3D path to every section | Recruiters, low-power phones, accessibility |
| 7 | Keyboard: `1–5` open, `Esc` close, `←`/`T` past, `→` present, `↑↓` rings; swipe on touch | Accessibility, power users |
| 8 | **◂ PAST: stump + growth-ring timeline** (right panel on desktop, bottom sheet on phones) | Tells the career story |
| 9 | **5/5 FOREST MAPPED** reward with *Start a conversation* (email) and *See the growth rings* | Turns exploring into contact |
| 10 | `<title>`, meta description, Open Graph and Twitter tags, `docs/og-image.jpg` | Search results and LinkedIn previews (live site title is "Bundled Page") |

The POC eases camera moves by elapsed time, not per frame, so glides and pans take the same
time on slow phones as on fast laptops.

## Phases

**Phase 0: snapshot (done).** `docs/v1/` is a frozen copy of the current site.

**Phase 1: quick wins (POC items 1–7, 9, 10).** Move them into
`Dmitry Grapov Forest.dc.html`, then re-export `docs/index.html`. Also:
- **Bundle three.js and React locally.** The live site loads them from `unpkg.com` at
  runtime, so if unpkg is slow or blocked, the site renders nothing. Put
  them in `docs/vendor/` or inline them in the bundle.
- Add the meta and Open Graph tags to the **outer** shell of `docs/index.html`. Link scrapers don't
  run JavaScript, so the tags inside the bundled template are invisible to them.

**Phase 2: the story (POC item 8 plus real content).**
- Fill `rings` in the POC with real dates and highlights from the résumé/CV folder
  (see *Content needed* below).
- Ring detail: clicking a row opens a short story card using the existing panel style:
  *problem → what I did → result (a number) → one link → one image*.
- Deep links (`#past`, `#code`, `#ring-3`), so a specific chapter can be shared.
- Optional: a creature (the crow) flies over to the stump when you arrive, so the transition
  feels alive.

**Phase 3: depth and polish.**
- ▸ Future / nursery view (see above).
- Visuals inside the panels: MetaMapR network graphic, talk thumbnails, Flickr photos.
- Opt-in ambient sound toggle (birds, water), off by default.
- Respect the OS "reduce motion" setting: skip the glitch and glide.
- Privacy-friendly analytics (GoatCounter or Plausible both work on Pages) to see which forms get opened.
- Time-of-day lighting (dawn/dusk palette shift from the visitor's clock).

## Content needed for the growth rings

The POC's `rings` array (near the top of the logic block in
`Dmitry Grapov Forest POC.dc.html`) is a **draft**. Its order and wording come from the
site's own copy, and its dates are placeholders (`—`). For each chapter, supply:

```js
{ when: '2019–2022', title: 'Company or milestone', where: 'SHORT DOMAIN LABEL',
  note: 'One sentence: what you did and what changed because of it.', url: 'optional link' }
```

Six to eight rings read best. The outermost ring is the most recent. Good candidates: degrees, each
role, flagship open-source releases (MetaMapR, DeviumWeb), notable talks and papers, founding CDS.

## Previewing locally

```bash
python3 -m http.server          # from the repo root
# open http://localhost:8000/docs/poc/   (the POC)
#      http://localhost:8000/docs/       (the live site)
```

The POC loads `support.js` (the authoring runtime) and `_ds/` next to itself, which is
why those are copied into `docs/poc/`. After editing the POC source, refresh the copy:

```bash
cp "site-src/3d-forest/Dmitry Grapov Forest POC.dc.html" docs/poc/index.html
```
