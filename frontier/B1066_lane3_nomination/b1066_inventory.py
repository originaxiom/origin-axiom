"""B1066 Stage 1's relation inventory — the exact computation (reproduces
Appendix A's results; run from repo root, no arguments, no network)."""
import sympy as sp
from itertools import combinations
phi = (1 + sp.sqrt(5))/2
T = [sp.Integer(0), 1/(2*phi), sp.Rational(1,2), phi/2, sp.Integer(1)]
M = [sp.Integer(0), sp.Rational(1,4), 1/(4*phi), sp.Rational(1,2), 1/(2*phi), phi/4, phi/2, sp.Integer(1)]
L = [(1 - 1/sp.sqrt(5))/2, (1 + 1/sp.sqrt(5))/2, sp.Integer(1)]
S = lambda x: sp.simplify(sp.radsimp(x))
def inmenu(x, menu): return any(S(x - m) == 0 for m in menu)
half_T = [S(t/2) for t in T]
assert all(inmenu(m, T + half_T) for m in M), "M subset of T u T/2"
assert all(inmenu(x, M) for x in T + half_T), "T u T/2 subset of M"
sums1 = [c for menu in (T, M, L) for r in (2, 3)
         for c in combinations(sorted(set(map(S, menu)) - {sp.S.Zero}, key=str), r)
         if S(sum(c) - 1) == 0]
assert len(sums1) == 1 and S(sums1[0][0] + sums1[0][1] - 1) == 0, "unique sum-to-1 = the listener pair"
pyth = [c for menu in (T, M) for r in (2, 3)
        for c in combinations(sorted(set(map(S, menu)) - {sp.S.Zero}, key=str), r)
        if S(sum(x**2 for x in c) - 1) == 0]
assert len(set(tuple(sorted(map(str, c))) for c in pyth)) == 1, "unique Pythagorean triple"
trip = sorted(pyth[0], key=lambda v: float(v))
assert [S(trip[1]/trip[0]), S(trip[2]/trip[1])] == [S(phi), S(phi)], "phi-geometric"
a = sp.symbols('a', positive=True)
sol = sp.solve(a**2*(1 + phi**2 + phi**4) - 1, a)
assert S(sol[0] - 1/(2*phi)) == 0, "unit-norm phi-geometric row forced to the triple"
print("B1066 inventory: all Appendix-A identities verified exactly.")
