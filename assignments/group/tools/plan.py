#!/usr/bin/env python3
"""Project plan model of the SEATS project (Milestone 2; CTRS in Milestone 1): WBS, tasks, bottom-up effort, resource assignment,
cost baseline, schedule and critical path. Every figure of the Milestone 2 report is generated from this file,
the way the financial tables of Milestone 1 are generated from finance.py, so the tables cannot contradict each other.

Anchors from Milestone 1 (do not change here; change Milestone 1 first): the iteration dates of Table 2.21, the
features of Tables 2.15 to 2.18, the hours per phase and per engineer and the rates of Table 3.4 (finance.PHASES,
finance.MEMBERS), the non-labor costs of Tables 3.5 and 3.6 (finance.CAPEX, finance.DEV_NONLABOR) and the 10 %
contingency reserve. The bottom-up hours of the tasks below are allocated within those phase totals, so that the
cost baseline stays at the budget of the charter (1,010,590 THB); the comparison table shows where the bottom-up
plan moves hours between phases (pilot KPI reviews and the close-out are drawn from the Release 2.1 pool).

Usage: python3 tools/plan.py            print every table and render assets/diagrams/schedule-tasks.png
       python3 tools/plan.py --check    print the checks only (phase totals, weekly load)
Tables are emitted between `<!-- name -->` … `<!-- /name -->` markers; build_pm_report.py pastes them into the
`<!-- plan: name -->` blocks of the Milestone 2 report.
"""
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import finance                                           # noqa: E402

GROUP = Path(__file__).resolve().parent.parent
ASSETS = GROUP / "workspace" / "report" / "assets" / "diagrams"

# ----------------------------------------------------------------------------------------------------- resources
KEYS = ["PM", "SA", "RS", "QA"]
MEMBERS = {k: (short, role, rate) for k, (role, short, rate) in zip(KEYS, finance.MEMBERS)}
NAMES = {"PM": "Boonnisa Tangjitpermkwamdee", "SA": "Sirapatr Chalermwattanatrai",
         "RS": "Chawanakorn Sanannam", "QA": "Watayut Aiamanan"}
RATE = {k: MEMBERS[k][2] for k in KEYS}
HOURS_PER_DAY = 8                                        # 100 % units = 8 hours a day (ch9)

PHYSICAL = [  # resource, type, use, cost basis, when
    ("Android phone and 10-inch tablet", "Equipment (CAPEX)", "LIFF and check-in testing (4.2 to 4.10, 5.1, 6.5, 8.5)", "15,000 THB, one set", "C1"),
    ("Development and staging hosting", "Service", "Build and test environments (3.3 to 8.5)", "300 THB a month, 12 months of Year 0", "I1 to T2"),
    ("Production hosting", "Service", "Pilot restaurant's live system (5.3 onwards)", "700 THB a month: 5 months of Year 0, 12 of Year 1", "T1 to P1"),
    ("Domain name and TLS certificate", "Service", "Production set-up (5.3)", "1,200 THB a year", "T1"),
    ("Payment gateway sandbox, LINE Developers, GitHub, Figma, PlantUML", "Service", "3.5 onwards", "free tiers, 0 THB", "E2 onwards"),
    ("Company registration, terms of service, privacy policy, data-processing agreement", "Legal (Year 1)", "Subscription business (8.3)", "15,000 THB, once", "C4"),
    ("Pilot restaurant's check-in tablet, LINE Official Account plan, gateway merchant account", "Customer-paid", "Operation at La Loy", "paid by La Loy (CON-03, CON-07); about 9,000 THB for the tablet", "T1 onwards"),
]

# ----------------------------------------------------------------------------------------------------- calendar
BREAK = (date(2026, 12, 21), date(2027, 1, 1))          # year-end break between C1 and C2 (Table 2.21 of Milestone 1)
PROJECT_START, PROJECT_END = date(2026, 8, 3), date(2028, 7, 28)


def is_workday(d: date) -> bool:
    return d.weekday() < 5 and not (BREAK[0] <= d <= BREAK[1])


WORKDAYS = [PROJECT_START + timedelta(n) for n in range((PROJECT_END - PROJECT_START).days + 1)]
WORKDAYS = [d for d in WORKDAYS if is_workday(d)]
INDEX = {d: i for i, d in enumerate(WORKDAYS)}          # working-day index, 0 = 3 Aug 2026


def wd(a: date, b: date) -> int:
    """Working days from a to b inclusive."""
    return INDEX[b] - INDEX[a] + 1


def D(s: str) -> date:
    y, m, d = s.split("-")
    return date(int(y), int(m), int(d))


def fmt_date(d: date) -> str:
    return f"{d.day} {d.strftime('%b')} {d.year}"


# ----------------------------------------------------------------------------------------------------- iterations
# id, name, start, end, phase pool of Milestone 1 Table 3.4 (None = no development hours in Milestone 1)
ITERATIONS = [
    ("I1", "Inception I1", "2026-08-03", "2026-08-24", "Inception"),
    ("I2", "Inception I2", "2026-08-25", "2026-09-02", "Inception"),
    ("E1", "Elaboration E1", "2026-09-03", "2026-09-16", "Elaboration"),
    ("E2", "Elaboration E2", "2026-09-17", "2026-10-23", "Elaboration"),
    ("C1", "Construction C1", "2026-10-26", "2026-12-18", "Construction R1.0"),
    ("C2", "Construction C2", "2027-01-04", "2027-02-26", "Construction R1.0"),
    ("T1", "Transition T1", "2027-03-01", "2027-04-02", "Transition R1.0"),
    ("C3", "Construction C3", "2027-04-05", "2027-06-25", "Construction R2.0"),
    ("T2", "Transition T2", "2027-06-28", "2027-07-30", "Transition R2.0"),
    ("P1", "Pilot year P1", "2027-08-02", "2028-07-28", None),
    ("C4", "Construction C4", "2027-08-02", "2028-01-14", "Construction R2.1"),
    ("T3", "Transition T3", "2028-01-17", "2028-02-11", "Transition R2.1"),
    ("CL", "Close-out", "2028-07-24", "2028-07-28", None),
]
ITER = {i[0]: (i[1], D(i[2]), D(i[3]), i[4]) for i in ITERATIONS}
ITER_PRED = {"I1": [], "I2": [("I1", "FS")], "E1": [("I2", "FS")], "E2": [("E1", "FS")], "C1": [("E2", "FS")],
             "C2": [("C1", "FS")], "T1": [("C2", "FS")], "C3": [("T1", "FS")], "T2": [("C3", "FS")],
             "P1": [("T2", "FS")], "C4": [("T2", "FS")], "T3": [("C4", "FS")], "CL": [("T3", "FS"), ("P1", "FF")]}
PHASE_ORDER = ["Inception", "Elaboration", "Construction R1.0", "Transition R1.0", "Construction R2.0",
               "Transition R2.0", "Construction R2.1", "Transition R2.1", "Pilot operation and close-out"]
PHASE_M1 = {name: (year, weeks, hpw) for name, year, weeks, hpw in finance.PHASES}
PHASE_KEY = {"Inception (I1, I2)": "Inception", "Elaboration (E1, E2)": "Elaboration",
             "Construction Release 1.0 (C1, C2)": "Construction R1.0", "Transition Release 1.0 (T1)": "Transition R1.0",
             "Construction Release 2.0 (C3)": "Construction R2.0", "Transition Release 2.0 (T2)": "Transition R2.0",
             "Construction Release 2.1 productization (C4)": "Construction R2.1", "Transition Release 2.1 (T3)": "Transition R2.1"}
M1_PHASE = {PHASE_KEY[n]: (y, w, hpw) for n, (y, w, hpw) in PHASE_M1.items()}
PHASE_LABEL = {"Inception": "Inception (I1, I2)", "Elaboration": "Elaboration (E1, E2)",
               "Construction R1.0": "Construction Release 1.0 (C1, C2)", "Transition R1.0": "Transition Release 1.0 (T1)",
               "Construction R2.0": "Construction Release 2.0 (C3)", "Transition R2.0": "Transition Release 2.0 (T2)",
               "Construction R2.1": "Construction Release 2.1 (C4)", "Transition R2.1": "Transition Release 2.1 (T3)",
               "Pilot operation and close-out": "Pilot operation and close-out (P1)"}

MILESTONES = [  # id, name, date, after task
    ("M1", "LCO: Lifecycle Objectives", "2026-09-02", "2.4"),
    ("M2", "LCA: Lifecycle Architecture, SRS baseline", "2026-10-23", "3.7"),
    ("M3", "IOC: Initial Operational Capability", "2027-02-26", "4.10"),
    ("M4", "Release 1.0 Core in operation", "2027-04-02", "5.4"),
    ("M5", "Release 2.0 Growth in operation", "2027-07-30", "6.7"),
    ("M6", "Release 2.1 in operation", "2028-02-11", "8.6"),
    ("M7", "Expansion decision, project closed", "2028-07-28", "1.9"),
]
MILESTONE_DECISION = {
    "M1": "Vision approved by the Owner; Business Case, charter, Development Case and plans accepted; go for Elaboration",
    "M2": "SRS signed off by the Owner; architecture, prototype and test plan accepted; gateway and LINE prerequisites verified; financial analysis re-run; go for Construction",
    "M3": "Release 1.0 passes the system and load tests (5 transactions a second); go for the pilot on concert nights",
    "M4": "Acceptance tests of the two main use cases passed with the Manager and Front Staff; data migrated; Release 1.0 declared in operation",
    "M5": "Acceptance tests of the Release 2.0 features passed; pilot year and KPI measurement begin",
    "M6": "La Loy migrated to the productized service; Free-plan sign-up released; hand-over to the support routine",
    "M7": "Pilot review against the seven success criteria of the charter; expansion decision of the software house; lessons learned; sign-off",
}

# ----------------------------------------------------------------------------------------------------- WBS and tasks
# Level 2 of the WBS: id, name (noun), kind
LEVEL2 = [
    ("1", "Project Management", "project management (runs through all phases)"),
    ("2", "Inception (I1, I2)", "Vision, use-case model, LCO"),
    ("3", "Elaboration (E1, E2)", "requirements, architecture, prototype, test plan, LCA"),
    ("4", "Release 1.0 Core: Construction (C1, C2)", "features F1 to F28, IOC"),
    ("5", "Release 1.0 Core: Transition (T1)", "acceptance, training, migration, go-live"),
    ("6", "Release 2.0 Growth (C3, T2)", "features F29 to F35, go-live"),
    ("7", "Pilot operation (P1)", "concert-night support"),
    ("8", "Release 2.1 Product (C4, T3)", "productization, migration of La Loy"),
]
PM, SA, RS, QA = "PM", "SA", "RS", "QA"
OWNER, MGR, STAFF, CUST, GATEWAY, LINE, SPONSOR = ("Owner", "Manager", "Front Staff", "Customers",
                                                    "Gateway provider", "LINE Platform", "Sponsor (partners)")

# Task = one work package of the WBS and its activity. Fields:
#   id, work package (noun), activity (verb), iteration(s), start, end, predecessors ("4.1", "4.2 SS"),
#   hours {member: h}, accountable owner, consulted, feature ids or content, expected output, phase pool,
#   method ("bottom-up" | "three-point"), three-point (O, M, P) or None, other costs [(item, THB, year)]
T = []


def task(id, wp, act, it, start, end, preds, hours, owner, consulted, content, output, phase,
         method="bottom-up", tp=None, other=()):
    T.append(dict(id=id, wp=wp, act=act, it=it, start=D(start), end=D(end), preds=preds, hours=hours, owner=owner,
                  consulted=consulted, content=content, output=output, phase=phase, method=method, tp=tp,
                  other=list(other)))


# 1 Project Management
task("1.1", "Project plans and baselines", "Produce the business case, the project charter, the organization, the Software Development Plan and the iteration plans I1 and I2",
     "I1, I2", "2026-08-03", "2026-09-02", [], {PM: 20}, PM, [SPONSOR, OWNER],
     "Milestone 1 artifacts", "Business Case, charter, organization chart, SDP (draft), iteration plans", "Inception")
task("1.2", "Risk List and Development Case", "Write the initial Risk List (RISK-01 to RISK-14) and the Development Case that tailors RUP for the project",
     "I1, I2", "2026-08-10", "2026-09-02", ["2.1 SS"], {PM: 4, QA: 8}, QA, [],
     "Process tailoring, risks", "Development Case v1, Risk List", "Inception")
task("1.3", "Iteration assessments and change control, Elaboration", "Run the weekly status assessments, the E1 and E2 iteration assessments and the Change Control Board",
     "E1, E2", "2026-09-03", "2026-10-23", ["1.1"], {PM: 28}, PM, [MGR],
     "Monitoring and control", "Status assessments, iteration assessments, change-request decisions", "Elaboration")
task("1.4", "Iteration assessments and change control, Release 1.0 Construction", "Run the weekly status assessments, the C1 and C2 iteration assessments and the Change Control Board",
     "C1, C2", "2026-10-26", "2027-02-26", ["1.3"], {PM: 64}, PM, [MGR],
     "Monitoring and control", "Status assessments, iteration assessments, change-request decisions, Risk List updates", "Construction R1.0")
task("1.5", "Iteration assessments and change control, Release 1.0 Transition", "Run the weekly status assessments, the T1 assessment and the Change Control Board",
     "T1", "2027-03-01", "2027-04-02", ["1.4"], {PM: 12}, PM, [MGR],
     "Monitoring and control", "Status assessments, go-live record", "Transition R1.0")
task("1.6", "Iteration assessments and change control, Release 2.0", "Run the weekly status assessments, the C3 and T2 iteration assessments and the Change Control Board",
     "C3, T2", "2027-04-05", "2027-07-30", ["1.5"], {PM: 46}, PM, [MGR],
     "Monitoring and control", "Status assessments, iteration assessments, change-request decisions", "Construction R2.0|Transition R2.0")
task("1.7", "Iteration assessments and change control, Release 2.1", "Run the status assessments, the C4 and T3 iteration assessments and the Change Control Board",
     "C4, T3", "2027-08-02", "2028-02-11", ["1.6"], {PM: 28}, PM, [SPONSOR],
     "Monitoring and control", "Status assessments, iteration assessments, change-request decisions", "Construction R2.1|Transition R2.1")
task("1.8", "Pilot KPI reports and reviews", "Collect the pilot KPIs of every concert night (booking time, double bookings, no-shows, check-in time, operating cost) and review them monthly with the Owner",
     "P1", "2027-08-02", "2028-07-21", ["6.7"], {PM: 12, QA: 8}, PM, [OWNER, MGR],
     "Pilot KPIs", "Monthly pilot KPI reports, waiting list of restaurants", "Pilot operation and close-out")
task("1.9", "Pilot review, expansion decision and close-out", "Review the pilot year against the success criteria of the charter, prepare the expansion decision, record lessons learned and obtain sign-off",
     "CL", "2028-07-24", "2028-07-28", ["1.8 FF", "8.6"], {PM: 8, SA: 4, QA: 4}, PM, [SPONSOR, OWNER],
     "Closing", "Pilot review, expansion decision record, hand-over record, lessons learned, sign-off", "Pilot operation and close-out")

# 2 Inception
task("2.1", "Stakeholder requests and problem analysis", "Interview the Owner and the Manager, observe concert nights, record the stakeholder requests, the problems and their root causes (5 Whys)",
     "I1", "2026-08-03", "2026-08-21", [], {PM: 4, SA: 16, RS: 8}, SA, [OWNER, MGR, STAFF],
     "P-01 to P-06, RC-01 to RC-07", "Stakeholder Requests, problem and root-cause tables (workshop of RISK-01)", "Inception")
task("2.2", "Vision and Glossary", "Write the Vision (problem statement, stakeholders, features F1 to F37 with value, cost and priority) and the Glossary",
     "I1, I2", "2026-08-10", "2026-09-02", ["2.1 SS"], {SA: 20, RS: 12}, SA, [OWNER, MGR],
     "F1 to F37", "Vision v1, Glossary", "Inception")
task("2.3", "Use-case model and release plan", "Outline the use-case model and assign the features to Release 1.0, Release 2.0 and Future",
     "I2", "2026-08-25", "2026-09-02", ["2.2 SS"], {SA: 4, RS: 12, QA: 4}, RS, [MGR],
     "Release 1.0: F1 to F28; Release 2.0: F29 to F35; Future: F36, F37", "Use-Case Model (outline), release plan", "Inception")
task("2.4", "Review records and LCO package", "Review the Inception artifacts against the RUP checkpoints, record the Review Records and assemble the LCO review",
     "I2", "2026-08-27", "2026-09-02", ["2.2 SS", "2.3 SS"], {PM: 4, QA: 12}, QA, [OWNER],
     "LCO", "Review Records, LCO decision", "Inception")

# 3 Elaboration
task("3.1", "Use-case specifications", "Specify the two main use cases, Reserve a concert table and Check in with e-ticket, with the Manager and the Front Staff",
     "E1", "2026-09-03", "2026-09-16", ["2.4"], {SA: 16, RS: 32, QA: 4}, RS, [MGR, STAFF],
     "F2 to F8, F15 to F20", "Use-case specifications", "Elaboration")
task("3.2", "Software Requirements Specification and Supplementary Specification", "Write the SRS and the Supplementary Specification with the quality targets of Table 2.19 of Milestone 1",
     "E1, E2", "2026-09-10", "2026-10-09", ["3.1 SS"], {PM: 4, SA: 12, RS: 28, QA: 8}, RS, [MGR],
     "F1 to F35, NFR", "SRS, Supplementary Specification", "Elaboration")
task("3.3", "Analysis model and Software Architecture Document", "Produce the analysis model and the Software Architecture Document (LIFF front end, back office, application server, central database, LINE and gateway integration)",
     "E2", "2026-09-17", "2026-10-16", ["3.1"], {PM: 4, SA: 48, RS: 8}, SA, [],
     "Table 2.12 components", "Analysis Model, SAD", "Elaboration")
task("3.4", "User-interface prototype", "Prototype the customer and back-office screens and have the Manager, the Front Staff and sample customers try them",
     "E2", "2026-09-24", "2026-10-16", ["3.1"], {SA: 4, RS: 24, QA: 4}, RS, [MGR, STAFF, CUST],
     "Customer and back-office screens", "UI prototype, trial records", "Elaboration")
task("3.5", "Payment gateway and LINE sandbox", "Open the gateway sandbox and the LINE Developers channel, verify the merchant onboarding and the LIFF and Messaging API settings (RISK-03, external dependency)",
     "E2", "2026-09-17", "2026-10-09", ["2.4"], {PM: 8, SA: 12, RS: 4}, SA, [GATEWAY, LINE, OWNER],
     "CON-07, RISK-03", "Sandbox accounts, onboarding checks, feasibility record", "Elaboration")
task("3.6", "Test plan and test cases", "Write the test plan and the test cases of the two main use cases, including the load-test design for 5 transactions a second (RISK-05)",
     "E2", "2026-09-24", "2026-10-23", ["3.1"], {PM: 4, QA: 32}, QA, [],
     "Table 2.19 targets", "Test plan, test cases, load-test design", "Elaboration")
task("3.7", "Requirements reviews, SRS baseline and LCA package", "Review the SRS, the SAD, the prototype and the test plan against the checkpoints, baseline the SRS and assemble the LCA review",
     "E2", "2026-10-12", "2026-10-23", ["3.2", "3.3 SS", "3.4 SS", "3.6 SS"], {PM: 8, SA: 4, QA: 16}, QA, [OWNER],
     "LCA", "Review Records, SRS baseline, LCA decision", "Elaboration")
task("3.8", "Scope baseline, estimates, schedule and cost baseline", "Produce the scope statement, the WBS and dictionary, the effort, resource and cost estimates, the schedule and cost baseline (this document) and the Construction plan",
     "E2", "2026-10-12", "2026-10-23", ["3.2 SS"], {PM: 8}, PM, [SPONSOR],
     "Milestone 2 artifacts", "Scope statement, WBS, estimates, schedule and cost baseline, Construction plan", "Elaboration")

# 4 Release 1.0 Core, Construction
task("4.1", "Concert rounds, zones and packages", "Design, implement and unit-test the management of concert rounds, zones, table types, packages and prices",
     "C1", "2026-10-26", "2026-11-13", ["3.7"], {PM: 8, SA: 16, RS: 32, QA: 8}, RS, [MGR],
     "F10, F11", "Back-office round and layout functions, unit tests", "Construction R1.0")
task("4.2", "Table map, selection and hold", "Implement the round list, the real-time table map, the table selection with the 15-minute hold and the automatic hold release",
     "C1", "2026-11-02", "2026-11-27", ["4.1 SS"], {PM: 8, SA: 32, RS: 36, QA: 16}, SA, [MGR],
     "F2, F3, F9, F21", "Customer table map and hold, first-lock-wins locking", "Construction R1.0",
     other=[("Test devices: Android phone and 10-inch tablet (Table 3.5 of Milestone 1)", 15000, 0)])
task("4.3", "Gateway payment and callback", "Integrate the hosted checkout, the booking terms, the payment webhook and the automatic confirmation of the booking",
     "C1", "2026-11-16", "2026-12-18", ["3.5", "4.2 SS"], {PM: 8, SA: 40, RS: 32, QA: 24}, SA, [GATEWAY],
     "F4, F7, F23", "Payment flow with automatic confirmation", "Construction R1.0", method="three-point", tp=(80, 100, 150))
task("4.4", "LINE sign-in, staff accounts and role access", "Implement LINE Login, the back-office accounts and the role-based access of Manager, Front Staff and Owner",
     "C1", "2026-11-16", "2026-12-04", ["3.7"], {SA: 16, RS: 16, QA: 8}, RS, [],
     "F1, F24", "Sign-in and staff accounts", "Construction R1.0")
task("4.5", "C1 integration and iteration test", "Integrate the C1 increment, run the iteration tests and the C1 assessment",
     "C1", "2026-12-07", "2026-12-18", ["4.1", "4.2", "4.3 SS", "4.4"], {PM: 8, SA: 8, RS: 8, QA: 24}, QA, [],
     "C1 increment", "Tested C1 increment, iteration assessment", "Construction R1.0")
task("4.6", "QR e-ticket and transactional messages", "Implement the QR e-ticket, the customer's booking list and the transactional LINE messages",
     "C2", "2027-01-04", "2027-01-22", ["4.5"], {SA: 16, RS: 32, QA: 8}, RS, [],
     "F5, F6, F8", "E-ticket and messages", "Construction R1.0")
task("4.7", "Door check-in and name lookup", "Implement the QR scan, the ticket details, the check-in, the invalid-ticket escalation, the no-show release and the name lookup",
     "C2", "2027-01-11", "2027-02-05", ["4.6 SS"], {PM: 8, SA: 16, RS: 32, QA: 16}, RS, [STAFF],
     "F15 to F20", "Front Staff check-in functions", "Construction R1.0")
task("4.8", "Live booking view and exception handling", "Implement the live booking view, the ticket escalation, the manual overrides and the degraded-mode switch",
     "C2", "2027-01-18", "2027-02-12", ["4.6"], {PM: 8, SA: 32, RS: 32, QA: 16}, SA, [MGR],
     "F12, F13, F14, F27", "Manager's live view and exception functions", "Construction R1.0")
task("4.9", "Audit trail, backup, consent and push budget", "Implement the audit trail, the daily backup with Excel export, the consent and profile access and the push-message budget",
     "C2", "2027-01-25", "2027-02-12", ["4.6"], {PM: 8, SA: 16, RS: 20, QA: 8}, RS, [],
     "F22, F25, F26, F28", "System functions of Release 1.0", "Construction R1.0")
task("4.10", "Load test, system test and IOC package", "Run the load test (5 transactions a second at booking-open time), the system test of Release 1.0 and assemble the IOC review",
     "C2", "2027-02-08", "2027-02-26", ["4.7", "4.8", "4.9"], {PM: 8, SA: 32, RS: 16, QA: 64}, QA, [],
     "Release 1.0, Table 2.19 targets", "Load-test and system-test records, IOC decision", "Construction R1.0",
     method="three-point", tp=(90, 115, 180))

# 5 Release 1.0 Core, Transition
task("5.1", "Acceptance tests of Release 1.0", "Run the acceptance tests of the two main use cases with the Manager and the Front Staff",
     "T1", "2027-03-01", "2027-03-12", ["4.10"], {PM: 8, SA: 8, RS: 12, QA: 28}, QA, [MGR, STAFF],
     "Acceptance criteria of the charter", "Acceptance records", "Transition R1.0")
task("5.2", "Training and user guide", "Train the Manager and the Front Staff and hand over the user guide",
     "T1", "2027-03-08", "2027-03-19", ["5.1 SS"], {PM: 8, RS: 16, QA: 4}, RS, [MGR, STAFF],
     "Back-office and check-in", "Training records, user guide", "Transition R1.0")
task("5.3", "Production set-up and data migration", "Set up the production hosting, the domain and the gateway merchant account of La Loy, and migrate the current bookings",
     "T1", "2027-03-15", "2027-03-26", ["5.1"], {SA: 24, RS: 10, QA: 8}, SA, [MGR, GATEWAY],
     "Current bookings, production environment", "Production system, migrated data", "Transition R1.0",
     other=[("Domain name and TLS certificate (first year)", 1200, 0)])
task("5.4", "Pilot concert nights and go-live of Release 1.0", "Support the first concert nights on site, fix the defects found and declare Release 1.0 in operation",
     "T1", "2027-03-22", "2027-04-02", ["5.2", "5.3"], {PM: 12, SA: 8, RS: 12, QA: 20}, PM, [OWNER, MGR, STAFF],
     "Release 1.0 Core", "Go-live record, Release 1.0 in operation", "Transition R1.0")

# 6 Release 2.0 Growth
task("6.1", "Scheduled reminders", "Implement the reminder scheduling and the scheduled LINE reminders within the push-message budget",
     "C3", "2027-04-05", "2027-05-07", ["5.4"], {PM: 8, SA: 32, RS: 40, QA: 20}, RS, [],
     "F32, F34", "Reminder functions", "Construction R2.0", method="three-point", tp=(80, 96, 150))
task("6.2", "Grace extension and waitlist", "Implement the grace extension, the waitlist and the waitlist offer (rules decided by the Owner, RISK-08)",
     "C3", "2027-04-26", "2027-06-04", ["6.1 SS"], {PM: 8, SA: 40, RS: 48, QA: 28}, SA, [OWNER, MGR],
     "F29, F30, F35", "Grace and waitlist functions", "Construction R2.0")
task("6.3", "Booking transfer", "Implement the official transfer of a confirmed booking to another LINE account",
     "C3", "2027-05-17", "2027-06-04", ["6.1"], {SA: 16, RS: 24, QA: 12}, RS, [],
     "F31", "Transfer function", "Construction R2.0")
task("6.4", "Reports and Excel export", "Implement the booking, revenue, artist-popularity and customer-history reports with export to Excel",
     "C3", "2027-05-24", "2027-06-18", ["6.1"], {PM: 8, SA: 24, RS: 32, QA: 16}, RS, [OWNER, MGR],
     "F33", "Reports", "Construction R2.0")
task("6.5", "C3 integration and system test", "Integrate Release 2.0, run the regression and system tests and the C3 assessment",
     "C3", "2027-06-07", "2027-06-25", ["6.2", "6.3", "6.4"], {PM: 12, SA: 32, RS: 24, QA: 44}, QA, [],
     "Release 2.0", "Tested Release 2.0, iteration assessment", "Construction R2.0")
task("6.6", "Acceptance tests and training on Release 2.0", "Run the acceptance tests of the new features with the Manager and train the staff on them",
     "T2", "2027-06-28", "2027-07-16", ["6.5"], {PM: 8, SA: 14, RS: 24, QA: 30}, QA, [MGR, STAFF],
     "F29 to F35", "Acceptance and training records", "Transition R2.0")
task("6.7", "Release 2.0 deployment and first concert nights", "Deploy Release 2.0, support the first concert nights and declare Release 2.0 in operation",
     "T2", "2027-07-12", "2027-07-30", ["6.6 SS"], {PM: 12, SA: 16, RS: 16, QA: 20}, PM, [OWNER, MGR],
     "Release 2.0 Growth", "Go-live record, Release 2.0 in operation, pilot year begins", "Transition R2.0")

# 7 Pilot operation
task("7.1", "Concert-night support and maintenance", "Support the pilot restaurant on concert nights (on-call engineer) and maintain the system: 8 hours a month, costed as operating expenditure of Year 1 in Milestone 1 (Table 3.6), outside the 2,632 development hours",
     "P1", "2027-08-02", "2028-07-28", ["6.7"], {RS: 48, QA: 48}, QA, [MGR, STAFF],
     "RISK-04 support routine", "Support log, maintenance releases", "OPEX",
     other=[("Production hosting during the pilot year (12 months x 700 THB)", 8400, 1)])

# 8 Release 2.1 Product
task("8.1", "Multi-tenant data model and tenant isolation", "Design and implement the multi-tenant data model, the tenant isolation and the migration path of La Loy's data",
     "C4", "2027-08-02", "2027-09-24", ["6.7"], {SA: 40, RS: 40, QA: 16}, SA, [],
     "Release 2.1 scope (Section 3.1 of Milestone 1)", "Multi-tenant core", "Construction R2.1", method="three-point", tp=(72, 92, 150))
task("8.2", "Plans, limits and tier enforcement", "Implement the Free, Standard and Premium plans, their limits and the automatic enforcement of the limits",
     "C4", "2027-09-20", "2027-10-29", ["8.1"], {SA: 20, RS: 40, QA: 20}, RS, [SPONSOR],
     "Table 3.1 of Milestone 1", "Plan and limit functions", "Construction R2.1")
task("8.3", "Subscription billing and company set-up", "Implement the subscription billing and the setup-fee invoicing; register the company and publish the terms of service, privacy policy and data-processing agreement",
     "C4", "2027-10-25", "2027-12-03", ["8.2 SS"], {PM: 8, SA: 24, RS: 40, QA: 24}, RS, [SPONSOR, "Legal counsel"],
     "Billing, legal set-up", "Billing functions, company registration, legal documents", "Construction R2.1",
     other=[("Company registration, terms of service, privacy policy and data-processing agreement (legal)", 15000, 1)])
task("8.4", "Self-service onboarding and service administration", "Implement the self-service onboarding of a restaurant (zone map, packages, gateway and LINE set-up) and the service administration console",
     "C4", "2027-11-15", "2027-12-24", ["8.2"], {SA: 20, RS: 40, QA: 20}, RS, [],
     "Onboarding, administration", "Onboarding and administration functions", "Construction R2.1")
task("8.5", "Security, load and integration test of Release 2.1", "Run the multi-tenant security test, the load test and the system test of Release 2.1 and the C4 assessment",
     "C4", "2027-12-13", "2028-01-14", ["8.3", "8.4 SS"], {PM: 8, SA: 12, RS: 20, QA: 28}, QA, [],
     "Release 2.1", "Test records, iteration assessment", "Construction R2.1")
task("8.6", "Migration of La Loy and release of the Free-plan sign-up", "Migrate La Loy to the productized service, release the Free-plan sign-up and hand over to the support routine",
     "T3", "2028-01-17", "2028-02-11", ["8.5"], {PM: 4, SA: 12, RS: 20, QA: 20}, SA, [OWNER, MGR],
     "Release 2.1 Product", "La Loy on the productized service, Release 2.1 in operation", "Transition R2.1")

TASK = {t["id"]: t for t in T}
LEVEL2_OTHER = {  # other costs that belong to a level-2 item as a whole (hosting by month, Table 3.6 of Milestone 1), year
    "2": [("Development and staging hosting, August 2026 (1 month x 300 THB)", 300, 0)],
    "3": [("Development and staging hosting, September to October 2026 (2 x 300 THB)", 600, 0)],
    "4": [("Development and staging hosting, November 2026 to February 2027 (4 x 300 THB)", 1200, 0)],
    "5": [("Development and staging hosting, March 2027 (300 THB)", 300, 0),
          ("Production hosting of the pilot restaurant, March 2027 (700 THB)", 700, 0)],
    "6": [("Development and staging hosting, April to July 2027 (4 x 300 THB)", 1200, 0),
          ("Production hosting of the pilot restaurant, April to July 2027 (4 x 700 THB)", 2800, 0)],
}
CONTINGENCY_RISKS = {0: "RISK-02, RISK-03, RISK-05, RISK-08, RISK-10", 1: "RISK-04, RISK-07, RISK-12"}
PILOT_FEE = finance.PILOT_FEE

# ----------------------------------------------------------------------------------------------------- derived
for t in T:
    t["dur"] = wd(t["start"], t["end"])
    t["total"] = sum(t["hours"].values())
    t["labor"] = sum(h * RATE[k] for k, h in t["hours"].items())
    t["l2"] = t["id"].split(".")[0]
    t["units"] = {k: h / (t["dur"] * HOURS_PER_DAY) for k, h in t["hours"].items()}


def pert(tp):
    o, m, p = tp
    return (o + 4 * m + p) / 6


def n(x, dec=0):
    return f"{x:,.{dec}f}" if dec else f"{round(x):,}"


# ----------------------------------------------------------------------------------------------------- checks
def phase_hours():
    """Bottom-up hours per Milestone 1 phase (tasks that span two phases are split by working days per phase)."""
    out = defaultdict(lambda: defaultdict(float))
    for t in T:
        if t["phase"] == "OPEX":
            continue
        phases = t["phase"].split("|")
        if len(phases) == 1:
            for k, h in t["hours"].items():
                out[phases[0]][k] += h
        else:                                       # split by the working days inside each iteration of the task
            its = [i.strip() for i in t["it"].split(",")]
            days = {it: wd(max(ITER[it][1], t["start"]), min(ITER[it][2], t["end"])) for it in its}
            tot = sum(days.values())
            for it in its:
                ph = ITER[it][3]
                for k, h in t["hours"].items():
                    out[ph][k] += h * days[it] / tot
    return out


def weekly_load():
    """Hours a week per member, assuming the hours of a task are spread evenly over its working days."""
    load = defaultdict(lambda: defaultdict(float))     # member -> monday -> hours
    for t in T:
        if t["phase"] == "OPEX":
            continue
        for k, h in t["hours"].items():
            per_day = h / t["dur"]
            for d in WORKDAYS[INDEX[t["start"]]:INDEX[t["end"]] + 1]:
                load[k][d - timedelta(d.weekday())] += per_day
    return load


def check(verbose=True):
    ok = True
    ph = phase_hours()
    for k in KEYS:
        tot = sum(ph[p][k] for p in ph)
        m1 = sum(w * hpw[KEYS.index(k)] for (_, w, hpw) in M1_PHASE.values())
        if abs(tot - m1) > 1e-6:
            ok = False; print(f"TOTAL MISMATCH {k}: bottom-up {tot} vs Milestone 1 {m1}")
    for y in (0, 1):
        tot = sum(ph[p][k] for p in ph for k in KEYS if (p in M1_PHASE and M1_PHASE[p][0] == y) or (p not in M1_PHASE and y == 1))
        m1 = sum(w * sum(hpw) for (yy, w, hpw) in M1_PHASE.values() if yy == y)
        if abs(tot - m1) > 1e-6:
            ok = False; print(f"YEAR MISMATCH {y}: bottom-up {tot} vs Milestone 1 {m1}")
    labor = sum(t["labor"] for t in T if t["phase"] != "OPEX")
    if labor != 846600:
        ok = False; print(f"LABOR MISMATCH {labor}")
    if verbose:
        load = weekly_load()
        for k in KEYS:
            peaks = []
            for it_id, (name, s, e, pool) in ITER.items():
                if pool is None:
                    continue
                weeks = [w for w in load[k] if s <= w + timedelta(4) and w <= e]
                avail = M1_PHASE[pool][2][KEYS.index(k)]
                mx = max((load[k][w] for w in weeks), default=0)
                peaks.append(f"{it_id} {mx:.0f}/{avail:g}" + (" !" if mx > avail * 1.3 else ""))
            print(f"  load {k}: " + ", ".join(peaks))
    return ok


# ----------------------------------------------------------------------------------------------------- CPM
def cpm():
    """Forward and backward pass over the iteration network, in working days (FS and FF relationships)."""
    dur = {i: wd(ITER[i][1], ITER[i][2]) for i in ITER}
    es, ef = {}, {}
    for i in [x[0] for x in ITERATIONS]:
        cands = [0]
        for p, rel in ITER_PRED[i]:
            cands.append(ef[p] if rel == "FS" else ef[p] - dur[i])
        es[i] = max(cands); ef[i] = es[i] + dur[i]
    end = max(ef.values())
    lf, ls = {}, {}
    for i in reversed([x[0] for x in ITERATIONS]):
        cands = [end]
        for j in ITER:
            for p, rel in ITER_PRED[j]:
                if p == i:
                    cands.append(ls[j] if rel == "FS" else lf[j])
        lf[i] = min(cands); ls[i] = lf[i] - dur[i]
    return {i: dict(dur=dur[i], es=es[i], ef=ef[i], ls=ls[i], lf=lf[i], ts=ls[i] - es[i]) for i in ITER}


CPM = cpm()
CRITICAL_ITER = {i for i, v in CPM.items() if v["ts"] == 0}


def critical_tasks():
    """Tasks on the critical path: in a critical iteration, finishing at its end, feeding the next iteration."""
    out = []
    for t in T:
        its = [i.strip() for i in t["it"].split(",")]
        last = its[-1]
        if last in CRITICAL_ITER and t["end"] == ITER[last][2] and t["phase"] != "OPEX" and not t["id"].startswith("1."):
            out.append(t["id"])
        elif t["id"] in ("1.8", "1.9"):
            out.append(t["id"])
    return out


CRITICAL_TASKS = critical_tasks()

# ----------------------------------------------------------------------------------------------------- tables
def md(rows, header):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def who(t):
    return ", ".join(f"{MEMBERS[k][0]} {t['units'][k] * 100:.0f} %" for k in KEYS if k in t["hours"])


def tables(render=False) -> dict[str, str]:
    out = {}
    # WBS outline
    rows = []
    for l2, name, kind in LEVEL2:
        rows.append((f"**{l2}**", f"**{name}**", "", "", f"*{kind}*"))
        for t in T:
            if t["l2"] == l2:
                rows.append((t["id"], t["wp"], t["it"], t["content"], t["output"]))
    out["wbs"] = md(rows, ["WBS ID", "Work package", "Iteration", "Features / content", "Deliverable (expected output)"])

    # WBS dictionary of two work packages
    def entry(t):
        return [("WBS item number", t["id"]), ("WBS item name", t["wp"]),
                ("Description", t["act"] + "."), ("Responsibility", f"{NAMES[t['owner']]} ({MEMBERS[t['owner']][1]}), accountable; " +
                 ", ".join(MEMBERS[k][0] for k in KEYS if k in t["hours"] and k != t["owner"]) + " contribute"),
                ("Input", {"4.3": "SRS and SAD baseline (3.7); sandbox and merchant account of 3.5; table hold of 4.2",
                           "4.10": "Tested C2 increment (4.7 to 4.9); test plan and load-test design (3.6); test devices",
                           "1.8": "Audit trail and reports of the system; Manager's concert-night log"}.get(t["id"], "")),
                ("Output", t["output"]), ("Features / content", t["content"]),
                ("Effort", f"{t['total']:g} h ({', '.join(f'{MEMBERS[k][0]} {h:g}' for k, h in t['hours'].items())}); method: {t['method']}" +
                 (f", O/M/P {t['tp'][0]}/{t['tp'][1]}/{t['tp'][2]} h, PERT {pert(t['tp']):.1f} h" if t["tp"] else "")),
                ("Duration", f"{t['dur']} working days, {fmt_date(t['start'])} to {fmt_date(t['end'])}"),
                ("Predecessors", ", ".join(t["preds"]) or "none"), ("Labor cost", f"{n(t['labor'])} THB"),
                ("Acceptance criteria", {"4.3": "A sandbox payment of the full table fee confirms the booking automatically within 10 seconds of the gateway's webhook; a timed-out hold rejects the payment; the webhook signature is verified; the degraded-mode switch (4.8) takes over when the gateway does not answer",
                                         "4.10": "50 concurrent reservations of the same table yield one hold and 49 rejections without deadlock; 5 transactions a second sustained for 10 minutes with responses within 2 seconds; every system test case of the two main use cases passes; the IOC review is accepted",
                                         "1.8": "A KPI report every month of the pilot year with the five KPIs of Table 2.23; reviewed with the Owner; the waiting list kept current"}.get(t["id"], ""))]
    for tid in ("4.3", "4.10"):
        out[f"dict_{tid.replace('.', '_')}"] = md(entry(TASK[tid]), ["Field", f"WBS {tid} {TASK[tid]['wp']}"])

    # schedule table of activities
    rows = []
    for l2, name, _ in LEVEL2:
        rows.append((f"**{l2}**", f"**{name}**", "", "", "", "", ""))
        for t in T:
            if t["l2"] == l2:
                rows.append((t["id"], t["act"], t["dur"], fmt_date(t["start"]), fmt_date(t["end"]),
                             ", ".join(t["preds"]) or "—", who(t)))
    for mid, name, d, after in MILESTONES:
        rows.append((mid, f"*{name}*", 0, fmt_date(D(d)), fmt_date(D(d)), after, "—"))
    out["schedule"] = md(rows, ["WBS ID", "Activity", "Duration (working days)", "Start", "Finish", "Predecessors", "Resources (units)"])

    # effort per task
    rows, tot = [], defaultdict(float)
    for l2, name, _ in LEVEL2:
        rows.append((f"**{l2}**", f"**{name}**", "", "", "", "", "", "", ""))
        for t in T:
            if t["l2"] != l2:
                continue
            h = t["hours"]
            opex = t["phase"] == "OPEX"
            rows.append((t["id"], t["wp"] + (" (operating expenditure, outside the 2,632 h)" if opex else ""),
                         t["method"], *(f"{h[k]:g}" if k in h else "-" for k in KEYS), f"{t['total']:g}", n(t["labor"])))
            if not opex:
                for k in KEYS:
                    tot[k] += h.get(k, 0)
    rows.append(("**Total development effort**", "", "", *(f"**{tot[k]:g}**" for k in KEYS), f"**{sum(tot.values()):g}**",
                 f"**{n(sum(tot[k] * RATE[k] for k in KEYS))}**"))
    rows.append(("Rate (THB/h)", "", "", *(str(RATE[k]) for k in KEYS), "", ""))
    rows.append(("**Labor cost (THB)**", "", "", *(f"**{n(tot[k] * RATE[k])}**" for k in KEYS), "", f"**{n(sum(tot[k] * RATE[k] for k in KEYS))}**"))
    out["effort"] = md(rows, ["WBS ID", "Work package", "Method", *(f"{MEMBERS[k][0]} ({k})" for k in KEYS), "Hours", "Labor (THB)"])
    out["effort_short"] = "\n".join(l for l in out["effort"].split("\n") if not l.startswith("| 7."))

    # three-point estimates
    rows = []
    for t in T:
        if t["tp"]:
            o, m, p = t["tp"]; pe = pert(t["tp"])
            rows.append((t["id"], t["wp"], o, m, p, f"{pe:.1f}", f"{t['total']:g}", f"{(t['total'] - pe) / pe * 100:+.1f} %"))
    out["three_point"] = md(rows, ["WBS ID", "Work package", "Optimistic O (h)", "Most likely M (h)", "Pessimistic P (h)",
                                   "PERT (O + 4M + P) / 6", "Allocated (h)", "Allocated vs PERT"])

    # per-phase comparison with Milestone 1
    ph = phase_hours(); rows = []
    for p in PHASE_ORDER:
        bu = sum(ph[p][k] for k in KEYS)
        td = M1_PHASE[p][1] * sum(M1_PHASE[p][2]) if p in M1_PHASE else 0
        diff = abs(bu - td) / ((bu + td) / 2) * 100 if (bu + td) else 0
        rows.append((PHASE_LABEL[p], *(f"{ph[p][k]:g}" for k in KEYS), f"{bu:g}", f"{td:g}", f"{bu - td:+g}", f"{diff:.1f} %"))
    bu = sum(ph[p][k] for p in ph for k in KEYS); td = sum(M1_PHASE[p][1] * sum(M1_PHASE[p][2]) for p in M1_PHASE)
    rows.append(("**Total**", *(f"**{sum(ph[p][k] for p in ph):g}**" for k in KEYS), f"**{bu:g}**", f"**{td:g}**", f"**{bu - td:+g}**", f"**{abs(bu - td) / ((bu + td) / 2) * 100:.1f} %**"))
    out["effort_phase"] = md(rows, ["Phase", *(MEMBERS[k][0] for k in KEYS), "Bottom-up (h)", "Milestone 1 top-down (h)", "Difference (h)", "Percent difference"])

    # resource rates and availability
    rows = []
    for k in KEYS:
        avail = "; ".join(f"{PHASE_LABEL[p].split(' (')[0].replace('Construction Release', 'C').replace('Transition Release', 'T')} {M1_PHASE[p][2][KEYS.index(k)]:g}" for p in M1_PHASE)
        rows.append((NAMES[k], MEMBERS[k][1], "Work (human)", f"{RATE[k]} THB/h", f"{avail} h/week"))
    for r in PHYSICAL:
        rows.append((r[0], r[2], r[1], r[3], r[4]))
    out["rates"] = md(rows, ["Resource", "Role / use", "Type", "Rate or cost basis", "Availability (hours a week per phase) / when"])

    # availability check per phase
    load = weekly_load(); rows = []
    for p in PHASE_ORDER:
        if p not in M1_PHASE:
            continue
        cells = []
        for k in KEYS:
            avail = M1_PHASE[p][2][KEYS.index(k)]
            its = [i for i in ITER if ITER[i][3] == p]
            weeks = [w for w in load[k] if any(ITER[i][1] <= w + timedelta(4) and w <= ITER[i][2] for i in its)]
            mx = max((load[k][w] for w in weeks), default=0)
            cells.append(f"{ph[p][k] / M1_PHASE[p][1]:.1f} avg, {mx:.0f} peak / {avail:g}")
        rows.append((PHASE_LABEL[p], f"{M1_PHASE[p][1]}", *cells))
    out["load"] = md(rows, ["Phase", "Weeks", *(f"{MEMBERS[k][0]}: hours a week (planned avg, peak / available)" for k in KEYS)])

    # RACI
    rows = []
    ext = [OWNER, MGR, STAFF]
    for l2, name, _ in LEVEL2:
        rows.append((f"**{l2}**", f"**{name}**", "", "", "", "", "", ""))
        for t in T:
            if t["l2"] != l2:
                continue
            cells = []
            for k in KEYS:
                if k == t["owner"]:
                    cells.append("A/R")
                elif k in t["hours"]:
                    cells.append("R")
                else:
                    cells.append("I")
            cells.append("C" if OWNER in t["consulted"] else ("I" if t["id"] in ("1.9", "5.4", "6.7", "8.6", "2.4", "3.7") else "-"))
            cells.append("C" if (MGR in t["consulted"] or STAFF in t["consulted"]) else "-")
            cells.append(", ".join(c for c in t["consulted"] if c not in (OWNER, MGR, STAFF)) or "-")
            rows.append((t["id"], t["wp"], *cells))
    out["raci"] = md(rows, ["WBS ID", "Work package", *(f"{MEMBERS[k][0]} ({MEMBERS[k][1].split(',')[0]})" for k in KEYS),
                            "Restaurant Owner", "Manager / Front Staff", "Other consulted"])

    # cost by WBS item (level 2)
    rows = []; tot_h = tot_l = tot_o = 0; year_cost = {0: 0.0, 1: 0.0}
    for l2, name, _ in LEVEL2:
        ts = [t for t in T if t["l2"] == l2]
        hours = sum(t["total"] for t in ts if t["phase"] != "OPEX")
        labor = sum(t["labor"] for t in ts if t["phase"] != "OPEX")
        opex_labor = sum(t["labor"] for t in ts if t["phase"] == "OPEX")
        other_items = [o for t in ts for o in t["other"]] + LEVEL2_OTHER.get(l2, [])
        other = sum(o[1] for o in other_items) + opex_labor
        for t in ts:
            for o in t["other"]:
                year_cost[o[2]] += o[1]
            if t["phase"] == "OPEX":
                year_cost[1] += t["labor"]
            else:
                year_cost[0 if (t["phase"].split("|")[0] in M1_PHASE and M1_PHASE[t["phase"].split("|")[0]][0] == 0) else 1] += t["labor"]
        for o in LEVEL2_OTHER.get(l2, []):
            year_cost[o[2]] += o[1]
        basis = "; ".join(f"{MEMBERS[k][0]} {sum(t['hours'].get(k, 0) for t in ts if t['phase'] != 'OPEX'):g} h x {RATE[k]}" for k in KEYS if any(k in t["hours"] for t in ts if t["phase"] != "OPEX"))
        other_txt = "; ".join(f"{o[0].split(' (')[0]} {n(o[1])}" for o in other_items if o[1]) + (f"; support labor 96 h x 300 = {n(opex_labor)}" if opex_labor else "")
        rows.append((l2, name, f"{hours:g}", basis, n(labor), other_txt or "-", n(labor + other)))
        tot_h += hours; tot_l += labor; tot_o += other
    rows.append(("", "**Work-package estimates**", f"**{tot_h:g}**", "", f"**{n(tot_l)}**", f"**{n(tot_o)}**", f"**{n(tot_l + tot_o)}**"))
    cont = {0: 69790, 1: 18700}
    for y in (0, 1):
        base = year_cost[y]
        rows.append(("", f"Contingency reserve, Year {y} ({CONTINGENCY_RISKS[y]})", "", f"10 % of {n(base if y == 0 else 187000)} THB" + ("" if y == 0 else " (labor of C4 and T3 and the legal set-up)"), "", "", n(cont[y])))
    baseline = tot_l + tot_o + cont[0] + cont[1]
    rows.append(("", "**Cost baseline**", "", "", "", "", f"**{n(baseline)}**"))
    rows.append(("", "Management reserve", "", "none held by the sponsor for this project (unknown unknowns escalate to the partners' meeting)", "", "", "0"))
    rows.append(("", "**Project budget (charter)**", "", "", "", "", f"**{n(baseline)}**"))
    rows.append(("", "Less: pilot implementation fee of La Loy (revenue inside the project)", "", "", "", "", f"({n(PILOT_FEE)})"))
    rows.append(("", "**Net investment of the software house**", "", "", "", "", f"**{n(baseline - PILOT_FEE)}**"))
    out["cost"] = md(rows, ["WBS", "Item", "Hours", "Labor basis (hours x THB/h)", "Labor (THB)", "Other costs (THB)", "Subtotal (THB)"])
    out["_baseline"] = str(baseline)

    # time-phased cost baseline by iteration
    rows = []; cum = 0.0
    labor_by_iter = defaultdict(float); other_by_iter = defaultdict(float)
    for t in T:
        for i_id, (name, s, e, pool) in ITER.items():
            a, b = max(s, t["start"]), min(e, t["end"])
            if a > b or i_id == "CL" and t["id"] != "1.9" or (i_id == "P1" and t["id"] not in ("1.8", "7.1")) or (i_id != "P1" and t["id"] in ("1.8", "7.1")):
                continue
            share = wd(a, b) / t["dur"]
            if t["phase"] == "OPEX":
                other_by_iter[i_id] += t["labor"] * share
            else:
                labor_by_iter[i_id] += t["labor"] * share
        for o in t["other"]:
            first = t["it"].split(",")[0].strip()
            other_by_iter[first] += o[1]
    for l2, items in LEVEL2_OTHER.items():
        its = sorted({i.strip() for t in T if t["l2"] == l2 for i in t["it"].split(",")}, key=lambda i: ITER[i][1])
        for o in items:
            other_by_iter[its[0] if "March" in o[0] or len(its) == 1 else its[-1] if "July" in o[0] else its[0]] += o[1]
    year_of = {i: (0 if ITER[i][2] <= date(2027, 7, 30) else 1) for i in ITER}
    ysum = {y: sum(labor_by_iter[i] + other_by_iter[i] for i in ITER if year_of[i] == y) for y in (0, 1)}
    for i_id, (name, s, e, pool) in ITER.items():
        lab, oth = labor_by_iter[i_id], other_by_iter[i_id]
        c = cont[year_of[i_id]] * (lab + oth) / ysum[year_of[i_id]]
        sub = lab + oth + c; cum += sub
        rows.append((i_id, name, f"{fmt_date(s)} to {fmt_date(e)}", n(lab), n(oth), n(c), n(sub), n(cum)))
    rows.append(("", "**Total**", "", f"**{n(sum(labor_by_iter.values()))}**", f"**{n(sum(other_by_iter.values()))}**",
                 f"**{n(cont[0] + cont[1])}**", f"**{n(cum)}**", ""))
    out["cost_phased"] = md(rows, ["Iteration", "Name", "Period", "Labor (THB)", "Other costs (THB)", "Contingency (THB)", "Subtotal (THB)", "Cumulative (THB)"])
    out["_phased_total"] = str(round(cum))

    # CPM table
    rows = []
    for i_id, (name, s, e, pool) in ITER.items():
        v = CPM[i_id]
        preds = ", ".join(f"{p}" + ("" if rel == "FS" else f" ({rel})") for p, rel in ITER_PRED[i_id]) or "—"
        rows.append((i_id, name, v["dur"], preds, v["es"], v["ef"], v["ls"], v["lf"], v["ts"], "Yes" if v["ts"] == 0 else "No",
                     fmt_date(WORKDAYS[v["es"]]), fmt_date(WORKDAYS[v["ef"] - 1])))
    out["cpm"] = md(rows, ["ID", "Iteration", "Duration (wd)", "Predecessors", "ES", "EF", "LS", "LF", "Total slack (wd)", "Critical", "Early start", "Early finish"])
    out["_project_wd"] = str(max(v["ef"] for v in CPM.values()))
    out["_t3_slack"] = str(CPM["T3"]["ts"])

    # critical tasks
    rows = [(tid, TASK[tid]["wp"], TASK[tid]["it"], fmt_date(TASK[tid]["end"]),
             next((m[1] for m in MILESTONES if m[3] == tid), "feeds the next iteration")) for tid in CRITICAL_TASKS]
    out["critical_tasks"] = md(rows, ["WBS ID", "Work package", "Iteration", "Finish", "Milestone or successor"])

    # milestones
    rows = [(mid, name, fmt_date(D(d)), after, MILESTONE_DECISION[mid]) for mid, name, d, after in MILESTONES]
    out["milestones"] = md(rows, ["ID", "Milestone", "Date", "After", "Acceptance / decision"])

    if render:
        render_gantt()
    return out


# ----------------------------------------------------------------------------------------------------- Gantt (SVG)
def render_gantt():
    """Task-level Gantt chart with the iteration bands, the milestones and the critical path; SVG and PNG."""
    import base64
    left, top, row_h, right, bottom = 840, 150, 30, 60, 120
    rows = [t for t in T] + [None] * len(MILESTONES)
    width = 3500                                           # wider than 1.6 x height: a landscape page
    height = top + row_h * len(rows) + bottom
    plot_w = width - left - right
    d0, d1 = date(2026, 8, 1), date(2028, 8, 1)
    span = (d1 - d0).days

    def x(d):
        return left + (d - d0).days / span * plot_w

    navy, red, gold, gray, ink = "#0b2a4a", "#8b1a1a", "#c9a227", "#9ca3af", "#1f2937"
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="Laksaman, \'TH Sarabun\', sans-serif" font-size="22">',
         f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
         f'<text x="{left}" y="40" font-size="34" font-weight="bold" fill="{navy}">Schedule of the SEATS project by work package, 3 August 2026 to 28 July 2028</text>',
         f'<text x="{left}" y="72" font-size="22" fill="#374151">Bars: work packages (activities) · red with dark outline: critical path · diamonds: milestones · bands: iterations of the tailored RUP</text>']
    # month grid
    m = date(2026, 8, 1)
    while m <= d1:
        xx = x(m)
        s.append(f'<line x1="{xx:.1f}" y1="{top - 10}" x2="{xx:.1f}" y2="{height - bottom + 10}" stroke="#e5e7eb" stroke-width="1"/>')
        if m.month in (1, 4, 7, 10):
            s.append(f'<text x="{xx + 4:.1f}" y="{height - bottom + 30}" fill="#374151">{m.strftime("%b %Y")}</text>')
        m = date(m.year + (m.month == 12), m.month % 12 + 1, 1)
    # iteration bands
    for i_id, (name, a, b, pool) in ITER.items():
        if i_id in ("P1", "CL"):
            continue
        xa, xb = x(a), x(b + timedelta(1))
        s.append(f'<rect x="{xa:.1f}" y="{top - 40}" width="{xb - xa:.1f}" height="{row_h * len(rows) + 40}" fill="{"#f3f4f6" if i_id in ("I2", "E2", "C2", "C3", "C4") else "#fafafa"}" opacity="0.9"/>')
        s.append(f'<text x="{(xa + xb) / 2:.1f}" y="{top - 16}" text-anchor="middle" font-weight="bold" fill="{navy}">{i_id}</text>')
    xa, xb = x(ITER["P1"][1]), x(ITER["P1"][2] + timedelta(1))
    s.append(f'<text x="{xb - 8:.1f}" y="{top - 16}" text-anchor="end" font-weight="bold" fill="{navy}">P1 pilot year</text>')
    # rows
    y = top
    for t in T:
        crit = t["id"] in CRITICAL_TASKS
        band = t["l2"]
        s.append(f'<text x="{left - 12}" y="{y + row_h * 0.68:.1f}" text-anchor="end" fill="{ink}" font-weight="{"bold" if crit else "normal"}">{t["id"]} {t["wp"]}</text>')
        xa, xb = x(t["start"]), x(t["end"] + timedelta(1))
        fill = red if crit else navy
        if t["id"] == "7.1":
            fill = gray
        s.append(f'<rect x="{xa:.1f}" y="{y + 6}" width="{max(xb - xa, 4):.1f}" height="{row_h - 12}" rx="3" fill="{fill}" opacity="{"1" if crit else "0.85"}" stroke="{"#111827" if crit else "none"}" stroke-width="{3 if crit else 0}"/>')
        label = ", ".join(f"{MEMBERS[k][0].split()[0]} {h:g}h" for k, h in t["hours"].items())
        if xb + 12 * len(label) > width - right:
            s.append(f'<text x="{xa - 8:.1f}" y="{y + row_h * 0.68:.1f}" text-anchor="end" fill="#374151" font-size="19">{label}</text>')
        else:
            s.append(f'<text x="{xb + 8:.1f}" y="{y + row_h * 0.68:.1f}" fill="#374151" font-size="19">{label}</text>')
        y += row_h
    for mid, name, d, after in MILESTONES:
        xx = x(D(d))
        s.append(f'<text x="{left - 12}" y="{y + row_h * 0.68:.1f}" text-anchor="end" fill="{ink}" font-style="italic">{mid} {name}</text>')
        s.append(f'<polygon points="{xx:.1f},{y + 4} {xx + 11:.1f},{y + row_h / 2} {xx:.1f},{y + row_h - 4} {xx - 11:.1f},{y + row_h / 2}" fill="{gold}" stroke="#111827" stroke-width="2"/>')
        if xx + 160 > width - right:
            s.append(f'<text x="{xx - 16:.1f}" y="{y + row_h * 0.68:.1f}" text-anchor="end" fill="#374151" font-size="19">{fmt_date(D(d))}</text>')
        else:
            s.append(f'<text x="{xx + 16:.1f}" y="{y + row_h * 0.68:.1f}" fill="#374151" font-size="19">{fmt_date(D(d))}</text>')
        y += row_h
    # legend
    ly = height - 22
    s.append(f'<rect x="{left}" y="{ly - 14}" width="40" height="16" rx="3" fill="{navy}" opacity="0.85"/><text x="{left + 48}" y="{ly}" fill="{ink}">work package</text>')
    s.append(f'<rect x="{left + 230}" y="{ly - 14}" width="40" height="16" rx="3" fill="{red}" stroke="#111827" stroke-width="3"/><text x="{left + 278}" y="{ly}" fill="{ink}">critical path (zero total slack)</text>')
    s.append(f'<rect x="{left + 640}" y="{ly - 14}" width="40" height="16" rx="3" fill="{gray}"/><text x="{left + 688}" y="{ly}" fill="{ink}">pilot support (operating expenditure)</text>')
    s.append(f'<polygon points="{left + 1100},{ly - 16} {left + 1111},{ly - 6} {left + 1100},{ly + 4} {left + 1089},{ly - 6}" fill="{gold}" stroke="#111827" stroke-width="2"/><text x="{left + 1120}" y="{ly}" fill="{ink}">milestone</text>')
    s.append("</svg>")
    svg = "\n".join(s)
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "schedule-tasks.svg").write_text(svg, encoding="utf-8")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright missing: PNG not rendered"); return
    font = Path("/workspaces/codespace_launcher/2110628_Requirement/resources/fonts/Laksaman.ttf")
    face = f"@font-face {{ font-family: Laksaman; src: url('{font.as_uri()}'); }}" if font.is_file() else ""
    html = f"<!doctype html><html><head><meta charset='utf-8'><style>{face} body{{margin:0}}</style></head><body>{svg}</body></html>"
    with sync_playwright() as pw:
        b = pw.chromium.launch(); p = b.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        p.set_content(html, wait_until="load"); p.evaluate("document.fonts.ready")
        p.screenshot(path=str(ASSETS / "schedule-tasks.png"), full_page=True); b.close()
    print(f"rendered {ASSETS / 'schedule-tasks.png'} ({width}x{height})")


if __name__ == "__main__":
    ok = check()
    if "--check" in sys.argv:
        sys.exit(0 if ok else 1)
    for name, text in tables(render=True).items():
        if not name.startswith("_"):
            print(f"<!-- {name} -->\n{text}\n<!-- /{name} -->\n")
