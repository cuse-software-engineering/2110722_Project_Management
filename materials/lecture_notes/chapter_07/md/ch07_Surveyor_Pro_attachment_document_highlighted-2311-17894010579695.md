# Surveyor Pro — Attachment Document (Basis of Estimates)

*Case-study attachment document for Chapter 7 (Project Cost Management): the "Surveyor Pro" cost-estimate example from the course textbook (Schwalbe, Information Technology Project Management, 9th ed.), used with slides 15–17 (How to Develop a Cost Estimate and Basis of Estimates). The lecturer highlighted most of the cost-driving facts in cyan; a few handwritten notes are transcribed in brackets. The three scanned pages are in `../ch07_Surveyor_Pro_attachment_document_highlighted-2311-17894010579695_png/` (page-1.png … page-3.png); the textbook prose is condensed here to the facts and figures needed for the estimate rather than copied word for word.*

| Page | Image | Content |
|---|---|---|
| 1 | [page-1.png](../ch07_Surveyor_Pro_attachment_document_highlighted-2311-17894010579695_png/page-1.png) | Project description, basis of estimates (bullets 1–9) |
| 2 | [page-2.png](../ch07_Surveyor_Pro_attachment_document_highlighted-2311-17894010579695_png/page-2.png) | Bullets 10–11, estimating approach, WBS items 1–3.1 |
| 3 | [page-3.png](../ch07_Surveyor_Pro_attachment_document_highlighted-2311-17894010579695_png/page-3.png) | WBS items 3.2–6 |

## Page 1 — Project description

- Surveyor Pro: a **government project** for an information system with expert systems, object-oriented databases and wireless communications.
- Purpose (highlighted): give **instant, graphical information to help government surveyors do their jobs** — the surveyor touches a map on a handheld device and the system prompts for the type of information needed for that area.
- Helps plan and implement many projects, **from layering fiber-optic cable to installing water lines**.

## Page 1 — Basis of estimates (assumptions)

1. **Preceded by a detailed study and proof of concept** that produced a prototype handheld device and much of the software (basic functionality, link to GPS and other government databases). Some data is available to estimate future labor costs (especially software development) and handheld-device costs.
2. **Main goal:** produce **100 handheld devices**, continue developing the software (especially the user interface), test the new system in the field, and **train 100 surveyors** in selected cities. A follow-up contract for many more devices is expected if this project succeeds.
3. **WBS:**
   - 1. Project management
   - 2. Hardware — 2.1 Handheld devices, 2.2 Servers
   - 3. Software — 3.1 Licensed software, 3.2 Software development
   - 4. Testing
   - 5. Training and support
   - 6. Reserves
4. **Costs must be estimated by WBS and by month**; progress will be reported with **earned value analysis**, which needs this type of estimate.
5. **Costs in U.S. dollars**; project length is one year, so **no inflation**.
6. Managed by the government's project office: a **part-time project manager and four team members**. Team members' hours: **25% project management, 25% software development, 25% training and support, 25% non-project work**.
7. Handheld devices are **purchased from the company that developed the prototype**; at 100 units the rate is **$600 per unit**. **Four additional servers** are needed.
8. **Purchased software licenses** for GPS and three other external systems. Software development covers a **graphical user interface, an online help system, and a new module for tracking surveyor performance** *[handwritten: "track on device"]*.
9. **Testing costs should be low** thanks to the prototype project: estimate = **10% of total hardware and software estimates** *[handwritten: "test cost = 10% hw/sw cost"]*.
10. **Training**: instructor-led classes in **five locations**; most training is **outsourced** (course materials, sessions, and **help-desk support for three months**).

## Page 2 — Assumptions (continued) and estimating approach

11. Several risks → include **20% of the total estimate as reserves**.
12. A **computer model** of the estimate is required so inputs (labor hours, labor rates …) can be changed easily.

- The team can access **cost estimates and actual information from similar projects**, the proof-of-concept project, and past contractors. **Software-estimating tools based on function points** are also available.
- **Function points** (highlighted definition): a measure of software size based on what the software does for end users — inputs, outputs, inquiries, internal data, external interface data. Defined by Allen Albrecht in the 1970s; today the international standard and the most commonly used size metric, followed by lines of code.
- Approach: **estimate the cost of each WBS item first, then determine when the work will be performed** (by month). The **budget expert approved this approach**.

### Cost assumptions per WBS category

1. **Project management** — compensation for the **part-time PM and 25% of the four team members' time**. Rates: **$100/hour (PM)**, **$75/hour (each team member)**, based on **160 hours/month full time**.
   - PM hours: 160/2 × 12 = **960 hours**.
   - Team members (25% each, four people): 160 × 12 = **1,920 hours** total.
   - Plus contracted labor: **10% of the software development + testing estimates** = 10% × ($594,000 + $69,000). *[handwritten margin note beside this item]*
2. **Hardware**
   - 2.1 Handheld devices: **100 devices × $600**.
   - 2.2 Servers: **4 servers × $4,000**.
3. **Software**
   - 3.1 Licensed software: negotiated per supplier; expected to be lower than usual because of the probable follow-up contracts and publicity — use **$200 per handheld device**.

## Page 3 — Cost assumptions (continued)

   - 3.2 Software development: **two approaches — a labor estimate and a function point estimate; the higher estimate is used**. If they **differ by more than 20%, a third estimation approach** is required. The proof-of-concept supplier gives the labor-estimate input; local technical experts make the function point estimate.
4. **Testing** — **10% of the total hardware and software cost** (based on similar projects).
5. **Training and support** — per-trainee basis plus travel: **$500 per trainee (100 trainees)**, travel **$700/day/person** for instructors and project team members, **12 travel days** in total. Team-member labor is added because they assist with training and post-training support: **1,920 hours** total.
6. **Reserves** — **20% of the total estimate**, as directed.
