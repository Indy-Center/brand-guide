"""Fail if an SVG's masks are filled with anything but white.

Masks marked mask-type:alpha ignore their fill colour in browsers, but tools
that read masks by brightness (some design apps and renderers) draw a grey or
dark mask as see-through, so the mark comes out faint or invisible. White
masks look the same everywhere.
"""

import pathlib
import sys
import xml.etree.ElementTree as ET

SVG_NS = "{http://www.w3.org/2000/svg}"
WHITE = {"#ffffff", "#fff", "white", "none"}
problems = []
for path in sorted(pathlib.Path(".").rglob("*.svg")):
    root = ET.parse(path).getroot()
    fills = {
        el.get("fill").lower()
        for mask in root.iter(f"{SVG_NS}mask")
        for el in mask.iter()
        if el.get("fill")
    } - WHITE
    if fills:
        problems.append(f"{path}: mask filled {', '.join(sorted(fills))}; fill masks #FFFFFF")

print("\n".join(problems) or "Every SVG mask is white.")
sys.exit(1 if problems else 0)
