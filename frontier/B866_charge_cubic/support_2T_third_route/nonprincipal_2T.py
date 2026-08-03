#!/usr/bin/env python3
"""B858 -- NON-PRINCIPAL EMBEDDINGS OF 2T IN E6.  The revival hatch registered by B854.

B854 computed that Cent_{e6}(2T) is abelian u(1)^4 when 2T enters through the PRINCIPAL sl2.
Its escape hatch: a NON-principal sl2 has a different centralizer.  This enumerates EVERY
conjugacy class of sl2 -> e6 (= every nilpotent orbit, Dynkin/Kostant), and for each one
computes dim Cent_{e6}(2T) and whether that centralizer is ABELIAN.

Everything exact over Q (Fractions).  Nothing cited: the root system, the structure constants,
the weighted Dynkin diagrams, the sl2 triples, the 2T-invariants and every bracket are computed
here, and each stage carries a check that could have failed.

Stages
  0  E6 Chevalley algebra over Q, Jacobi-verified (same construction as B854).
  1  enumerate the 3^6 = 729 candidate weighted Dynkin diagrams; a candidate is a genuine
     nilpotent orbit iff an sl2-triple (e,h,f) with e in g_2, f in g_{-2} actually EXISTS --
     certified by exhibiting it, not by a table.
  2  the sl2-decomposition of the 78 from the ad(h) spectrum.
  3  dim Cent(2T) two independent ways:
        (a) character theory   sum_d mult(d) * <triv, Res_{2T} V_d>
        (b) construction       explicit 2T-invariant vectors in e6, rank of their span
  4  the bracket structure of Cent(2T): abelian or not, EXACTLY.
  5  the reductive centralizer z(e,h,f) = Cent(sl2) and its isomorphism type.

~5 min.  The simple-ideal count that separates the two 16-dimensional cases is run by
verify_group_fixed.py (which is also an INDEPENDENT route to Cent(2T) itself).
"""
from fractions import Fraction as F
from itertools import product
import random
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ================================================================ 0. E6 over Q
# Bourbaki labels: node 0..5 = alpha_1..alpha_6 with chain 0-2-3-4-5 and node 1 hung on node 3.
C = [[2, 0, -1, 0, 0, 0],
     [0, 2, 0, -1, 0, 0],
     [-1, 0, 2, -1, 0, 0],
     [0, -1, -1, 2, -1, 0],
     [0, 0, 0, -1, 2, -1],
     [0, 0, 0, 0, -1, 2]]
N = 6
DIAG_AUT = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}   # -w0 on E6


def ip(a, b):
    return sum(a[i] * b[j] * C[i][j] for i in range(N) for j in range(N))


pos = [tuple(a) for a in product(range(4), repeat=N) if any(a) and ip(a, a) == 2]
ROOTS = pos + [tuple(-x for x in a) for a in pos]
IDX = {r: k for k, r in enumerate(ROOTS)}
DIM = N + len(ROOTS)
print(f"[0] positive roots {len(pos)}  total {len(ROOTS)}  dim {DIM}   (E6: 36 / 72 / 78)")

E0 = [[(-1 if i == j else ((-1) ** C[i][j] if i < j else 1)) for j in range(N)] for i in range(N)]


def eps(a, b):
    s = 1
    for i in range(N):
        if a[i] == 0:
            continue
        for j in range(N):
            if b[j] == 0:
                continue
            if E0[i][j] == -1 and (a[i] * b[j]) % 2:
                s = -s
    return s


def bracket_basis(p, q):
    """[b_p, b_q] as a SPARSE dict {index: Fraction}.  Basis: 0..5 = h_1..h_6, then e_root."""
    if p < N and q < N:
        return {}
    if p < N:
        b = ROOTS[q - N]
        c = sum(b[j] * C[p][j] for j in range(N))
        return {q: F(c)} if c else {}
    if q < N:
        a = ROOTS[p - N]
        c = -sum(a[j] * C[q][j] for j in range(N))
        return {p: F(c)} if c else {}
    a, b = ROOTS[p - N], ROOTS[q - N]
    s = tuple(a[i] + b[i] for i in range(N))
    if not any(s):
        sgn = eps(a, tuple(-v for v in a))
        return {i: F(sgn * a[i]) for i in range(N) if a[i]}
    if s in IDX:
        return {N + IDX[s]: F(eps(a, b))}
    return {}


BB = [[bracket_basis(p, q) for q in range(DIM)] for p in range(DIM)]


def br(u, v):
    out = {}
    for p, up in u.items():
        row = BB[p]
        for q, vq in v.items():
            c = up * vq
            for k, rk in row[q].items():
                w = out.get(k, 0) + c * rk
                if w:
                    out[k] = w
                elif k in out:
                    del out[k]
    return out


def bvec(k):
    return {k: F(1)}


def sub(u, v):
    out = dict(u)
    for k, x in v.items():
        w = out.get(k, 0) - x
        if w:
            out[k] = w
        elif k in out:
            del out[k]
    return out


def addv(u, v):
    out = dict(u)
    for k, x in v.items():
        w = out.get(k, 0) + x
        if w:
            out[k] = w
        elif k in out:
            del out[k]
    return out


def smul(c, u):
    return {k: c * x for k, x in u.items()} if c else {}


# ---- Jacobi check (the signs are the risky part; a wrong eps gives a non-Lie algebra)
random.seed(11)
bad = 0
for _ in range(4000):
    i, j, k = random.sample(range(DIM), 3)
    J = addv(addv(br(BB[i][j], bvec(k)), br(BB[j][k], bvec(i))), br(BB[k][i], bvec(j)))
    if J:
        bad += 1
print(f"[0] Jacobi on 4000 random basis triples: {'PASS' if bad == 0 else f'FAIL {bad}'}")
assert bad == 0

# ================================================================ exact linear algebra over Q


def rref(rows, ncol):
    rows = [r[:] for r in rows]
    m = len(rows)
    piv = []
    r = 0
    for col in range(ncol):
        pr = None
        for k in range(r, m):
            if rows[k][col] != 0:
                pr = k
                break
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        iv = F(1) / rows[r][col]
        rows[r] = [x * iv for x in rows[r]]
        for k in range(m):
            if k != r and rows[k][col] != 0:
                f = rows[k][col]
                rows[k] = [a - f * b for a, b in zip(rows[k], rows[r])]
        piv.append(col)
        r += 1
        if r == m:
            break
    return rows[:r], piv


def rank_of(vecs, ncol=DIM):
    rows = []
    for v in vecs:
        r = [F(0)] * ncol
        for k, x in (v.items() if isinstance(v, dict) else enumerate(v)):
            r[k] = x
        rows.append(r)
    if not rows:
        return 0
    R, _ = rref(rows, ncol)
    return len(R)


def nullspace(rows, ncol):
    """basis of {x in Q^ncol : rows . x = 0}"""
    if not rows:
        return [[F(1) if i == j else F(0) for i in range(ncol)] for j in range(ncol)]
    R, piv = rref(rows, ncol)
    free = [c for c in range(ncol) if c not in piv]
    out = []
    for fc in free:
        v = [F(0)] * ncol
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        out.append(v)
    return out


def solve(cols, b, ncol):
    """solve sum_j x_j cols[j] = b ; cols/b are dicts over DIM.  None if inconsistent."""
    rows = []
    for i in range(DIM):
        rows.append([cols[j].get(i, F(0)) for j in range(ncol)] + [b.get(i, F(0))])
    R, piv = rref(rows, ncol + 1)
    if ncol in piv:
        return None
    x = [F(0)] * ncol
    for i, pc in enumerate(piv):
        x[pc] = R[i][ncol]
    return x


# ================================================================ 1. weighted Dynkin diagrams
Cinv_num = None
import fractions


def cartan_inverse():
    n = N
    M = [[F(C[i][j]) for j in range(n)] + [F(1) if i == k else F(0) for k in range(n)]
         for i in range(n)]
    R, piv = rref(M, 2 * n)
    assert piv == list(range(n))
    return [[R[i][n + j] for j in range(n)] for i in range(n)]


CINV = cartan_inverse()


def h_of_labels(L):
    """H = sum u_p h_p with <alpha_i, H> = L_i  ->  u = C^{-1} L (C symmetric)."""
    u = [sum(CINV[i][j] * L[j] for j in range(N)) for i in range(N)]
    return {i: u[i] for i in range(N) if u[i]}


def grade(L, r):
    return sum(r[i] * L[i] for i in range(N))


print("[1] scanning 729 candidate weighted Dynkin diagrams for a REAL sl2-triple ...")
orbits = []
for L in product(range(3), repeat=N):
    g2 = [r for r in ROOTS if grade(L, r) == 2]
    gm2 = [r for r in ROOTS if grade(L, r) == -2]
    H = h_of_labels(list(L))
    if not g2:                       # only the zero orbit
        if not any(L):
            orbits.append((L, {}, {}, {}))
        continue
    found = None
    rnd = random.Random(hash(L) & 0xffff)
    for attempt in range(8):
        e = {N + IDX[r]: F(rnd.randint(1, 9)) for r in g2}
        cols = [br(e, bvec(N + IDX[r])) for r in gm2]
        x = solve(cols, H, len(gm2))
        if x is None:
            continue
        f = {}
        for j, r in enumerate(gm2):
            if x[j]:
                f[N + IDX[r]] = x[j]
        # certify the triple
        if br(e, f) == H and br(H, e) == smul(F(2), e) and br(H, f) == smul(F(-2), f):
            found = (e, f)
            break
    if found:
        orbits.append((L, H, found[0], found[1]))

print(f"[1] nilpotent orbits certified by an explicit sl2-triple: {len(orbits)}")
sym = all(tuple(L[DIAG_AUT[i]] for i in range(N)) == tuple(L) for L, _, _, _ in orbits)
print(f"[1] every diagram invariant under -w0 (E6 diagram automorphism): {sym}   "
      f"[forced, since h ~ -h]")

# ================================================================ 2T character theory
# 2T = SL(2,3), 24 elements; classes (size, cos(theta)) with theta the SU(2) rotation angle
CLASSES = [(1, F(1)), (1, F(-1)), (6, F(0)), (8, F(1, 2)), (8, F(-1, 2))]
assert sum(c for c, _ in CLASSES) == 24


def chi(d, c):
    """character of the d-dimensional SL(2) irrep at an element with eigenvalues e^{+-i theta},
    c = cos(theta):  chi_d = U_{d-1}(c)."""
    a, b = F(0), F(1)          # U_{-1}=0, U_0=1
    for _ in range(d - 1):
        a, b = b, 2 * c * b - a
    return b


def triv_mult(d):
    s = sum(sz * chi(d, c) for sz, c in CLASSES)
    assert s % 24 == 0
    return int(s / 24)


TRIV = {d: triv_mult(d) for d in range(1, 40)}
print("[2] <triv, Res_2T V_d> for d=1..24:", [TRIV[d] for d in range(1, 25)])
assert TRIV[1] == 1 and TRIV[2] == 0 and TRIV[3] == 0 and TRIV[7] == 1

# ================================================================ 2T invariants in Sym^n over Q
# 2T as 2x2 matrices over Q(i) via unit quaternions; represented as ((re,im),...) Fractions.


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def q2m(a, b, c, d):
    return ((F(a), F(b)), (F(c), F(d)), (F(-c), F(d)), (F(a), F(-b)))   # (m00,m01,m10,m11)


GEN = [q2m(0, 1, 0, 0), q2m(F(1, 2), F(1, 2), F(1, 2), F(1, 2))]


def mmul(M, Mp):
    return (cadd(cmul(M[0], Mp[0]), cmul(M[1], Mp[2])),
            cadd(cmul(M[0], Mp[1]), cmul(M[1], Mp[3])),
            cadd(cmul(M[2], Mp[0]), cmul(M[3], Mp[2])),
            cadd(cmul(M[2], Mp[1]), cmul(M[3], Mp[3])))


grp = {q2m(1, 0, 0, 0)}
frontier_ = [q2m(1, 0, 0, 0)]
while frontier_:
    nxt = []
    for g in frontier_:
        for s in GEN:
            p = mmul(g, s)
            if p not in grp:
                grp.add(p)
                nxt.append(p)
    frontier_ = nxt
print(f"[2] group generated by <i, (1+i+j+k)/2> has order {len(grp)}   (2T: 24)")
assert len(grp) == 24


def symn_matrix(M, n):
    """matrix of Sym^n on the monomial basis x^{n-k} y^k, k=0..n, for the substitution
    X = m00 x + m10 y, Y = m01 x + m11 y  (B854's convention)."""
    m00, m01, m10, m11 = M
    cols = []
    for k in range(n + 1):
        # coefficients of X^{n-k} Y^k
        poly = {(0, 0): (F(1), F(0))}
        for _ in range(n - k):
            new = {}
            for (i, j), c in poly.items():
                for (di, dj), t in (((1, 0), m00), ((0, 1), m10)):
                    key = (i + di, j + dj)
                    new[key] = cadd(new.get(key, (F(0), F(0))), cmul(c, t))
            poly = new
        for _ in range(k):
            new = {}
            for (i, j), c in poly.items():
                for (di, dj), t in (((1, 0), m01), ((0, 1), m11)):
                    key = (i + di, j + dj)
                    new[key] = cadd(new.get(key, (F(0), F(0))), cmul(c, t))
            poly = new
        cols.append([poly.get((n - j, j), (F(0), F(0))) for j in range(n + 1)])
    return cols          # cols[k][j] = coeff of x^{n-j}y^j in image of x^{n-k}y^k


INVPOLY = {}


def invariants_symn(n):
    """rational basis of the 2T-invariants in Sym^n.  Invariance of a REAL vector v under
    S = A + iB is (A-I)v = 0 AND Bv = 0, so the whole thing stays over Q."""
    if n in INVPOLY:
        return INVPOLY[n]
    rows = []
    for M in GEN:
        cols = symn_matrix(M, n)
        for j in range(n + 1):                      # row j of A - I  and of B
            rows.append([cols[k][j][0] - (F(1) if j == k else F(0)) for k in range(n + 1)])
            rows.append([cols[k][j][1] for k in range(n + 1)])
    ns = nullspace(rows, n + 1)
    INVPOLY[n] = ns
    return ns


# cross-check against the character count on the plain SL(2) irreps
for n in [0, 4, 6, 8, 10, 12, 14, 16, 22]:
    assert len(invariants_symn(n)) == TRIV[n + 1], (n, len(invariants_symn(n)), TRIV[n + 1])
print("[2] Sym^n 2T-invariant dimensions agree with the character count for n in "
      "{0,4,6,8,10,12,14,16,22}")

# ================================================================ subspace tools
from math import factorial


def dense(v):
    r = [F(0)] * DIM
    for k, x in v.items():
        r[k] = x
    return r


def independent_basis(vecs):
    """maximal independent subset of vecs (as dicts), in order."""
    rows = []
    keep = []
    for v in vecs:
        cand = rows + [dense(v)]
        R, _ = rref(cand, DIM)
        if len(R) > len(rows):
            rows = cand
            keep.append(v)
    return keep


def coord_maker(basis):
    """returns f(v) -> coordinates of v in `basis` (v MUST lie in the span)."""
    k = len(basis)
    M = [[b.get(i, F(0)) for b in basis] for i in range(DIM)]     # DIM x k
    # find k independent rows
    rows, piv, chosen = [], [], []
    for i in range(DIM):
        cand = rows + [M[i]]
        R, _ = rref(cand, k)
        if len(R) > len(rows):
            rows = cand
            chosen.append(i)
        if len(chosen) == k:
            break
    assert len(chosen) == k
    aug = [rows[i][:] + [F(1) if i == j else F(0) for j in range(k)] for i in range(k)]
    R, p = rref(aug, 2 * k)
    inv = [[R[i][k + j] for j in range(k)] for i in range(k)]

    def f(v):
        b = [v.get(i, F(0)) for i in chosen]
        return [sum(inv[i][j] * b[j] for j in range(k)) for i in range(k)]
    return f


def ad_matrix_full(v):
    """ad(v) as a DIM x DIM dense matrix (rows = output coords)."""
    cols = [br(v, bvec(j)) for j in range(DIM)]
    return [[cols[j].get(i, F(0)) for j in range(DIM)] for i in range(DIM)]


def killing_e6(basis):
    A = [ad_matrix_full(v) for v in basis]
    n = len(basis)
    K = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            s = F(0)
            Ai, Aj = A[i], A[j]
            for k in range(DIM):
                rk = Ai[k]
                for l in range(DIM):
                    if rk[l]:
                        s += rk[l] * Aj[l][k]
            K[i][j] = K[j][i] = s
    return K


def matrank(M, ncol):
    R, _ = rref([r[:] for r in M], ncol)
    return len(R)


def ideal_structure(basis):
    """For a SEMISIMPLE subalgebra ss of e6 given by `basis`: use the e6-Casimir
    Phi = sum_a ad(u_a) ad(u^a)  (duals w.r.t. K_e6|ss).  Phi is ss-equivariant and acts as
    1/c_i on the i-th simple ideal, where K_e6|ideal_i = c_i * K_{ideal_i}.  Distinct
    eigenvalues  ->  the simple ideals and their dimensions, COMPUTED."""
    n = len(basis)
    if n == 0:
        return []
    K = killing_e6(basis)
    aug = [K[i][:] + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    R, p = rref(aug, 2 * n)
    if p != list(range(n)):
        return None                      # degenerate: not semisimple
    Kinv = [[R[i][n + j] for j in range(n)] for i in range(n)]
    dualb = []
    for a in range(n):
        v = {}
        for b in range(n):
            if Kinv[a][b]:
                v = addv(v, smul(Kinv[a][b], basis[b]))
        dualb.append(v)
    co = coord_maker(basis)

    def adss(v):
        return [co(br(v, b)) for b in basis]      # columns

    Phi = [[F(0)] * n for _ in range(n)]
    for a in range(n):
        A = adss(basis[a])       # A[j] = coords of [u_a, b_j]  (column j)
        B = adss(dualb[a])
        for j in range(n):
            colj = B[j]
            acc = [F(0)] * n
            for m in range(n):
                if colj[m]:
                    c = colj[m]
                    Am = A[m]
                    for i in range(n):
                        if Am[i]:
                            acc[i] += c * Am[i]
            for i in range(n):
                if acc[i]:
                    Phi[i][j] += acc[i]
    # eigenvalues of a scalar-on-each-ideal operator: read off from the diagonal candidates
    evs = sorted({Phi[i][i] for i in range(n)})
    out = []
    for lam in evs:
        M = [[Phi[i][j] - (lam if i == j else F(0)) for j in range(n)] for i in range(n)]
        d = n - matrank(M, n)
        if d:
            out.append((lam, d))
    if sum(d for _, d in out) != n:
        return None
    return out


P_MOD = 2147483647          # 2^31 - 1


def n_invariant_forms(ssb):
    """#simple ideals of a semisimple ss = dim of its space of ad-invariant symmetric bilinear
    forms.  Done mod p with integer arithmetic (the exact-Q version is correct but blows up):
    rank_p <= rank_Q, so nullity_p >= nullity_Q -- a rigorous UPPER bound on the ideal count,
    which is the direction that disambiguates downward."""
    P = P_MOD
    n = len(ssb)
    co = coord_maker(ssb)
    A = [[[int(c.numerator) * pow(int(c.denominator), P - 2, P) % P
           for c in co(br(ssb[x], ssb[j]))] for j in range(n)] for x in range(n)]
    pairs = [(a, b) for a in range(n) for b in range(a, n)]
    pidx = {q: i for i, q in enumerate(pairs)}
    m = len(pairs)
    rows = []
    for x in range(n):
        Ax = A[x]
        for (a, b) in pairs:
            row = [0] * m
            for i in range(n):
                if Ax[a][i]:
                    k = pidx[(min(i, b), max(i, b))]
                    row[k] = (row[k] + Ax[a][i]) % P
                if Ax[b][i]:
                    k = pidx[(min(a, i), max(a, i))]
                    row[k] = (row[k] + Ax[b][i]) % P
            if any(row):
                rows.append(row)
    r = 0
    for col in range(m):
        pr = next((k for k in range(r, len(rows)) if rows[k][col]), None)
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        iv = pow(rows[r][col], P - 2, P)
        rows[r] = [v * iv % P for v in rows[r]]
        pv = rows[r]
        for k in range(len(rows)):
            if k != r and rows[k][col]:
                fq = rows[k][col]
                rows[k] = [(a - fq * b) % P for a, b in zip(rows[k], pv)]
        r += 1
        if r == len(rows):
            break
    return m - r


SIMPLE_DIM = {"A1": 3, "A2": 8, "A3": 15, "A4": 24, "A5": 35, "A6": 48,
              "B2=C2": 10, "B3": 21, "C3": 21, "B4": 36, "C4": 36, "D4": 28,
              "G2": 14, "F4": 52, "E6": 78}


def name_simple(d):
    hits = sorted(k for k, v in SIMPLE_DIM.items() if v == d)
    return "/".join(hits) if hits else f"dim{d}"



def analyse(L, H, e, f):
    lab = list(L)
    gr = {}
    for r in ROOTS:
        gr[N + IDX[r]] = grade(lab, r)
    for i in range(N):
        gr[i] = 0
    spec = {}
    for k in range(DIM):
        spec[gr[k]] = spec.get(gr[k], 0) + 1
    # sl2 decomposition: mult of highest weight n
    mult = {}
    for n in sorted(spec):
        if n < 0:
            continue
        m = spec.get(n, 0) - spec.get(n + 2, 0)
        if m:
            mult[n] = m
    assert sum(m * (n + 1) for n, m in mult.items()) == DIM, (L, mult)
    # (a) dim Cent(2T) by character
    dim_char = sum(m * TRIV[n + 1] for n, m in mult.items())
    dim_sl2 = mult.get(0, 0)
    assert dim_sl2 == spec.get(0, 0) - spec.get(2, 0)
    # orbit dimension = 78 - dim z(e) , dim z(e) = dim g_0 + dim g_1
    orbdim = DIM - (spec.get(0, 0) + spec.get(1, 0))

    # (b) dim Cent(2T) by construction + its bracket structure
    inv_vecs = []
    for n, m in sorted(mult.items()):
        if TRIV[n + 1] == 0:
            continue
        gn = [k for k in range(DIM) if gr[k] == n]
        rows = []
        for i in range(DIM):
            rows.append([br(e, bvec(k)).get(i, F(0)) for k in gn])
        hw = nullspace(rows, len(gn))
        assert len(hw) == m, (L, n, len(hw), m)
        polys = invariants_symn(n)
        for w in hw:
            v = {}
            for j, k in enumerate(gn):
                if w[j]:
                    v[k] = w[j]
            chain = [v]
            for _ in range(n):
                chain.append(br(f, chain[-1]))
            for p in polys:
                out = {}
                for k in range(n + 1):
                    if p[k]:
                        out = addv(out, smul(p[k] * F(factorial(n - k), factorial(n)), chain[k]))
                inv_vecs.append(out)
    dim_built = rank_of(inv_vecs)
    Cb = independent_basis(inv_vecs)
    assert len(Cb) == dim_built

    brs = []
    for i in range(len(Cb)):
        for j in range(i + 1, len(Cb)):
            b = br(Cb[i], Cb[j])
            if b:
                brs.append(b)
    dim_derived = rank_of(brs)

    # centre of C, rank of C, intrinsic Killing form of C, K_e6 restricted to C
    nC = len(Cb)
    rows = []
    for a in Cb:
        for i in range(DIM):
            rows.append([br(a, Cb[j]).get(i, F(0)) for j in range(nC)])
    C_centre = len(nullspace(rows, nC))
    rr = random.Random(23)
    C_rank = 10 ** 9
    for _ in range(3):
        x = {}
        for a in Cb:
            x = addv(x, smul(F(rr.randint(1, 30)), a))
        rows = [[br(x, Cb[j]).get(i, F(0)) for j in range(nC)] for i in range(DIM)]
        C_rank = min(C_rank, len(nullspace(rows, nC)))
    coC = coord_maker(Cb)
    adC = [[coC(br(a, b)) for b in Cb] for a in Cb]
    KC = [[sum(adC[i][m][l] * adC[j][l][m] for l in range(nC) for m in range(nC))
           for j in range(nC)] for i in range(nC)]
    KC_rank = matrank(KC, nC)
    KE6_rank = matrank(killing_e6(Cb), nC)
    # simple ideals of [C,C]
    ssC = independent_basis(brs)
    ideals = ideal_structure(ssC) if ssC else []
    ideal_dims = sorted(d for _, d in ideals) if ideals else []
    nforms = None
    if ideal_dims and any(d not in SIMPLE_DIM.values() for d in ideal_dims):
        # the e6-Casimir did not separate (equal Dynkin indices): count invariant forms
        # the ideal count is slow here; it is run separately by verify_group_fixed.py
        nforms = None
        if nforms == 2 and ideal_dims == [16]:
            ideal_dims = [8, 8]
    ideal_names = "+".join(name_simple(d) for d in ideal_dims) if ideal_dims else "0"

    # reductive centralizer z(e,h,f) = Cent(sl2)  (joint kernel, inside g_0)
    g0 = [k for k in range(DIM) if gr[k] == 0]
    rows = []
    for X in (e, f):
        for i in range(DIM):
            rows.append([br(X, bvec(k)).get(i, F(0)) for k in g0])
    zb = nullspace(rows, len(g0))
    zvecs = []
    for w in zb:
        v = {}
        for j, k in enumerate(g0):
            if w[j]:
                v[k] = w[j]
        zvecs.append(v)
    assert len(zvecs) == dim_sl2, (L, len(zvecs), dim_sl2)
    zbr = [br(a, b) for i, a in enumerate(zvecs) for b in zvecs[i + 1:]]
    z_der = rank_of([x for x in zbr if x])
    # centre of z
    rows = []
    for a in zvecs:
        for i in range(DIM):
            rows.append([br(a, zvecs[j]).get(i, F(0)) for j in range(len(zvecs))])
    z_cent = len(nullspace(rows, len(zvecs))) if zvecs else 0
    # rank of z = dim of the centraliser in z of a generic element of z
    z_rank = 0
    if zvecs:
        rr = random.Random(7)
        best = 10 ** 9
        for _ in range(3):
            x = {}
            for a in zvecs:
                x = addv(x, smul(F(rr.randint(1, 20)), a))
            rows = []
            for i in range(DIM):
                rows.append([br(x, zvecs[j]).get(i, F(0)) for j in range(len(zvecs))])
            best = min(best, len(nullspace(rows, len(zvecs))))
        z_rank = best
    zss = independent_basis([x for x in zbr if x])
    zideals = ideal_structure(zss) if zss else []
    z_ideal_dims = sorted(d for _, d in zideals) if zideals else []
    z_name = ("+".join(name_simple(d) for d in z_ideal_dims) if z_ideal_dims else "0") + \
             (f"+u(1)^{z_cent}" if z_cent else "")
    C_name = ideal_names + (f"+u(1)^{C_centre}" if C_centre else "")
    return dict(labels=list(L), mult={str(k): v for k, v in sorted(mult.items())},
                orbit_dim=orbdim, dim_cent_sl2=dim_sl2, z_derived=z_der, z_centre=z_cent,
                z_rank=z_rank, z_ideal_dims=z_ideal_dims, z_type=z_name,
                dim_cent_2T_char=dim_char, dim_cent_2T_built=dim_built,
                cent_2T_derived=dim_derived, abelian=(dim_derived == 0),
                C_centre=C_centre, C_rank=C_rank, C_KC_rank=KC_rank, C_Ke6_rank=KE6_rank,
                C_ideal_dims=ideal_dims, C_type=C_name, C_n_invariant_forms=nforms,
                meridian_jordan=sorted([n + 1] * m for n, m in mult.items()) and
                sorted([n + 1 for n, m in mult.items() for _ in range(m)], reverse=True),
                reductive_check=(dim_derived + C_centre == nC))


# ================================================================ run
print("[3] analysing each orbit (exact) ...")
rows_out = []
for L, H, e, f in orbits:
    if not any(L):
        rows_out.append(dict(labels=list(L), mult={"0": 78}, orbit_dim=0, dim_cent_sl2=78,
                             z_derived=78, z_centre=0, z_rank=6, z_type="e6", z_ideal_dims=[78],
                             dim_cent_2T_char=78, dim_cent_2T_built=78, cent_2T_derived=78,
                             abelian=False, C_centre=0, C_rank=6, C_KC_rank=78, C_Ke6_rank=78,
                             C_ideal_dims=[78], C_type="E6", reductive_check=True,
                             note="zero orbit: 2T -> identity; not an embedding"))
        continue
    r = analyse(L, H, e, f)
    rows_out.append(r)
    print(f"    {''.join(map(str,L))}  orbdim {r['orbit_dim']:>2}  "
          f"Cent(sl2) {r['dim_cent_sl2']:>2} = {r['z_type']:<16} "
          f"Cent(2T) {r['dim_cent_2T_char']:>2}/{r['dim_cent_2T_built']:>2} = "
          f"{r['C_type']:<16} [C,C] {r['cent_2T_derived']:>2}  "
          f"{'ABELIAN' if r['abelian'] else 'NON-ABELIAN'}")

rows_out.sort(key=lambda r: r["orbit_dim"])
json.dump(dict(n_orbits=len(rows_out), orbits=rows_out),
          open(os.path.join(HERE, "results.json"), "w"), indent=1)

print()
print("=" * 108)
print(f"{'wDyn':<8}{'orbdim':>7}{'dimC(sl2)':>10}  {'z type':<18}"
      f"{'dimC(2T)':>9}{'[C,C]':>7}  {'Cent(2T) type':<20} verdict")
print("=" * 108)
for r in rows_out:
    print(f"{''.join(map(str,r['labels'])):<8}{r['orbit_dim']:>7}{r['dim_cent_sl2']:>10}  "
          f"{r['z_type']:<18}{r['dim_cent_2T_char']:>9}{r['cent_2T_derived']:>7}  "
          f"{r['C_type']:<20} {'ABELIAN' if r['abelian'] else 'NON-ABELIAN'}")
print("=" * 108)
nab = [r for r in rows_out if not r["abelian"] and any(r["labels"])]
print(f"orbits with NON-ABELIAN Cent(2T): {len(nab)} of {len(rows_out)-1} nonzero orbits")
print(f"character count == constructed count on every orbit: "
      f"{all(r['dim_cent_2T_char']==r['dim_cent_2T_built'] for r in rows_out)}")
print(f"reductivity check (dim[C,C]+dim z(C) = dim C) on every orbit: "
      f"{all(r['reductive_check'] for r in rows_out)}")
print(f"K_e6 restricted to Cent(2T) nondegenerate on every orbit: "
      f"{all(r['C_Ke6_rank']==r['dim_cent_2T_built'] for r in rows_out)}")
ew = [r for r in rows_out if r['cent_2T_derived'] == 3 and r['C_centre'] == 1]
print(f"orbits whose Cent(2T) is EXACTLY su(2)+u(1): "
      f"{[''.join(map(str,r['labels'])) for r in ew]}")
sm = [r for r in rows_out if sorted(r['C_ideal_dims']) == [3, 8]]
print(f"orbits whose Cent(2T) has semisimple part su(3)+su(2): "
      f"{[(''.join(map(str,r['labels'])), r['C_type']) for r in sm]}")
