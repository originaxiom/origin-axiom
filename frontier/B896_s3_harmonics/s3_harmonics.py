"""B896 M1: the S3-harmonic analysis of the banked frame-indexed tables.

The alignment across frames is solved JOINTLY: block permutation (3! x 3!)
x row assignment (Hungarian) per frame -- the naive fixed-row model leaves
5/11 rows misaligned (bimodal residue, caught and discarded). Then the
isotypic split: trivial (frame-symmetric) + standard (frame-breaking).
Sign cannot appear in single-frame functions (rep theory) -- placement
stated. Inputs: B889 tables, B890/B891 deviations.
"""
import json, os
from itertools import permutations
import numpy as np
from scipy.optimize import linear_sum_assignment

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
B889 = json.load(open(os.path.join(ROOT, "B889_canonical_dictionary/results.json")))
B890 = json.load(open(os.path.join(ROOT, "B890_foreign_pair/results.json")))
B891 = json.load(open(os.path.join(ROOT, "B891_matter_extension/results.json")))

tables = {i: np.array([[float(x) for x in r["mass"]]
                       for r in B889["tables"][str(i)]]) for i in (0, 1, 2)}
dims = [int(r["dim"]) for r in B889["tables"]["0"]]
NR = tables[0].shape[0]

def apply_perm(T, ps, po):
    out = np.zeros_like(T)
    for b in range(3): out[:, ps[b]] = T[:, b]
    for b in range(3): out[:, 3+po[b]] = T[:, 3+b]
    return out

# ---- 1. joint alignment: block perms x Hungarian row assignment ----
ALIGN = {0: {"ps": (0,1,2), "po": (0,1,2), "rows": list(range(NR)), "cost": 0.0}}
for i in (1, 2):
    best = None
    for ps in permutations(range(3)):
        for po in permutations(range(3)):
            P = apply_perm(tables[i], ps, po)
            # cost[r0, ri] = ||T0[r0] - P[ri]||^2, forbid dim-mismatched rows
            C = ((tables[0][:, None, :] - P[None, :, :])**2).sum(axis=2)
            for a in range(NR):
                for b in range(NR):
                    if dims[a] != dims[b]: C[a, b] = 1e9
            ri, ci = linear_sum_assignment(C)
            cost = C[ri, ci].sum()
            if best is None or cost < best["cost"]:
                best = {"ps": ps, "po": po,
                        "rows": [int(c) for c in ci], "cost": float(cost)}
    ALIGN[i] = best
    print(f"frame {i}: singlet-perm {best['ps']} octet-perm {best['po']} "
          f"residual {best['cost']:.3e} rowmap {best['rows']}")

sq = lambda p: tuple(p[p[b]] for b in range(3))
cyc_blocks = (sq(ALIGN[1]["ps"]) == ALIGN[2]["ps"]
              and sq(ALIGN[1]["po"]) == ALIGN[2]["po"])
r1 = ALIGN[1]["rows"]; r2 = ALIGN[2]["rows"]
cyc_rows = [r1[r1[k]] for k in range(NR)] == r2
print("cyclic consistency: blocks", cyc_blocks, "rows", cyc_rows)

A = {}
for i in (0, 1, 2):
    P = apply_perm(tables[i], ALIGN[i]["ps"], ALIGN[i]["po"])
    A[i] = P[ALIGN[i]["rows"], :]

# ---- 2. isotypic split of the jointly aligned family ----
V = np.stack([A[i] for i in (0, 1, 2)])          # (3, NR, 6)
M = V.mean(axis=0, keepdims=True)                 # trivial component
tot2 = float((V**2).sum()); std2 = float(((V - M)**2).sum())
row_std = [float(((V[:, r] - M[0, r])**2).sum() / (V[:, r]**2).sum())
           for r in range(NR)]
print(f"B889 jointly aligned: trivial fraction {1 - std2/tot2:.10f}, "
      f"standard fraction {std2/tot2:.3e}")
print("per-row standard fraction:", ["%.1e" % x for x in row_std])

# ---- 3. the sealed-cell deviations: the per-frame asymmetry, quantified ----
def split3(v):
    v = [float(x) for x in v]
    m = sum(v)/3
    t2 = 3*m*m; s2 = sum((x-m)**2 for x in v)
    return {"values": v, "mean": m, "std_fraction": s2/(t2+s2)}

r890 = split3([B890["frames"][str(i)]["max_dev"] for i in (0, 1, 2)])
r891 = split3([B891["frames"][str(i)]["max_dev"] for i in (0, 1, 2)])
print("B890 vacuum-deviation split:", r890)
print("B891 matter-deviation split:", r891)

# ---- 4. sign placement (rep theory, exact) ----
sign_note = ("sign isotypic absent from all single-frame tables (C^3 = "
             "trivial + standard as an S3 rep); the banked Z2 cocycle "
             "(prod c = -1, B892) is exactly the nontrivial sign-class "
             "in oriented pair data")
print(sign_note)

json.dump({
    "alignment": {str(i): {"singlet_perm": list(ALIGN[i]["ps"]),
                           "octet_perm": list(ALIGN[i]["po"]),
                           "row_map": ALIGN[i]["rows"],
                           "residual": ALIGN[i]["cost"]} for i in ALIGN},
    "cyclic_consistent_blocks": bool(cyc_blocks),
    "cyclic_consistent_rows": bool(cyc_rows),
    "b889_trivial_fraction": 1 - std2/tot2,
    "b889_standard_fraction": std2/tot2,
    "b889_per_row_standard_fraction": row_std,
    "b890_dev_split": r890, "b891_dev_split": r891,
    "sign_isotypic": sign_note,
}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "results.json"), "w"), indent=1)
print("saved")
