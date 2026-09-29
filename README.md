# 2110722 Software Project Management

การจัดการโครงการทางซอฟต์แวร์ — Department of Computer Engineering, Chula Engineering, Chulalongkorn University.

## Course Information

| | |
|---|---|
| **Course code** | 2110722 |
| **Course title** | SOFTWARE PROJECT MANAGEMENT (การจัดการโครงการทางซอฟต์แวร์) |
| **Short title** | S/W PROJ MGT |
| **Academic year** | 2026 / Semester 1 |
| **Sections** | 1 & 5 |

## Affiliation

- Department of Computer Engineering
- Chula Engineering
- Chulalongkorn University

## Staff

- **Instructor:** รศ. ดร. ทวิตีย์ เสนีวงศ์ ณ อยุธยา (Assoc. Prof. Dr. Twittie Senivongse)

## Course Description

แนวคิดของโครงการและการจัดการโครงการ การจัดการโครงการในบริบทของซอฟต์แวร์และเทคโนโลยีสารสนเทศ จริยธรรมในการจัดการโครงการ กลุ่มกระบวนการ หมวดองค์ความรู้ การจัดการการบูรณาการโครงการ การจัดการขอบเขต การจัดการกำหนดการ การจัดการต้นทุน การจัดการทรัพยากร การจัดการคุณภาพ การจัดการความเสี่ยง การจัดการการสื่อสาร การจัดการการจัดหา และการจัดการผู้มีส่วนได้เสีย (แก้ไข 1/66)

Concepts of project and project management; project management in software and IT contexts; ethics in project management; process groups; knowledge areas: project integration management, scope management, schedule management, cost management, resource management, quality management, risk management, communication management, procurement management, and stakeholder management. (adjust 1/66)

## Knowledge Areas Covered

1. Project integration management
2. Scope management
3. Schedule management
4. Cost management
5. Resource management
6. Quality management
7. Risk management
8. Communication management
9. Procurement management
10. Stakeholder management

## Student

- **Name:** Watayut Aiamanan
- **Student ID:** 6970267821

## Project Structure

Same layout as the 2110628 Requirements Engineering repository of the same student.

```
assignments/
  individual/<NN>/    Individual assignments (00 = personality, 01 = review questions, chapters 1 and 2, ...)
  group/              The term project: project-management report of CTRS (Concert Table Reservation System),
                      the project that 2110628 runs as a tailored RUP requirements project
    problem/          The project brief (.md + .pdf); read-only
    workspace/        The report, markdown-first: report/milestoneN/ sources + report/assets/ figures,
                      working builds in report/build/ (ignored); received/ = material received (sample report)
    tools/            Build scripts: financial model (finance.py) and report builder (build_pm_report.py)
    deliverables/     What was handed in: report/ (submitted PDFs per milestone)
materials/
  lecture_notes/<chapter>/   Lecture slide PDFs, with extracted md/ transcripts
tools/
  pdf_to_png.py              Generic, assignment-agnostic script: render any PDF's pages to PNG
```

Individual assignments follow a four-way split:

| Folder | Contents |
|---|---|
| `problem/` | The task as given: the original assignment brief/PDF, grading criteria. Read-only reference, never edited. |
| `workspace/` | Everything used to work toward the answer: drafts, notes, source diagrams, extracted material, raw photos. Messy is fine here. |
| `tools/` | Build scripts specific to that assignment. Scripts useful across *all* assignments live in the top-level `tools/` instead. |
| `report/` | Only the final deliverable(s) actually submitted, nothing else. |

The group project uses the same split once at `assignments/group/`, with `deliverables/` in place of `report/`
(see [assignments/group/README.md](assignments/group/README.md)). Its build reuses the report builder, fonts and
RUP artifacts of the 2110628 repository, which it looks up next to or around this one.

Raw source photos/screenshots and intermediate renders are gitignored; only the figures actually embedded in a report
are tracked (see `.gitignore`).
