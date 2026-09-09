#!/usr/bin/env python3
"""B1352 stage A' -- WHICH FAMILY THE LOCUS POINTS LIE ON.  A point of the subregular sl2 family (rho = iota_sub o rho_SL2,
27 = V13 + V9 + V5) has rho(a) with eigenvalues {s^k : k = -6..6} u {s^k : k = -4..4} u {s^k : k = -2..2} for one s
(the exponents of the three odd-dimensional blocks); three of them are s^0 = 1 -- the three cusp-fixed vectors that the
whole family carries.  Test: read the 27 eigenvalues of A (and of B) at each banked point, fit s from the eigenvalue of
largest |log|, and report the integer exponents and the largest misfit.  The V10 points of B1350 are the control (they
should NOT fit).  Usage: python3 locus_point_is_sl2.py [points.json ...]"""
import sys, os, json
import mpmath as mp
mp.mp.dps = 110
HERE = os.path.dirname(os.path.abspath(__file__))
paths = sys.argv[1:] or [os.path.join(HERE, "fixed_locus_points.json"),
                         os.path.join(HERE, "..", "..", "B1350_the_v10_direction", "verification", "v10_direction_points.json")]
PATTERN = sorted(list(range(-6, 7)) + list(range(-4, 5)) + list(range(-2, 3)))
def load(path):
    d = json.load(open(path))
    for name, v in d.items():
        mats = {}
        for g in ("1", "2"):
            mats[int(g)] = mp.matrix([[mp.mpc(mp.mpf(re), mp.mpf(im)) for (re, im) in row] for row in v[g]])
        yield name, mats
def fit(M, label):
    ev = mp.eig(M, left=False, right=False)
    logs = [mp.log(z) for z in ev]                      # all eigenvalues are near 1 (the points sit ~1e-6 from rho_0): principal log is safe
    big = max(logs, key=lambda z: abs(z))
    if abs(big) < mp.mpf('1e-40'):
        print(f"      {label}: all eigenvalues 1 to 1e-40 (unipotent)"); return
    ls = big / 6
    ks = [l / ls for l in logs]
    kint = [int(mp.nint(k.real)) for k in ks]
    mis = max(abs(k - ki) for k, ki in zip(ks, kint))
    print(f"      {label}: s = exp({mp.nstr(ls, 8)}); exponents {sorted(kint)}")
    print(f"        matches the sl2 pattern {'YES' if sorted(kint) == PATTERN else 'NO'}; largest misfit of an exponent from an integer: {mp.nstr(mis, 3)}; eigenvalues equal to 1 (|log| < 1e-40): {sum(1 for l in logs if abs(l) < mp.mpf('1e-40'))}")
for path in paths:
    print(f"== {os.path.relpath(path, HERE)}")
    for name, mats in load(path):
        print(f"    {name}")
        fit(mats[1], "rho(a)"); fit(mats[2], "rho(b)")
