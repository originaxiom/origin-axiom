"""B2012, added at Review 87 (2026-11-26; a reader asked for the plane computation behind N1 to be checked by machine): for
projections P (onto C-invariant functions) and E = (1 + S)/2 in general position at angle theta, on their plane
T4 = 3(SP + PS) - 2S has eigenvalues 3 cos 2theta +- 1; on the four intersections it is 4, -4, -2, 2 (sympy, exact).
    python3 -B two_subspace.py > two_subspace_run.txt"""
import sympy as sp
th = sp.Symbol("theta", real=True)
c, s = sp.cos(th), sp.sin(th)
P = sp.Matrix([[1, 0], [0, 0]]); E = sp.Matrix([[c * c, c * s], [c * s, s * s]])
S = 2 * E - sp.eye(2)
T = (3 * (S * P + P * S) - 2 * S).applyfunc(sp.simplify)
ev = [sp.simplify(sp.trigsimp(e)) for e in T.eigenvals()]
print("on the plane: T4 =", T.tolist())
print("its eigenvalues:", ev, "; equal to 3 cos 2theta +- 1:", sorted(sp.simplify(e - 3 * sp.cos(2 * th)) for e in ev) == [-1, 1])
for p_, e_ in ((1, 1), (1, 0), (0, 1), (0, 0)):
    Sv = 2 * e_ - 1
    print("on ran P^%d cap ran E^%d (P = %d, E = %d): T4 = %d" % (p_, e_, p_, e_, 3 * (Sv * p_ + p_ * Sv) - 2 * Sv))
