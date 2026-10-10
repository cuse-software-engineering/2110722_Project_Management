#!/usr/bin/env python3
"""Fill the lecturer's Exercise 2 answer form (critical path method) and write the submission PDF.

The form (problem/exercise2_1_69_6aae126231e5a.pdf) is kept as it is: the answers are written into its
answer boxes, dotted blanks and check boxes with PyMuPDF, and the PDM network diagram of question 1 is
drawn as vector graphics in the blank area below the question, in the node layout of slide 33 of
chapter 6 (ES TS EF above the box, act=dur inside, LS FS LF below; critical path in red).

The schedule numbers (forward pass, backward pass, slacks, paths) are computed here from the activity
table, so the diagram and the written answers cannot disagree; the worked solution is also written to
workspace/solution.md for review.

Usage:  python3 tools/fill_form.py            (from assignments/individual/exercises/exercise_2/)
Output: report/watayut_6970267821.pdf
"""
import pathlib

import pymupdf

EXERCISE = pathlib.Path(__file__).resolve().parent.parent
FORM = EXERCISE / "problem" / "exercise2_1_69_6aae126231e5a.pdf"
OUT = EXERCISE / "report" / "watayut_6970267821.pdf"
SOLUTION_MD = EXERCISE / "workspace" / "solution.md"
FONT_DIR = EXERCISE.parents[5] / "resources" / "fonts" / "20180808-TH-Sarabun-PSK"   # 2110628 repository
FONTS = {"sb": FONT_DIR / "THSarabun.ttf", "sbb": FONT_DIR / "THSarabun Bold.ttf"}

STUDENT = "Watayut Aiamanan  6970267821"
INK = (0.05, 0.15, 0.55)          # answers in dark blue, so they stand apart from the printed form
RED = (0.85, 0.1, 0.1)

# ----------------------------------------------------------------------------------------------- schedule
ACTIVITIES = {  # activity -> (predecessors, duration in days), from the exercise table
    "A": ([], 2), "B": (["A"], 2), "C": (["A"], 3), "D": (["A"], 4), "E": (["B"], 2), "F": (["C"], 3),
    "G": (["D"], 6), "H": (["E", "F"], 2), "I": (["E", "F"], 5), "J": (["G", "I"], 1), "K": (["H", "J"], 2),
}


def schedule() -> tuple[dict[str, dict[str, int]], list[tuple[list[str], int]], int]:
    """Forward pass, backward pass and slacks (chapter 6 slides 31-32), and every path from A to K."""
    succ = {a: [b for b, (p, _) in ACTIVITIES.items() if a in p] for a in ACTIVITIES}
    v = {a: {"dur": d} for a, (_, d) in ACTIVITIES.items()}
    for a, (pred, d) in ACTIVITIES.items():                       # forward pass
        v[a]["ES"] = max((v[p]["EF"] for p in pred), default=0)
        v[a]["EF"] = v[a]["ES"] + d
    finish = max(x["EF"] for x in v.values())
    for a in reversed(list(ACTIVITIES)):                          # backward pass
        v[a]["LF"] = min((v[s]["LS"] for s in succ[a]), default=finish)
        v[a]["LS"] = v[a]["LF"] - v[a]["dur"]
    for a in ACTIVITIES:
        v[a]["TS"] = v[a]["LS"] - v[a]["ES"]
        v[a]["FS"] = min((v[s]["ES"] for s in succ[a]), default=finish) - v[a]["EF"]

    def walk(a: str, acc: list[str]):
        acc = acc + [a]
        if not succ[a]:
            yield acc
        for s in succ[a]:
            yield from walk(s, acc)

    paths = [(p, sum(ACTIVITIES[x][1] for x in p)) for p in walk("A", [])]
    return v, paths, finish


V, PATHS, FINISH = schedule()
CRITICAL = [p for p, length in PATHS if length == FINISH]
assert CRITICAL == [["A", "C", "F", "I", "J", "K"]] and FINISH == 16, (CRITICAL, FINISH)
ON_CRITICAL = set(CRITICAL[0])


def fmt_path(p: list[str]) -> str:
    return "-".join(p)


def fmt_sum(p: list[str]) -> str:
    return "+".join(str(ACTIVITIES[x][1]) for x in p)


# ------------------------------------------------------------------------------------------------ answers
def answers() -> dict:
    fs = {a: x["FS"] for a, x in V.items() if x["FS"] > 0}
    ts = {a: x["TS"] for a, x in V.items() if x["TS"] > 0}
    crit = ", ".join(CRITICAL[0])
    join = lambda d: ", ".join(f"{a} = {n}" for a, n in d.items())          # noqa: E731
    return {
        "paths": [f"Path {i}:  {fmt_path(p):<14} length = {fmt_sum(p)} = {n} days"
                  + ("   (longest)" if n == FINISH else "") for i, (p, n) in enumerate(PATHS, 1)],
        "critical": f"{fmt_path(CRITICAL[0])} (Path 4) – the longest path through the network diagram; "
                    f"every activity on it has TS = FS = 0.",
        "critical_days": str(FINISH),
        "shortest_days": str(FINISH),
        "q5": f"E, G and H – the activities with free slack FS > 0 ({join(fs)} days); every other activity has "
              f"FS = 0.",
        "q5_why": f"FS = (min ES of successors) – EF: E may finish as late as day 8 (H and I also wait for F), G day 13 "
                  f"(J waits for I), H day 14 (K waits for J).",
        "q6": f"B, D, E, G and H – the activities with total slack TS > 0 ({join(ts)} days).",
        "q6_why": f"TS = LS – ES: a delay within the TS leaves the project finish date (day {FINISH}) unchanged; "
                  f"{crit} are critical (TS = 0).",
        "q7_choice": 0, "q7_days": "1",
        "q7": f"B has ES = {V['B']['ES']}, LS = {V['B']['LS']}, TS = {V['B']['TS']} days (day numbers on the same "
              f"scale as ES/LS: B normally starts on day 2). Starting on day 5 delays B by 3 days, 1 day more than its "
              f"total slack: B 5–7, E 7–9, I 9–14, J 14–15, K 15–17. The project finishes on day 17 instead of "
              f"{FINISH}, at least 1 day late (A-B-E-I-J-K becomes the critical path).",
        "q8_choice": 1,
        "q8": f"H has ES = {V['H']['ES']}, LS = {V['H']['LS']}, TS = {V['H']['TS']} days (FS = {V['H']['FS']}). "
              f"Starting on day 10 delays H by 2 days, within its total slack: H finishes on day 12, still before the "
              f"early start of K on day 14 (K must also wait for J, EF = 14), so K and the project finish date "
              f"(day {FINISH}) are unchanged.",
        "q9_choice": 2,
        "q9": f"D has ES = {V['D']['ES']}, LS = {V['D']['LS']}, TS = {V['D']['TS']}, FS = {V['D']['FS']}. Starting "
              f"on day 3 delays D by 1 day: D finishes on day 7, so the early start of G moves from day 6 to 7 – G is "
              f"affected (G 7–13, its slack is used up). J waits for G (EF 13) and I (EF 13), so its early start "
              f"stays day 13: J and the project finish date (day {FINISH}) are not affected.",
    }


# ------------------------------------------------------------------------------------------------- drawing
def write(page: pymupdf.Page, rect: pymupdf.Rect, text: str, size: float = 13, font: str = "sb",
          align: int = 0, color=INK, lineheight: float = 1.0) -> None:
    """Write text into rect, shrinking the font until it fits (TH Sarabun is small for its point size)."""
    r = pymupdf.Rect(rect.x0 + 3, rect.y0 + 0.5, rect.x1 - 3, rect.y1 - 0.5)
    while size >= 8:
        if page.insert_textbox(r, text, fontname=font, fontsize=size, color=color, align=align,
                               lineheight=lineheight) >= 0:
            return
        size -= 0.5
    raise SystemExit(f"text does not fit {rect}: {text[:40]}…")


def dots_rect(page: pymupdf.Page, after: str) -> pymupdf.Rect:
    """Bounding box of the dotted blank ('……') that follows the text `after` on the page."""
    for block in page.get_text("rawdict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                text = "".join(c["c"] for c in span["chars"])
                if after in text and "…" in text:
                    dots = [c for c in span["chars"] if c["c"] == "…"]
                    r = pymupdf.Rect(dots[0]["bbox"])
                    for c in dots[1:]:
                        r |= pymupdf.Rect(c["bbox"])
                    return r
    raise SystemExit(f"dotted blank after {after!r} not found")


def fill_blank(page: pymupdf.Page, after: str, value: str) -> None:
    r = dots_rect(page, after)
    write(page, pymupdf.Rect(r.x0 - 6, r.y0 - 5, r.x1 + 6, r.y1 + 5), value, size=15, font="sbb", align=1)


def check(page: pymupdf.Page, box: pymupdf.Rect) -> None:
    """Draw a check mark over one of the form's Wingdings check-box glyphs."""
    x0, y0 = box.x0 + 2.2, box.y0 + 4.5
    s = page.new_shape()
    s.draw_polyline([(x0, y0 + 4.5), (x0 + 3, y0 + 7.5), (x0 + 8.5, y0 + 0.5)])
    s.finish(color=INK, width=1.6, lineCap=1, lineJoin=1)
    s.commit()


def checkboxes(page: pymupdf.Page, y_after: float, n: int) -> list[pymupdf.Rect]:
    """The n Wingdings check-box glyphs below y_after, top to bottom."""
    boxes = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                if "Wingdings" in span["font"] and span["bbox"][1] > y_after:
                    boxes.append(pymupdf.Rect(span["bbox"]))
    boxes.sort(key=lambda r: r.y0)
    assert len(boxes) >= n, boxes
    return boxes[:n]


def draw_network(page: pymupdf.Page) -> None:
    """PDM diagram with the slide-33 node layout, in the blank area below question 1 (y 530-800)."""
    col = [84, 150, 216, 282, 352, 420, 488]                     # x centres: Start, A, BCD, EFG, HI, J, K
    row = {"top": 612, "mid": 688, "bot": 764}                   # y centres of the three branches
    pos = {"Start": (col[0], row["mid"]), "A": (col[1], row["mid"]),
           "B": (col[2], row["top"]), "C": (col[2], row["mid"]), "D": (col[2], row["bot"]),
           "E": (col[3], row["top"]), "F": (col[3], row["mid"]), "G": (col[3], row["bot"]),
           "H": (col[4], row["top"]), "I": (col[4], row["mid"]), "J": (col[5], row["mid"]), "K": (col[6], row["mid"])}
    W, H = 40, 28                                                # box size
    small, label = 9.5, 11                                       # font sizes: value labels, box text

    def box(name: str) -> pymupdf.Rect:
        x, y = pos[name]
        return pymupdf.Rect(x - W / 2, y - H / 2, x + W / 2, y + H / 2)

    def put(x: float, y: float, text: str, size: float, align: int = 1, font: str = "sb", color=(0, 0, 0)):
        """Text anchored at x: left-aligned from x (0), centred on x (1) or right-aligned to x (2)."""
        x0, x1 = {0: (x, x + 60), 1: (x - 40, x + 40), 2: (x - 60, x)}[align]
        if page.insert_textbox(pymupdf.Rect(x0, y, x1, y + size * 1.5), text, fontname=font,
                               fontsize=size, align=align, color=color) < 0:
            raise SystemExit(f"label {text!r} does not fit")

    shape = page.new_shape()
    # arrows (drawn before the boxes so the boxes sit on top)
    for a, (pred, _) in ACTIVITIES.items():
        for p in pred or ["Start"]:
            crit = p in ON_CRITICAL and a in ON_CRITICAL
            src, dst = box(p), box(a)
            x0, y0, x1, y1 = src.x1, (src.y0 + src.y1) / 2, dst.x0, (dst.y0 + dst.y1) / 2
            if p == "H":                                          # H -> K: aim at the top of K's left edge
                y1 = dst.y0 + 9
            if p == "G":                                          # G -> J: aim at the bottom of J's left edge
                y1 = dst.y1 - 9
            shape.draw_line((x0, y0), (x1, y1))
            shape.finish(color=RED if crit else (0, 0, 0), width=1.6 if crit else 1)
            # arrow head
            import math
            ang = math.atan2(y1 - y0, x1 - x0)
            tip = pymupdf.Point(x1, y1)
            left = pymupdf.Point(x1 - 7 * math.cos(ang - 0.4), y1 - 7 * math.sin(ang - 0.4))
            right = pymupdf.Point(x1 - 7 * math.cos(ang + 0.4), y1 - 7 * math.sin(ang + 0.4))
            shape.draw_polyline([left, tip, right, left])
            shape.finish(color=RED if crit else (0, 0, 0), fill=RED if crit else (0, 0, 0), width=0.5)
    # boxes
    for name in pos:
        r = box(name)
        crit = name in ON_CRITICAL
        shape.draw_rect(r)
        shape.finish(color=RED if crit else (0, 0, 0), fill=(0.96, 0.85, 0.75), width=1.8 if crit else 1)
    shape.commit()
    # texts
    for name in pos:
        r = box(name)
        cx = (r.x0 + r.x1) / 2
        if name == "Start":
            put(cx, r.y0 + 7, "Start", label, font="sbb")
            for y in (r.y0 - small - 3, r.y1 + 1):
                put(r.x0 + 2, y, "0", small, align=0)
                put(r.x1 - 2, y, "0", small, align=2)
            continue
        v = V[name]
        put(cx, r.y0 + 7, f"{name} = {v['dur']}", label, font="sbb")
        ya, yb = r.y0 - small - 3, r.y1 + 1                      # above / below label rows
        put(r.x0 + 2, ya, str(v["ES"]), small, align=0)
        put(cx, ya - 1, f"TS={v['TS']}", small - 1, color=INK)
        put(r.x1 - 2, ya, str(v["EF"]), small, align=2)
        put(r.x0 + 2, yb, str(v["LS"]), small, align=0)
        put(cx, yb + 1, f"FS={v['FS']}", small - 1, color=INK)
        put(r.x1 - 2, yb, str(v["LF"]), small, align=2)
    # legend (slide 33 style) at the right of the band above the diagram, the formulas used at its left
    lx, ly = 478, 540
    write(page, pymupdf.Rect(318, 526, lx - 8, 586),
          "Legend: ES = early start, EF = early finish, LS = late start, LF = late finish, "
          "TS = total slack, FS = free slack (days). Red = critical path.", size=10.5, color=(0, 0, 0))
    r = pymupdf.Rect(lx, ly + 12, lx + 46, ly + 36)
    s = page.new_shape()
    s.draw_rect(r)
    s.finish(color=(0, 0, 0), fill=(0.96, 0.85, 0.75), width=1)
    s.commit()
    put(r.x0, ly, "ES", 9, align=0)
    put((r.x0 + r.x1) / 2, ly, "TS", 9)
    put(r.x1, ly, "EF", 9, align=2)
    put((r.x0 + r.x1) / 2, r.y0 + 5, "act=dur", 10)
    put(r.x0, r.y1 + 1, "LS", 9, align=0)
    put((r.x0 + r.x1) / 2, r.y1 + 1, "FS", 9)
    put(r.x1, r.y1 + 1, "LF", 9, align=2)
    write(page, pymupdf.Rect(86, 526, 312, 586),
          f"Forward pass: ES = max EF of predecessors, EF = ES + dur. Backward pass: LF = min LS of "
          f"successors, LS = LF – dur. TS = LS – ES; FS = (min ES of successors) – EF. Critical path "
          f"{fmt_path(CRITICAL[0])}, project duration {FINISH} days.", size=10.5)


# ------------------------------------------------------------------------------------------------- output
def solution_markdown() -> str:
    rows = "\n".join(f"| {a} | {', '.join(ACTIVITIES[a][0]) or '-'} | {v['dur']} | {v['ES']} | {v['EF']} | {v['LS']} "
                     f"| {v['LF']} | {v['TS']} | {v['FS']} |" for a, v in V.items())
    paths = "\n".join(f"| {i} | {fmt_path(p)} | {fmt_sum(p)} = {n} |" + (" **critical** |" if n == FINISH else " |")
                      for i, (p, n) in enumerate(PATHS, 1))
    ans = answers()
    return f"""# Exercise 2 – worked solution (generated by tools/fill_form.py)

Forward pass: ES = max EF of predecessors, EF = ES + dur. Backward pass: LF = min LS of successors, LS = LF − dur.
TS = LS − ES, FS = (min ES of successors) − EF. Project duration {FINISH} days.

| Activity | Pred. | Dur | ES | EF | LS | LF | TS | FS |
|---|---|---|---|---|---|---|---|---|
{rows}

| Path | Activities | Length (days) | |
|---|---|---|---|
{paths}

3. Critical path: {ans['critical']} It takes {ans['critical_days']} days.
4. Shortest possible time: {ans['shortest_days']} days.
5. {ans['q5']} {ans['q5_why']}
6. {ans['q6']} {ans['q6_why']}
7. Choice {ans['q7_choice'] + 1} (delayed for at least {ans['q7_days']} day). {ans['q7']}
8. Choice {ans['q8_choice'] + 1} (not affected). {ans['q8']}
9. Choice {ans['q9_choice'] + 1} (affects G but not J). {ans['q9']}
"""


def main() -> None:
    ans = answers()
    doc = pymupdf.open(FORM)
    for page in doc:
        for name, path in FONTS.items():
            page.insert_font(fontname=name, fontfile=str(path))
        write(page, pymupdf.Rect(240, 31, 470, 53), STUDENT, size=13, font="sbb", align=1)
    p1, p2, p3 = doc[0], doc[1], doc[2]

    draw_network(p1)

    write(p2, pymupdf.Rect(90, 93.5, 505, 198.3), "\n".join(ans["paths"]), size=14, lineheight=1.15)
    write(p2, pymupdf.Rect(90, 241.2, 505, 262.2), ans["critical"], size=13)
    fill_blank(p2, "It takes", ans["critical_days"])
    fill_blank(p2, "shortest possible time", ans["shortest_days"])
    write(p2, pymupdf.Rect(90, 389.0, 505, 410.0), ans["q5"], size=13)
    write(p2, pymupdf.Rect(90, 411, 505, 429), ans["q5_why"], size=11)
    write(p2, pymupdf.Rect(90, 473.8, 505, 494.8), ans["q6"], size=13)
    write(p2, pymupdf.Rect(90, 496, 505, 514), ans["q6_why"], size=11)
    q7 = checkboxes(p2, 530, 2)
    check(p2, q7[ans["q7_choice"]])
    fill_blank(p2, "at least", ans["q7_days"])
    write(p2, pymupdf.Rect(90, 621.6, 505, 663.5), ans["q7"], size=12.5, lineheight=0.9)

    q8 = checkboxes(p3, 90, 2)
    check(p3, q8[ans["q8_choice"]])
    write(p3, pymupdf.Rect(90, 177.3, 505, 219.3), ans["q8"], size=12.5, lineheight=0.9)
    q9 = checkboxes(p3, 280, 4)
    check(p3, q9[ans["q9_choice"]])
    write(p3, pymupdf.Rect(90, 408.9, 505, 450.9), ans["q9"], size=12.5, lineheight=0.9)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.subset_fonts()
    doc.save(OUT, garbage=4, deflate=True)
    SOLUTION_MD.write_text(solution_markdown(), encoding="utf-8")
    print(f"Wrote {OUT} and {SOLUTION_MD}")


if __name__ == "__main__":
    main()
