"""S302 check of the lane's Theorem 68, value-free parts only, on MAIN's code:
(a) the planted relations (B1835 sec. 1b) at the lane's own test points: slope 0, offset 1/N (w = p1 tau - p2 with
    (p1, p2) = (0, 1/N), i.e. B1726's (a, b) = (0, -1/N)), N = 2..6, through B1835's card_instrument (DR, readings S, S~,
    L_max), at main's two control tau; deviations only. No order-10 line is touched; no neutrino output is printed.
(b) the Dirac neutrino (-3, 0) channel exponents on alpha = 2/5 from the channel-exponent law (structure, as B1835 sec. 2
    already records), exact; and its within-sector channel-class gap."""
import math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1835_u_e_and_the_pmns/verification"))
from card_instrument import yukawas

def prop(X, Y):
    c = np.vdot(Y.ravel(), X.ravel()) / np.vdot(Y.ravel(), Y.ravel()); return float(np.max(np.abs(X - c * Y)) / np.max(np.abs(X)))
def left(Ym): return np.linalg.svd(Ym)[0][:, ::-1]
for (re_t, im_t) in ((0.31, 2.9), (0.12, 3.2)):
    for N in (2, 3, 4, 5, 6):
        a, b = 0.0, float(F(-1, N) % 1)
        Y = yukawas(re_t, im_t, a, b, "L_max", ("up", "down", "lep", "nu"))
        r1 = prop(Y[("nu", "St")], Y[("lep", "St")])
        r2 = max(prop(Y[("nu", "St")], Y[("up", "St")]), prop(Y[("lep", "S")], Y[("down", "S")]))
        line = "tau=(%.2f,%.1f) N=%d: (1) nu~e %s ; (2) nu~u, e~d %s" % (re_t, im_t, N,
               ("holds %.0e" % r1) if 6 % N == 0 else ("breaks %.2f" % r1), ("holds %.0e" % r2) if 4 % N == 0 else ("breaks %.2f" % r2))
        if 4 % N == 0:
            V = left(Y[("up", "St")]).conj().T @ left(Y[("down", "S")]); P = left(Y[("lep", "S")]).conj().T @ left(Y[("nu", "St")])
            line += " ; (3) ||U_PMNS| - |V_CKM^dag|| max %.0e" % float(np.max(np.abs(np.abs(P) - np.abs(V.conj().T))))
        print(line)

def nn(x):
    x = x - (x.numerator // x.denominator); return min(x, 1 - x)
al = F(2, 5); ql, qr = -3, 0
e = {(i, j): nn(ql * al + F(i, 2)) ** 2 + nn(qr * al + F(j, 2)) ** 2 - F(1, 8) for i in (0, 1) for j in (0, 1)}
print("Dirac nu (-3,0) on 2/5: e00 %s e11 %s e01 %s e10 %s ; channel-class gap %s" % (
    float(e[0, 0]), float(e[1, 1]), float(e[0, 1]), float(e[1, 0]), abs(min(e[0, 0], e[1, 1]) - min(e[0, 1], e[1, 0]))))
