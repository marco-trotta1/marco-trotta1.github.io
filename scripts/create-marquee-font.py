"""Package the site's marker lettering from licensed handwriting outlines."""

from pathlib import Path

from fontTools import subset
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts/font-source/AnnieUseYourTelescope-Regular.ttf"
OUTPUT = ROOT / "public/fonts/marco-marker.woff"
TEXT = "Marco Trotta Mail: marcotrotta909 [at] gmail [dot] com"


def build_font() -> None:
    font = TTFont(SOURCE, recalcTimestamp=False)
    options = subset.Options()
    options.name_IDs = [0, 1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14]
    options.name_legacy = True
    options.name_languages = [0x409]
    options.drop_tables += ["FFTM"]
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(text=TEXT)
    subsetter.subset(font)

    # Keep the source curves. Shorten the tall l to match the reference lettering.
    glyph_set = font.getGlyphSet()
    pen = TTGlyphPen(glyph_set)
    glyph_set["l"].draw(TransformPen(pen, (1, 0, 0, 0.89, 0, 0)))
    font["glyf"]["l"] = pen.glyph()
    font["hmtx"]["space"] = (300, 0)

    addOpenTypeFeaturesFromString(font, """
        languagesystem DFLT dflt;
        feature kern {
            pos M a -12;
            pos a r -8;
            pos r c -10;
            pos T r -26;
            pos r o -8;
            pos o t -12;
            pos t t -20;
            pos t a -14;
            pos a i -8;
            pos i l 10;
            pos nine zero 6;
        } kern;
    """)

    names = {
        1: "Marco Marker",
        2: "Regular",
        3: "Marco Marker Regular 2.1",
        4: "Marco Marker Regular",
        5: "Version 2.1",
        6: "MarcoMarker-Regular",
    }
    for record in font["name"].names:
        if record.nameID in names:
            record.string = names[record.nameID].encode(record.getEncoding())

    font["hhea"].ascent = 800
    font["hhea"].descent = -240
    font["hhea"].lineGap = 0
    font["OS/2"].version = 4
    font["OS/2"].sTypoAscender = 800
    font["OS/2"].sTypoDescender = -240
    font["OS/2"].sTypoLineGap = 0
    font["OS/2"].fsSelection |= 1 << 7
    font.flavor = "woff"
    font.save(OUTPUT)
    print(f"Built {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    build_font()
