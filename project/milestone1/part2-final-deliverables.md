<!-- Source of the Milestone 1 "Part 2 Final Deliverables" PDF of course 2110722 Software Project Management.
     "include:" blocks quote the CTRS artifacts of the Requirements Engineering project (assignments/group/project/)
     and are expanded IN PLACE by tools/build_pm_report.py; "finance:" blocks are generated from tools/finance.py.
     Edit the prose here; edit quoted tables in the artifacts; edit figures in tools/finance.py. -->

# Executive Summary

La Loy is a medium-sized live-music restaurant in Bangkok that sells every table of a concert night in advance as a package, and today does so entirely through one-to-one LINE chats handled by the Manager, with table status kept in a hand-edited image, holds in the Manager's memory and payment slips checked by eye. The Concert Table Reservation System (CTRS) replaces this process with a LINE-integrated self-service reservation flow (table map, 15-minute hold, full payment through a payment gateway, QR e-ticket) and a shared back-office for the Manager, Owner and Front Staff, all on one central record.

The four members of the team are engineers of one software house, and CTRS is that software house's product. It is built for La Loy under a pilot implementation agreement as a tailored Rational Unified Process (RUP) project, run for La Loy alone during a pilot year while it is productized, and then offered to other live-music restaurants as a subscription service priced within the restaurant's own 1,000 THB a month ceiling. This document is Milestone 1 of the project's management: the business case with its financial analysis, the project charter and the project organization. Its key figures are:

- **Schedule.** 3 August 2026 to 28 July 2028 (two years): Release 1.0 Core in operation at La Loy on 2 April 2027, Release 2.0 Growth on 30 July 2027, the productized Release 2.1 on 11 February 2028, and the expansion decision at the end of the pilot year.
- **Budget.** 1,010,590 THB for the build, the pilot and the productization (Years 0 and 1, labor at the software house's cost rates, contingency reserves included), of which La Loy's pilot implementation fee covers 150,000 THB; the software house's net investment is 860,590 THB.
- **Revenue and return.** Three plans, Free, Standard (690 THB a month) and Premium (990 THB a month), plus a setup fee; 130 paying restaurants by Year 5 give revenues of 2,526,000 THB over Years 0 to 5 and, at a 10 % discount rate, an NPV of 18,971 THB, an ROI of 22 %, a discounted payback of 5.0 years and an IRR of 11 %. The case is marginal within five years and positive from Year 6 on; adoption is the decisive lever, so the expansion is authorized only at the gate at the end of the pilot year. The restaurant's own benefits are not counted.

# Document Revision History

| Version | Date | Description | Author |
|---|---|---|---|
| 1.0 | 10 September 2026 | Milestone 1: Review Board Decision Log, business case, financial analysis, project charter, project organization chart | SE69 Group 1 |

# 1. Review Board Decision Log

Before submission the four members meet as the Review Board and decide, for every artifact of this milestone, whether the prompted and revised result is accepted, revised or rejected. Table 1.1 records the decisions; the prompt design of each artifact is documented in the GenAI Log file (Part 1).

*Table 1.1 Review Board Decision Log, Milestone 1*

| No. | Artifact | Member (prompt design) | Suggestion from team (in brief) | Decision (Accept / Revise / Reject) |
|---|---|---|---|---|
| 1 | Business case: background, business objective, current situation and problem (Sections 2.1 to 2.3) | Sirapatr C. | Present the team as a software house engaged by La Loy, not as a student project. Add the 5 Whys, a root-cause table and the business requirements so that problem, root cause and requirement can be read in sequence without the Vision. | Revise |
| 2 | Business case: critical assumptions and constraints (Section 2.4) | Chawanakorn S. | The 1,000 THB a month operating-cost ceiling is the constraint the pricing plans must respect; keep it as stated. | Accept |
| 3 | Business case: analysis of options and recommendation (Section 2.5) | Sirapatr C. | Re-state the in-house option as the software house's build under a pilot implementation agreement, with the pilot fee and the product investment reflected in its cost, time and risk. | Revise |
| 4 | Business case: preliminary project requirements (Section 2.6) | Chawanakorn S. | Add the goal and date of each release, the value, cost and priority of each feature and the preliminary quality targets. Drop the trace columns; this is not a requirements document. | Revise |
| 5 | Business case: schedule estimate, development process and potential risks (Sections 2.8 to 2.10) | Boonnisa T. | The development-process figure described the requirements work; redraw it from the project-management view (PMBOK process groups over the tailored RUP). Extend the schedule to the pilot year and the expansion decision. | Revise |
| 6 | Financial analysis: business model, revenue plan, cost model and budget estimate (Sections 2.7 and 3.1 to 3.3) | Watayut A. | Cost the project from the software house's side: Year 0 build plus Year 1 pilot and productization, hosting per subscriber and the legal set-up of the subscription business. Offer Free, Standard and Premium plans within the operating-cost ceiling. | Revise |
| 7 | Financial analysis: revenue, cost-benefit analysis, sensitivity and expansion gate (Sections 3.4 to 3.7) | Watayut A. | Do not add La Loy's savings to the software house's benefits; count only the pilot fee and the subscription revenue. Show the sensitivity to adoption and price, and define the criteria of the expansion decision. | Revise |
| 8 | Project charter and stakeholder list (Section 4) | Boonnisa T. | Remove the lecturers from the stakeholder list; they are not stakeholders of the software house's project. Name the software house as sponsor and La Loy as the pilot customer. | Revise |
| 9 | Project organization chart (Section 5) | Boonnisa T. | Remove the lecturer node and show the two parties of the pilot agreement, the project team, the user side and the change control board. | Revise |

Artifacts marked Revise were revised as suggested before submission, and the sections of this document are the revised versions; the review and the revision of each artifact are recorded in the Review and Revision fields of its GenAI Log record (Part 1).

# 2. Business Case

## 2.1 Background

La Loy is a medium-sized live-music restaurant and bar, open daily from 17:00 to 02:00. In the early evening it serves food and drinks; from 19:00 it serves alcoholic beverages together with a full live show. On ordinary nights it takes walk-ins and phone bookings. On nights with a concert by a well-known artist every table is sold in advance as a package: tables are grouped into Zone A (2-person round tables at 2,400 THB, 4-person square tables at 4,800 THB, 6-person sofas at 7,200 THB) and Zone B (the same three types at 2,000, 4,000 and 6,000 THB plus 1-person seats at 700 THB); each package includes a liquor tower and ice, and an extra person costs 600 THB. This advance sale is handled entirely through LINE by the Manager alone, who answers every chat and maintains the table plan by hand. The restaurant has no IT staff, and its key people (Owner, Manager, Front Staff) work evenings and nights.

The four members of the team are engineers of one software house. The Concert Table Reservation System (CTRS) is that software house's product, built first for La Loy under a pilot implementation agreement and run as a tailored RUP project with versioned artifacts (Vision, Business Case, Use-Case Model, Software Requirements Specification, Development Case, iteration plans); after a pilot year with La Loy alone it is offered to other live-music restaurants as a subscription service. This business case therefore has two parties: the pilot restaurant, whose problem the product solves and whose situation, requirements and constraints Sections 2.2 to 2.6 describe, and the software house, whose investment, revenue plan and return the budget, schedule and risk sections and the financial analysis of Section 3 evaluate. The RUP Business Case of the requirements work is restated here in PMBOK terms; the figures it left qualitative are quantified.

## 2.2 Business Objective

The project objectives (Table 2.1) are the outcomes the project delivers; the strategic business objectives (Table 2.2) are the restaurant-level results the Owner expects from them, with the targets the Vision is held against. The baselines of the targets have not been measured yet and are to be validated with the Owner.

*Table 2.1 Project objectives*

| No. | Objective |
|---|---|
| 1 | Study and develop an online concert table reservation system connected to the restaurant's LINE Official Account, through which customers can browse concert rounds, check table availability, choose their own table and pay the full table fee conveniently and in real time. |
| 2 | Reduce errors in the booking process and prevent double booking through automatic table-status management (hold with timeout, first lock wins) and automatic verification of the full table fee. |
| 3 | Develop a back-office system through which the Manager, Owner and Front Staff manage concert rounds, table layouts, prices, bookings and check-in from one shared screen and record. |
| 4 | Store booking data and customer history centrally, to notify customers at the scheduled times of their booking and to analyze artist popularity and plan the restaurant's marketing. |

*Table 2.2 Strategic business objectives and targets*

<!-- include: ../../../assignments/group/project/management/business-case.md#4.2 Strategic business objectives no-prose -->
<!-- source: ../../../assignments/group/project/management/business-case.md · Business Case v1.7 (In review) · Develop Business Case (ac_dbzcs) -->

| Objective | Target | Means |
|---|---|---|
| Reduce the customer no-show rate | −35 % | Full table fee paid before confirmation (BRULE-01), terms accepted before paying (BRULE-16), reminders before the event and the check-in window (F32, F34) |
| Shorten booking and confirmation | ≤ 3 minutes per booking (from hours waiting for the Manager) | Self-service seat map, 15-minute hold and gateway payment with automatic confirmation (BR-01, BR-03) |
| Sell every table as fast as possible on big concert nights | Table status real-time 100 % | Central database as the single record; automatic hold release; waitlist and transfer for freed tables (BR-01, BR-02) |

<!-- /include -->

## 2.3 Current Situation and Problem

### 2.3.1 As-is tools and process

The restaurant runs its concert-night sales on communication and note-taking tools rather than on a system (Table 2.3). The as-is process has nine steps, drawn as an activity diagram in Figure 2.1: (1) the Manager announces the concert on social media and by a LINE Official Account notification; (2) an interested customer messages the Manager on LINE to ask for free tables; (3) the Manager sends the zone-map image with the taken tables marked, editing the image by hand every time the status changes; (4) the customer chooses a table and tells the Manager its number; (5) the Manager keeps the choice in mind for the duration of the chat, normally up to an hour, without any written lock, and when several customers want the same table the first transfer slip wins; (6) the Manager sends the bank account details; (7) the customer transfers the full table fee and sends the slip; (8) the Manager checks the slip by eye, confirms the reservation and writes it into Excel or the notebook; (9) on the night, check-in opens two hours before the show and the Front Staff looks the customer up by name; arrival up to 30 minutes after the start is accepted, after that the table is released to walk-in guests and the fee is not refunded.

*Table 2.3 As-is tools*

<!-- include: ../../../assignments/group/project/management/business-case.md#3.2 As-is tools no-prose -->
<!-- source: ../../../assignments/group/project/management/business-case.md · Business Case v1.7 (In review) · Develop Business Case (ac_dbzcs) -->

| Tool | Use today |
|---|---|
| LINE (Official Account and chat) | Announcements; every booking conversation; sending the zone-map image; receiving transfer slips. The Manager reads and answers each message by hand. |
| Excel / Google Sheets or a notebook | Record of bookings (date, name, phone, zone/table, party size, amount, status, remarks); table plan; artist schedule. No duplicate check; status updated by hand. |
| Facebook / Instagram | Concert schedule, artists, zone map with table types and prices. |
| Bank transfer and slip in chat | The customer transfers the full table fee in their own banking app and sends a screenshot; the Manager verifies it by eye and sends the account details by hand each time. |

<!-- /include -->

![As-is booking process](../../../assignments/group/project/business-modeling/diagrams/asis-booking-activity.png)

*Figure 2.1 As-is concert table booking process (UML activity diagram, one swimlane per participant)*

### 2.3.2 Problems

Six problems were identified from observation of the process, review of the restaurant's channels and the team's root-cause analysis; Table 2.4 ranks them by an Impact × Frequency rubric (each 1 to 5, team judgment, no incident data) and traces each to its root cause and to the business requirement that answers it.

*Table 2.4 Problems, ranked*

<!-- include: ../../../assignments/group/project/management/business-case.md#3.3 Problems, ranked no-prose -->
<!-- source: ../../../assignments/group/project/management/business-case.md · Business Case v1.7 (In review) · Develop Business Case (ac_dbzcs) -->

| Rank | ID | Problem | Impact | Freq. | Score | Root cause | Business requirement |
|---|---|---|---|---|---|---|---|
| 1 | P-02 | Double booking and data errors: table status on a hand-edited image, holds in the Manager's head, no single record; customers lose the table they picked when a faster slip arrives; disputes and refunds; confusion at the door | 5 | 4 | 20 | RC-02 | BR-02 |
| 2 | P-01 | Manual booking through chat (merged with the former P-03): every step waits for the Manager; no self-service; bookings lost during booking-open waves; name lookup at check-in; missing table information; Manager hours and customer churn | 4 | 5 | 20 | RC-01 (RC-03 merged) | BR-01 |
| 3 | P-04 | Payment verification risk: slips checked by eye, bank details typed by hand; fake or wrong slips are a direct loss | 4 | 4 | 16 | RC-04 | BR-03 |
| 4 | P-06 | No reminders and no terms shown before payment: forfeits and disputes at the door | 3 | 4 | 12 | RC-06 | BR-01 |
| 5 | P-05 | No visibility beyond the Manager: no live status for the Owner and the staff (everything in the Manager's LINE account, a single point of failure) and no history for planning | 3 | 3 | 9 | RC-05 | BR-04, BR-05 |
| 6 | P-07 | Freed tables are not resold: no waitlist when a hold expires or a no-show frees a table; no official transfer; informal resale in chat with no record | 3 | 2 | 6 | RC-07 | BR-02 |

<!-- /include -->

The root causes RC-01 to RC-07 named in Table 2.4 were reached by asking "why" until a structural cause that the project can act on appeared; RC-03 was merged into RC-01 when the former problem P-03 was merged into P-01.

<!-- include: ../../../assignments/group/project/requirements/vision.md#2.1.2 Root cause analysis (5 Whys) no-prose -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

- **P-02 double bookings.** Why do two customers get the same table? Because the map the Manager sends is already stale when the second customer picks. Why is it stale? Because the Manager edits an image by hand and keeps pending picks in memory while chatting. Why is there no live record? Because bookings are spread over LINE, Excel and paper with no central database (RC-02).
- **P-01 manual chat process.** Why do customers wait hours? Because the Manager reads and answers every chat personally, one at a time. Why must the Manager answer? Because there is no self-service channel to see the map or reserve. Why none? Because the whole process was built on LINE chat, which has no application behind it (RC-01).
- **P-04 payment verification.** Why is verification risky? Because slips are checked by eye, one by one. Why by eye? Because nothing connects the booking to a bank or gateway. Why not? Because chat-based booking was never designed for payment integration (RC-04).
- **P-06 notifications and terms.** Why are tables forfeited without warning? Because no reminder is sent before the check-in cutoff. Why not? Because reminders and terms depend on the Manager typing them. Why is that the only way? Because no system holds the booking's timeline (RC-06).
- **P-05 visibility.** Why can the Owner not see the current bookings? Because they exist only in the Manager's chat and file. Why are they not shared? Because the tools are for communication and notes, not shared structured data (RC-05).
- **P-07 released tables.** Why are freed tables lost? Because only the Manager learns that a hold expired or a customer did not come. Why is nobody else offered the table? Because there is no queue of interested customers and no transferable booking identity (RC-07).

<!-- /include -->

Table 2.5 states each root cause as the Vision records it, next to the problem it explains, so that the ranking of Table 2.4 and the comparison of the options in Section 2.5 can be read without the requirements artifacts.

*Table 2.5 Root causes*

<!-- include: ../../../assignments/group/project/requirements/vision.md#2.1.1 Problems, root causes and priority no-prose keep=6,2 rename=ID:Problem split=Root_cause -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| ID | Root cause | Problem |
| --- | --- | --- |
| RC-02 | There is no single real-time record of table status; information is scattered across LINE, Excel and paper | P-02 |
| RC-01 | The whole process depends on the Manager's manual work in LINE with no system behind it, so every step waits for a human reply | P-01 |
| RC-04 | The chat-based process has no connection to a bank or payment gateway, so payment cannot be verified automatically | P-04 |
| RC-06 | Terms and reminders depend on the Manager remembering to type them; no system holds the booking timeline that could trigger them | P-06 |
| RC-05 | The tools in use (LINE, Excel, social media) are communication and note-taking tools, not a database, so data is neither shared nor analyzable | P-05 |
| RC-07 | Freed tables are known only to the Manager, there is no queue of interested customers, and a booking has no identity that can be reassigned | P-07 |

<!-- /include -->

Each root cause is answered by one of the five business requirements BR-01 to BR-05 (Table 2.6), which are the needs the features of Section 2.6 trace to; the priority is the Vision's (1 = highest).

*Table 2.6 Business requirements*

<!-- include: ../../../assignments/group/project/requirements/vision.md#3.4 Summary of Key Stakeholder or User Needs no-prose -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| ID | Need | Priority | Concerns / current solution | Proposed solution |
|---|---|---|---|---|
| BR-01 | Automated self-service booking and customer communication: customers must be able to browse rounds, choose a zone and table, reserve and pay by themselves through LINE, and receive confirmations, terms and reminders from the system | 1 | every step waits for the Manager in chat; no terms or reminders (P-01, P-06) | LIFF web application inside the LINE Official Account with transactional and scheduled LINE messages |
| BR-02 | Real-time availability and booking-lifecycle management: a selected table must be held and shown as taken immediately for everyone, released when the hold or grace period expires, and re-offered through a waitlist or transferred officially | 1 | holds in the Manager's memory, hand-edited map, first slip wins, freed tables lost (P-02, P-07) | central record with automatic hold, release, waitlist and transfer |
| BR-03 | Integrated payment verification of the full table fee: payment must be verified automatically and the booking confirmed without human slip checking | 2 | bank details typed by hand, slips checked by eye (P-04) | payment gateway with automatic confirmation and e-ticket |
| BR-04 | Centralized management dashboard: the Manager, Owner and Front Staff must manage rounds, prices and layouts, and see the same live booking status in one place | 2 | information locked in the Manager's chat and file; no handover (P-05, P-02) | shared real-time back-office |
| BR-05 | Analytics and reporting: booking summaries, revenue, customer history and artist popularity must be available for planning | 3 | no structured data at all (P-05) | reports and export from the central record |

<!-- /include -->

Table 2.7 sets the proposed system against the problems from the other side: the positive and negative impacts it will have on the organization and beyond, which the options analysis of Section 2.5 and the risks of Section 2.10 take up.

*Table 2.7 Impacts of the proposed system*

<!-- include: ../../../assignments/group/project/management/business-case.md#3.4 Impacts of the proposed system no-prose -->
<!-- source: ../../../assignments/group/project/management/business-case.md · Business Case v1.7 (In review) · Develop Business Case (ac_dbzcs) -->

| Context | Positive impact | Negative impact |
|---|---|---|
| Societal | A fair first-come, first-served system; less reliance on personal connections to get a table; terms known before paying | Older customers who are less comfortable with technology may find booking harder than chatting with the Manager, so the shop must keep a staff-assisted booking path as an alternative |
| Environmental | Paperless: no booking notebook, no printed lists, no paper slips; all records digital | Cloud hosting and message sending add a small amount of energy use |
| Economic | Fewer Manager hours per booking; less revenue lost to double bookings, fake slips and unsold freed tables; reliable revenue figures per round | Initial development effort; monthly cost of hosting, APIs and the LINE Official Account plan (bounded by CON-03); a gateway fee on every payment (CON-07) |
| Global | Digital transformation of a restaurant business to a common international pattern; foreign customers can book through an easy, automatic flow instead of a Thai chat | Dependence on external platforms (LINE and the payment gateway) ties the system to their policies and availability |

<!-- /include -->

## 2.4 Critical Assumptions and Constraints

The assumptions (Table 2.8) are conditions the plan relies on and that the team cannot control, grouped by the party they concern. The constraints (Table 2.9) are limits imposed from outside, grouped as business, cost, regulatory and technical. Both tables are quoted from the project's Vision, which also records the rationale of each item; the identifiers are kept as row keys.

*Table 2.8 Critical assumptions*

<div class="asm grouped" markdown="1">

<!-- include: ../../../assignments/group/project/requirements/vision.md#4.2 Assumptions and Dependencies no-prose drop=Rationale -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| Type | ID | Assumption |
| --- | --- | --- |
| Customer | ASM-01 | Customers own a smartphone, already use LINE, and have a stable internet connection while reserving and paying |
| Customer | ASM-03 | Customers read Thai or English; the user interface is provided in Thai and English only |
| Customer | ASM-04 | Customers have a mobile banking application or PromptPay that can pay through the selected gateway |
| Customer | ASM-08 | One LINE account represents one customer; LINE Login is the customer's identity and no separate registration exists |
| Shop | ASM-05 | The shop has at least one internet-connected computer or tablet for the back-office; Front Staff have a smartphone with a camera for QR scanning and can use a web browser and LINE |
| Shop | ASM-06 | The shop already has a LINE Official Account, can enable the Messaging API and LIFF, and can open a merchant account with the selected gateway after identity verification |
| Shop | ASM-07 | The Manager defines the round, zone map, table numbers and package prices before a round opens for booking, and the layout stays fixed for that round (no ad-hoc merging or splitting of tables) |
| External services | ASM-02 | The external services the system depends on, the LINE Platform and the payment gateway, are highly available under their providers' service levels |

<!-- /include -->

</div>

*Table 2.9 Constraints*

<div class="asm grouped" markdown="1">

<!-- include: ../../../assignments/group/project/requirements/vision.md#6.1 Constraints no-prose drop=Rationale -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| Type | ID | Constraint |
| --- | --- | --- |
| Business | CON-02 | The customer channel must be LINE, through the LINE Official Account and LIFF; no separate mobile application |
| Business | CON-08 | Package screens and LINE messages present packages factually (name, contents, price) with no wording or images that induce drinking, as required by the Alcoholic Beverage Control Act B.E. 2551 |
| Cost | CON-03 | The operating cost of the system, hosting, APIs and LINE plan together, must not exceed 1,000 THB per month |
| Cost | CON-07 | Per-transaction payment fees, VAT included, shall not exceed 1 % of the charged amount for PromptPay QR and 3 % for cards; payment methods above these limits are not offered; the shop absorbs the fee inside the package price |
| Regulatory | CON-05 | Personal data (name, phone, payment history) must be handled under the Personal Data Protection Act: stated purpose, consent, retention period and deletion |
| Technical | CON-01 | The customer-facing screens must be designed mobile-first |
| Technical | CON-04 | Demand concentrates in the first minutes after a round opens; the design must handle concurrent reservations and table locking under burst load |
| Technical | CON-06 | Core functions, LINE Login, notifications and payment, depend on external APIs the team does not control; the design must tolerate their failure |
| Technical | CON-09 | The number of push messages of the LINE Official Account is limited by the shop's plan; notification design must stay within the quota or the budget of CON-03 |
| Technical | CON-10 | The customer frontend must run inside LINE's in-app browser (LIFF); the back-office runs on a standard desktop browser on the shop's computer |

<!-- /include -->

</div>

## 2.5 Analysis of Problem Resolution Options and Recommendation

Four options were considered (Table 2.10) and compared on fit to the root causes, cost, time to operate, LINE integration, control of the restaurant's own rules, data ownership and risk (Table 2.11). Ratings are team judgment; no vendor quotation was obtained.

*Table 2.10 Options considered*

<!-- include: ../../../assignments/group/project/management/business-case.md#2.1 Alternatives considered no-prose -->
<!-- source: ../../../assignments/group/project/management/business-case.md · Business Case v1.7 (In review) · Develop Business Case (ac_dbzcs) -->

| ID | Alternative | Description |
|---|---|---|
| ALT-01 | Process fix without new software | Keep the LINE chat; introduce a shared Google Sheet as the single record of tables and holds, LINE reply templates for bank details and terms, and written hold and check-in rules for the Manager and the Front Staff. |
| ALT-02 | Off-the-shelf reservation or event-ticketing platform | Subscribe to an existing restaurant-reservation or event-ticketing service and link to it from the LINE Official Account. |
| ALT-03 | Outsourced custom build | Commission an external developer to build a system of the CTRS scope. |
| ALT-04 (selected) | Custom build by the team's software house: CTRS | The team, four engineers of one software house, specifies and builds a LINE-integrated concert table reservation system tailored to the restaurant's own rules, run as a tailored RUP project; the restaurant pays a fixed pilot implementation fee and the software house carries the rest of the development as its own product investment, to be offered to other restaurants after a pilot year. |

<!-- /include -->

*Table 2.11 Comparison of the options*

<!-- include: ../../../assignments/group/project/management/business-case.md#2.2 Trade-off no-prose -->
<!-- source: ../../../assignments/group/project/management/business-case.md · Business Case v1.7 (In review) · Develop Business Case (ac_dbzcs) -->

| Criterion | ALT-01 process fix | ALT-02 off-the-shelf platform | ALT-03 outsourced build | ALT-04 CTRS (selected) |
|---|---|---|---|---|
| Fit to the root causes (RC-01, RC-02, RC-04..RC-07) | Partial: a single record (RC-02) but the manual bottleneck (RC-01) and the slip check (RC-04) remain | Partial: seat map and ticketing yes; hold, grace, transfer and package rules only as far as the platform allows | Full | Full |
| Cost | Lowest (no software) | Recurring subscription and/or per-ticket commission (not priced) | Highest: external development fee (not priced) plus operation | Fixed pilot implementation fee (150,000 THB) instead of the full price of a custom build; operation within CON-03; gateway fee per CON-07 |
| Time to operate | Days | Weeks (set-up) | Depends on the vendor | Release 1.0 after Construction C1–C2 (April 2027) |
| LINE integration | None beyond the chat itself | Usually a link out of LINE to the vendor's site | Possible, at extra cost | Native: LIFF app, LINE Login, Messaging API push (CON-02, CON-10) |
| Control of the restaurant's own rules (hold, grace, transfer, pricing) | Manual, depends on the Manager following the written rules | Limited to the platform's rule set | Full, but every change costs money | Full; rules are the project's Business Rules |
| Data ownership | Restaurant (spreadsheet) | Platform holds customer and sales data (PDPA processor arrangement needed) | Restaurant | Restaurant (central database; CON-05) |
| Risk | Low technical risk; the operational risks P-01, P-02 and P-04 largely remain | Vendor lock-in; rule mismatch; commission on every ticket | Budget and vendor availability; knowledge leaves with the vendor | Team capacity; support after go-live; dependence on LINE and the payment gateway (CON-06) |

<!-- /include -->

**Recommendation: ALT-04, the in-house custom build of CTRS.** It is the only option that addresses all root causes, keeps the customer inside LINE, leaves the restaurant in control of its own hold, grace, transfer and package rules and of its data, and costs the restaurant a fixed pilot implementation fee rather than the full price of a custom build, because the software house carries the rest of the development as its own product investment. Its risks, the team's capacity, the support of the system after go-live, the dependence on the LINE Platform and the payment gateway and, for the software house, the uptake by other restaurants, are carried in Section 2.10. The process fix (ALT-01) is retained as the fallback if the project is stopped, and the bank-transfer-plus-slip path survives inside CTRS as the degraded payment mode.

## 2.6 Preliminary Project Requirements

### 2.6.1 To-be system

Customers enter CTRS from the Rich Menu of the restaurant's existing LINE Official Account, sign in with LINE Login, browse the upcoming concert rounds, see a real-time table map with table types, packages and prices, select a table (which holds it for 15 minutes), accept the booking terms and pay the full table fee through the payment gateway selected by the team's feasibility study (Beam Checkout, fallback Opn Payments). The booking is confirmed automatically on the gateway's callback and a QR-coded e-ticket is sent as a LINE message. On the night, Front Staff scan the e-ticket, the booking is set to Checked-in, and tables of no-shows are released after the grace period. For the restaurant, one central database and a back-office web application replace the chat process, the hand-edited image, the slip check and the Excel record: the Manager creates rounds, zones, table types and prices, the Manager and the Owner share one live view of holds, bookings and payments, and reports support marketing and planning. Figure 2.2 shows the system context and Table 2.12 its components.

![CTRS system context and high-level architecture](../../../assignments/group/project/requirements/diagrams/system-context.png)

*Figure 2.2 System context and high-level architecture of CTRS*

*Table 2.12 Components of the to-be system*

<!-- include: ../../../assignments/group/project/requirements/vision.md#4.1.3 Components no-prose -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| Component | Type | Description |
|---|---|---|
| Customer Frontend | internal | mobile-first LIFF web application opened from the Rich Menu of the LINE Official Account; browse rounds, view the live table map, reserve, pay, keep the e-ticket, join the waitlist, transfer a booking |
| Back-office Frontend | internal | web application for the Manager, Owner and Front Staff: rounds, layouts and prices, shared live dashboard, exception handling, QR scanning and check-in, reports |
| Application Server | internal | cloud-hosted business logic: real-time hold and release, payment confirmation, ticket validation, notifications, waitlist, reports |
| Central Database | internal | encrypted relational database holding rounds, layouts, bookings, payments, tickets, customer profiles and history |
| LINE Platform | external | LINE Login for identity, LIFF for the web application, Messaging API for push messages, Rich Menu as the entry point |
| Payment Gateway | external | Beam Checkout, selected by the Payment Gateway Feasibility Study (Opn Payments as fallback): PromptPay QR, cards, mobile banking and e-wallets for the Thai market, payment result by signed webhook, refund API; per-transaction fee (CON-07) |

<!-- /include -->

### 2.6.2 Releases and features

The product is delivered in two releases (Table 2.13), each with a goal, a set of iterations and a date from the schedule estimate of Section 2.8 (Table 2.14). Tables 2.15 to 2.18 list the features by user role with the attributes the Vision records for each: its value to the restaurant (High, Medium, Low, inherited from the ranking of the problem it solves), its implementation cost as judged by the team (Low, Medium, High), and its priority 1 to 5, from which the target release follows (Release 1.0 = priorities 1 and 2, Release 2.0 = 3, Future = 4 and 5). The Vision also traces every feature to its problem and business requirement; that traceability is not repeated here. System features are automatic behavior.

*Table 2.13 Releases*

<!-- include: ../../../assignments/group/project/requirements/vision.md#5.5 Releases no-prose -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| Release | Scope | Delivered by |
|---|---|---|
| 1.0 Core | create a concert round, reserve and pay, watch the live booking view, check in, staff accounts, audit trail, degraded-mode switch and consent: F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F15, F16, F17, F21, F23, F24, F25, F27, F28; exceptions on the concert night, backup and push budget: F13, F14, F18, F19, F20, F22, F26 | the Construction iterations C1 and C2 and the Transition iteration T1 (April 2027) |
| 2.0 Growth | reminders, waitlist, transfer, reports, grace extension: F29, F30, F31, F32, F33, F34, F35 | the Construction iteration C3 and the Transition iteration T2 after Release 1.0 (July 2027) |
| Future | F36 split payment, F37 table photos and stage distance, configurable business rules | candidates |

<!-- /include -->

*Table 2.14 Goal and timing of each release*

| Release | Goal | Iterations | In operation |
|---|---|---|---|
| 1.0 Core | Replace the chat process on concert nights: customers reserve and pay by themselves, every table and payment is on one record, staff check in by QR, and the Manager handles exceptions only (28 features, priorities 1 and 2) | C1, C2, T1 | 2 April 2027 |
| 2.0 Growth | Use the record to sell more and lose less: scheduled reminders, grace extension, waitlist, official booking transfer and reports (7 features, priority 3) | C3, T2 | 30 July 2027 |
| 2.1 Product | Productize the pilot system for other restaurants: multi-tenant service, Free / Standard / Premium plans and limits, subscription billing, self-service onboarding, service administration (software house scope, Section 3.1) | C4, T3 | 11 February 2028 |
| Future | Candidates outside the project: split payment, table photos and stage distance, configurable business rules (priorities 4 and 5) | — | not scheduled |

*Table 2.15 Features for the Customer*

<!-- include: ../../../assignments/group/project/requirements/vision.md#5.1 Customer no-prose drop=Traces -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| Release | ID | Feature | Description | Value | Cost | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | F1 | LINE sign-in | Sign in with LINE Login; no separate registration | High | Low | 1 |
| 1.0 | F2 | Table map | View the real-time table map of a round with table status, seats, package and price | High | High | 1 |
| 1.0 | F3 | Table selection and hold | Select a table; the system holds it for 15 minutes while paying; on the first booking enter name and phone into a profile that is pre-filled afterwards | High | Medium | 1 |
| 1.0 | F4 | Gateway payment | Choose a payment method offered by the payment gateway (Beam Checkout) and pay the full table fee; the booking is confirmed automatically | Medium | High | 1 |
| 1.0 | F5 | QR e-ticket | Receive a QR e-ticket for the booking | High | Low | 1 |
| 1.0 | F6 | Transactional messages | Receive transactional LINE messages: booking confirmation, payment result and hold timeout | Medium | Low | 1 |
| 1.0 | F7 | Booking terms | See and accept the booking terms (full payment, check-in window, grace period, no refund) before paying | Medium | Low | 1 |
| 1.0 | F8 | My bookings | View own bookings and their status | High | Low | 1 |
| 1.0 | F9 | Round list | Browse upcoming concert rounds with date, time and artist | High | Low | 1 |
| 2.0 | F29 | Grace extension | Reply "on my way" or request a 30-minute grace extension from the reminder (subject to the Owner's decision on the rule) | Medium | Medium | 3 |
| 2.0 | F30 | Waitlist | Join the waitlist of a full round or zone and be notified when a table is freed | Low | Medium | 3 |
| 2.0 | F31 | Booking transfer | Transfer a confirmed booking officially to another LINE account | Low | Medium | 3 |
| 2.0 | F32 | Scheduled reminders | Receive scheduled LINE reminders before the event, when the check-in window opens and before the grace cutoff | Medium | Medium | 3 |
| Future | F36 | Split payment | Share a payment link so that group members pay their share of the table fee within the hold | Low | High | 5 |
| Future | F37 | Table photos | See a photo of the view from each table and its distance to the stage on the table map | Low | Medium | 4 |

<!-- /include -->

*Table 2.16 Features for the Manager (the Owner uses the same back-office read-only)*

<!-- include: ../../../assignments/group/project/requirements/vision.md#5.2 Manager (the Owner uses the same back-office read-only) no-prose drop=Traces -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| Release | ID | Feature | Description | Value | Cost | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | F10 | Concert rounds | Manage concert rounds: artist, date and time, booking-open time, table layout of the round | High | Medium | 1 |
| 1.0 | F11 | Zones and packages | Define zones, table types, packages, prices and the extra-person fee | High | Medium | 1 |
| 1.0 | F12 | Live booking view | Live booking view: every table of the current round with its hold, booking, payment status and check-in in real time; the Owner reads the same screen read-only | High | Low | 1 |
| 1.0 | F13 | Ticket escalation management | Resolve duplicate or invalid QR ticket cases | High | Low | 2 |
| 1.0 | F14 | Manual booking and payment overrides | Handle exceptions: lock or unlock a table by hand, cancel a booking, confirm or reject a transfer-slip payment while the payment gateway is unreachable (degraded mode) | High | Medium | 2 |
| 2.0 | F33 | Reports | Reports on bookings, revenue, artist popularity and customer history, with export to Excel | Low | Medium | 3 |

<!-- /include -->

*Table 2.17 Features for the Front Staff*

<!-- include: ../../../assignments/group/project/requirements/vision.md#5.3 Front Staff no-prose drop=Traces -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| Release | ID | Feature | Description | Value | Cost | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | F15 | QR scan | Scan the customer's QR e-ticket at the door | High | Low | 1 |
| 1.0 | F16 | Ticket details | See the round, table number and payment status of the scanned ticket in real time | High | Low | 1 |
| 1.0 | F17 | On-site check-in processing | Set the booking to Checked-in | High | Low | 1 |
| 1.0 | F18 | Invalid ticket escalation | Escalate an invalid ticket to the Manager | High | Low | 2 |
| 1.0 | F19 | No-show and table release management | Mark a no-show after the grace period; the table is released to walk-in guests or the waitlist | Low | Low | 2 |
| 1.0 | F20 | Name lookup | Look a booking up by name or phone when the customer cannot show the QR code | High | Low | 2 |

<!-- /include -->

*Table 2.18 System features (automatic behavior)*

<!-- include: ../../../assignments/group/project/requirements/vision.md#5.4 System (automatic behavior) no-prose drop=Traces -->
<!-- source: ../../../assignments/group/project/requirements/vision.md · Vision v1.11 (In review) · Develop Vision (ac_dvisn) -->

| Release | ID | Feature | Description | Value | Cost | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | F21 | Hold release | Release a held table when the 15-minute hold expires and notify the customer | High | Low | 1 |
| 1.0 | F22 | Daily backup | Back up booking data daily and produce the Excel export | Low | Low | 2 |
| 1.0 | F23 | Payment callback | Confirm the booking and issue the e-ticket on the gateway's payment callback | Medium | Medium | 1 |
| 1.0 | F24 | Staff accounts | Back-office accounts with the roles Manager, Front Staff and Owner (read-only) and role-based access to each back-office function | Medium | Low | 1 |
| 1.0 | F25 | Audit trail | Keep an audit trail of every booking state change and manual action with time, acting account and reason | Medium | Low | 1 |
| 1.0 | F26 | Push-message budget | Count the LINE push messages per month and stop non-essential reminders within the plan's quota | Low | Low | 2 |
| 1.0 | F27 | Degraded-mode switch | Switch new payments to degraded mode when the payment gateway does not answer and return to gateway mode when it answers again | Medium | Medium | 1 |
| 1.0 | F28 | Consent and profile access | Obtain consent before personal data is collected and let the customer view and correct the profile | Medium | Low | 1 |
| 2.0 | F34 | Reminder scheduling | Send scheduled reminders before the event, the check-in window and the grace cutoff | Medium | Medium | 3 |
| 2.0 | F35 | Waitlist offer | Offer a freed table to the waitlist in queue order | Low | Medium | 3 |

<!-- /include -->

### 2.6.3 Quality targets

The measurable targets that the Vision hands to the Supplementary Specification bound the design and the acceptance tests (Table 2.19); the full non-functional specification is produced in Elaboration. Personal data is handled under the Personal Data Protection Act and package screens follow the Alcoholic Beverage Control Act.

*Table 2.19 Preliminary quality targets*

| Quality requirement | Target | Why |
|---|---|---|
| Throughput at booking-open time | at least 5 transactions per second | demand concentrates in the first minutes after a round opens |
| Recovery after an outage | within 2 hours during opening hours | a concert-night sale cannot wait for the next day |
| Supported browsers | the current LINE in-app browser and the last two versions of Chrome, Safari and Edge | customer frontend inside LINE, back-office on the shop's desktop browser |
| Response time | within 2 seconds for customer and Front Staff transactions | self-service booking must not feel slower than chat |
| Check-in time | within 15 seconds per table | queue at the door two hours before the show |
| Backup | daily backup of booking data with export to Excel | the Excel record is the shop's habit and its fallback |

## 2.7 Budget Estimate

The budget is the software house's cost of the project: the effort of the four engineers per phase at the software house's internal cost rates, the test devices, the hosting and services of the build and the pilot, the company and legal set-up of the subscription business in Year 1, and a contingency reserve (Table 2.20). Year 0 builds Release 1.0 and 2.0 for the pilot restaurant; Year 1 runs the pilot and productizes the service (Release 2.1). The only revenue inside the project is La Loy's pilot implementation fee; the subscription revenues start after the expansion decision and are analyzed in Section 3.

*Table 2.20 Budget estimate*

<!-- finance: budget -->

| Category | Basis | THB |
|---|---|---|
| CAPEX, Year 0 | Test devices (Table 3.5) | 15,000 |
| Development labor, Year 0 | 2,092 hours of the four engineers at 300 to 350 THB/h, Release 1.0 and 2.0 for the pilot restaurant (Table 3.4) | 674,600 |
| Hosting and services, Year 0 | Development, staging and pilot hosting, domain (Table 3.6) | 8,300 |
| Contingency reserve, Year 0 | 10 % of the Year 0 cost, for the risks of Table 2.24 | 69,790 |
| **Budget, Year 0 (build)** | | **767,690** |
| Development labor, Year 1 | 540 hours: multi-tenant productization, plans and billing (C4, T3) | 172,000 |
| Company, legal, hosting and support, Year 1 | Registration and legal documents, pilot hosting and support (Table 3.6) | 52,200 |
| Contingency reserve, Year 1 | 10 % of the productization work | 18,700 |
| **Budget, Year 1 (pilot and productization)** | | **242,900** |
| **Project budget, Years 0 and 1** | | **1,010,590** |
| Revenue inside the project | Pilot implementation fee paid by La Loy in Year 0 | 150,000 |
| **Net investment of the software house** | budget less the pilot fee | **860,590** |

<!-- /finance -->

## 2.8 Schedule Estimate

The project follows the four phases of the tailored RUP defined in the project's Development Case, each closed by a milestone decision: Inception (Lifecycle Objectives, LCO), Elaboration (Lifecycle Architecture, LCA), Construction (Initial Operational Capability, IOC) and Transition (Product Release). Year 0 (August 2026 to July 2027) builds Release 1.0 and 2.0 for La Loy in eight iterations; Year 1 (August 2027 to July 2028) is the pilot year, in which La Loy operates the system on its concert nights while the software house productizes it as Release 2.1 in two further iterations, and it ends with the expansion decision that closes the project (Table 2.21, Figure 2.3). In PMBOK terms the Initiating process group is I1, Planning is I2 and the two Elaboration iterations, Executing is Construction and Transition, Monitoring and Controlling runs through every iteration (weekly status assessment, iteration assessment, milestone review) and through the pilot measurement, and Closing is the expansion decision at the end of the pilot year.

*Table 2.21 Schedule estimate by phase and iteration*

| Phase | Iteration | Content | Start | End | Milestone |
|---|---|---|---|---|---|
| Inception | I1 | Problem, scope, stakeholders, high-level features; first elicitation | 3 Aug 2026 | 24 Aug 2026 | |
| Inception | I2 | Vision revised, Development Case, Business Case, iteration plans, WBS | 25 Aug 2026 | 2 Sep 2026 | LCO, 2 Sep 2026 |
| Elaboration | E1 | The two main use cases (reserve a concert table, check in with e-ticket), Software Requirements Specification, Supplementary Specification | 3 Sep 2026 | 16 Sep 2026 | |
| Elaboration | E2 | Analysis model, software architecture, user-interface prototype, test plan, Construction plan, SRS baseline | 17 Sep 2026 | 23 Oct 2026 | LCA, 23 Oct 2026 |
| Construction | C1 | Concert set-up, zones and packages, table map, table selection and hold, gateway payment, payment callback, staff accounts | 26 Oct 2026 | 18 Dec 2026 | |
| Construction | C2 | QR e-ticket, transactional messages, check-in, live booking view, exceptions and degraded mode, audit trail, backup, consent | 4 Jan 2027 | 26 Feb 2027 | IOC, 26 Feb 2027 |
| Transition | T1 | Pilot on concert nights, training of Manager and Front Staff, data migration of the current bookings, go-live | 1 Mar 2027 | 2 Apr 2027 | Release 1.0 in operation, 2 Apr 2027 |
| Construction | C3 | Release 2.0: scheduled reminders, grace extension, waitlist, booking transfer, reports | 5 Apr 2027 | 25 Jun 2027 | |
| Transition | T2 | Release 2.0 on La Loy's concert nights, training on the new features, end of the build year | 28 Jun 2027 | 30 Jul 2027 | Release 2.0 in operation, 30 Jul 2027 |
| Pilot year | P1 | La Loy operates Release 2.0 alone, free of charge; pilot KPIs measured on every concert night (booking time, double bookings, no-shows, check-in time, operating cost) | 2 Aug 2027 | 28 Jul 2028 | |
| Construction | C4 | Release 2.1 productization: multi-tenant data model, plans and limits, subscription billing, self-service onboarding, service administration | 2 Aug 2027 | 14 Jan 2028 | |
| Transition | T3 | Migration of La Loy to the productized service, release of the Free-plan sign-up, hand-over to the support routine | 17 Jan 2028 | 11 Feb 2028 | Release 2.1 in operation, 11 Feb 2028 |
| Close-out | — | Pilot review against the charter's success criteria, expansion decision of the software house, lessons learned, project close-out | 24 Jul 2028 | 28 Jul 2028 | Expansion decision, project closed, 28 Jul 2028 |

![Schedule of the CTRS project](../assets/diagrams/schedule-gantt.png)

*Figure 2.3 Schedule estimate of the CTRS project (Gantt chart)*

## 2.9 Development Process

The project follows the tailored Rational Unified Process recorded in the project's Development Case rather than a sequential life cycle (Figure 2.4). Year 0 runs the four phases twice for the pilot restaurant, Inception and Elaboration once and Construction and Transition for Release 1.0 and again for Release 2.0, in eight iterations; Year 1 runs Construction and Transition a third time for the productized Release 2.1 while the pilot operation P1 measures the system on La Loy's concert nights, and ends with the expansion gate that closes the project. Every phase is closed by a milestone decision and every iteration by an assessment against its evaluation criteria. The PMBOK process groups map onto this life cycle as bars over time rather than as stages: Initiating is I1, Planning is I2 and the two Elaboration iterations and then repeats before every iteration and at every milestone, Executing is the build for the pilot restaurant, the productization and the pilot operation, Monitoring and Controlling runs through the whole project (weekly status assessment, iteration assessment, milestone review, change control, risk review, pilot KPIs), and Closing is the expansion decision, with a phase close-out at each milestone. Table 2.22 lists the activities and the project-management artifacts of each process group, and Table 2.23 the artifacts the Project Manager produces in each phase next to the requirements and engineering work that the same iterations carry.

![Development process of the CTRS project](../assets/diagrams/dev-process.png)

*Figure 2.4 Development process of the CTRS project: tailored RUP phases, iterations, milestones, expansion gate and PMBOK process groups over the two project years*

*Table 2.22 PMBOK process groups mapped to the tailored RUP*

| Process group | RUP phase and iterations | Activities | Project-management artifacts |
|---|---|---|---|
| Initiating | Inception I1 | Conceive New Project: problem, scope, stakeholders and high-level features agreed; first elicitation; Develop Business Case | Business Case (draft); project charter (this document); stakeholder list |
| Planning | Inception I2, Elaboration E1 and E2 | Plan the Project: Development Case, Software Development Plan with organization and WBS, iteration plans, Risk List; Plan for Next Iteration before every iteration; use-case prioritization sets the scope of C1 and C2; financial analysis re-run at LCA | Software Development Plan; iteration plans; Risk List; scope statement, WBS, estimates, schedule and cost baseline; quality, risk and communication plans |
| Executing | Elaboration E1 and E2 (requirements, architecture, prototype, test plan); Construction C1, C2, C3, C4; Transition T1, T2, T3 | Requirements, analysis and design, implementation, test and deployment activities of each iteration; pilot on concert nights; training; data migration | Iteration deliverables (use-case specifications, SRS, Software Architecture Document, prototype, builds, test results); Review Records |
| Monitoring and Controlling | Every iteration | Monitor and Control Project: weekly Status Assessment, iteration assessment against the evaluation criteria, Lifecycle Milestone Reviews (LCO, LCA, IOC, Product Release); change requests decided by the Change Control Board with impact analysis through traceability; Risk List reviewed each iteration | Status Assessments; iteration assessments; decided Change Requests; updated Risk List; earned-value and schedule tracking against the cost and schedule baselines; pilot KPI measurement |
| Closing | End of the pilot year | Close-Out Phase and project: pilot review against the success criteria, expansion decision of the software house, hand-over to the support routine, lessons learned, sign-off by the sponsor and the pilot customer | Pilot review; expansion decision record; hand-over record; lessons learned; final Status Assessment |

*Table 2.23 Project-management artifacts by phase*

| Phase (iterations) | Project-management artifacts | Requirements and engineering work in the same iterations |
|---|---|---|
| Inception (I1, I2) | Business Case with financial analysis; project charter and stakeholder list; project organization; Development Case (process tailoring); Software Development Plan (draft); iteration plans I1 and I2; Risk List (initial); LCO review | Vision, Glossary, Stakeholder Requests, Business Rules, Domain Model, Use-Case Model survey |
| Elaboration (E1, E2) | Scope statement; WBS and WBS dictionary; effort, resource and cost estimates; schedule (Gantt chart, critical path) and cost baseline; quality, risk and communication management plans; iteration plans E1 and E2 and the Construction plan; LCA review with the financial analysis re-run | Use-case specifications, Software Requirements Specification, Supplementary Specification, Analysis Model, Software Architecture Document, user-interface prototype, test plan and test cases; SRS baseline under the Change Control Board |
| Construction and Transition (C1, C2, T1, C3, T2 in Year 0; C4, T3 in Year 1) | Iteration plan and assessment per iteration; weekly status assessments; decided change requests; updated Risk List; load-test and acceptance records; IOC and Product Release reviews; training and go-live records | Builds of the features of each iteration, tests and load test; pilot on concert nights, training, data migration, go-live; in Year 1 the multi-tenant data model, plans and limits, billing, self-service onboarding and service administration of Release 2.1 |
| Pilot year and close-out (P1) | Monthly pilot KPI reports (booking time, double bookings, no-shows, check-in time, operating cost); plans, prices and adoption plan of the service; waiting list; expansion gate record; lessons learned; project close-out and sign-off | Operation and support of the pilot restaurant; migration of La Loy to the productized service |

## 2.10 Potential Risks

Table 2.24 lists the risks identified at this stage with a first probability and impact rating (Low, Medium, High) and the planned response; they seed the project's Risk List, which the Project Manager reviews at the end of every iteration, and the risk register of the risk management plan. The contingency reserve of the budget (Section 2.7) is sized against them.

*Table 2.24 Potential risks*

| ID | Risk | Category | Probability | Impact | Response |
|---|---|---|---|---|---|
| RISK-01 | The restaurant-side stakeholders have not been interviewed yet and are available only in the afternoons; the Owner's approval of the Vision (LCO) and the validation of the benefit volumes depend on securing one workshop | Stakeholder | High | High | Mitigate: the System Analyst books one afternoon workshop with the Owner and Manager in September 2026; open decisions and volumes collected in a single visit; asynchronous follow-up through LINE |
| RISK-02 | The four engineers are allocated to the project part-time; other client work of the software house delays an iteration | Resource, schedule | High | Medium | Mitigate: weekly status assessment, iteration scope re-planned at each iteration end (Manage the Scope of the System); features of priority 2 are the first to move to the next iteration |
| RISK-03 | Merchant onboarding with the payment gateway (business type accepted, identity verification) and the LINE Official Account settings (Messaging API, LIFF) are external prerequisites that may take longer than planned or fail for the shop's business type | External | Medium | High | Mitigate: the two checks named in the feasibility study are run before LCA; Opn Payments is the fallback gateway; the degraded payment mode (bank transfer plus slip) keeps Release 1.0 operable |
| RISK-04 | A defect on a concert night has no responder because the same four engineers support the pilot and build the productized version at the same time | Organizational | Medium | High | Mitigate: a support routine of 8 hours a month with an on-call engineer on concert nights is budgeted from Release 1.0 (Section 3.3); the concert calendar is known weeks ahead and drives the on-call roster |
| RISK-05 | Burst load at booking-open time exceeds the design (5 transactions a second) and holds or payments fail on the busiest nights | Technical | Medium | High | Mitigate: load test before IOC; first-lock-wins locking in the database; hosting sized to the tested load within the operating-cost ceiling |
| RISK-06 | Outage or policy change of the LINE Platform or the payment gateway during a concert-night sale | External | Low | High | Accept with contingency: degraded payment mode, reconciliation through the gateway's status query, the Manager's manual overrides; providers' service levels monitored |
| RISK-07 | The restaurant's operating cost exceeds the 1,000 THB a month ceiling, for example if push messages exceed the LINE plan's quota | Cost | Medium | Medium | Mitigate: push-message budget in the system, the shop's current LINE plan kept, hosting cost reviewed monthly during the pilot |
| RISK-08 | Business rules still pending the Owner's decision (grace extension, transfer cut-off, waitlist, refund policy, retention period) change late and force rework of Release 2.0 | Scope | Medium | Medium | Mitigate: decisions requested at the workshop of RISK-01 and closed before LCA; changes after the baseline go through the Change Control Board |
| RISK-09 | Personal-data handling or the presentation of drink packages does not meet the law (Personal Data Protection Act, Alcoholic Beverage Control Act) and the shop has to stop using a function | Regulatory | Low | High | Avoid: consent, retention and correction designed in; package content guideline written in E1; QA reviews both before IOC |
| RISK-10 | Late change requests from reviews and prototype trials widen the scope after the SRS baseline | Scope | Medium | Low | Mitigate: every request is filed as a Change Request and decided by the Change Control Board against the release plan; the requirements baseline is re-planned, not silently extended |
| RISK-11 | (positive) The feasibility study's selected gateway offers PromptPay QR at no fee, so the gateway cost stays below the fee limit the restaurant accepts | Cost, opportunity | High | Medium | Exploit: PromptPay QR presented as the default payment method; card payments kept for foreign customers |
| RISK-12 | Other restaurants adopt the service more slowly than the plan of Table 3.2, and the 1,000 THB a month price ceiling leaves no room to compensate; the investment is not recovered | Market | Medium | High | Mitigate: expansion gate at the end of the pilot year (waiting list of at least 10 restaurants, La Loy on a paid plan); Free plan and the "Powered by CTRS" footer as the acquisition channel; exposure limited to the net investment of Years 0 and 1 |
| RISK-13 | A reservation or ticketing platform, or LINE itself, adds concert-table sales and undercuts the price | Market | Low | High | Accept with contingency: the shop-specific rules (hold, grace, transfer, packages) and the LINE-native flow are the differentiation; plans and prices reviewed yearly |
| RISK-14 | The pilot restaurant stops the pilot (closes, changes Manager, loses interest) before the KPIs are measured, and the reference customer for the expansion is lost | Stakeholder | Low | High | Mitigate: pilot agreement with the free pilot year and the KPIs written down; monthly review with the Owner; a second pilot venue lined up on the waiting list |

# 3. Financial Analysis

## 3.1 Business Model and Revenue Plan

The four members of the team are engineers of one software house, and CTRS is that software house's product. La Loy is the pilot customer: it pays a fixed pilot implementation fee for the build of Release 1.0 and 2.0 (Year 0) and uses the system free of charge during the pilot year (Year 1), while the software house productizes it (multi-tenant service, plans and limits, subscription billing, self-service onboarding, Release 2.1) and measures the pilot against the success criteria of the charter. At the end of the pilot year the software house decides whether to expand; from Year 2 the service is offered to other live-music restaurants and bars that sell concert tables in advance, as a subscription.

The pricing follows the restaurant's own constraint: a restaurant of this size will pay at most 1,000 THB a month for hosting, APIs and the LINE plan together (constraint CON-03 of Table 2.9), so the top plan costs 990 THB a month with hosting included, the restaurant keeps its own LINE Official Account plan and its own merchant account with the payment gateway (the transaction fees stay with the restaurant), and the software house carries no payment-processing cost. Three plans (Table 3.1) separate acquisition from revenue: the Free plan lets a restaurant run one concert round a month with the core flow and the "Powered by CTRS" footer on the customer screens, which is the product's own marketing channel; Standard sells every Release 1.0 feature; Premium adds the Release 2.0 features that earn the restaurant money on top of the core flow (reminders, waitlist, transfer, reports). Every paid subscription starts with a setup fee that covers the configuration and training of the shop. For the restaurant the Premium fee of 11,880 THB a year is small against the Manager time and the lost or unsold tables it replaces (one lost table a month already costs more than the fee); those benefits are the customer's reason to subscribe and are deliberately not counted in the software house's analysis below.

*Table 3.1 Subscription plans and fees*

<!-- finance: plans -->

| Plan | Price (THB a month, VAT excluded) | Contents and limits |
|---|---|---|
| Free | 0 | 1 concert round a month; up to 20 tables; Release 1.0 core: round list, table map, hold, gateway payment through the shop's own merchant account, QR e-ticket, check-in, name lookup; 1 Manager and 1 Front Staff account; "Powered by CTRS" on the customer screens; self-service set-up; community support (LINE group) |
| Standard | 690 | Unlimited rounds; up to 60 tables; every Release 1.0 feature: live booking view, exceptions and degraded payment mode, audit trail, daily backup with Excel export; up to 5 staff accounts; support by LINE within one business day |
| Premium | 990 | Standard plus the Release 2.0 features: scheduled reminders, grace extension, waitlist, booking transfer, reports and analytics; unlimited tables and staff accounts; concert-night priority support (response within 2 hours) |
| Setup (paid plans, one-time) | 2,500 | zone map, packages and prices configured; LINE Official Account and payment gateway connected; 2-hour training of the Manager and Front Staff |
| Pilot implementation (La Loy, Year 0, one-time) | 150,000 | custom build of Release 1.0 and 2.0 for the pilot restaurant, paid 30 % at LCA, 40 % at IOC and 30 % at go-live; Premium free of charge during the pilot year |

<!-- /finance -->

The adoption plan (Table 3.2) assumes an addressable market of about 500 live-music venues in Bangkok and the major cities that sell tables for concert nights, of which 130 pay for the service by the end of Year 5 (26 %), with a Free-plan base about as large as the paying base and a churn of 10 % a year. The plan is deliberately slow in Year 2, when the software house sells with one reference customer.

*Table 3.2 Adoption plan*

<!-- finance: adoption -->

| Shops | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|---|
| Paying shops at year end (Standard + Premium) | - | - | 15 | 40 | 80 | 130 |
| Free-plan shops at year end | - | La Loy (pilot) | 20 | 50 | 90 | 140 |
| New paid subscriptions during the year (incl. replacement of 10 % churn) | - | - | 15 | 27 | 44 | 58 |
| Average paying shops during the year | - | - | 8 | 28 | 60 | 105 |

<!-- /finance -->

## 3.2 Basis of the Analysis

The analysis covers Year 0, the build year from 3 August 2026 to 30 July 2027, Year 1, the pilot and productization year to 28 July 2028, and four expansion years, Years 2 to 5 (August 2028 to July 2032). Costs and revenues are in 2026 Thai Baht, held constant, VAT excluded (the software house stays below the VAT registration threshold within the horizon), and discounted at 10 % a year. The software house's labor is costed at its internal cost rates although the four partners could choose to defer their own pay; the partners' cash view is shown separately in Section 3.6. The restaurant's benefits are not part of the analysis. The volumes that drive the revenue, the number of restaurants that adopt the service and the plan mix, are planning assumptions (Table 3.3) that the pilot year has to confirm before the expansion is authorized.

*Table 3.3 Planning assumptions of the financial analysis*

| Assumption | Value | Basis |
|---|---|---|
| Discount rate | 10 % a year | hurdle rate of a small software house for an internal product investment |
| Horizon | Year 0 (build) + Year 1 (pilot, productization) + Years 2 to 5 (expansion) | useful life of the product before a major rewrite |
| Pilot implementation fee | 150,000 THB, paid 30 % at LCA, 40 % at IOC, 30 % at go-live | fixed price for a custom LINE booking system of this size; the rest of the build is the software house's product investment |
| Plan prices | Free 0, Standard 690, Premium 990 THB a month; setup 2,500 THB | ceiling of 1,000 THB a month including hosting; Premium below the ceiling; setup covers 2 hours of configuration and training |
| Plan mix and average revenue | 50 % Standard, 50 % Premium: 840 THB a month per paying shop | Premium carries the features restaurants ask for first (reminders, waitlist, reports) |
| Adoption | paying shops at year end 15, 40, 80, 130 in Years 2 to 5; Free-plan shops 20, 50, 90, 140; churn 10 % a year | about 500 addressable venues; 26 % share by Year 5; one reference customer in Year 2 |
| Team cost rates | 350 THB/h (Project Manager, System Analyst / Architect), 300 THB/h (Requirements Specifier / Designer, QA / Tester) | the software house's internal cost rates for its engineers, 2026 |
| Team availability | 6 to 16 hours a week per engineer in Year 0, 2 to 7.5 hours a week in Year 1 (Table 3.4) | part-time allocation alongside the software house's other work |
| Hosting | 700 THB a month for the service plus 50 THB a month per shop, free or paying | one application server and database serving all shops; storage and messages grow per shop |
| Support and maintenance | 16 hours a month base plus 0.5 hour a month per paying shop, at 300 THB/h | second-line support, LINE and gateway API changes, concert-night incidents |
| Sales and marketing | 2,000 THB a month from Year 2 | LINE ads, venue visits, demo events; the Free plan and the "Powered by CTRS" footer do the rest |
| Contingency reserve | 10 % of the development cost of Year 0 and of the productization work of Year 1 | known risks of Table 2.24; a management reserve is not budgeted |
| Payment gateway fees, LINE Official Account plan, door tablet | none for the software house | each restaurant holds its own merchant account and LINE plan and buys its own check-in device (about 9,000 THB) |

## 3.3 Cost Analysis

### 3.3.1 Effort and labor cost

Effort is estimated top-down per phase from the planned hours a week of each engineer (Table 3.4): Year 0 builds Release 1.0 and 2.0 for the pilot restaurant in the eight iterations of the schedule (Section 2.8), Year 1 adds the productization of Release 2.1 (C4, T3). The engineers hold the RUP roles fixed in the project's Development Case; in Construction the Designer and the QA engineer also implement. Milestone 2 replaces this top-down figure by a bottom-up estimate per WBS task.

*Table 3.4 Effort and labor cost by phase*

<!-- finance: effort -->

| Phase (iterations) | Year | Weeks | Project Manager (Boonnisa T.) | System Analyst (Sirapatr C.) | Requirements Specifier (Chawanakorn S.) | Quality Assurance (Watayut A.) | Hours |
|---|---|---|---|---|---|---|---|
| Inception (I1, I2) | 0 | 4 | 32 | 40 | 32 | 24 | 128 |
| Elaboration (E1, E2) | 0 | 8 | 64 | 96 | 96 | 64 | 320 |
| Construction Release 1.0 (C1, C2) | 0 | 16 | 128 | 224 | 256 | 192 | 800 |
| Transition Release 1.0 (T1) | 0 | 5 | 40 | 40 | 50 | 60 | 190 |
| Construction Release 2.0 (C3) | 0 | 12 | 72 | 144 | 168 | 120 | 504 |
| Transition Release 2.0 (T2) | 0 | 5 | 30 | 30 | 40 | 50 | 150 |
| Construction Release 2.1 productization (C4) | 1 | 24 | 60 | 120 | 180 | 120 | 480 |
| Transition Release 2.1 (T3) | 1 | 4 | 8 | 12 | 20 | 20 | 60 |
| **Total hours** | | **78** | **434** | **706** | **842** | **650** | **2,632** |
| Rate (THB/h) | | | 350 | 350 | 300 | 300 | |
| **Labor cost (THB)** | | | **151,900** | **247,100** | **252,600** | **195,000** | **846,600** |
| of which Year 0 (build for the pilot restaurant) | 0 | 50 | | | | | 674,600 |
| of which Year 1 (productization) | 1 | 28 | | | | | 172,000 |

<!-- /finance -->

### 3.3.2 Capital expenditure (CAPEX)

The service runs in the cloud and the engineers develop on the software house's existing laptops; capital expenditure is limited to the test devices for the LINE in-app browser and the door check-in (Table 3.5). The pilot restaurant buys its own check-in tablet.

*Table 3.5 CAPEX*

<!-- finance: capex -->

| CAPEX | Unit price | Units | Year 0 | Years 1 to 5 | Total |
|---|---|---|---|---|---|
| Test devices: Android phone and 10-inch tablet for LIFF and check-in testing | 15,000 | 1 | 15,000 | - | 15,000 |
| **Total CAPEX** | | | **15,000** | - | **15,000** |

<!-- /finance -->

### 3.3.3 Operating expenditure (OPEX)

Operating expenditure in Years 0 and 1 is the development labor of Table 3.4, the hosting and services used during the build and the pilot, and the company and legal set-up the subscription business needs; from Year 2 it is the running cost of the multi-tenant service, which scales with the number of shops (Table 3.6).

*Table 3.6 OPEX*

<!-- finance: opex -->

<div class="compact" markdown="1">

| OPEX | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Total |
|---|---|---|---|---|---|---|---|
| Development labor (Table 3.4) | 674,600 | 172,000 | - | - | - | - | 846,600 |
| Development and staging hosting (12 months x 300 THB) | 3,600 | - | - | - | - | - | 3,600 |
| Production hosting for the pilot restaurant (Mar-Jul 2027, 5 months x 700 THB) | 3,500 | - | - | - | - | - | 3,500 |
| Domain name and TLS certificate (first year) | 1,200 | - | - | - | - | - | 1,200 |
| Payment gateway sandbox, LINE Developers, GitHub, Figma, PlantUML (free tiers) | - | - | - | - | - | - | 0 |
| Company registration, terms of service, privacy policy and data-processing agreement (legal) | - | 15,000 | - | - | - | - | 15,000 |
| Production hosting during the pilot year (12 months x 700 THB) | - | 8,400 | - | - | - | - | 8,400 |
| Support of the pilot restaurant (8 h/month x 300 THB) | - | 28,800 | - | - | - | - | 28,800 |
| Hosting of the service: base (700 THB/month) plus 50 THB/month per shop | - | - | 19,200 | 45,900 | 86,400 | 140,400 | 291,900 |
| Support and maintenance: 16 h/month base plus 0.5 h/month per paying shop, at 300 THB/h | - | - | 71,100 | 107,100 | 165,600 | 246,600 | 590,400 |
| Sales and marketing (2,000 THB/month) | - | - | 24,000 | 24,000 | 24,000 | 24,000 | 96,000 |
| Onboarding of new paid subscriptions (2 h each) | - | - | 9,000 | 16,200 | 26,400 | 34,800 | 86,400 |
| **Total OPEX** | **682,900** | **224,200** | **123,300** | **193,200** | **302,400** | **445,800** | **1,971,800** |

</div>

<!-- /finance -->

### 3.3.4 Total cost

*Table 3.7 Total cost*

<!-- finance: totalcost -->

| Cost | Details | Total (THB) |
|---|---|---|
| CAPEX | Test devices | 15,000 |
| OPEX, Year 0 build | Labor of the eight-iteration build, development and pilot hosting, domain | 682,900 |
| Contingency reserve, Year 0 | 10 % of the Year 0 cost, for the risks of Table 2.24 | 69,790 |
| **Project budget, Year 0** | | **767,690** |
| OPEX, Year 1 pilot and productization | Labor of C4 and T3, company and legal set-up, hosting and support of the pilot restaurant | 224,200 |
| Contingency reserve, Year 1 | 10 % of the productization work | 18,700 |
| **Project budget, Year 1** | | **242,900** |
| **Project budget, Years 0 and 1** | development, pilot and productization | **1,010,590** |
| OPEX, Years 2 to 5 | Operation of the subscription service: hosting, support, sales, onboarding | 1,064,700 |
| **Total cost, Years 0 to 5** | | **2,075,290** |

<!-- /finance -->

## 3.4 Revenue Analysis

The software house earns the pilot implementation fee in Year 0, nothing in the pilot year, and from Year 2 the subscriptions of Table 3.1 on the paying shops of Table 3.2 plus a setup fee for every new paid subscription (Table 3.8). Free-plan shops earn nothing and cost hosting; they are the sales funnel.

*Table 3.8 Revenue per year*

<!-- finance: revenue -->

| Revenue | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Total |
|---|---|---|---|---|---|---|---|
| Pilot implementation fee (La Loy) | 150,000 | - | - | - | - | - | 150,000 |
| Subscriptions (840 THB a month per paying shop on average, 50 % Standard, 50 % Premium) | - | - | 75,600 | 277,200 | 604,800 | 1,058,400 | 2,016,000 |
| Setup fees (2,500 THB per new paid subscription) | - | - | 37,500 | 67,500 | 110,000 | 145,000 | 360,000 |
| **Total revenue** | **150,000** | **-** | **113,100** | **344,700** | **714,800** | **1,203,400** | **2,526,000** |

<!-- /finance -->

## 3.5 Cost-Benefit Analysis

Table 3.9 brings the costs of Section 3.3 and the revenues of Section 3.4 together as a discounted cash flow; Table 3.10 derives from it the net present value (NPV), the return on investment (ROI, undiscounted, over Years 0 to 5), the discounted payback period, the internal rate of return (IRR) and the discounted life-cycle cost.

*Table 3.9 Cost-benefit analysis*

<!-- finance: cba -->

<div class="compact landscape" markdown="1">

| Item (discount rate 10 %) | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Total |
|---|---|---|---|---|---|---|---|
| Discount factor | 1.0000 | 0.9091 | 0.8264 | 0.7513 | 0.6830 | 0.6209 | |
| **1. Costs** | | | | | | | |
| 1.1 CAPEX | 15,000 | - | - | - | - | - | 15,000 |
| 1.2 OPEX | 682,900 | 224,200 | 123,300 | 193,200 | 302,400 | 445,800 | 1,971,800 |
| 1.3 Contingency reserve | 69,790 | 18,700 | - | - | - | - | 88,490 |
| Total costs | 767,690 | 242,900 | 123,300 | 193,200 | 302,400 | 445,800 | 2,075,290 |
| Total discounted costs | 767,690 | 220,818 | 101,901 | 145,154 | 206,543 | 276,807 | 1,718,913 |
| Cumulative discounted costs | 767,690 | 988,508 | 1,090,409 | 1,235,563 | 1,442,106 | 1,718,913 | |
| **2. Revenues** | | | | | | | |
| 2.1 Pilot implementation fee | 150,000 | - | - | - | - | - | 150,000 |
| 2.2 Subscriptions | - | - | 75,600 | 277,200 | 604,800 | 1,058,400 | 2,016,000 |
| 2.3 Setup fees | - | - | 37,500 | 67,500 | 110,000 | 145,000 | 360,000 |
| Total revenues | 150,000 | - | 113,100 | 344,700 | 714,800 | 1,203,400 | 2,526,000 |
| Total discounted revenues | 150,000 | - | 93,471 | 258,978 | 488,218 | 747,217 | 1,737,884 |
| Cumulative discounted revenues | 150,000 | 150,000 | 243,471 | 502,449 | 990,667 | 1,737,884 | |
| **3. Net cash flow** | | | | | | | |
| Net cash flow (revenues - costs) | -617,690 | -242,900 | -10,200 | 151,500 | 412,400 | 757,600 | 450,710 |
| Discounted net cash flow | -617,690 | -220,818 | -8,430 | 113,824 | 281,675 | 470,410 | 18,971 |
| Cumulative discounted net cash flow | -617,690 | -838,508 | -846,938 | -733,114 | -451,439 | 18,971 | |

</div>

<!-- /finance -->

*Table 3.10 Financial results*

<!-- finance: results -->

| Measure | Value | Meaning |
|---|---|---|
| Net present value (NPV, 10 %) | **18,971 THB** | present value of revenues minus costs over Years 0 to 5; positive, but small against the 1,010,590 THB invested in Years 0 and 1 |
| Return on investment (ROI, undiscounted, Years 0 to 5) | **22 %** | (total revenues - total costs) / total costs = (2,526,000 - 2,075,290) / 2,075,290 |
| Discounted payback period | **5.0 years (during Year 5)** | cumulative discounted net cash flow turns positive |
| Internal rate of return (IRR) | **11 %** | discount rate at which NPV = 0; just above the 10 % hurdle |
| Life-cycle cost (discounted, Years 0 to 5) | **1,718,913 THB** | present value of all costs, development, pilot and operation |
| Break-even scale | **about 40 paying shops** | the year in which subscriptions and setup fees first exceed the operating cost and pay off the investment is Year 3 to 4 at the base adoption |

<!-- /finance -->

**Results.** At the base-case assumptions the investment is recovered at the end of Year 5 with an NPV just above zero and an IRR just above the 10 % hurdle: the software house invests about 860,000 THB net in Years 0 and 1, the service breaks even on its operating cost at about 15 paying shops (Year 2), and the surplus of Years 4 and 5 (about 410,000 and 760,000 THB a year) pays the investment back. Within five years the case is therefore marginal; its value lies in Year 6 and later, when a service with 130 paying shops earns about 750,000 THB a year net without further development, and in the product the software house then owns.

## 3.6 Sensitivity and the Partners' Cash View

Table 3.11 recomputes the result for the levers the software house controls or must watch: adoption, prices, the pilot fee, the decision to stop after the pilot year, and the partners' cash position if they defer their own pay for this project.

*Table 3.11 Sensitivity of the result*

<!-- finance: sensitivity -->

| Case | Budget Years 0 and 1 | Revenue Years 0 to 5 | NPV (10 %) | ROI | Discounted payback | IRR |
|---|---|---|---|---|---|---|
| Base case (adoption as planned, pilot fee 150,000 THB, labor at the software house's cost rates) | 1,010,590 | 2,526,000 | 18,971 | 22 % | 5.0 years | 11 % |
| Adoption 30 % higher (paying shops 20 / 52 / 104 / 169 at year end) | 1,010,590 | 3,240,840 | 355,608 | 42 % | 4.4 years | 20 % |
| Adoption 30 % lower (paying shops 10 / 28 / 56 / 91) | 1,010,590 | 1,808,660 | -319,093 | -3 % | beyond Year 5 | -1 % |
| Prices 20 % lower (Standard 552, Premium 792, setup 2,000) | 1,010,590 | 2,050,800 | -298,606 | -1 % | beyond Year 5 | -1 % |
| No pilot implementation fee (La Loy as an unpaid design partner) | 1,010,590 | 2,376,000 | -131,029 | 14 % | beyond Year 5 | 6 % |
| Stop after the pilot year (expansion gate not passed): exposure of the software house | 1,010,590 | 150,000 | -838,508 | -85 % | beyond Year 5 | n/a |
| Partners' cash view: the four partners draw no salary for this project in Years 0 and 1 | 79,330 | 2,526,000 | 933,031 | 121 % | 2.5 years | above 500 % |

<!-- /finance -->

Adoption is the decisive lever: 30 % more shops turn the case clearly positive, 30 % fewer shops or a 20 % lower price turn it negative, and the 1,000 THB a month price ceiling leaves no room to compensate a slow uptake by charging more. The pilot fee matters because it is the only revenue before Year 2: without it the case does not pay back within the horizon. The exposure of the software house is bounded by the expansion gate: if the pilot does not confirm the plan, the loss is limited to the net investment of Years 0 and 1. From the partners' cash view the project needs about 80,000 THB of cash and returns it within the third year, which is why a four-partner software house can carry it as a product investment.

## 3.7 Conclusion

The project is financially justified as a product investment with a stage gate, not as a one-off custom build: the pilot implementation fee covers only a fifth of the build, and the return depends on selling the service to other restaurants at up to 990 THB a month. The team recommends that the software house authorizes Years 0 and 1 (build, pilot and productization, 1,010,590 THB with reserves, 860,590 THB net of the pilot fee) and decides the expansion at the end of the pilot year against three gate criteria: (1) La Loy meets the pilot success criteria of the charter and continues on a paid plan; (2) at least 10 restaurants are on the waiting list for the Free or a paid plan; (3) the productized Release 2.1 runs La Loy's concert nights with the per-shop hosting and support cost at or below the figures of Table 3.3. The financial analysis is re-run with the bottom-up cost estimate of Milestone 2 at the Lifecycle Architecture milestone and with the pilot data at the expansion gate.

# 4. Project Charter

*Table 4.1 Project charter*

<div class="charter" markdown="1">

| Project Charter | |
|---|---|
| **Project title** | Concert Table Reservation System (CTRS): pilot implementation for La Loy Restaurant and productization as a subscription service |
| **Performing organization** | The software house of the four team members (company name to be confirmed by the partners) |
| **Project start date** | 3 August 2026 |
| **Project finish date** | 28 July 2028 (Release 1.0 in operation at La Loy 2 April 2027; Release 2.0 30 July 2027; productized Release 2.1 11 February 2028; expansion decision 28 July 2028) |
| **Budget information** | Project budget 1,010,590 THB: Year 0 build 767,690 THB (labor 674,600 THB for 2,092 hours at the software house's cost rates, test devices 15,000 THB, hosting and domain 8,300 THB, contingency reserve 69,790 THB) and Year 1 pilot and productization 242,900 THB (labor 172,000 THB for 540 hours, company and legal set-up 15,000 THB, pilot hosting and support 37,200 THB, contingency reserve 18,700 THB). Revenue inside the project: La Loy's pilot implementation fee of 150,000 THB. Net investment of the software house: 860,590 THB. |
| **Financial analysis** | Software-house view over Years 0 to 5, 10 % discount rate: revenues 2,526,000 THB (pilot fee, subscriptions at 690 and 990 THB a month, setup fees; 130 paying restaurants by Year 5); NPV 18,971 THB; ROI 22 % (undiscounted); discounted payback 5.0 years; IRR 11 %; discounted life-cycle cost 1,718,913 THB. Marginal within five years, positive from Year 6; adoption is the decisive lever, so the expansion is decided at the gate at the end of the pilot year (Section 3). |
| **Project manager** | Boonnisa Tangjitpermkwamdee (Project Manager and Change Control Manager) |
| **Project objectives** | 1. Deliver, for La Loy's concert nights, a LINE-integrated self-service reservation system with real-time table map, automatic 15-minute hold, full payment through a payment gateway with automatic confirmation and QR e-ticket, and a shared back-office with live booking view and QR check-in on one central record, so that double bookings and payment fraud are eliminated, the Manager handles exceptions only, and booking data serves reminders, reports and marketing (Table 2.1).<br>2. Run the system through a pilot year at La Loy and measure it against the success criteria below.<br>3. Productize it as a multi-tenant subscription service with Free, Standard and Premium plans within the 1,000 THB a month ceiling, ready to be offered to other live-music restaurants at the expansion decision. |
| **Project success criteria** | 1. Release 1.0 Core in operation at La Loy on 2 April 2027, Release 2.0 Growth on 30 July 2027 and Release 2.1 on 11 February 2028, within the project budget of 1,010,590 THB.<br>2. Zero double bookings on La Loy's concert nights after go-live; table status real-time on one record.<br>3. A booking completed within 3 minutes from table selection to confirmation, without a Manager reply (Table 2.2).<br>4. No-show rate at La Loy reduced by 35 % within six months of Release 2.0 (Table 2.2).<br>5. The restaurant's operating cost of hosting, APIs and LINE plan at or below 1,000 THB a month; check-in within 15 seconds per table; 5 transactions per second at booking-open time.<br>6. Vision approved by the Owner at LCO, SRS signed off at LCA, and the acceptance tests of the two main use cases (reserve a concert table, check in with e-ticket) passed with the Manager and the Front Staff.<br>7. At the expansion decision: La Loy continues on a paid plan, at least 10 restaurants are on the waiting list, and the per-shop hosting and support cost of the productized service is at or below the figures of Table 3.3. |
| **Approach** | 1. Tailored Rational Unified Process with four phases and ten iterations (I1, I2, E1, E2, C1, C2, T1, C3, T2, then C4 and T3 in the pilot year), each closed by an assessment and each phase by a milestone decision (LCO, LCA, IOC, Product Release); the tailoring is recorded in the project's Development Case.<br>2. Requirements engineering with RUP artifacts (Vision, Use-Case Model, use-case specifications, Software Requirements Specification, Supplementary Specification), reviewed by an independent QA role and baselined under a Change Control Board.<br>3. Project management with PMBOK artifacts (business case, charter, scope statement, WBS, estimates, schedule, cost baseline, quality, risk and communication plans), produced with Generative AI as an assistant and decided by the team's Review Board.<br>4. Construction in two-month iterations that each deliver a testable increment, with a load test before IOC and a pilot on real concert nights in Transition.<br>5. Payment gateway and LINE integration verified early: sandbox from Elaboration, merchant onboarding checks before LCA, degraded payment mode as the fallback.<br>6. Pilot year with one restaurant before any expansion: KPIs measured on every concert night, productization in parallel, expansion decided against written gate criteria. |
| **Stakeholders** | The software house (sponsor and product owner), Restaurant Owner of La Loy (pilot customer), Restaurant Manager (customer representative, domain expert), Front Staff, customers, artists, the four-member project team, LINE Corporation, the payment gateway provider and the cloud hosting provider (Table 4.2). |
| **Sign-off** | Project Sponsor: managing partner of the software house · Pilot customer: Restaurant Owner, La Loy · Project Manager: Boonnisa Tangjitpermkwamdee · Date: |

</div>

*Table 4.2 Stakeholder list*

| No. | Stakeholder | Internal / external | Role in the project | Interest and expectation | Contact |
|---|---|---|---|---|---|
| 1 | The software house (its four partners as management) | Internal | Project Sponsor and product owner: funds the build and the productization, owns the product, decides the expansion at the end of the pilot year | Recover the investment through subscriptions; own a product it can sell to other restaurants | Partners' meeting |
| 2 | Restaurant Owner, La Loy | External (pilot customer) | Pilot customer executive: signs the pilot implementation agreement, approves business rules and scope, approves the Vision at LCO and signs off the SRS at LCA, decides change requests that affect scope or budget | Accurate revenue and booking figures from one record; fewer losses; operating cost within 1,000 THB a month; a fixed price for the build | In person at the restaurant, afternoons, through the Manager |
| 3 | Restaurant Manager | External (pilot customer) | Customer representative and domain expert; source of the business rules and the as-is process; sets benefit and priority of features; reviews use-case specifications and the back-office prototype; member of the Change Control Board; joins acceptance testing | Chat and data-entry workload replaced by monitoring one live view; control of rounds, prices and exceptions | LINE Official Account of the restaurant; in person, afternoons |
| 4 | Front Staff | External (pilot customer) | On-site end users; describe the check-in procedure; review and accept the check-in use case and prototype | Check-in by QR instead of name lookup; fewer seating disputes | Through the Manager |
| 5 | Customers | External | Primary users; answer the questionnaire on the LINE booking channel; a sample tries the booking prototype | Book and pay by themselves at any time; immediate confirmation, ticket and reminders | LINE Official Account; survey |
| 6 | Artists | External | Indirect stakeholder; informed through the Manager | Reliable attendance figures ahead of the show | Through the Manager |
| 7 | Boonnisa Tangjitpermkwamdee | Internal (project team) | Project Manager, Change Control Manager; Implementer in Construction | Project delivered on schedule and budget; pilot KPIs met | Software house |
| 8 | Sirapatr Chalermwattanatrai | Internal (project team) | System Analyst, Software Architect | Requirements and architecture accepted at LCO and LCA; multi-tenant architecture for Release 2.1 | Software house |
| 9 | Chawanakorn Sanannam | Internal (project team) | Requirements Specifier, User-Interface Designer, Designer; Implementer in Construction | Use-case specifications, SRS and prototype accepted | Software house |
| 10 | Watayut Aiamanan | Internal (project team) | Quality Assurance (Requirements Reviewer, Process Engineer), Test Designer and Tester; Implementer in Construction | Reviews independent of authorship; testable requirements | Software house |
| 11 | Other live-music restaurants (future subscribers) | External (market) | Target customers of the subscription service from Year 2; a waiting list is built during the pilot year | A working, affordable concert-table system with a reference customer | Waiting list, Free-plan sign-up |
| 12 | LINE Corporation | External (platform provider) | Provides LINE Login, LIFF, Messaging API and the Official Account plan | Use within the platform's policies and quota | LINE Developers console |
| 13 | Beam Checkout (fallback: Opn Payments) | External (service provider) | Payment gateway: each restaurant's merchant account, hosted checkout, webhooks, refunds | Merchant onboarding of the shops; transaction volume | Merchant support of the gateway |
| 14 | Cloud hosting provider | External (service provider) | Hosts the multi-tenant service within the hosting assumptions of Table 3.3 | Paid subscription | Provider console |

# 5. Project Organization Chart

The project organization (Figure 5.1) has a sponsor side and a customer side. The software house, represented by its four partners as management, sponsors the project, owns the product and decides the expansion; the Project Manager leads the four-member team, in which each engineer holds several RUP roles under two rules fixed in the Development Case: every artifact has exactly one owner role, and the reviewer of an artifact is never its author, which is why Quality Assurance is a separate role that produces no requirements artifact. The Restaurant Owner of La Loy is the pilot customer under the pilot implementation agreement; the Restaurant Manager represents the users day to day and sits on the Change Control Board, with the Front Staff and the customers as end users behind the Manager. The Change Control Board (chaired by the Change Control Manager, with the System Analyst, the Manager, QA and, when scope or budget is affected, the Owner) decides change requests. Table 5.1 gives the responsibilities of each role.

![Project organization chart](../assets/diagrams/org-chart.png)

*Figure 5.1 Project organization chart of the CTRS project*

*Table 5.1 Roles and responsibilities*

| Group | Role (holder) | Key responsibilities |
|---|---|---|
| Sponsor | The software house (four partners as management) | Funds the build, the pilot and the productization; owns the product and the plans and prices; reviews the pilot KPIs; decides the expansion at the end of the pilot year |
| Pilot customer | Restaurant Owner | Signs the pilot implementation agreement; sets business goals and key policies (zone prices, table fee, refunds); approves the Vision at LCO and signs off the SRS at LCA; decides change requests that affect scope or budget |
| User side | Restaurant Manager | Main customer representative; provides the business rules and as-is knowledge through interviews and observation; sets benefit and priority of features; reviews use-case specifications and the back-office prototype; Change Control Board member; joins acceptance testing |
| User side | Front Staff | Describe the check-in procedure and on-site problems; review the check-in use case and prototype; join acceptance testing of check-in |
| User side | Customers | Answer the questionnaire on the LINE booking channel; a sample tries the booking prototype; no approval authority |
| Project team | Project Manager and Change Control Manager (Boonnisa T.) | Plans and controls scope, schedule, budget and risks; produces the business case, charter, Software Development Plan, iteration plans, Risk List and status assessments; runs iteration assessments, milestone reviews and the pilot review; chairs the Change Control Board and keeps the baselines in Git |
| Project team | System Analyst and Software Architect (Sirapatr C.) | Leads elicitation and the Use-Case Model; owns the Vision, Stakeholder Requests, Glossary and Requirements Attributes; main contact with the restaurant; prioritizes use cases, produces the Software Architecture Document (including the multi-tenant architecture of Release 2.1), assesses the LINE Platform and the payment gateway |
| Project team | Requirements Specifier, User-Interface Designer and Designer (Chawanakorn S.) | Details the use cases and the software requirements (SRS, Supplementary Specification); models and prototypes the user interface and has users try it; produces the Analysis Model; implements in Construction |
| Project team | Quality Assurance, Test Designer and Tester (Watayut A.) | Reviews the requirements against the RUP checkpoints and records Review Records; produces and audits the Development Case; designs the test plan and test cases of the main use cases; runs tests, load tests and acceptance tests; implements in Construction |
| Board | Change Control Board | Approves, rejects or defers change requests after impact analysis through traceability; members: Change Control Manager (chair), System Analyst, Manager, QA, and the Owner when scope or budget is affected |
