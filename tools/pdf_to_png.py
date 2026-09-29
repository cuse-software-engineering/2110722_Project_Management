#!/usr/bin/env python3
"""Convert a PDF file to PNG images (one PNG per page).

Usage:
    python3 pdf_to_png.py <input.pdf> [output_dir] [--dpi N]
"""
import argparse
import pathlib

import pymupdf


def pdf_to_png(pdf_path: pathlib.Path, output_dir: pathlib.Path, dpi: int = 200) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    stem = pdf_path.stem
    for page in doc:
        pix = page.get_pixmap(dpi=dpi)
        out_file = output_dir / f"{stem}_page{page.number + 1:02d}.png"
        pix.save(out_file)
        print(f"Saved {out_file}")
    page_count = doc.page_count
    doc.close()
    print(f"Done: {page_count} page(s) converted.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF pages to PNG images")
    parser.add_argument("pdf", type=pathlib.Path, help="Path to the input PDF")
    parser.add_argument("output_dir", type=pathlib.Path, nargs="?", default=None,
                        help="Output directory (default: <pdf_dir>/png)")
    parser.add_argument("--dpi", type=int, default=200, help="Render resolution (default: 200)")
    args = parser.parse_args()

    out_dir = args.output_dir or args.pdf.parent / "png"
    pdf_to_png(args.pdf, out_dir, args.dpi)
