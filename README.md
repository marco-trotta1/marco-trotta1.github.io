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

The custom font lives in `public/fonts/marco-marker.woff`. It appears only in the name and contact line.
It uses licensed handwriting outlines, with spacing and proportions chosen from the reference photo.
The source, attribution, and modification details are in `scripts/font-source/README.md`.

The contact line displays `marcotrotta909 [at] gmail [dot] com`. The link opens an email to `marcotrotta909@gmail.com`.

Install the font builder with `python3 -m pip install -r requirements-font.txt`.

Run `python3 scripts/create-marquee-font.py` to rebuild the font. It supports the characters used in the name and email.

## Signature and sections

The supplied wave drawing appears beside the name as a decorative signature mark.
The signature has a small rightward offset to balance the wave beside the name.
The original image is stored in `public/signature-wave.png`. An SVG mask removes its background and paints the drawing with the text color.
The mask stays fixed during theme changes. The wave follows the text color transition without a separate background or blend mode.
The sections span the page with small side margins. About me appears above Things I have built, and both headings stay centered.
The about text and project descriptions are in `src/app/page.tsx`. The project names use italics, and the body text uses a system font.

Run `npm run build`, then `node --test tests/wave-theme.test.mjs` to check the wave rendering.
The deployment workflow runs this check before it uploads the site.

## OPEN sign

The sign uses bright tube cores, saturated color, and layered fluorescent halos. The blue oval surrounds the letters.
The animation adds slow light variation and occasional brief dips. It keeps the sign lit.
The sign stays steady when the visitor requests reduced motion.
