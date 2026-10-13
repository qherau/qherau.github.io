# Quentin Herau

Personal research website: **[qherau.github.io](https://qherau.github.io/)**.

Static HTML, CSS and JavaScript, with a small Python script to generate the
publication list. No package installation is required.

## Preview

From this folder, run:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open [localhost:8765](http://127.0.0.1:8765/).

## Edit

Edit the biography and publication records in `build_personal.py`, then run:

```sh
python3 build_personal.py
```

This regenerates `index.html` and `publications.json`. Edit the generator
instead of the generated files. Styles and interactions live in
`assets/personal.css` and `assets/personal.js`. Images are stored in `assets/`;
their sources are recorded in `assets-sources.json`.

## Deploy

GitHub Pages serves the repository root on `main`. After previewing a change,
commit and push the source, regenerated files and any updated assets.
Keep `.nojekyll` and relative asset paths intact.
