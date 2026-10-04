#!/usr/bin/env python3
"""B1471 -- score the sealed predictions P1-P5 from realness.json; write analysis.json and print the table."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
rows = json.load(open(HERE / "realness.json"))
LANE_FIVE = ["m206", "m207", "s957", "s960", "s961"]
LANE_CHIRAL_8 = None   # the lane's chiral eight are not named in its FINDINGS; the 16 usable of xB007's 21 are its population


def verdicts(r, n):
    t = r.get("n", {}).get(str(n)) or r.get("n", {}).get(n)
    if not t or "error" in t: return None
    return dict(T1=t["T1_verdict"], phase=t.get("T1_phase"), T2=t["T2_verdict"], T3=t["T3_verdict"], R2=t["values"].get("2.0"))


usable = [r for r in rows if "error" not in r]
excluded = [(r["name"], r["error"]) for r in rows if "error" in r]
out = dict(members=len(rows), usable=len(usable), excluded=excluded, table=[])
P1 = dict(holds=[], fails=[]); P2 = dict(holds=[], fails=[]); chiral = dict(complex=[], real=[]); five = {}
col_disagree = []
for r in usable:
    amph_iso, amph_sn, amph_b = r["amphichiral_by_isometry"], r["amphichiral_snappy"], r.get("amphichiral_B1235")
    if not (amph_iso == amph_sn == amph_b): col_disagree.append((r["name"], amph_iso, amph_sn, amph_b))
    ev = {n: verdicts(r, n) for n in (2, 4)}; od = {n: verdicts(r, n) for n in (1, 3)}
    row = dict(name=r["name"], h1=r["h1"], phi_per=r["phi_per"], amphi_iso=amph_iso, amphi_snappy=amph_sn, amphi_B1235=amph_b,
               reversing_signs=r["reversing_signs"], even={n: ev[n] for n in ev}, odd={n: od[n] for n in od})
    out["table"].append(row)
    even_ok = [v for v in ev.values() if v]
    if not even_ok: continue
    dual = all(v["T2"].startswith("holds") for v in even_ok)
    (P1["holds"] if dual else P1["fails"]).append(r["name"])
    real = all(v["T1"] == "real-up-to-unit" for v in even_ok)
    if amph_iso: (P2["holds"] if real else P2["fails"]).append(r["name"])
    else: (chiral["real"] if real else chiral["complex"]).append(r["name"])
    if r["name"] in LANE_FIVE:
        five[r["name"]] = dict(amphi_iso=amph_iso, amphi_snappy=amph_sn, signs=r["reversing_signs"], duality=dual, real_even=real,
                               phase_even=[v.get("phase") for v in even_ok], T3_even=[v["T3"] for v in even_ok], R2_even=[v["R2"] for v in even_ok],
                               odd=[(n, od[n]["T1"], od[n].get("phase")) if od[n] else (n, None, None) for n in od])
# P5: odd-n pattern on amphichiral members
odd_pattern = collections.Counter()
for r in usable:
    if not r["amphichiral_by_isometry"]: continue
    od = {n: verdicts(r, n) for n in (1, 3)}; ev = {n: verdicts(r, n) for n in (2, 4)}
    if not all(od.values()) or not all(ev.values()): continue
    key = ("even " + ("real" if all(v["T1"] == "real-up-to-unit" for v in ev.values()) else "cplx"),
           "odd " + ("real" if all(v["T1"] == "real-up-to-unit" for v in od.values()) else "cplx"), "signs " + ",".join(r["reversing_signs"]))
    odd_pattern[key] += 1
out.update(P1=P1, P2=P2, chiral_members=chiral, lane_five=five, column_disagreements=col_disagree, odd_pattern={" | ".join(k): v for k, v in odd_pattern.items()})
def unit_agree(r):
    """retriangulated vs original: R'(t)/R(t) = +- t^k with one k at t = 2 and t = 3"""
    from mpmath import mpc, log, mpf
    res = {}
    for n, (vals2, verdict2) in r["retriangulated"].items():
        v1 = r["n"][str(n)]["values"] if str(n) in r["n"] else r["n"][n]["values"]
        ks = []
        for t in ("2.0", "3.0"):
            cx = lambda z: complex(z.replace(" ", ""))
            a, b = cx(v1[t]), cx(vals2[t])
            q = b / a; k = log(abs(q)) / log(mpf(t)); ks.append((round(float(k), 6), round(q.real / abs(q), 6)))
        res[n] = dict(k_sign_at_2_3=ks, agree=(len({k for k, s in ks}) == 1 and abs(ks[0][0] - round(ks[0][0])) < 1e-9 and len({s for k, s in ks}) == 1 and abs(abs(ks[0][1]) - 1) < 1e-9), verdict_retri=verdict2)
    return res
out["retriangulation_controls"] = {r["name"]: unit_agree(r) for r in usable if r.get("retriangulated")}
json.dump(out, open(HERE / "analysis.json", "w"), indent=1, default=str)

print("members %d usable %d excluded %d" % (len(rows), len(usable), len(excluded)))
for nm, e in excluded: print("   excluded", nm, e)
print("P1 duality at even n: holds %d fails %d %s" % (len(P1["holds"]), len(P1["fails"]), P1["fails"]))
print("P2 amphichiral (by isometry) real-up-to-unit at even n: holds %d fails %d %s" % (len(P2["holds"]), len(P2["fails"]), P2["fails"]))
print("chiral members: complex %d real %d %s" % (len(chiral["complex"]), len(chiral["real"]), chiral["real"]))
print("column disagreements (iso, snappy, B1235):", col_disagree)
print("the lane's five:")
for k, v in five.items(): print("  ", k, json.dumps(v, default=str))
print("odd-n pattern on amphichiral members:", dict(out["odd_pattern"]))
print("retriangulation controls:", json.dumps(out["retriangulation_controls"], default=str)[:600])
