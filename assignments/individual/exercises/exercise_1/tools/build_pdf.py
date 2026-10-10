#!/usr/bin/env python3
"""Build the Exercise 1 submission PDF from workspace/exercise1.md.

Steps:
1. Render exercise1.md to PDF with WeasyPrint (A4 portrait, TH Sarabun from
   resources/fonts via @font-face, Laksaman as fallback). The WBS chart is workspace/diagrams/wbs.png, rendered
   beforehand by tools/render_wbs.py.
2. Post-process with PyMuPDF: stamp the student ID/name header and
   "Page i of n" footers on every page.
3. Output: report/watayut_6970267821.pdf (file named by name and student ID,
   as the exercise asks).

Usage: python3 tools/build_pdf.py [--preview DIR]
  --preview DIR   also render every page to DIR/page-N.png for checking
"""
import argparse
import pathlib

import pymupdf
import weasyprint
from markdown_it import MarkdownIt
from weasyprint.text.fonts import FontConfiguration

EXERCISE = pathlib.Path(__file__).resolve().parent.parent
BASE = EXERCISE / "workspace"
REPORT_DIR = EXERCISE / "report"
SOURCE = BASE / "exercise1.md"
STUDENT_ID = "6970267821"
STUDENT_NAME = "Watayut Aiamanan"
OUT_NAME = f"{STUDENT_NAME.split()[0].lower()}_{STUDENT_ID}.pdf"
FONT_DIR = pathlib.Path("/workspaces/2110628_Requirement/resources/fonts/20180808-TH-Sarabun-PSK")
FONT_FACES = "".join(
    f"@font-face {{ font-family: 'TH Sarabun'; src: url('{(FONT_DIR / file).as_uri()}'); "
    f"font-weight: {weight}; font-style: {style}; }}\n"
    for file, weight, style in [("THSarabun.ttf", "normal", "normal"), ("THSarabun Bold.ttf", "bold", "normal"),
                                ("THSarabun Italic.ttf", "normal", "italic"), ("THSarabun Bold Italic.ttf", "bold", "italic")]
)

CSS = """
@page { size: A4; margin: 1.9cm 1.6cm 1.9cm 1.6cm; }
/* TH Sarabun comes from FONT_FACES (resources/fonts); WeasyPrint only picks the
   @font-face files up when the same FontConfiguration is given to CSS() and
   write_pdf(). Laksaman is the fallback (it renders with wrong advance widths
   here, so the build checks that TH Sarabun really was embedded). */
body { font-family: "TH Sarabun", "Laksaman", sans-serif; font-size: 14pt; line-height: 1.3; color: #111; }
h1 { font-size: 18pt; border-bottom: 2px solid #444; padding-bottom: 4px; margin: 0 0 8px; }
h2 { font-size: 15pt; color: #1a3e6e; margin: 14px 0 4px; break-after: avoid; }
h3 { font-size: 13.5pt; color: #1a3e6e; margin: 10px 0 0; break-after: avoid; }
h2 + p, h3 + p, h3 + div { break-before: avoid; }
p { margin: 5px 0; orphans: 3; widows: 3; }
table { border-collapse: collapse; width: 100%; margin: 4px 0 8px; font-size: 11pt; line-height: 1.2; }
th, td { border: 1px solid #888; padding: 1.5px 4px; text-align: left; vertical-align: top; overflow-wrap: break-word; }
th { color: #1a3e6e; border-bottom: 2px solid #4f81bd; background: #f4f7fb; }
thead { display: table-header-group; }
tr { break-inside: avoid; }

/* figure: chart and caption stay together */
.figure { break-inside: avoid; margin: 4px 0 6px; }
.fig-wbs { display: block; width: 15.6cm; margin: 0 auto; }
.caption { text-align: center; font-size: 11.5pt; color: #333; margin: 3px 0 0; }
.keep-next { break-after: avoid; margin: 10px 0 2px; }

/* student header block: label | value, hide the empty markdown header row */
.kv table { font-size: 12.5pt; }
.kv thead { display: none; }
.kv td:nth-child(1) { width: 14%; font-weight: bold; background: #f4f7fb; }

/* Table 1, WBS in tabular form: level columns narrow, Level 4 (widest) unsized */
.wbs td:nth-child(1), .wbs th:nth-child(1) { width: 17%; }
.wbs td:nth-child(2), .wbs th:nth-child(2) { width: 19%; }
.wbs td:nth-child(3), .wbs th:nth-child(3) { width: 27%; }
.wbs td:nth-child(5), .wbs th:nth-child(5) { width: 5%; text-align: center; font-weight: bold; color: #8a6d00; }

/* Table 2, activity list: description column (4) unsized */
.act td:nth-child(1), .act th:nth-child(1) { width: 14%; font-weight: bold; }
.act td:nth-child(2), .act th:nth-child(2) { width: 9.5%; white-space: nowrap; }
.act td:nth-child(3), .act th:nth-child(3) { width: 25%; }
.act td:nth-child(5), .act th:nth-child(5) { width: 13%; }

/* Table 3, milestones */
.ms td:nth-child(1), .ms th:nth-child(1) { width: 10%; font-weight: bold; }
.ms td:nth-child(3), .ms th:nth-child(3) { width: 30%; }
"""


def stamp(pdf_path: pathlib.Path, header: str) -> None:
    """Post-process: stamp the ID/name header and page numbers on every page."""
    doc = pymupdf.open(pdf_path)
    total = doc.page_count
    for page in doc:
        width = pymupdf.get_text_length(header, fontname="helv", fontsize=9)
        page.insert_text(
            pymupdf.Point((page.rect.width - width) / 2, 24), header,
            fontname="helv", fontsize=9, color=(0.45, 0.45, 0.45), overlay=False,
        )
        footer = f"Page {page.number + 1} of {total}"
        fwidth = pymupdf.get_text_length(footer, fontname="helv", fontsize=9)
        page.insert_text(
            pymupdf.Point((page.rect.width - fwidth) / 2, page.rect.height - 18), footer,
            fontname="helv", fontsize=9, color=(0.45, 0.45, 0.45), overlay=False,
        )
    doc.save(pdf_path, incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
    doc.close()


def preview(pdf_path: pathlib.Path, out_dir: pathlib.Path, dpi: int = 90) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    for page in doc:
        page.get_pixmap(dpi=dpi).save(out_dir / f"page-{page.number + 1}.png")
    print(f"Rendered {doc.page_count} page(s) to {out_dir}")
    doc.close()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--preview", type=pathlib.Path, help="also render every page to this directory as PNG")
    args = ap.parse_args()

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORT_DIR / OUT_NAME

    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    html = md.render(SOURCE.read_text(encoding="utf-8"))
    font_config = FontConfiguration()
    weasyprint.HTML(string=html, base_url=str(BASE)).write_pdf(
        out, stylesheets=[weasyprint.CSS(string=FONT_FACES + CSS, font_config=font_config)],
        font_config=font_config,
    )
    stamp(out, f"{STUDENT_ID} {STUDENT_NAME}")
    doc = pymupdf.open(out)
    fonts = sorted({f[3].split("+")[-1] for page in doc for f in page.get_fonts()})
    if not any("Sarabun" in f for f in fonts):
        raise SystemExit(f"TH Sarabun was not embedded (fonts: {fonts}); check FONT_DIR / FontConfiguration")
    print(f"Wrote {out} ({doc.page_count} pages; fonts: {', '.join(fonts)})")
    if args.preview:
        preview(out, args.preview)


if __name__ == "__main__":
    main()
