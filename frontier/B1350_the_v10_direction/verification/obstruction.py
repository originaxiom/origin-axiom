#!/usr/bin/env python3
"""B1350 stage (5): THE SECOND-ORDER OBSTRUCTION, exactly (modulo two primes p = 1 mod 3, omega -> a cube root of 1 in F_p).

The Newton search of stage (4) stalls at |res| ~ 3e-13 along the V10 classes: Gauss-Newton cannot remove the residual,
which is the signature of an OBSTRUCTED first-order deformation.  Here the obstruction is computed exactly.  For a cocycle
Y = (Y_a, Y_b) in Z^1(pi_1 M; e6) (values in e6 c gl(27), exact over Q(omega)), the deformation rho_eps(g) = exp(eps Y_g) rho_0(g)
satisfies the relator to first order; its eps^2 term Q(Y) := [rho_eps(REL)]_2 lies in e6, and the deformation extends to
second order (rho_eps(g) = exp(eps Y_g + eps^2 W_g) rho_0(g) with rho_eps(REL) = I + O(eps^3)) iff Q(Y) lies in the image of
the linearised relator map d1: e6 + e6 -> e6, W -> [rho(REL)]_1.  So [Q(Y)] in H^2(M; e6) = e6 / im d1 is the obstruction.

Computed for all eight sl2-blocks of e6 at the subregular point (one exact cocycle class per block; the two V10's), the
quadratic map Q: H^1(M; e6) (dim 8) -> H^2(M; e6) (dim 8) by polarisation, and its zero set restricted to the V10 plane
and to each single block.  Everything is exact: matrices over Q(omega) reduced modulo two primes; a rank computed modulo
a prime is a lower bound for the exact rank, so 'obstructed' (rank grows) is exact, and 'unobstructed' is exact whenever
the rank of d1 attains its known value 156 - 86 = 70 (h^1(M; e6) = 8, h^0 = 0)."""
from __future__ import annotations
import os, sys, time, itertools
from fractions import Fraction as F
import numpy as np
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1268_cusped_net_chirality_bound', 'verification'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1267_spectrum_law_rebuilt', 'verification'))
import e6_instrument as E
import spectrum_law as S
Qw = E.Qw
t0 = time.time()

# ---------------------------------------------------------------- the subregular point and its blocks (as in v10_direction.py)
e2, h2, f2, g2 = E.subregular_sl2()
C_SUB = (2, 2, 2, 0, 2, 2)
wt = lambda r: sum(C_SUB[i] * r[i] for i in range(E.N))
def hw_vectors_sub(weight):
    basis = [r for r in E.POS if wt(r) == weight]
    if not basis:
        return []
    A = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in E.br(e2, E.vec(E.N + E.IDX[r]))] for r in basis]).T
    out = []
    for coef in A.nullspace():
        lcm = 1
        for c in coef:
            lcm = sp.ilcm(lcm, int(sp.Rational(c).q))
        v = [F(0)] * E.DIM
        for i, r in enumerate(basis):
            q = sp.Rational(coef[i] * lcm)
            if q != 0:
                v[E.N + E.IDX[r]] = F(int(q.p), int(q.q))
        out.append(v)
    return out
BLOCKS = []            # (weight, hv)
for w in range(2, 18, 2):
    for hv in hw_vectors_sub(w):
        BLOCKS.append((w, hv))
assert [w for w, _ in BLOCKS] == [2, 4, 6, 8, 10, 10, 14, 16], [w for w, _ in BLOCKS]
rho0 = S.build_rep(e2, f2)
S.check_rep(rho0, [1, 2], [S.REL])

def block_cocycle(hv, weight):
    """one exact non-coboundary cocycle of the block V_weight (basis ad(f)^k hv), lifted to e6 coordinates (78 Qw)."""
    m = weight // 2
    v = hv; basis = [v]
    for k in range(2 * m):
        v = E.br(f2, v); basis.append(v)
    d = len(basis)
    Bm = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in b] for b in basis]).T
    def restrict(y):
        img = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in E.br(y, b)] for b in basis]).T
        return Bm.gauss_jordan_solve(img)[0]
    ade, adf = restrict(e2), restrict(f2)
    def qwm(M, c):
        out = E.qw_zeros(d)
        for i in range(d):
            for j in range(d):
                x = sp.Rational(M[i, j]); out[i, j] = Qw(F(int(x.p), int(x.q))) * c
        return out
    Aa = E.qw_expm_nilpotent(qwm(ade, E.ONE)); Aai = E.qw_expm_nilpotent(qwm(ade, Qw(-1)))
    Bb = E.qw_expm_nilpotent(qwm(adf, E.U_RILEY)); Bbi = E.qw_expm_nilpotent(qwm(adf, -E.U_RILEY))
    R = S.Rep({1: Aa, 2: Bb}, {1: Aai, 2: Bbi}); S.check_rep(R, [1, 2], [S.REL])
    d1 = np.hstack([R.fox(S.REL, 1), R.fox(S.REL, 2)])
    A = [[d1[i, j] for j in range(2 * d)] for i in range(d)]
    nn, mm = d, 2 * d; r = 0; pivcols = []
    for c in range(mm):
        piv = next((i for i in range(r, nn) if not A[i][c].is_zero()), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]; inv = A[r][c].inv(); A[r] = [x * inv for x in A[r]]
        for i in range(nn):
            if i != r and not A[i][c].is_zero():
                fct = A[i][c]; A[i] = [x - fct * y for x, y in zip(A[i], A[r])]
        pivcols.append(c); r += 1
    free = [c for c in range(mm) if c not in pivcols]
    kern = []
    for fc in free:
        vct = [E.ZERO] * mm; vct[fc] = E.ONE
        for i, pc in enumerate(pivcols): vct[pc] = -A[i][fc]
        kern.append(vct)
    I = E.qw_eye(d)
    cob = np.vstack([Aa - I, Bb - I]); rB = S.exact_rank_qw(cob)
    h1b = len(kern) - rB
    za = zb = None
    for vct in kern:
        test = np.hstack([cob, np.array([[x] for x in vct], dtype=object)])
        if S.exact_rank_qw(test) > rB:
            za, zb = vct[:d], vct[d:]; break
    assert za is not None, "no non-coboundary cocycle in this block"
    Za = [sum((Qw(F(int(sp.Rational(Bm[k, i]).p), int(sp.Rational(Bm[k, i]).q))) * za[i] for i in range(d)), E.ZERO) for k in range(78)]
    Zb = [sum((Qw(F(int(sp.Rational(Bm[k, i]).p), int(sp.Rational(Bm[k, i]).q))) * zb[i] for i in range(d)), E.ZERO) for k in range(78)]
    return Za, Zb, dict(dimZ1=len(kern), dimB1=rB, h1=h1b)

print("=== (5a) one exact cocycle class per sl2-block of e6 at the subregular point ===")
COC = []
for i, (w, hv) in enumerate(BLOCKS):
    Za, Zb, info = block_cocycle(hv, w)
    print(f"    block V{w}{'#2' if i == 5 else ''}: dim Z1 = {info['dimZ1']}, dim B1 = {info['dimB1']}, h1 = {info['h1']}")
    assert info['h1'] == 1
    COC.append((w, Za, Zb))
print(f"    ({time.time() - t0:.0f} s)")

# ---------------------------------------------------------------- reduction modulo p
def cube_root_mod(p):
    for g in range(2, p):
        r = pow(g, (p - 1) // 3, p)
        if r != 1 and (r * r + r + 1) % p == 0:
            return r
    raise ValueError
def make_red(p):
    w = cube_root_mod(p)
    def red(q):
        if isinstance(q, Qw):
            x, y = q.x, q.y
        else:
            x, y = F(q), F(0)
        return (x.numerator * pow(x.denominator, -1, p) + (y.numerator * pow(y.denominator, -1, p)) * w) % p
    return red, w
def red_mat(M, red, p):
    return np.array([[red(M[i, j]) for j in range(M.shape[1])] for i in range(M.shape[0])], dtype=np.int64)
def mm(A, B, p):
    return (A @ B) % p
def rank_mod(rows, p):
    """rank over F_p of a list of row vectors (python ints)."""
    A = [list(r) for r in rows]
    nrow = len(A); ncol = len(A[0]); r = 0
    for c in range(ncol):
        piv = next((i for i in range(r, nrow) if A[i][c] % p), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], -1, p); A[r] = [(x * inv) % p for x in A[r]]
        for i in range(nrow):
            if i != r and A[i][c] % p:
                f = A[i][c]; A[i] = [(x - f * y) % p for x, y in zip(A[i], A[r])]
        r += 1
        if r == nrow: break
    return r

def series_mul(P, Q, p, deg=2):
    """truncated matrix series P = [P0, P1, P2], Q likewise (mod p)."""
    out = []
    for k in range(deg + 1):
        acc = np.zeros_like(P[0])
        for i in range(k + 1):
            if i < len(P) and k - i < len(Q):
                acc = (acc + mm(P[i], Q[k - i], p)) % p
        out.append(acc)
    return out

def relator_series(M, Mi, Y, p, deg=2):
    """rho_eps(REL) to order eps^deg for rho_eps(g) = exp(eps Y_g) rho_0(g); Y = {1: Y_a, 2: Y_b} mod p (or zero)."""
    n = 27; I = np.eye(n, dtype=np.int64)
    inv2 = pow(2, -1, p)
    def letter(L):
        g = abs(L); Yg = Y[g]; Y2 = mm(Yg, Yg, p) * inv2 % p
        if L > 0:
            ser = [I, Yg % p, Y2]
            return [mm(s, M[g], p) for s in ser[:deg + 1]]
        else:
            ser = [I, (-Yg) % p, Y2]
            return [mm(Mi[g], s, p) for s in ser[:deg + 1]]
    cur = [I] + [np.zeros((n, n), dtype=np.int64)] * deg
    for L in S.REL:
        cur = series_mul(cur, letter(L), p, deg)
    return cur

def analyse(p):
    red, w = make_red(p)
    print(f"=== (5b) modulo p = {p} (omega -> {w}) ===")
    M = {g: red_mat(rho0.M[g], red, p) for g in (1, 2)}
    Mi = {g: red_mat(rho0.I[g], red, p) for g in (1, 2)}
    for g in (1, 2):
        assert np.array_equal(mm(M[g], Mi[g], p), np.eye(27, dtype=np.int64))
    REP = [np.array([[int(F(x).numerator) * pow(int(F(x).denominator), -1, p) % p for x in row] for row in E.REP[k].tolist()], dtype=np.int64) for k in range(78)]
    def e6mat(Z):
        acc = np.zeros((27, 27), dtype=np.int64)
        for k in range(78):
            c = red(Z[k])
            if c:
                acc = (acc + c * REP[k]) % p
        return acc
    # the linearised relator map d1 on e6 + e6 (156 columns of length 729)
    zero = np.zeros((27, 27), dtype=np.int64)
    cols = []
    for g in (1, 2):
        for k in range(78):
            Y = {1: zero, 2: zero}; Y = dict(Y); Y[g] = REP[k]
            ser = relator_series(M, Mi, Y, p, deg=1)
            assert np.array_equal(ser[0], np.eye(27, dtype=np.int64))
            cols.append([int(x) for x in ser[1].reshape(-1)])
    rk = rank_mod(cols, p)
    print(f"    rank d1 = {rk} (expected 156 - dim Z1 = 156 - (78 + 8) = 70); dim H^2(M; e6) = {78 - rk}")
    # the cocycles as e6 matrices; first-order check; the quadratic terms
    Ys = [{1: e6mat(Za), 2: e6mat(Zb)} for _, Za, Zb in COC]
    def Q(Y):
        ser = relator_series(M, Mi, Y, p, deg=2)
        assert np.array_equal(ser[0], np.eye(27, dtype=np.int64))
        assert not ser[1].any(), "first-order term does not vanish: not a cocycle (convention error)"
        return [int(x) for x in ser[2].reshape(-1)]
    def add(Y, Z):
        return {g: (Y[g] + Z[g]) % p for g in (1, 2)}
    def in_image(v):
        return rank_mod(cols + [v], p) == rk
    Qi = [Q(Y) for Y in Ys]
    labels = [f"V{w}" + ("#2" if i == 5 else "") for i, (w, _, _) in enumerate(COC)]
    print("    single blocks: is the second-order obstruction [Q(Y)] zero in H^2 (the class integrates to second order)?")
    single = {}
    for lab, q in zip(labels, Qi):
        single[lab] = in_image(q)
        print(f"      {lab:5s}: {'UNOBSTRUCTED (Q in im d1)' if single[lab] else 'OBSTRUCTED (rank grows by 1)'}")
    # the V10 plane: Q(c1 Y1 + c2 Y2) = c1^2 Q1 + c2^2 Q2 + c1 c2 B, B = Q(Y1+Y2) - Q1 - Q2
    i1, i2 = 4, 5
    B12 = [(a - b - c) % p for a, b, c in zip(Q(add(Ys[i1], Ys[i2])), Qi[i1], Qi[i2])]
    r_span = rank_mod(cols + [Qi[i1], Qi[i2], B12], p) - rk
    print(f"    the V10 plane: dim span{{[Q(Y1)], [Q(Y2)], [B(Y1,Y2)]}} in H^2 = {r_span}"
          + ("  => the three classes are independent: Q(c) = 0 in H^2 forces c1^2 = c2^2 = c1 c2 = 0, i.e. c = 0 -- EVERY direction of the V10 plane is obstructed at second order" if r_span == 3 else "  => a conic of second-order-integrable directions may exist; solve below"))
    if r_span < 3:
        # find the relations among the three classes modulo im d1 and solve the conic c1^2 [Q1] + c2^2 [Q2] + c1 c2 [B] = 0
        print("      (relations among the three classes:) rank pairs:", {"Q1,Q2": rank_mod(cols + [Qi[i1], Qi[i2]], p) - rk, "Q1,B": rank_mod(cols + [Qi[i1], B12], p) - rk, "Q2,B": rank_mod(cols + [Qi[i2], B12], p) - rk})
    # the full quadratic map on H^1 (8 classes): polarisation B_ij and the span of all classes in H^2
    allq = list(Qi)
    pairs = {}
    for i in range(8):
        for j in range(i + 1, 8):
            pairs[(i, j)] = [(a - b - c) % p for a, b, c in zip(Q(add(Ys[i], Ys[j])), Qi[i], Qi[j])]
            allq.append(pairs[(i, j)])
    r_all = rank_mod(cols + allq, p) - rk
    print(f"    the full quadratic map H^1 (8) -> H^2 ({78 - rk}): its 36 coefficient classes span a subspace of dimension {r_all} of H^2")
    # which mixed terms involve the V10 classes non-trivially?
    mixed = {}
    for (i, j), v in pairs.items():
        if i in (i1, i2) or j in (i1, i2):
            mixed[(labels[i], labels[j])] = rank_mod(cols + [v], p) - rk
    print(f"    mixed terms B(Y_i, Y_j) with a V10 factor, nonzero in H^2 (1) or zero (0): {mixed}")
    print(f"    ({time.time() - t0:.0f} s)")
    return dict(rank_d1=rk, single=single, v10_span=r_span, full_span=r_all, mixed=mixed)

if __name__ == "__main__":
    PR = [int(x) for x in sys.argv[1:]] or [67108819, 67108837]
    from sympy import isprime
    res = []
    for p in PR:
        if not (isprime(p) and p % 3 == 1):
            # find the next prime = 1 mod 3
            q = p
            while not (isprime(q) and q % 3 == 1): q += 1
            p = q
        res.append(analyse(p))
    print("\n=== summary ===")
    print(f"    agreement of the two primes on every rank: {all(r == res[0] for r in res)}")
    print(f"    V10 classes: {[res[0]['single'][k] for k in res[0]['single'] if k.startswith('V10')]} (True = unobstructed); V10 plane span {res[0]['v10_span']}; rank d1 {res[0]['rank_d1']}")
    print(f"[{time.time() - t0:.0f} s]")
