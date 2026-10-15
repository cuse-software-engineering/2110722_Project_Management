#!/usr/bin/env python3
"""Fill the lecturer's Exercise 3 answer form (function point, COCOMO II, cost estimation, earned value) and write
the submission PDF.

The form (problem/exercise3_1_69_6abb503eb7b0c.pdf) is kept as it is: the answers are written into its answer
cells, dotted blanks and check boxes with PyMuPDF, in dark blue so they stand apart from the printed form. The
calculation parts (COCOMO II steps 4-8, the cost-estimation table, the earned value figures) are also written out
in the blank space of the pages, as the form asks ("show how you calculate").

All numbers (function point ratings, unadjusted FP, KLOC, E, PM, TDEV, staff size, the cost table, EVM) are computed
here from the inputs and the chapter 7 tables, so the written answers cannot disagree with each other; the worked
solution is also written to workspace/solution.md for review.

Usage:  python3 tools/fill_form.py            (from assignments/individual/exercises/exercise_3/)
Output: report/watayut_6970267821.pdf, workspace/solution.md
"""
import math
import pathlib

import pymupdf

EXERCISE = pathlib.Path(__file__).resolve().parent.parent
FORM = EXERCISE / "problem" / "exercise3_1_69_6abb503eb7b0c.pdf"
OUT = EXERCISE / "report" / "watayut_6970267821.pdf"
SOLUTION_MD = EXERCISE / "workspace" / "solution.md"
FONT_DIR = EXERCISE.parents[4] / "2110628_Requirement" / "resources" / "fonts"
FONTS = {"sb": FONT_DIR / "Sarabun-Regular.ttf", "sbb": FONT_DIR / "Sarabun-Bold.ttf"}

STUDENT = "Watayut Aiamanan  6970267821"
INK = (0.05, 0.15, 0.55)

# ======================================================================================= part 1: function points
# Rating tables of chapter 7 slide 37: (FTR-or-RET bands, DET bands) -> (rating, value)
EI_TABLE = {"ftr": [(0, 1), (2, 2), (3, 99)], "det": [(1, 4), (5, 15), (16, 999)],
            "grid": [["Low", "Low", "Average"], ["Low", "Average", "High"], ["Average", "High", "High"]],
            "value": {"Low": 3, "Average": 4, "High": 6}}
EO_TABLE = {"ftr": [(0, 1), (2, 3), (4, 99)], "det": [(1, 5), (6, 19), (20, 999)],
            "grid": [["Low", "Low", "Average"], ["Low", "Average", "High"], ["Average", "High", "High"]],
            "value": {"Low": 4, "Average": 5, "High": 7}}
EQ_TABLE = {**EO_TABLE, "value": {"Low": 3, "Average": 4, "High": 6}}
ILF_TABLE = {"ftr": [(1, 1), (2, 5), (6, 99)], "det": [(1, 19), (20, 50), (51, 999)],
             "grid": [["Low", "Low", "Average"], ["Low", "Average", "High"], ["Average", "High", "High"]],
             "value": {"Low": 7, "Average": 10, "High": 15}}
EIF_TABLE = {**ILF_TABLE, "value": {"Low": 5, "Average": 7, "High": 10}}
TABLES = {"EI": EI_TABLE, "EO": EO_TABLE, "EQ": EQ_TABLE, "ILF": ILF_TABLE, "EIF": EIF_TABLE}


def rate(kind: str, files: int, dets: int) -> tuple[str, int]:
    """Rating and value of a function from its FTR (transactions) or RET (data) count and DET count."""
    t = TABLES[kind]
    row = next(i for i, (lo, hi) in enumerate(t["ftr"]) if lo <= files <= hi)
    col = next(i for i, (lo, hi) in enumerate(t["det"]) if lo <= dets <= hi)
    rating = t["grid"][row][col]
    return rating, t["value"][rating]


# Each question: function type, DET list, FTR list (transactions) or RET list (data), and the reasoning.
FP = {
    1: dict(kind="EO", why="EO – the report sends derived data across the boundary to the user: the hits, % of total "
                           "hits, user sessions and weekday/weekend totals are calculated from the event records, not "
                           "just retrieved, so it is an External Output (not an EQ).",
           dets=["Display button (input, action key)", "Day (output, recursive – Sun … Sat)",
                 "Number of hits (output, derived – count of events per day, recursive)",
                 "% of total hits (output, derived, recursive)",
                 "Number of user sessions (output, derived – count of sessions per day, recursive)",
                 "Total hits (weekdays / weekend) (output, derived)", "Total % of hits (weekdays / weekend) (output, derived)",
                 "Total user sessions (weekdays / weekend) (output, derived)"],
           det_note="(The row number 1–7 and the report title are static labels, not DETs.)",
           ftrs=["Event table (ILF – the interaction data collected per hit, maintained by the software)"],
           rets=None),
    2: dict(kind="EQ", why="EQ – input (the click on a map location) plus output that only retrieves stored data (city, "
                           "state, population, coordinate) from the files; nothing is derived and no ILF is updated, "
                           "so it is an External Inquiry.",
           dets=["Map location clicked (input, action key – e.g. Kansas City)", "City (output)", "State (output)",
                 "Population (output)", "State coordinate (output – e.g. 39.1 N, 94.5 W)"],
           det_note="",
           ftrs=["State population data (ILF – maintained by the US Census Bureau)",
                 "State coordinate data (EIF – maintained by the Surveying and Mapping Section of the US Army, "
                 "only referenced by this application)"],
           rets=None),
    3: dict(kind="EI", why="EI – the user's personal data cross the boundary from outside (the user) into the "
                           "application and maintain an ILF (the user data): the Mor Prom registration form is an "
                           "External Input.",
           dets=["Title (คำนำหน้าชื่อ, drop-down list)", "First name (ชื่อ)", "Last name (นามสกุล)",
                 "National ID number (เลขประจำตัวประชาชน)", "Birth day (วันที่เกิด, drop-down list)",
                 "Birth month (เดือนที่เกิด, drop-down list)", "Birth year (ปีที่เกิด, drop-down list)",
                 "Phone number (เบอร์โทรศัพท์)",
                 "Gender (เพศ – เพศชาย/เพศหญิง, one DET for the pair of radio-style buttons)", "Address (ที่อยู่)",
                 "Province (จังหวัด, drop-down list)", "District (อำเภอ, drop-down list)",
                 "Sub-district (ตำบล, drop-down list)", "Postcode (รหัสไปรษณีย์)", "Hospital (เลือกโรงพยาบาล, drop-down list)",
                 "Save button (บันทึก – the action key that saves the registration)",
                 "Error message (e.g. “กรุณากรอกข้อมูลให้ครบ” / invalid national ID)",
                 "Confirmation message (registration successful)"],
           det_note="(15 personal data fields, as question 4 states, + 1 action key + 1 error message + 1 "
                    "confirmation message. The greyed-out target group (กลุ่มเป้าหมาย = ประชาชนทั่วไป) is filled by the "
                    "system, not entered by the user, so it is not counted; counting it (19 DETs) would not change "
                    "the rating. The drop-down choices for province/district/hospital are code data, not logical "
                    "files, so they add no FTR.)",
           ftrs=["User data (ILF – maintained by the registration, i.e. the personal data are stored in it)"],
           rets=None),
    4: dict(kind="ILF", why="ILF – a user-identifiable group of logically related data (the user data) kept entirely "
                            "inside the Mor Prom boundary and maintained by the application itself (registration, "
                            "recording of shots), so it is an Internal Logical File.",
           dets=["Personal data: 15 data fields (title, first name, last name, national ID, birth day, birth month, "
                 "birth year, phone number, gender, address, province, district, sub-district, postcode, hospital)",
                 "Date of vaccination", "Vaccine name", "Vaccine manufacturer", "Vaccine lot", "Vaccination site"],
           det_note="",
           ftrs=None,
           rets=["Personal data (parent – the user)",
                 "Vaccine shot data (child – one user has many shots; a shot is meaningless without its user)"]),
    5: dict(kind="EIF", why="EIF – a group of logically related data (the organ donation data) that Mor Prom only "
                            "references; it lives outside the boundary and is maintained by another application (the "
                            "Thai Red Cross system, via the Organ Donation API), so it is an External Interface File.",
           dets=["National ID", "Title", "First name", "Last name", "Date of birth", "Occupation", "Address", "Tumbol",
                 "District", "Province", "Postcode", "House phone", "Mobile phone",
                 "Donation date", "Donated organ", "Witness name"],
           det_note="(13 donor-information fields + 3 fields per donated organ.)",
           ftrs=None,
           rets=["Donor information (parent – the donor)",
                 "Donated organ information (child – one donor may donate several organs: donation date, donated "
                 "organ, witness name)"]),
}


def det_count(q: dict) -> int:
    return 15 + 5 if q["kind"] == "ILF" else len(q["dets"])


for q in FP.values():
    n_files = len(q["ftrs"]) if q["ftrs"] is not None else len(q["rets"])
    q["n_det"] = det_count(q)
    q["n_files"] = n_files
    q["rating"], q["value"] = rate(q["kind"], n_files, q["n_det"])

assert [(q["kind"], q["n_det"], q["n_files"], q["rating"], q["value"]) for q in FP.values()] == [
    ("EO", 8, 1, "Low", 4), ("EQ", 5, 2, "Low", 3), ("EI", 18, 1, "Average", 4), ("ILF", 20, 2, "Average", 10),
    ("EIF", 16, 2, "Low", 5)], [(q["kind"], q["n_det"], q["n_files"], q["rating"]) for q in FP.values()]

# Question 6: unadjusted function points
Q6_COUNTS = {"EI": (3, 1, 0), "EO": (1, 0, 0), "EQ": (2, 1, 0), "ILF": (5, 0, 0), "EIF": (1, 0, 0)}
Q6_WEIGHTS = {"EI": (3, 4, 6), "EO": (4, 5, 7), "EQ": (3, 4, 6), "ILF": (7, 10, 15), "EIF": (5, 7, 10)}
Q6_ROWS = {k: [n * w for n, w in zip(Q6_COUNTS[k], Q6_WEIGHTS[k])] for k in Q6_COUNTS}
UFP = sum(sum(r) for r in Q6_ROWS.values())
assert UFP == 67, UFP

# =========================================================================================== part 2: COCOMO II
FP_SIZE = 67
GEARING = 47                                   # QSM table v5.0: JavaScript average = 47 SLOC/FP (median 53)
KLOC = FP_SIZE * GEARING / 1000                # 3.149
A, B, C, D = 2.94, 0.91, 3.67, 0.28

# Ratings chosen for a small JavaScript web application (the kind of system built in this course's group project):
# a familiar kind of product by a small, co-located team with little experience in the language and platform,
# with a somewhat compressed schedule. Scores from chapter 7 slides 54 and 57-61.
SF = {  # scale factor: (rating, value, reason)
    "PREC": ("High", 2.48, "generally familiar – a web application like many built before"),
    "FLEX": ("High", 2.03, "general conformity – few pre-established external interface constraints"),
    "RESL": ("Nominal", 4.24, "about 60% of risk items identified and resolved, architecture reviewed"),
    "TEAM": ("High", 2.19, "largely cooperative stakeholders and team"),
    "PMAT": ("Nominal", 4.68, "SW-CMM level 2 – basic project planning and tracking"),
}
EM = {  # effort multiplier: (rating, value, reason)
    "RELY": ("Nominal", 1.00, "moderate, easily recoverable losses if it fails"),
    "DATA": ("Low", 0.90, "small testing database, D/P < 10"),
    "CPLX": ("Low", 0.87, "simple control, data and user-interface operations"),
    "RUSE": ("Nominal", 1.00, "reusable across the project only"),
    "DOCU": ("Nominal", 1.00, "documentation right-sized to life-cycle needs"),
    "TIME": ("Nominal", 1.00, "≤ 50% use of available execution time"),
    "STOR": ("Nominal", 1.00, "≤ 50% use of available storage"),
    "PVOL": ("Low", 0.87, "stable platform – major change every 12 months"),
    "ACAP": ("Nominal", 1.00, "analysts at the 55th percentile"),
    "PCAP": ("Nominal", 1.00, "programmers at the 55th percentile"),
    "PCON": ("Nominal", 1.00, "12% annual turnover"),
    "APEX": ("Low", 1.10, "about 6 months of experience with this kind of application"),
    "PLEX": ("Low", 1.09, "about 6 months of experience with the web platform"),
    "LTEX": ("Nominal", 1.00, "about 1 year of JavaScript and tool experience"),
    "TOOL": ("Nominal", 1.00, "basic life-cycle tools, moderately integrated"),
    "SITE": ("High", 0.93, "same city, wideband electronic communication"),
    "SCED": ("Low", 1.14, "schedule compressed to 85% of nominal"),
}
SCED_PCT = 85
SUM_SF = round(sum(v for _, v, _ in SF.values()), 2)
E = B + 0.01 * SUM_SF
PROD_EM = math.prod(v for _, v, _ in EM.values())
PROD_EM_NS = PROD_EM / EM["SCED"][1]
PM = A * KLOC ** E * PROD_EM
PM_NS = A * KLOC ** E * PROD_EM_NS
TDEV_EXP = D + 0.2 * (E - B)
TDEV = C * PM_NS ** TDEV_EXP * SCED_PCT / 100
STAFF = PM / TDEV

# ====================================================================================== part 3: cost estimation
TOTAL_PM = 5
SPRINT = {"Analysis": 5, "Design": 15, "Implementation": 50, "Testing": 20, "Management": 10}   # % of sprint effort
N_SPRINTS, SPRINT_PCT = 4, 20                                                                   # 4 sprints x 20 %
RATE = {"Management": 90_000, "Analysis": 50_000, "Design": 50_000, "Implementation": 30_000, "Testing": 30_000}
DIRECT = {"Management": 10, "Analysis": 10}                                                      # % of project effort


def cost_rows() -> list[dict]:
    rows = []
    for act in RATE:
        direct = DIRECT.get(act, 0)
        in_sprints = N_SPRINTS * SPRINT_PCT * SPRINT[act] / 100          # % of project effort inside the 4 sprints
        pct = direct + in_sprints
        effort = TOTAL_PM * pct / 100
        rows.append(dict(act=act, direct=direct, in_sprints=in_sprints, pct=pct, effort=effort, rate=RATE[act],
                         cost=effort * RATE[act]))
    return rows


COST = cost_rows()
TOTAL_COST = sum(r["cost"] for r in COST)
assert abs(sum(r["pct"] for r in COST) - 100) < 1e-9 and TOTAL_COST == 230_000, (COST, TOTAL_COST)

# ===================================================================================== part 4: earned value
BAC, PV, EV, AC, MONTHS, ELAPSED = 1_200_000, 230_000, 200_000, 250_000, 12, 2
CV, SV = EV - AC, EV - PV
CPI, SPI = EV / AC, EV / PV
EAC = BAC / CPI
EST_TIME = MONTHS / SPI
ETC = EAC - AC
TCPI = (BAC - EV) / (BAC - AC)


def baht(x: float) -> str:
    return f"{x:,.0f}"


# ============================================================================================ drawing helpers
def write(page: pymupdf.Page, rect: pymupdf.Rect, text: str, size: float = 9.5, font: str = "sb", align: int = 0,
          color=INK, lineheight: float = 1.05, pad: float = 3) -> None:
    """Write text into rect, shrinking the font until it fits."""
    r = pymupdf.Rect(rect.x0 + pad, rect.y0 + 1, rect.x1 - pad, rect.y1 - 1)
    while size >= 5.5:
        if page.insert_textbox(r, text, fontname=font, fontsize=size, color=color, align=align,
                               lineheight=lineheight) >= 0:
            return
        size -= 0.25
    raise SystemExit(f"text does not fit {rect}: {text[:50]}…")


def cell(x0: float, y0: float, x1: float, y1: float) -> pymupdf.Rect:
    return pymupdf.Rect(x0, y0, x1, y1)


def dot_runs(page: pymupdf.Page, contains: str, min_len: int = 2, after_y: float = 0) -> list[pymupdf.Rect]:
    """Bounding boxes of the runs of dot characters ('…' or '.') on the first text line below `after_y` that
    contains `contains`."""
    for block in page.get_text("rawdict")["blocks"]:
        for line in block.get("lines", []):
            chars = [c for span in line["spans"] for c in span["chars"]]
            text = "".join(c["c"] for c in chars)
            if contains not in text or line["bbox"][1] < after_y:
                continue
            runs, cur = [], []
            for c in chars + [{"c": "x", "bbox": None}]:
                if c["c"] in "….":
                    cur.append(c)
                else:
                    if len(cur) >= min_len:
                        r = pymupdf.Rect(cur[0]["bbox"])
                        for d in cur[1:]:
                            r |= pymupdf.Rect(d["bbox"])
                        runs.append(r)
                    cur = []
            if runs:
                return runs
    raise SystemExit(f"dotted blank on the line containing {contains!r} not found")


def fill_dots(page: pymupdf.Page, contains: str, value: str, run: int = 0, size: float = 9.5, font: str = "sb",
              align: int = 0, grow: float = 0, after_y: float = 0) -> None:
    """Write value over the `run`-th dotted blank of the line containing `contains` (left-aligned by default)."""
    r = dot_runs(page, contains, after_y=after_y)[run]
    write(page, pymupdf.Rect(r.x0 - grow, r.y0 - 3, r.x1 + grow, r.y0 - 3 + size * 1.3), value, size=size, font=font,
          align=align, pad=1, lineheight=1.0)


def check(page: pymupdf.Page, box: pymupdf.Rect) -> None:
    """Draw a check mark over one of the form's Wingdings check-box glyphs."""
    x0, y0 = box.x0 + 2.2, box.y0 + 4.5
    s = page.new_shape()
    s.draw_polyline([(x0, y0 + 4.5), (x0 + 3, y0 + 7.5), (x0 + 8.5, y0 + 0.5)])
    s.finish(color=INK, width=1.6, lineCap=1, lineJoin=1)
    s.commit()


def checkboxes(page: pymupdf.Page) -> list[pymupdf.Rect]:
    """The Wingdings check-box glyphs on the page, in reading order (row by row, left to right)."""
    boxes = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                if "Wingdings" in span["font"]:
                    boxes.append(pymupdf.Rect(span["bbox"]))
    boxes.sort(key=lambda r: (round(r.y0), r.x0))
    return boxes


def numbered(items: list[str]) -> str:
    return "\n".join(f"{i}. {t}" for i, t in enumerate(items, 1))


# ================================================================================================ fill the form
def fp_answers(q: dict) -> dict[str, str]:
    kind, n_files = q["kind"], q["n_files"]
    t = TABLES[kind]
    files_word = "FTR" if q["ftrs"] is not None else "RET"
    row = next((lo, hi) for lo, hi in t["ftr"] if lo <= n_files <= hi)
    col = next((lo, hi) for lo, hi in t["det"] if lo <= q["n_det"] <= hi)
    band = lambda lo, hi: (f"{lo}" if lo == hi else f"{lo}–{hi}" if hi < 99 else f"> {lo - 1}")        # noqa: E731
    rating = (f"{q['rating']}  ({kind} with {n_files} {files_word}{'s' if n_files > 1 else ''} "
              f"[{files_word} band {band(*row)}] and {q['n_det']} DETs [DET band {band(*col)}] – slide 37 table)")
    if kind == "ILF":
        dets = f"{q['n_det']} DETs:\n" + numbered([q["dets"][0]] + [f"{d} (vaccine shot data)" for d in q["dets"][1:]])
    else:
        dets = f"{q['n_det']} DETs:\n" + numbered(q["dets"])
    if q["det_note"]:
        dets += "\n" + q["det_note"]
    if q["ftrs"] is not None:
        ftr = f"{n_files} FTR{'s' if n_files > 1 else ''}:\n" + numbered(q["ftrs"])
        ret = f"N/A – RETs are counted only for data functions (ILF, EIF), not for an {kind}."
    else:
        ftr = f"N/A – FTRs are counted only for transactions (EI, EO, EQ), not for an {kind}."
        ret = f"{n_files} RETs:\n" + numbered(q["rets"])
    return dict(which=q["why"], dets=dets, ftr=ftr, ret=ret, rating=rating,
                value=f"{q['value']}  ({kind}, {q['rating']} = {q['value']} function points)")


def fill_fp_page(page: pymupdf.Page, x0: float, rows: dict[str, tuple[float, float]], ans: dict[str, str]) -> None:
    sizes = {"which": 9.5, "dets": 9.5, "ftr": 9.5, "ret": 9.5, "rating": 9.5, "value": 10}
    for key, (y0, y1) in rows.items():
        write(page, cell(x0, y0, 504.9, y1), ans[key], size=sizes[key],
              font="sbb" if key == "value" else "sb")


def fill_function_points(doc: pymupdf.Document) -> None:
    a = {n: fp_answers(q) for n, q in FP.items()}
    fill_fp_page(doc[0], 262, {"which": (540.4, 583.5), "dets": (583.5, 775.8)}, a[1])
    write(doc[1], cell(262, 72, 504.9, 221.5), "(continuation of the DET cell – all 8 DETs are listed on page 1)",
          size=8, color=(0.4, 0.4, 0.4))
    fill_fp_page(doc[1], 262, {"ftr": (221.5, 307.2), "ret": (307.2, 392.9), "rating": (392.9, 414.8),
                               "value": (414.8, 436.6)}, a[1])
    fill_fp_page(doc[2], 257.1, {"which": (72, 115.1), "dets": (115.1, 243.4), "ftr": (243.4, 329.1),
                                 "ret": (329.1, 414.8), "rating": (414.8, 436.6), "value": (436.6, 458.5)}, a[2])
    fill_fp_page(doc[3], 253, {"which": (72, 115.1), "dets": (115.1, 477.7), "ftr": (477.7, 563.3),
                               "ret": (563.3, 649.1), "rating": (649.1, 670.9), "value": (670.9, 692.7)}, a[3])
    fill_fp_page(doc[4], 257.1, {"which": (199.8, 242.9), "dets": (242.9, 392.4), "ftr": (392.4, 478.1),
                                 "ret": (478.1, 563.8), "rating": (563.8, 585.7), "value": (585.7, 607.5)}, a[4])
    fill_fp_page(doc[5], 257.1, {"which": (157.2, 200.3), "dets": (200.3, 562.9), "ftr": (562.9, 648.6),
                                 "ret": (648.6, 734.3), "rating": (734.3, 756.1)}, a[5])
    fill_fp_page(doc[6], 257.1, {"value": (72, 93.9)}, a[5])

    # question 6: the unadjusted FP table (page 7)
    p = doc[6]
    labels = {"EI": "External Input (EI)", "EO": "External Output (EO)", "EQ": "External Inquiry (EQ)",
              "ILF": "Internal Logical File (ILF)", "EIF": "External Interface File (EIF)"}
    rows_y = {"EI": (377.8, 397.0), "EO": (397.0, 416.1), "EQ": (416.1, 435.3), "ILF": (435.3, 454.4),
              "EIF": (454.4, 473.6)}
    for kind, (y0, y1) in rows_y.items():
        # the three "……*w = ……" cells of the row are three separate text lines (one per cell)
        for col, (n, w, prod) in enumerate(zip(Q6_COUNTS[kind], Q6_WEIGHTS[kind], Q6_ROWS[kind])):
            x_cell = [(215.8, 296.8), (296.8, 382.4), (382.4, 467.9)][col]
            runs = dot_runs_in(p, x_cell, (y0, y1))
            over(p, runs[0], str(n))
            over(p, runs[1], str(prod))
        write(p, cell(467.9, y0, 504.9, y1), str(sum(Q6_ROWS[kind])), size=10, font="sbb", align=1)
    write(p, cell(467.9, 473.6, 504.9, 492.7), str(UFP), size=10.5, font="sbb", align=1)
    write(p, cell(90, 500, 505, 560),
          "Unadjusted FP = sum of (count × weight) = EI (3×3 + 1×4 + 0×6 = 13) + EO (1×4 = 4) + EQ (2×3 + 1×4 = 10) "
          "+ ILF (5×7 = 35) + EIF (1×5 = 5) = 13 + 4 + 10 + 35 + 5 = 67 function points (weights from slide 43).",
          size=9.5)


def dot_runs_in(page: pymupdf.Page, xr: tuple[float, float], yr: tuple[float, float],
                min_runs: int = 2) -> list[pymupdf.Rect]:
    """Dotted runs of the text line inside the given area (x-range, y-range)."""
    for block in page.get_text("rawdict")["blocks"]:
        for line in block.get("lines", []):
            chars = [c for span in line["spans"] for c in span["chars"]
                     if xr[0] <= c["bbox"][0] < xr[1] and yr[0] <= c["bbox"][1] < yr[1]]
            if not chars:
                continue
            runs, cur = [], []
            for c in chars + [{"c": "x", "bbox": None}]:
                if c["c"] in "….":
                    cur.append(c)
                else:
                    if len(cur) >= 2:
                        r = pymupdf.Rect(cur[0]["bbox"])
                        for d in cur[1:]:
                            r |= pymupdf.Rect(d["bbox"])
                        runs.append(r)
                    cur = []
            if len(runs) >= min_runs:
                return runs
    raise SystemExit(f"dotted blank at {xr}, {yr} not found")


def over(page: pymupdf.Page, r: pymupdf.Rect, value: str) -> None:
    write(page, pymupdf.Rect(r.x0 - 2, r.y0 - 3, r.x1 + 2, r.y1 + 1), value, size=10, font="sbb", align=1, pad=0)


def fmt(x: float, nd: int = 2) -> str:
    return f"{x:.{nd}f}"


def fill_cocomo(doc: pymupdf.Document) -> None:
    p8, p9 = doc[7], doc[8]
    fill_dots(p8, "average gearing factor is", f"{GEARING}", align=1, font="sbb", size=10)
    r = dot_runs_in(p8, (100, 270), (134, 156), min_runs=1)[0]          # the blank before "KLOC." is its own line
    write(p8, pymupdf.Rect(r.x0 - 12, r.y0 - 3, r.x1 + 12, r.y1 + 1), f"67 × {GEARING} / 1000 = {KLOC:.3f}", size=10,
          font="sbb", align=1, pad=1)
    write(p8, cell(90, 176, 505, 196),
          f"(QSM Function Point Languages Table v5.0: JavaScript gearing factor avg {GEARING}, median 53, "
          f"range 31–63 SLOC/FP; KLOC = FP × gearing factor / 1000, slide 47.)", size=8.5)
    # scale factors
    for name, (y0, y1) in {"PREC": (240.3, 259.3), "FLEX": (259.3, 278.6), "RESL": (278.6, 297.7),
                           "TEAM": (297.7, 316.8), "PMAT": (316.8, 335.9)}.items():
        rating, value, reason = SF[name]
        write(p8, cell(355.4, y0, 427.4, y1), rating, size=9.5, align=1)
        write(p8, cell(427.4, y0, 504.9, y1), fmt(value), size=9.5, align=1)
    write(p8, cell(427.4, 335.9, 504.9, 356.9), fmt(SUM_SF), size=10, font="sbb", align=1)
    write(p8, cell(91, 338, 350, 356),
          "sum of SF = 2.48 + 2.03 + 4.24 + 2.19 + 4.68 (values from slide 54, Table 10)", size=8)
    # effort multipliers
    em_rows = {"RELY": (438.3, 457.4), "DATA": (457.4, 476.6), "CPLX": (476.6, 495.7), "RUSE": (495.7, 514.9),
               "DOCU": (514.9, 534.0), "TIME": (553.0, 572.2), "STOR": (572.2, 591.3), "PVOL": (591.3, 610.5),
               "ACAP": (629.6, 648.8), "PCAP": (648.8, 667.9), "PCON": (667.9, 687.1), "APEX": (687.1, 706.2),
               "PLEX": (706.2, 725.3), "LTEX": (725.3, 744.5)}
    em_rows9 = {"TOOL": (72, 91.1), "SITE": (91.1, 110.3), "SCED": (110.3, 129.4)}
    for page, rows in ((p8, em_rows), (p9, em_rows9)):
        for name, (y0, y1) in rows.items():
            rating, value, reason = EM[name]
            write(page, cell(355.4, y0, 427.4, y1), rating, size=9.5, align=1)
            write(page, cell(427.4, y0, 504.9, y1), fmt(value), size=9.5, align=1)
    write(p9, cell(427.4, 129.4, 504.9, 150.4), fmt(PROD_EM, 4), size=10, font="sbb", align=1)
    write(p9, cell(91, 132, 390, 150),
          f"product of EM = 0.90 × 0.87 × 0.87 × 1.10 × 1.09 × 0.93 × 1.14 (all other EMs = 1.00) = {PROD_EM:.4f}",
          size=8)
    # 4-8: short form on the dotted lines
    fill_dots(p9, "4. E =", f"B + 0.01 × (sum of SF) = 0.91 + 0.01 × {SUM_SF} = {E:.4f}", size=9.5)
    fill_dots(p9, "5. Project effort PM =",
              f"A × Size^E × (product of EM) = 2.94 × {KLOC:.3f}^{E:.4f} × {PROD_EM:.4f} = {PM:.2f}", size=9)
    fill_dots(p9, "= …", f"2.94 × {KLOC:.3f}^{E:.4f} × {PROD_EM_NS:.4f} (EM product without SCED) = {PM_NS:.2f}",
              size=8.5, after_y=234)
    fill_dots(p9, "7. Calendar time to develop TDEV is",
              f"3.67 × {PM_NS:.2f}^{TDEV_EXP:.4f} × {SCED_PCT}/100 = {TDEV:.2f}", size=9)
    fill_dots(p9, "is …", f"PM / TDEV = {PM:.2f} / {TDEV:.2f} = {STAFF:.2f}, i.e. 2 persons (rounded up)", size=9.5,
              after_y=295)
    # full substitution below
    text = (
        f"Calculations (COCOMO II.2000 post-architecture model, slides 52, 66 and 67; A = 2.94, B = 0.91, "
        f"C = 3.67, D = 0.28; Size = {KLOC:.3f} KLOC from step 1):\n\n"
        f"4.  E = B + 0.01 × (sum of SF) = 0.91 + 0.01 × (2.48 + 2.03 + 4.24 + 2.19 + 4.68) = 0.91 + 0.01 × {SUM_SF} "
        f"= 0.91 + {0.01 * SUM_SF:.4f} = {E:.4f}\n\n"
        f"5.  PM = A × Size^E × (product of EM) = 2.94 × {KLOC:.3f}^{E:.4f} × (1.00 × 0.90 × 0.87 × 1.00 × 1.00 × 1.00 × 1.00 "
        f"× 0.87 × 1.00 × 1.00 × 1.00 × 1.10 × 1.09 × 1.00 × 1.00 × 0.93 × 1.14)\n"
        f"      = 2.94 × {KLOC ** E:.4f} × {PROD_EM:.4f} = {PM:.2f} person-months\n\n"
        f"6.  PM_NS = effort with a nominal schedule, i.e. the same product without the SCED multiplier (1.14):\n"
        f"      PM_NS = 2.94 × {KLOC:.3f}^{E:.4f} × ({PROD_EM:.4f} / 1.14) = 2.94 × {KLOC ** E:.4f} × "
        f"{PROD_EM_NS:.4f} = {PM_NS:.2f} person-months\n\n"
        f"7.  TDEV = [C × PM_NS^(D + 0.2 × (E − B))] × SCED% / 100\n"
        f"      = [3.67 × {PM_NS:.2f}^(0.28 + 0.2 × ({E:.4f} − 0.91))] × {SCED_PCT} / 100 "
        f"= [3.67 × {PM_NS:.2f}^{TDEV_EXP:.4f}] × 0.{SCED_PCT}\n"
        f"      = [3.67 × {PM_NS ** TDEV_EXP:.4f}] × 0.{SCED_PCT} = {C * PM_NS ** TDEV_EXP:.2f} × 0.{SCED_PCT} "
        f"= {TDEV:.2f} months (SCED rated Low = 85% of the nominal schedule)\n\n"
        f"8.  Staff size = PM / TDEV = {PM:.2f} person-months / {TDEV:.2f} months = {STAFF:.2f} persons, "
        f"i.e. about 1.5 full-time persons – in practice 2 persons (rounded up; with 2 persons the work takes "
        f"{PM / 2:.1f} months, within the {TDEV:.2f}-month schedule).")
    write(p9, cell(90, 335, 505, 578), text, size=9.5, lineheight=1.15)
    # why the scale factors and effort multipliers were rated as they were (steps 2 and 3)
    why = ["Rating rationale (steps 2 and 3) – a small JavaScript web application built by a small co-located team:"]
    why += [f"•  {k} {r} ({v:.2f}): {reason}" for k, (r, v, reason) in {**SF, **EM}.items()]
    write(p9, cell(90, 584, 505, 812), "\n".join(why), size=8, lineheight=1.12)


def fill_cost(doc: pymupdf.Document) -> None:
    p11 = doc[10]
    rows_y = {"Management": (157.7, 174.1), "Analysis": (174.1, 190.7), "Design": (190.7, 207.1),
              "Implementation": (207.1, 223.6), "Testing": (223.6, 240.0)}
    for r in COST:
        y0, y1 = rows_y[r["act"]]
        direct = f"{r['direct']}% + " if r["direct"] else ""
        write(p11, cell(176.2, y0, 254.8, y1),
              f"{direct}4×20%×{SPRINT[r['act']]}% = {r['pct']:g}%", size=7.5, align=1, pad=1)
        write(p11, cell(254.8, y0, 335.4, y1), f"{r['pct']:g}% × 5 = {r['effort']:g}", size=8, align=1, pad=1)
        write(p11, cell(423.8, y0, 504.9, y1), f"{r['effort']:g} × {baht(r['rate'])} = {baht(r['cost'])}", size=7,
              align=1, pad=1)
    write(p11, cell(423.8, 240.0, 504.9, 256.6), baht(TOTAL_COST), size=9.5, font="sbb", align=1)
    lines = [
        "Calculations (effort 5 person-months; management 10% and analysis 10% are project-level activities, the "
        "remaining 80% is spread over 4 sprints of 20% each, and inside every sprint the effort is split into "
        "analysis 5%, design 15%, implementation 50%, testing 20% and management 10%):",
        "",
        "% of project effort of an activity = its project-level % + the sum over the 4 sprints of (sprint % of project × "
        "activity % of sprint):",
    ]
    for r in COST:
        n = SPRINT[r["act"]]
        direct = f"{r['direct']}% + " if r["direct"] else ""
        lines.append(f"•  {r['act']}: {direct}4 × (20% × {n}%) = {direct}4 × {20 * n / 100:g}% = "
                     f"{direct}{r['in_sprints']:g}% = {r['pct']:g}%")
    lines.append("   Check: 18% + 14% + 12% + 40% + 16% = 100% of the project effort.")
    lines.append("")
    lines.append("Activity effort (person-months) = % of project effort × 5 PM; activity labor cost = activity effort "
                 "× average labor cost per person-month:")
    for r in COST:
        lines.append(f"•  {r['act']}: {r['pct']:g}% × 5 = {r['effort']:g} PM;  {r['effort']:g} × "
                     f"{baht(r['rate'])} = {baht(r['cost'])} THB")
    lines.append("   Check: 0.9 + 0.7 + 0.6 + 2.0 + 0.8 = 5 PM.")
    lines.append("")
    lines.append(f"Total project labor cost = 81,000 + 35,000 + 30,000 + 60,000 + 24,000 = {baht(TOTAL_COST)} THB "
                 f"(an average of {baht(TOTAL_COST / TOTAL_PM)} THB per person-month).")
    write(p11, cell(90, 268, 505, 700), "\n".join(lines), size=9.5, lineheight=1.15)


def fill_evm(doc: pymupdf.Document) -> None:
    p = doc[11]
    s = 9
    fill_dots(p, "Budget at completion (BAC) =", f"{baht(BAC)} baht (the original total budget of the project)",
              size=s)
    fill_dots(p, "Planned Value (PV) =", f"{baht(PV)} baht (the budget for the work scheduled in the first two "
                                         f"months)", size=s)
    fill_dots(p, "Earned Value (EV) =", f"{baht(EV)} baht (the budgeted value of the work actually finished)",
              size=s)
    fill_dots(p, "Actual Cost (AC) =", f"{baht(AC)} baht (the actual cost of the first two months)", size=s)
    fill_dots(p, "Cost Variance (CV) =", f"EV − AC = {baht(EV)} − {baht(AC)} = −{baht(-CV)} baht (negative: over "
                                         f"budget)", size=s)
    fill_dots(p, "Schedule Variance (SV) =", f"EV − PV = {baht(EV)} − {baht(PV)} = −{baht(-SV)} baht (negative: "
                                             f"behind schedule)", size=s)
    fill_dots(p, "Cost Performance Index (CPI) =", f"EV / AC = {baht(EV)} / {baht(AC)} = {CPI:.2f} (80%: 20% over "
                                                   f"budget)", size=s)
    fill_dots(p, "Schedule Performance Index (SPI) =", f"EV / PV = {baht(EV)} / {baht(PV)} = {SPI:.4f} (86.96%: "
                                                       f"13% behind schedule)", size=s)
    fill_dots(p, "Estimate at completion (EAC) =", f"BAC / CPI = {baht(BAC)} / {CPI:.2f} = {baht(EAC)} baht",
              size=s)
    fill_dots(p, "Estimated time to complete =", f"original time estimate / SPI = 12 months / {SPI:.4f} = "
                                                 f"{EST_TIME:.2f} months", size=s)
    fill_dots(p, "Estimated to complete (ETC) =", f"EAC − AC = {baht(EAC)} − {baht(AC)} = {baht(ETC)} baht",
              size=s)
    fill_dots(p, "(TCPI) =", f"(BAC − EV) / (BAC − AC) = ({baht(BAC)} − {baht(EV)}) / ({baht(BAC)} − {baht(AC)}) "
                             f"= {baht(BAC - EV)} / {baht(BAC - AC)} = {TCPI:.4f}", size=s)
    boxes = checkboxes(p)
    assert len(boxes) == 6, boxes
    check(p, boxes[2])        # over budget   (CPI < 1)
    check(p, boxes[5])        # behind schedule (SPI < 1)
    write(p, cell(441, 519, 508, 537), f"(CPI = {CPI:.2f} < 1)", size=8)
    write(p, cell(441, 540, 508, 558), f"(SPI = {SPI:.2f} < 1)", size=8)
    fill_dots(p, "completing the project would be",
              f"EAC = BAC / CPI = {baht(EAC)} baht ({baht(EAC - BAC)} baht or 25% more than the BAC)", size=s,
              after_y=575)
    fill_dots(p, "completing the project would be",
              f"12 / SPI = {EST_TIME:.2f} months (about {EST_TIME - MONTHS:.1f} months or 15% longer than planned)",
              size=s, after_y=620)
    fill_dots(p, "reasonable for completing the project? Why?",
              "Yes, still reasonable, but only with better cost efficiency:", size=s)
    # the two remaining dotted lines (21.2 pt apart) and the blank space under them
    r = dot_runs(p, "…", after_y=688)[0]
    write(p, pymupdf.Rect(90, r.y0 - 3, 506, r.y0 - 3 + 2 * 21.2 + 2),
          f"TCPI = {TCPI:.2f} > 1: the remaining {baht(BAC - EV)} baht of work must be done with the remaining "
          f"{baht(BAC - AC)} baht, so the\n"
          f"cost efficiency must rise from CPI {CPI:.2f} to {TCPI:.2f} (+{(TCPI - CPI) / CPI * 100:.0f}%). "
          f"TCPI − CPI = {TCPI - CPI:.2f} is within 0.5 × CPI = {0.5 * CPI:.2f}, so (slide 79) the BAC is reasonable.",
          size=8, lineheight=21.2 / 8, pad=1)
    write(p, cell(90, 732, 506, 800),
          f"(The required improvement is demanding but not overly optimistic by the rule of thumb; if the team keeps "
          f"CPI = {CPI:.2f}, the project would cost EAC = {baht(EAC)} baht instead of the {baht(BAC)}-baht budget.)",
          size=8, lineheight=1.2)


# ============================================================================================ solution markdown
def solution_markdown() -> str:
    out = ["# Exercise 3 – worked solution (generated by tools/fill_form.py)", "",
           "## Function points (chapter 7 slides 26–43)", ""]
    for n, q in FP.items():
        a = fp_answers(q)
        out += [f"### Question {n}: {q['kind']}, {q['rating']} = {q['value']} FP", "",
                f"- **Function:** {a['which']}", f"- **DETs:** {a['dets'].replace(chr(10), '  ')}",
                f"- **FTRs:** {a['ftr'].replace(chr(10), '  ')}", f"- **RETs:** {a['ret'].replace(chr(10), '  ')}",
                f"- **Rating:** {a['rating']}", f"- **Value:** {a['value']}", ""]
    out += ["### Question 6: unadjusted function points", "", "| Type | Low | Average | High | Total |",
            "|---|---|---|---|---|"]
    for k in Q6_COUNTS:
        n, w, pr = Q6_COUNTS[k], Q6_WEIGHTS[k], Q6_ROWS[k]
        out.append(f"| {k} | {n[0]}×{w[0]} = {pr[0]} | {n[1]}×{w[1]} = {pr[1]} | {n[2]}×{w[2]} = {pr[2]} | "
                   f"{sum(pr)} |")
    out += [f"| **Unadjusted FP** | | | | **{UFP}** |", "",
            "## COCOMO II post-architecture model (slides 47, 52–67)", "",
            f"1. JavaScript gearing factor (QSM table, average) = {GEARING} SLOC/FP; "
            f"KLOC = 67 × {GEARING} / 1000 = {KLOC:.3f} KLOC", "",
            "| Scale factor | Rating | Score | Reason |", "|---|---|---|---|"]
    out += [f"| {k} | {r} | {v:.2f} | {why} |" for k, (r, v, why) in SF.items()]
    out += [f"| **ΣSF** | | **{SUM_SF:.2f}** | |", "", "| Effort multiplier | Rating | Score | Reason |",
            "|---|---|---|---|"]
    out += [f"| {k} | {r} | {v:.2f} | {why} |" for k, (r, v, why) in EM.items()]
    out += [f"| **ΠEM** | | **{PROD_EM:.4f}** | (without SCED: {PROD_EM_NS:.4f}) |", "",
            f"4. E = 0.91 + 0.01 × {SUM_SF} = {E:.4f}",
            f"5. PM = 2.94 × {KLOC:.3f}^{E:.4f} × {PROD_EM:.4f} = {PM:.2f} person-months",
            f"6. PM_NS = 2.94 × {KLOC:.3f}^{E:.4f} × {PROD_EM_NS:.4f} = {PM_NS:.2f} person-months",
            f"7. TDEV = [3.67 × {PM_NS:.2f}^({TDEV_EXP:.4f})] × {SCED_PCT}/100 = {TDEV:.2f} months",
            f"8. Staff = {PM:.2f} / {TDEV:.2f} = {STAFF:.2f} ≈ 2 persons", "",
            "## Cost estimation", "",
            "| Activity | % of project effort | Effort (PM) | Rate (THB/PM) | Cost (THB) |", "|---|---|---|---|---|"]
    for r in COST:
        direct = f"{r['direct']}% + " if r["direct"] else ""
        out.append(f"| {r['act']} | {direct}4×20%×{SPRINT[r['act']]}% = {r['pct']:g}% | {r['effort']:g} | "
                   f"{baht(r['rate'])} | {baht(r['cost'])} |")
    out += [f"| **Total** | 100% | {TOTAL_PM} | | **{baht(TOTAL_COST)}** |", "",
            "## Earned value analysis (slides 73–79)", "",
            f"- BAC = {baht(BAC)}; PV = {baht(PV)}; EV = {baht(EV)}; AC = {baht(AC)} baht",
            f"- CV = EV − AC = {CV:,.0f}; SV = EV − PV = {SV:,.0f} baht",
            f"- CPI = {CPI:.2f}; SPI = {SPI:.4f}", f"- EAC = BAC / CPI = {baht(EAC)} baht",
            f"- Estimated time to complete = 12 / SPI = {EST_TIME:.2f} months",
            f"- ETC = EAC − AC = {baht(ETC)} baht", f"- TCPI (BAC) = (BAC − EV) / (BAC − AC) = {TCPI:.4f}",
            "1. Over budget (CPI < 1) and behind schedule (SPI < 1).",
            f"2. Cost at the current cost efficiency = EAC = {baht(EAC)} baht.",
            f"3. Time at the current schedule efficiency = {EST_TIME:.2f} months.",
            f"4. TCPI = {TCPI:.2f} > 1: the remaining work needs cost efficiency 1.05 instead of the current 0.80 "
            f"(+{(TCPI - CPI) / CPI * 100:.0f}%); TCPI − CPI = {TCPI - CPI:.2f} < 0.5 × CPI = {0.5 * CPI:.2f}, "
            f"so the original budget is still reasonable (slide 79 rule of thumb), though demanding.", ""]
    return "\n".join(out)


def main() -> None:
    doc = pymupdf.open(FORM)
    for page in doc:
        for name, path in FONTS.items():
            page.insert_font(fontname=name, fontfile=str(path))
    write(doc[0], cell(352, 66, 503, 86), STUDENT, size=10, font="sbb", align=1)
    fill_function_points(doc)
    fill_cocomo(doc)
    fill_cost(doc)
    fill_evm(doc)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.subset_fonts()
    doc.save(OUT, garbage=4, deflate=True)
    SOLUTION_MD.parent.mkdir(parents=True, exist_ok=True)
    SOLUTION_MD.write_text(solution_markdown(), encoding="utf-8")
    print(f"Wrote {OUT} and {SOLUTION_MD}")


if __name__ == "__main__":
    main()
