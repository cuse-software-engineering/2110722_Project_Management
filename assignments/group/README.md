# Group project: CTRS project-management report, 2110722 Software Project Management

Project-management report of the Concert Table Reservation System (CTRS), the same project that the team runs as a
tailored-RUP requirements project in the 2110628 repository (`assignments/group/` there). The PMBOK artifacts of this
course quote the RUP artifacts (`assignments/group/project/` of that repository) wherever they overlap and add what
those leave out (quantified financial analysis, schedule, risks, charter, organization).

One folder per kind of thing, as in the 2110628 repository. Generated files live only under `workspace/report/build/`
(ignored by git) until they are handed in, and then only in `deliverables/`.

| Path | What it is | Edit? |
|---|---|---|
| `problem/project_1_69-2311-17860377260714.pdf` / `.md` | The assignment brief and its markdown extraction. | no |
| `workspace/received/examples/2025_Pet_Care-2311-17856882876674.pdf` | Previous-year sample report used for the expected format; its page PNGs sit in the folder of the same name (ignored). | no |
| `workspace/report/milestone1/part2-final-deliverables.md` | **Source** of the Milestone 1 "Part 2 Final Deliverables" PDF: Review Board Decision Log, business case, financial analysis, project charter, organization chart. `<!-- include: … -->` blocks quote artifact sections of the 2110628 repository (same directive syntax as its group report; expanded in place, the quoted text between the markers is regenerated on every build, so edit the artifact, not the copy); `<!-- finance: … -->` blocks are generated from `tools/finance.py`. | yes (prose) |
| `workspace/report/milestone2/part2-final-deliverables.md` | **Source** of the Milestone 2 "Part 2 Final Deliverables" PDF (project renamed SEATS): Review Board Decision Log, scope statement, WBS and tasks, effort estimation, resource assignment and rates, cost estimate, schedule with Gantt chart and critical path. `<!-- plan: … -->` blocks are generated from `tools/plan.py`; merged on 15 Oct 2026 from the teammates' drafts in `workspace/received/examples/teammate_milestone_2/`. | yes (prose) |
| `workspace/report/milestone2/part1-genai-log.md` | Source of the Milestone 2 "Part 1 GenAI Log" PDF: the teammates' eight records in the Milestone 1 record format, final outputs quoted from Part 2 with `flat`. | yes |
| `workspace/report/milestone2/m2-how-to-notes.md` | Study notes on how to do each Milestone 2 section (lecture slides, PMBOK 7, the Pet Care sample); not part of the submission. | yes |
| `workspace/report/milestone1/part1-genai-log.md` | Source of the "Part 1 GenAI Log" PDF: one record per prompt, two per member, one record per page (`---` = page break). Each record is an HTML table (`table.rec`) whose cells hold markdown: the prompts name the material they were given, the initial output is a summary with an excerpt, and the final output is quoted from Part 2 with `flat`, so it regenerates on every build. Records 1 to 6 are drafted from the Review Board decisions; each member confirms their own tool, initial output and wording before submission. | yes |
| `workspace/report/assets/diagrams/` | Organization chart (`org-chart.html`, hand-laid HTML like the group report figures), schedule Gantt (`schedule-gantt.puml`) and development-process figure (`dev-process.html`). Render with `python3 <2110628 repo>/assignments/group/tools/render_diagrams.py <file>` (PNG next to the source). The PNGs are tracked because the report embeds them. | yes |
| `workspace/report/build/` | PDF and HTML output (ignored): `2110722_M1_part1_genai_log.pdf`, `2110722_M1_part2_final_deliverables.pdf`. | no |
| `tools/plan.py` | The Milestone 2 plan model: iterations and calendar, the 49 work packages with hours per engineer, dates, predecessors, owners, three-point estimates and other costs; computes the effort, RACI, load, cost, time-phased baseline, CPM and critical-path tables and renders the task-level Gantt chart (`assets/diagrams/schedule-tasks.svg/.png`). Checks that the totals per engineer, per year and per phase equal Milestone 1 (`--check`). | yes (plan) |
| `tools/finance.py` | The financial model (software-house view): plans, adoption, effort, costs, revenues, NPV / ROI / payback / IRR and sensitivity; every assumption is a named constant; prints the markdown tables. | yes (assumptions) |
| `tools/build_pm_report.py` | Expands the include and finance blocks and renders the PDFs with the 2110628 group report's builder (`assignments/group/tools/build_pdf.py` there: TH Sarabun, Chula header, TOC with page numbers) using the 2110722 cover and lecturer. Extra include attributes for quoted tables: `drop=<Header,…>` removes named columns, `keep=<i,j,…>` keeps 1-based columns in that order, `rename=<Old:New,…>` renames header cells, `split=<Header>` splits `<ID>: <text>` cells into an ID column and a text column (underscore = space in names); `flat` quotes an already expanded section of the Part 2 report as plain text (nested markers removed, headings and captions demoted, figures dropped with `no-images`), which is how the GenAI log records carry their final outputs. Part 2 is expanded before Part 1 for that reason. | rarely |
| `deliverables/report/` | What was handed in: the Milestone 1 PDFs as built on 2026-09-10. | only by copying a finished build |

Build (from this folder):

```
python3 tools/finance.py                  # print the financial tables and the key figures
python3 tools/build_pm_report.py          # expand blocks + both Milestone 1 PDFs into workspace/report/build/
python3 tools/build_pm_report.py --milestone 2   # the two Milestone 2 PDFs (plan tables regenerated, Gantt rendered)
python3 tools/plan.py --check             # verify the plan totals against Milestone 1; without --check print the tables
python3 tools/build_pm_report.py --no-pdf # expand blocks only
```

Hand-in: copy the finished PDF into `deliverables/report/` and commit it.

Dependency on the 2110628 repository: its RUP artifacts are quoted by the include blocks, and its report builder
(`assignments/group/tools/build_report.py`, `build_pdf.py`) and fonts (`resources/fonts/`) render the PDFs.
`tools/build_pm_report.py` finds it as `$REQ_REPO`, else the repository this one is nested in
(`<2110628>/workspace/2110722_Project_Management/`), else a sibling folder `2110628_Requirement`. Paths into it from
the milestone files (include targets, provenance comments, image links) are relative and re-pointed on every build to
wherever it was found. The diagram HTML sources load TH Sarabun from the absolute path
`file:///workspaces/2110628_Requirement/resources/fonts/`. While that repository is unreachable (checked 15 Oct 2026),
the sibling folder `../../../2110628_Requirement` is a stand-in that provides the builder and fonts only: the include
blocks that quote its RUP artifacts are left as already expanded (the build prints `keep …` for each), so edit those
quotations in the milestone file itself until the repository is back.

Conventions: English; captions `*Table N.n …*` above tables and `*Figure N.n …*` below figures (numbered per section);
identifiers of the RUP artifacts (P-nn, BR-nn, F-nn, ASM/CON-nn, NFR-nn, BRULE-nn) are kept so that the two courses'
documents cross-reference; new risk ids RISK-nn seed the RUP Risk List. Business model (owner decision 2026-09-10): the four members are engineers of one software house; CTRS is built for
La Loy under a pilot implementation agreement (Year 0 = 3 Aug 2026 – 30 Jul 2027, fee 150,000 THB), run for La Loy
alone in the pilot year while it is productized (Year 1, to 28 Jul 2028, expansion gate), then sold as a subscription
(Free / Standard 690 / Premium 990 THB a month, setup 2,500) to other restaurants (Years 2–5). The restaurant's own
benefits are not counted; figures in 2026 THB, discount rate 10 %, labor at the software house's cost rates.
