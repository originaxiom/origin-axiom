#!/usr/bin/env python3
"""Refinement check for tnorm.py's invariant Gram: the classes with the largest n = 32 off-diagonal and the largest
n = 20 vs 32 change, re-integrated over the 4-fold cover at n = 32, 48, 64.  Also corrects one prediction label of
tnorm.py's control C-(ii) (see the docstring of the corrected function below) and stores both in refine_results.json.
    OMP_NUM_THREADS=1 nice -n 10 python3 -I refine.py"""
import json, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tnorm as T

R = json.loads((HERE / "tnorm_results.json").read_text())
G = R["G_results"]
pick = set(sorted(range(len(G)), key=lambda i: -G[i]["cover"]["max_offdiag"])[:4])
pick |= set(sorted(range(len(G)), key=lambda i: -G[i]["cover"]["conv_n20_vs_n32_diag"])[:4])
out = {"refined": []}
mats = [Cp.conj().T @ Cq for _, Cp in T.BLOCKS for _, Cq in T.BLOCKS]
for i in sorted(pick):
    g = G[i]; a, b = Fr(g["a"]), Fr(g["b"]); tau = complex(*g["tau"])
    f = T.integrand(a, b, tau, mats); row = {"class": g["key"], "a": g["a"], "b": g["b"], "tau": g["tau"]}
    prev = None
    for n in (32, 48, 64):
        Gm = T.gram_from(T.quad(f, T.OFF[0], T.OFF[0] + 2, T.OFF[1], T.OFF[1] + 2, tau, n) / 4)
        off, spread, d = T.gram_stats(Gm)
        row["n=%d" % n] = {"max_offdiag": off, "max_diag_spread": spread, "norm_F2": float(d[0]),
                           "diag change from previous n": None if prev is None else float(abs(d[0] / prev - 1))}
        prev = d[0]
    out["refined"].append(row); print(json.dumps(row), flush=True)


def control_frame_negative_corrected(a, b, tau, theta=0.3):
    """C-(ii) with its second prediction corrected.  C' = cos(th) QI + sin(th) QJ in place of QI.
    (QJ, C'): cos(th) F^dag QJ^dag QI F [a cross term, character non-trivial, cover 0] + sin(th) |F|^2 -> sin(th).
    (C', QK): cos(th) F^dag QI^dag QK F + sin(th) F^dag QJ^dag QK F; QI^dag QK = QJ and QJ^dag QK = -QI are both
    non-trivial-character cross terms, so the cover value is 0 (tnorm.py's first label, sin(th), was an error of mine)."""
    r = T.control_frame_negative(a, b, tau, theta)
    r["predicted (C',QK)"] = 0.0
    r["note"] = "the (C', QK) prediction corrected from sin(theta) to 0 after the run; the measured value is unchanged"
    return r


out["C-_frame_rotated_block_corrected"] = {str(t): control_frame_negative_corrected(Fr(2, 5), Fr(-1, 5), t) for t in (1j, 0.35 + 2.75j)}
json.dump(out, open(HERE / "refine_results.json", "w"), indent=1)
print(json.dumps(out["C-_frame_rotated_block_corrected"], indent=1))
