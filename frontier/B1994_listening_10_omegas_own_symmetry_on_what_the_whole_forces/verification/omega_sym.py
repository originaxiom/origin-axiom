"""B1994 (main, 2026-11-25; data-free): omega's own symmetry. W1: words in L, R, L^-1, R^-1 up to length 6 whose trace map fixes
(3, 3, 3); W2: a generator's linear part at the common point (the cube group), order, axis, eigenvalues on the triplet; W3: its
action on the cube's orbits and on the four sign patterns of the integer readings. Exact (sympy).
    python3 -B omega_sym.py > omega_sym_run.txt"""
import sympy as sp
from itertools import product
X, Y, Z = sp.symbols("X Y Z")
M = {"L": (X, Z, X * Z - Y), "R": (Z, Y, Y * Z - X), "l": (X, X * Y - Z, Y), "r": (X * Y - Z, Y, X)}
def comp(w):
    v = (X, Y, Z)
    for c in w:
        f = M[c]; v = tuple(sp.expand(e.subs({X: v[0], Y: v[1], Z: v[2]}, simultaneous=True)) for e in f)
    return v
def at(v, p): return tuple(e.subs({X: p[0], Y: p[1], Z: p[2]}) for e in v)
def reduced(w):
    for a, b in (("L", "l"), ("l", "L"), ("R", "r"), ("r", "R")):
        if a + b in w: return False
    return True
fix = []
for n in range(1, 7):
    for w in product("LRlr", repeat=n):
        w = "".join(w)
        if not reduced(w): continue
        v = comp(w)
        if at(v, (3, 3, 3)) == (3, 3, 3): fix.append((w, v))
print("W1: reduced words up to length 6 whose trace map fixes (3, 3, 3): %d; the shortest: %s" % (len(fix), [w for w, _ in fix[:6]]))
if fix:
    w, v = fix[0]
    J = sp.Matrix([[sp.diff(e, s).subs({X: 0, Y: 0, Z: 0}) for s in (X, Y, Z)] for e in v])
    k = next(k for k in range(1, 13) if J ** k == sp.eye(3))
    ev = J.eigenvals()
    axis = J.eigenvects()
    print("W2: the generator %s: its trace map acts on the readings as %s" % (w, v))
    print("W2: its linear part at the common point %s; order %d; eigenvalues on the triplet %s; fixed axis %s" % (
        J.tolist(), k, ev, [list(vec[2][0]) for vec in axis if vec[0] == 1]))
    print("W2: acting on (3, 3, 3)'s neighbours: w(3, 3, 6) = %s; order of w on the readings (smallest k with w^k = id on a test point): %s" % (
        at(v, (3, 3, 6)), next((kk for kk in range(1, 13) if (lambda p: [p := at(v, p) for _ in range(kk)][-1])((3, 3, 6)) == (3, 3, 6)), None)))
    cube = {"faces": [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)],
            "vertices": [(a, b, c) for a in (1, -1) for b in (1, -1) for c in (1, -1)],
            "edges": [v_ for v_ in product((-1, 0, 1), repeat=3) if sum(1 for x in v_ if x) == 2]}
    for name, pts in cube.items():
        img = [tuple(int(x) for x in J * sp.Matrix(p)) for p in pts]
        fixed = [p for p, q in zip(pts, img) if p == q]
        print("W3: on the cube's %s: fixed %s" % (name, fixed))
    pats = {s: tuple(3 * c for c in s) for s in ((1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1))}
    sign = lambda p: tuple(1 if c > 0 else -1 for c in p)
    print("W3: on the four lifts (the sign pattern of w applied to each (+-3, +-3, +-3)): %s" % {s: sign(at(v, p)) for s, p in pats.items()})
