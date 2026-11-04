"""P-638's planted relations, re-derived by main from B1728's charge-shift law and checked through the card's instrument:
(1) M_nu ∝ M_e on lines whose order divides 6 (right charges 0 and 6); (2) M_nu ∝ M_u and M_e ∝ M_d on lines whose order
divides 4 (both charges shifted by 4); (3) hence, with nu read like up (I-35: S~), U_PMNS = U_e^L† U_nu^L = V_CKM† on order-4
lines. Deviations only; the control lines (order 5) must break (1) and (2)."""
import pathlib, sys, math
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from card_instrument import yukawas
def order(a, b): return math.lcm(F(a).denominator, F(b).denominator)
def prop(X, Y):
    c = np.vdot(Y.ravel(), X.ravel()) / np.vdot(Y.ravel(), Y.ravel()); return float(np.max(np.abs(X - c * Y)) / np.max(np.abs(X)))
def left(Ym): return np.linalg.svd(Ym)[0][:, ::-1]           # light to heavy, as B1726's CKM
lines = [(F(a, n), F(b, n)) for n in (2, 3, 4, 5, 6) for a in range(n) for b in range(n) if (a, b) != (0, 0)]
lines = sorted({(x, y) for x, y in lines if order(x, y) in (2, 3, 4, 5, 6)})
res = {}
for (re_t, im_t) in ((0.31, 2.9), (0.12, 3.2)):
    for (a, b) in lines:
        N = order(a, b)
        Y = yukawas(re_t, im_t, float(a), float(b), "L_max", ("up", "down", "lep", "nu"))
        r1 = prop(Y[("nu", "St")], Y[("lep", "St")])     # same reading on both: the M's proportionality shows through Y
        r2 = max(prop(Y[("nu", "St")], Y[("up", "St")]), prop(Y[("lep", "S")], Y[("down", "S")]))
        k = "order %d" % N; e = res.setdefault(k, [0.0, 0.0, 0.0, 9.0, 9.0, 0])
        if 6 % N == 0: e[0] = max(e[0], r1)
        else: e[3] = min(e[3], r1)
        if 4 % N == 0:
            e[1] = max(e[1], r2)
            V = left(Y[("up", "St")]).conj().T @ left(Y[("down", "S")])
            P = left(Y[("lep", "S")]).conj().T @ left(Y[("nu", "St")])
            e[2] = max(e[2], float(np.max(np.abs(np.abs(P) - np.abs(V.conj().T)))))
        else: e[4] = min(e[4], r2)
        e[5] += 1
for k in sorted(res):
    e = res[k]; N = int(k.split()[1])
    print("%s (%d line-points): (1) M_nu∝M_e %s ; (2) M_nu∝M_u, M_e∝M_d %s ; (3) |U_PMNS| = |V_CKM^†| %s" % (k, e[5],
          ("holds, max dev %.1e" % e[0]) if 6 % N == 0 else ("breaks as it should, min dev %.2f" % e[3]),
          ("holds, max dev %.1e" % e[1]) if 4 % N == 0 else ("breaks as it should, min dev %.2f" % e[4]),
          ("holds, max dev %.1e" % e[2]) if 4 % N == 0 else "n/a"))
