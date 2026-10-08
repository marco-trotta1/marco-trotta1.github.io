# Marco Trotta

This repository contains a static personal website. Next.js exports the site to the `out` directory.

## Run locally

1. Install Node.js 22 or later.
2. Run `npm install`.
3. Run `npm run dev`.
4. Open `http://localhost:3000`.

## Deploy to GitHub Pages

1. Push this repository to GitHub with the `main` branch.
2. Open the repository settings.
3. Select **Pages** and set the source to **GitHub Actions**.
4. Push a change to `main`, or run the **Deploy to GitHub Pages** workflow.

The workflow builds the static site and deploys it to GitHub Pages. It sets the repository path automatically for project sites.

## Marquee font

The custom font lives in `public/fonts/marco-marquee.ttf`. It follows the visible marker strokes in the reference photo.

Install the font builder with `python3 -m pip install -r requirements-font.txt`.

Run `python3 scripts/create-marquee-font.py` to rebuild the font. It supports the characters used in the name and email.
