"""Build the site-specific handwritten font from the marquee reference."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public" / "fonts" / "marco-marquee.ttf"
UNITS_PER_EM = 1000
STROKE_WIDTH = 58

Point = tuple[float, float]
Stroke = tuple[Point, ...]


def oval(
    center_x: float,
    center_y: float,
    radius_x: float,
    radius_y: float,
    phase: float = 0,
    steps: int = 36,
) -> Stroke:
    points = []
    for index in range(steps):
        angle = (2 * math.pi * index / steps) + phase
        wobble = 1 + 0.032 * math.sin(3 * angle + phase) + 0.012 * math.sin(7 * angle)
        points.append(
            (
                center_x + radius_x * math.cos(angle) * wobble,
                center_y + radius_y * math.sin(angle) * wobble,
            )
        )
    return tuple(points)


def arc(
    center_x: float,
    center_y: float,
    radius_x: float,
    radius_y: float,
    start_degrees: float,
    end_degrees: float,
    steps: int = 20,
) -> Stroke:
    points = []
    for index in range(steps + 1):
        fraction = index / steps
        angle = math.radians(start_degrees + (end_degrees - start_degrees) * fraction)
        wobble = 1 + 0.032 * math.sin(3 * angle + start_degrees) + 0.012 * math.sin(7 * angle)
        points.append(
            (
                center_x + radius_x * math.cos(angle) * wobble,
                center_y + radius_y * math.sin(angle) * wobble,
            )
        )
    return tuple(points)


GLYPHS: dict[str, tuple[int, tuple[Stroke, ...]]] = {
    "space": (280, ()),
    "M": (760, (
        ((40, 40), (35, 690), (100, 700), (365, 385), (635, 705), (690, 680), (700, 45)),
    )),
    "T": (680, (
        ((35, 670), (300, 690), (640, 670)),
        ((335, 675), (320, 480), (330, 260), (315, 55)),
    )),
    "a": (545, (
        ((430, 535), (365, 625), (260, 642), (155, 580), (112, 450), (128, 305), (220, 210), (340, 225), (420, 328)),
        ((420, 670), (423, 465), (432, 280), (420, 65)),
    )),
    "c": (480, (
        arc(250, 375, 174, 250, 45, 315),
    )),
    "e": (495, (
        arc(253, 370, 176, 232, 42, 318),
        ((92, 375), (250, 407), (402, 380)),
    )),
    "g": (540, (
        oval(263, 435, 163, 206, phase=0.08),
        ((420, 520), (415, 315), (418, 105), (360, -45), (220, -70), (135, -5)),
    )),
    "i": (260, (
        ((125, 70), (135, 295), (130, 525)),
        ((137, 665),),
    )),
    "l": (330, (
        ((190, 700), (150, 570), (140, 390), (155, 205), (205, 85)),
    )),
    "m": (790, (
        ((55, 70), (70, 560), (135, 582), (230, 365), (300, 575), (365, 590), (485, 360), (535, 570), (625, 590), (720, 375), (742, 70)),
    )),
    "o": (565, (
        oval(283, 365, 206, 260, phase=0.03),
    )),
    "r": (440, (
        ((55, 75), (70, 565), (135, 575), (184, 455), (278, 545), (360, 535)),
    )),
    "t": (440, (
        ((235, 690), (210, 520), (220, 320), (200, 95)),
        ((60, 455), (235, 468), (390, 450)),
    )),
    "0": (570, (
        oval(288, 365, 207, 278, phase=-0.04),
        ((130, 205), (442, 545)),
    )),
    "9": (570, (
        oval(275, 505, 190, 195, phase=0.02),
        ((428, 520), (420, 330), (410, 130), (340, -48), (250, -70)),
    )),
    "at": (710, (
        oval(332, 380, 250, 270, phase=0.05),
        oval(330, 380, 112, 145, phase=-0.02),
        ((438, 424), (474, 297), (572, 315), (610, 420), (595, 560)),
    )),
    "period": (210, (
        ((118, 82),),
    )),
    "colon": (245, (
        ((122, 535),),
        ((126, 180),),
    )),
    ".notdef": (600, (
        ((45, 45), (45, 650), (555, 650), (555, 45), (45, 45)),
        ((105, 100), (495, 590)),
        ((495, 100), (105, 590)),
    )),
}


CHARACTER_MAP = {
    " ": "space",
    "M": "M",
    "T": "T",
    "a": "a",
    "c": "c",
    "e": "e",
    "g": "g",
    "i": "i",
    "l": "l",
    "m": "m",
    "o": "o",
    "r": "r",
    "t": "t",
    "0": "0",
    "9": "9",
    "@": "at",
    ".": "period",
    ":": "colon",
}


def signed_area(points: Iterable[Point]) -> float:
    point_list = list(points)
    return sum(
        point_list[index][0] * point_list[(index + 1) % len(point_list)][1]
        - point_list[(index + 1) % len(point_list)][0] * point_list[index][1]
        for index in range(len(point_list))
    ) / 2


def add_polygon(pen: TTGlyphPen, points: list[Point]) -> None:
    if signed_area(points) > 0:
        points.reverse()
    pen.moveTo((round(points[0][0]), round(points[0][1])))
    for point in points[1:]:
        pen.lineTo((round(point[0]), round(point[1])))
    pen.closePath()


def add_disc(pen: TTGlyphPen, center: Point, radius: float) -> None:
    points = [
        (
            center[0] + radius * math.cos(2 * math.pi * index / 16),
            center[1] + radius * math.sin(2 * math.pi * index / 16),
        )
        for index in range(16)
    ]
    add_polygon(pen, points)


def add_stroke(pen: TTGlyphPen, points: Stroke) -> None:
    if len(points) == 1:
        add_disc(pen, points[0], STROKE_WIDTH / 2)
        return

    radius = STROKE_WIDTH / 2
    for start, end in zip(points, points[1:]):
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.hypot(dx, dy)
        if length == 0:
            continue
        offset = (-dy * radius / length, dx * radius / length)
        add_polygon(
            pen,
            [
                (start[0] + offset[0], start[1] + offset[1]),
                (end[0] + offset[0], end[1] + offset[1]),
                (end[0] - offset[0], end[1] - offset[1]),
                (start[0] - offset[0], start[1] - offset[1]),
            ],
        )

    for point in points:
        add_disc(pen, point, radius)


def build_font() -> None:
    glyph_order = [".notdef", *dict.fromkeys(CHARACTER_MAP.values())]
    font_builder = FontBuilder(UNITS_PER_EM, isTTF=True)
    font_builder.setupGlyphOrder(glyph_order)
    font_builder.setupCharacterMap(
        {ord(character): glyph_name for character, glyph_name in CHARACTER_MAP.items()}
    )

    glyphs = {}
    metrics = {}
    for glyph_name in glyph_order:
        advance_width, strokes = GLYPHS[glyph_name]
        pen = TTGlyphPen(None)
        for stroke in strokes:
            add_stroke(pen, stroke)
        glyphs[glyph_name] = pen.glyph()
        metrics[glyph_name] = (advance_width, 20)

    font_builder.setupGlyf(glyphs)
    font_builder.setupHorizontalMetrics(metrics)
    font_builder.setupHorizontalHeader(ascent=800, descent=-190)
    font_builder.setupNameTable(
        {
            "familyName": "Marco Marquee",
            "styleName": "Regular",
            "uniqueFontIdentifier": "Marco Marquee Regular 1.0",
            "fullName": "Marco Marquee Regular",
            "psName": "MarcoMarquee-Regular",
            "version": "Version 1.0",
        }
    )
    font_builder.setupOS2(
        sTypoAscender=800,
        sTypoDescender=-190,
        usWinAscent=800,
        usWinDescent=190,
    )
    font_builder.setupPost()
    font_builder.setupMaxp()
    font_builder.setupHead()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    font_builder.save(OUTPUT)


if __name__ == "__main__":
    build_font()
