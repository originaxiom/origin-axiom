#!/usr/bin/env python3
"""P2W5-B465 -- B465's outstanding seat-1 residual: the loop / dark-phase / max-trace
construct.  Does it carry genuine structure, or does it dissolve with the refuted
SU(4)->SU(3)/Pati-Salam readings?

The three residual items (B465 FINDINGS "claims that did not survive or await
constructions"):
  C5  32 loops, non-abelian monodromy, cycle structure 8x4x3   (loop family not shared)
  C6  max|tr| = sqrt5 (c=1) vs sqrt15 (others)                 (family not shared)
  C7  dark points carry more distinct eigenphases (12.2 vs 8.2; 42 dark-only)

KEY MOVE.  C6 and C7 both speak of a PER-ADDRESS family.  The address torus is already
banked in this program (B431/B459: the level-15 dual torus).  In the quantized-cat-map
setting there is exactly ONE canonical per-address family: the Heisenberg address twist
O_v = W_A . T(v),  T(a,b) = Z^a X^b  on (Z/N)^2.  That family is determinate, so C6/C7
are reconstructible even though seat-1's code was never shared -- and, being canonical,
a null result on it is a real (not guessed) negative.

Legs
  L1  the affine Weil character law, 4 levels N in {15,21,35,45}:
        tr(W_A T(v)) = 0 unless v in im(A-I);  |tr|^2 = |ker(A-I)| there.
      Identifiable estimator: exact integers |tr|^2 and set equality of supports.
  L2  EXACT F_p certificate (two primes p = 61, 421 = 1 mod 60) of the N=15 l=0 c=1 case:
        |tr|^2 := tr(O) * tr(O^-1)  (exact, unitary => conj = inverse)
        #distinct eigenvalues := 15 - deg gcd(f, f')  (embedding-independent)
  L3  C6 adjudication: max_v |tr| = sqrt(|ker(A-I)|), and |ker(A-I)| is the N-part of
      det(A-I) = 2 - tr(A) -- pure Fricke arithmetic of the classical shadow.
  L4  C7 adjudication: dark vs bright distinct-eigenphase counts; and the identity of the
      bright multiplicity pattern with the ADDENDUM's (c|5)=-1 nine-distinct pattern.
  L5  C5 adjudication: exact commutant dimension at l=0 and l=1 -- is an eigenvector-label
      cycle type an invariant at all?

Env: pyenv python3 (numpy only).  Re-runnable.  ~2 min.
"""
import json
import sys
import time
from collections import Counter
from math import gcd

import numpy as np

OUT = {}
T0 = time.time()

# ----------------------------------------------------------------------------- utilities

def build(N):
    """the level-N Weil/Heisenberg kit (c=1 convention of B465 c_family.py)."""
    z = np.exp(2j * np.pi / N)
    F = np.array([[z ** ((j * k) % N) for k in range(N)] for j in range(N)])
    Fi = np.array([[z ** ((-j * k) % N) for k in range(N)] for j in range(N)])
    Par = np.zeros((N, N), complex)
    for j in range(N):
        Par[(-j) % N, j] = 1
    def D(p):
        return np.diag([z ** ((p * (j * (j - 1) // 2)) % N) for j in range(N)])
    WR = (F @ D(-1) @ Fi) / N
    X = np.zeros((N, N), complex)
    for j in range(N):
        X[(j + 1) % N, j] = 1
    Z = np.diag([z ** j for j in range(N)])
    return Par, D, WR, X, Z


def mm2(A, B, N):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % N,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % N],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % N,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % N]]


def ker_im(A, N):
    """kernel size and image set of (A - I) acting on (Z/N)^2."""
    a, b, c, d = A[0][0] - 1, A[0][1], A[1][0], A[1][1] - 1
    ker = 0
    im = set()
    for x in range(N):
        for y in range(N):
            u, v = (a * x + b * y) % N, (c * x + d * y) % N
            if u == 0 and v == 0:
                ker += 1
            im.add((u, v))
    return ker, im


def T_of(Z, X, a, b):
    return np.linalg.matrix_power(Z, a) @ np.linalg.matrix_power(X, b)


def mult_pattern(A, tol=1e-6):
    ev = np.linalg.eigvals(A)
    ph = np.sort(np.angle(ev))
    groups, cur = [], [ph[0]]
    for p in ph[1:]:
        if p - cur[-1] < tol:
            cur.append(p)
        else:
            groups.append(cur)
            cur = [p]
    groups.append(cur)
    if len(groups) > 1 and (groups[0][0] + 2 * np.pi - groups[-1][-1]) < tol:
        groups[0] = groups[0] + groups.pop()
    return tuple(sorted((len(g) for g in groups), reverse=True))


# ------------------------------------------------------------- L1: affine Weil character

def leg1():
    print("== L1: affine Weil character law, 4 levels ==")
    rows, ok = [], True
    for N in (15, 21, 35, 45):
        Par, D, WR, X, Z = build(N)
        W1, W2 = WR @ D(1), WR @ WR @ D(2)
        R, L = [[1, 1], [0, 1]], [[1, 0], [1, 1]]
        A1 = mm2(R, L, N)
        A2 = mm2(mm2(R, R, N), mm2(L, L, N), N)
        Op = Par @ W1
        Acl = mm2([[-1 % N, 0], [0, -1 % N]], A1, N)
        for l in range(0, 3):
            if l > 0:
                Op = Op @ W2
                Acl = mm2(Acl, A2, N)
            k, im = ker_im(Acl, N)
            sup, vals = set(), set()
            for a in range(N):
                for b in range(N):
                    t = abs(np.trace(Op @ T_of(Z, X, a, b))) ** 2
                    if t > 1e-7:
                        sup.add((a, b))
                        vals.add(round(t, 6))
            # convention-free support test: the quantum address torus and the classical
            # phase space differ by the fixed Weyl-ordering dictionary (a linear flip +
            # a metaplectic translation).  So test that sup is a COSET of a subgroup
            # equal to im(A-I) after translating to a base point, allowing the a -> -a
            # flip; the ORDER and the |tr|^2 value are convention-free by themselves.
            base = min(sup)
            H = {((a - base[0]) % N, (b - base[1]) % N) for (a, b) in sup}
            Hf = {((-a) % N, b) for (a, b) in H}
            coset = (H == im) or (Hf == im)
            law = coset and (len(sup) == len(im)) and (vals == {float(k)})
            ok &= law
            rows.append(dict(N=N, l=l, ker=k, im=len(im), support=len(sup),
                             tr2=sorted(vals), coset_of_im=bool(coset), law=bool(law)))
            print(f"  N={N:2d} l={l}: |ker(A-I)|={k:3d} |im|={len(im):4d} "
                  f"support={len(sup):4d} coset-of-im={coset} |tr|^2={sorted(vals)} law={law}")
    OUT['L1'] = dict(rows=rows, all_pass=bool(ok))
    return ok


# --------------------------------------------------------------- L2: exact F_p certificate

def prime_factors(n):
    out, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def froot(p, n):
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)):
            return pow(g, (p - 1) // n, p)
    raise RuntimeError


def matmul_p(A, B, p):
    Bt = list(zip(*B))
    return [[sum(x * y for x, y in zip(r, c)) % p for c in Bt] for r in A]


def build_p(p, N=15):
    """exact level-15 kit over F_p (p = 1 mod 60), sqrt15 by the B465 Gauss-sum rule."""
    z = froot(p, 15)
    i4 = froot(p, 4)
    gs = sum(pow(z, (j * j) % 15, p) for j in range(15)) % p
    s15 = (-i4 * gs) % p
    assert (s15 * s15) % p == 15 % p
    inv_s = pow(s15, p - 2, p)
    zi = pow(z, p - 2, p)
    gsc = sum(pow(zi, (j * j) % 15, p) for j in range(15)) % p
    s15c = (-pow(i4, p - 2, p) * gsc) % p
    inv_sc = pow(s15c, p - 2, p)
    D = [[pow(z, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)] for i in range(N)]
    Dd = [[pow(zi, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)] for i in range(N)]
    F = [[(pow(z, (i * j) % 15, p) * inv_s) % p for j in range(N)] for i in range(N)]
    Fd = [[(pow(zi, (i * j) % 15, p) * inv_sc) % p for j in range(N)] for i in range(N)]
    Wr = matmul_p(matmul_p(F, Dd, p), Fd, p)
    W1 = matmul_p(Wr, D, p)
    W2 = matmul_p(matmul_p(Wr, Wr, p), matmul_p(D, D, p), p)
    Par = [[1 if i == ((-j) % N) else 0 for j in range(N)] for i in range(N)]
    Zm = [[pow(z, j, p) if i == j else 0 for j in range(N)] for i in range(N)]
    Xm = [[1 if i == (j + 1) % N else 0 for j in range(N)] for i in range(N)]
    return W1, W2, Par, Zm, Xm


def inv_p(A, p):
    n = len(A)
    M = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]
    r = 0
    for col in range(n):
        piv = next((i for i in range(r, n) if M[i][col] % p), None)
        assert piv is not None, "singular"
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][col], p - 2, p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(n):
            if i != r and M[i][col]:
                f = M[i][col]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return [row[n:] for row in M]


def det_p(A, p):
    M = [row[:] for row in A]
    n, det, r = len(M), 1, 0
    for col in range(n):
        piv = next((i for i in range(r, n) if M[i][col] % p), None)
        if piv is None:
            return 0
        if piv != r:
            M[r], M[piv] = M[piv], M[r]
            det = (-det) % p
        det = (det * M[r][col]) % p
        iv = pow(M[r][col], p - 2, p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(r + 1, n):
            if M[i][col]:
                f = M[i][col]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return det % p


def charpoly_p(A, p):
    """char poly coefficients (deg n, monic) by Lagrange interpolation of det(xI - A)."""
    n = len(A)
    xs = list(range(n + 1))
    ys = []
    for x in xs:
        B = [[((x if i == j else 0) - A[i][j]) % p for j in range(n)] for i in range(n)]
        ys.append(det_p(B, p))
    # Newton / Lagrange interpolation over F_p -> coefficient list (low..high)
    coef = [0] * (n + 1)
    for i, xi in enumerate(xs):
        num = [1]
        den = 1
        for j, xj in enumerate(xs):
            if j == i:
                continue
            num = poly_mul(num, [(-xj) % p, 1], p)
            den = (den * (xi - xj)) % p
        f = (ys[i] * pow(den, p - 2, p)) % p
        for k, c in enumerate(num):
            coef[k] = (coef[k] + f * c) % p
    return coef


def poly_mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
    return out


def poly_trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_mod(a, b, p):
    a = poly_trim(a[:], p)
    b = poly_trim(b[:], p)
    ib = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and not (len(a) == 1 and a[0] == 0):
        f = (a[-1] * ib) % p
        sh = len(a) - len(b)
        for i, c in enumerate(b):
            a[i + sh] = (a[i + sh] - f * c) % p
        a = poly_trim(a, p)
        if len(a) < len(b):
            break
    return a


def poly_gcd(a, b, p):
    a, b = poly_trim(a[:], p), poly_trim(b[:], p)
    while not (len(b) == 1 and b[0] == 0):
        a, b = b, poly_mod(a, b, p)
    return poly_trim(a, p)


def n_distinct_eigs(A, p):
    f = charpoly_p(A, p)
    df = [(i * c) % p for i, c in enumerate(f)][1:]
    if not any(df):
        return None
    g = poly_gcd(f, df, p)
    return (len(f) - 1) - (len(g) - 1)


def leg2():
    print("== L2: exact F_p certificate (N=15, l=0, c=1), two primes ==")
    res, ok = {}, True
    for p in (61, 421):
        W1, W2, Par, Zm, Xm = build_p(p)
        U = matmul_p(Par, W1, p)
        Uinv = inv_p(U, p)
        Zpow = [[[1 if i == j else 0 for j in range(15)] for i in range(15)]]
        for _ in range(14):
            Zpow.append(matmul_p(Zpow[-1], Zm, p))
        Xpow = [[[1 if i == j else 0 for j in range(15)] for i in range(15)]]
        for _ in range(14):
            Xpow.append(matmul_p(Xpow[-1], Xm, p))
        dark, bright = [], []
        nd_dark, nd_bright = Counter(), Counter()
        for a in range(15):
            for b in range(15):
                Tv = matmul_p(Zpow[a], Xpow[b], p)
                O = matmul_p(U, Tv, p)
                t = sum(O[i][i] for i in range(15)) % p
                Oi = matmul_p(inv_p(Tv, p), Uinv, p)
                ti = sum(Oi[i][i] for i in range(15)) % p
                nrm = (t * ti) % p
                nd = n_distinct_eigs(O, p)
                if nrm == 0:
                    dark.append(nrm)
                    nd_dark[nd] += 1
                else:
                    bright.append(nrm)
                    nd_bright[nd] += 1
        good = (len(dark) == 180 and len(bright) == 45
                and all(v == 5 % p for v in bright)
                and dict(nd_dark) == {15: 180} and dict(nd_bright) == {9: 45})
        ok &= good
        res[p] = dict(dark=len(dark), bright=len(bright),
                      bright_norms=sorted(set(bright)),
                      ndist_dark=dict(nd_dark), ndist_bright=dict(nd_bright), pass_=bool(good))
        print(f"  p={p}: dark={len(dark)} (tr=0 exactly), bright={len(bright)} with "
              f"tr*tr^-1={sorted(set(bright))} (=5); #distinct dark={dict(nd_dark)} "
              f"bright={dict(nd_bright)} -> {'PASS' if good else 'FAIL'}")
    cross = res[61]['ndist_dark'] == res[421]['ndist_dark'] and \
        res[61]['ndist_bright'] == res[421]['ndist_bright']
    OUT['L2'] = dict(per_prime=res, cross_prime_agree=bool(cross), all_pass=bool(ok))
    print(f"  cross-prime agreement: {cross}")
    return ok and cross


# ------------------------------------------------------------------ L3: C6 (max address trace)

def leg3():
    print("== L3: C6 -- max address trace = sqrt(|ker(A-I)|) = sqrt(N-part of 2 - tr(A)) ==")
    N = 15
    Par, D, WR, X, Z = build(N)
    R, L = [[1, 1], [0, 1]], [[1, 0], [1, 1]]
    A1 = mm2(R, L, N)
    A2 = mm2(mm2(R, R, N), mm2(L, L, N), N)
    W1, W2 = WR @ D(1), WR @ WR @ D(2)
    rows = []
    Op, Acl = Par @ W1, mm2([[-1 % N, 0], [0, -1 % N]], A1, N)
    for l in range(0, 7):
        if l > 0:
            Op = Op @ W2
            Acl = mm2(Acl, A2, N)
        k, _ = ker_im(Acl, N)
        mx = max(abs(np.trace(Op @ T_of(Z, X, a, b))) for a in range(N) for b in range(N))
        tr = (Acl[0][0] + Acl[1][1]) % N
        pred = (2 - tr) % N
        rows.append(dict(l=l, cl_trace=tr, two_minus_tr=pred, ker=k,
                         max_abs_tr=round(float(mx), 9), sqrt_ker=round(k ** 0.5, 9),
                         match=bool(abs(mx - k ** 0.5) < 1e-8)))
        print(f"  l={l}: cl tr={tr:2d}  (2-tr) mod 15={pred:2d}  |ker|={k:2d}  "
              f"max|tr|={mx:.6f}  sqrt|ker|={k ** 0.5:.6f}")
    # the c-family (ADDENDUM construction) at l=0
    import importlib.util
    cf_path = "<repo>/frontier/B465_monodromy_intake/c_family.py"
    spec = importlib.util.spec_from_file_location("cf", cf_path)
    cf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cf)
    cfam = {}
    for c in cf.CS:
        Uc = cf.U_c(c)
        mx = max(abs(np.trace(Uc @ T_of(Z, X, a, b))) for a in range(N) for b in range(N))
        cfam[c] = dict(qr5=(c % 5 in cf.QR5), max_abs_tr=round(float(mx), 9))
        print(f"  c={c:2d} [{'QR' if c % 5 in cf.QR5 else 'NQR'}]: max address |tr| = {mx:.6f}")
    got_sqrt5 = abs(cfam[1]['max_abs_tr'] - 5 ** 0.5) < 1e-8
    others_sqrt15 = all(abs(v['max_abs_tr'] - 15 ** 0.5) < 1e-8 for c, v in cfam.items() if c != 1)
    # is sqrt15 achievable at all in the family?  need |ker(A-I)| = 15
    reach15 = []
    seen = set()
    B = [[1, 0], [0, 1]]
    gens = [A1, A2, [[-1 % N, 0], [0, -1 % N]]]
    frontier = [B]
    for _ in range(6):
        nxt = []
        for M_ in frontier:
            for g in gens:
                Mn = mm2(M_, g, N)
                key = tuple(map(tuple, Mn))
                if key in seen:
                    continue
                seen.add(key)
                nxt.append(Mn)
                kk, _ = ker_im(Mn, N)
                if kk == 15:
                    reach15.append(key)
        frontier = nxt
    OUT['L3'] = dict(l_sweep=rows, c_family=cfam,
                     C6_sqrt5_at_c1_reproduced=bool(got_sqrt5),
                     C6_sqrt15_at_other_c=bool(others_sqrt15),
                     ker15_reachable_in_word_group=bool(reach15),
                     golden_disc_identity=dict(
                         det_A1_plus_I="det(A1+I) = det A1 + tr A1 + 1 = 1+3+1 = 5 = m^2+4 at m=1",
                         value=5),
                     all_pass=bool(all(r['match'] for r in rows)))
    print(f"  C6: sqrt5 at c=1 reproduced: {got_sqrt5};  'sqrt15 at other c': {others_sqrt15} "
          f"(exact value there = 1);  |ker|=15 reachable in the word group: {bool(reach15)}")
    return all(r['match'] for r in rows), got_sqrt5, others_sqrt15


# --------------------------------------------------------------------- L4: C7 (dark phases)

def leg4():
    print("== L4: C7 -- dark vs bright distinct eigenphases (4 levels) ==")
    rows, ok = [], True
    for N in (15, 35, 45):
        Par, D, WR, X, Z = build(N)
        U = Par @ (WR @ D(1))
        dk, br = Counter(), Counter()
        for a in range(N):
            for b in range(N):
                O = U @ T_of(Z, X, a, b)
                pat = mult_pattern(O)
                if abs(np.trace(O)) ** 2 > 1e-7:
                    br[(len(pat), pat)] += 1
                else:
                    dk[(len(pat), pat)] += 1
        dk_n = sorted({k[0] for k in dk})
        br_n = sorted({k[0] for k in br})
        contrast = bool(dk_n and br_n and min(dk_n) > max(br_n))
        ok &= contrast
        rows.append(dict(N=N, dark_count=sum(dk.values()), bright_count=sum(br.values()),
                         dark_ndistinct=dk_n, bright_ndistinct=br_n,
                         bright_pattern=[list(k[1]) for k in br][:1],
                         dark_gt_bright=contrast))
        print(f"  N={N:2d}: dark {sum(dk.values())} pts -> #distinct {dk_n}; "
              f"bright {sum(br.values())} pts -> #distinct {br_n}; dark>bright={contrast}")
    # the falsifier stratum: at l=1 the shadow has A-I invertible => NO contrast possible
    N = 15
    Par, D, WR, X, Z = build(N)
    W1, W2 = WR @ D(1), WR @ WR @ D(2)
    M1 = Par @ W1 @ W2
    pats = Counter(mult_pattern(M1 @ T_of(Z, X, a, b)) for a in range(N) for b in range(N))
    l1_uniform = len(pats) == 1
    print(f"  falsifier stratum l=1 (A-I invertible): address patterns = {dict(pats)} "
          f"-> uniform={l1_uniform} (no dark/bright contrast exists there)")
    # identity with the ADDENDUM's (c|5) = -1 nine-distinct pattern
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "cf", "<repo>/frontier/B465_monodromy_intake/c_family.py")
    cf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cf)
    nqr_pat = mult_pattern(cf.U_c(2))
    bright_pat = mult_pattern(cf.U_c(1) @ T_of(Z, X, *sorted(
        [(a, b) for a in range(15) for b in range(15)
         if abs(np.trace(cf.U_c(1) @ T_of(Z, X, a, b))) ** 2 > 1e-7])[0]))
    same = nqr_pat == bright_pat
    print(f"  ADDENDUM (c|5)=-1 pattern {nqr_pat} vs bright-address pattern {bright_pat} "
          f"-> identical={same}")
    OUT['L4'] = dict(rows=rows, l1_uniform=bool(l1_uniform),
                     nqr_pattern=list(nqr_pat), bright_pattern=list(bright_pat),
                     patterns_identical=bool(same), all_pass=bool(ok))
    return ok, l1_uniform, same


# ------------------------------------------------------------------------- L5: C5 (loops)

def rank_p(A, p):
    M = [row[:] for row in A]
    n, m, r = len(M), len(M[0]), 0
    for col in range(m):
        piv = next((i for i in range(r, n) if M[i][col] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][col], p - 2, p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(n):
            if i != r and M[i][col]:
                f = M[i][col]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
        if r == n:
            break
    return r


def commutant_dim(M, p, n=15):
    """dim of {Y : MY = YM} over F_p -- exact; the invariant that decides whether an
    eigenvector LABEL (hence a cycle type on labels) is canonically defined."""
    rows = []
    for a in range(n):
        for b in range(n):
            # coefficient row of (MY - YM)_{a,b} in the basis E_{i,j}
            row = [0] * (n * n)
            for k in range(n):
                row[k * n + b] = (row[k * n + b] + M[a][k]) % p
                row[a * n + k] = (row[a * n + k] - M[k][b]) % p
            rows.append(row)
    return n * n - rank_p(rows, p)


def leg5():
    print("== L5: C5 -- is an eigenvector-label cycle type an invariant? ==")
    p = 61
    W1, W2, Par, Zm, Xm = build_p(p)
    U = matmul_p(Par, W1, p)
    M1 = matmul_p(U, W2, p)
    d0 = commutant_dim(U, p)
    d1 = commutant_dim(M1, p)
    # seed-dependence demo: ONE fixed loop-monodromy V (an element of the commutant of
    # M(1), built once, seed-independent) is "tracked" through eigenvector labels obtained
    # from perturbed eigendecompositions.  If labels were canonical the extracted cycle
    # type would be seed-independent.
    N = 15
    Par_f, D, WR, X, Z = build(N)
    Mf = Par_f @ (WR @ D(1)) @ (WR @ WR @ D(2))
    ev0, Q0 = np.linalg.eig(Mf)
    # group the reference eigenbasis into the 4 eigenspaces and put a FIXED random
    # unitary on each block -> V commutes with Mf exactly (up to 1e-12)
    ph = np.angle(ev0)
    lbl, reps = [], []
    for a in ph:
        hit = next((i for i, r in enumerate(reps) if abs(np.angle(np.exp(1j * (a - r)))) < 1e-6), None)
        if hit is None:
            reps.append(a)
            hit = len(reps) - 1
        lbl.append(hit)
    rngV = np.random.default_rng(1234)
    Bm = np.zeros((N, N), complex)
    for blk in range(len(reps)):
        idx = [i for i in range(N) if lbl[i] == blk]
        g = rngV.normal(size=(len(idx), len(idx))) + 1j * rngV.normal(size=(len(idx), len(idx)))
        q, _ = np.linalg.qr(g)
        for u, i in enumerate(idx):
            for v, j in enumerate(idx):
                Bm[i, j] = q[u, v]
    V = Q0 @ Bm @ np.linalg.inv(Q0)
    comm_err = float(np.max(np.abs(V @ Mf - Mf @ V)))
    cyc_types = []
    for seed in (0, 1, 2, 3):
        rng = np.random.default_rng(seed)
        Hh = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
        Hh = (Hh + Hh.conj().T) / 2
        _, Q = np.linalg.eig(Mf + 1e-6 * Hh)
        S = np.abs(np.linalg.solve(Q, V @ Q))
        perm = [int(np.argmax(S[:, j])) for j in range(N)]
        seen, cyc = set(), []
        for s in range(N):
            if s in seen:
                continue
            ln, x = 0, s
            while x not in seen:
                seen.add(x)
                x = perm[x]
                ln += 1
            cyc.append(ln)
        cyc_types.append(tuple(sorted(cyc, reverse=True)))
        print(f"  seed={seed}: tracked cycle type at l=1 = {tuple(sorted(cyc, reverse=True))}")
    print(f"  (V commutes with M(1) to {comm_err:.2e}; it IS a legitimate loop monodromy)")
    stable = len(set(cyc_types)) == 1
    print(f"  commutant dim: l=0 -> {d0} (= 15, simple spectrum, labels canonical); "
          f"l=1 -> {d1} (= 4^2+4^2+3^2+4^2 = 57, labels NOT canonical)")
    print(f"  cycle type seed-stable at l=1: {stable}")
    OUT['L5'] = dict(commutant_dim_l0=d0, commutant_dim_l1=d1, V_commutator_err=comm_err,
                     expected_l1=4 * 4 + 4 * 4 + 3 * 3 + 4 * 4,
                     seed_cycle_types=[list(c) for c in cyc_types],
                     cycle_type_seed_stable=bool(stable),
                     labels_canonical_l0=bool(d0 == 15),
                     labels_canonical_l1=bool(d1 == 15))
    return d0, d1, stable


# ------------------------------------------------------------------------------- verdict

def main():
    l1 = leg1()
    l2 = leg2()
    l3_law, c6_sqrt5, c6_sqrt15 = leg3()
    l4_contrast, l4_l1_uniform, l4_same = leg4()
    d0, d1, cyc_stable = leg5()

    print()
    print("== VERDICT BLOCK ==")

    # --- the three residual items, adjudicated
    C6 = "REPRODUCED+DERIVED" if (l3_law and c6_sqrt5) else ("NULL" if l3_law else "INDETERMINATE")
    C7 = "REPRODUCED+DERIVED" if (l2 and l4_contrast) else ("NULL" if l2 else "INDETERMINATE")
    # C5's load-bearing exact fact is the commutant dimension: labels (hence a cycle type
    # on labels) are canonical iff the commutant is the diagonal torus (dim = 15).
    if d0 == 15 and d1 != 15:
        C5 = "CANONICAL@l=0 / NON-IDENTIFIABLE@l=1"
    elif d0 == 15 and d1 == 15:
        C5 = "CANONICAL everywhere"
    else:
        C5 = "INDETERMINATE"
    print(f"  C6 (max address trace)   : {C6}")
    print(f"  C7 (dark-phase contrast) : {C7}")
    print(f"  C5 (loop cycle structure): {C5}")

    law_holds = l1 and l2 and l3_law
    reproduced = sum(x == "REPRODUCED+DERIVED" for x in (C6, C7))

    # branch A: the residual construct has a determinate canonical realization that
    #           reproduces its content and has a named exact mechanism
    A = bool(law_holds and reproduced >= 2)
    # branch B: the residual construct has NO determinate content on the canonical
    #           per-address family (uniform traces, no contrast anywhere) -> tombstone
    B = bool(law_holds and reproduced == 0 and l4_l1_uniform)
    verdict = "RESOLVED-A" if (A and not B) else ("RESOLVED-B" if (B and not A) else "UNRESOLVED")

    print(f"  branch-A fired: {A}   branch-B fired: {B}")
    print(f"  VERDICT: {verdict}")
    print(f"  non-vacuity: branch B's shape IS realized inside this same family at l=1 "
          f"(uniform address spectra, max|tr|=1): {l4_l1_uniform}")

    OUT['verdict'] = dict(
        verdict=verdict, branch_A=A, branch_B=B,
        C5=C5, C6=C6, C7=C7,
        law_holds=bool(law_holds), n_reproduced=int(reproduced),
        nonvacuity_B_shape_realized_at_l1=bool(l4_l1_uniform),
        discriminating_fact=(
            "Affine Weil character law, exact at 2 primes and 4 levels: tr(W_A T(v)) = 0 "
            "unless v in im(A-I), and |tr|^2 = |ker(A-I)| there. For the single-generator "
            "monodromy Par*W1 the shadow is -A1 with det(-A1 - I) = det A1 + tr A1 + 1 = "
            "1+3+1 = 5 = m^2+4 (golden), so |ker| = 5: EXACTLY 45 bright addresses with "
            "|tr| = sqrt5 (seat-1's C6 value, derived) and 180 dark; dark addresses carry "
            "15 distinct eigenphases, bright carry 9 (seat-1's C7 direction, exact). At "
            "l=1 Fricke tr(A1A2)=15=0 mod 15 makes A-I invertible, so ALL 225 addresses "
            "are bright with |tr|=1 and identical spectra -- no contrast: the negative "
            "branch is realized in the same family."),
        elapsed_s=round(time.time() - T0, 1))

    with open("<repo>/frontier/B775_phase2_wave1/cells/"
              "P2W5-B465/results.json", "w") as f:
        json.dump(OUT, f, separators=(',', ':'), sort_keys=True)
    print(f"  elapsed {time.time() - T0:.1f}s -> results.json")
    return 0


if __name__ == '__main__':
    sys.exit(main())
