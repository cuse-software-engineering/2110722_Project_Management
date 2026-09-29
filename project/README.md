# 2110722 Software Project Management — CTRS project report

Project-management report of the Concert Table Reservation System (CTRS), the same project that the team runs as a
tailored-RUP requirements project in `assignments/group/` for course 2110628. The PMBOK artifacts of this course
quote the RUP artifacts (`assignments/group/project/`) wherever they overlap and add what those leave out
(quantified financial analysis, schedule, risks, charter, organization).

| Path | What it is | Edit? |
|---|---|---|
| `project_1_69-2311-17860377260714.pdf` / `.md` | The assignment brief and its markdown extraction | No |
| `2025_Pet_Care-2311-17856882876674.pdf` (+ page PNGs in the folder of the same name, git-ignored) | Previous-year sample report used for the expected format | No |
| `milestone1/part2-final-deliverables.md` | **Source** of the Milestone 1 "Part 2 Final Deliverables" PDF: Review Board Decision Log, business case, financial analysis, project charter, organization chart. `<!-- include: … -->` blocks quote artifact sections (same directive syntax as the group report; expanded in place, the quoted text between the markers is regenerated on every build, so edit the artifact, not the copy); `<!-- finance: … -->` blocks are generated from `tools/finance.py`. | Yes (prose) |
| `milestone1/part1-genai-log.md` | Source of the "Part 1 GenAI Log" PDF: one record per prompt, two per member, one record per page (`---` = page break). Each record is an HTML table (`table.rec`) whose cells hold markdown: the prompts name the material they were given, the initial output is a summary with an excerpt, and the final output is quoted from Part 2 with `flat`, so it regenerates on every build. Records 1 to 6 are drafted from the Review Board decisions; each member confirms their own tool, initial output and wording before submission. | Yes |
| `tools/finance.py` | The financial model (software-house view): plans, adoption, effort, costs, revenues, NPV / ROI / payback / IRR and sensitivity; every assumption is a named constant; prints the markdown tables. | Yes (assumptions) |
| `tools/build_pm_report.py` | Expands the include and finance blocks and renders the PDFs with the group report's builder (`assignments/group/tools/build_pdf.py`: TH Sarabun, Chula header, TOC with page numbers) using the 2110722 cover and lecturer. Extra include attributes for quoted tables: `drop=<Header,…>` removes named columns, `keep=<i,j,…>` keeps 1-based columns in that order, `rename=<Old:New,…>` renames header cells, `split=<Header>` splits `<ID>: <text>` cells into an ID column and a text column (underscore = space in names); `flat` quotes an already expanded section of the Part 2 report as plain text (nested markers removed, headings and captions demoted, figures dropped with `no-images`), which is how the GenAI log records carry their final outputs. Part 2 is expanded before Part 1 for that reason. | Rarely |
| `assets/diagrams/` | Organization chart (`org-chart.html`, hand-laid HTML like the group report figures) and schedule Gantt (`schedule-gantt.puml`); and development-process figure (`dev-process.html`); render with `python3 assignments/group/tools/render_diagrams.py workspace/project-management/assets/diagrams/<file>` (PNG next to the source). The PNGs are not tracked (`*.png` is ignored): render all three before building the PDFs on a fresh checkout. | Yes |
| `build/` | PDF and HTML output (git-ignored): `2110722_M1_part1_genai_log.pdf`, `2110722_M1_part2_final_deliverables.pdf`. | No |

Build (from `workspace/project-management/`):

```
python3 tools/finance.py                  # print the financial tables and the key figures
python3 tools/build_pm_report.py          # expand blocks + both Milestone 1 PDFs into build/
python3 tools/build_pm_report.py --no-pdf # expand blocks only
```

Conventions: English; captions `*Table N.n …*` above tables and `*Figure N.n …*` below figures (numbered per section);
identifiers of the RUP artifacts (P-nn, BR-nn, F-nn, ASM/CON-nn, NFR-nn, BRULE-nn) are kept so that the two courses'
documents cross-reference; new risk ids RISK-nn seed the RUP Risk List. Business model (owner decision 2026-09-10): the four members are engineers of one software house; CTRS is built for
La Loy under a pilot implementation agreement (Year 0 = 3 Aug 2026 – 30 Jul 2027, fee 150,000 THB), run for La Loy
alone in the pilot year while it is productized (Year 1, to 28 Jul 2028, expansion gate), then sold as a subscription
(Free / Standard 690 / Premium 990 THB a month, setup 2,500) to other restaurants (Years 2–5). The restaurant's own
benefits are not counted; figures in 2026 THB, discount rate 10 %, labor at the software house's cost rates.
