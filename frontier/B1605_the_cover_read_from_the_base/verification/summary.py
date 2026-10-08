#!/usr/bin/env python3
"""B1605 -- the cells from the per-thread files (schreier_<thread>.json) against B1602's readings at 40 digits."""
import json, glob, pathlib
HERE = pathlib.Path(__file__).resolve().parent
B1602 = HERE.parents[1] / "B1602_the_forced_cover_on_every_thread" / "verification"
MATS = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1))}
def trace(w):
    A = ((1, 0), (0, 1))
    for c in w:
        B = MATS[c]; A = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return A[0][0] + A[1][1]
rows = {}
for f in glob.glob(str(HERE / "schreier_b*.json")):
    d = json.load(open(f)); rows[d["thread"]] = d
pop = [l.strip() for l in open(HERE / "unreliable_threads.txt") if l.strip()]
odd = [t for t in pop if trace(t[3:]) % 2]; even = [t for t in pop if t not in odd]
old = {d["thread"]: [c["members"] for c in d["covers"]] for d in (json.load(open(f)) for f in glob.glob(str(B1602 / "forced_b*.json")))}
gen = sum(1 for t in pop for c in rows[t]["covers"] for m in c["members"] for r in m["readings"] if (r["I_W1"], r["I_L2W1"]) == (-1, -1) and all(r["dead_on_cusps"]))
summary = {
 "population": len(pop), "odd": len(odd), "even": len(even), "kernels": sum(len(rows[t]["covers"]) for t in pop),
 "V1_pm_LR_reproduced": (rows["b++LR"]["covers"][0]["member_count"] == 24 and rows["b++LR"]["covers"][0]["structures"] == [[1, 0, 1]] and rows["b++LR"]["covers"][0]["kinds"] == [[-1, -1]]
                         and rows["b+-LR"]["covers"][0]["member_count"] == 6 and rows["b+-LR"]["covers"][0]["structures"] == [[4, 0, 4]] and rows["b+-LR"]["covers"][0]["kinds"] == [[0, -3]]),
 "R1_all_accepted": all(float(c["four_residual"]) < 1e-30 and c["chi_fails"] == 0 for t in pop for c in rows[t]["covers"]),
 "max_residual": max(float(c["four_residual"]) for t in pop for c in rows[t]["covers"]),
 "R2_no_odd_carrier": all(c["member_count"] == 0 for t in odd for c in rows[t]["covers"]),
 "R3_even_status_changes": {t: (old[t], [c["member_count"] for c in rows[t]["covers"]]) for t in pop if old[t] != [c["member_count"] for c in rows[t]["covers"]]},
 "R4_kinds": sorted({tuple(k) for t in pop for c in rows[t]["covers"] for k in c["kinds"]}),
 "even_carriers": [t for t in even if any(c["member_count"] for c in rows[t]["covers"])],
 "readings_on_population": sum(len(m["readings"]) for t in pop for c in rows[t]["covers"] for m in c["members"]), "generation_shaped_on_population": gen,
 "chi_checked_every_character_on": sum(1 for t in pop for c in rows[t]["covers"] if c["chi_checked"] == "every character"),
 "chi_sampled_on": sum(1 for t in pop for c in rows[t]["covers"] if c["chi_checked"] != "every character"),
 "seconds_total": round(sum(rows[t]["s"] for t in pop) + rows["b++LR"]["s"] + rows["b+-LR"]["s"], 1)}
json.dump(summary, open(HERE / "summary.json", "w"), indent=1); print(json.dumps(summary, indent=1))
