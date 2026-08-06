#!/usr/bin/env python3
"""
B932 -- R-EMB, the chain-selection cell (structure only -- never a number).

LEG 1 (the verification, in-house): the (E6)_1 conformal-embedding chain
    (E6)_1  >  (A2)_2 x (G2)_1  >  SU(3)_2 x SU(2)_3 x SU(2)_1
and the exact branching of the 27.  Claimed (Chat-1, masterplan R-EMB
registration 2026-08-05; wall W18 of B926/ANATOMY.md):
    27 = (3,2,2) + (3,3,1) + (6,1,1)   -- no color singlets, no leptons.

LEG 2 (the selection question): does any banked structure realize the
conformal chain's subalgebra su(3)+su(2)+su(2) as a centralizer/wall?
Sweep of the banked centralizer lattice (B854/B874/B877/B892/B897/B909
typings) + the regularity (Levi) obstruction.

CONVENTIONS BLOCK (WORKING_RULES rule 4 -- every choice declared):
  * Split octonions O = Zorn vector matrices over Q: x = (a, v, w, b),
    a,b in Q, v,w in Q^3; coordinates ordered [a, v1,v2,v3, w1,w2,w3, b].
    Product: (a1,v1,w1,b1)(a2,v2,w2,b2) =
      (a1a2 + v1.w2,  a1v2 + b2v1 - w1 x w2,  a2w1 + b1w2 + v1 x v2,
       b1b2 + w1.v2).
    Norm n(x) = ab - v.w;  conjugate xbar = (b, -v, -w, a);  t(x) = a+b.
    The sign convention is VERIFIED at runtime (composition n(xy)=n(x)n(y),
    alternativity); a failure aborts the run.
  * The complexified statement "27 of E6 branches as ..." is a statement
    about complex representations; it is computed here in the SPLIT forms
    over Q (same complexification -- branching is a complex-rep fact,
    independent of real form).
  * J = J3(O): 3x3 Hermitian (X_ji = conj(X_ij), diagonal in Q.1), dim 27.
    Jordan product X o Y = (XY + YX)/2; generic (Freudenthal) cubic norm
    N(X) = (t1^3 - 3 t1 t2 + 2 t3)/6 with tk = tr(X^(o k)); polarized
    trilinear theta with theta(x,x,x) = 6 N(x) via inclusion-exclusion.
  * sl(3) acts by rho(A): X -> A X + X A^T (A in sl3(Q), scalar entries);
    g2 = Der(O) acts entrywise.  Both are verified to annihilate theta,
    i.e. to lie in Lie(Inv(N)); that Lie algebra's dimension is pinned to
    exactly 78 in-house (see the sandwich below).  Its identification as
    (split) e6 is the classical Chevalley--Schafer theorem (cited), and is
    corroborated by B854's independent exact Chevalley e6 (dim 78, same
    exponents).
  * su(2) x su(2) in g2: the stabilizer of the split quaternion subalgebra
    H = span{E1, U1, V1, E2} (= M2(Q)); ideals split over Q.
  * Mod-p linear algebra appears ONLY in the two valid directions:
    rank_p <= rank_Q.  Upper bound on dim Lie(Inv theta): dim_Q <= dim_p
    (nullity of the exact integer constraint system, two primes).  Lower
    bound: exactly-theta-invariant integer vectors whose mod-p rank is 78
    force dim_Q >= 78.  Every verdict-carrying quantity is exact over Q.
  * h_dual(E6) = 12 is taken from B854's banked exponents [1,4,5,7,8,11]
    (simply-laced: h = h_dual = 1 + max exponent -- classical relation).
    h_dual(A2)=3, h_dual(A1)=2, h_dual(G2)=4 (classical).
  * Levels: k_sub = j * k_e6 with k_e6 = 1; embedding index j of an sl2
    coroot h computed as kappa_e6(h,h)/(4 h_dual(E6)) with kappa the
    Killing form of the constructed 78-dim algebra (exact).
  * TWO-OUTCOME CELL (vacuity-checked): outcome B ("the conformal
    subalgebra IS realized by a banked wall") is statable -- the Levi type
    A2+A1+A1 exists in e6 (subdiagram check computed below), so the sweep
    could in principle have found it.  Outcome A = not realized.

House rules: exact arithmetic for verdicts; no absolute machine paths
(repo-root-relative I/O via __file__); structure only, never a measured
number; nothing here contacts any physical quantity.
"""

import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": str(detail)})
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f" -- {detail}" if detail else ""))
    return bool(ok)


# ----------------------------------------------------------------------
# 1. Split octonions (Zorn vector matrices) over Q
# ----------------------------------------------------------------------

def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def octmul(x, y):
    a1, v1, w1, b1 = x[0], x[1:4], x[4:7], x[7]
    a2, v2, w2, b2 = y[0], y[1:4], y[4:7], y[7]
    cw = cross(w1, w2)
    cv = cross(v1, v2)
    a = a1 * a2 + dot(v1, w2)
    v = tuple(a1 * v2[i] + b2 * v1[i] - cw[i] for i in range(3))
    w = tuple(a2 * w1[i] + b1 * w2[i] + cv[i] for i in range(3))
    b = b1 * b2 + dot(w1, v2)
    return (a,) + v + w + (b,)


def octconj(x):
    return (x[7], -x[1], -x[2], -x[3], -x[4], -x[5], -x[6], x[0])


def octnorm(x):
    return x[0] * x[7] - dot(x[1:4], x[4:7])


def octtrace(x):
    return x[0] + x[7]


OUNIT = (1, 0, 0, 0, 0, 0, 0, 1)
OBASIS = [tuple(1 if i == k else 0 for i in range(8)) for k in range(8)]


def oadd(x, y):
    return tuple(x[i] + y[i] for i in range(8))


def oscale(c, x):
    return tuple(c * x[i] for i in range(8))


def verify_octonions():
    import random
    rng = random.Random(93201)
    ok_unit = all(octmul(OUNIT, e) == e and octmul(e, OUNIT) == e
                  for e in OBASIS)
    check("oct: two-sided unit", ok_unit)
    ok_comp = True
    ok_alt = True
    ok_conj = True
    for _ in range(60):
        x = tuple(rng.randint(-5, 5) for _ in range(8))
        y = tuple(rng.randint(-5, 5) for _ in range(8))
        if octnorm(octmul(x, y)) != octnorm(x) * octnorm(y):
            ok_comp = False
        xx = octmul(x, x)
        if octmul(xx, y) != octmul(x, octmul(x, y)):
            ok_alt = False
        if octmul(octmul(y, x), x) != octmul(y, xx):
            ok_alt = False
        if octconj(octmul(x, y)) != octmul(octconj(y), octconj(x)):
            ok_conj = False
        if octmul(x, octconj(x)) != oscale(octnorm(x), OUNIT):
            ok_conj = False
    check("oct: composition n(xy)=n(x)n(y) (60 random exact)", ok_comp)
    check("oct: alternativity (60 random exact)", ok_alt)
    check("oct: conjugation anti-automorphism + x xbar = n(x) 1", ok_conj)
    return ok_unit and ok_comp and ok_alt and ok_conj


# ----------------------------------------------------------------------
# 2. Exact linear algebra over Q
# ----------------------------------------------------------------------

def rref(rows, ncols):
    """Exact RREF over Fractions. rows: list of sequences. Returns
    (rank, pivot_cols, reduced rows as lists of Fractions)."""
    mat = [[Fraction(x) for x in r] for r in rows]
    pivots = []
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(mat)):
            if mat[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        pv = mat[r][c]
        mat[r] = [x / pv for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] != 0:
                f = mat[i][c]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[r])]
        pivots.append(c)
        r += 1
        if r == len(mat):
            break
    return r, pivots, mat[:r]


def nullspace(rows, ncols):
    """Exact rational nullspace basis (list of Fraction tuples)."""
    rank, pivots, red = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -red[i][fc]
        basis.append(tuple(v))
    return basis


def clear_denoms(vec):
    from math import lcm
    den = 1
    for x in vec:
        den = lcm(den, Fraction(x).denominator)
    return tuple(int(Fraction(x) * den) for x in vec)


def rank_mod_p(mat_int, p):
    """Row-echelon rank of an integer numpy matrix mod prime p (valid
    use: rank_p <= rank_Q)."""
    m = np.array(mat_int, dtype=np.int64) % p
    rows, cols = m.shape
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        nz = np.nonzero(m[r:, c])[0]
        if len(nz) == 0:
            continue
        piv = r + nz[0]
        m[[r, piv]] = m[[piv, r]]
        inv = pow(int(m[r, c]), p - 2, p)
        m[r] = (m[r] * inv) % p
        col = m[r + 1:, c].copy()
        mask = col != 0
        if mask.any():
            m[r + 1:][mask] = (m[r + 1:][mask] - np.outer(col[mask], m[r])) % p
        r += 1
    return r


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# ----------------------------------------------------------------------
# 3. g2 = Der(O), exact
# ----------------------------------------------------------------------

def build_der():
    M = [[octmul(OBASIS[i], OBASIS[j]) for j in range(8)] for i in range(8)]
    rows = []
    for i in range(8):
        for j in range(8):
            for r in range(8):
                row = [0] * 64
                for q in range(8):
                    row[r * 8 + q] += M[i][j][q]
                for pidx in range(8):
                    row[pidx * 8 + i] -= M[pidx][j][r]
                    row[pidx * 8 + j] -= M[i][pidx][r]
                rows.append(row)
    basis = nullspace(rows, 64)
    ders = []
    for v in basis:
        vi = clear_denoms(v)
        D = [[vi[r * 8 + c] for c in range(8)] for r in range(8)]
        ders.append(np.array(D, dtype=np.int64))
    return ders


def der_checks(ders):
    check("g2: dim Der(O) = 14", len(ders) == 14, f"dim={len(ders)}")
    ok_unit = all((D @ np.array(OUNIT)).tolist() == [0] * 8 for D in ders)
    check("g2: derivations kill the unit", ok_unit)
    C = np.zeros((8, 8), dtype=np.int64)
    for k in range(8):
        cc = octconj(OBASIS[k])
        for r in range(8):
            C[r, k] = cc[r]
    ok_conj = all(np.array_equal(D @ C, C @ D) for D in ders)
    check("g2: derivations commute with octonion conjugation", ok_conj)
    flat = [D.flatten().tolist() for D in ders]
    brk = []
    for i in range(14):
        for j in range(i + 1, 14):
            B = ders[i] @ ders[j] - ders[j] @ ders[i]
            brk.append(B.flatten().tolist())
    rank_all, _, _ = rref(flat + brk, 64)
    check("g2: closed under bracket (exact rank stays 14)", rank_all == 14,
          f"rank={rank_all}")
    return ok_unit and ok_conj and rank_all == 14


# ----------------------------------------------------------------------
# 4. J = J3(O): basis, Jordan structure, cubic norm, polarization
# ----------------------------------------------------------------------

SLOTS = [(0, 1), (0, 2), (1, 2)]


def jb_matrix(t):
    """27-basis element as 3x3 octonionic matrix."""
    Z = [[(0,) * 8 for _ in range(3)] for _ in range(3)]
    if t < 3:
        Z[t][t] = OUNIT
        return Z
    t -= 3
    s, u = divmod(t, 8)
    i, j = SLOTS[s]
    Z[i][j] = OBASIS[u]
    Z[j][i] = octconj(OBASIS[u])
    return Z


JB = [jb_matrix(t) for t in range(27)]


def matadd(X, Y):
    return [[oadd(X[i][j], Y[i][j]) for j in range(3)] for i in range(3)]


def matscale(c, X):
    return [[oscale(c, X[i][j]) for j in range(3)] for i in range(3)]


def matmul3(X, Y):
    R = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            acc = (0,) * 8
            for k in range(3):
                acc = oadd(acc, octmul(X[i][k], Y[k][j]))
            R[i][j] = acc
    return R


def tr2(X):
    """2 * tr(X) = sum of octonion traces of the diagonal."""
    return sum(octtrace(X[i][i]) for i in range(3))


def coordize(X, strict=True):
    """3x3 octonionic Hermitian matrix -> exact 27-coordinate list."""
    v = [Fraction(0)] * 27
    for i in range(3):
        d = X[i][i]
        if strict:
            assert d[1:7] == (0,) * 6 and d[0] == d[7], f"non-scalar diag {d}"
        v[i] = Fraction(d[0] + d[7], 2)
    for s, (i, j) in enumerate(SLOTS):
        if strict:
            assert X[j][i] == octconj(X[i][j]), "not Hermitian"
        for u in range(8):
            v[3 + s * 8 + u] = Fraction(X[i][j][u])
    return v


def from_coords(vec):
    Z = [[(0,) * 8 for _ in range(3)] for _ in range(3)]
    X = [row[:] for row in Z]
    for t in range(27):
        c = vec[t]
        if c == 0:
            continue
        B = JB[t]
        X = matadd(X, matscale(c, B))
    return X


_NCACHE = {}


def norm_of(vec):
    """Freudenthal cubic N on an exact 27-coordinate vector."""
    key = tuple(vec)
    if key in _NCACHE:
        return _NCACHE[key]
    X = from_coords(vec)
    X2 = matmul3(X, X)
    t1 = Fraction(tr2(X), 2) if isinstance(tr2(X), int) else tr2(X) / 2
    T2 = tr2(X2)
    t2 = Fraction(T2, 2) if isinstance(T2, int) else T2 / 2
    X3a = matmul3(X2, X)
    X3b = matmul3(X, X2)
    T3 = tr2(X3a) + tr2(X3b)
    t3 = Fraction(T3, 4) if isinstance(T3, int) else T3 / 4
    N = (t1 ** 3 - 3 * t1 * t2 + 2 * t3) / 6
    _NCACHE[key] = N
    return N


def basis_vec(t, scale=1):
    v = [0] * 27
    v[t] = scale
    return v


def vsum(*vecs):
    out = [0] * 27
    for v in vecs:
        for i in range(27):
            out[i] += v[i]
    return out


def build_theta():
    """theta(i,j,k) for i<=j<=k with theta(x,x,x) = 6 N(x)."""
    theta = {}
    for i in range(27):
        for j in range(i, 27):
            for k in range(j, 27):
                u, v, w = basis_vec(i), basis_vec(j), basis_vec(k)
                val = (norm_of(vsum(u, v, w))
                       - norm_of(vsum(u, v)) - norm_of(vsum(u, w))
                       - norm_of(vsum(v, w))
                       + norm_of(u) + norm_of(v) + norm_of(w))
                if val != 0:
                    theta[(i, j, k)] = val
    return theta


def th(theta, i, j, k):
    return theta.get(tuple(sorted((i, j, k))), Fraction(0))


def theta_invariant(theta, Mcols):
    """Check sum theta(M e_i, e_j, e_k)+... = 0 for all i<=j<=k.
    Mcols[t] = list of (row, val) for column t of M."""
    for i in range(27):
        for j in range(i, 27):
            for k in range(j, 27):
                s = Fraction(0)
                for (m, val) in Mcols[i]:
                    s += val * th(theta, m, j, k)
                for (m, val) in Mcols[j]:
                    s += val * th(theta, i, m, k)
                for (m, val) in Mcols[k]:
                    s += val * th(theta, i, j, m)
                if s != 0:
                    return False
    return True


def cols_of(mat27):
    cols = []
    for t in range(27):
        col = []
        for r in range(27):
            x = mat27[r][t]
            if x != 0:
                col.append((r, Fraction(x)))
        cols.append(col)
    return cols


# ----------------------------------------------------------------------
# 5. The two actions on the 27
# ----------------------------------------------------------------------

def rho_matrix(A):
    """sl3 action X -> A X + X A^T as an exact 27x27 matrix (columns =
    images of the 27 basis)."""
    out = [[Fraction(0)] * 27 for _ in range(27)]
    for t in range(27):
        X = JB[t]
        Y = [[(0,) * 8 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                acc = (0,) * 8
                for k in range(3):
                    if A[i][k]:
                        acc = oadd(acc, oscale(A[i][k], X[k][j]))
                    if A[j][k]:
                        acc = oadd(acc, oscale(A[j][k], X[i][k]))
                Y[i][j] = acc
        img = coordize(Y)
        for r in range(27):
            out[r][t] = img[r]
    return out


def der27_matrix(D):
    """g2 entrywise action as an exact 27x27 matrix."""
    out = [[Fraction(0)] * 27 for _ in range(27)]
    for t in range(27):
        X = JB[t]
        Y = [[tuple(int(z) for z in (D @ np.array(X[i][j], dtype=np.int64)))
              for j in range(3)] for i in range(3)]
        img = coordize(Y)
        for r in range(27):
            out[r][t] = img[r]
    return out


def mat_to_np(mat27, scale=1):
    a = np.zeros((27, 27), dtype=np.int64)
    for r in range(27):
        for c in range(27):
            x = Fraction(mat27[r][c]) * scale
            assert x.denominator == 1
            a[r, c] = int(x)
    return a


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------

def main():
    results = {"arc": "B932", "cell": "R-EMB chain selection",
               "leg1": {}, "leg2": {}, "checks": CHECKS}

    print("== LEG 1: the conformal chain, in-house ==")
    print("-- split octonions (Zorn) --")
    verify_octonions()

    print("-- g2 = Der(O) --")
    ders = build_der()
    der_checks(ders)

    print("-- J3(O), cubic norm, polarization --")
    NI = norm_of(vsum(basis_vec(0), basis_vec(1), basis_vec(2)))
    check("J: N(identity) = 1", NI == 1, f"N(I)={NI}")
    Xd = vsum(basis_vec(0, 1), basis_vec(1, 1), basis_vec(2, 1))
    nd = norm_of([2 if i == 0 else (3 if i == 1 else (5 if i == 2 else 0))
                  for i in range(27)])
    check("J: N(diag(2,3,5)) = 30 (det on diagonals)", nd == 30, f"N={nd}")
    theta = build_theta()
    tsum = norm_of(basis_vec(0))  # touch cache
    x_spot = [1, 2, 0, 3, 0, 0, 0, -1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0,
              0, 0, 0, 0, 1, 0, 0]
    lhs = Fraction(0)
    for i in range(27):
        for j in range(27):
            for k in range(27):
                if x_spot[i] and x_spot[j] and x_spot[k]:
                    lhs += x_spot[i] * x_spot[j] * x_spot[k] * th(theta, i, j, k)
    check("J: theta(x,x,x) = 6 N(x) on a spot vector",
          lhs == 6 * norm_of(x_spot))

    print("-- the 22 generators: sl3 (+) g2 --")
    E = lambda i, j: [[1 if (r, c) == (i, j) else 0 for c in range(3)]
                      for r in range(3)]
    H1 = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
    H2 = [[0, 0, 0], [0, 1, 0], [0, 0, -1]]
    sl3_mats_A = [E(0, 1), E(1, 0), E(0, 2), E(2, 0), E(1, 2), E(2, 1), H1, H2]
    sl3_27 = [rho_matrix(A) for A in sl3_mats_A]
    g2_27 = [der27_matrix(D) for D in ders]

    # rho is a homomorphism: [rho(A),rho(B)] = rho([A,B]) for A,B in basis
    def brk3(A, B):
        return [[sum(A[i][k] * B[k][j] - B[i][k] * A[k][j] for k in range(3))
                 for j in range(3)] for i in range(3)]

    np_sl3 = [mat_to_np(m) for m in sl3_27]
    ok_hom = True
    for a in range(8):
        for b in range(8):
            lhs_m = np_sl3[a] @ np_sl3[b] - np_sl3[b] @ np_sl3[a]
            rhs_m = mat_to_np(rho_matrix(brk3(sl3_mats_A[a], sl3_mats_A[b])))
            if not np.array_equal(lhs_m, rhs_m):
                ok_hom = False
    check("sl3: rho is a Lie homomorphism (all 64 basis pairs)", ok_hom)

    np_g2 = [mat_to_np(m) for m in g2_27]
    ok_comm = all(np.array_equal(np_sl3[a] @ np_g2[d], np_g2[d] @ np_sl3[a])
                  for a in range(8) for d in range(14))
    check("[sl3, g2] = 0 on the 27 (all 8x14 pairs, exact)", ok_comm)

    gens22 = sl3_27 + g2_27
    ok_inv = all(theta_invariant(theta, cols_of(m)) for m in gens22)
    check("all 22 generators annihilate theta (land in Lie(Inv N))", ok_inv)

    flat22 = [mat_to_np(m).flatten() for m in gens22]
    p1, p2 = 46337, 46327
    assert is_prime(p1) and is_prime(p2)
    r22 = rank_mod_p(np.array(flat22), p1)
    check("the 22 generators are independent (rank_p=22 => rank_Q=22)",
          r22 == 22, f"rank={r22}")

    print("-- the e6 sandwich: dim Lie(Inv theta) = 78 exactly --")
    # L_a for the 26 trace-0 elements (x2 to stay integral), plus inner
    # derivations [L_a, L_b]; each L_a verified theta-invariant exactly.
    JT = {}
    for s in range(27):
        for t in range(s, 27):
            P = matadd(matmul3(JB[s], JB[t]), matmul3(JB[t], JB[s]))
            JT[(s, t)] = coordize(P)  # = 2 (jb_s o jb_t)

    def L2_matrix(avec):
        """2 L_a as a 27x27 integer matrix, a given in coordinates."""
        out = np.zeros((27, 27), dtype=np.int64)
        for t in range(27):
            img = [Fraction(0)] * 27
            for s in range(27):
                if avec[s] == 0:
                    continue
                key = (min(s, t), max(s, t))
                jt = JT[key]
                for r in range(27):
                    img[r] += avec[s] * jt[r]
            for r in range(27):
                assert img[r].denominator == 1
                out[r, t] = int(img[r])
        return out

    trace0 = []
    v = [0] * 27; v[0], v[1] = 1, -1; trace0.append(v)
    v = [0] * 27; v[1], v[2] = 1, -1; trace0.append(v)
    for t in range(3, 27):
        v = [0] * 27; v[t] = 1; trace0.append(v)
    L_mats = [L2_matrix(a) for a in trace0]
    ok_Linv = True
    for Lm in L_mats:
        colsL = []
        for t in range(27):
            col = [(r, Fraction(int(Lm[r, t]))) for r in range(27)
                   if Lm[r, t] != 0]
            colsL.append(col)
        if not theta_invariant(theta, colsL):
            ok_Linv = False
            break
    check("all 26 L_a (trace-0 Jordan mult.) annihilate theta", ok_Linv)

    span_vecs = [m.flatten() for m in
                 ([mat_to_np(m) for m in gens22] + L_mats)]
    for i in range(26):
        for j in range(i + 1, 26):
            B = L_mats[i] @ L_mats[j] - L_mats[j] @ L_mats[i]
            span_vecs.append(B.flatten())
    span_arr = np.array(span_vecs)
    r_lo_1 = rank_mod_p(span_arr, p1)
    r_lo_2 = rank_mod_p(span_arr, p2)
    # brackets of theta-invariant maps are theta-invariant (Lie-subalgebra
    # lemma, classical one-liner) -- so every span vector is an exact
    # element of Lie(Inv theta); rank_p <= rank_Q gives dim_Q >= 78.
    check("e6 lower bound: exhibited invariant span has rank 78 "
          "(both primes)", r_lo_1 == 78 and r_lo_2 == 78,
          f"rank@{p1}={r_lo_1}, rank@{p2}={r_lo_2}")

    # Upper bound: the exact integer constraint system for theta-invariance
    # (unknown M in gl(27), 729 unknowns).  dim_Q <= 729 - rank_p.
    con_rows = np.zeros((3654, 729), dtype=np.int64)
    ridx = 0
    for i in range(27):
        for j in range(i, 27):
            for k in range(j, 27):
                row = con_rows[ridx]
                for m in range(27):
                    a1 = th(theta, m, j, k)
                    if a1:
                        assert a1.denominator == 1
                        row[m * 27 + i] += int(a1)
                    a2 = th(theta, i, m, k)
                    if a2:
                        row[m * 27 + j] += int(a2)
                    a3 = th(theta, i, j, m)
                    if a3:
                        row[m * 27 + k] += int(a3)
                ridx += 1
    r_up_1 = rank_mod_p(con_rows, p1)
    r_up_2 = rank_mod_p(con_rows, p2)
    check("e6 upper bound: constraint rank 651 at two primes "
          "(=> dim_Q <= 78)", r_up_1 == 651 and r_up_2 == 651,
          f"rank@{p1}={r_up_1}, rank@{p2}={r_up_2}")
    dim_e6 = 78 if (r_lo_1 == 78 and r_up_1 == 651 and r_up_2 == 651) else None
    check("dim Lie(Inv N) = 78 EXACTLY (sandwich closed)", dim_e6 == 78)
    results["leg1"]["dim_inv_algebra"] = dim_e6

    print("-- su(2) x su(2) in g2 (stabilizer of the split quaternions) --")
    # H = coords {0 (a), 1 (v1), 4 (w1), 7 (b)}; complement rows {2,3,5,6}.
    hcols = [0, 1, 4, 7]
    mrows = [2, 3, 5, 6]
    rows = []
    for r in mrows:
        for c in hcols:
            rows.append([int(ders[d][r, c]) for d in range(14)])
    s_basis_c = nullspace(rows, 14)
    check("stab(H) in g2 has dim 6 (= so(4)-type)", len(s_basis_c) == 6,
          f"dim={len(s_basis_c)}")
    s_ders = []
    for cvec in s_basis_c:
        ci = clear_denoms(cvec)
        D = sum(int(ci[d]) * ders[d] for d in range(14))
        s_ders.append(D)

    # b = the ideal acting trivially on Im H = span{q=e0-e7, U1=e1, V1=e4}
    imh = [np.array([1, 0, 0, 0, 0, 0, 0, -1], dtype=np.int64),
           np.array([0, 1, 0, 0, 0, 0, 0, 0], dtype=np.int64),
           np.array([0, 0, 0, 0, 1, 0, 0, 0], dtype=np.int64)]
    rows = []
    for x in imh:
        for r in range(8):
            rows.append([int((s_ders[d] @ x)[r]) for d in range(6)])
    b_c = nullspace(rows, 6)
    check("kernel-on-ImH ideal b has dim 3", len(b_c) == 3,
          f"dim={len(b_c)}")
    b_ders = []
    for cvec in b_c:
        ci = clear_denoms(cvec)
        b_ders.append(sum(int(ci[d]) * s_ders[d] for d in range(6)))

    # a = centralizer of b in s
    rows = []
    for Bd in b_ders:
        for r in range(8):
            for c in range(8):
                rows.append([int((s_ders[d] @ Bd - Bd @ s_ders[d])[r, c])
                             for d in range(6)])
    a_c = nullspace(rows, 6)
    check("centralizer ideal a has dim 3", len(a_c) == 3, f"dim={len(a_c)}")
    a_ders = []
    for cvec in a_c:
        ci = clear_denoms(cvec)
        a_ders.append(sum(int(ci[d]) * s_ders[d] for d in range(6)))
    ok_ab = all(np.array_equal(A @ B, B @ A) for A in a_ders for B in b_ders)
    check("[a, b] = 0 (all 9 pairs)", ok_ab)
    fl = [D.flatten().tolist() for D in a_ders + b_ders]
    rk_ab, _, _ = rref(fl, 64)
    check("s = a (+) b (exact rank 6)", rk_ab == 6, f"rank={rk_ab}")

    def sl2_triple(ideal_ders, action_vectors, h_conditions=None):
        """Find an exact split sl2 triple (e,h,f) in a 3-dim ideal."""
        # h by explicit action conditions if given, else scan
        n = len(ideal_ders)
        if h_conditions is not None:
            rows_, rhs = [], []
            for (x, lam) in h_conditions:
                for r in range(8):
                    rows_.append([int((ideal_ders[d] @ x)[r])
                                  for d in range(n)])
                    rhs.append(int(lam * x[r]))
            aug = [row + [rh] for row, rh in zip(rows_, rhs)]
            rank_a, piv, red = rref(aug, n + 1)
            assert n not in piv, "inconsistent h-conditions"
            sol = [Fraction(0)] * n
            for i, pc in enumerate(piv):
                sol[pc] = red[i][n]
            h = sum(sol[d] * ideal_ders[d].astype(object)
                    for d in range(n))
        else:
            h = None
            for combo in itertools.product(range(-4, 5), repeat=n):
                if all(c == 0 for c in combo):
                    continue
                X = sum(int(combo[d]) * ideal_ders[d] for d in range(n))
                admats = []
                for d in range(n):
                    Br = X @ ideal_ders[d] - ideal_ders[d] @ X
                    admats.append(Br)
                # coordinates of brackets in the ideal basis
                flat_basis = [ideal_ders[d].flatten().tolist()
                              for d in range(n)]
                admat = []
                for Bm in admats:
                    aug_rows = [list(col) for col in
                                zip(*flat_basis, Bm.flatten().tolist())]
                    rk_, piv_, red_ = rref(aug_rows, n + 1)
                    if n in piv_:
                        admat = None
                        break
                    col = [Fraction(0)] * n
                    for ii, pc in enumerate(piv_):
                        col[pc] = red_[ii][n]
                    admat.append(col)
                if admat is None:
                    continue
                A = [[admat[c][r] for c in range(n)] for r in range(n)]
                tr2_ = sum(sum(A[i][k] * A[k][i] for k in range(n))
                           for i in range(n))
                c_ = tr2_ / 2
                if c_ <= 0:
                    continue
                num, den = Fraction(c_).numerator, Fraction(c_).denominator
                import math
                sn, sd = math.isqrt(num), math.isqrt(den)
                if sn * sn == num and sd * sd == den:
                    s_ = Fraction(sn, sd)
                    h = X.astype(object) * Fraction(2, 1) / s_
                    break
            assert h is not None, "no rational split h found in scan"
        # e, f as ad_h eigenvectors inside the ideal
        flat_basis = [ideal_ders[d].flatten().tolist() for d in range(n)]

        def in_ideal_coords(M):
            aug_rows = [list(col) for col in
                        zip(*flat_basis, M.flatten().tolist())]
            rk_, piv_, red_ = rref(aug_rows, n + 1)
            assert n not in piv_, "not in ideal"
            col = [Fraction(0)] * n
            for ii, pc in enumerate(piv_):
                col[pc] = red_[ii][n]
            return col

        adcols = []
        for d in range(n):
            Bm = h @ ideal_ders[d].astype(object) \
                - ideal_ders[d].astype(object) @ h
            adcols.append(in_ideal_coords(Bm))
        A = [[adcols[c][r] for c in range(n)] for r in range(n)]
        eig = {}
        for lam in (2, -2):
            rows_ = [[A[r][c] - (lam if r == c else 0) for c in range(n)]
                     for r in range(n)]
            ns = nullspace(rows_, n)
            assert len(ns) == 1, f"eigenvalue {lam} multiplicity != 1"
            eig[lam] = sum(Fraction(ns[0][d])
                           * ideal_ders[d].astype(object) for d in range(n))
        e_, f_ = eig[2], eig[-2]
        # normalize [e,f] = h
        Bm = e_ @ f_ - f_ @ e_
        cb = in_ideal_coords(np.array(
            [[Bm[r, c] for c in range(8)] for r in range(8)], dtype=object))
        ch = in_ideal_coords(h)
        ratios = [cb[d] / ch[d] for d in range(n) if ch[d] != 0]
        assert all(r == ratios[0] for r in ratios), "[e,f] not prop. to h"
        gam = ratios[0]
        f_ = f_ / gam
        okt = (np.array_equal(h @ e_ - e_ @ h, 2 * e_)
               and np.array_equal(h @ f_ - f_ @ h, -2 * f_)
               and np.array_equal(e_ @ f_ - f_ @ e_, h))
        return h, e_, f_, okt

    q = imh[0]; U1 = imh[1]; V1 = imh[2]
    h_a, e_a, f_a, ok_ta = sl2_triple(
        a_ders, None, h_conditions=[(U1, 2), (V1, -2), (q, 0)])
    check("sl2 triple in a (h: U1->2U1, V1->-2V1, q->0)", ok_ta)
    h_b, e_b, f_b, ok_tb = sl2_triple(b_ders, None, h_conditions=None)
    check("sl2 triple in b (rational split scan)", ok_tb)

    print("-- weights of the 27 under (h1, h2, h_a, h_b) --")

    def lift_obj(D8):
        out = [[Fraction(0)] * 27 for _ in range(27)]
        for t in range(27):
            X = JB[t]
            Y = [[tuple(sum(Fraction(D8[r_, c_]) * X[i][j][c_]
                            for c_ in range(8)) for r_ in range(8))
                  for j in range(3)] for i in range(3)]
            img = coordize(Y, strict=False)
            for r in range(27):
                out[r][t] = img[r]
        return out

    ha27 = lift_obj(h_a)
    hb27 = lift_obj(h_b)
    h1_27, h2_27 = sl3_27[6], sl3_27[7]

    def fmat(m):
        return [[Fraction(x) for x in row] for row in m]

    def mateq(A, B):
        return all(A[i][j] == B[i][j] for i in range(27) for j in range(27))

    def matcomm(A, B):
        A, B = fmat(A), fmat(B)
        C = [[sum(A[i][k] * B[k][j] - B[i][k] * A[k][j] for k in range(27))
              for j in range(27)] for i in range(27)]
        return C

    Z27 = [[Fraction(0)] * 27 for _ in range(27)]
    cart = [h1_27, h2_27, ha27, hb27]
    ok_cart = all(mateq(matcomm(cart[i], cart[j]), Z27)
                  for i in range(4) for j in range(i + 1, 4))
    check("the four Cartan operators commute pairwise (exact)", ok_cart)

    # h1, h2 are diagonal on the J-basis; (h_a,h_b) act within each
    # octonion slot: joint eigenbasis on the octonion coordinate space.
    diag_ok = True
    sl3_w = {}
    for t in range(27):
        col1 = [h1_27[r][t] for r in range(27)]
        col2 = [h2_27[r][t] for r in range(27)]
        for r in range(27):
            if r != t and (col1[r] != 0 or col2[r] != 0):
                diag_ok = False
        sl3_w[t] = (col1[t], col2[t])
    check("h1, h2 diagonal on the J-basis", diag_ok)

    ha8 = [[Fraction(h_a[r, c]) for c in range(8)] for r in range(8)]
    hb8 = [[Fraction(h_b[r, c]) for c in range(8)] for r in range(8)]
    joint = {}
    total = 0
    for la in range(-2, 3):
        for lb in range(-2, 3):
            rows_ = []
            for r in range(8):
                rows_.append([ha8[r][c] - (la if r == c else 0)
                              for c in range(8)])
            for r in range(8):
                rows_.append([hb8[r][c] - (lb if r == c else 0)
                              for c in range(8)])
            ns = nullspace(rows_, 8)
            if ns:
                joint[(la, lb)] = len(ns)
                total += len(ns)
    check("joint (h_a,h_b) spectrum on O is integral and exhausts dim 8",
          total == 8, f"spectrum={joint}")
    exp_joint = {(0, 0): 2, (2, 0): 1, (-2, 0): 1,
                 (1, 1): 1, (1, -1): 1, (-1, 1): 1, (-1, -1): 1}
    check("octonion spectrum = (1+ImH) (+) M: {(0,0)x2, (+-2,0), (+-1,+-1)}",
          joint == exp_joint, f"{joint}")

    # full weight multiset of the 27
    weights = []
    for t in range(3):
        weights.append((sl3_w[t][0], sl3_w[t][1], Fraction(0), Fraction(0)))
    for s in range(3):
        base = 3 + s * 8
        wsl = sl3_w[base]  # all 8 units in a slot share the sl3 weight
        for (la, lb), mult in joint.items():
            for _ in range(mult):
                weights.append((wsl[0], wsl[1], Fraction(la), Fraction(lb)))
    weights = sorted(weights)

    # claimed multiset: (3bar,2,2) + (3bar,3,1) + (6,1,1)
    w3 = [(1, 0), (-1, 1), (0, -1)]        # weights of the 3 (V)
    w3bar = [(-a, -b) for (a, b) in w3]
    w6 = [(a1 + a2, b1 + b2) for (a1, b1), (a2, b2)
          in itertools.combinations_with_replacement(w3, 2)]
    claimed = []
    for (x, y) in w3bar:
        for la in (1, -1):
            for lb in (1, -1):
                claimed.append((x, y, la, lb))        # (3bar, 2, 2)
        for la in (2, 0, -2):
            claimed.append((x, y, la, 0))             # (3bar, 3, 1)
    for (x, y) in w6:
        claimed.append((x, y, 0, 0))                  # (6, 1, 1)
    claimed = sorted([(Fraction(a), Fraction(b), Fraction(c), Fraction(d))
                      for (a, b, c, d) in claimed])
    ok_branch = weights == claimed
    check("BRANCHING: 27 = (3bar,2,2) + (3bar,3,1) + (6,1,1) "
          "(exact weight multisets)", ok_branch)
    n_singlet = sum(1 for w in weights if w[0] == 0 and w[1] == 0)
    check("NO COLOR SINGLETS: zero sl3-weight-(0,0) states in the 27",
          n_singlet == 0, f"count={n_singlet}")
    results["leg1"]["branching"] = "(3bar,2,2) + (3bar,3,1) + (6,1,1)"
    results["leg1"]["conjugation_note"] = (
        "triplets and sextet are OPPOSITELY conjugated (invariant fact; "
        "the other fundamental gives (3,2,2)+(3,3,1)+(6bar,1,1)); the "
        "registered same-handed label '(3,2,2)+(3,3,1)+(6,1,1)' carries a "
        "bar slip on one piece -- immaterial to every verdict here")
    results["leg1"]["color_singlet_states"] = n_singlet

    print("-- embedding indices and levels (exact Killing) --")
    tr_h1 = sum(Fraction(h1_27[t][t]) ** 2 for t in range(27))
    # build exact e6 basis (78 of the span vectors) and Killing values
    span_int = span_arr  # integer numpy (n,729)
    # greedy independent set mod p1
    sel = []
    elim = np.zeros((0, 729), dtype=np.int64)
    basis_rows = []
    cur = []
    m_work = []
    r = 0
    mat = None
    idxs = []
    work = np.zeros((78, 729), dtype=np.int64)
    nsel = 0
    for vi in range(span_int.shape[0]):
        cand = np.vstack([work[:nsel], span_int[vi] % p1])
        if rank_mod_p(cand, p1) > nsel:
            work[nsel] = span_int[vi] % p1
            idxs.append(vi)
            nsel += 1
        if nsel == 78:
            break
    check("selected 78 independent e6 span vectors", nsel == 78)
    Bmat = span_int[idxs].T.astype(object)  # 729 x 78 exact integers

    # pivot rows mod p1
    mm = (span_int[idxs] % p1).astype(np.int64)
    piv_rows = []
    m2 = mm.copy()
    rr = 0
    for c in range(729):
        if rr >= 78:
            break
        nz = np.nonzero(m2[rr:, c])[0]
        if len(nz) == 0:
            continue
        piv = rr + nz[0]
        m2[[rr, piv]] = m2[[piv, rr]]
        inv = pow(int(m2[rr, c]), p1 - 2, p1)
        m2[rr] = (m2[rr] * inv) % p1
        for i in range(78):
            if i != rr and m2[i, c]:
                m2[i] = (m2[i] - m2[i, c] * m2[rr]) % p1
        piv_rows.append(c)
        rr += 1
    check("78 pivot coordinates found", len(piv_rows) == 78)

    G = [[Fraction(int(Bmat[piv_rows[r_], c_])) for c_ in range(78)]
         for r_ in range(78)]
    # exact inverse of G
    aug = [G[r_] + [Fraction(1 if c_ == r_ else 0) for c_ in range(78)]
           for r_ in range(78)]
    rkG, pivG, redG = rref(aug, 156)
    check("chosen 78x78 coordinate block invertible over Q",
          pivG[:78] == list(range(78)))
    Ginv = [[redG[r_][78 + c_] for c_ in range(78)] for r_ in range(78)]

    def e6_coords(Wflat):
        """exact coordinates of a 729-Fraction vector in the e6 basis,
        with full verification W = B c."""
        wr = [Wflat[piv_rows[r_]] for r_ in range(78)]
        c_ = [sum(Ginv[r_][k] * wr[k] for k in range(78)) for r_ in range(78)]
        # verify all 729 rows
        for row in range(729):
            s = Fraction(0)
            for k in range(78):
                if c_[k] != 0 and Bmat[row][k] != 0:
                    s += Fraction(int(Bmat[row][k])) * c_[k]
            if s != Wflat[row]:
                raise AssertionError("vector not in e6 span")
        return c_

    def kappa_of(hmat27):
        """kappa(h,h) = Tr(ad_h^2) on the constructed 78-dim algebra."""
        H = fmat(hmat27)
        AD = []
        for k in range(78):
            V = [[Fraction(int(Bmat[r_ * 27 + c_][k]))
                  for c_ in range(27)] for r_ in range(27)]
            # commutator H V - V H
            C = [[sum(H[i][t] * V[t][j] - V[i][t] * H[t][j]
                      for t in range(27)) for j in range(27)]
                 for i in range(27)]
            flat = [C[i][j] for i in range(27) for j in range(27)]
            AD.append(e6_coords(flat))
        kap = Fraction(0)
        for s_ in range(78):
            for t_ in range(78):
                kap += AD[t_][s_] * AD[s_][t_]
        return kap

    kap_h1 = kappa_of(h1_27)
    kap_ha = kappa_of(ha27)
    kap_hb = kappa_of(hb27)
    h_dual_e6 = 12  # = 1 + max(B854 exponents), simply-laced (cited below)
    j_sl3 = kap_h1 / (4 * h_dual_e6)
    j_a = kap_ha / (4 * h_dual_e6)
    j_b = kap_hb / (4 * h_dual_e6)
    check("kappa(h1,h1)=96, kappa(h_a,h_a)=144, kappa(h_b,h_b)=48",
          (kap_h1, kap_ha, kap_hb) == (96, 144, 48),
          f"({kap_h1},{kap_ha},{kap_hb})")
    check("embedding indices (j_sl3, j_a, j_b) = (2, 3, 1)",
          (j_sl3, j_a, j_b) == (2, 3, 1), f"({j_sl3},{j_a},{j_b})")
    tr_ha = sum(Fraction(ha27[t][t2_]) * Fraction(ha27[t2_][t])
                for t in range(27) for t2_ in range(27))
    tr_hb = sum(Fraction(hb27[t][t2_]) * Fraction(hb27[t2_][t])
                for t in range(27) for t2_ in range(27))
    tr_h1v = sum(Fraction(h1_27[t][t]) ** 2 for t in range(27))
    check("27-trace cross-check: Tr(h1^2)=24, Tr(h_a^2)=36, Tr(h_b^2)=12 "
          "(= 4*T with T = j*T_e6(27), T_e6(27)=3)",
          (tr_h1v, tr_ha, tr_hb) == (24, 36, 12),
          f"({tr_h1v},{tr_ha},{tr_hb})")

    Fr = Fraction
    c_e6 = Fr(1 * 78, 1 + 12)
    c_a2 = Fr(2 * 8, 2 + 3)
    c_g2 = Fr(1 * 14, 1 + 4)
    c_a1_3 = Fr(3 * 3, 3 + 2)
    c_a1_1 = Fr(1 * 3, 1 + 2)
    ok_conf1 = c_a2 + c_g2 == c_e6 == 6
    ok_conf2 = c_a1_3 + c_a1_1 == c_g2
    check("conformality: c(A2,2)+c(G2,1) = 16/5+14/5 = 6 = c(E6,1)",
          ok_conf1)
    check("conformality: c(A1,3)+c(A1,1) = 9/5+1 = 14/5 = c(G2,1)",
          ok_conf2)
    results["leg1"]["levels"] = {"su3": 2, "su2_a": 3, "su2_b": 1}
    results["leg1"]["central_charges"] = {
        "e6_1": str(c_e6), "a2_2": str(c_a2), "g2_1": str(c_g2),
        "a1_3": str(c_a1_3), "a1_1": str(c_a1_1)}
    results["leg1"]["kappa"] = {"h1": str(kap_h1), "h_a": str(kap_ha),
                                "h_b": str(kap_hb)}
    results["leg1"]["weights_verified"] = ok_branch

    # ------------------------------------------------------------------
    print("== LEG 2: the selection sweep ==")
    target = {"name": "su(3)+su(2)+su(2) (the conformal chain's subalgebra)",
              "dim": 14, "derived_dim": 14, "center_dim": 0, "rank": 4,
              "semisimple_type": "A2+A1+A1",
              "embedding_indices": [2, 3, 1]}

    def load(relpath):
        p = REPO / relpath
        if p.exists():
            with open(p) as f:
                return json.load(f)
        return None

    j854 = load("frontier/B854_centralizer_exact/results.json")
    j874 = load("frontier/B874_measurement_ladder/results.json")
    j874j = load("frontier/B874_measurement_ladder/joint_results.json")
    j892 = load("frontier/B892_second_measurement/wall_results.json")
    j897 = load("frontier/B897_27_under_g20/results.json")
    j909 = load("frontier/B909_frame_arc/results.json")

    confirms = {}
    confirms["B854_abelian_u1_4"] = bool(
        j854 and j854.get("all_brackets_vanish") and
        j854.get("invariant_rank") == 4)
    confirms["B854_exponents"] = (j854 or {}).get("exponents") == \
        [1, 4, 5, 7, 8, 11]
    confirms["B874_census_values_30_12"] = bool(
        j874 and sorted(set(j874["census"].values())) == [12, 30])
    confirms["B874_centC_12_8_4"] = bool(
        j874 and j874.get("cent_dim") == 12 and j874.get("derived_dim") == 8
        and j874.get("center_dim") == 4)
    confirms["B874_no_26_stratum"] = bool(j874j and j874j.get("no_26_stratum"))
    confirms["B874_kern_s1_46"] = bool(
        j874j and all(r["kern_s1"] == 46 for r in j874j["rows"]))
    confirms["B892_plane_stratum_30_28"] = bool(
        j892 and j892.get("wall_dim") == 30 and j892.get("wall_derived") == 28)
    confirms["B897_g20_20_19"] = bool(
        j897 and j897["p1"]["g_dim"] == 20 and j897["p1"]["derived_dim"] == 19
        and j897["p2"]["g_dim"] == 20)
    csing = None
    if j897:
        for b in j897["p1"]["blocks"]:
            if b["c"] == 0 and b["f"] != 0:
                csing = b["dim"]
    confirms["B897_color_singlet_states_9"] = csing == 9
    confirms["B909_cmt_30_18_2"] = bool(
        j909 and j909["cmt_typing"]["dim_z"] == 30
        and j909["cmt_typing"]["z_cap_core"] == 18
        and j909["cmt_typing"]["center_by_count"] == 2)
    for k, v in confirms.items():
        check(f"banked-data confirm: {k}", v)

    # the banked wall lattice, typed (citations in DRAFT_FINDINGS.md)
    walls = [
        {"wall": "C = Cent_e6(2T) (the charge torus)", "arc": "B854",
         "dim": 4, "derived_dim": 0, "center_dim": 4,
         "semisimple_type": None, "is_charge_centralizer": False,
         "note": "centralizer of the finite holonomy image, not of charges"},
        {"wall": "FMT K-walls (three lines; kern(s1))", "arc": "B866/B877/B874",
         "dim": 46, "derived_dim": 45, "center_dim": 1,
         "semisimple_type": "D5 (so(10))", "is_charge_centralizer": True},
        {"wall": "core / soft-plane stratum / compact wall (CMT)",
         "arc": "B874/B875/B877/B892/B909",
         "dim": 30, "derived_dim": 28, "center_dim": 2,
         "semisimple_type": "D4 (so(8))", "is_charge_centralizer": True},
        {"wall": "cross-shadow", "arc": "B909 (solo sXXI)",
         "dim": 18, "derived_dim": 15, "center_dim": 3,
         "semisimple_type": "A3 (su(4)) -- forced (see enumeration)",
         "is_charge_centralizer": True},
        {"wall": "SMT wall z(x1, y*)", "arc": "B892",
         "dim": 14, "derived_dim": 11, "center_dim": 3,
         "semisimple_type": "A2+A1 (su(3)+su(2))",
         "is_charge_centralizer": True},
        {"wall": "Cent(C) (the full-measurement floor)", "arc": "B874",
         "dim": 12, "derived_dim": 8, "center_dim": 4,
         "semisimple_type": "A2 (su(2,1) real form)",
         "is_charge_centralizer": True},
        {"wall": "G20 (generated by all three breakings; NOT a centralizer)",
         "arc": "B892/B897",
         "dim": 20, "derived_dim": 19, "center_dim": 1,
         "semisimple_type": "A2+A2+A1", "is_charge_centralizer": False},
    ]
    matches = []
    for w in walls:
        is_match = (w["derived_dim"] == target["derived_dim"]
                    and w["center_dim"] == target["center_dim"])
        w["matches_target"] = is_match
        if is_match:
            matches.append(w["wall"])
    check("SWEEP: no banked wall has (derived, center) = (14, 0) "
          "= su(3)+su(2)+su(2)", len(matches) == 0,
          f"matches={matches}")

    # rank<=3 semisimple dimension enumeration (types the 18-stratum and
    # guards the dim-14 near-miss): simple types of rank <= 3
    simples = {"A1": (1, 3), "A2": (2, 8), "A3": (3, 15), "B2": (2, 10),
               "B3": (3, 21), "C3": (3, 21), "G2": (2, 14)}
    combos = {}
    names = list(simples)
    for rsize in range(1, 4):
        for combo in itertools.combinations_with_replacement(names, rsize):
            rk = sum(simples[c][0] for c in combo)
            dm = sum(simples[c][1] for c in combo)
            if rk <= 3:
                combos.setdefault(dm, []).append("+".join(combo))
    check("typing lemma: dim-15 semisimple of rank<=3 is A3 uniquely",
          combos.get(15) == ["A3"], f"{combos.get(15)}")
    check("typing lemma: dim-11 semisimple of rank<=3 is A2+A1 uniquely",
          [set(x.split("+")) for x in combos.get(11, [])] == [{"A2", "A1"}],
          f"{combos.get(11)}")
    check("typing lemma: A2+A1+A1 (dim 14, rank 4) is NOT available at "
          "rank<=3; the only rank<=3 dim-14 semisimple is G2",
          combos.get(14) == ["G2"], f"{combos.get(14)}")

    # vacuity certificate: the Levi homonym A2+A1+A1 EXISTS in e6
    e6_edges = {(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)}

    def adj(x, y):
        return (min(x, y), max(x, y)) in e6_edges

    homonyms = []
    for sub in itertools.combinations(range(1, 7), 4):
        edges = [(x, y) for x, y in itertools.combinations(sub, 2)
                 if adj(x, y)]
        if len(edges) == 1:
            # exactly one edge => A2 + A1 + A1 induced
            homonyms.append({"nodes": sub, "A2_edge": edges[0]})
    check("VACUITY: Levi type A2+A1+A1 exists in e6 (subdiagram found) "
          "-- outcome B was statable", len(homonyms) > 0,
          f"{len(homonyms)} subdiagrams, e.g. {homonyms[0]}")

    # the two theorem-shaped obstructions (proof sketches in FINDINGS):
    # T1 (center): z(S) contains S in its center for any nonempty charge
    #    set S => center >= 1 > 0 = center(target).  All banked walls
    #    show center >= 1, monotone along the cascade.
    t1 = all(w["center_dim"] >= 1 for w in walls
             if w["is_charge_centralizer"])
    check("T1 (center obstruction): every banked charge wall has "
          "center >= 1; the conformal subalgebra has center 0", t1)
    # T2 (regularity): charge centralizers are full-rank regular (Levi)
    #    subalgebras; in simply-laced e6 every Levi simple factor has
    #    embedding index 1.  The conformal chain's A2 has index 2 and its
    #    su(2)_3 has index 3 (computed exactly above) => neither is
    #    E6-conjugate to any factor of ANY charge wall, banked or future.
    t2 = (j_sl3 == 2 and j_a == 3)
    check("T2 (regularity obstruction): conformal factors have indices "
          "(2,3) != 1 -- S-subalgebra, unreachable by any charge "
          "centralizer", t2)

    results["leg2"]["target"] = target
    results["leg2"]["walls"] = walls
    results["leg2"]["banked_confirms"] = confirms
    results["leg2"]["levi_homonyms_in_e6"] = [
        {"nodes": list(h["nodes"]), "A2_edge": list(h["A2_edge"])}
        for h in homonyms]
    results["leg2"]["gut_side_color_singlets_B897"] = csing
    results["leg2"]["conformal_color_singlets"] = n_singlet
    results["leg2"]["outcome"] = (
        "A -- NOT REALIZED: no banked structure carries "
        "su(3)+su(2)+su(2) as a centralizer/wall; the banked cascade "
        "(FMT 46 = so(10)+u(1) -> SMT 14 = su(3)+su(2)+u(1)^3, SU(5) "
        "skipped) IS the GUT-side chain; the conformal chain's factors "
        "are S-type (indices 2,3) and center-0, unreachable by charge "
        "measurement (T1+T2).  The object selects the GUT chain at the "
        "structural level.")

    ok_all = all(c["ok"] for c in CHECKS)
    results["all_checks_pass"] = ok_all
    with open(HERE / "results.json", "w") as f:
        json.dump(results, f, indent=1, default=str)
    print(f"\nALL CHECKS PASS: {ok_all}  ({len(CHECKS)} checks)")
    print("results.json written")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
