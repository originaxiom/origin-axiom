#!/usr/bin/env python3
"""The same with the determinant-one line: W = [[A, c], [0, L]], L = det(A)^-1 = (nu^-4, lambda^-4), which is non-trivial on the
fibre when nu^4 != 1 (the seat's case (b)).  W = L (x) [[A/L, c'], [0, 1]] with c' a cocycle of A/L."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import tower_own as to
jo, ix = to.jo, to.ix
from mpmath import mp, mpf, mpc, sqrt, exp, pi, nstr, inverse
mp.dps = 60
def count(q, n, nu, lam, label):
    L = (nu[0] ** -4, nu[1] ** -4, lam ** -4); out = []
    Phi, h, T = to.level(q, n, (nu[0] / L[0], nu[1] / L[1]), lam / L[2])            # the module A/L
    for name, (P, hh, TT), LL in (("W1", (Phi, h, T), L), ("W1[A*]", to.dual(Phi, h, T), tuple(1 / x for x in L))):
        reps, ext = to.cocycles(P, hh, TT)
        if not reps: out.append("%s: h1(A/L) = 0" % name); continue
        hw, Tw = ext([reps[0][i] for i in range(12)])
        hw = {1: LL[0] * hw[1], 2: LL[1] * hw[2]}; Tw = LL[2] * Tw
        I, a, b = ix.index(P, hw, Tw)
        out.append("%s: h1(A/L) = %d, index %+d (h1 %d/%d, interior %d/%d, kept %s dropped %s)" % (name, len(reps), I, a["h1"], b["h1"], a["interior"], b["interior"], nstr(a["gaps"][1][0], 2), nstr(a["gaps"][1][1], 2)))
    print("%-52s %s" % (label, " | ".join(out)), flush=True)
if __name__ == "__main__":
    phi = (1 + sqrt(mpf(5))) / 2; w = exp(2j * pi / 3); s2 = sqrt(mpf(2))
    count(17 + 12 * s2, 1, (1, 1), mpc(-1), "level 1 (B1509), trivial line")
    for q in (phi ** 4, phi ** -4):
        for nu in ((w, 1), (1, w), (w, w), (w, w ** 2), (w ** 2, 1), (1, w ** 2), (w ** 2, w ** 2), (w ** 2, w)):
            count(q, 4, nu, mpc(1), "level 4, nu = (%s, %s), q = %s" % (nstr(nu[0], 3), nstr(nu[1], 3), nstr(q, 6)))
    count(mpf(2), 4, (w, 1), mpc(1), "level 4, nu = (w, 1), q = 2 (control)")
