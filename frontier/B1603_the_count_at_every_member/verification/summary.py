#!/usr/bin/env python3
"""B1603 -- the cells from the per-thread files (count_<thread>.json): C1-C5 as sealed, the kinds, the generation-shaped
readings per thread with their sign twins, the floor and ceiling on every reading."""
import json, glob, pathlib
from collections import Counter
HERE = pathlib.Path(__file__).resolve().parent
rows = {}
for f in sorted(glob.glob(str(HERE / "count_b*.json"))):
    d = json.load(open(f)); rows[d["thread"]] = d
readings = [(t, cv, m, r) for t, d in rows.items() for cv in d["covers"] for m in cv["members"] for r in m["readings"]]
kinds = Counter((r["I_W1"], r["I_L2W1"]) for _, _, _, r in readings)
gen = Counter(t for t, _, _, r in readings if r["generation_shaped"])
odd = lambda t: (1 if t[2] == "+" else -1) * 1  # sign only; parity from the word below
MATS = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1))}
def trace(w):
    A = ((1, 0), (0, 1))
    for c in w:
        B = MATS[c]; A = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return A[0][0] + A[1][1]
is_odd = {t: trace(t[3:]) % 2 == 1 for t in rows}
plus = [r for t, _, _, r in readings if t == "b++LR"]; minus = [r for t, _, _, r in readings if t == "b+-LR"]
summary = {
 "threads": len(rows), "members": sum(len(m) for d in rows.values() for cv in d["covers"] for m in [cv["members"]]), "readings": len(readings),
 "C1_plus_LR_all_generation_shaped": {"readings": len(plus), "holds": bool(plus) and all(r["generation_shaped"] for r in plus)},
 "C2_minus_LR_all_0_minus_3": {"readings": len(minus), "holds": bool(minus) and all((r["I_W1"], r["I_L2W1"]) == (0, -3) and all(r["dead_on_cusps"]) for r in minus)},
 "C3_no_even_generation_shaped": {"even_generation_shaped": {t: n for t, n in sorted(gen.items()) if not is_odd[t]}, "holds": not any(not is_odd[t] for t in gen)},
 "C4_floor_and_ceiling": {"floor_fails": sum(1 for _, _, _, r in readings if not r["floor_holds"]), "ceiling_fails": sum(1 for _, _, _, r in readings if not r["ceiling_holds"]), "holds": all(r["floor_holds"] and r["ceiling_holds"] for _, _, _, r in readings)},
 "C5_at_most_five_kinds": {"kinds": {str(k): v for k, v in sorted(kinds.items())}, "count": len(kinds), "holds": len(kinds) <= 5},
 "generation_shaped_total": sum(gen.values()), "generation_shaped_by_thread": dict(sorted(gen.items())),
 "odd_threads_generation_shaped": {t: n for t, n in gen.items() if is_odd[t]},
 "readings_by_thread": {t: sum(len(m["readings"]) for cv in d["covers"] for m in cv["members"]) for t, d in sorted(rows.items())},
}
json.dump(summary, open(HERE / "summary.json", "w"), indent=1); print(json.dumps(summary, indent=1))
