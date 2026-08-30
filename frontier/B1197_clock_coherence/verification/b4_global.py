#!/usr/bin/env python3
"""B4 part 2: per-slope-family AND global monotonicity across the closings census.

'Same clock up to monotone reparameterization' is a GLOBAL statement: across the
whole census, Vol_i < Vol_j must imply |CS|_i >= |CS|_j. Per-family monotonicity
is necessary but not sufficient. Both are computed; a two-sided control (a
deliberately shuffled sequence) checks the monotonicity detector itself bites.
"""
import json, random
from math import gcd
import snappy

def fill(p, q):
    M = snappy.Manifold('m004')
    try: _ = float(M.chern_simons())
    except Exception: return None
    M.dehn_fill((p, q))
    try:
        if 'positively' not in str(M.solution_type()): return None
        return float(M.volume()), abs(((float(M.chern_simons()) + .5) % 1.) - .5)
    except Exception: return None

# dedupe: (p,q) ~ (-p,-q) is the same filled manifold
seen, rows = set(), []
for p in range(-8, 9):
    for q in range(-8, 9):
        if (p,q) == (0,0) or gcd(abs(p), abs(q)) != 1: continue
        key = (p,q) if (p > 0 or (p == 0 and q > 0)) else (-p,-q)
        if key in seen: continue
        seen.add(key)
        r = fill(*key)
        if r: rows.append({"p": key[0], "q": key[1], "vol": r[0], "abs_cs": r[1]})
print(f"distinct hyperbolic closings (up to (p,q)~(-p,-q)): {len(rows)}")

# --- per-family monotonicity: fix p, vary q ---
from collections import defaultdict
fam = defaultdict(list)
for r in rows: fam[r["p"]].append(r)
print("\nPER-FAMILY (fix p, sort by Vol; is |CS| non-increasing?):")
fam_ok = {}
for p in sorted(fam):
    seq = sorted(fam[p], key=lambda r: r["vol"])
    if len(seq) < 3: continue
    mono = all(seq[i]["abs_cs"] >= seq[i+1]["abs_cs"] - 1e-12 for i in range(len(seq)-1))
    fam_ok[p] = mono
    print(f"  p={p:>2}: n={len(seq):>2}  monotone={mono}")

# --- GLOBAL monotonicity across the whole census ---
allseq = sorted(rows, key=lambda r: r["vol"])
viol = [(allseq[i], allseq[i+1]) for i in range(len(allseq)-1)
        if allseq[i]["abs_cs"] < allseq[i+1]["abs_cs"] - 1e-9]
print(f"\nGLOBAL across {len(allseq)} closings: monotone={len(viol)==0}; violations={len(viol)}")
for a, b in viol[:6]:
    print(f"    ({a['p']},{a['q']}) Vol={a['vol']:.6f} |CS|={a['abs_cs']:.6f}"
          f"  ->  ({b['p']},{b['q']}) Vol={b['vol']:.6f} |CS|={b['abs_cs']:.6f}  (|CS| ROSE)")

# --- two-sided control: the detector must flag a shuffled sequence ---
rnd = random.Random(20260828)
sh = [dict(r) for r in allseq]; cs_vals = [r["abs_cs"] for r in sh]; rnd.shuffle(cs_vals)
for r, c in zip(sh, cs_vals): r["abs_cs"] = c
sh_viol = sum(1 for i in range(len(sh)-1) if sh[i]["abs_cs"] < sh[i+1]["abs_cs"] - 1e-9)
print(f"CONTROL (shuffled |CS| against the same Vol order): violations={sh_viol} "
      f"-> detector {'BITES' if sh_viol > 0 else 'IS VACUOUS'}")

json.dump({"n_closings": len(rows), "per_family": fam_ok,
           "global_monotone": len(viol) == 0, "n_violations": len(viol),
           "violations": [[a, b] for a, b in viol[:20]],
           "control_shuffled_violations": sh_viol, "rows": allseq},
          open("b4_global.json", "w"), indent=1)
print("DONE")
