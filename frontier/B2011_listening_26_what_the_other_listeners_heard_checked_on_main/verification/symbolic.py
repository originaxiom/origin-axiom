"""B2011, B2 and B4 (main, 2026-11-26; data-free; sympy, exact).
B2: B2000's covariant linearisation S6 = sum_k C^k (J_L + J_R) C^-k at a general point (x, y, z), read in C's charge basis;
the average of its neutral and charged entries over the three cyclic rotations of the point; their ratio; its values on
omega's tree and its limit.
B4: (LR)^3 - id for both orders of composition (L after R, and R after L): the lowest total degree present and that part.
    python3 -B symbolic.py > symbolic_run.txt"""
import sympy as sp
x, y, z = sp.symbols("x y z")
L = (x, z, x * z - y); R = (z, y, y * z - x)
J = lambda F: sp.Matrix(F).jacobian([x, y, z])
C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
# B2011 disclosure: the first run wrote w = exp(2 pi i/3); sympy left (-1)^(1/3), (-1)^(2/3) unsimplified and two comparisons printed
# False (kept as symbolic_run_first_unsimplified.txt). w is now written in radicals and every entry is expanded.
w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
U = sp.Matrix.hstack(*[sp.Matrix([1, w ** q, w ** (2 * q)]) / sp.sqrt(3) for q in range(3)])
S2 = J(L) + J(R)
S6 = sum((C ** k * S2 * C ** (-k) for k in range(3)), sp.zeros(3, 3))
D = (U.H * S6 * U).applyfunc(lambda e: sp.simplify(sp.expand(e)))
diag = [sp.expand(sp.simplify(D[i, i])) for i in range(3)]
off = [sp.simplify(D[i, j]) for i in range(3) for j in range(3) if i != j]
print("B2: S6 in the charge basis: diagonal (q = 0, 1, 2) %s; off-diagonal all zero: %s" % (diag, all(o == 0 for o in off)))
rot = lambda e: [e, e.subs({x: y, y: z, z: x}, simultaneous=True), e.subs({x: z, y: x, z: y}, simultaneous=True)]
n_avg = sp.expand(sum(rot(diag[0])) / 3); c_avg = sp.expand(sum(rot(diag[1])) / 3)
s = sp.Symbol("s")
ratio = sp.simplify(n_avg / c_avg)
print("    averages over the three rotations: neutral %s, charged %s; ratio %s; equals (4s + 6)/(s + 6) with s = x + y + z: %s" % (
    n_avg, c_avg, ratio, sp.simplify(ratio - (4 * (x + y + z) + 6) / ((x + y + z) + 6)) == 0))
for node in ((0, 0, 0), (3, 3, 3), (3, 3, 6), (3, 6, 15), (3, 15, 39), (6, 15, 87), (15, 39, 582)):
    sub = dict(zip((x, y, z), node))
    print("    node %s: ratio %s; on the Markov surface x^2 + y^2 + z^2 = xyz: %s" % (node, sp.nsimplify(ratio.subs(sub)), node[0] ** 2 + node[1] ** 2 + node[2] ** 2 == node[0] * node[1] * node[2]))
print("    limit as s -> infinity: %s" % sp.limit((4 * s + 6) / (s + 6), s, sp.oo))


def compose(F, G):   # F after G
    return tuple(sp.expand(e.subs({x: G[0], y: G[1], z: G[2]}, simultaneous=True)) for e in F)


for name, A in (("L after R", compose(L, R)), ("R after L", compose(R, L))):
    A3 = compose(A, compose(A, A))
    diff = [sp.Poly(sp.expand(a - v), x, y, z) for a, v in zip(A3, (x, y, z))]
    low = min(min(sum(m) for m in d.monoms()) for d in diff if not d.is_zero)
    part = [sp.expand(sum(c * x ** m[0] * y ** m[1] * z ** m[2] for m, c in d.terms() if sum(m) == low)) for d in diff]
    print("B4 (%s)^3 - id: lowest degree %d; that part %s; equals (x(z^2 - y^2), y(x^2 - z^2), z(y^2 - x^2)): %s; its negative: %s" % (
        name, low, part, part == [sp.expand(x * (z ** 2 - y ** 2)), sp.expand(y * (x ** 2 - z ** 2)), sp.expand(z * (y ** 2 - x ** 2))],
        part == [sp.expand(-x * (z ** 2 - y ** 2)), sp.expand(-y * (x ** 2 - z ** 2)), sp.expand(-z * (y ** 2 - x ** 2))]))
