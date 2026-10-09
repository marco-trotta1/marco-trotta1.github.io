import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

test("the wave uses an alpha mask and follows the text color", () => {
  const html = readFileSync(new URL("../out/index.html", import.meta.url), "utf8");
  const css = readFileSync(new URL("../src/app/globals.css", import.meta.url), "utf8");
  const wave = html.match(/<span\b[^>]*class="signature-wave"[^>]*><\/span>/)?.[0];

  assert.ok(wave, "Render the wave with a span and a transparent alpha mask.");
  assert.doesNotMatch(html, /<mask\b/);
  assert.match(html, /rel="preload"[^>]*href="\/fonts\/marco-marker\.woff\?v=2\.1"[^>]*as="font"/);

  const waveStyle = css.match(/\.signature-wave\s*\{([^}]+)\}/)?.[1];
  assert.ok(waveStyle);
  assert.match(waveStyle, /background-color:\s*currentColor/);
  assert.match(waveStyle, /-webkit-mask-image:\s*url\("\/signature-wave-alpha\.png"\)/);
  assert.match(waveStyle, /mask-image:\s*url\("\/signature-wave-alpha\.png"\)/);
  assert.match(css, /font-family:\s*"Marco Marker",\s*system-ui,\s*sans-serif/);
  assert.doesNotMatch(css, /\bcursive\b/);
});
