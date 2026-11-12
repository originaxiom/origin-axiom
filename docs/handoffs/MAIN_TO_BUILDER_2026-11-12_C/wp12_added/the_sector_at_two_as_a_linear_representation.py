#!/usr/bin/env python3
"""WP-1.2, statement E at the prime 2, after a second derivation made from the statements alone on another family of
model: is "a sector carried to itself" a statement about the scalar of [a, b], or about a linear representation?

THE POINT RAISED (read through main's mask; nothing of that session's code is run).  In the clock-and-shift
representation at p = 2, a^2 = b^2 = 1 and (ab)^2 = -1.  The tick (a, b) -> (ab, a) therefore gives a representation in
which the first generator squares to -1: it is not the one started from.  So "carried to itself at p = 2" holds for the
scalar of [a, b] and fails for the linear representation.
WHAT MAIN COMPUTES, exactly.  The two-dimensional representations of the free group with [a, b] = -1 and a^2, b^2 = +-1
are four, one for each pair of signs (a^2, b^2); (ab)^2 = -a^2 b^2.  Such a representation is fixed up to conjugacy by
its two signs (the algebra a^2 = alpha, b^2 = beta, ab = -ba has dimension 4 and one irreducible module).  For each of
the six moves and each of the four: the signs of the image, and for a representation carried to itself an explicit
invertible matrix that conjugates the one to the other.
HOW IT COULD FAIL: a move that does not keep [a, b] = -1 up to the sign found in statement B; no intertwiner where the
signs agree (planted: an intertwiner asked for where the signs differ must not exist)."""
import itertools, json, pathlib, sympy as sp
I2 = sp.eye(2); i = sp.I; sx = sp.Matrix([[0, 1], [1, 0]]); sz = sp.diag(1, -1)
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:300]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:230]) if detail else ""))
reps = {(e1, e2): ((1 if e1 == 1 else i) * sx, (1 if e2 == 1 else i) * sz) for e1 in (1, -1) for e2 in (1, -1)}
MOVES = {"a -> ab": lambda a, b: (a * b, b), "a -> ba": lambda a, b: (b * a, b), "b -> ba": lambda a, b: (a, b * a), "b -> ab": lambda a, b: (a, a * b),
         "the swap": lambda a, b: (b, a), "the tick": lambda a, b: (a * b, a)}
sign = lambda M: 1 if sp.simplify(M - I2) == sp.zeros(2) else (-1 if sp.simplify(M + I2) == sp.zeros(2) else None)
def intertwiner(a1, b1, a2, b2):
    x = sp.symbols("x0:4"); X = sp.Matrix(2, 2, x)
    sol = sp.solve(list(X * a1 - a2 * X) + list(X * b1 - b2 * X), x, dict=True)
    if not sol: return None
    Xs = X.subs(sol[0]); free = sorted(Xs.free_symbols, key=str)
    for vals in itertools.product((1, 0, 2, -1), repeat=len(free)):
        Y = Xs.subs(dict(zip(free, vals)))
        if sp.simplify(Y.det()) != 0: return Y
    return None
ok0 = all(sign(a * a) == e1 and sign(b * b) == e2 and sp.simplify(a * b * a.inv() * b.inv() + I2) == sp.zeros(2) and sign((a * b) ** 2) == -e1 * e2 for (e1, e2), (a, b) in reps.items())
check("the four representations: a^2 and b^2 are the two signs, [a, b] = -1, and (ab)^2 = -a^2 b^2", ok0)
table, fixed = {}, {}
for name, mv in MOVES.items():
    for key, (a, b) in reps.items():
        a2, b2 = mv(a, b); img = (sign(a2 * a2), sign(b2 * b2)); table[(name, key)] = img
        assert sp.simplify(a2 * b2 * a2.inv() * b2.inv() + I2) == sp.zeros(2)          # the scalar -1 is its own inverse
        if img == key:
            X = intertwiner(a, b, a2, b2); fixed[(name, key)] = X is not None
for name in MOVES: print("  %-9s %s" % (name, {str(k): str(table[(name, k)]) for k in reps}))
Q = (-1, -1); cs = (1, 1)
check("the scalar of [a, b] is kept by all six moves on all four (at p = 2 the scalar -1 is its own inverse)", True, "asserted in the loop, 24 cases")
check("the representation with a^2 = b^2 = -1 (the quaternion point of statement C) is carried to itself by all six moves, with an explicit invertible intertwiner each time", all(table[(n, Q)] == Q and fixed.get((n, Q)) for n in MOVES))
others = [k for k in reps if k != Q]
orbit = {cs}; fr = [cs]
while fr:
    k = fr.pop()
    for n in MOVES:
        j = table[(n, k)]
        if j not in orbit: orbit.add(j); fr.append(j)
check("the other three, clock-and-shift among them, are one orbit of the moves: each has exactly one of a^2, b^2, (ab)^2 equal to -1", orbit == set(others) and all([e1, e2, -e1 * e2].count(-1) == 1 for e1, e2 in others), sorted(orbit))
check("clock-and-shift (a^2 = b^2 = 1) is NOT carried to itself by the tick, nor by a -> ab; it is by the swap", table[("the tick", cs)] != cs and table[("a -> ab", cs)] != cs and table[("the swap", cs)] == cs and fixed.get(("the swap", cs)), {n: str(table[(n, cs)]) for n in MOVES})
a, b = reps[cs]; a2, b2 = MOVES["the tick"](a, b)
check("planted: no invertible matrix carries clock-and-shift to its image under the tick", intertwiner(a, b, a2, b2) is None)
json.dump({"signs of the image, by move and representation": {"%s | %s" % (n, k): str(v) for (n, k), v in table.items()}, "checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]},
          open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
