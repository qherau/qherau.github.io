# Quentin Herau — personal page

A standalone academic website with a biography, portrait, publications,
research service and contact links. It uses static HTML, CSS and JavaScript,
with local images and no external font or build dependency.

## Preview

From this folder, run:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open http://127.0.0.1:8765/. In the combined website preview, use
http://127.0.0.1:8765/Personal/.

## Edit

Edit the biography or publication records in `build_personal.py`, then run:

```sh
python3 build_personal.py
```

This regenerates `index.html` and `publications.json`. Style and interactions
are in `assets/personal.css` and `assets/personal.js`. Publication entries
support paper, project, calibration-code and benchmark links. The header
dropdown connects the personal page and four research projects. Asset sources are recorded in
`assets-sources.json`.

## Host

Published at https://qherau.github.io/ from the `main` branch, repository root,
of [qherau/qherau.github.io](https://github.com/qherau/qherau.github.io).
Keep `.nojekyll` and the relative asset paths. Commit the regenerated HTML,
publication records and any changed assets; GitHub Pages deploys the update.

The calibration and benchmark code repositories are separate and remain
private during final release review. Their links become available to everyone
when those repositories are released.
