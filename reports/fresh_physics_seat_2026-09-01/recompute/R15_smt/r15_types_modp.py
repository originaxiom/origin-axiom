#!/usr/bin/env python3
"""R15 stage 3: landing type (mod-p squeeze at two primes), banked-residue diff,
sector matching, and the planted su(5) positive control.

Bracket table rebuilt with the SAME conventions as stage 1 (no sympy needed).
"""
import pickle, json
from fractions import Fraction
from math import gcd, lcm
from flint import fmpz_mat, nmod_mat, nmod_poly, fmpz_poly

HERE = __file__.rsplit("/", 1)[0]

# ---------------- rebuild e6 bracket table (identical conventions to stage 1) ----
EDGES = [(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)]
N = 6
A = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in EDGES:
    A[i][j] = A[j][i] = -1
simple = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
roots = set(simple)
while True:
    new = set()
    for r in list(roots):
        for i in range(N):
            c = sum(r[j] * A[j][i] for j in range(N))
            refl = tuple(r[k] - (c if k == i else 0) for k in range(N))
            if refl not in roots:
                new.add(refl)
    if not new:
        break
    roots |= new
roots = sorted(roots)
assert len(roots) == 72
rootset = set(roots)
eps_s = [[1] * N for _ in range(N)]
for i in range(N):
    eps_s[i][i] = -1
for i, j in EDGES:
    a, b = (i, j) if i < j else (j, i)
    eps_s[a][b] = -1
    eps_s[b][a] = 1
def eps(a, b):
    s = 1
    for i in range(N):
        if a[i] == 0: continue
        for j in range(N):
            if b[j] == 0: continue
            if eps_s[i][j] == -1 and (a[i] * b[j]) % 2 == 1:
                s = -s
    return s
basis = [("h", i) for i in range(N)] + [("e", r) for r in roots]
DIM = 78
idx = {b: k for k, b in enumerate(basis)}
def bracket(u, v):
    tu, du = u; tv, dv = v
    out = {}
    if tu == "h" and tv == "h": return out
    if tu == "h" and tv == "e":
        c = sum(A[du][j] * dv[j] for j in range(N))
        if c: out[idx[("e", dv)]] = c
        return out
    if tu == "e" and tv == "h":
        return {k: -c for k, c in bracket(v, u).items()}
    ra, rb = du, dv
    s = tuple(ra[i] + rb[i] for i in range(N))
    if all(x == 0 for x in s):
        e0 = eps(ra, rb)
        for i in range(N):
            if ra[i]: out[idx[("h", i)]] = e0 * ra[i]
        return out
    if s in rootset:
        out[idx[("e", s)]] = eps(ra, rb)
    return out
TAB = [[bracket(basis[a], basis[b]) for b in range(DIM)] for a in range(DIM)]

# ---------------- load charges (integer-scaled as in stage 2) ----------------
D = pickle.load(open(HERE + "/r15_e6_data.pkl", "rb"))
charges = {}
for n, dic in D["charges"].items():
    n = int(n)
    v = {int(k): Fraction(x) for k, x in dic.items()}
    L = 1
    for f in v.values(): L = lcm(L, f.denominator)
    ints = {k: int(f * L) for k, f in v.items()}
    g = 0
    for x in ints.values(): g = gcd(g, abs(x))
    charges[n] = {k: x // g for k, x in ints.items()}
EX = json.load(open(HERE + "/r15_exact_out.json"))
MU = EX["mu_mine"]           # degree 3, coeff list low->high
SEXT2 = [f for f, m in EX["joint_factors"] if m == 2][0]
SEXT6 = [f for f, m in EX["joint_factors"] if m == 6][0]

def ad_int(vec):
    M = [[0] * DIM for _ in range(DIM)]
    for b in range(DIM):
        for a, ca in vec.items():
            for k, c in TAB[a][b].items():
                M[k][b] += ca * c
    return M

AD = {n: ad_int(charges[n]) for n in (8, 14, 16, 22)}
# sanity vs stage-1 ads (stage 2 rescaled identically)
A8z = fmpz_mat(AD[8]); A14z = fmpz_mat(AD[14]); A16z = fmpz_mat(AD[16]); A22z = fmpz_mat(AD[22])
assert A8z.ncols() - A8z.rank() == 30 and A14z.ncols() - A14z.rank() == 12

def modmat(M, p):
    return nmod_mat([[x % p for x in row] for row in M], p)

def poly_roots_modp(coeffs, p):
    f = nmod_poly([c % p for c in coeffs], p)
    rs = []
    for fac, m in f.factor()[1]:
        if fac.degree() == 1:
            # fac = x + c -> root -c
            rs.append((-int(fac[0])) % p)
    return rs, f.factor()

def joint_nullity(p, r, s):
    rows = []
    M1 = [[(AD[8][i][j] + r * AD[16][i][j]) % p for j in range(DIM)] for i in range(DIM)]
    M2 = [[(AD[14][i][j] + s * AD[16][i][j]) % p for j in range(DIM)] for i in range(DIM)]
    Mat = nmod_mat(M1 + M2, p)
    return DIM - Mat.rank(), Mat

def kernel_basis(p, r, s):
    nul, Mat = joint_nullity(p, r, s)
    X, k = Mat.nullspace()
    cols = [[int(X[i, j]) for i in range(DIM)] for j in range(k)]
    return cols[:nul] if False else [c for c in cols][:k], nul

def brk_modp(u, v, p):
    out = [0] * DIM
    for a in range(DIM):
        if u[a] == 0: continue
        for b in range(DIM):
            if v[b] == 0: continue
            for k, c in TAB[a][b].items():
                out[k] = (out[k] + u[a] * v[b] * c) % p
    return out

def analyze(p, r, s, label):
    nul, Mat = joint_nullity(p, r, s)
    X, k = Mat.nullspace()
    Z = [[int(X[i, j]) for i in range(DIM)] for j in range(k)][:k]
    Z = Z[:nul] if nul <= k else Z
    # derived span
    brs = []
    for a in range(len(Z)):
        for b in range(a + 1, len(Z)):
            w = brk_modp(Z[a], Z[b], p)
            if any(w): brs.append(w)
    dspan = nmod_mat(brs, p).rank() if brs else 0
    # center: v in Z with [v, z_b] = 0 for all b: matrix over coefficients
    # column c -> stacked brackets [Z_c, Z_b]
    colmat = []
    for cix in range(len(Z)):
        col = []
        for b in range(len(Z)):
            col += brk_modp(Z[cix], Z[b], p)
        colmat.append(col)
    Cm = nmod_mat(colmat, p).transpose()
    cdim = len(Z) - Cm.rank()
    print(f"  [{label}] p={p} r={r} s={s}: dim z = {nul}, derived span = {dspan}, center = {cdim}")
    return nul, dspan, cdim

def first_measurement_type(p, r):
    M1 = nmod_mat([[(AD[8][i][j] + r * AD[16][i][j]) % p for j in range(DIM)] for i in range(DIM)], p)
    nul = DIM - M1.rank()
    X, k = M1.nullspace()
    Z = [[int(X[i, j]) for i in range(DIM)] for j in range(k)][:k]
    brs = []
    for a in range(len(Z)):
        for b in range(a + 1, len(Z)):
            w = brk_modp(Z[a], Z[b], p)
            if any(w): brs.append(w)
    dspan = nmod_mat(brs, p).rank() if brs else 0
    colmat = []
    for cix in range(len(Z)):
        col = []
        for b in range(len(Z)):
            col += brk_modp(Z[cix], Z[b], p)
        colmat.append(col)
    Cm = nmod_mat(colmat, p).transpose()
    cdim = len(Z) - Cm.rank()
    print(f"  [z(x1)] p={p} r={r}: dim = {nul}, derived span = {dspan}, center = {cdim}")
    return nul, dspan, cdim

# ---------------- run at banked prime + a second prime ----------------
for p in (40123, 40493, 41023):
    rs, facmu = poly_roots_modp(MU, p)
    s2, fac2 = poly_roots_modp(SEXT2, p)
    s6, fac6 = poly_roots_modp(SEXT6, p)
    print(f"p={p}: mu roots {rs}; sext2 roots {s2}; sext6 roots {s6}")
    if not rs or not s2:
        print("   (skipping p: not enough splitting)")
        continue
    # banked residue diff at 40123: s_theirs = -a_q/(13*gamma_q)
    if p == 40123:
        inv = pow((13 * 13410) % p, p - 2, p)
        st = (-2675 * inv) % p
        print("  banked-residue slope -a_q/(13 gamma_q) mod p =", st, " in my sext2 roots?", st in s2, " in sext6?", st in s6)
        st2 = (2675 * inv) % p
        print("  +a_q/(13 gamma_q) =", st2, " in sext2?", st2 in s2, " in sext6?", st2 in s6)
    # first measurement type at each root
    for r in rs[:1]:
        first_measurement_type(p, r)
    # grid: which (r, s) matches (14) vs not (12)
    grid = {}
    for r in rs:
        for s in s2:
            nul, _ = joint_nullity(p, r, s)
            grid[(r, s)] = nul
    print("  sext2 grid nullities:", sorted(set(grid.values())), "counts:",
          {v: sum(1 for x in grid.values() if x == v) for v in set(grid.values())})
    # full analysis on one matched pair
    matched = [(r, s) for (r, s), v in grid.items() if v == 14]
    if matched:
        r, s = matched[0]
        analyze(p, r, s, "SMT wall")
    # an 18-wall for the ladder
    done18 = False
    for r in rs:
        for s in s6:
            nul, _ = joint_nullity(p, r, s)
            if nul == 18 and not done18:
                analyze(p, r, s, "18-wall")
                done18 = True
    if p != 40123:
        break

# ---------------- planted su(5) positive control (exact /Q) ----------------
# Cartan element killing the A4 subsystem on Bourbaki nodes 1,3,4,5 (indices 0,2,3,4):
# h = sum c_i h_i with alpha_j(h) = sum_i A_ji c_i = 0 for j in {0,2,3,4}, nonzero else.
import itertools
from fractions import Fraction as Fr
# solve A c = target with target = (0, t1, 0, 0, 0, t2), pick t generic
import sympy as sp
Am = sp.Matrix(A)
targ = sp.Matrix([0, 7, 0, 0, 0, 11])
cvec = Am.solve(targ)
hplant = {}
L = 1
for i in range(N):
    L = lcm(L, int(sp.fraction(cvec[i])[1]))
for i in range(N):
    hplant[idx[("h", i)]] = int(cvec[i] * L)
Mh = fmpz_mat(ad_int(hplant))
nulh = DIM - Mh.rank()
print("[control] planted A4-annihilating Cartan element: dim z =", nulh, "(expect 26 = su(5)+u(1)^2)")
# derived dim of the planted centralizer, exact mod a prime
p = 40123
Xh, kh = modmat(ad_int(hplant), p).nullspace()
Zh = [[int(Xh[i, j]) for i in range(DIM)] for j in range(kh)][:kh]
brs = [brk_modp(Zh[a], Zh[b], p) for a in range(len(Zh)) for b in range(a + 1, len(Zh))]
brs = [w for w in brs if any(w)]
print("[control] derived span mod p:", nmod_mat(brs, p).rank(), "(expect 24 = A4)")
