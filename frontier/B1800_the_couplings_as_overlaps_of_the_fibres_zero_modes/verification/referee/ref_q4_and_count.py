"""Referee B1800, Q4 and (c).
Q4: with hypercharge Wilson lines (a field of 6Y charge q at boundary phases (c + q w_a, c_b + q w_b)), does an overlap
depend on (q_L - q_R) w only, or also on the sum (q_L + q_R) w (the Higgs's sector)?  Computed by quadrature (own
code), the Higgs placed at the summed (unreduced) phases, for sectors with equal difference and different sums.
(c): the diagonal sector (0,0) - how many independent Higgs components enter the three diagonal entries?
    python3 -B ref_q4_and_count.py"""
import math
import numpy as np
from ref_overlaps import mode, gl_grid, inner, th

def overlap(t, ap, aq, z, dA):
    """<psi_p psi_q, chi_k>, chi at the unreduced sum (a_p + a_q); returns (Y_0, Y_1)."""
    f = lambda M, j, c: mode(M, j, c[0], c[1], z, t)
    nrm = lambda g: g/math.sqrt(inner(g, g, dA).real)
    pp, qq = nrm(f(1, 0, ap)), nrm(f(1, 0, aq))
    s = (ap[0] + aq[0], ap[1] + aq[1])
    return [inner(pp*qq, nrm(f(2, k, s)), dA) for k in (0, 1)]

def periodic(t, ap, aq, s, k):
    rng = np.random.default_rng(3); zz = rng.random(4) + t*rng.random(4)
    F = lambda w: mode(1, 0, *ap, w, t)*mode(1, 0, *aq, w, t)*np.conj(mode(2, k, *s, w, t))
    return max(np.max(np.abs(F(zz + sh) - F(zz))/np.abs(F(zz))) for sh in (1, t))

t = complex(0.23, 1.13); z, dA = gl_grid(t, 80)
w = (0.071, 0.043)                      # a generic hypercharge Wilson line (boundary phases per unit 6Y charge)
c3, c2 = (0.0, 0.0), (0.5, 0.0)        # a generation pair: L in theta3's sector, R in theta2's
print("tau", t, " w =", w)
rows = [("down (1, 2): diff -1, sum 3", 1, 2), ("fictitious (-1, 0): diff -1, sum -1", -1, 0),
        ("fictitious (3, 4): diff -1, sum 7", 3, 4), ("up (1, -4): diff 5, sum -3", 1, -4),
        ("fictitious (6, 1): diff 5, sum 7", 6, 1), ("leptons (-3, 6): diff -9, sum 3", -3, 6)]
for name, qL, qR in rows:
    ap = (c3[0] + qL*w[0], c3[1] + qL*w[1]); aq = (c2[0] + qR*w[0], c2[1] + qR*w[1])
    Y = overlap(t, ap, aq, z, dA)
    da, db = ap[0] - aq[0], ap[1] - aq[1]
    pred = [t.imag**-0.25*th((da + m)/2, db, 0j, 2*t)[0] for m in (0, 1)]
    print("  %-38s Y0 %+.10f%+.10fi  Y1 %+.10f%+.10fi | vs K*theta[(da+m)/2, db](0,2tau): %.1e" % (
        name, Y[0].real, Y[0].imag, Y[1].real, Y[1].imag, max(abs(Y[m] - pred[m]) for m in (0, 1))))
# the Higgs NOT at the matter's summed phase (e.g. the Higgs's own line held where the sum is not): integrand not periodic
ap = (c3[0] + 1*w[0], c3[1] + 1*w[1]); aq = (c2[0] + 2*w[0], c2[1] + 2*w[1])
print("  integrand periodicity, Higgs at the sum: %.1e; Higgs at the sum + 0.1 w: %.1e" % (
    periodic(t, ap, aq, (ap[0] + aq[0], ap[1] + aq[1]), 0), periodic(t, ap, aq, (ap[0] + aq[0] + 0.1*w[0], ap[1] + aq[1] + 0.1*w[1]), 0)))
# the Higgs at the sum REDUCED mod 1 in a: relabels the two modes (k <-> m) and the phase; same set of moduli
ap = (0.5 + 0.3, 0.0); aq = (0.5 + 0.4, 0.1)
Yu = overlap(t, ap, aq, z, dA)
f = lambda M, j, c: mode(M, j, c[0], c[1], z, t); nrm = lambda g: g/math.sqrt(inner(g, g, dA).real)
s_red = ((ap[0] + aq[0]) % 1, (ap[1] + aq[1]) % 1)
Yr = [inner(nrm(f(1, 0, ap))*nrm(f(1, 0, aq)), nrm(f(2, k, s_red)), dA) for k in (0, 1)]
print("  sum a = 1.7: unreduced |Y| = (%.10f, %.10f); reduced to 0.7 |Y| = (%.10f, %.10f)" % (abs(Yu[0]), abs(Yu[1]), abs(Yr[0]), abs(Yr[1])))

# (c) the diagonal sector: Y_pp = h0 A_p + h1 B_p; rank of the 3 x 2 map
from ref_overlaps import overlaps
Y, *_ = overlaps(t)
M = np.array([[Y[(p, p, 0)], Y[(p, p, 1)]] for p in ("3", "2", "4")])
sv = np.linalg.svd(M, compute_uv=False)
print("(c) diagonal entries as a map of the sector-(0,0) Higgs (h0, h1): rows 33, 22, 44 =\n", np.round(M, 8), "\n   singular values", sv, "-> rank", int(np.sum(sv > 1e-10*sv[0])))
print("ref_q4_and_count exit 0")
