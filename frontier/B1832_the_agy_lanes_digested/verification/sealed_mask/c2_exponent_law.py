"""SEALED-DIGEST CHECK c2 (value-free; main's residues).
Claim (agy Theorem 18 Part B.1; Theorem 19 Part B): the leading q-exponent (|R| ~ e^{-2 pi Im(tau) E}) of each channel
residue on a line of slope alpha is fixed by the bilinear's four entries,
    e_{ab} = ||q_L alpha + a/2||^2 + ||q_R alpha + b/2||^2 - 1/8   (a, b in {0, 1}),
channels j, k (diagonal entries) -> min(e00, e11), channels 1, i (off-diagonal) -> min(e01, e10), independent of Re(tau)
and of the line's offset p2.
FIREWALL: the inter-sector exponent (dominant down minus dominant up), which fixes the order of magnitude of a held-out
target, is NEVER computed or printed here.  Printed: per sector, each channel's exponent RELATIVE to that sector's own
dominant channel (rule and numeric), the within-sector block gap Delta E, and a PASS/FAIL for the absolute exponents
(rule vs numeric) without their values."""
import math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
B = Z.mods()["B"]
SECT = [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]

def dzf(x):
    x = x - (x.numerator // x.denominator); return min(x, 1 - x)
def rule_exact(alpha, ql, qr):
    ax, ay = ql * alpha, qr * alpha
    e = {(a, b): dzf(ax + F(a, 2)) ** 2 + dzf(ay + F(b, 2)) ** 2 - F(1, 8) for a in (0, 1) for b in (0, 1)}
    d = min(e[(0, 0)], e[(1, 1)]); o = min(e[(0, 1)], e[(1, 0)])
    return {"1": o, "i": o, "j": d, "k": d}
def numeric(alpha, p2, ql, qr, x, y1, y2):
    out = {}
    Rs = []
    for y in (y1, y2):
        t = complex(x, y); w = B.line_w(float(alpha), p2, t); xx, yy = B.sector_twists(w, t, ql, qr); Rs.append(B.residues(xx, yy, t))
    m1 = max(abs(v) for v in Rs[0].values()); m2 = max(abs(v) for v in Rs[1].values())
    for s in B.UNITS:
        a1, a2 = abs(Rs[0][s]), abs(Rs[1][s])
        if a1 < 1e-9 * m1 and a2 < 1e-9 * m2: out[s] = None          # vanishes identically (to precision) on this line
        else: out[s] = -(math.log(a2) - math.log(a1)) / (2 * math.pi * (y2 - y1))
    return out

worst_abs = 0.0; rows = 0; fails = []
for alpha in (F(2, 5), F(1, 5)):
    for p2 in (0.0, 0.1, 0.2, 0.3, 0.137):
        for x in (0.13, 0.41):
            for sn, ql, qr in SECT:
                R = rule_exact(alpha, ql, qr); N = numeric(alpha, p2, ql, qr, x, 14.0, 20.0)
                Edom = min(R.values()); Ndom = min(v for v in N.values() if v is not None)
                rel_rule = {s: R[s] - Edom for s in R}
                rel_num = {s: (round(N[s] - Ndom, 4) if N[s] is not None else "zero") for s in N}
                offs = {s: (round(N[s] - float(R[s]), 4) if N[s] is not None else "zero") for s in N}
                dev = max(abs(float(R[s]) - N[s]) for s in N if N[s] is not None)
                worst_abs = max(worst_abs, dev); rows += 1
                if dev > 2e-3: fails.append((str(alpha), p2, x, sn, round(dev, 4)))
                gap = sorted(set(rel_rule.values()))
                dE = gap[1] if len(gap) > 1 else F(0)
                if x == 0.13:
                    print(f"alpha={alpha} p2={p2} {sn:6s} rule rel(1,i,j,k)=({rel_rule['1']},{rel_rule['i']},{rel_rule['j']},{rel_rule['k']}) "
                          f"num rel=({rel_num['1']},{rel_num['i']},{rel_num['j']},{rel_num['k']})  within-sector gap Delta E = {dE}"
                          f"  dominant block = {'diag (j,k)' if R['j'] < R['1'] else 'offdiag (1,i)' if R['1'] < R['j'] else 'tie'}  abs-match {'PASS' if dev < 2e-3 else 'FAIL'}  num-minus-rule per channel {offs}")
print("rows", rows, " absolute exponents rule vs numeric: worst |dev| =", round(worst_abs, 5), " (values not printed)")
print("FAIL rows (absolute exponent off by > 2e-3):", fails if fails else "none")
