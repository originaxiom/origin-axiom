"""Exact over Q(sqrt-3): conjugators of the two involutions on Riley's presentation, their determinants,
and whether the axis endpoints are cusp points (rational over Q(omega)) or not."""
import sympy as sp
w = sp.Rational(-1, 2) + sp.sqrt(3)*sp.I/2   # omega
x = sp.Matrix([[1, 1], [0, 1]]); y = sp.Matrix([[1, 0], [-w, 1]])
def ev(word, D):
    M = sp.eye(2)
    for ch in word: M = M * D[ch]
    return sp.simplify(M)
D = {'x': x, 'y': y, 'X': x.inv(), 'Y': y.inv()}
REL = 'xyXYxYXyxY'
assert sp.simplify(ev(REL, D) - sp.eye(2)) == sp.zeros(2)
def invw(s): return ''.join(c.swapcase() for c in reversed(s))
autos = {'sigma (strong inversion) x->X,y->Y': {'x': 'X', 'y': 'Y'},
         'iota (fiber -I) x->xyX, y->xYxyX': {'x': 'xyX', 'y': 'xYxyX'}}
g = sp.symbols('g0:4')
for name, mp in autos.items():
    def iw(word): return ''.join(mp[c] if c.islower() else invw(mp[c.lower()]) for c in word)
    assert sp.simplify(ev(iw(REL), D) - sp.eye(2)) == sp.zeros(2)
    E = sp.Matrix([[g[0], g[1]], [g[2], g[3]]])
    eqs = []
    for u in 'xy':
        eqs += list(sp.expand(E*ev(iw(u), D) - D[u]*E))
    sol = sp.solve(eqs, g, dict=True)
    assert len(sol) == 1
    Gm = sp.simplify(E.subs(sol[0]))
    free = [s for s in g if s not in sol[0]]
    Gm = sp.simplify(Gm.subs({free[0]: 1}))
    d = sp.simplify(Gm.det()); tr = sp.simplify(Gm.trace())
    # axis endpoints: fixed points of z -> (a z + b)/(c z + d): c z^2 + (d-a) z - b = 0
    a_, b_, c_, d_ = Gm
    z = sp.symbols('z'); roots = sp.solve(c_*z**2 + (d_ - a_)*z - b_, z)
    disc = sp.simplify((d_ - a_)**2 + 4*b_*c_)
    # is disc a square in Q(omega)?  minimal polynomial of sqrt(disc) over Q
    mp_ = sp.minimal_polynomial(sp.sqrt(disc), z)
    print(f"{name}\n   G = {Gm.tolist()}\n   det = {d}, trace = {tr}\n   axis discriminant = {disc}, minpoly of sqrt(disc) over Q: {mp_} (degree {sp.degree(mp_, z)})")
    print(f"   endpoints in Q(omega) (a cusp point => the fixed component is an ARC to the cusp): {sp.degree(mp_, z) <= 2 and sp.simplify(sp.sqrt(disc)).has(sp.I) or sp.degree(mp_, z) == 1}")
    print(f"   endpoints: {[sp.simplify(r) for r in roots]}")
