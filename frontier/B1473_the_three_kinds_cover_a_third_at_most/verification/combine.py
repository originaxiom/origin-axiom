#!/usr/bin/env python3
"""L244 (a): combine the first reading (census.json) with the adversarial second reading (verified_*.json)."""
import json, pathlib, collections
S = pathlib.Path(__file__).resolve().parent
R = S / "readers" if (S / "readers").exists() else S
c = json.load(open(S / "census.json")); v = json.load(open(R / "verified_0.json")) + json.load(open(R / "verified_1.json"))
vd = {r["id"]: r for r in v}
first = collections.Counter(r["kind"] for r in c["rows"].values())
conf, numer, demoted, final = collections.Counter(), collections.Counter(), collections.Counter(), {}
for i, r in c["rows"].items():
    if r["kind"] == "OTHER": final[i] = "OTHER:" + (r.get("label") or ""); continue
    s = vd[i]
    if s["verdict"] == "CONFIRM": conf[r["kind"]] += 1; final[i] = r["kind"]
    elif any(w in s["kind"].lower() for w in ("numerolog", "fit", "catalogue")):
        numer[r["kind"]] += 1; final[i] = r["kind"] + " (fitted/numerology: kept per the brief; second reader demoted)"
    else: demoted[(r["kind"], s["kind"])] += 1; final[i] = s["kind"]
tot = len(c["rows"]); three = sum(first[k] for k in ("PAIRING", "FLATNESS", "NON-UNIQUENESS")); core = sum(conf.values())
out = dict(population=tot, first_readers=dict(first), three_kinds_first=three, adversarial_confirmed=dict(conf), core=core,
           fitted_kept=dict(numer), core_plus_fitted=core + sum(numer.values()),
           demoted={" -> ".join(k): n for k, n in demoted.items()}, demoted_total=sum(demoted.values()), final=final)
json.dump(out, open(S / "census_final.json", "w"), indent=1)
print("population", tot, "| first readers three kinds", three, "| adversarial core", core, "| core + fitted", out["core_plus_fitted"], "| demoted", out["demoted_total"])
print(dict(first)); print(dict(conf)); print(demoted.most_common(10))
