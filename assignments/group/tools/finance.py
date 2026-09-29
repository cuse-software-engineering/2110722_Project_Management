#!/usr/bin/env python3
"""Financial model of the CTRS project for the 2110722 Milestone 1 report — software-house view.

Business model (owner decision 2026-09-10): the four team members are engineers of one software house. CTRS is built
for La Loy under a pilot implementation agreement (Year 0), run for La Loy alone during a pilot year while it is
productized (Year 1), and then sold to other live-music restaurants as a subscription service (Years 2 to 5).
The restaurant's own benefits are NOT counted here; the software house's revenues are the pilot fee, subscriptions
and setup fees.  Every figure printed in Sections 2.7 and 3 of milestone1/part2-final-deliverables.md comes from
this script (tools/build_pm_report.py pastes the tables), so change an assumption here, not in the report.
"""
RATE = 0.10              # discount rate
YEARS = 5                # operating years after Year 0 (Year 1 = pilot year, Years 2..5 = expansion)

# --- Subscription plans (THB per shop per month, VAT excluded) ------------------------------------------
PLANS = [  # name, price, limits / contents
    ("Free", 0, "1 concert round a month; up to 20 tables; Release 1.0 core: round list, table map, hold, gateway payment "
                "through the shop's own merchant account, QR e-ticket, check-in, name lookup; 1 Manager and 1 Front Staff "
                "account; \"Powered by CTRS\" on the customer screens; self-service set-up; community support (LINE group)"),
    ("Standard", 690, "Unlimited rounds; up to 60 tables; every Release 1.0 feature: live booking view, exceptions and "
                      "degraded payment mode, audit trail, daily backup with Excel export; up to 5 staff accounts; support "
                      "by LINE within one business day"),
    ("Premium", 990, "Standard plus the Release 2.0 features: scheduled reminders, grace extension, waitlist, booking "
                     "transfer, reports and analytics; unlimited tables and staff accounts; concert-night priority support "
                     "(response within 2 hours)"),
]
SETUP_FEE = 2500         # one-time, every new paid subscription: zone map, packages, gateway and LINE OA set-up, 2 h training
PILOT_FEE = 150000       # pilot implementation fee paid by La Loy in Year 0 (30 % at LCA, 40 % at IOC, 30 % at go-live)
MIX_STANDARD = 0.5       # share of paying shops on Standard (the rest on Premium)
ARPU = MIX_STANDARD * 690 + (1 - MIX_STANDARD) * 990      # 840 THB a month per paying shop
CHURN = 0.10             # of the paying shops at the start of a year leave during the year

# --- Adoption plan (shops at year end; Year 1 = La Loy alone, free of charge as the pilot restaurant) ----------
PAYING_END = [0, 0, 15, 40, 80, 130]      # Year 0 .. Year 5
FREE_END = [0, 1, 20, 50, 90, 140]        # free-plan shops (cost, no revenue); Year 1 = La Loy on Premium free

# --- Development effort: hours per week per member, per phase (PM, SA/Architect, RS/UI/Implementer, QA/Test) ----
PHASES = [  # name, year, weeks, hours/week per member
    ("Inception (I1, I2)",                      0, 4, (8, 10, 8, 6)),
    ("Elaboration (E1, E2)",                    0, 8, (8, 12, 12, 8)),
    ("Construction Release 1.0 (C1, C2)",       0, 16, (8, 14, 16, 12)),
    ("Transition Release 1.0 (T1)",             0, 5, (8, 8, 10, 12)),
    ("Construction Release 2.0 (C3)",           0, 12, (6, 12, 14, 10)),
    ("Transition Release 2.0 (T2)",             0, 5, (6, 6, 8, 10)),
    ("Construction Release 2.1 productization (C4)", 1, 24, (2.5, 5, 7.5, 5)),
    ("Transition Release 2.1 (T3)",             1, 4, (2, 3, 5, 5)),
]
MEMBERS = [  # role bundle, member, THB per hour (the software house's internal cost rate)
    ("Project Manager, Change Control Manager", "Boonnisa T.", 350),
    ("System Analyst, Software Architect", "Sirapatr C.", 350),
    ("Requirements Specifier, User-Interface Designer, Designer / Implementer", "Chawanakorn S.", 300),
    ("Quality Assurance, Test Designer / Tester, Implementer (Construction)", "Watayut A.", 300),
]
CAPEX = [  # item, unit price, units (Year 0)
    ("Test devices: Android phone and 10-inch tablet for LIFF and check-in testing", 15000, 1),
]
DEV_NONLABOR = {  # year -> [(item, THB)]
    0: [("Development and staging hosting (12 months x 300 THB)", 3600),
        ("Production hosting for the pilot restaurant (Mar-Jul 2027, 5 months x 700 THB)", 3500),
        ("Domain name and TLS certificate (first year)", 1200),
        ("Payment gateway sandbox, LINE Developers, GitHub, Figma, PlantUML (free tiers)", 0)],
    1: [("Company registration, terms of service, privacy policy and data-processing agreement (legal)", 15000),
        ("Production hosting during the pilot year (12 months x 700 THB)", 8400),
        ("Support of the pilot restaurant (8 h/month x 300 THB)", 8 * 300 * 12)],
}
CONTINGENCY = 0.10       # of the development cost of Years 0 and 1 (CAPEX + labor + non-labor)

# --- Operating cost of the subscription service, Years 2..5 ----------------------------------------------
HOSTING_BASE = 700 * 12          # application server, database, backup, domain, monitoring
HOSTING_PER_SHOP = 50 * 12       # storage, messages and traffic per shop (free or paying)
SUPPORT_BASE_H = 16              # hours a month: second-line support, maintenance, LINE and gateway API changes
SUPPORT_PER_SHOP_H = 0.5         # hours a month per paying shop: first-line support and concert-night incidents
SUPPORT_RATE = 300
SALES_MARKETING = 2000 * 12      # LINE ads, venue visits, demo events
ONBOARDING_H = 2                 # hours per new paid subscription (setup fee delivery)


def fmt(x):
    return "-" if x == 0 else f"{x:,.0f}"


def avg(end, y):
    return (end[y - 1] + end[y]) / 2 if y > 0 else 0


def model(adoption=1.0, price=1.0, pilot_fee=PILOT_FEE, labor_free=False, stop_after_pilot=False):
    hours = [[w * h[i] for (_, _, w, h) in PHASES] for i in range(4)]
    labor_y = {0: 0, 1: 0}
    for k, (_, year, w, h) in enumerate(PHASES):
        labor_y[year] += sum(w * h[i] * MEMBERS[i][2] for i in range(4))
    if labor_free:
        labor_y = {0: 0, 1: 0}
    capex = sum(p * u for _, p, u in CAPEX)
    nonlabor = {y: sum(v for _, v in DEV_NONLABOR[y]) for y in (0, 1)}
    reserve = {0: round(CONTINGENCY * (capex + labor_y[0] + nonlabor[0])),
               1: round(CONTINGENCY * (labor_y[1] + DEV_NONLABOR[1][0][1]))}   # Year 1 reserve on the productization work
    paying_end = [round(x * adoption) for x in PAYING_END]
    free_end = [round(x * adoption) if y >= 2 else x for y, x in enumerate(FREE_END)]
    cost, revenue, detail = [], [], []
    for y in range(YEARS + 1):
        d = {}
        if y <= 1:
            d["capex"] = capex if y == 0 else 0
            d["labor"] = labor_y[y]; d["nonlabor"] = nonlabor[y]; d["reserve"] = reserve[y]
            d["hosting"] = d["support"] = d["sales"] = d["onboarding"] = 0
            new = 0
        else:
            if stop_after_pilot:
                d = dict.fromkeys(["capex", "labor", "nonlabor", "reserve", "hosting", "support", "sales", "onboarding"], 0)
                cost.append(0); revenue.append(0); detail.append(dict(d, new=0, pay_avg=0, free_avg=0, subs=0, setup=0, pilot=0)); continue
            d["capex"] = d["labor"] = d["nonlabor"] = d["reserve"] = 0
            pay_avg, free_avg = avg(paying_end, y), avg(free_end, y)
            churned = round(CHURN * paying_end[y - 1])
            new = paying_end[y] - paying_end[y - 1] + churned
            d["hosting"] = HOSTING_BASE + round(HOSTING_PER_SHOP * (pay_avg + free_avg))
            d["support"] = SUPPORT_BASE_H * 12 * SUPPORT_RATE + round(SUPPORT_PER_SHOP_H * 12 * SUPPORT_RATE * pay_avg)
            d["sales"] = SALES_MARKETING
            d["onboarding"] = ONBOARDING_H * SUPPORT_RATE * new
        pilot = pilot_fee if y == 0 else 0
        subs = round(avg(paying_end, y) * ARPU * price * 12) if y >= 2 else 0
        setup = round(new * SETUP_FEE * price) if y >= 2 else 0
        cost.append(sum(d.values())); revenue.append(pilot + subs + setup)
        detail.append(dict(d, new=new, pay_avg=avg(paying_end, y) if y >= 2 else 0, free_avg=avg(free_end, y) if y >= 2 else 0,
                           subs=subs, setup=setup, pilot=pilot))
    df = [1 / (1 + RATE) ** t for t in range(YEARS + 1)]
    net = [r - c for r, c in zip(revenue, cost)]
    npv = sum(n * d for n, d in zip(net, df))
    roi = (sum(revenue) - sum(cost)) / sum(cost)
    cum, payback = 0, None
    for t in range(YEARS + 1):
        prev, cum = cum, cum + net[t] * df[t]
        if payback is None and cum >= 0 and t > 0:
            payback = t - 1 + (-prev) / (net[t] * df[t])
    lo, hi = -0.99, 10.0
    f = lambda r: sum(n / (1 + r) ** t for t, n in enumerate(net))
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
    return dict(hours=hours, labor_y=labor_y, capex=capex, nonlabor=nonlabor, reserve=reserve, cost=cost, revenue=revenue,
                detail=detail, df=df, net=net, npv=npv, roi=roi, payback=payback, irr=(lo + hi) / 2,
                lcc=sum(c * d for c, d in zip(cost, df)), paying_end=paying_end, free_end=free_end)


def years(fn, m, total=True):
    row = " | ".join(fn(y) for y in range(YEARS + 1))
    return row + (f" | {sum(float(fn(y).replace(',', '')) if fn(y) != '-' else 0 for y in range(YEARS + 1)):,.0f} |" if total else " | |")


def tables():
    m = model()
    D = m["detail"]
    out = []
    HDR = "| Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Total |"
    SEP = "|---|---|---|---|---|---|---|---|"
    def line(label, vals, total=True, bold=False):
        cells = [fmt(v) for v in vals]
        tot = f" {sum(vals):,.0f} |" if total else " |"
        if bold:
            cells = [f"**{c}**" for c in cells]; tot = f" **{sum(vals):,.0f}** |" if total else " |"
        return f"| {label} | " + " | ".join(cells) + " |" + tot

    # plans
    out.append("<!-- plans -->")
    out.append("| Plan | Price (THB a month, VAT excluded) | Contents and limits |")
    out.append("|---|---|---|")
    for name, price, what in PLANS:
        out.append(f"| {name} | {price:,} | {what} |")
    out.append(f"| Setup (paid plans, one-time) | {SETUP_FEE:,} | zone map, packages and prices configured; LINE Official Account and payment gateway connected; 2-hour training of the Manager and Front Staff |")
    out.append(f"| Pilot implementation (La Loy, Year 0, one-time) | {PILOT_FEE:,} | custom build of Release 1.0 and 2.0 for the pilot restaurant, paid 30 % at LCA, 40 % at IOC and 30 % at go-live; Premium free of charge during the pilot year |")
    out.append("<!-- /plans -->")
    # adoption
    out.append("<!-- adoption -->")
    out.append("| Shops | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |")
    out.append("|---|---|---|---|---|---|---|")
    out.append("| Paying shops at year end (Standard + Premium) | " + " | ".join(fmt(x) for x in m["paying_end"]) + " |")
    out.append("| Free-plan shops at year end | " + " | ".join(("La Loy (pilot)" if y == 1 else fmt(x)) for y, x in enumerate(m["free_end"])) + " |")
    out.append("| New paid subscriptions during the year (incl. replacement of 10 % churn) | " + " | ".join(fmt(D[y]["new"]) for y in range(YEARS + 1)) + " |")
    out.append("| Average paying shops during the year | " + " | ".join(fmt(D[y]["pay_avg"]) for y in range(YEARS + 1)) + " |")
    out.append("<!-- /adoption -->")
    # effort
    out.append("<!-- effort -->")
    out.append("| Phase (iterations) | Year | Weeks | " + " | ".join(f"{r.split(',')[0]} ({n})" for r, n, _ in MEMBERS) + " | Hours |")
    out.append("|---|---|---|" + "---|" * 5)
    tot = [0] * 4
    for k, (name, year, w, h) in enumerate(PHASES):
        cells = [w * h[i] for i in range(4)]
        for i in range(4): tot[i] += cells[i]
        out.append(f"| {name} | {year} | {w} | " + " | ".join(f"{c:,.0f}" for c in cells) + f" | {sum(cells):,.0f} |")
    out.append(f"| **Total hours** | | **{sum(w for _, _, w, _ in PHASES)}** | " + " | ".join(f"**{t:,.0f}**" for t in tot) + f" | **{sum(tot):,.0f}** |")
    out.append("| Rate (THB/h) | | | " + " | ".join(f"{r:,}" for *_, r in MEMBERS) + " | |")
    out.append("| **Labor cost (THB)** | | | " + " | ".join(f"**{t * r:,.0f}**" for t, (*_, r) in zip(tot, MEMBERS)) + f" | **{m['labor_y'][0] + m['labor_y'][1]:,.0f}** |")
    out.append(f"| of which Year 0 (build for the pilot restaurant) | 0 | 50 | | | | | {m['labor_y'][0]:,.0f} |")
    out.append(f"| of which Year 1 (productization) | 1 | 28 | | | | | {m['labor_y'][1]:,.0f} |")
    out.append("<!-- /effort -->")
    # capex
    out.append("<!-- capex -->")
    out.append("| CAPEX | Unit price | Units | Year 0 | Years 1 to 5 | Total |")
    out.append("|---|---|---|---|---|---|")
    for item, p, u in CAPEX:
        out.append(f"| {item} | {p:,} | {u} | {p*u:,} | - | {p*u:,} |")
    out.append(f"| **Total CAPEX** | | | **{m['capex']:,}** | - | **{m['capex']:,}** |")
    out.append("<!-- /capex -->")
    # opex
    out.append("<!-- opex -->")
    out.append('<div class="compact" markdown="1">\n')
    out.append("| OPEX " + HDR)
    out.append(SEP)
    out.append(line("Development labor (Table 3.4)", [m['labor_y'].get(y, 0) for y in range(YEARS + 1)]))
    for y in (0, 1):
        for item, v in DEV_NONLABOR[y]:
            out.append(line(item, [v if yy == y else 0 for yy in range(YEARS + 1)]))
    out.append(line("Hosting of the service: base (700 THB/month) plus 50 THB/month per shop", [D[y]["hosting"] for y in range(YEARS + 1)]))
    out.append(line("Support and maintenance: 16 h/month base plus 0.5 h/month per paying shop, at 300 THB/h", [D[y]["support"] for y in range(YEARS + 1)]))
    out.append(line("Sales and marketing (2,000 THB/month)", [D[y]["sales"] for y in range(YEARS + 1)]))
    out.append(line("Onboarding of new paid subscriptions (2 h each)", [D[y]["onboarding"] for y in range(YEARS + 1)]))
    opex = [m['cost'][y] - (m['capex'] if y == 0 else 0) - m['reserve'].get(y, 0) for y in range(YEARS + 1)]
    out.append(line("**Total OPEX**", opex, bold=True))
    out.append("\n</div>")
    out.append("<!-- /opex -->")
    # total cost
    out.append("<!-- totalcost -->")
    out.append("| Cost | Details | Total (THB) |")
    out.append("|---|---|---|")
    out.append(f"| CAPEX | Test devices | {m['capex']:,} |")
    out.append(f"| OPEX, Year 0 build | Labor of the eight-iteration build, development and pilot hosting, domain | {opex[0]:,.0f} |")
    out.append(f"| Contingency reserve, Year 0 | 10 % of the Year 0 cost, for the risks of Table 2.24 | {m['reserve'][0]:,} |")
    out.append(f"| **Project budget, Year 0** | | **{m['cost'][0]:,.0f}** |")
    out.append(f"| OPEX, Year 1 pilot and productization | Labor of C4 and T3, company and legal set-up, hosting and support of the pilot restaurant | {opex[1]:,.0f} |")
    out.append(f"| Contingency reserve, Year 1 | 10 % of the productization work | {m['reserve'][1]:,} |")
    out.append(f"| **Project budget, Year 1** | | **{m['cost'][1]:,.0f}** |")
    out.append(f"| **Project budget, Years 0 and 1** | development, pilot and productization | **{m['cost'][0] + m['cost'][1]:,.0f}** |")
    out.append(f"| OPEX, Years 2 to 5 | Operation of the subscription service: hosting, support, sales, onboarding | {sum(m['cost'][2:]):,.0f} |")
    out.append(f"| **Total cost, Years 0 to 5** | | **{sum(m['cost']):,.0f}** |")
    out.append("<!-- /totalcost -->")
    # revenue
    out.append("<!-- revenue -->")
    out.append("| Revenue " + HDR)
    out.append(SEP)
    out.append(line("Pilot implementation fee (La Loy)", [D[y]["pilot"] for y in range(YEARS + 1)]))
    out.append(line(f"Subscriptions ({ARPU:,.0f} THB a month per paying shop on average, 50 % Standard, 50 % Premium)", [D[y]["subs"] for y in range(YEARS + 1)]))
    out.append(line(f"Setup fees ({SETUP_FEE:,} THB per new paid subscription)", [D[y]["setup"] for y in range(YEARS + 1)]))
    out.append(line("**Total revenue**", m["revenue"], bold=True))
    out.append("<!-- /revenue -->")
    # cba
    out.append("<!-- cba -->")
    out.append('<div class="compact landscape" markdown="1">\n')
    out.append("| Item (discount rate 10 %) " + HDR)
    out.append(SEP)
    out.append("| Discount factor | " + " | ".join(f"{d:.4f}" for d in m['df']) + " | |")
    cum = lambda xs: [sum(xs[:i+1]) for i in range(len(xs))]
    c, r, df = m['cost'], m['revenue'], m['df']
    dc = [x * d for x, d in zip(c, df)]; dr = [x * d for x, d in zip(r, df)]
    out.append("| **1. Costs** | | | | | | | |")
    out.append(line("1.1 CAPEX", [m['capex'] if y == 0 else 0 for y in range(YEARS + 1)]))
    out.append(line("1.2 OPEX", opex))
    out.append(line("1.3 Contingency reserve", [m['reserve'].get(y, 0) for y in range(YEARS + 1)]))
    out.append(line("Total costs", c))
    out.append(line("Total discounted costs", dc))
    out.append(line("Cumulative discounted costs", cum(dc), total=False))
    out.append("| **2. Revenues** | | | | | | | |")
    out.append(line("2.1 Pilot implementation fee", [D[y]["pilot"] for y in range(YEARS + 1)]))
    out.append(line("2.2 Subscriptions", [D[y]["subs"] for y in range(YEARS + 1)]))
    out.append(line("2.3 Setup fees", [D[y]["setup"] for y in range(YEARS + 1)]))
    out.append(line("Total revenues", r))
    out.append(line("Total discounted revenues", dr))
    out.append(line("Cumulative discounted revenues", cum(dr), total=False))
    out.append("| **3. Net cash flow** | | | | | | | |")
    net = m['net']; dn = [n * d for n, d in zip(net, df)]
    out.append(line("Net cash flow (revenues - costs)", net))
    out.append(line("Discounted net cash flow", dn))
    out.append(line("Cumulative discounted net cash flow", cum(dn), total=False))
    out.append("\n</div>")
    out.append("<!-- /cba -->")
    # results
    out.append("<!-- results -->")
    out.append("| Measure | Value | Meaning |")
    out.append("|---|---|---|")
    out.append(f"| Net present value (NPV, 10 %) | **{m['npv']:,.0f} THB** | present value of revenues minus costs over Years 0 to 5; positive, but small against the {m['cost'][0] + m['cost'][1]:,.0f} THB invested in Years 0 and 1 |")
    out.append(f"| Return on investment (ROI, undiscounted, Years 0 to 5) | **{m['roi']*100:.0f} %** | (total revenues - total costs) / total costs = ({sum(m['revenue']):,.0f} - {sum(m['cost']):,.0f}) / {sum(m['cost']):,.0f} |")
    pb = f"{m['payback']:.1f} years (during Year {int(m['payback'])+1})" if m['payback'] is not None else "beyond Year 5"
    out.append(f"| Discounted payback period | **{pb}** | cumulative discounted net cash flow turns positive |")
    out.append(f"| Internal rate of return (IRR) | **{m['irr']*100:.0f} %** | discount rate at which NPV = 0; just above the 10 % hurdle |")
    out.append(f"| Life-cycle cost (discounted, Years 0 to 5) | **{m['lcc']:,.0f} THB** | present value of all costs, development, pilot and operation |")
    out.append(f"| Break-even scale | **about {m['paying_end'][3]} paying shops** | the year in which subscriptions and setup fees first exceed the operating cost and pay off the investment is Year 3 to 4 at the base adoption |")
    out.append("<!-- /results -->")
    # sensitivity
    out.append("<!-- sensitivity -->")
    out.append("| Case | Budget Years 0 and 1 | Revenue Years 0 to 5 | NPV (10 %) | ROI | Discounted payback | IRR |")
    out.append("|---|---|---|---|---|---|---|")
    cases = [("Base case (adoption as planned, pilot fee 150,000 THB, labor at the software house's cost rates)", {}),
             ("Adoption 30 % higher (paying shops 20 / 52 / 104 / 169 at year end)", dict(adoption=1.3)),
             ("Adoption 30 % lower (paying shops 10 / 28 / 56 / 91)", dict(adoption=0.7)),
             ("Prices 20 % lower (Standard 552, Premium 792, setup 2,000)", dict(price=0.8)),
             ("No pilot implementation fee (La Loy as an unpaid design partner)", dict(pilot_fee=0)),
             ("Stop after the pilot year (expansion gate not passed): exposure of the software house", dict(stop_after_pilot=True)),
             ("Partners' cash view: the four partners draw no salary for this project in Years 0 and 1", dict(labor_free=True))]
    for label, kw in cases:
        s = model(**kw)
        pb = f"{s['payback']:.1f} years" if s['payback'] is not None else "beyond Year 5"
        irr = f"{s['irr']*100:.0f} %" if -0.9 < s['irr'] < 5 else ("above 500 %" if s['irr'] >= 5 else "n/a")
        out.append(f"| {label} | {s['cost'][0] + s['cost'][1]:,.0f} | {sum(s['revenue']):,.0f} | {s['npv']:,.0f} | {s['roi']*100:.0f} % | {pb} | {irr} |")
    out.append("<!-- /sensitivity -->")
    # budget (Section 2.7)
    out.append("<!-- budget -->")
    out.append("| Category | Basis | THB |")
    out.append("|---|---|---|")
    out.append(f"| CAPEX, Year 0 | Test devices (Table 3.5) | {m['capex']:,} |")
    out.append(f"| Development labor, Year 0 | {sum(sum(m['hours'][i][:6]) for i in range(4)):,.0f} hours of the four engineers at 300 to 350 THB/h, Release 1.0 and 2.0 for the pilot restaurant (Table 3.4) | {m['labor_y'][0]:,.0f} |")
    out.append(f"| Hosting and services, Year 0 | Development, staging and pilot hosting, domain (Table 3.6) | {m['nonlabor'][0]:,} |")
    out.append(f"| Contingency reserve, Year 0 | 10 % of the Year 0 cost, for the risks of Table 2.24 | {m['reserve'][0]:,} |")
    out.append(f"| **Budget, Year 0 (build)** | | **{m['cost'][0]:,.0f}** |")
    out.append(f"| Development labor, Year 1 | {sum(sum(m['hours'][i][6:]) for i in range(4)):,.0f} hours: multi-tenant productization, plans and billing (C4, T3) | {m['labor_y'][1]:,.0f} |")
    out.append(f"| Company, legal, hosting and support, Year 1 | Registration and legal documents, pilot hosting and support (Table 3.6) | {m['nonlabor'][1]:,} |")
    out.append(f"| Contingency reserve, Year 1 | 10 % of the productization work | {m['reserve'][1]:,} |")
    out.append(f"| **Budget, Year 1 (pilot and productization)** | | **{m['cost'][1]:,.0f}** |")
    out.append(f"| **Project budget, Years 0 and 1** | | **{m['cost'][0] + m['cost'][1]:,.0f}** |")
    out.append(f"| Revenue inside the project | Pilot implementation fee paid by La Loy in Year 0 | {PILOT_FEE:,} |")
    out.append(f"| **Net investment of the software house** | budget less the pilot fee | **{m['cost'][0] + m['cost'][1] - PILOT_FEE:,.0f}** |")
    out.append("<!-- /budget -->")
    return "\n".join(out), m


if __name__ == "__main__":
    text, m = tables()
    print(text)
    print(f"\ncost {[round(c) for c in m['cost']]}\nrevenue {m['revenue']}\nnet {[round(n) for n in m['net']]}\n"
          f"NPV {m['npv']:,.0f}; ROI {m['roi']*100:.1f}%; payback {m['payback']}; IRR {m['irr']*100:.1f}%; LCC {m['lcc']:,.0f}; ARPU {ARPU}")
