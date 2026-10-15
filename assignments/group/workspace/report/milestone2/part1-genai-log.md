<!-- Source of the Milestone 2 "Part 1 GenAI Log file" PDF of course 2110722 Software Project Management.
     The eight records are the teammates' records (workspace/received/examples/teammate_milestone_2/
     SEATS_Generative_AI_Log.docx) in the format of the Milestone 1 log: prompt, initial output, review and revision
     as the members wrote them; only the identifiers (R1 to R7 became the feature identifiers of Milestone 1) and
     the section references were re-pointed to the merged Part 2, "6-workstream" became "workstream", and the final
     output of each record is quoted from Part 2 with the `flat` attribute, so it regenerates on every build.
     Each member confirms their own two records before submission. -->

# GenAI Log

This log records the prompts with which the members produced the Milestone 2 artifacts of the Seating & Event Availability Tracking System (SEATS) project for La Loy Restaurant, and how each initial output was evaluated and revised. Each member submits two prompt log records, one per page. The prompts of records 1 to 6 are written in the CREATE framework (Character, Request, Examples, Adjustments, Type of output, Evaluation), those of records 7 and 8 in the RTF framework (Role, Task, Format) because they were quick requests to an agent that already had the project files as context, and every output was evaluated against the three course criteria: requirement satisfaction, PMBOK correctness and project consistency, with the Milestone 1 report and with the other Milestone 2 artifacts. GenAI is used as an assistant rather than a project manager: every output is reviewed and, where needed, revised by the member, who remains responsible for the artifact.

All prompts draw on one single source of truth, the Milestone 1 Part 2 Final Deliverables (project dates, release scope, role rates, phase effort totals and budget), so that the independently generated artifacts stay mutually consistent; where the AI's output was a structure or a draft, the figures of the final tables were computed from the project's plan model, so that the WBS, effort, assignment, cost and schedule tables cannot contradict each other. Members prompted through their own tool: Boonnisa Tangjitpermkwamdee used ChatGPT (drafting assistance); Sirapatr Chalermwattanatrai used Google Gemini (gemini.google.com); Chawanakorn Sanannam used the OpenCode terminal CLI (opencode.ai) with the model "Big Pickle" (opencode/big-pickle); Watayut Aiamanan used Claude Code (Anthropic, model Claude Fable 5.1) inside the project repository, so that the model read the Milestone 1 sources, the drafts and the financial model directly and wrote its results into the report sources. Every record is linked to its row of the Review Board Decision Log (Part 2, Table 1.1).

*Table 0.1 Prompt log records of Milestone 2*

| Record | Artifact | Member (prompt design) | RUP role of the member and why the material is theirs | Artifact owner (RUP) | Framework |
|---|---|---|---|---|---|
| 1 | Scope statement and deliverables | Boonnisa T. | Project Manager and Change Control Manager: owns the scope baseline and the scope statement, so the scope wording and the deliverable categories are her responsibility | Project Manager | CREATE |
| 2 | Success criteria and budget baseline | Boonnisa T. | Project Manager and Change Control Manager: accountable for the cost baseline and the measurable success criteria agreed with the sponsor | Project Manager | CREATE |
| 3 | WBS and detailed schedule | Sirapatr C. | System Analyst and Software Architect: owns the decomposition of the requirements and architecture into work packages and the derivation of the task list from the RUP iterations | System Analyst / Software Architect | CREATE |
| 4 | Milestones and critical path | Sirapatr C. | System Analyst and Software Architect: derives the logical dependency chain and the critical path from the technical work packages and the RUP milestones | System Analyst / Software Architect | CREATE |
| 5 | Effort estimation for tasks | Chawanakorn S. | Requirements Specifier and Implementer: estimates the hours of the feature work he will build, so the estimates come from the person doing the work | Requirements Specifier | CREATE |
| 6 | WBS decomposition and features by release | Chawanakorn S. | Requirements Specifier and User-Interface Designer: turns the feature set into the deliverable-oriented decomposition and keeps each feature in exactly one release | Requirements Specifier | CREATE |
| 7 | Consistency review of the Milestone 2 drafts, quality requirements and verification | Watayut A. | Quality Assurance and Tester: reviews every artifact against the criteria and the single source of truth, and maps every quality target to an independent test | Quality Assurance / Test Designer | RTF |
| 8 | Cost estimate consistency and the plan model | Watayut A. | Quality Assurance and Tester: independently verifies that effort, assignment, cost and schedule agree with each other and with Milestone 1 | Quality Assurance / Test Designer | RTF |

---

## Record 1: Scope statement and deliverables

<table class="rec" markdown="1">
<tr markdown="1"><td class="k">1. Artifact</td><td markdown="block">

Project scope statement (Part 2, Section 2): project summary, product characteristics and requirements, project-management and product-related deliverables, exclusions and success criteria for Release 1.0 Core, Release 2.0 Growth and Release 2.1 productization.

</td></tr>
<tr markdown="1"><td class="k">2. Member</td><td markdown="block">

Boonnisa Tangjitpermkwamdee

</td></tr>
<tr markdown="1"><td class="k">3. AI Tool</td><td markdown="block">

ChatGPT (drafting assistance). The Milestone 1 report was supplied as the single source of truth.

</td></tr>
<tr markdown="1"><td class="k">4. Initial Prompt</td><td markdown="block">

**[character]** You are a project manager who owns the scope baseline.

**[request]** Using the SEATS report for La Loy Restaurant, draft a scope statement with project summary, product characteristics, project-management and product deliverables, exclusions and measurable success criteria.

**[examples]** Separate Release 1.0 Core, Release 2.0 Growth and Release 2.1 productization.

**[adjustments]** Do not invent requirements; keep the release boundaries of the source report.

**[type of output]** A scope statement table with a clear deliverable category column.

**[evaluation]** Every deliverable category must be distinct and the exclusions must be explicit.

</td></tr>
<tr markdown="1"><td class="k">5. Initial Output</td><td markdown="block">

The initial draft summarized booking, payment, QR check-in and staff functions, but did not clearly separate project-management, product and closure deliverables, and the exclusions were missing.

</td></tr>
<tr markdown="1"><td class="k">6. Review</td><td markdown="block">

Review Board row 1: the draft mixed product deliverables with project-management deliverables and did not clearly list exclusions. Requirement satisfaction was partial; PMBOK correctness required a single scope statement with explicit exclusions; project consistency required the release boundaries of the source report to be retained.

</td></tr>
<tr markdown="1"><td class="k">7. Revision</td><td markdown="block">

Asked for separate project-management and product deliverables, explicit exclusions and measurable, source-based success criteria. By hand, the product characteristics were restated with the feature identifiers F1 to F37 of Milestone 1 instead of the requirement labels the AI had invented, the closure deliverables were folded into the project-management deliverables as the brief's two categories ask, and the exclusions were tied to the Future features and the restaurant-paid items of Milestone 1.

</td></tr>
<tr markdown="1"><td class="k">8. Final Output</td><td markdown="block">

Part 2, Sections 2.1, 2.3 and 2.4, as delivered below (the feature table and the quality table are in Record 7 and Part 2, Section 2.2; the success criteria in Record 2). Acceptable because the deliverables are separated into the two categories of the brief, the exclusions are explicit and the release boundaries and dates are those of Milestone 1. Review Board decision: Revise; accepted after the revision.

**2.1 Project Summary**

<!-- include: part2-final-deliverables.md#2.1 Project Summary flat -->
<!-- source: part2-final-deliverables.md -->

SEATS is a LINE-integrated web application for reserving tables at La Loy Restaurant's live-music concerts. Customers use a LIFF web application opened from the Rich Menu of the restaurant's LINE Official Account to browse concert rounds, view a live table map, select a table, hold it for 15 minutes, pay the full table fee through a payment gateway and receive a QR e-ticket. Restaurant staff use a shared back-office to manage rounds, layouts and prices, watch the live booking view, handle exceptions and scan QR codes at the door. One central record replaces the chat, the hand-edited image and the notebook, so that double bookings and payment disputes disappear and the Manager handles exceptions only. After the build, the system is run through a pilot year at La Loy and productized as a multi-tenant subscription service for other live-music restaurants.

The project runs from 3 August 2026 to 28 July 2028 (two project years) under the tailored Rational Unified Process of the Development Case: Year 0 builds and deploys Release 1.0 Core (in operation 2 April 2027) and Release 2.0 Growth (30 July 2027); Year 1 runs the live pilot and delivers Release 2.1 Product (11 February 2028), and closes with the expansion decision of the software house on 28 July 2028. The project budget is 1,010,590 THB (charter, Table 4.1 of Milestone 1), of which La Loy's pilot implementation fee covers 150,000 THB. The scope statement, the WBS of Section 3 and the WBS dictionary of Section 3.3 form the scope baseline; changes to it go through the Change Control Board.

<!-- /include -->

**2.3 Project Deliverables**

<!-- include: part2-final-deliverables.md#2.3 Project Deliverables flat -->
<!-- source: part2-final-deliverables.md -->

**Table 2.3 Project deliverables**

| Category | Deliverables |
|---|---|
| Project-management deliverables | Business case with financial analysis, project charter, stakeholder list and project organization (Milestone 1); scope statement, WBS and WBS dictionary, effort, resource and cost estimates, schedule and cost baseline (this document); quality, risk and communication management plans (Milestone 3); Development Case and Software Development Plan; iteration plan and assessment of every iteration; weekly status assessments; change-request decisions of the Change Control Board; Risk List updates; milestone reviews (LCO, LCA, IOC, Product Release 1.0, 2.0 and 2.1); monthly pilot KPI reports; pilot review, expansion decision record, hand-over record, lessons learned and sign-off |
| Product-related deliverables | Requirements and design artifacts of the tailored RUP: Vision, Glossary, Stakeholder Requests, Business Rules, Domain Model, Use-Case Model and use-case specifications, Software Requirements Specification, Supplementary Specification, Analysis Model, Software Architecture Document, user-interface prototype, test plan and test cases; the tested increment of every Construction iteration; Release 1.0 Core in operation at La Loy (2 April 2027), Release 2.0 Growth (30 July 2027) and the productized Release 2.1 (11 February 2028); load-test, system-test and acceptance records; training and user guide for the Manager and the Front Staff; migration of the current bookings and, in Release 2.1, of La Loy to the productized service; production environment, support routine and Free-plan sign-up |

<!-- /include -->

**2.4 Exclusions**

<!-- include: part2-final-deliverables.md#2.4 Exclusions flat -->
<!-- source: part2-final-deliverables.md -->

- Split payment among the members of a party (F36) and table photos with distance to the stage (F37): Future candidates outside the project (Table 2.13 of Milestone 1).
- Restaurant-configurable booking rules beyond the rules agreed for the defined releases (hold, grace, transfer cut-off, waitlist, refund policy are fixed by the Owner's decisions before LCA).
- Payment-gateway fees, each restaurant's LINE Official Account plan and the pilot restaurant's own check-in tablet (about 9,000 THB): paid by the restaurant (CON-03, CON-07), not by the project budget.
- Sales, onboarding and operation of the subscription service for other restaurants after the expansion decision (Years 2 to 5 of the financial analysis): outside the project.
- Hardware at the venue beyond the test devices of the software house; any change to the restaurant's own LINE Official Account content.

<!-- /include -->

</td></tr>
</table>

---

## Record 2: Success criteria and budget baseline

<table class="rec" markdown="1">
<tr markdown="1"><td class="k">1. Artifact</td><td markdown="block">

Success criteria and budget baseline (Part 2, Sections 2.5 and 6): measurable targets with evidence, and the cost baseline (Year 0 767,690 THB; Year 1 242,900 THB; total 1,010,590 THB; labor 846,600 THB; contingency 88,490 THB; net investment 860,590 THB).

</td></tr>
<tr markdown="1"><td class="k">2. Member</td><td markdown="block">

Boonnisa Tangjitpermkwamdee

</td></tr>
<tr markdown="1"><td class="k">3. AI Tool</td><td markdown="block">

ChatGPT (drafting assistance). The budget and success-criteria figures of Milestone 1 were supplied as the single source of truth.

</td></tr>
<tr markdown="1"><td class="k">4. Initial Prompt</td><td markdown="block">

**[character]** You are a project manager checking measurable success criteria and a budget baseline.

**[request]** Check the SEATS success criteria and budget against the project period 3 Aug 2026 to 28 Jul 2028, total budget 1,010,590 THB, labor 846,600 THB, pilot fee 150,000 THB and net investment 860,590 THB.

**[examples]** Use source targets and flag values needing human verification.

**[adjustments]** Include numerical thresholds and evidence for each criterion.

**[type of output]** A criteria/evidence table plus a budget reconciliation summary.

**[evaluation]** Preserve the reported baseline figures and show how each target is verified.

</td></tr>
<tr markdown="1"><td class="k">5. Initial Output</td><td markdown="block">

The draft included general success criteria and the headline budget but did not explain how the targets would be verified or distinguish the source figures from assumptions.

</td></tr>
<tr markdown="1"><td class="k">6. Review</td><td markdown="block">

Review Board row 2: success measures needed numeric targets and evidence linked to the source report; the budget needed a transparent category split. PMBOK correctness: the cost baseline must reconcile.

</td></tr>
<tr markdown="1"><td class="k">7. Revision</td><td markdown="block">

Requested a criteria/evidence table and a clear distinction between source figures and assumptions, keeping the budget aligned with the source. By hand, the criteria were matched one-to-one with the seven criteria of the charter and the budget summary was replaced by the cost build-up from the work packages (Section 6), which reproduces the figures.

</td></tr>
<tr markdown="1"><td class="k">8. Final Output</td><td markdown="block">

Part 2, Section 2.5, as delivered below, and the cost reconciliation of Section 6.4 (quoted in Record 8). The criteria include booking within 3 minutes, a 35 % no-show reduction, at least 5 transactions a second, response within 2 seconds, check-in within 15 seconds per table and recovery within 2 hours, each with its evidence; the budget figures are retained and reproduced by the bottom-up cost baseline. Review Board decision: Accept.

**2.5 Project Success Criteria**

<!-- include: part2-final-deliverables.md#2.5 Project Success Criteria flat -->
<!-- source: part2-final-deliverables.md -->

The success criteria are the seven criteria of the charter (Table 4.1 of Milestone 1), each with the evidence that shows it is met (Table 2.4). They are also the acceptance criteria of the major deliverables: Release 1.0 is accepted when criteria 2, 3, 5 and 6 are shown on the pilot nights of T1; Release 2.0 when the acceptance tests of F29 to F35 pass; Release 2.1 when La Loy runs on the productized service and the per-shop cost assumption holds.

**Table 2.4 Success criteria and evidence**

| No. | Success criterion (charter) | Target / evidence |
|---|---|---|
| 1 | Release milestones within budget | Release 1.0 Core in operation at La Loy on 2 April 2027, Release 2.0 Growth on 30 July 2027, Release 2.1 on 11 February 2028; cost at close-out within the project budget of 1,010,590 THB (go-live records, iteration assessments, cost baseline of Section 6) |
| 2 | Booking integrity | Zero double bookings on La Loy's concert nights after go-live; table status real-time on one record (audit trail and pilot KPI reports) |
| 3 | Customer experience | A booking completed within 3 minutes from table selection to confirmation, without a Manager reply (timestamps of the booking record; sample of pilot nights) |
| 4 | Business outcome | No-show rate at La Loy reduced by 35 % within six months of Release 2.0, against the baseline of Table 2.2 of Milestone 1 (check-in records versus bookings) |
| 5 | Operational quality and cost | Check-in within 15 seconds per table; at least 5 transactions a second at booking-open time; response within 2 seconds; recovery within 2 hours; the restaurant's hosting, APIs and LINE plan at or below 1,000 THB a month (Table 2.2 tests; monthly cost review) |
| 6 | Requirements and acceptance | Vision approved by the Owner at LCO, SRS signed off at LCA, acceptance tests of the two main use cases (reserve a concert table, check in with e-ticket) passed with the Manager and the Front Staff (milestone review and acceptance records) |
| 7 | Expansion gate | At the expansion decision: La Loy continues on a paid plan, at least 10 restaurants are on the waiting list, and the per-shop hosting and support cost of the productized service is at or below the assumptions of Table 3.3 of Milestone 1 (pilot review, waiting list, cost report) |

<!-- /include -->

</td></tr>
</table>

---

## Record 3: WBS and detailed schedule

<table class="rec" markdown="1">
<tr markdown="1"><td class="k">1. Artifact</td><td markdown="block">

Work breakdown structure and activity list (Part 2, Sections 3.1 and 3.2): the WBS decomposed to work packages as deliverable-oriented noun phrases, mapped to the ten tailored RUP iterations I1 to T3, and the activity list with WBS ID, activity, duration, predecessors, start, finish and resources.

</td></tr>
<tr markdown="1"><td class="k">2. Member</td><td markdown="block">

Sirapatr Chalermwattanatrai

</td></tr>
<tr markdown="1"><td class="k">3. AI Tool</td><td markdown="block">

Google Gemini (gemini.google.com). The Milestone 1 baseline (requirements, the ten RUP iterations and the WBS workstreams) was pasted as the single source of truth.

</td></tr>
<tr markdown="1"><td class="k">4. Initial Prompt</td><td markdown="block">

**[character]** You are a system analyst building a PMBOK-compliant WBS.

**[request]** Make a workstream WBS for SEATS decomposed down to two levels, then convert it into a detailed schedule table with WBS ID, Task, Responsible Role, Duration, Predecessor(s), Start, Finish and Expected Output/Milestone Measure.

**[examples]** Align the iteration dates with the SEATS M1 baseline I1 to T3.

**[adjustments]** Make every task label a 100 % deliverable-oriented noun phrase rather than a verb action, and label estimated task-level durations as estimates.

**[type of output]** A workstream outline plus a schedule-style WBS table.

**[evaluation]** Every task must be a noun phrase with an owner, dates, dependencies and an output measure, and the source iteration dates must be preserved.

</td></tr>
<tr markdown="1"><td class="k">5. Initial Output</td><td markdown="block">

The first WBS was phase-based but several task labels were verb actions (for example "Build table map") and the schedule fields and dependencies were missing.

</td></tr>
<tr markdown="1"><td class="k">6. Review</td><td markdown="block">

Review Board row 3: the WBS was not 100 % deliverable-oriented and lacked schedule-table columns and clear task dependencies. PMBOK correctness: a WBS needs noun-phrase work packages and a schedule format needs duration, predecessor and output columns; project consistency required the source iteration dates to be preserved.

</td></tr>
<tr markdown="1"><td class="k">7. Revision</td><td markdown="block">

Re-decomposed the workstreams to two levels with noun-phrase work packages and added the schedule columns (WBS ID, Task, Responsible Role, Duration, Predecessors, Start, Finish, Expected Output), preserving the source dates. By hand, the work packages were taken one level further (49 work packages in eight branches, the features F1 to F35 placed each in exactly one package) and the dates, predecessors and resource units of every activity were computed in the project's plan model inside the iteration windows, with the year-end break of Milestone 1, because the AI's dates had ignored it.

</td></tr>
<tr markdown="1"><td class="k">8. Final Output</td><td markdown="block">

Part 2, Sections 3.1 and 3.2, as delivered below: the WBS as a deliverable-oriented outline and the activity list with owners, dates, dependencies, resources and outputs, keeping the iteration dates of Milestone 1. Review Board decision: Revise; accepted after the revision.

**3.1 Work Breakdown Structure**

<!-- include: part2-final-deliverables.md#3.1 Work Breakdown Structure flat -->
<!-- source: part2-final-deliverables.md -->

The WBS (Table 3.1) is a deliverable-oriented decomposition of the total scope: level 1 is the project, level 2 the eight branches (project management, the phases of the tailored RUP by release, the pilot operation), level 3 the 49 work packages, named as nouns. It follows the rules of the course: every unit of work appears in exactly one work package (100 % rule, checked for F1 to F35 and the Release 2.1 items), the work of a branch is the sum of its work packages, each work package has one accountable engineer (Table 5.2), each is described in the WBS dictionary (Section 3.3, two entries printed), and the structure matches how the work is performed, by iteration. Project management is one branch that runs through all phases, so that the Project Manager's status assessments, iteration assessments, change control, milestone reviews, pilot KPI reports and close-out are visible as work of their own. The pilot support of the restaurant (7.1) is in the WBS because it is work of the project team, but its hours are operating expenditure of Year 1 in the financial analysis (Table 3.6 of Milestone 1), not development effort. Work packages are planned in detail up to Release 2.0; the productization iterations (C4, T3) and the pilot year are planned at work-package level only and will be detailed before C4 (rolling wave planning).


| WBS ID | Work package | Iteration | Features / content | Deliverable (expected output) |
|---|---|---|---|---|
| **1** | **Project Management** |  |  | *project management (runs through all phases)* |
| 1.1 | Project plans and baselines | I1, I2 | Milestone 1 artifacts | Business Case, charter, organization chart, SDP (draft), iteration plans |
| 1.2 | Risk List and Development Case | I1, I2 | Process tailoring, risks | Development Case v1, Risk List |
| 1.3 | Iteration assessments and change control, Elaboration | E1, E2 | Monitoring and control | Status assessments, iteration assessments, change-request decisions |
| 1.4 | Iteration assessments and change control, Release 1.0 Construction | C1, C2 | Monitoring and control | Status assessments, iteration assessments, change-request decisions, Risk List updates |
| 1.5 | Iteration assessments and change control, Release 1.0 Transition | T1 | Monitoring and control | Status assessments, go-live record |
| 1.6 | Iteration assessments and change control, Release 2.0 | C3, T2 | Monitoring and control | Status assessments, iteration assessments, change-request decisions |
| 1.7 | Iteration assessments and change control, Release 2.1 | C4, T3 | Monitoring and control | Status assessments, iteration assessments, change-request decisions |
| 1.8 | Pilot KPI reports and reviews | P1 | Pilot KPIs | Monthly pilot KPI reports, waiting list of restaurants |
| 1.9 | Pilot review, expansion decision and close-out | CL | Closing | Pilot review, expansion decision record, hand-over record, lessons learned, sign-off |
| **2** | **Inception (I1, I2)** |  |  | *Vision, use-case model, LCO* |
| 2.1 | Stakeholder requests and problem analysis | I1 | P-01 to P-06, RC-01 to RC-07 | Stakeholder Requests, problem and root-cause tables (workshop of RISK-01) |
| 2.2 | Vision and Glossary | I1, I2 | F1 to F37 | Vision v1, Glossary |
| 2.3 | Use-case model and release plan | I2 | Release 1.0: F1 to F28; Release 2.0: F29 to F35; Future: F36, F37 | Use-Case Model (outline), release plan |
| 2.4 | Review records and LCO package | I2 | LCO | Review Records, LCO decision |
| **3** | **Elaboration (E1, E2)** |  |  | *requirements, architecture, prototype, test plan, LCA* |
| 3.1 | Use-case specifications | E1 | F2 to F8, F15 to F20 | Use-case specifications |
| 3.2 | Software Requirements Specification and Supplementary Specification | E1, E2 | F1 to F35, NFR | SRS, Supplementary Specification |
| 3.3 | Analysis model and Software Architecture Document | E2 | Table 2.12 components | Analysis Model, SAD |
| 3.4 | User-interface prototype | E2 | Customer and back-office screens | UI prototype, trial records |
| 3.5 | Payment gateway and LINE sandbox | E2 | CON-07, RISK-03 | Sandbox accounts, onboarding checks, feasibility record |
| 3.6 | Test plan and test cases | E2 | Table 2.19 targets | Test plan, test cases, load-test design |
| 3.7 | Requirements reviews, SRS baseline and LCA package | E2 | LCA | Review Records, SRS baseline, LCA decision |
| 3.8 | Scope baseline, estimates, schedule and cost baseline | E2 | Milestone 2 artifacts | Scope statement, WBS, estimates, schedule and cost baseline, Construction plan |
| **4** | **Release 1.0 Core: Construction (C1, C2)** |  |  | *features F1 to F28, IOC* |
| 4.1 | Concert rounds, zones and packages | C1 | F10, F11 | Back-office round and layout functions, unit tests |
| 4.2 | Table map, selection and hold | C1 | F2, F3, F9, F21 | Customer table map and hold, first-lock-wins locking |
| 4.3 | Gateway payment and callback | C1 | F4, F7, F23 | Payment flow with automatic confirmation |
| 4.4 | LINE sign-in, staff accounts and role access | C1 | F1, F24 | Sign-in and staff accounts |
| 4.5 | C1 integration and iteration test | C1 | C1 increment | Tested C1 increment, iteration assessment |
| 4.6 | QR e-ticket and transactional messages | C2 | F5, F6, F8 | E-ticket and messages |
| 4.7 | Door check-in and name lookup | C2 | F15 to F20 | Front Staff check-in functions |
| 4.8 | Live booking view and exception handling | C2 | F12, F13, F14, F27 | Manager's live view and exception functions |
| 4.9 | Audit trail, backup, consent and push budget | C2 | F22, F25, F26, F28 | System functions of Release 1.0 |
| 4.10 | Load test, system test and IOC package | C2 | Release 1.0, Table 2.19 targets | Load-test and system-test records, IOC decision |
| **5** | **Release 1.0 Core: Transition (T1)** |  |  | *acceptance, training, migration, go-live* |
| 5.1 | Acceptance tests of Release 1.0 | T1 | Acceptance criteria of the charter | Acceptance records |
| 5.2 | Training and user guide | T1 | Back-office and check-in | Training records, user guide |
| 5.3 | Production set-up and data migration | T1 | Current bookings, production environment | Production system, migrated data |
| 5.4 | Pilot concert nights and go-live of Release 1.0 | T1 | Release 1.0 Core | Go-live record, Release 1.0 in operation |
| **6** | **Release 2.0 Growth (C3, T2)** |  |  | *features F29 to F35, go-live* |
| 6.1 | Scheduled reminders | C3 | F32, F34 | Reminder functions |
| 6.2 | Grace extension and waitlist | C3 | F29, F30, F35 | Grace and waitlist functions |
| 6.3 | Booking transfer | C3 | F31 | Transfer function |
| 6.4 | Reports and Excel export | C3 | F33 | Reports |
| 6.5 | C3 integration and system test | C3 | Release 2.0 | Tested Release 2.0, iteration assessment |
| 6.6 | Acceptance tests and training on Release 2.0 | T2 | F29 to F35 | Acceptance and training records |
| 6.7 | Release 2.0 deployment and first concert nights | T2 | Release 2.0 Growth | Go-live record, Release 2.0 in operation, pilot year begins |
| **7** | **Pilot operation (P1)** |  |  | *concert-night support* |
| 7.1 | Concert-night support and maintenance | P1 | RISK-04 support routine | Support log, maintenance releases |
| **8** | **Release 2.1 Product (C4, T3)** |  |  | *productization, migration of La Loy* |
| 8.1 | Multi-tenant data model and tenant isolation | C4 | Release 2.1 scope (Section 3.1 of Milestone 1) | Multi-tenant core |
| 8.2 | Plans, limits and tier enforcement | C4 | Table 3.1 of Milestone 1 | Plan and limit functions |
| 8.3 | Subscription billing and company set-up | C4 | Billing, legal set-up | Billing functions, company registration, legal documents |
| 8.4 | Self-service onboarding and service administration | C4 | Onboarding, administration | Onboarding and administration functions |
| 8.5 | Security, load and integration test of Release 2.1 | C4 | Release 2.1 | Test records, iteration assessment |
| 8.6 | Migration of La Loy and release of the Free-plan sign-up | T3 | Release 2.1 Product | La Loy on the productized service, Release 2.1 in operation |


**Table 3.1 Work breakdown structure of the SEATS project**

<!-- /include -->

**3.2 Activity List and Milestones**

<!-- include: part2-final-deliverables.md#3.2 Activity List and Milestones flat -->
<!-- source: part2-final-deliverables.md -->

Each work package is carried out by one activity (verb phrase) with a duration in working days, a start and finish inside the iteration dates of Milestone 1 (Table 2.21), its predecessors (finish-to-start unless marked SS, start-to-start, or FF, finish-to-finish) and the engineers assigned with their units, where 100 % is 8 hours a day (Table 3.2). The seven milestones have zero duration and the dates of the charter. The working-day calendar is Monday to Friday with the year-end break of 21 December 2026 to 1 January 2027 between C1 and C2; Thai public holidays are absorbed by the part-time allocation.


| WBS ID | Activity | Duration (working days) | Start | Finish | Predecessors | Resources (units) |
|---|---|---|---|---|---|---|
| **1** | **Project Management** |  |  |  |  |  |
| 1.1 | Produce the business case, the project charter, the organization, the Software Development Plan and the iteration plans I1 and I2 | 23 | 3 Aug 2026 | 2 Sep 2026 | — | Boonnisa T. 11 % |
| 1.2 | Write the initial Risk List (RISK-01 to RISK-14) and the Development Case that tailors RUP for the project | 18 | 10 Aug 2026 | 2 Sep 2026 | 2.1 SS | Boonnisa T. 3 %, Watayut A. 6 % |
| 1.3 | Run the weekly status assessments, the E1 and E2 iteration assessments and the Change Control Board | 37 | 3 Sep 2026 | 23 Oct 2026 | 1.1 | Boonnisa T. 9 % |
| 1.4 | Run the weekly status assessments, the C1 and C2 iteration assessments and the Change Control Board | 80 | 26 Oct 2026 | 26 Feb 2027 | 1.3 | Boonnisa T. 10 % |
| 1.5 | Run the weekly status assessments, the T1 assessment and the Change Control Board | 25 | 1 Mar 2027 | 2 Apr 2027 | 1.4 | Boonnisa T. 6 % |
| 1.6 | Run the weekly status assessments, the C3 and T2 iteration assessments and the Change Control Board | 85 | 5 Apr 2027 | 30 Jul 2027 | 1.5 | Boonnisa T. 7 % |
| 1.7 | Run the status assessments, the C4 and T3 iteration assessments and the Change Control Board | 140 | 2 Aug 2027 | 11 Feb 2028 | 1.6 | Boonnisa T. 2 % |
| 1.8 | Collect the pilot KPIs of every concert night (booking time, double bookings, no-shows, check-in time, operating cost) and review them monthly with the Owner | 255 | 2 Aug 2027 | 21 Jul 2028 | 6.7 | Boonnisa T. 1 %, Watayut A. 0 % |
| 1.9 | Review the pilot year against the success criteria of the charter, prepare the expansion decision, record lessons learned and obtain sign-off | 5 | 24 Jul 2028 | 28 Jul 2028 | 1.8 FF, 8.6 | Boonnisa T. 20 %, Sirapatr C. 10 %, Watayut A. 10 % |
| **2** | **Inception (I1, I2)** |  |  |  |  |  |
| 2.1 | Interview the Owner and the Manager, observe concert nights, record the stakeholder requests, the problems and their root causes (5 Whys) | 15 | 3 Aug 2026 | 21 Aug 2026 | — | Boonnisa T. 3 %, Sirapatr C. 13 %, Chawanakorn S. 7 % |
| 2.2 | Write the Vision (problem statement, stakeholders, features F1 to F37 with value, cost and priority) and the Glossary | 18 | 10 Aug 2026 | 2 Sep 2026 | 2.1 SS | Sirapatr C. 14 %, Chawanakorn S. 8 % |
| 2.3 | Outline the use-case model and assign the features to Release 1.0, Release 2.0 and Future | 7 | 25 Aug 2026 | 2 Sep 2026 | 2.2 SS | Sirapatr C. 7 %, Chawanakorn S. 21 %, Watayut A. 7 % |
| 2.4 | Review the Inception artifacts against the RUP checkpoints, record the Review Records and assemble the LCO review | 5 | 27 Aug 2026 | 2 Sep 2026 | 2.2 SS, 2.3 SS | Boonnisa T. 10 %, Watayut A. 30 % |
| **3** | **Elaboration (E1, E2)** |  |  |  |  |  |
| 3.1 | Specify the two main use cases, Reserve a concert table and Check in with e-ticket, with the Manager and the Front Staff | 10 | 3 Sep 2026 | 16 Sep 2026 | 2.4 | Sirapatr C. 20 %, Chawanakorn S. 40 %, Watayut A. 5 % |
| 3.2 | Write the SRS and the Supplementary Specification with the quality targets of Table 2.19 of Milestone 1 | 22 | 10 Sep 2026 | 9 Oct 2026 | 3.1 SS | Boonnisa T. 2 %, Sirapatr C. 7 %, Chawanakorn S. 16 %, Watayut A. 5 % |
| 3.3 | Produce the analysis model and the Software Architecture Document (LIFF front end, back office, application server, central database, LINE and gateway integration) | 22 | 17 Sep 2026 | 16 Oct 2026 | 3.1 | Boonnisa T. 2 %, Sirapatr C. 27 %, Chawanakorn S. 5 % |
| 3.4 | Prototype the customer and back-office screens and have the Manager, the Front Staff and sample customers try them | 17 | 24 Sep 2026 | 16 Oct 2026 | 3.1 | Sirapatr C. 3 %, Chawanakorn S. 18 %, Watayut A. 3 % |
| 3.5 | Open the gateway sandbox and the LINE Developers channel, verify the merchant onboarding and the LIFF and Messaging API settings (RISK-03, external dependency) | 17 | 17 Sep 2026 | 9 Oct 2026 | 2.4 | Boonnisa T. 6 %, Sirapatr C. 9 %, Chawanakorn S. 3 % |
| 3.6 | Write the test plan and the test cases of the two main use cases, including the load-test design for 5 transactions a second (RISK-05) | 22 | 24 Sep 2026 | 23 Oct 2026 | 3.1 | Boonnisa T. 2 %, Watayut A. 18 % |
| 3.7 | Review the SRS, the SAD, the prototype and the test plan against the checkpoints, baseline the SRS and assemble the LCA review | 10 | 12 Oct 2026 | 23 Oct 2026 | 3.2, 3.3 SS, 3.4 SS, 3.6 SS | Boonnisa T. 10 %, Sirapatr C. 5 %, Watayut A. 20 % |
| 3.8 | Produce the scope statement, the WBS and dictionary, the effort, resource and cost estimates, the schedule and cost baseline (this document) and the Construction plan | 10 | 12 Oct 2026 | 23 Oct 2026 | 3.2 SS | Boonnisa T. 10 % |
| **4** | **Release 1.0 Core: Construction (C1, C2)** |  |  |  |  |  |
| 4.1 | Design, implement and unit-test the management of concert rounds, zones, table types, packages and prices | 15 | 26 Oct 2026 | 13 Nov 2026 | 3.7 | Boonnisa T. 7 %, Sirapatr C. 13 %, Chawanakorn S. 27 %, Watayut A. 7 % |
| 4.2 | Implement the round list, the real-time table map, the table selection with the 15-minute hold and the automatic hold release | 20 | 2 Nov 2026 | 27 Nov 2026 | 4.1 SS | Boonnisa T. 5 %, Sirapatr C. 20 %, Chawanakorn S. 22 %, Watayut A. 10 % |
| 4.3 | Integrate the hosted checkout, the booking terms, the payment webhook and the automatic confirmation of the booking | 25 | 16 Nov 2026 | 18 Dec 2026 | 3.5, 4.2 SS | Boonnisa T. 4 %, Sirapatr C. 20 %, Chawanakorn S. 16 %, Watayut A. 12 % |
| 4.4 | Implement LINE Login, the back-office accounts and the role-based access of Manager, Front Staff and Owner | 15 | 16 Nov 2026 | 4 Dec 2026 | 3.7 | Sirapatr C. 13 %, Chawanakorn S. 13 %, Watayut A. 7 % |
| 4.5 | Integrate the C1 increment, run the iteration tests and the C1 assessment | 10 | 7 Dec 2026 | 18 Dec 2026 | 4.1, 4.2, 4.3 SS, 4.4 | Boonnisa T. 10 %, Sirapatr C. 10 %, Chawanakorn S. 10 %, Watayut A. 30 % |
| 4.6 | Implement the QR e-ticket, the customer's booking list and the transactional LINE messages | 15 | 4 Jan 2027 | 22 Jan 2027 | 4.5 | Sirapatr C. 13 %, Chawanakorn S. 27 %, Watayut A. 7 % |
| 4.7 | Implement the QR scan, the ticket details, the check-in, the invalid-ticket escalation, the no-show release and the name lookup | 20 | 11 Jan 2027 | 5 Feb 2027 | 4.6 SS | Boonnisa T. 5 %, Sirapatr C. 10 %, Chawanakorn S. 20 %, Watayut A. 10 % |
| 4.8 | Implement the live booking view, the ticket escalation, the manual overrides and the degraded-mode switch | 20 | 18 Jan 2027 | 12 Feb 2027 | 4.6 | Boonnisa T. 5 %, Sirapatr C. 20 %, Chawanakorn S. 20 %, Watayut A. 10 % |
| 4.9 | Implement the audit trail, the daily backup with Excel export, the consent and profile access and the push-message budget | 15 | 25 Jan 2027 | 12 Feb 2027 | 4.6 | Boonnisa T. 7 %, Sirapatr C. 13 %, Chawanakorn S. 17 %, Watayut A. 7 % |
| 4.10 | Run the load test (5 transactions a second at booking-open time), the system test of Release 1.0 and assemble the IOC review | 15 | 8 Feb 2027 | 26 Feb 2027 | 4.7, 4.8, 4.9 | Boonnisa T. 7 %, Sirapatr C. 27 %, Chawanakorn S. 13 %, Watayut A. 53 % |
| **5** | **Release 1.0 Core: Transition (T1)** |  |  |  |  |  |
| 5.1 | Run the acceptance tests of the two main use cases with the Manager and the Front Staff | 10 | 1 Mar 2027 | 12 Mar 2027 | 4.10 | Boonnisa T. 10 %, Sirapatr C. 10 %, Chawanakorn S. 15 %, Watayut A. 35 % |
| 5.2 | Train the Manager and the Front Staff and hand over the user guide | 10 | 8 Mar 2027 | 19 Mar 2027 | 5.1 SS | Boonnisa T. 10 %, Chawanakorn S. 20 %, Watayut A. 5 % |
| 5.3 | Set up the production hosting, the domain and the gateway merchant account of La Loy, and migrate the current bookings | 10 | 15 Mar 2027 | 26 Mar 2027 | 5.1 | Sirapatr C. 30 %, Chawanakorn S. 12 %, Watayut A. 10 % |
| 5.4 | Support the first concert nights on site, fix the defects found and declare Release 1.0 in operation | 10 | 22 Mar 2027 | 2 Apr 2027 | 5.2, 5.3 | Boonnisa T. 15 %, Sirapatr C. 10 %, Chawanakorn S. 15 %, Watayut A. 25 % |
| **6** | **Release 2.0 Growth (C3, T2)** |  |  |  |  |  |
| 6.1 | Implement the reminder scheduling and the scheduled LINE reminders within the push-message budget | 25 | 5 Apr 2027 | 7 May 2027 | 5.4 | Boonnisa T. 4 %, Sirapatr C. 16 %, Chawanakorn S. 20 %, Watayut A. 10 % |
| 6.2 | Implement the grace extension, the waitlist and the waitlist offer (rules decided by the Owner, RISK-08) | 30 | 26 Apr 2027 | 4 Jun 2027 | 6.1 SS | Boonnisa T. 3 %, Sirapatr C. 17 %, Chawanakorn S. 20 %, Watayut A. 12 % |
| 6.3 | Implement the official transfer of a confirmed booking to another LINE account | 15 | 17 May 2027 | 4 Jun 2027 | 6.1 | Sirapatr C. 13 %, Chawanakorn S. 20 %, Watayut A. 10 % |
| 6.4 | Implement the booking, revenue, artist-popularity and customer-history reports with export to Excel | 20 | 24 May 2027 | 18 Jun 2027 | 6.1 | Boonnisa T. 5 %, Sirapatr C. 15 %, Chawanakorn S. 20 %, Watayut A. 10 % |
| 6.5 | Integrate Release 2.0, run the regression and system tests and the C3 assessment | 15 | 7 Jun 2027 | 25 Jun 2027 | 6.2, 6.3, 6.4 | Boonnisa T. 10 %, Sirapatr C. 27 %, Chawanakorn S. 20 %, Watayut A. 37 % |
| 6.6 | Run the acceptance tests of the new features with the Manager and train the staff on them | 15 | 28 Jun 2027 | 16 Jul 2027 | 6.5 | Boonnisa T. 7 %, Sirapatr C. 12 %, Chawanakorn S. 20 %, Watayut A. 25 % |
| 6.7 | Deploy Release 2.0, support the first concert nights and declare Release 2.0 in operation | 15 | 12 Jul 2027 | 30 Jul 2027 | 6.6 SS | Boonnisa T. 10 %, Sirapatr C. 13 %, Chawanakorn S. 13 %, Watayut A. 17 % |
| **7** | **Pilot operation (P1)** |  |  |  |  |  |
| 7.1 | Support the pilot restaurant on concert nights (on-call engineer) and maintain the system: 8 hours a month, costed as operating expenditure of Year 1 in Milestone 1 (Table 3.6), outside the 2,632 development hours | 260 | 2 Aug 2027 | 28 Jul 2028 | 6.7 | Chawanakorn S. 2 %, Watayut A. 2 % |
| **8** | **Release 2.1 Product (C4, T3)** |  |  |  |  |  |
| 8.1 | Design and implement the multi-tenant data model, the tenant isolation and the migration path of La Loy's data | 40 | 2 Aug 2027 | 24 Sep 2027 | 6.7 | Sirapatr C. 12 %, Chawanakorn S. 12 %, Watayut A. 5 % |
| 8.2 | Implement the Free, Standard and Premium plans, their limits and the automatic enforcement of the limits | 30 | 20 Sep 2027 | 29 Oct 2027 | 8.1 | Sirapatr C. 8 %, Chawanakorn S. 17 %, Watayut A. 8 % |
| 8.3 | Implement the subscription billing and the setup-fee invoicing; register the company and publish the terms of service, privacy policy and data-processing agreement | 30 | 25 Oct 2027 | 3 Dec 2027 | 8.2 SS | Boonnisa T. 3 %, Sirapatr C. 10 %, Chawanakorn S. 17 %, Watayut A. 10 % |
| 8.4 | Implement the self-service onboarding of a restaurant (zone map, packages, gateway and LINE set-up) and the service administration console | 30 | 15 Nov 2027 | 24 Dec 2027 | 8.2 | Sirapatr C. 8 %, Chawanakorn S. 17 %, Watayut A. 8 % |
| 8.5 | Run the multi-tenant security test, the load test and the system test of Release 2.1 and the C4 assessment | 25 | 13 Dec 2027 | 14 Jan 2028 | 8.3, 8.4 SS | Boonnisa T. 4 %, Sirapatr C. 6 %, Chawanakorn S. 10 %, Watayut A. 14 % |
| 8.6 | Migrate La Loy to the productized service, release the Free-plan sign-up and hand over to the support routine | 20 | 17 Jan 2028 | 11 Feb 2028 | 8.5 | Boonnisa T. 2 %, Sirapatr C. 8 %, Chawanakorn S. 12 %, Watayut A. 12 % |
| M1 | *LCO: Lifecycle Objectives* | 0 | 2 Sep 2026 | 2 Sep 2026 | 2.4 | — |
| M2 | *LCA: Lifecycle Architecture, SRS baseline* | 0 | 23 Oct 2026 | 23 Oct 2026 | 3.7 | — |
| M3 | *IOC: Initial Operational Capability* | 0 | 26 Feb 2027 | 26 Feb 2027 | 4.10 | — |
| M4 | *Release 1.0 Core in operation* | 0 | 2 Apr 2027 | 2 Apr 2027 | 5.4 | — |
| M5 | *Release 2.0 Growth in operation* | 0 | 30 Jul 2027 | 30 Jul 2027 | 6.7 | — |
| M6 | *Release 2.1 in operation* | 0 | 11 Feb 2028 | 11 Feb 2028 | 8.6 | — |
| M7 | *Expansion decision, project closed* | 0 | 28 Jul 2028 | 28 Jul 2028 | 1.9 | — |


**Table 3.2 Activity list with duration, dates, predecessors and resources**

<!-- /include -->

</td></tr>
</table>

---

## Record 4: Milestones and critical path

<table class="rec" markdown="1">
<tr markdown="1"><td class="k">1. Artifact</td><td markdown="block">

Schedule, milestone log and critical path (Part 2, Section 7): the Gantt chart of the project from August 2026 to July 2028 aligned to the ten RUP iterations, the milestone log (LCO, LCA, IOC, Release 1.0, Release 2.0, Release 2.1, expansion decision of 28 July 2028) and the float-based critical-path analysis (TS = LS − ES = LF − EF).

</td></tr>
<tr markdown="1"><td class="k">2. Member</td><td markdown="block">

Sirapatr Chalermwattanatrai

</td></tr>
<tr markdown="1"><td class="k">3. AI Tool</td><td markdown="block">

Google Gemini (gemini.google.com). The iteration dates and milestone gates of Milestone 1 were pasted as the single source of truth.

</td></tr>
<tr markdown="1"><td class="k">4. Initial Prompt</td><td markdown="block">

**[character]** You are a scheduling analyst using formal dependency logic.

**[request]** Construct a high-level Gantt chart text view and milestone log from August 2026 to July 2028 that aligns all ten RUP iterations and marks LCO, LCA, IOC, REL 1.0, REL 2.0, REL 2.1 and the 28 July 2028 Expansion Decision Gate, then derive the critical path with TS = LS − ES.

**[examples]** Show pilot operation as parallel work with non-zero float.

**[adjustments]** Qualify the critical path as a planning analysis rather than a source-approved critical path.

**[type of output]** A milestone log, a Gantt chart text view and a float-based critical-path table.

**[evaluation]** Source milestones must be unchanged and the critical path must be justified by the float calculation.

</td></tr>
<tr markdown="1"><td class="k">5. Initial Output</td><td markdown="block">

The draft aligned the iterations to the Gantt view but stated a critical path too definitively and omitted the parallel pilot work with non-zero float.

</td></tr>
<tr markdown="1"><td class="k">6. Review</td><td markdown="block">

Review Board row 4: Milestone 1 gives iteration dates but does not formally calculate a task-level critical path. PMBOK correctness: the chain must be qualified as a planning analysis with an explicit float formula; project consistency required the source milestone dates to be retained. A second review of the AI's float table found that its early-start dates ignored the year-end break and the gaps between iterations (C2 on 21 December instead of 4 January, T1 on 15 February instead of 1 March), and that the AI had once named the productization branch and once the pilot year as critical.

</td></tr>
<tr markdown="1"><td class="k">7. Revision</td><td markdown="block">

Applied the standard float formulas (TS = LS − ES = LF − EF), traced the continuous zero-slack path, marked the chain as a planning analysis and showed the parallel branch with its float. By hand, the forward and backward pass were recomputed in the plan model on a working-day calendar with the year-end break, with the close-out linked finish-to-finish to the pilot year, which settles the branch question: the pilot year is critical and the productization branch C4, T3 has 115 working days of total slack; the Gantt chart was drawn from the activity list rather than from the iteration view.

</td></tr>
<tr markdown="1"><td class="k">8. Final Output</td><td markdown="block">

Part 2, Sections 7.2 and 7.3, as delivered below (the Gantt chart, Figure 7.1, is in Part 2). Source milestones remain unchanged; the critical path I1 to T2, then the pilot year and the close-out, is justified by the float table and presented as a planning analysis. Review Board decision: Accept.

**7.2 Critical Path**

<!-- include: part2-final-deliverables.md#7.2 Critical Path flat no-images -->
<!-- source: part2-final-deliverables.md -->

The critical path is calculated on the iteration network with the forward and backward pass in working days (Table 7.1): ES and EF from the predecessors, LS and LF from the project finish, total slack TS = LS − ES = LF − EF. The iterations are linked finish-to-start as the Development Case prescribes; the pilot year P1 and the productization branch C4, T3 both start after Release 2.0 is in operation, and the close-out follows T3 and finishes together with the pilot year (finish-to-finish), because the expansion decision needs both the pilot KPIs and the productized service. The project is 510 working days long. The zero-slack path is I1, I2, E1, E2, C1, C2, T1, C3, T2, P1 and the close-out: every iteration up to Release 2.0 is critical, because each starts when the previous one ends, and after Release 2.0 the pilot year drives the finish date, since its 260 working days of KPI measurement are longer than the 140 working days of C4 and T3. The productization branch has 115 working days of total slack, so a delay of Release 2.1 by up to 23 weeks would not move the expansion decision; a delay of any iteration up to T2, or a shorter pilot year, would. This is a planning analysis: the task-level dependencies inside an iteration are in Table 3.2, and the critical work packages within the critical iterations are the ones that end on the iteration's last day and feed the next iteration (Table 7.2). If an iteration threatens its milestone, the responses are, in order, the re-planning of priority-2 features (RISK-02), fast-tracking the next iteration's design work in parallel with the current iteration's test package, and crashing by raising the engineers' hours a week within the contingency reserve.


| ID | Iteration | Duration (wd) | Predecessors | ES | EF | LS | LF | Total slack (wd) | Critical | Early start | Early finish |
|---|---|---|---|---|---|---|---|---|---|---|---|
| I1 | Inception I1 | 16 | — | 0 | 16 | 0 | 16 | 0 | Yes | 3 Aug 2026 | 24 Aug 2026 |
| I2 | Inception I2 | 7 | I1 | 16 | 23 | 16 | 23 | 0 | Yes | 25 Aug 2026 | 2 Sep 2026 |
| E1 | Elaboration E1 | 10 | I2 | 23 | 33 | 23 | 33 | 0 | Yes | 3 Sep 2026 | 16 Sep 2026 |
| E2 | Elaboration E2 | 27 | E1 | 33 | 60 | 33 | 60 | 0 | Yes | 17 Sep 2026 | 23 Oct 2026 |
| C1 | Construction C1 | 40 | E2 | 60 | 100 | 60 | 100 | 0 | Yes | 26 Oct 2026 | 18 Dec 2026 |
| C2 | Construction C2 | 40 | C1 | 100 | 140 | 100 | 140 | 0 | Yes | 4 Jan 2027 | 26 Feb 2027 |
| T1 | Transition T1 | 25 | C2 | 140 | 165 | 140 | 165 | 0 | Yes | 1 Mar 2027 | 2 Apr 2027 |
| C3 | Construction C3 | 60 | T1 | 165 | 225 | 165 | 225 | 0 | Yes | 5 Apr 2027 | 25 Jun 2027 |
| T2 | Transition T2 | 25 | C3 | 225 | 250 | 225 | 250 | 0 | Yes | 28 Jun 2027 | 30 Jul 2027 |
| P1 | Pilot year P1 | 260 | T2 | 250 | 510 | 250 | 510 | 0 | Yes | 2 Aug 2027 | 28 Jul 2028 |
| C4 | Construction C4 | 120 | T2 | 250 | 370 | 365 | 485 | 115 | No | 2 Aug 2027 | 14 Jan 2028 |
| T3 | Transition T3 | 20 | C4 | 370 | 390 | 485 | 505 | 115 | No | 17 Jan 2028 | 11 Feb 2028 |
| CL | Close-out | 5 | T3, P1 (FF) | 505 | 510 | 505 | 510 | 0 | Yes | 24 Jul 2028 | 28 Jul 2028 |


**Table 7.1 Critical path method on the iteration network (working days from 3 August 2026)**


| WBS ID | Work package | Iteration | Finish | Milestone or successor |
|---|---|---|---|---|
| 1.8 | Pilot KPI reports and reviews | P1 | 21 Jul 2028 | feeds the next iteration |
| 1.9 | Pilot review, expansion decision and close-out | CL | 28 Jul 2028 | Expansion decision, project closed |
| 2.2 | Vision and Glossary | I1, I2 | 2 Sep 2026 | feeds the next iteration |
| 2.3 | Use-case model and release plan | I2 | 2 Sep 2026 | feeds the next iteration |
| 2.4 | Review records and LCO package | I2 | 2 Sep 2026 | LCO: Lifecycle Objectives |
| 3.1 | Use-case specifications | E1 | 16 Sep 2026 | feeds the next iteration |
| 3.6 | Test plan and test cases | E2 | 23 Oct 2026 | feeds the next iteration |
| 3.7 | Requirements reviews, SRS baseline and LCA package | E2 | 23 Oct 2026 | LCA: Lifecycle Architecture, SRS baseline |
| 3.8 | Scope baseline, estimates, schedule and cost baseline | E2 | 23 Oct 2026 | feeds the next iteration |
| 4.3 | Gateway payment and callback | C1 | 18 Dec 2026 | feeds the next iteration |
| 4.5 | C1 integration and iteration test | C1 | 18 Dec 2026 | feeds the next iteration |
| 4.10 | Load test, system test and IOC package | C2 | 26 Feb 2027 | IOC: Initial Operational Capability |
| 5.4 | Pilot concert nights and go-live of Release 1.0 | T1 | 2 Apr 2027 | Release 1.0 Core in operation |
| 6.5 | C3 integration and system test | C3 | 25 Jun 2027 | feeds the next iteration |
| 6.7 | Release 2.0 deployment and first concert nights | T2 | 30 Jul 2027 | Release 2.0 Growth in operation |


**Table 7.2 Work packages on the critical path**

<!-- /include -->

**7.3 Milestone Control Points**

<!-- include: part2-final-deliverables.md#7.3 Milestone Control Points flat -->
<!-- source: part2-final-deliverables.md -->


| ID | Milestone | Date | After | Acceptance / decision |
|---|---|---|---|---|
| M1 | LCO: Lifecycle Objectives | 2 Sep 2026 | 2.4 | Vision approved by the Owner; Business Case, charter, Development Case and plans accepted; go for Elaboration |
| M2 | LCA: Lifecycle Architecture, SRS baseline | 23 Oct 2026 | 3.7 | SRS signed off by the Owner; architecture, prototype and test plan accepted; gateway and LINE prerequisites verified; financial analysis re-run; go for Construction |
| M3 | IOC: Initial Operational Capability | 26 Feb 2027 | 4.10 | Release 1.0 passes the system and load tests (5 transactions a second); go for the pilot on concert nights |
| M4 | Release 1.0 Core in operation | 2 Apr 2027 | 5.4 | Acceptance tests of the two main use cases passed with the Manager and Front Staff; data migrated; Release 1.0 declared in operation |
| M5 | Release 2.0 Growth in operation | 30 Jul 2027 | 6.7 | Acceptance tests of the Release 2.0 features passed; pilot year and KPI measurement begin |
| M6 | Release 2.1 in operation | 11 Feb 2028 | 8.6 | La Loy migrated to the productized service; Free-plan sign-up released; hand-over to the support routine |
| M7 | Expansion decision, project closed | 28 Jul 2028 | 1.9 | Pilot review against the seven success criteria of the charter; expansion decision of the software house; lessons learned; sign-off |


**Table 7.3 Milestones and their acceptance decisions**

<!-- /include -->

</td></tr>
</table>

---

## Record 5: Effort estimation for tasks

<table class="rec" markdown="1">
<tr markdown="1"><td class="k">1. Artifact</td><td markdown="block">

Effort estimation (Part 2, Section 4): bottom-up person-hours per work package and engineer, reconciled to the baseline of Milestone 1 (2,632 hours: Year 0 2,092 h, Year 1 540 h; labor 846,600 THB), with three-point estimates for the risky packages and the comparison with the top-down estimate.

</td></tr>
<tr markdown="1"><td class="k">2. Member</td><td markdown="block">

Chawanakorn Sanannam

</td></tr>
<tr markdown="1"><td class="k">3. AI Tool</td><td markdown="block">

OpenCode (terminal CLI agent at opencode.ai), model "Big Pickle" (opencode/big-pickle); the baseline of Milestone 1 (2,632 h; Year 0 2,092 h; Year 1 540 h; labor 846,600 THB) was pasted.

</td></tr>
<tr markdown="1"><td class="k">4. Initial Prompt</td><td markdown="block">

**[character]** You are a project estimator working bottom-up per WBS task.

**[request]** Prepare SEATS effort estimates using the source baseline of 2,632 hours, Year 0 2,092 hours, Year 1 540 hours and labor cost 846,600 THB.

**[examples]** Allocate tasks provisionally and label new task-level hours as estimates.

**[adjustments]** Keep each phase total inside its source share and state the basis of estimates.

**[type of output]** A work-package effort table plus a basis-of-estimates note.

**[evaluation]** The total must reconcile to 2,632 hours / 846,600 THB with zero variance.

</td></tr>
<tr markdown="1"><td class="k">5. Initial Output</td><td markdown="block">

Summed role-based hours but did not distinguish the source totals from the task-level estimates and mismatched the C1/C2 distribution against the source phase baseline.

</td></tr>
<tr markdown="1"><td class="k">6. Review</td><td markdown="block">

Review Board row 5: the source estimate is top-down; detailed effort per task is not fully provided. PMBOK correctness: effort is estimated bottom-up and the basis of estimates must be stated; project consistency required the total to hit the 2,632-hour ceiling. A second output still gave hours per phase group only, which is the Milestone 1 table restated, not a bottom-up estimate.

</td></tr>
<tr markdown="1"><td class="k">7. Revision</td><td markdown="block">

Rebalanced the work-package hours to exact zero variance with the source baseline, kept Year 0 at 2,092 h and Year 1 at 540 h, and labelled the task-level allocation as provisional. By hand, the hours were then estimated per work package and per engineer (49 packages), the four risky packages (gateway payment, load test, scheduled reminders, multi-tenant model) three-point with the PERT average, and the plan model checks that every phase, engineer and year total equals Milestone 1 and prints the percent difference per phase.

</td></tr>
<tr markdown="1"><td class="k">8. Final Output</td><td markdown="block">

Part 2, Section 4, as delivered below: the basis of estimates, the effort per work package and engineer, the three-point estimates and the comparison with the top-down estimate (0 % in total, below 8 % per phase). Review Board decision: Revise; accepted after the revision.

**4. Effort Estimation**

<!-- include: part2-final-deliverables.md#4. Effort Estimation flat -->
<!-- source: part2-final-deliverables.md -->

**4.1 Basis of Estimates**

Effort is estimated in person-hours per work package, bottom-up, by the engineer who will do the work and reviewed by the Quality Assurance role; duration is derived from the effort and the engineer's part-time availability, not the other way round. The assumptions are those of Milestone 1: the four engineers work part-time at the hours a week per phase of Table 3.4 of Milestone 1 (for example 16 hours a week for the Requirements Specifier in Construction), at the software house's internal cost rates of 300 and 350 THB an hour; a working week has five days of 8 hours; the two Construction iterations of Release 1.0 deliver the 28 features of priority 1 and 2 and C3 the seven features of priority 3. Two techniques are used and compared, as the course asks: the bottom-up estimate per work package (Section 4.2, with three-point estimates for the four risky packages, Section 4.3) and the top-down estimate per phase of Milestone 1 (Section 4.4). The Review Board decided (Table 1.1, row 5) to allocate the bottom-up hours within the phase totals of Milestone 1, so that the labor cost stays at 846,600 THB and the cost baseline at the budget of the charter; the estimate therefore moves from the budgetary accuracy of Milestone 1 (−10 % to +25 %) toward a definitive estimate (−5 % to +10 %) for the iterations up to Release 2.0, while C4 and T3 remain at budgetary accuracy until they are detailed before C4.

**4.2 Bottom-up Estimate per Work Package**

Table 4.1 gives the hours of each engineer on each work package, the estimation method and the labor cost at the rates of Table 5.1. The 96 hours of concert-night support (7.1) are shown for completeness but are operating expenditure (28,800 THB in Table 3.6 of Milestone 1), outside the 2,632 development hours.


| WBS ID | Work package | Method | Boonnisa T. (PM) | Sirapatr C. (SA) | Chawanakorn S. (RS) | Watayut A. (QA) | Hours | Labor (THB) |
|---|---|---|---|---|---|---|---|---|
| **1** | **Project Management** |  |  |  |  |  |  |  |
| 1.1 | Project plans and baselines | bottom-up | 20 | - | - | - | 20 | 7,000 |
| 1.2 | Risk List and Development Case | bottom-up | 4 | - | - | 8 | 12 | 3,800 |
| 1.3 | Iteration assessments and change control, Elaboration | bottom-up | 28 | - | - | - | 28 | 9,800 |
| 1.4 | Iteration assessments and change control, Release 1.0 Construction | bottom-up | 64 | - | - | - | 64 | 22,400 |
| 1.5 | Iteration assessments and change control, Release 1.0 Transition | bottom-up | 12 | - | - | - | 12 | 4,200 |
| 1.6 | Iteration assessments and change control, Release 2.0 | bottom-up | 46 | - | - | - | 46 | 16,100 |
| 1.7 | Iteration assessments and change control, Release 2.1 | bottom-up | 28 | - | - | - | 28 | 9,800 |
| 1.8 | Pilot KPI reports and reviews | bottom-up | 12 | - | - | 8 | 20 | 6,600 |
| 1.9 | Pilot review, expansion decision and close-out | bottom-up | 8 | 4 | - | 4 | 16 | 5,400 |
| **2** | **Inception (I1, I2)** |  |  |  |  |  |  |  |
| 2.1 | Stakeholder requests and problem analysis | bottom-up | 4 | 16 | 8 | - | 28 | 9,400 |
| 2.2 | Vision and Glossary | bottom-up | - | 20 | 12 | - | 32 | 10,600 |
| 2.3 | Use-case model and release plan | bottom-up | - | 4 | 12 | 4 | 20 | 6,200 |
| 2.4 | Review records and LCO package | bottom-up | 4 | - | - | 12 | 16 | 5,000 |
| **3** | **Elaboration (E1, E2)** |  |  |  |  |  |  |  |
| 3.1 | Use-case specifications | bottom-up | - | 16 | 32 | 4 | 52 | 16,400 |
| 3.2 | Software Requirements Specification and Supplementary Specification | bottom-up | 4 | 12 | 28 | 8 | 52 | 16,400 |
| 3.3 | Analysis model and Software Architecture Document | bottom-up | 4 | 48 | 8 | - | 60 | 20,600 |
| 3.4 | User-interface prototype | bottom-up | - | 4 | 24 | 4 | 32 | 9,800 |
| 3.5 | Payment gateway and LINE sandbox | bottom-up | 8 | 12 | 4 | - | 24 | 8,200 |
| 3.6 | Test plan and test cases | bottom-up | 4 | - | - | 32 | 36 | 11,000 |
| 3.7 | Requirements reviews, SRS baseline and LCA package | bottom-up | 8 | 4 | - | 16 | 28 | 9,000 |
| 3.8 | Scope baseline, estimates, schedule and cost baseline | bottom-up | 8 | - | - | - | 8 | 2,800 |
| **4** | **Release 1.0 Core: Construction (C1, C2)** |  |  |  |  |  |  |  |
| 4.1 | Concert rounds, zones and packages | bottom-up | 8 | 16 | 32 | 8 | 64 | 20,400 |
| 4.2 | Table map, selection and hold | bottom-up | 8 | 32 | 36 | 16 | 92 | 29,600 |
| 4.3 | Gateway payment and callback | three-point | 8 | 40 | 32 | 24 | 104 | 33,600 |
| 4.4 | LINE sign-in, staff accounts and role access | bottom-up | - | 16 | 16 | 8 | 40 | 12,800 |
| 4.5 | C1 integration and iteration test | bottom-up | 8 | 8 | 8 | 24 | 48 | 15,200 |
| 4.6 | QR e-ticket and transactional messages | bottom-up | - | 16 | 32 | 8 | 56 | 17,600 |
| 4.7 | Door check-in and name lookup | bottom-up | 8 | 16 | 32 | 16 | 72 | 22,800 |
| 4.8 | Live booking view and exception handling | bottom-up | 8 | 32 | 32 | 16 | 88 | 28,400 |
| 4.9 | Audit trail, backup, consent and push budget | bottom-up | 8 | 16 | 20 | 8 | 52 | 16,800 |
| 4.10 | Load test, system test and IOC package | three-point | 8 | 32 | 16 | 64 | 120 | 38,000 |
| **5** | **Release 1.0 Core: Transition (T1)** |  |  |  |  |  |  |  |
| 5.1 | Acceptance tests of Release 1.0 | bottom-up | 8 | 8 | 12 | 28 | 56 | 17,600 |
| 5.2 | Training and user guide | bottom-up | 8 | - | 16 | 4 | 28 | 8,800 |
| 5.3 | Production set-up and data migration | bottom-up | - | 24 | 10 | 8 | 42 | 13,800 |
| 5.4 | Pilot concert nights and go-live of Release 1.0 | bottom-up | 12 | 8 | 12 | 20 | 52 | 16,600 |
| **6** | **Release 2.0 Growth (C3, T2)** |  |  |  |  |  |  |  |
| 6.1 | Scheduled reminders | three-point | 8 | 32 | 40 | 20 | 100 | 32,000 |
| 6.2 | Grace extension and waitlist | bottom-up | 8 | 40 | 48 | 28 | 124 | 39,600 |
| 6.3 | Booking transfer | bottom-up | - | 16 | 24 | 12 | 52 | 16,400 |
| 6.4 | Reports and Excel export | bottom-up | 8 | 24 | 32 | 16 | 80 | 25,600 |
| 6.5 | C3 integration and system test | bottom-up | 12 | 32 | 24 | 44 | 112 | 35,800 |
| 6.6 | Acceptance tests and training on Release 2.0 | bottom-up | 8 | 14 | 24 | 30 | 76 | 23,900 |
| 6.7 | Release 2.0 deployment and first concert nights | bottom-up | 12 | 16 | 16 | 20 | 64 | 20,600 |
| **7** | **Pilot operation (P1)** |  |  |  |  |  |  |  |
| 7.1 | Concert-night support and maintenance (operating expenditure, outside the 2,632 h) | bottom-up | - | - | 48 | 48 | 96 | 28,800 |
| **8** | **Release 2.1 Product (C4, T3)** |  |  |  |  |  |  |  |
| 8.1 | Multi-tenant data model and tenant isolation | three-point | - | 40 | 40 | 16 | 96 | 30,800 |
| 8.2 | Plans, limits and tier enforcement | bottom-up | - | 20 | 40 | 20 | 80 | 25,000 |
| 8.3 | Subscription billing and company set-up | bottom-up | 8 | 24 | 40 | 24 | 96 | 30,400 |
| 8.4 | Self-service onboarding and service administration | bottom-up | - | 20 | 40 | 20 | 80 | 25,000 |
| 8.5 | Security, load and integration test of Release 2.1 | bottom-up | 8 | 12 | 20 | 28 | 68 | 21,400 |
| 8.6 | Migration of La Loy and release of the Free-plan sign-up | bottom-up | 4 | 12 | 20 | 20 | 56 | 17,600 |
| **Total development effort** |  |  | **434** | **706** | **842** | **650** | **2632** | **846,600** |
| Rate (THB/h) |  |  | 350 | 350 | 300 | 300 |  |  |
| **Labor cost (THB)** |  |  | **151,900** | **247,100** | **252,600** | **195,000** |  | **846,600** |


**Table 4.1 Effort per work package and engineer**

**4.3 Three-point Estimates of the Risky Work Packages**

The four work packages that carry the technical risks of Milestone 1 (RISK-03 gateway onboarding, RISK-05 burst load, the LINE push quota of RISK-07, the multi-tenant architecture of Release 2.1) were estimated three-point by the engineers who will build them, with the PERT weighted average (O + 4M + P) / 6 (Table 4.2). The allocated hours of Table 4.1 are within 2.5 % of the PERT values; the difference between the most likely and the pessimistic values is the reason these packages are named in the contingency reserve (Section 6.2).


| WBS ID | Work package | Optimistic O (h) | Most likely M (h) | Pessimistic P (h) | PERT (O + 4M + P) / 6 | Allocated (h) | Allocated vs PERT |
|---|---|---|---|---|---|---|---|
| 4.3 | Gateway payment and callback | 80 | 100 | 150 | 105.0 | 104 | -1.0 % |
| 4.10 | Load test, system test and IOC package | 90 | 115 | 180 | 121.7 | 120 | -1.4 % |
| 6.1 | Scheduled reminders | 80 | 96 | 150 | 102.3 | 100 | -2.3 % |
| 8.1 | Multi-tenant data model and tenant isolation | 72 | 92 | 150 | 98.3 | 96 | -2.4 % |


**Table 4.2 Three-point estimates and PERT weighted average**

**4.4 Comparison with the Top-down Estimate of Milestone 1**

Table 4.3 compares the bottom-up hours per phase and engineer with the top-down estimate of Milestone 1 (Table 3.4 there). The totals per engineer and per year are identical by the Review Board's decision; per phase the bottom-up plan differs in two places: the monthly pilot KPI reports and the close-out (1.8, 1.9, 36 hours) are drawn from the Release 2.1 pool, which Milestone 1 had no row for, and 3.5 hours of the Project Manager's control work move from C3 to T2 because the control work package 1.6 spans both iterations. The percent difference is below 8 % for every phase that has hours in both estimates and 0 % in total, which confirms the Milestone 1 figures as the planning baseline.


| Phase | Boonnisa T. | Sirapatr C. | Chawanakorn S. | Watayut A. | Bottom-up (h) | Milestone 1 top-down (h) | Difference (h) | Percent difference |
|---|---|---|---|---|---|---|---|---|
| Inception (I1, I2) | 32 | 40 | 32 | 24 | 128 | 128 | +0 | 0.0 % |
| Elaboration (E1, E2) | 64 | 96 | 96 | 64 | 320 | 320 | +0 | 0.0 % |
| Construction Release 1.0 (C1, C2) | 128 | 224 | 256 | 192 | 800 | 800 | +0 | 0.0 % |
| Transition Release 1.0 (T1) | 40 | 40 | 50 | 60 | 190 | 190 | +0 | 0.0 % |
| Construction Release 2.0 (C3) | 68.4706 | 144 | 168 | 120 | 500.471 | 504 | -3.52941 | 0.7 % |
| Transition Release 2.0 (T2) | 33.5294 | 30 | 40 | 50 | 153.529 | 150 | +3.52941 | 2.3 % |
| Construction Release 2.1 (C4) | 40 | 116 | 180 | 108 | 444 | 480 | -36 | 7.8 % |
| Transition Release 2.1 (T3) | 8 | 12 | 20 | 20 | 60 | 60 | +0 | 0.0 % |
| Pilot operation and close-out (P1) | 20 | 4 | 0 | 12 | 36 | 0 | +36 | 200.0 % |
| **Total** | **434** | **706** | **842** | **650** | **2632** | **2632** | **+0** | **0.0 %** |


**Table 4.3 Bottom-up versus top-down effort by phase**

<!-- /include -->

</td></tr>
</table>

---

## Record 6: WBS decomposition and features by release

<table class="rec" markdown="1">
<tr markdown="1"><td class="k">1. Artifact</td><td markdown="block">

WBS decomposition and features-by-release mapping (Part 2, Sections 2.2 and 3.1): deliverable-oriented work packages in noun form, with every feature F1 to F35 assigned to Release 1.0 Core or Release 2.0 Growth and the productization items to Release 2.1.

</td></tr>
<tr markdown="1"><td class="k">2. Member</td><td markdown="block">

Chawanakorn Sanannam

</td></tr>
<tr markdown="1"><td class="k">3. AI Tool</td><td markdown="block">

OpenCode (terminal CLI agent at opencode.ai), model "Big Pickle" (opencode/big-pickle); the feature tables and release boundaries of Milestone 1 were pasted.

</td></tr>
<tr markdown="1"><td class="k">4. Initial Prompt</td><td markdown="block">

**[character]** You are a requirements specifier building a deliverable-oriented WBS.

**[request]** Organize the SEATS features by release (Core, Growth and productization) and decompose them into 100 % deliverable-oriented noun work packages.

**[examples]** Keep booking/payment/QR check-in separate from reminders/waitlist/transfers/reports and multi-tenant subscription features.

**[adjustments]** Map every feature to exactly one work package (100 % rule) and avoid adding new scope.

**[type of output]** A WBS table plus a features-by-release table.

**[evaluation]** A unit of work appears once; work packages are nouns and every feature sits in exactly one release.

</td></tr>
<tr markdown="1"><td class="k">5. Initial Output</td><td markdown="block">

The initial feature list mixed features from different releases and the Construction branches were decomposed by page instead of by feature groups, mixing nouns and verbs.

</td></tr>
<tr markdown="1"><td class="k">6. Review</td><td markdown="block">

Review Board row 6: Core, Growth and productization features were mixed together, and the WBS did not use deliverable-oriented nouns. PMBOK correctness: the decomposition must be mutually exclusive and collectively exhaustive.

</td></tr>
<tr markdown="1"><td class="k">7. Revision</td><td markdown="block">

Re-grouped the features by release using the source report only and re-decomposed Construction into noun-form feature-group work packages, verifying every feature appears exactly once. By hand, the feature groups were aligned with the iteration contents of Milestone 1 (C1: rounds and packages, table map and hold, payment, sign-in and accounts; C2: e-ticket and messages, check-in, live view and exceptions, audit, backup and consent; C3: reminders, grace and waitlist, transfer, reports) and the features-by-release table became Table 2.1 of the scope statement.

</td></tr>
<tr markdown="1"><td class="k">8. Final Output</td><td markdown="block">

Part 2, Section 2.2 (Table 2.1), as delivered below, and the WBS of Section 3.1 (quoted in Record 3): Release 1.0 contains the core booking, payment and QR check-in features; Release 2.0 the reminders, grace extension, waitlist, transfer and reports; Release 2.1 the multi-tenant plans, billing and onboarding, with one numbering scheme shared by all tables. Review Board decision: Revise; accepted after the revision.

**2.2 Product Characteristics and Requirements**

<!-- include: part2-final-deliverables.md#2.2 Product Characteristics and Requirements flat -->
<!-- source: part2-final-deliverables.md -->

The product scope is the feature set of the Vision (Tables 2.15 to 2.18 of Milestone 1), grouped by release and user role in Table 2.1; the detailed requirements are the use-case specifications, the Software Requirements Specification and the Supplementary Specification of the Requirements Engineering project. The quality characteristics (Table 2.2) are the preliminary quality targets of Milestone 1 (Table 2.19), each now tied to the test that verifies it, as the Review Board asked (Table 1.1, row 7). Personal data is handled under the Personal Data Protection Act, with consent, retention and correction designed in; drink packages are presented within the Alcoholic Beverage Control Act.

**Table 2.1 Product scope by release and role**

| Release | Role | Features | Characteristics |
|---|---|---|---|
| 1.0 Core | Customer | F1 LINE sign-in, F2 table map, F3 table selection and 15-minute hold, F4 gateway payment, F5 QR e-ticket, F6 transactional messages, F7 booking terms, F8 my bookings, F9 round list | Self-service booking inside LINE: browse, choose, hold, pay the full fee, keep the e-ticket; no Manager reply needed |
| 1.0 Core | Manager (Owner read-only) | F10 concert rounds, F11 zones and packages, F12 live booking view, F13 ticket escalation management, F14 manual booking and payment overrides | Set up each concert round and watch every table, hold, payment and check-in on one live screen; exceptions by hand, including the degraded payment mode |
| 1.0 Core | Front Staff | F15 QR scan, F16 ticket details, F17 on-site check-in, F18 invalid-ticket escalation, F19 no-show and table release, F20 name lookup | Check-in by QR within 15 seconds per table; release of no-show tables after the grace period |
| 1.0 Core | System | F21 hold release, F22 daily backup, F23 payment callback, F24 staff accounts, F25 audit trail, F26 push-message budget, F27 degraded-mode switch, F28 consent and profile access | First-lock-wins hold with timeout, automatic confirmation on the gateway's webhook, role-based access, audit trail, backup with Excel export, consent |
| 2.0 Growth | Customer and System | F29 grace extension, F30 waitlist, F31 booking transfer, F32 scheduled reminders, F34 reminder scheduling, F35 waitlist offer | Use the central record to lose fewer tables: reminders, grace extension, waitlist in queue order, official transfer |
| 2.0 Growth | Manager and Owner | F33 reports | Booking, revenue, artist-popularity and customer-history reports with export |
| 2.1 Product | Software house | Multi-tenant data model and tenant isolation; Free, Standard and Premium plans with limits and enforcement; subscription billing and setup-fee invoicing; self-service onboarding; service administration; migration of La Loy | The pilot system productized as a subscription service within the 1,000 THB a month ceiling (Section 3.1 of Milestone 1) |

**Table 2.2 Quality requirements and their verification**

| Quality requirement | Target (Table 2.19 of Milestone 1) | Verification (test evidence) | When |
|---|---|---|---|
| Throughput at booking-open time | at least 5 transactions a second | Load test with simulated customers opening a round: 5 transactions a second sustained for 10 minutes, one hold per table, no deadlock (WBS 4.10) | before IOC; repeated for Release 2.1 (8.5) |
| Response time | within 2 seconds for customer and Front Staff transactions | Response-time measurement during the load test and in the acceptance tests on the test devices inside LINE (4.10, 5.1) | IOC, T1 |
| Check-in time | within 15 seconds per table | Timed check-in of 30 tickets by the Front Staff with the tablet at a pilot night (5.1, 5.4) | T1 |
| Recovery after an outage | within 2 hours during opening hours | Restore drill: restore the daily backup to a fresh environment and bring the service up within 2 hours (4.10, repeated in 8.5) | IOC, C4 |
| Backup and export | daily backup of booking data with export to Excel | Backup job verified daily in the test environment; the Excel export opened by the Manager (4.9, 5.1) | C2, T1 |
| Supported browsers | current LINE in-app browser; last two versions of Chrome, Safari and Edge | Browser-compatibility checklist run on the test devices and the shop's desktop browser (4.10, 5.1) | IOC, T1 |
| Operating cost of the restaurant | hosting, APIs and LINE plan at or below 1,000 THB a month | Monthly cost review of hosting and push messages during the pilot year (1.8) | P1 |

<!-- /include -->

</td></tr>
</table>

---

## Record 7: Consistency review of the drafts, quality requirements and verification

<table class="rec" markdown="1">
<tr markdown="1"><td class="k">1. Artifact</td><td markdown="block">

Consistency review of the three Milestone 2 drafts (decision log, final deliverable, GenAI log) against Milestone 1, the brief and each other, and the quality requirements with their verification (Part 2, Table 2.2 and the evidence column of Table 2.4): every target of Table 2.19 of Milestone 1 linked to a test, a threshold and the work package that runs it.

</td></tr>
<tr markdown="1"><td class="k">2. Member</td><td markdown="block">

Watayut Aiamanan

</td></tr>
<tr markdown="1"><td class="k">3. AI Tool</td><td markdown="block">

Claude Code (Anthropic, model Claude Fable 5.1), run inside the project repository, with the Milestone 1 report sources, the project brief, the teammates' three drafts and the financial model (tools/finance.py) readable by the agent.

</td></tr>
<tr markdown="1"><td class="k">4. Initial Prompt</td><td markdown="block">

**[role]** Claude Code working in the 2110722 repository, where the Milestone 1 report, its build tools and the brief are the context.

**[task]** "Please check the teammates' Milestone 2 drafts (workspace/received/examples/teammate_milestone_2) and merge them with the current Milestone 1"; then, before merging: "please check any inconsistency in the M2 draft also; if you find one, let me know."

**[format]** The report sources of the Milestone 1 pipeline (markdown built to PDF) and, first, a list of the inconsistencies found.

</td></tr>
<tr markdown="1"><td class="k">5. Initial Output</td><td markdown="block">

A list of inconsistencies in three groups. Conflicts with Milestone 1: the drafts named the system SEATS while Milestone 1 said CTRS; the scope statement used requirement identifiers R1 to R7 that exist in no project document; the critical-path table's early-start dates ignored the year-end break and the gaps between iterations (C2 on 21 December instead of 4 January, T1 on 15 February instead of 1 March); pilot-monitoring hours were folded into the Release 2.1 pool. Internal contradictions: the decision log named the productization branch as the zero-slack path while the deliverable gave it 121 days of float; verb labels remained although the log recorded their replacement by nouns; a task started before its predecessor finished; summary durations did not equal their children; three-point estimates were claimed but no values shown; three decisions read Accept in the log and "Accept with edits" in the records. Gaps against the brief: effort per task, assignment of resources to tasks and a cost derived from them were missing, the Gantt and critical path were at iteration level, and the quality requirements had thresholds but no verification method. The agent also proposed the quality-requirements table with a verification, a threshold and a work package per target.

</td></tr>
<tr markdown="1"><td class="k">6. Review</td><td markdown="block">

Requirement satisfaction: the review covered the three criteria of the brief for every artifact of the drafts, and the quality table answered the Review Board's row 7 for all seven targets (six of Table 2.19 plus the operating-cost ceiling of the charter). PMBOK correctness: each verification is a test with a measurable threshold run by the Quality Assurance role, not by the author of the function, and the date findings used the working-day logic of the critical path method. Project consistency: every finding was checked against the Milestone 1 tables it cited (2.13 to 2.21, 3.4, 3.6, 4.1) and found correct, including the name of the project, which the team had in fact changed to SEATS after Milestone 1 without recording it.

</td></tr>
<tr markdown="1"><td class="k">7. Revision</td><td markdown="block">

The member answered the agent's questions with the team's decisions: the project name is SEATS (recorded in the Document Revision History), the eight rows of the decision log stay as the teammates wrote them with the section references re-pointed, the prompt records of the other members are aligned but not rewritten, and the merged deliverable goes to task level. The agent then merged the drafts into the Milestone 1 format, replaced R1 to R7 by the feature identifiers, placed each verification of the quality table in the work package and iteration that runs it (4.10, 5.1, 5.4, 8.5, 1.8), and built the remaining tables from a plan model (Record 8).

</td></tr>
<tr markdown="1"><td class="k">8. Final Output</td><td markdown="block">

Part 2, Table 2.2 (quoted with Section 2.2 in Record 6) and the evidence column of Table 2.4 (quoted in Record 2); the findings of the review are resolved in Part 2 as follows: one name (SEATS), feature identifiers F1 to F37, dates from the working-day calendar of Milestone 1 (Tables 3.2 and 7.1), one critical path justified by the float table (Section 7.2), noun work packages (Table 3.1), three-point values shown (Table 4.2), pilot KPI work and close-out as work packages of their own (1.8, 1.9). Acceptable because every quality target has a measurable threshold and an independent test, and because no finding of the review remains open. Review Board decision: Revise; accepted after the revision.

</td></tr>
</table>

---

## Record 8: Cost estimate consistency and the plan model

<table class="rec" markdown="1">
<tr markdown="1"><td class="k">1. Artifact</td><td markdown="block">

Cost estimate consistency (Part 2, Section 6) and the plan model behind Sections 3 to 7: one source (tools/plan.py) that holds the 49 work packages with their hours per engineer, dates, predecessors, owners, three-point estimates and other costs, and generates the WBS, activity, effort, RACI, loading, cost, time-phased baseline, CPM and critical-path tables and the Gantt chart on every build, checking the totals against Milestone 1.

</td></tr>
<tr markdown="1"><td class="k">2. Member</td><td markdown="block">

Watayut Aiamanan

</td></tr>
<tr markdown="1"><td class="k">3. AI Tool</td><td markdown="block">

Claude Code (Anthropic, model Claude Fable 5.1), run inside the project repository (same session as Record 7).

</td></tr>
<tr markdown="1"><td class="k">4. Initial Prompt</td><td markdown="block">

**[role]** Claude Code in the repository, with the Milestone 1 effort and cost tables (Tables 2.20, 3.4 to 3.7) and the financial model as context.

**[task]** Merge the drafts at full task level: effort per work package and engineer, resources assigned to the work packages with rates, a cost estimate derived from them with the contingency reserve, and the schedule with Gantt chart and critical path, all reconciled with Milestone 1.

**[format]** Generated tables in the report sources, regenerated on every build, with a check that the totals equal Milestone 1.

</td></tr>
<tr markdown="1"><td class="k">5. Initial Output</td><td markdown="block">

The agent reported that the draft's cost table copied the Milestone 1 figures by category and could not show that they follow from the resource assignment, the rates and the effort, that the contingency was a bare 10 % without the risks it covers, and that the management reserve was mentioned but not decided. It then produced the plan model: 49 work packages whose hours per engineer sum to the phase totals of Table 3.4 of Milestone 1, the other costs of Tables 3.5 and 3.6 attached to the work packages that use them, labor as hours times rate, contingency per year, a time-phased baseline by iteration, the forward and backward pass on the iteration network with a working-day calendar, and the Gantt chart. Its checks printed the totals per engineer, per year and per phase and the weekly load of each engineer, which showed peaks above the Milestone 1 availability in the middle of the Construction iterations.

</td></tr>
<tr markdown="1"><td class="k">6. Review</td><td markdown="block">

Requirement satisfaction: items 4 to 7 of the brief are now derived from one model, and the cost reconciles to 1,010,590 THB, 767,690 THB in Year 0 and 242,900 THB in Year 1, labor 846,600 THB for 2,632 hours, net investment 860,590 THB. PMBOK correctness: the budget build-up (work-package estimates, contingency reserve, cost baseline, management reserve, project budget) is explicit, the contingency reserve is in the baseline and tied to identified risks, effort and duration are kept apart, and the critical path is justified by total slack. Project consistency: the model refuses to build if a total differs from Milestone 1. Weaknesses: two decisions had been written by the agent on its own (no management reserve; the per-risk split of the Year 0 reserve), and the loading peaks needed a stated leveling policy.

</td></tr>
<tr markdown="1"><td class="k">7. Revision</td><td markdown="block">

The member confirmed the two decisions as the team's (no management reserve, so that the project budget equals the cost baseline of the charter; the per-risk split kept as provisional amounts until the Milestone 3 risk register) and asked for the loading to be shown honestly: the agent moved the test plan (3.6) and the Release 2.1 test (8.5) earlier in their iterations and wrote the leveling policy of Section 5.3 (planned averages equal the availability; peaks leveled by the engineer sequencing overlapping packages inside their free slack; milestone dates unchanged). Arithmetic was not done by the model's prose but by the code, which is kept with the report sources.

</td></tr>
<tr markdown="1"><td class="k">8. Final Output</td><td markdown="block">

Part 2, Section 6, as delivered below (the effort, assignment and schedule tables of the same model are quoted in Records 3, 5 and 4). Acceptable because every figure of the cost baseline is traceable to hours, rates and listed items, the reserves are decided and justified, and the reconciliation with Milestone 1 is exact. Review Board decision: Accept.

**6. Cost Estimate**

<!-- include: part2-final-deliverables.md#6. Cost Estimate flat -->
<!-- source: part2-final-deliverables.md -->

**6.1 Cost by WBS Item**

The cost baseline is built up from the work packages, as the PMBOK budget build-up prescribes: the labor of each work package is its hours times the rate of each assigned engineer (Table 4.1), the other costs are the physical resources of Table 5.1 attached to the work packages that use them, and the contingency reserve for the identified risks is added to form the cost baseline (Table 6.1). The totals equal the budget of the charter and the cost tables of Milestone 1 (Tables 2.20 and 3.7 there): labor 846,600 THB, other costs 75,500 THB (test devices 15,000, hosting and domain 8,300, legal set-up 15,000, pilot hosting 8,400, pilot support 28,800), contingency 88,490 THB.


| WBS | Item | Hours | Labor basis (hours x THB/h) | Labor (THB) | Other costs (THB) | Subtotal (THB) |
|---|---|---|---|---|---|---|
| 1 | Project Management | 246 | Boonnisa T. 222 h x 350; Sirapatr C. 4 h x 350; Watayut A. 20 h x 300 | 85,100 | - | 85,100 |
| 2 | Inception (I1, I2) | 96 | Boonnisa T. 8 h x 350; Sirapatr C. 40 h x 350; Chawanakorn S. 32 h x 300; Watayut A. 16 h x 300 | 31,200 | Development and staging hosting, August 2026 300 | 31,500 |
| 3 | Elaboration (E1, E2) | 292 | Boonnisa T. 36 h x 350; Sirapatr C. 96 h x 350; Chawanakorn S. 96 h x 300; Watayut A. 64 h x 300 | 94,200 | Development and staging hosting, September to October 2026 600 | 94,800 |
| 4 | Release 1.0 Core: Construction (C1, C2) | 736 | Boonnisa T. 64 h x 350; Sirapatr C. 224 h x 350; Chawanakorn S. 256 h x 300; Watayut A. 192 h x 300 | 235,200 | Test devices: Android phone and 10-inch tablet 15,000; Development and staging hosting, November 2026 to February 2027 1,200 | 251,400 |
| 5 | Release 1.0 Core: Transition (T1) | 178 | Boonnisa T. 28 h x 350; Sirapatr C. 40 h x 350; Chawanakorn S. 50 h x 300; Watayut A. 60 h x 300 | 56,800 | Domain name and TLS certificate 1,200; Development and staging hosting, March 2027 300; Production hosting of the pilot restaurant, March 2027 700 | 59,000 |
| 6 | Release 2.0 Growth (C3, T2) | 608 | Boonnisa T. 56 h x 350; Sirapatr C. 174 h x 350; Chawanakorn S. 208 h x 300; Watayut A. 170 h x 300 | 193,900 | Development and staging hosting, April to July 2027 1,200; Production hosting of the pilot restaurant, April to July 2027 2,800 | 197,900 |
| 7 | Pilot operation (P1) | 0 |  | 0 | Production hosting during the pilot year 8,400; support labor 96 h x 300 = 28,800 | 37,200 |
| 8 | Release 2.1 Product (C4, T3) | 476 | Boonnisa T. 20 h x 350; Sirapatr C. 128 h x 350; Chawanakorn S. 200 h x 300; Watayut A. 128 h x 300 | 150,200 | Company registration, terms of service, privacy policy and data-processing agreement 15,000 | 165,200 |
|  | **Work-package estimates** | **2632** |  | **846,600** | **75,500** | **922,100** |
|  | Contingency reserve, Year 0 (RISK-02, RISK-03, RISK-05, RISK-08, RISK-10) |  | 10 % of 697,900 THB |  |  | 69,790 |
|  | Contingency reserve, Year 1 (RISK-04, RISK-07, RISK-12) |  | 10 % of 187,000 THB (labor of C4 and T3 and the legal set-up) |  |  | 18,700 |
|  | **Cost baseline** |  |  |  |  | **1,010,590** |
|  | Management reserve |  | none held by the sponsor for this project (unknown unknowns escalate to the partners' meeting) |  |  | 0 |
|  | **Project budget (charter)** |  |  |  |  | **1,010,590** |
|  | Less: pilot implementation fee of La Loy (revenue inside the project) |  |  |  |  | (150,000) |
|  | **Net investment of the software house** |  |  |  |  | **860,590** |


**Table 6.1 Cost estimate by WBS item, contingency reserve, cost baseline and project budget**

**6.2 Contingency Reserve and Management Reserve**

The contingency reserve covers identified risks (known unknowns) and is part of the cost baseline. Year 0 holds 69,790 THB, 10 % of the Year 0 cost, for the risks that can lengthen the build: RISK-02 (part-time engineers delayed by other work, about 2 weeks of an iteration, 35,000 THB), RISK-03 (gateway onboarding or LINE settings late, a re-run of the gateway package, 20,000 THB), RISK-05 (burst load above design, an extra load-test and tuning cycle, 10,000 THB), RISK-08 and RISK-10 (late business rules and change requests after the SRS baseline, rework in C3, 5,000 THB). Year 1 holds 18,700 THB, 10 % of the productization labor and the legal set-up, for RISK-04 (support and productization competing for the same engineers), RISK-07 (push messages or hosting above the operating-cost ceiling) and RISK-12 (slower adoption, which may require a second pilot venue before the gate). The reserve is released by the Project Manager at an iteration assessment against a recorded risk event, never for new features. The sponsor holds no management reserve for this project: unknown unknowns are escalated to the partners' meeting of the software house, which decides on additional funds or a scope change through the Change Control Board; the project budget therefore equals the cost baseline, 1,010,590 THB.

**6.3 Time-phased Cost Baseline**

Table 6.2 phases the cost baseline over the iterations: the labor of each work package is spread evenly over its working days, the other costs fall in the iteration that uses them, and the contingency reserve of each year is distributed in proportion to the cost of the iterations of that year. The cumulative column is the S-curve against which cost performance is measured at every iteration assessment; the Year 0 cumulative at the end of T2 is the 767,690 THB of the Year 0 budget.


| Iteration | Name | Period | Labor (THB) | Other costs (THB) | Contingency (THB) | Subtotal (THB) | Cumulative (THB) |
|---|---|---|---|---|---|---|---|
| I1 | Inception I1 | 3 Aug 2026 to 24 Aug 2026 | 23,070 | 300 | 2,337 | 25,707 | 25,707 |
| I2 | Inception I2 | 25 Aug 2026 to 2 Sep 2026 | 18,930 | 0 | 1,893 | 20,823 | 46,530 |
| E1 | Elaboration E1 | 3 Sep 2026 to 16 Sep 2026 | 22,776 | 600 | 2,338 | 25,714 | 72,244 |
| E2 | Elaboration E2 | 17 Sep 2026 to 23 Oct 2026 | 81,224 | 0 | 8,122 | 89,346 | 161,590 |
| C1 | Construction C1 | 26 Oct 2026 to 18 Dec 2026 | 122,800 | 16,200 | 13,900 | 152,900 | 314,490 |
| C2 | Construction C2 | 4 Jan 2027 to 26 Feb 2027 | 134,800 | 0 | 13,480 | 148,280 | 462,770 |
| T1 | Transition T1 | 1 Mar 2027 to 2 Apr 2027 | 61,000 | 2,200 | 6,320 | 69,520 | 532,290 |
| C3 | Construction C3 | 5 Apr 2027 to 25 Jun 2027 | 160,765 | 0 | 16,076 | 176,841 | 709,131 |
| T2 | Transition T2 | 28 Jun 2027 to 30 Jul 2027 | 49,235 | 4,000 | 5,324 | 58,559 | 767,690 |
| P1 | Pilot year P1 | 2 Aug 2027 to 28 Jul 2028 | 6,600 | 37,200 | 3,653 | 47,453 | 815,143 |
| C4 | Construction C4 | 2 Aug 2027 to 14 Jan 2028 | 141,000 | 15,000 | 13,012 | 169,012 | 984,155 |
| T3 | Transition T3 | 17 Jan 2028 to 11 Feb 2028 | 19,000 | 0 | 1,585 | 20,585 | 1,004,740 |
| CL | Close-out | 24 Jul 2028 to 28 Jul 2028 | 5,400 | 0 | 450 | 5,850 | 1,010,590 |
|  | **Total** |  | **846,600** | **75,500** | **88,490** | **1,010,590** |  |


**Table 6.2 Time-phased cost baseline by iteration**

**6.4 Reconciliation and Cost-control Rules**

The bottom-up cost baseline reconciles with Milestone 1 without variance: 846,600 THB of labor for 2,632 hours, 75,500 THB of other costs, 88,490 THB of contingency, 1,010,590 THB in total, of which 767,690 THB in Year 0 and 242,900 THB in Year 1; less the pilot implementation fee of 150,000 THB, the net investment of the software house is 860,590 THB, as in the charter. The cost-control rules of the project are:

- The Project Manager tracks actual hours against the 2,632-hour plan and actual cost against the time-phased baseline at every iteration assessment; the control threshold is ±10 % of the cumulative baseline, above which a change request or a re-plan is raised.
- Any change that affects scope, budget or milestone dates is assessed for impact and decided by the Change Control Board; the baseline is re-planned, not silently extended (RISK-10).
- The contingency reserve is held for identified risks and released against a recorded risk event; it is not planned feature-development effort.
- The budget excludes the costs that Milestone 1 assigns to the restaurant: its LINE plan, the gateway's merchant fees and the check-in tablet.
- Figures are kept in 2026 THB, rounded to the nearest 10 THB in the tables and to the hour in the effort plan.

<!-- /include -->

</td></tr>
</table>
