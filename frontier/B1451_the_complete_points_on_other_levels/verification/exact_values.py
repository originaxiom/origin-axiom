#!/usr/bin/env python3
"""Exact identification at a complete point: the point is polished to 300 digits and the coordinates and sector
torsions are identified by PARI's algdep, accepted only when the polynomial is short against the precision.
Not part of the sealed run.   usage: exact_values.py <state> <k> <l0,l1> [beta0,beta1 ...]"""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import complete_points as cp
ce, mt = cp.ce, cp.mt
from mpmath import mp, mpf, mpc, nstr, exp, pi, matrix, zeros, lu_solve
from cypari import pari
DIG = 300
def polish(B, p):
    mp.dps = DIG + 30; h = mpf(10) ** (-(DIG // 2 + 20)); p = [mpc(c) for c in p]
    def F(p):
        q = ce.tracemap(B.Phi, p); return [q[i] - B.sig[i] * p[i] for i in range(3)] + [ce.kappa(p) + 2]
    for it in range(40):
        f0 = F(p); J = zeros(4, 3)
        for j in range(3):
            pp = list(p); pp[j] += h; f1 = F(pp)
            for i in range(4): J[i, j] = (f1[i] - f0[i]) / h
        d = lu_solve(J.H * J, -(J.H * matrix(f0))); p = [p[i] + d[i] for i in range(3)]
        if max(abs(d[i]) for i in range(3)) < mpf(10) ** (-(DIG + 10)): break
    assert max(abs(c) for c in F(p)) < mpf(10) ** (-DIG), "polish failed"
    return p
def S(zv, dig=DIG - 10):
    zv = mpc(zv); re = nstr(zv.real, dig) if abs(zv.real) > mpf(10) ** (-dig + 20) else "0"; im = nstr(zv.imag, dig) if abs(zv.imag) > mpf(10) ** (-dig + 20) else "0"
    return "(%s + (%s)*I)" % (re, im)
def alg(zv, degs=(2, 4, 8, 12, 16, 24, 32, 48)):
    """the minimal polynomial, or None: accepted when (degree + 1) * digits of the largest coefficient < 40% of the precision"""
    s = S(zv)
    for d in degs:
        pol = pari("algdep(%s, %d)" % (s, d)); big = max(abs(int(c)) for c in pari.Vec(pol))
        if (d + 1) * len(str(big)) < 0.4 * DIG and abs(complex(pari("subst(%s, x, %s)" % (pol, s)))) < 1e-200:
            fac = pari.factor(pol)[0]; best = min(fac, key=lambda f: abs(complex(pari("subst(%s, x, %s)" % (f, s)))))
            return str(best)
    return None
if __name__ == "__main__":
    pari.set_real_precision(DIG + 20); pari.allocatemem(2 * 10 ** 9)
    name, k = sys.argv[1], int(sys.argv[2]); l = tuple(int(x) for x in sys.argv[3].split(","))
    L = mt.Level(name, k); P = cp.Points(L); pt = P.cusp(l); assert pt[0] is not None, pt[4]
    B = pt[0]; p = polish(B, pt[1]); zz = exp(1j * pi / L.N); B.v = (zz ** l[0], zz ** l[1])      # the characters again, at the working precision
    g = ce.rep(p); T = ce.intertwiner(B.Phi, g, B.sig); z = exp(2j * pi / L.N)
    print("%s %d  l = %s  slope %s  (%s point, %d digits)" % (name, k, l, nstr(L.S[l], 10), pt[4]["kind"], DIG))
    for nm, c in zip("XYZ", p): print("   %s = %s   %s" % (nm, nstr(c, 20), alg(c)), flush=True)
    for arg in sys.argv[4:]:
        be = tuple(int(x) for x in arg.split(","))
        tau = ce.sector_torsion(B.Phi, g, T, B.v[0] * z ** be[0], B.v[1] * z ** be[1])[0]
        print("   beta = %s  torsion %s  |.| = %s   %s   |.|^2: %s" % (be, nstr(tau, 20), nstr(abs(tau), 15), alg(tau), alg(abs(tau) ** 2)), flush=True)
