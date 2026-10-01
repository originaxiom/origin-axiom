#!/usr/bin/env python3
"""Reader of the sealed run.  usage: read_mass.py population | control     (writes ../mass_<which>_summary.json)"""
import sys, json, re, pathlib, collections
from fractions import Fraction
HERE = pathlib.Path(__file__).resolve().parent
which = sys.argv[1]
pat = re.compile(r"^mass_(frame|free)_\d\d\.json$") if which == "population" else re.compile(r"^mass_control_.*\.json$")
files = sorted(f for f in HERE.iterdir() if pat.match(f.name))
T = collections.Counter(); bad = collections.defaultdict(list); reach = collections.Counter(); table = []
for f in files:
    rec = json.load(open(f)); tag = "%s level %d" % (rec["state"], rec["k"]); T["levels"] += 1; T["levels_" + rec["mode"]] += 1
    for t, c in rec.get("reachable_types_per_background", {}).items(): reach[t] += c
    for k, v in rec.get("skipped", {}).items(): T["skipped: " + k] += v
    T["backgrounds"] += rec.get("backgrounds", 0)
    lev = collections.Counter()
    for c in rec["cases"]:
        T["cases"] += 1; T["cases_" + rec["mode"]] += 1
        if "error" in c: T["not_followed"] += 1; bad["not_followed"].append((tag, c["l"], c["eta"], c["A1"], c["error"])); continue
        T["tested"] += 1
        if c["agree"]: T["agree"] += 1
        else: bad["Q1"].append((tag, c["l"], c["eta"], c["A1"], c["predicted"], c["computed"]))
        s = float(c["s_l"]) - float(c["s_eta"]); irr = abs(float(c["s_l"]) * 60 - round(float(c["s_l"]) * 60)) > 1e-9 or abs(float(c["s_eta"]) * 60 - round(float(c["s_eta"]) * 60)) > 1e-9
        T["cases_with_a_slope_outside_(1/60)Z"] += irr
        if rec["mode"] == "frame":
            a = [float(x) for x in c["a"]]; b = [float(x) for x in c["b"]]; p = [float(x) for x in c["predicted"]]; Y = s
            z = lambda x: abs(x) < 1e-12
            plus = z(a[0]) and z(a[3]); minus = z(a[1]) and z(a[2])
            if not (plus or minus): bad["Q2"].append((tag, c["l"], c["eta"], c["A1"], "neither firing pattern", a)); continue
            if plus: want11, want02 = -Y * Y * a[1] * a[2], Y * Y * b[1] * b[2]; okY = abs(b[0] - Y) < 1e-9 and abs(b[3] - Y) < 1e-9
            else: want11, want02 = -Y * Y * a[0] * a[3], Y * Y * b[0] * b[3]; okY = abs(b[1] - Y) < 1e-9 and abs(b[2] - Y) < 1e-9
            ok = z(p[0]) and okY and abs(p[2] - want11) < 1e-9 * max(1, abs(want11)) and abs(p[1] - want02) < 1e-9 * max(1, abs(want02))
            T["frame_tested"] += 1; T["frame_structure_ok"] += ok
            if not ok: bad["Q2"].append((tag, c["l"], c["eta"], c["A1"], p, want11, want02))
            T["frame_mass_term_nonzero"] += not z(want11)
            cl = lambda x: 0.0 if abs(x) < 1e-12 else x
            for typ, sign in c["uses"]: lev[(typ, "Y^2 = %.6g" % cl(Y * Y), "e1e2 coefficient = %.6g" % cl(want11), "e2^2 coefficient = %.6g" % cl(want02))] += 1
    if lev: table.append(dict(level=tag, couplings={" | ".join(k): v for k, v in sorted(lev.items())}))
both = sum(c for t, c in reach.items() if "up" in t.split(",") and ("down" in t.split(",") or "lepton" in t.split(",")))
pred = dict(
    Q1=dict(statement="every case followed: the quadratic form of the bidoublet's torsion is the predicted one, to 1e-6", holds=not bad["Q1"] and T["tested"] > 0, tested=T["tested"], failures=len(bad["Q1"])),
    Q2=dict(statement="every frame case: no e1^2 term; the e1 e2 coefficient is -Y^2 times the product of the two unmatched differences to l; the e2^2 coefficient is Y^2 times the product of the two other differences to eta", holds=not bad["Q2"] and T["frame_tested"] > 0, tested=T["frame_tested"], failures=len(bad["Q2"])),
    Q3=dict(statement="some background has an up-type and a down-type (down or lepton) coupling both reachable", holds=both > 0, backgrounds=both),
    Q4=dict(statement="some case with a slope outside (1/60)Z agrees", holds=T["cases_with_a_slope_outside_(1/60)Z"] > 0 and not bad["Q1"], cases=T["cases_with_a_slope_outside_(1/60)Z"]))
out = dict(which=which, files=[f.name for f in files], totals=dict(T), reachable_types_per_background=dict(reach), predictions=pred, failures={k: v[:40] for k, v in bad.items() if v}, couplings=table)
json.dump(out, open(HERE.parent / ("mass_%s_summary.json" % which), "w"), indent=1)
print(json.dumps(dict(totals=dict(T), reach=dict(reach), predictions={k: v["holds"] for k, v in pred.items()}), indent=1))
for k, v in bad.items():
    if v: print(k, "failures (first 5):", v[:5])
