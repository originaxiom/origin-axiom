#!/usr/bin/env python3
"""Re-audit 6, the finding E5: the same computation at the cubic's other two roots.  A READ-OUT, WITH NO EXPECTATION.

Written after e5_independent.py ran (9 of 9), and because of what was read beside it.  Main's instrument, like the scan it
replaces, takes ONE point: s1 = x8 + t1 x16 with t1 = 13 x the smallest real root of the cubic.  The cubic has three real
roots, and the paper's skeleton (papers/structure_paper/SKELETON.md, (iv)) says of the same line: "no real nullity-14 point
exists there. This holds at all three Galois roots".

The dimensions 46, 30 and 12 are the same at conjugate roots.  Whether a wall is REAL is not: a wall value is an algebraic
number, and a conjugate of a purely imaginary number may be real.  So this script asks, at each of the three roots, where
the 16 finite walls of the line y = x14 + t x16 lie.  This seat did not know the answer when it wrote this file.

    python3 e5_other_roots.py --main DIR          (DIR: a scratch checkout of main)
"""
import sys, os, io, contextlib, time
from fractions import Fraction
import mpmath as mp

main_dir = os.path.abspath(sys.argv[sys.argv.index("--main") + 1])
B854 = os.path.join(main_dir, "frontier", "B854_centralizer_exact", "e6_centralizer.py")
CUBIC = [500716339200, -159667200, -28224, 1]
t0 = time.time()
g = {"__file__": B854, "__name__": "b854_for_the_reaudit"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(B854).read(), B854, "exec"), g)
DIM, N, br, hvec, evec, ROOTS, INV = g["DIM"], g["N"], g["br"], g["hvec"], g["evec"], g["ROOTS"], g["INV"]
basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]
NS = (8, 14, 16, 22)
mp.mp.dps = 60


def ad_mp(v):
    cols = [[Fraction(c) for c in br(v, basis[q])] for q in range(DIM)]
    return mp.matrix([[mp.mpf(cols[q][r].numerator) / mp.mpf(cols[q][r].denominator) for q in range(DIM)] for r in range(DIM)])


X = {n: ad_mp(INV[n]) for n in NS}
norm1 = lambda M: max(sum(abs(M[i, j]) for i in range(M.rows)) for j in range(M.cols))
coef = {8: mp.mpf(7) / 11, 14: mp.mpf(5) / 13, 16: mp.mpf(3) / 17, 22: mp.mpf(1)}
G = sum((coef[n] / norm1(X[n])) * X[n] for n in NS) + mp.mpf(9) / 7 * mp.eye(DIM)
E, V = mp.eig(G)
Vi = mp.inverse(V)
W = {}
worst = mp.mpf(0)
for n in NS:
    Dn = Vi * X[n] * V
    W[n] = [Dn[i, i] for i in range(DIM)]
    worst = max(worst, max(abs(Dn[i, j]) for i in range(DIM) for j in range(DIM) if i != j) / max(abs(d) for d in W[n]))
print("the four ad-matrices diagonalised together at 60 digits: largest off-diagonal part %s of the largest weight" % mp.nstr(worst, 3))
assert worst < mp.mpf(10) ** -30
TINY = mp.mpf(10) ** -30
big = {n: max(abs(w) for w in W[n]) for n in NS}
zero = lambda n, i: abs(W[n][i]) < TINY * big[n]
roots = sorted((r.real for r in mp.polyroots([mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=200)))
print("the cubic's three roots are real: %s" % ", ".join(mp.nstr(r, 15) for r in roots))
print()
for k, r in enumerate(roots, 1):
    tk = 13 * r
    s = [W[8][i] + tk * W[16][i] for i in range(DIM)]
    sbig = max(abs(x) for x in s)
    Z = [i for i in range(DIM) if abs(s[i]) < TINY * sbig]
    plane = [i for i in Z if zero(16, i)]
    generic = [i for i in plane if zero(14, i)]
    ts = [-W[14][i] / W[16][i] for i in Z if i not in plane]
    groups = {}
    for t in ts:
        kind = "REAL" if abs(t.imag) < TINY * abs(t) else ("purely imaginary" if abs(t.real) < TINY * abs(t) else "complex")
        key = (kind, mp.nstr(t.real, 12) if kind == "REAL" else (mp.nstr(t.imag, 12) + " i" if kind == "purely imaginary" else mp.nstr(t, 12)))
        groups[key] = groups.get(key, 0) + 1
    real_walls = sum(v for (kind, _), v in groups.items() if kind == "REAL")
    print("root %d, the point x8 + t x16 at t = %s%s" % (k, mp.nstr(tk, 15), "   (main's s1)" if k == 1 else ""))
    print("   weights that vanish there: %d; of them on x16: %d; on x14 and x16: %d; finite walls of the line y = x14 + t x16: %d" % (len(Z), len(plane), len(generic), len(ts)))
    for (kind, val), n in sorted(groups.items()):
        print("      %-17s t = %-22s %d weights, nullity %d" % (kind, val, n, len(generic) + n))
    print("   => on the real line: %s" % ("NO wall at a finite real t; the nullity is %d at every real point but pure x16" % len(generic) if real_walls == 0
                                          else "%d weights vanish at REAL finite t: the nullity rises above %d on the real line" % (real_walls, len(generic))))
    print()
print("(%.0f s)" % (time.time() - t0))
