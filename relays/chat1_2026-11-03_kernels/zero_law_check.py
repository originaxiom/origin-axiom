"""The web seat's check of the Re tau = 0 zero law in its kernels note (data-free; no measured value is read).

The law (from the pair expansion of W177's series): on a line where the summed twist has a_S = 1/4 (mod 1/2) and
4M odd, M = frac(1/2 - b_S/2), at Re tau = 0 the channel norms satisfy c_1 = c_i, c_j = c_k and
sigma_b = c_j + c_k - c_1 - c_i = 0, so B1788's det M -- main's D = sum_s c_s R_s^2 (B1716) -- vanishes at every Im tau.
For the quark sectors (|q_L + q_R| = 3) the condition is 12 p1 odd and 12 p2 odd (P-292's family); for the lepton
doublet pair LL (q_L = q_R = -3; R_1 = 0, so D = (c_j - c_k)(r00^2 + r11^2) + 2 r00 r11 (c_j + c_k - 2 c_i)) it is
24 p1 odd and 24 p2 odd (P-404's family).

It prints:
 (1) the census count (lines of order <= 12 up to w -> -w) meeting each condition, by order;
 (2) on every quark-condition line, at Re tau = 0 (Im tau 2.2 and 3.1): the largest |D| / sum |R_s|^2 in the up and
     down sectors, and the largest |c_1 - c_i|, |c_j - c_k|, |sigma_b|; then the same at Re tau = 0.13 (no zero
     expected); and the lepton sector's |D| / sum |R_s|^2 on those lines at both Re tau;
 (3) on every LL-condition line, the LL pair's |D| / sum |R_s|^2, |c_j - c_k| and |c_j + c_k - 2 c_i|, at Re tau = 0 and
     at Re tau = 0.13;
 (4) two controls at Re tau = 0: (1/12, 0) (the slope, 4M even) and (1/7, 1/12) (4M odd, not the slope).

Usage: python3 zero_law_check.py <main checkout>   (main at 354a4ea4d)
"""
import contextlib
import io
import pathlib
import sys
from collections import Counter
from fractions import Fraction as Fr

import numpy as np

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]
QUARKS = {"up": (1, -4), "down": (1, 2)}


def data(line, t, ql, qr):
    w = B.line_w(line[0], line[1], t); x, y = B.sector_twists(w, t, ql, qr)
    with contextlib.redirect_stdout(io.StringIO()):
        R = B.residues(x, y, t); c = B.cA(x, y, t, R)
    return R, c


def rel_D(R, c):
    return abs(B.D_of(c, R)) / B.nR2(R)


lines = {}
for N in range(1, 13):
    for a in range(N):
        for b in range(N):
            p = (Fr(a, N), Fr(b, N))
            if int(np.lcm(p[0].denominator, p[1].denominator)) > 12:
                continue
            lines[min(p, ((-p[0]) % 1, (-p[1]) % 1))] = True


def order(l):
    return int(np.lcm(l[0].denominator, l[1].denominator))


def odd_int(v):
    return v.denominator == 1 and v.numerator % 2 == 1


Q = sorted(l for l in lines if odd_int(12 * l[0]) and odd_int(12 * l[1]))
LL = sorted(l for l in lines if odd_int(24 * l[0]) and odd_int(24 * l[1]))
print("(1) census lines (order <= 12, up to w -> -w): %d" % len(lines))
print("    12 p1 odd and 12 p2 odd: %d lines, by order %s" % (len(Q), dict(sorted(Counter(order(l) for l in Q).items()))))
print("    24 p1 odd and 24 p2 odd: %d lines, by order %s: %s" % (len(LL), dict(sorted(Counter(order(l) for l in LL).items())),
                                                               ", ".join("(%s, %s)" % l for l in LL)))

print("(2) the quark sectors on the %d lines" % len(Q))
for re in (0.0, 0.13):
    worst = {"D": 0.0, "c1-ci": 0.0, "cj-ck": 0.0, "sigma_b": 0.0}; lep = 0.0; least = np.inf
    for l in Q:
        for im in (2.2, 3.1):
            t = complex(re, im)
            for sn, (ql, qr) in QUARKS.items():
                R, c = data(l, t, ql, qr)
                d = rel_D(R, c); worst["D"] = max(worst["D"], d); least = min(least, d)
                worst["c1-ci"] = max(worst["c1-ci"], abs(c["1"] - c["i"])); worst["cj-ck"] = max(worst["cj-ck"], abs(c["j"] - c["k"]))
                worst["sigma_b"] = max(worst["sigma_b"], abs(c["j"] + c["k"] - c["1"] - c["i"]))
            R, c = data(l, t, -3, 6); lep = max(lep, rel_D(R, c))
    print("    Re tau %.2f (Im tau 2.2, 3.1), up and down: max |D|/sum|R|^2 %.1e (least %.1e), max |c_1 - c_i| %.1e, "
          "|c_j - c_k| %.1e, |sigma_b| %.1e; leptons: max |D|/sum|R|^2 %.1e"
          % (re, worst["D"], least, worst["c1-ci"], worst["cj-ck"], worst["sigma_b"], lep))

print("(3) the LL pair (q_L = q_R = -3) on the %d lines" % len(LL))
for re in (0.0, 0.13):
    wd = wjk = wsum = 0.0; least = np.inf
    for l in LL:
        for im in (2.2, 3.1):
            R, c = data(l, complex(re, im), -3, -3)
            d = rel_D(R, c); wd = max(wd, d); least = min(least, d)
            wjk = max(wjk, abs(c["j"] - c["k"])); wsum = max(wsum, abs(c["j"] + c["k"] - 2 * c["i"]))
    print("    Re tau %.2f: max |D|/sum|R|^2 %.1e (least %.1e), max |c_j - c_k| %.1e, max |c_j + c_k - 2 c_i| %.1e"
          % (re, wd, least, wjk, wsum))

print("(4) controls at Re tau = 0, Im tau 2.2 (up and down)")
for l, why in (((Fr(1, 12), Fr(0)), "the slope, 4M even"), ((Fr(1, 7), Fr(1, 12)), "4M odd, not the slope")):
    out = []
    for sn, (ql, qr) in QUARKS.items():
        R, c = data(l, complex(0.0, 2.2), ql, qr)
        out.append("%s |D|/sum|R|^2 %.2e, c_1 - c_i %.1e, c_j - c_k %.1e, sigma_b %.2e"
                   % (sn, rel_D(R, c), c["1"] - c["i"], c["j"] - c["k"], c["j"] + c["k"] - c["1"] - c["i"]))
    print("    (%s, %s) (%s): %s" % (l[0], l[1], why, "; ".join(out)))
