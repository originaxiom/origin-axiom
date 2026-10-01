#!/usr/bin/env python3
"""Reader of the sealed run.  usage: read_law.py population | control      (writes ../law_<which>_summary.json)"""
import sys, json, re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
which = sys.argv[1]
pat = re.compile(r"^law_population_\d\d\.json$") if which == "population" else re.compile(r"^law_control_.*\.json$")
files = sorted(f for f in HERE.iterdir() if pat.match(f.name))
T = collections.Counter(); bad = collections.defaultdict(list); seconds = []
for f in files:
    rec = json.load(open(f)); T["levels"] += 1; tag = "%s level %d" % (rec["state"], rec["k"])
    for b in rec["backgrounds"]:
        T["backgrounds"] += 1
        if "error" in b: T["backgrounds_not_followed"] += 1; bad["not_followed"].append((tag, b["ell"], b["error"])); continue
        for d in b["sectors"]:
            T["sectors"] += 1
            if d["matches"] == 0:
                T["unmatched"] += 1
                if d.get("first_order_ok"): T["unmatched_first_order_ok"] += 1
                else: bad["P1"].append((tag, b["ell"], d["beta"], d["order"], d.get("coeff"), d["predicted_first"]))
            else:
                T["matched"] += 1
                if d["order"] is None: T["matched_identically_zero"] += 1
                elif d["order"] >= 2: T["matched_order_ge_2"] += 1; T["matched_order_%d" % d["order"]] += 1; seconds.append((tag, b["ell"], d["matches"], d["order"], d["coeff"]))
                else: bad["P2"].append((tag, b["ell"], d["beta"], d["order"], d.get("coeff")))
            if d["matches"] == 0 and d["order"] is None: bad["P2b"].append((tag, b["ell"], d["beta"]))
        if "slope_limit_ok" in b:
            T["slope_limit_tested"] += 1; T["slope_limit_ok"] += b["slope_limit_ok"]
            if not b["slope_limit_ok"]: bad["P3"].append((tag, b["ell"], b["slope"], b["cusp_shape_limit"]))
        else: T["slope_limit_not_tested"] += 1
        if b["filling_type"] is None: T["filling_not_tested"] += 1
        else:
            T["filling_tested"] += 1; T["zero_type"] += b["zero_type"]; T["filling_type"] += b["filling_type"]
            if b["zero_type"] == b["filling_type"]: T["zero_iff_filling_ok"] += 1
            else: bad["P4"].append((tag, b["ell"], b["slope"], b["zero_type"], b["filling_type"]))
pred = dict(
    P1=dict(statement="every unmatched sector: order 1 with coefficient (s(alpha) - s(l)) (s(1/beta) - s(l))", holds=not bad["P1"] and T["unmatched"] > 0, tested=T["unmatched"], failures=len(bad["P1"])),
    P2=dict(statement="every matched sector: order at least 2 (or identically zero); no unmatched sector is identically zero", holds=not bad["P2"] and not bad["P2b"], tested=T["matched"], failures=len(bad["P2"]) + len(bad["P2b"])),
    P3=dict(statement="the cusp shape of the curve tends to |s(l)| at the reducible end", holds=not bad["P3"] and T["slope_limit_tested"] > 0, tested=T["slope_limit_tested"], failures=len(bad["P3"])),
    P4=dict(statement="matched sectors identically zero  <=>  the meridian is +-(longitude)^(+-s) along the curve", holds=not bad["P4"] and T["filling_tested"] > 0, tested=T["filling_tested"], failures=len(bad["P4"])),
    P5=dict(statement="some background of the population is of filling type and some is not", holds=0 < T["filling_type"] < T["filling_tested"], filling=T["filling_type"], tested=T["filling_tested"]))
out = dict(which=which, files=[f.name for f in files], totals=dict(T), predictions=pred, failures={k: v[:40] for k, v in bad.items() if v}, second_order_sample=seconds[:60])
json.dump(out, open(HERE.parent / ("law_%s_summary.json" % which), "w"), indent=1)
print(json.dumps(dict(totals=dict(T), predictions={k: (v["holds"], v.get("tested"), v.get("failures")) for k, v in pred.items()}), indent=1))
for k, v in bad.items():
    if v: print(k, "failures (first 5):", v[:5])
