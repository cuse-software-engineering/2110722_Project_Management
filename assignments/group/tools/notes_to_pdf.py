#!/usr/bin/env python3
"""Render a study-notes markdown file (with <figure> blocks) to an A4 PDF with WeasyPrint.

Images are shrunk to JPEG (max 1400 px wide) in $IMG_CACHE (default /tmp/md2pdf_cache) to keep the PDF small.
Requires: pip install markdown weasyprint pymupdf
Usage:    python3 tools/notes_to_pdf.py workspace/report/milestone2/m2-how-to-notes.md workspace/report/milestone2/m2-how-to-notes.pdf
"""
import sys, pathlib, markdown, weasyprint
src = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]).resolve()
body = markdown.markdown(src.read_text(), extensions=['tables', 'fenced_code', 'sane_lists', 'toc'])
css = """
@page { size: A4; margin: 16mm 14mm 18mm 14mm;
  @bottom-center { content: counter(page) " / " counter(pages); font-size: 8pt; color: #666; }
  @top-right { content: "CTRS · Milestone 2 how-to notes"; font-size: 8pt; color: #888; } }
body { font-family: 'DejaVu Sans', sans-serif; font-size: 8.6pt; line-height: 1.42; color: #1a1a1a; }
h1 { font-size: 17pt; color: #12355b; border-bottom: 2px solid #12355b; padding-bottom: 3pt; }
h2 { font-size: 13pt; color: #12355b; margin-top: 16pt; border-bottom: 1px solid #c8d3e0; padding-bottom: 2pt; page-break-after: avoid; }
h2:not(:first-of-type) { page-break-before: always; }
h3 { font-size: 10.5pt; color: #1f4e79; margin-top: 12pt; page-break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 8pt; font-size: 7.6pt; page-break-inside: auto; }
th, td { border: 1px solid #b7c3d0; padding: 2.5pt 4pt; vertical-align: top; text-align: left; }
th { background: #e8eef5; } tr { page-break-inside: avoid; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 7.6pt; background: #f2f4f7; padding: 0 2pt; }
pre { background: #f2f4f7; border: 1px solid #dde3ea; padding: 6pt; white-space: pre-wrap; font-size: 7.2pt; page-break-inside: avoid; }
pre code { background: none; padding: 0; }
a { color: #1f5fa8; text-decoration: none; }
hr { border: none; border-top: 1px solid #ccc; }
ul, ol { padding-left: 16pt; } li { margin: 1.5pt 0; }
.figs { margin: 6pt 0 10pt; }
.row { display: flex; gap: 8pt; margin-bottom: 6pt; page-break-inside: avoid; justify-content: center; }
.row figure { margin: 0; flex: 1 1 0; max-width: 72%; text-align: center; }
.row.two figure { max-width: 50%; }
.row figure img { width: 100%; border: 1px solid #c9d1db; }
.row:not(.two) img[data-src*="Pet_Care"] { width: 68%; }
figcaption { font-size: 7.2pt; color: #444; margin-top: 2pt; font-style: italic; }
"""
html = f'<html><head><meta charset="utf-8"><title>Milestone 2 how-to notes</title><style>{css}</style></head><body>{body}</body></html>'
import pymupdf, re, hashlib, os
cache = pathlib.Path(os.environ.get('IMG_CACHE', '/tmp/md2pdf_cache')); cache.mkdir(parents=True, exist_ok=True)
def shrink(m):
    p = (src.parent / m.group(1)).resolve()
    if p.suffix.lower() != '.png' or not p.exists(): return m.group(0)
    o = cache / (hashlib.md5(str(p).encode()).hexdigest() + '.jpg')
    if not o.exists():
        pix = pymupdf.Pixmap(str(p))
        if pix.alpha: pix = pymupdf.Pixmap(pix, 0)
        while pix.width > 1400: pix.shrink(1)
        pix.save(str(o), jpg_quality=72)
    return f'src="{o.as_uri()}" data-src="{m.group(1)}"'
html = re.sub(r'src="([^"]+)"', shrink, html)
html = html.replace('img[src*=\"Pet_Care\"]', 'img[data-src*=\"Pet_Care\"]')
weasyprint.HTML(string=html, base_url=str(src.parent)).write_pdf(out)
print('wrote', out, round(out.stat().st_size / 1e6, 1), 'MB')
