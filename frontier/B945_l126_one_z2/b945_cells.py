#!/usr/bin/env python3
"""B945 / L126 -- one Z/2 or two?  Sealed 48732158..., before compute.

Two involutions on cyclic LR-words:
    rho (reverse)  -- word reversal      = reversing the base S^1 = TIME reversal
    sigma (swap)   -- R <-> L            = fiber orientation flip = CHIRALITY
They generate a Klein group V = {1, rho, sigma, rho.sigma}.
GHH (B136): amphichiral <=> rho.sigma fixes W cyclically.

The question is what the OBJECT's stabilizer in V actually is.
"""
import json
import pathlib
from itertools import product

import sympy as sp

R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])
res = {}


def rots(w):
    return {w[i:] + w[:i] for i in range(len(w))} if w else {""}


def rho(w):                       # reverse
    return w[::-1]


def sigma(w):                     # swap R <-> L
    return w.translate(str.maketrans("RL", "LR"))


def stab(w):
    """Stabilizer of the cyclic word w inside V = {1, rho, sigma, rho.sigma}."""
    rs = rots(w)
    out = []
    if w in rs:
        out.append("1")
    if rho(w) in rs:
        out.append("rho")
    if sigma(w) in rs:
        out.append("sigma")
    if sigma(rho(w)) in rs:
        out.append("rho.sigma")
    return out


def mat(w):
    M = sp.eye(2)
    for ch in w:
        M = M * (R if ch == "R" else L)
    return M


# ---------------------------------------------------------------- CELL 1
obj = "RL"
res["cell1"] = {
    "word": obj,
    "cyclic_rotations": sorted(rots(obj)),
    "rho(W)": rho(obj), "sigma(W)": sigma(obj), "rho.sigma(W)": sigma(rho(obj)),
    "stabilizer": stab(obj),
}
res["cell1"]["is_amphichiral_GHH"] = "rho.sigma" in res["cell1"]["stabilizer"]
res["cell1"]["rho_alone_fixes"] = "rho" in res["cell1"]["stabilizer"]
res["cell1"]["sigma_alone_fixes"] = "sigma" in res["cell1"]["stabilizer"]

# ---------------------------------------------------------------- CELL 2
fam = []
for m in range(1, 9):
    w = "R" * m + "L" * m
    s = stab(w)
    fam.append({"m": m, "word": w, "stabilizer": s,
                "amphichiral": "rho.sigma" in s,
                "rho_alone": "rho" in s, "sigma_alone": "sigma" in s})
res["cell2"] = fam
res["cell2_all_amphichiral"] = all(f["amphichiral"] for f in fam)
res["cell2_rho_alone_always"] = all(f["rho_alone"] for f in fam)
res["cell2_sigma_alone_always"] = all(f["sigma_alone"] for f in fam)

# ---------------------------------------------------------------- CELL 3
census = {}
amph_stabs = {}
seen = set()
for n in range(2, 11):
    for bits in product("RL", repeat=n):
        w = "".join(bits)
        if "R" not in w or "L" not in w:      # need both letters for a bundle
            continue
        canon = min(rots(w))                   # one representative per cyclic class
        if canon in seen:
            continue
        seen.add(canon)
        s = tuple(stab(canon))
        census[str(s)] = census.get(str(s), 0) + 1
        if "rho.sigma" in s:
            amph_stabs[str(s)] = amph_stabs.get(str(s), 0) + 1
res["cell3_all_words"] = census
res["cell3_amphichiral_only"] = amph_stabs
res["cell3_n_cyclic_classes"] = len(seen)
# among AMPHICHIRAL words, how many are fixed by rho alone / sigma alone?
res["cell3_amphichiral_with_full_V"] = amph_stabs.get(str(("1", "rho", "sigma", "rho.sigma")), 0)
res["cell3_amphichiral_diagonal_only"] = amph_stabs.get(str(("1", "rho.sigma")), 0)

# ---------------------------------------------------------------- CELL 4
Rt_is_L = sp.simplify(R.T - L) == sp.zeros(2, 2)
W = mat(obj)
res["cell4"] = {
    "R_transpose_is_L": bool(Rt_is_L),
    "W": [[int(x) for x in r] for r in W.tolist()],
    "W_is_symmetric": bool(sp.simplify(W - W.T) == sp.zeros(2, 2)),
    "reverse_equals_swap_of_transpose": bool(
        sp.simplify(mat(rho(obj)) - mat(sigma(obj)).T) == sp.zeros(2, 2)),
}
# vacuity check: is "conjugate to its transpose" content-free?
res["cell4"]["every_matrix_conj_to_transpose_over_a_field"] = True
res["cell4"]["so_the_content_must_be_integral"] = True

# ---------------------------------------------------------------- VERDICT
s1 = res["cell1"]["stabilizer"]
if not res["cell1"]["is_amphichiral_GHH"]:
    outcome = "INSTRUMENT FAILURE"
elif res["cell1"]["rho_alone_fixes"] and res["cell1"]["sigma_alone_fixes"]:
    outcome = "INDEPENDENT"
elif s1 == ["1", "rho.sigma"]:
    outcome = "LOCKED"
else:
    outcome = "INSTRUMENT FAILURE"
res["verdict"] = {"outcome_at_the_object": outcome, "object_stabilizer": s1}

print(json.dumps(res, indent=1))
pathlib.Path("results.json").write_text(json.dumps(res, indent=1) + "\n")
