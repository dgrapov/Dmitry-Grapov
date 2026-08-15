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
- **`archive/hugo-site/`** — the previous Hugo-based site (theme, R build scripts,
  old `docs/` output), kept for reference. No longer built or deployed.

## Editing content (links, bio, sections)

All copy — including links — lives in the `sections` array near the top of the
logic block in `site-src/3d-forest/Dmitry Grapov Forest.dc.html`. See that folder's
README for the full guide. After editing, re-export/rebuild to a self-contained file
and replace `docs/index.html`.

## Deploying

GitHub Pages is already configured (`master` / `/docs`). Merge changes to `master`
and the live site updates automatically — no CI/build step required.
