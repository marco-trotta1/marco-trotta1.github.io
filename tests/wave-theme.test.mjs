import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

test("the wave uses a stable transparent mask and follows the text color", () => {
  const html = readFileSync(new URL("../out/index.html", import.meta.url), "utf8");
  const css = readFileSync(new URL("../src/app/globals.css", import.meta.url), "utf8");
  const wave = html.match(/<svg\b[^>]*class="signature-wave"[^>]*>[\s\S]*?<\/svg>/)?.[0];

  assert.ok(wave, "Render the wave as an SVG mask instead of an opaque image.");
  assert.match(wave, /<mask\b[^>]*id="signature-wave-mask"[^>]*style="mask-type:luminance"/);
  assert.match(wave, /<image\b[^>]*href="\/signature-wave.png"/);

  const visibleMarkup = wave.replace(/<defs>[\s\S]*?<\/defs>/, "");
  assert.doesNotMatch(visibleMarkup, /<(?:image|img)\b/);
  assert.match(visibleMarkup, /<rect\b[^>]*fill="currentColor"[^>]*mask="url\(#signature-wave-mask\)"/);

  const wrapperStyle = css.match(/\.signature-wave\s*\{([^}]+)\}/)?.[1];
  assert.ok(wrapperStyle);
  assert.doesNotMatch(wrapperStyle, /(?:filter|mix-blend-mode)\s*:/);
  assert.doesNotMatch(css, /data-theme[^}]*\.signature-wave(?:-source)?\s*\{/);

  const sourceStyle = css.match(/\.signature-wave-source\s*\{([^}]+)\}/)?.[1];
  assert.ok(sourceStyle);
  assert.match(sourceStyle, /filter:\s*grayscale\(1\) contrast\(1\.5\) invert\(1\)/);
});
