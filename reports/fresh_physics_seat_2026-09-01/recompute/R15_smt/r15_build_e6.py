#!/usr/bin/env python3
"""R15 blind recomputation, stage 1: my own e6 Chevalley construction + 2T charges.

Written BEFORE reading any arc solver (wall_search.py / measurement_ladder.py /
levi*/fmt* / the vendored module body). Inputs taken as committed DATA only:
  - E6 Cartan matrix (Bourbaki labels, chain 1-3-4-5-6, node 2 on 4).
  - Charges are the 2T-invariants t = x^5 y - x y^5, W = x^8 + 14 x^4 y^4 + y^8,
    embedded in the principal-sl2 blocks by x^{n-k} y^k |-> ((n-k)!/n!) f^k . v_n:
    g8 = W, g14 = t W, g16 = W^2, g22 = t W^2.
Everything exact (Fraction).  Output: pickled ad-matrices + charge vectors.
"""
import itertools, pickle, random, sys
from fractions import Fraction

import sympy as sp

random.seed(20260901)

# ---------------------------------------------------------------- roots of E6
# Bourbaki numbering, nodes 0..5 (= 1..6): chain 0-2-3-4-5, node 1 attached to 3.
EDGES = [(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)]
N = 6
A = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in EDGES:
    A[i][j] = A[j][i] = -1

def ip(a, b):
    """(a,b) with all roots length^2 = 2: a^T A b / ... simply-laced: (ai,aj)=A_ij."""
    return sum(a[i] * A[i][j] * b[j] for i in range(N) for j in range(N))

simple = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
roots = set(simple)
frontier = set(simple)
while frontier:
    new = set()
    for r in roots | new:
        pass
    for r in list(roots):
        for i in range(N):
            # reflect r in simple root i: r - (r, ai) ai
            c = sum(r[j] * A[j][i] for j in range(N))
            refl = tuple(r[k] - (c if k == i else 0) for k in range(N))
            if refl not in roots:
                new.add(refl)
    if not new:
        break
    roots |= new
roots = sorted(roots)
assert len(roots) == 72, len(roots)
rootset = set(roots)
pos = [r for r in roots if r > tuple([0] * N)]  # lexicographic positivity is wrong;
# use height/first-nonzero sign instead:
def is_pos(r):
    for x in r:
        if x != 0:
            return x > 0
    return False
pos = [r for r in roots if is_pos(r)]
assert len(pos) == 36, len(pos)
assert all(tuple(-x for x in r) in rootset for r in roots)

# ------------------------------------------------- Frenkel-Kac asymmetry eps
# eps bimultiplicative, eps(ai,ai) = -1, eps(ai,aj) eps(aj,ai) = (-1)^{(ai,aj)}.
eps_s = [[1] * N for _ in range(N)]
for i in range(N):
    eps_s[i][i] = -1
for i, j in EDGES:
    a, b = (i, j) if i < j else (j, i)
    eps_s[a][b] = -1   # oriented edge
    eps_s[b][a] = 1

def eps(a, b):
    s = 1
    for i in range(N):
        if a[i] == 0:
            continue
        for j in range(N):
            if b[j] == 0:
                continue
            if eps_s[i][j] == -1 and (a[i] * b[j]) % 2 == 1:
                s = -s
    return s

# ------------------------------------------------------------------ basis
# order: h_0..h_5 (coroots of simple), then e_r for r in roots (sorted order)
basis = [("h", i) for i in range(N)] + [("e", r) for r in roots]
DIM = len(basis)
assert DIM == 78
idx = {b: k for k, b in enumerate(basis)}

def bracket(u, v):
    """bracket of basis elements -> dict index->Fraction coeff"""
    tu, du = u
    tv, dv = v
    out = {}
    if tu == "h" and tv == "h":
        return out
    if tu == "h" and tv == "e":
        # [h_i, e_r] = r(h_i) e_r ; r(h_i) = sum_j r_j <alpha_j, alpha_i^v> = (A r)_i
        c = sum(A[du][j] * dv[j] for j in range(N))
        if c:
            out[idx[("e", dv)]] = Fraction(c)
        return out
    if tu == "e" and tv == "h":
        for k, c in bracket(v, u).items():
            out[k] = -c
        return out
    ra, rb = du, dv
    s = tuple(ra[i] + rb[i] for i in range(N))
    if all(x == 0 for x in s):
        # [e_a, e_-a] = eps(a,-a) * h_a, h_a = sum a_i h_i  (simply-laced)
        e0 = eps(ra, rb)
        for i in range(N):
            if ra[i]:
                out[idx[("h", i)]] = Fraction(e0 * ra[i])
        return out
    if s in rootset:
        out[idx[("e", s)]] = Fraction(eps(ra, rb))
    return out

# structure table as dict of dicts
TAB = [[None] * DIM for _ in range(DIM)]
for a in range(DIM):
    for b in range(DIM):
        TAB[a][b] = bracket(basis[a], basis[b])

def brk_vec(x, y):
    """bracket of two coefficient dicts index->Fraction"""
    out = {}
    for a, ca in x.items():
        if not ca:
            continue
        for b, cb in y.items():
            if not cb:
                continue
            for k, c in TAB[a][b].items():
                out[k] = out.get(k, Fraction(0)) + ca * cb * c
    return {k: v for k, v in out.items() if v}

# antisymmetry + Jacobi spot check (exact) on random triples
for _ in range(400):
    a, b, c = (random.randrange(DIM) for _ in range(3))
    xa, xb, xc = ({a: Fraction(1)}, {b: Fraction(1)}, {c: Fraction(1)})
    j1 = brk_vec(xa, brk_vec(xb, xc))
    j2 = brk_vec(xb, brk_vec(xc, xa))
    j3 = brk_vec(xc, brk_vec(xa, xb))
    tot = {}
    for d in (j1, j2, j3):
        for k, v in d.items():
            tot[k] = tot.get(k, Fraction(0)) + v
    assert all(v == 0 for v in tot.values()), (a, b, c, tot)
print("[PASS] Jacobi on 400 random triples (exact)")

def ad_matrix(x):
    """78x78 Fraction matrix of ad(x) for coefficient dict x"""
    M = [[Fraction(0)] * DIM for _ in range(DIM)]
    for b in range(DIM):
        res = brk_vec(x, {b: Fraction(1)})
        for k, v in res.items():
            M[k][b] = v
    return M

# ------------------------------------------------------------ principal sl2
# h: alpha_i(h)=2 for all i  ->  h = sum c_j h_j with A c = 2*ones
Asym = sp.Matrix(A)
cvec = Asym.solve(sp.Matrix([2] * N))
h_el = {idx[("h", i)]: Fraction(int(cvec[i].p), int(cvec[i].q)) for i in range(N)}
e_el = {idx[("e", r)]: Fraction(1) for r in simple}
# f = sum d_i e_{-a_i}: solve [e,f]=h
fvars = sp.symbols("d0:6")
f_sym = {idx[("e", tuple(-x for x in r))]: fvars[i] for i, r in enumerate(simple)}
# [e, f]:
comm = {}
for a, ca in e_el.items():
    for b, cb in f_sym.items():
        for k, c in TAB[a][b].items():
            comm[k] = comm.get(k, 0) + ca * cb * c
eqs = []
for i in range(N):
    k = idx[("h", i)]
    eqs.append(sp.Eq(comm.get(k, 0), sp.Rational(int(h_el.get(k, Fraction(0)).numerator), int(h_el.get(k, Fraction(0)).denominator))))
for k, expr in comm.items():
    if basis[k][0] == "e":
        eqs.append(sp.Eq(expr, 0))
sol = sp.solve(eqs, fvars, dict=True)
assert len(sol) == 1, sol
f_el = {}
for i, r in enumerate(simple):
    val = sol[0][fvars[i]]
    f_el[idx[("e", tuple(-x for x in r))]] = Fraction(int(val.p), int(val.q))
# verify sl2
assert brk_vec(e_el, f_el) == {k: v for k, v in h_el.items()}
he = brk_vec(h_el, e_el)
assert he == {k: 2 * v for k, v in e_el.items()}
hf = brk_vec(h_el, f_el)
assert hf == {k: -2 * v for k, v in f_el.items()}
print("[PASS] principal sl2 (e,h,f) exact")

adh = ad_matrix(h_el)
ade = ad_matrix(e_el)
adf = ad_matrix(f_el)

Mh = sp.Matrix([[sp.Rational(int(x.numerator), int(x.denominator)) for x in row] for row in adh])
Me = sp.Matrix([[sp.Rational(int(x.numerator), int(x.denominator)) for x in row] for row in ade])

# eigen-decomposition of ad h: eigenvalues integers
evals = {}
for lam in range(-22, 23):
    ns = (Mh - lam * sp.eye(DIM)).nullspace()
    if ns:
        evals[lam] = ns
dims = {lam: len(v) for lam, v in sorted(evals.items())}
tops = {}
for n in (2, 8, 10, 14, 16, 22):
    space = evals[n]
    B = sp.Matrix.hstack(*space)
    MeB = Me * B
    # kernel of ad e on this eigenspace: solve Me*B*c in span?? ad e maps weight n -> n+2.
    # highest vector: Me*B*c = 0
    K = MeB.nullspace()
    assert len(K) == 1, (n, len(K))
    v = B * K[0]
    # clear denominators to a primitive integer vector for a determinate scale
    num = [sp.nsimplify(x) for x in v]
    dens = [sp.fraction(x)[1] for x in v]
    L = sp.ilcm(*[int(d) for d in dens]) if dens else 1
    v = v * L
    nz = [int(x) for x in v if x != 0]
    g = abs(nz[0]) if len(nz) == 1 else sp.igcd(*nz)
    v = v / g
    # sign convention: first nonzero entry positive
    for x in v:
        if x != 0:
            if x < 0:
                v = -v
            break
    tops[n] = v
print("[PASS] ad(h) blocks; top-weight dims", dims)

x_, y_ = sp.symbols("x y")
t_poly = x_**5 * y_ - x_ * y_**5
W_poly = x_**8 + 14 * x_**4 * y_**4 + y_**8

def embed(pol, n):
    """Sym^n -> weight-n block: x^{n-k} y^k |-> ((n-k)!/n!) f^k . v_n"""
    p = sp.Poly(sp.expand(pol), x_, y_)
    vec = sp.zeros(DIM, 1)
    fk = tops[n]  # f^0 . v
    Mf = sp.Matrix([[sp.Rational(int(q.numerator), int(q.denominator)) for q in row] for row in adf])
    cur = fk
    fs = [cur]
    for k in range(1, n + 1):
        cur = Mf * cur
        fs.append(cur)
    for (i, j), c in p.terms():
        # term x^i y^j, i + j = n, k = j
        k = j
        vec += sp.Rational(c) * sp.Rational(sp.factorial(n - k), sp.factorial(n)) * fs[k]
    return vec

g8 = embed(W_poly, 8)
g14 = embed(t_poly * W_poly, 14)
g16 = embed(W_poly**2, 16)
g22 = embed(t_poly * W_poly**2, 22)

def tovecdict(v):
    return {i: Fraction(int(v[i].p), int(v[i].q)) for i in range(DIM) if v[i] != 0}

G = {8: g8, 14: g14, 16: g16, 22: g22}
Gd = {n: tovecdict(v) for n, v in G.items()}
# pairwise commuting?
for a, b in itertools.combinations(G, 2):
    com = brk_vec(Gd[a], Gd[b])
    assert not com, (a, b, com)
print("[PASS] charges g8,g14,g16,g22 pairwise commute (exact /Q)")

ads = {n: ad_matrix(Gd[n]) for n in G}
with open(sys.path[0] + "/r15_e6_data.pkl", "wb") as fh:
    pickle.dump({"basis": basis, "TAB_dims": DIM,
                 "ads": {n: [[str(x) for x in row] for row in ads[n]] for n in ads},
                 "charges": {n: {k: str(v) for k, v in Gd[n].items()} for n in Gd},
                 }, fh)
print("saved r15_e6_data.pkl")
