"""B1988 (main, 2026-11-25; data-free): the math decides PF5's loop. S1: the moves on the readings are the trace identity
(symbolic, SL(2)). S2: the readings fixed by L and R together over Q-bar (sympy) and over F_p, p <= 47. S3: with the swap P,
and with the central sign actions on the characters. S4: kappa at each fixed point. See ../CARD.md.
    python3 -B loop.py > loop_run.txt"""
import sympy as sp
a11, a12, a21, b11, b12, b21 = sp.symbols("a11 a12 a21 b11 b12 b21")
A = sp.Matrix([[a11, a12], [a21, (1 + a12 * a21) / a11]]); B = sp.Matrix([[b11, b12], [b21, (1 + b12 * b21) / b11]])
tr = lambda M: sp.simplify(M.trace())
x, y, z = tr(A), tr(B), tr(A * B)
lhs = tr(A * B * B.inv())  # tr(a): sanity
s1 = sp.simplify(tr(A * B) + tr(A * B.inv()) - x * y) == 0
print("S1: tr(ab) + tr(ab^-1) = tr a tr b on SL(2) (the trace identity the moves are made of): %s" % s1)
# L: a -> a, b -> ab (one convention) sends (tr a, tr b, tr ab) to (tr a, tr ab, tr a.ab) = (x, z, x z - y)
s1b = sp.simplify(tr(A * A * B) - (x * z - y)) == 0
print("S1: tr(a.ab) = x z - y, so L's new reading is a product of the current readings minus one: %s" % s1b)
X, Y, Z = sp.symbols("X Y Z")
Lm = (X, Z, X * Z - Y); Rm = (Z, Y, Y * Z - X); Pm = (Y, X, Z)
kap = X ** 2 + Y ** 2 + Z ** 2 - X * Y * Z - 2
sol = sp.solve([Lm[i] - (X, Y, Z)[i] for i in range(3)] + [Rm[i] - (X, Y, Z)[i] for i in range(3)], [X, Y, Z], dict=True)
pts = sorted({(s[X], s[Y], s[Z]) for s in sol})
print("S2: the readings fixed by L and R together over Q-bar: %s; kappa there: %s" % (pts, [kap.subs({X: p[0], Y: p[1], Z: p[2]}) for p in pts]))
signs = [(-X, -Y, Z), (-X, Y, -Z), (X, -Y, -Z)]
for s in signs: assert sp.expand(kap.subs({X: s[0], Y: s[1], Z: s[2]}, simultaneous=True) - kap) == 0
withP = [p for p in pts if (p[1], p[0], p[2]) == p]
withS = [p for p in pts if all(tuple(e.subs({X: p[0], Y: p[1], Z: p[2]}, simultaneous=True) for e in s) == p for s in signs)]
print("S3: fixed also by the swap P: %s; fixed also by the three central sign actions (which preserve kappa): %s" % (withP, withS))
ok = True
for p in [q for q in range(2, 48) if all(q % d for d in range(2, int(q ** 0.5) + 1))]:
    F = [(u, v, w) for u in range(p) for v in range(p) for w in range(p) if (u, w, (u * w - v) % p) == (u, v, w) and (w, v, (v * w - u) % p) == (u, v, w)]
    ok &= sorted(F) == sorted({(0, 0, 0), (2 % p, 2 % p, 2 % p)})
print("S2 over F_p, every prime p <= 47: the fixed points are exactly the common point and (2, 2, 2) mod p: %s" % ok)
print("S4: kappa = -2 at the common point (existence: kappa != 2) and kappa = 2 at (2, 2, 2), where cancelling completes (PF1)")
print("SUMMARY: the one reading every history returns, with existence, is the common point: %s" % (s1 and s1b and pts == [(0, 0, 0), (2, 2, 2)] and withS == [(0, 0, 0)] and ok))
