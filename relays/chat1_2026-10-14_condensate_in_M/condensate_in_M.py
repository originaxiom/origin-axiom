"""The cusp condensate's direction in M (PREREGISTRATION.md, sealed at aa4dad108, sha256 c0d61a05...).

Instrument: W70's script, copied verbatim as w70_lib.py (SM seat d73c539b0); its roots, chain, weights, h_Q, colour,
weak axis and hypercharge Cartans are used unchanged. This file adds only projections and a classification, exact.

  Q0  W70's own main() re-run here (its cells N1-N5), and the neutral Higgs-like roots recomputed by its rule
  A1a su(2)_Q (Cartan h_Q, raising roots ws_2r - ws_2r+1, taken diagonally) is a Standard Model singlet
  A1b no p-odd root is a root of su(2)_Q, so every condensate E_alpha has zero projection on M (Reading A)
  A1c H_alpha's M-component (alpha.h_Q / h_Q.h_Q) h_Q: non-zero and real for all 112
  B1  the SU(2)_Q x SU(3)_B content of every p-odd root (Reading B): real integer block weights
  B2  per admissible Y, the four neutral Higgs-like condensates' block roots are +-(e_r - e_s), {r, s} the blocks with
      Y != -5/6
  read-outs: tables; Reading B's axis read as B1644's a and B1645's m at tau = iy
"""
import json, itertools, pathlib, sys
from fractions import Fraction as F
from collections import Counter
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import w70_lib as W

out = {}

# ---------------------------------------------------------------- Q0: W70 re-run through its own main()
W.main()
w70 = json.loads((HERE / "the_cusp_condensate_charge_map.json").read_text())
admissible = [tuple(F(x) for x in y) for y in w70["N2"]["admissible"]]
odd = [r for r in W.RR if W.dot(r, W.HQ).denominator == 1 and W.dot(r, W.HQ) % 2 != 0]

def higgs_like(y):
    Y = W.ycartan(y); rows = []
    for r in sorted(odd):
        if W.colour(r) != (0, 0):
            continue
        t3, yr = W.dot(r, W.WEAK) / 2, W.dot(r, Y)
        if abs(yr) == F(1, 2) and t3 + yr == 0:
            rows.append(r)
    return rows

HL = {y: higgs_like(y) for y in admissible}
out["Q0"] = {"w70_cells": w70["cells"], "p_odd": len(odd), "admissible": [[str(x) for x in y] for y in admissible],
             "higgs_like_per_Y": {",".join(map(str, y)): len(v) for y, v in HL.items()},
             "holds": bool(all(w70["cells"].values()) and len(odd) == 112 and len(admissible) == 6
                           and all(len(v) == 4 for v in HL.values()))}

# ---------------------------------------------------------------- Reading A: su(2)_Q inside su(6)
BETA = [W.add(W.WS[2 * r], W.WS[2 * r + 1], -1) for r in range(3)]
roots_Q = BETA + [W.scale(b, -1) for b in BETA]
HQ = W.HQ
a1a = {
    "beta_are_E8_roots": all(b in W.RR for b in roots_Q),
    "beta.h_Q": [str(W.dot(b, HQ)) for b in BETA],
    "colour_singlet": all(W.dot(b, c) == 0 for b in roots_Q for c in W.COLOUR) and all(W.dot(HQ, c) == 0 for c in W.COLOUR),
    "weak_singlet": all(W.dot(b, W.WEAK) == 0 for b in roots_Q) and W.dot(HQ, W.WEAK) == 0,
    "Y_zero_for_all_admissible": all(W.dot(b, W.ycartan(y)) == 0 for b in roots_Q for y in admissible),
    "h_Q.h_Q": str(W.dot(HQ, HQ)),
}
a1a["holds"] = bool(a1a["beta_are_E8_roots"] and a1a["colour_singlet"] and a1a["weak_singlet"] and a1a["Y_zero_for_all_admissible"])
out["A1a"] = a1a

a1b = {"p_odd_roots_that_are_su2Q_roots": sum(1 for r in odd if r in roots_Q),
       "su2Q_roots_parity": [str(W.dot(b, HQ) % 2) for b in roots_Q]}
a1b["holds"] = bool(a1b["p_odd_roots_that_are_su2Q_roots"] == 0)
out["A1b"] = a1b

hq2 = W.dot(HQ, HQ)
coef = Counter(str(W.dot(r, HQ) / hq2) for r in odd)
hl_union = sorted({r for v in HL.values() for r in v})
out["A1c"] = {"M_component_coefficient_distribution_(alpha.hQ/hQ.hQ)": dict(coef),
              "nonzero_for_all_112": all(W.dot(r, HQ) != 0 for r in odd),
              "higgs_like_union": len(hl_union),
              "higgs_like_coefficients": dict(Counter(str(W.dot(r, HQ) / hq2) for r in hl_union)),
              "real": True,
              "holds": bool(all(W.dot(r, HQ) != 0 for r in odd))}

# ---------------------------------------------------------------- Reading B: the block space 3_B
BLOCK = {0: "b", 1: "b", 2: "a", 3: "a", 4: "ab", 5: "ab"}
NAMES = ["b", "a", "ab"]
def su6_content(r):
    v = [W.dot(r, w) for w in W.WS]
    if sorted(v) == sorted([F(5, 6)] + [F(-1, 6)] * 5):
        return ("6", (v.index(F(5, 6)),))
    if sorted(v) == sorted([F(-5, 6)] + [F(1, 6)] * 5):
        return ("6bar", (v.index(F(-5, 6)),))
    if all(x in (F(1, 2), F(-1, 2)) for x in v) and v.count(F(1, 2)) == 3:
        return ("20", tuple(j for j in range(6) if v[j] == F(1, 2)))
    if all(x == 0 for x in v):
        return ("1", ())
    pos = [j for j in range(6) if v[j] == 1]; neg = [j for j in range(6) if v[j] == -1]
    if len(pos) == 1 and len(neg) == 1 and all(v[j] == 0 for j in range(6) if j not in pos + neg):
        return ("35", (pos[0], neg[0]))
    if all(x in (F(1, 3), F(-2, 3)) for x in v) or all(x in (F(-1, 3), F(2, 3)) for x in v):
        return ("15", tuple(j for j in range(6) if v[j] in (F(2, 3), F(-2, 3))))
    return ("?", tuple(v))
def block_weight(kind, S):
    c = Counter(BLOCK[j] for j in S)
    w = {n: c.get(n, 0) for n in NAMES}
    if kind == "6bar":
        w = {n: -x for n, x in w.items()}
    tot = sum(w.values()); tr = F(tot, 3)
    return tuple(F(w[n]) - tr for n in NAMES)            # traceless SU(3)_B weight
def classify_B(kind, S):
    bw = block_weight(kind, S)
    if kind in ("6", "6bar"):
        return "vector", bw
    if kind == "20":
        c = Counter(BLOCK[j] for j in S)
        if max(c.values()) == 2:
            r = [n for n in NAMES if c.get(n, 0) == 2][0]; s = [n for n in NAMES if c.get(n, 0) == 0][0]
            return f"root e_{r} - e_{s}", bw
        return "block-Cartan (one per block: mixes (4,1) and (2,8))", bw
    return kind, bw
b1 = Counter(); table = []
for r in sorted(odd):
    kind, S = su6_content(r); cls, bw = classify_B(kind, S)
    b1[(kind, cls.split(":")[0] if cls.startswith("block") else ("root" if cls.startswith("root") else cls))] += 1
    table.append({"root": [str(x) for x in r], "su6": kind, "indices": list(S), "B": cls, "B_weight": [str(x) for x in bw],
                  "alpha.hQ": str(W.dot(r, HQ))})
out["B1"] = {"classes": {f"{k[0]}|{k[1]}": v for k, v in b1.items()},
             "all_block_weights_rational_real": all(all(F(x).denominator in (1, 3) for x in row["B_weight"]) for row in table),
             "holds": bool(sum(b1.values()) == 112 and not any(k[0] == "?" for k in b1))}

b2 = {}; ok2 = True
for y in admissible:
    ylab = dict(zip(NAMES, y)); not_m56 = sorted(n for n in NAMES if ylab[n] != F(-5, 6))
    rows = []
    for r in HL[y]:
        kind, S = su6_content(r); cls, _ = classify_B(kind, S)
        rows.append({"root": [str(x) for x in r], "B": cls, "Y": str(W.dot(r, W.ycartan(y)))})
        if not cls.startswith("root"):
            ok2 = False
        else:
            pair = sorted(cls.replace("root ", "").replace("e_", "").split(" - "))
            ok2 &= (pair == not_m56)
    b2[",".join(map(str, y))] = {"blocks_not_-5/6": not_m56, "rows": rows}
out["B2"] = {"per_Y": b2, "holds": bool(ok2)}

# ---------------------------------------------------------------- read-out: Reading B's axis as B1644's a (B1645's m)
UNIT_OF_BLOCK = {"b": 1, "a": 0, "ab": 2}            # units' labels (i, j, k) = (a, b, ab)
def R_np(t, K=60):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])
def m_of(a, t):
    R = R_np(t); Y = np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)
    s = np.linalg.svd(Y, compute_uv=False); return float(s[1] / s[0])
axis_m = {}
for y in admissible:
    ylab = dict(zip(NAMES, y)); t_block = [n for n in NAMES if ylab[n] == F(-5, 6)][0]
    a = np.zeros(3); a[UNIT_OF_BLOCK[t_block]] = 1.0
    axis_m[",".join(map(str, y))] = {"axis_block": t_block, "unit": "ijk"[UNIT_OF_BLOCK[t_block]],
                                     "m_at_tau=iy": {str(yy): m_of(a, 1j * yy) for yy in (1, 2, 4)}}
out["readout_axis_as_Higgs"] = axis_m
out["verdict_V"] = {"no_single_root_condensate_gives_a_complex_null_vector_in_M":
                    bool(out["A1b"]["holds"] and out["A1c"]["holds"] and out["B1"]["holds"]),
                    "reason": "Reading A: E_alpha has zero M-part (A1b); H_alpha's M-part is real (A1c). "
                              "Reading B: every block weight is rational and real (B1)."}
out["cells"] = {k: out[k]["holds"] for k in ("Q0", "A1a", "A1b", "A1c", "B1", "B2")}
out["cells"]["V"] = out["verdict_V"]["no_single_root_condensate_gives_a_complex_null_vector_in_M"]
(HERE / "condensate_in_M.json").write_text(json.dumps({**out, "table_112": table}, indent=1, default=str) + "\n")
print(json.dumps({k: v for k, v in out.items() if k not in ("B2",)}, indent=1, default=str))
print(json.dumps(out["cells"], indent=1))
