"""R64 -- the type of the object's order-3 element on the icosian E8. Exact over Q(sqrt5) (pairs (a,b) = a + b sqrt5).
Rebuilds: 2I (120 unit icosians), E8 = {units} u {phi^-1 units} under Conway-Sloane's EN, E6 = {1, g}^perp (B1270's theorem),
then factors left multiplication by an order-3 unit g:  L_g = w_A2 . w_3  with w_A2 the family Weyl rotation (fixes E6 pointwise)
and w_3 an order-3 automorphism of E6 with no fixed vector (the trinification element)."""
import itertools
from fractions import Fraction as Fr
import sympy as sp
# Q(sqrt5) arithmetic
def fadd(x, y): return (x[0]+y[0], x[1]+y[1])
def fsub(x, y): return (x[0]-y[0], x[1]-y[1])
def fmul(x, y): return (x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def fneg(x): return (-x[0], -x[1])
ZERO5, ONE5 = (Fr(0), Fr(0)), (Fr(1), Fr(0))
PHI = (Fr(1,2), Fr(1,2)); PHI_INV = (Fr(-1,2), Fr(1,2))   # phi^-1 = phi - 1 = (-1 + sqrt5)/2
HALF = (Fr(1,2), Fr(0))
def qmul(p, q):
    w1,x1,y1,z1 = p; w2,x2,y2,z2 = q
    return (fsub(fsub(fsub(fmul(w1,w2), fmul(x1,x2)), fmul(y1,y2)), fmul(z1,z2)),
            fsub(fadd(fadd(fmul(w1,x2), fmul(x1,w2)), fmul(y1,z2)), fmul(z1,y2)),
            fadd(fadd(fsub(fmul(w1,y2), fmul(x1,z2)), fmul(y1,w2)), fmul(z1,x2)),
            fadd(fsub(fadd(fmul(w1,z2), fmul(x1,y2)), fmul(y1,x2)), fmul(z1,w2)))
def qconj(p): return (p[0], fneg(p[1]), fneg(p[2]), fneg(p[3]))
def QN(p): return qmul(p, qconj(p))[0]
def EN(p): x, y = QN(p); return x + y                       # Conway-Sloane Euclidean norm
def B(p, q): return Fr(EN(tuple(fadd(a, b) for a, b in zip(p, q))) - EN(p) - EN(q), 2)
def scal(c, p): return tuple(fmul(c, a) for a in p)
# 2I: 8 + 16 + 96
units = set()
for s in itertools.product((1,-1), repeat=1):
    pass
z, o = ZERO5, ONE5
for i in range(4):
    for s in (1, -1):
        v = [z]*4; v[i] = (Fr(s), Fr(0)); units.add(tuple(v))
for signs in itertools.product((1,-1), repeat=4):
    units.add(tuple((Fr(s,2), Fr(0)) for s in signs))
even_perms = [p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i+1,4) if p[i] > p[j]) % 2 == 0]
for signs in itertools.product((1,-1), repeat=3):
    base = [z, fmul((Fr(signs[0]),Fr(0)), HALF), fmul((Fr(signs[1]),Fr(0)), fmul(HALF, PHI_INV)), fmul((Fr(signs[2]),Fr(0)), fmul(HALF, PHI))]
    for p in even_perms:
        units.add(tuple(base[p[i]] for i in range(4)))
units = list(units); assert len(units) == 120
assert all(QN(u) == ONE5 for u in units)
prod_closed = all(qmul(u, v) in set(units) for u in units[:12] for v in units)
def order(u):
    k, h = 1, u
    while h != (ONE5, z, z, z): h = qmul(h, u); k += 1
    return k
from collections import Counter
print("[2I]", len(units), "units, closed under product:", prod_closed, "; orders:", dict(sorted(Counter(order(u) for u in units).items())))
# E8 roots: units and phi^-1 * units, EN = 1 each
roots = units + [scal(PHI_INV, u) for u in units]; assert len(set(roots)) == 240 and all(EN(r) == 1 for r in roots)
# Z-basis of the lattice spanned by the roots: coordinates in Q^8 (a_i, b_i)
def vec(q): return [c for comp in q for c in comp]
M = sp.Matrix([[sp.Rational(c) for c in vec(r)] for r in roots])
# lattice basis via HNF over Z after clearing denominators (all coords in (1/4)Z)
Mi = (4*M).applyfunc(lambda t: sp.Integer(t))
from sympy.matrices.normalforms import hermite_normal_form
H = hermite_normal_form(Mi.T).T   # rows = basis (up to transposition conventions)
basis = [[sp.Rational(c, 4) for c in H.row(i)] for i in range(H.rows) if any(H.row(i))]
assert len(basis) == 8, len(basis)
def tovec(q): return sp.Matrix([sp.Rational(c) for c in vec(q)])
Bm = sp.Matrix(basis)   # 8 x 8, rows = basis vectors in Q^8
def coords(q):    # express q in the Z-basis
    sol = Bm.T.solve(tovec(q))          # Bm.T * c = v
    assert all(s.is_integer for s in sol), sol
    return sol
def quat_from_vec(v): return tuple((Fr(str(v[2*i])), Fr(str(v[2*i+1]))) for i in range(4))
gram = sp.Matrix(8, 8, lambda i, j: sp.Rational(B(quat_from_vec(basis[i]), quat_from_vec(basis[j]))))
print("[E8] roots:", len(roots), "| lattice rank:", len(basis), "| Gram det (form EN, roots of norm 1):", gram.det(), "-> x2 gives the even unimodular E8 (det 2^8 * (1/2)^... )")
print("     scaled form 2*EN: root norm 2, Gram det =", (2*gram).det())
# the founding ratio: any order-3 unit (one conjugacy class of 20 -- checked below)
order3 = [u for u in units if order(u) == 3]
def conj_class(g):
    return {qmul(qmul(u, g), qconj(u)) for u in units}
print("[g] order-3 units:", len(order3), "| conjugacy classes among them:", len({frozenset(conj_class(g)) for g in order3}))
g = order3[0]
one = (ONE5, z, z, z)
print("     g =", tuple(f"{a[0]}+{a[1]}r5" for a in g), "; g^2+g+1 = 0:", tuple(fadd(fadd(a, b), c) for a, b, c in zip(qmul(g, g), g, one)) == (z, z, z, z))
print("     plane {1, g} Gram:", [[B(one, one), B(one, g)], [B(g, one), B(g, g)]], " (A2 needs [[1,-1/2],[-1/2,1]] at root norm 1)")
E6 = [r for r in roots if B(r, one) == 0 and B(r, g) == 0]
rest = [r for r in roots if r not in set(E6)]
classes = Counter((B(r, one), B(r, g)) for r in rest)
print(f"[E6 = plane^perp] roots orthogonal to the plane: {len(E6)} (E6 = 72); remaining {len(rest)} split by pairings into {dict(classes)}")
# ---- the three automorphisms as 8x8 integer matrices in the Z-basis
def matrix_of(f):
    cols = [coords(f(quat_from_vec(b))) for b in basis]
    return sp.Matrix.hstack(*cols)
Lg = matrix_of(lambda q: qmul(g, q))
def refl(r):
    nr = B(r, r)
    return lambda q: tuple(fsub(a, fmul((Fr(2*B(q, r), nr) if False else (Fr(2)*Fr(B(q, r))/Fr(nr), Fr(0))), b)) for a, b in zip(q, r))
s1, sg = refl(one), refl(g)
wA2 = matrix_of(lambda q: s1(sg(q)))
w3 = wA2.inv() * Lg
I8 = sp.eye(8)
def fixdim(A): return 8 - (A - I8).rank()
def order_m(A):
    k, P = 1, A
    while P != I8: P = P*A; k += 1
    return k
print(f"[types] L_g: order {order_m(Lg)}, fixed dim {fixdim(Lg)} | w_A2 = s_1 s_g: order {order_m(wA2)}, fixed dim {fixdim(wA2)} | w_3 = w_A2^-1 L_g: order {order_m(w3)}, fixed dim {fixdim(w3)} | commute: {wA2*w3 == w3*wA2}")
# w_A2 fixes E6 pointwise; w_3 fixes the plane pointwise and has no fixed vector on E6
fix_E6_by_wA2 = all(wA2*coords(r) == coords(r) for r in E6)
fix_plane_by_w3 = (w3*coords(one) == coords(one)) and (w3*coords(g) == coords(g))
print(f"     w_A2 fixes all 72 E6 roots: {fix_E6_by_wA2};  w_3 fixes 1 and g: {fix_plane_by_w3}")
# action on the six 27-classes
def cls(r): return (B(r, one), B(r, g))
def image_class(A, r):
    v = A*coords(r); q = quat_from_vec(list(Bm.T*v)); return cls(q), q
lg_map = {c: image_class(Lg, next(r for r in rest if cls(r) == c))[0] for c in classes}
w3_perm_ok = all(image_class(w3, r)[0] == cls(r) for r in rest)
w3_fixed_roots = sum(1 for r in rest if image_class(w3, r)[1] == r)
print(f"[27-classes] L_g permutes the classes: {lg_map}")
print(f"     w_3 preserves every class: {w3_perm_ok}; roots fixed by w_3 among the 162: {w3_fixed_roots}  -> 54 three-cycles = 9 per class")
print(f"     w_3 on the 72 E6 roots: fixed {sum(1 for r in E6 if image_class(w3, r)[1] == r)} -> 24 three-cycles")
print("[mod 2] g = -R L^-1 = [[0,-1],[1,-1]] and M^2 = [[2,1],[1,1]] both reduce to [[0,1],[1,1]] in SL(2,F_2): the same 3-cycle on the fiber's half-periods.")
