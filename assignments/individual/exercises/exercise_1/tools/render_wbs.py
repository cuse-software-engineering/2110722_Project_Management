#!/usr/bin/env python3
"""Render workspace/diagrams/wbs.puml to wbs.png with PlantUML and trim the
blank margin (the chart uses an invisible dummy root, which leaves a white
strip above the real level-1 node).

Usage: python3 tools/render_wbs.py
"""
import pathlib
import subprocess

from PIL import Image, ImageChops

EXERCISE = pathlib.Path(__file__).resolve().parent.parent
DIAGRAMS = EXERCISE / "workspace" / "diagrams"
JAR = pathlib.Path("/workspaces/2110628_Requirement/resources/plantuml/plantuml-1.2026.7.jar")
MARGIN = 12  # px kept around the drawing


def main() -> None:
    subprocess.run(
        ["java", "-jar", str(JAR), "-tpng", "-o", str(DIAGRAMS), str(DIAGRAMS / "wbs.puml")],
        check=True,
    )
    png = DIAGRAMS / "wbs.png"
    img = Image.open(png).convert("RGB")
    bg = Image.new("RGB", img.size, (255, 255, 255))
    bbox = ImageChops.difference(img, bg).getbbox()
    if bbox:
        left, top, right, bottom = bbox
        img = img.crop((max(0, left - MARGIN), max(0, top - MARGIN),
                        min(img.width, right + MARGIN), min(img.height, bottom + MARGIN)))
        img.save(png)
    print(f"Wrote {png} ({img.width}x{img.height})")


if __name__ == "__main__":
    main()
