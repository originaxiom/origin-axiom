# e1_modnull.py -- modular-discovery / exact-certificate linear algebra over
# K = Q(sqrt(-3)), reused wholesale from loop4/d2_351/d2_modnull.py (same
# soundness argument: discovery runs over GF(p) under BOTH sqrt(-3) embeddings
# -- numpy, fast -- every result is then verified EXACTLY over K; no modular
# result is trusted unverified).
#
# Adds modular_solve_multi(...): a particular-solution solver for A.y = b_k
# (several right-hand sides at once, ONE shared augmented RREF pass per prime)
# -- needed for the SELF-SILENT verdict path (exact coboundary solve), which
# modular_leftnull's kernel-only machinery does not provide. Not needed by
# loop4/d2_351 (all six of its off-diagonal pairs SPOKE, so no SILENT case
# ever arose there); E1's diagonal may produce one.
from fractions import Fraction
import numpy as np


def _is_probable_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _tonelli(a, p):
    a %= p
    if a == 0:
        return 0
    assert pow(a, (p - 1) // 2, p) == 1, "not a QR"
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, tt = 0, t
        while tt != 1:
            tt = tt * tt % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t, r = t * c % p, r * b % p
    return r


def make_primes(count, start=1 << 30):
    out, n = [], start | 1
    while len(out) < count:
        if _is_probable_prime(n) and n % 3 == 1:
            out.append(n)
        n += 2
    return out


def _entry_modp(x, p, z):
    # x is a K instance with .a, .b (int or Fraction); K value = a + b*sqrt(-3)
    def fmod(f):
        f = Fraction(f)
        if f.denominator % p == 0:
            raise ZeroDivisionError("denominator divisible by p")
        return f.numerator * pow(f.denominator, -1, p) % p
    return (fmod(x.a) + fmod(x.b) * z) % p


def _gfp_rref_kernel(A, p):
    # A: numpy 2D array mod p, p < 2^31 so int64 products (< 2^62) are exact.
    # Returns rank, pivots, free cols, kernel basis mod p (one vector per free
    # col: v[free]=1, v[piv[i]]=-R[i][free]).
    A = (A.astype(np.int64)) % p
    rows, cols = A.shape
    r = 0
    piv = []
    for c in range(cols):
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        pr = r + int(nz[0])
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), -1, p)
        A[r] = (A[r] * inv) % p
        col = A[:, c].copy()
        col[r] = 0
        mask = col != 0
        if mask.any():
            A[mask] = (A[mask] - col[mask, None] * A[r][None, :]) % p
        piv.append(c)
        r += 1
        if r == rows:
            break
    free = [c for c in range(cols) if c not in set(piv)]
    kern = []
    for fc in free:
        v = [0] * cols
        v[fc] = 1
        for ri, pc in enumerate(piv):
            v[pc] = (-int(A[ri, fc])) % p
        kern.append(v)
    return r, piv, free, kern


def _gfp_rref_augmented(Ab, p, n_cols):
    """Ab: numpy 2D array mod p, shape (rows, n_cols + n_rhs). Pivot search is
    restricted to the FIRST n_cols columns (the coefficient block); the SAME
    row operations are applied to the RHS columns. Returns rank, pivots, free
    cols (within n_cols), per-RHS consistency flags, and per-RHS particular
    solutions (free vars set to 0)."""
    A = (Ab.astype(np.int64)) % p
    rows, cols_total = A.shape
    n_rhs = cols_total - n_cols
    r = 0
    piv = []
    for c in range(n_cols):
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        pr = r + int(nz[0])
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), -1, p)
        A[r] = (A[r] * inv) % p
        col = A[:, c].copy()
        col[r] = 0
        mask = col != 0
        if mask.any():
            A[mask] = (A[mask] - col[mask, None] * A[r][None, :]) % p
        piv.append(c)
        r += 1
        if r == rows:
            break
    free = [c for c in range(n_cols) if c not in set(piv)]
    consistent = [True] * n_rhs
    for i in range(r, rows):
        for rhs in range(n_rhs):
            if int(A[i, n_cols + rhs]) % p != 0:
                consistent[rhs] = False
    sol = []
    for rhs in range(n_rhs):
        y = [0] * n_cols
        for ri, pc in enumerate(piv):
            y[pc] = int(A[ri, n_cols + rhs]) % p
        sol.append(y)
    return r, piv, free, consistent, sol


def _crt_pair(a1, m1, a2, m2):
    d = pow(m1, -1, m2)
    t = (a2 - a1) * d % m2
    return a1 + m1 * t, m1 * m2


def _rat_recon(u, M):
    # Wang: find a/b with u*b = a mod M, |a|, b <= sqrt(M/2)
    u %= M
    a0, a1 = M, u
    b0, b1 = 0, 1
    bound = int((M // 2) ** 0.5)
    while a1 > bound:
        q = a0 // a1
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    if b1 == 0 or abs(b1) > bound:
        raise ValueError("reconstruction failed")
    if b1 < 0:
        a1, b1 = -a1, -b1
    from math import gcd
    if gcd(a1, b1) != 1:
        raise ValueError("not coprime")
    return Fraction(a1, b1)


def _embed_and_kernel(Ft_rows, p, z, n_rows, n_cols):
    A = np.empty((n_rows, n_cols), dtype=object)
    for i, row in enumerate(Ft_rows):
        for j, x in enumerate(row):
            A[i, j] = _entry_modp(x, p, z)
    return _gfp_rref_kernel(A, p)


def modular_leftnull(Ft_rows, Kclass, log, label, max_primes=40):
    """Ft_rows: list of rows (lists) of K instances = F^T. Returns exact,
    verified, complete left-null basis as list of K-vectors. The kernel is a
    K-vector space; RREF normal form is CANONICAL, so eliminating under BOTH
    embeddings sqrt(-3) -> z and -> p-z yields the two conjugate images of the
    same canonical kernel vector; each entry's (a,b) solves from the pair."""
    n_rows, n_cols = len(Ft_rows), len(Ft_rows[0])
    per_prime = {}  # p -> (rank, piv, free, kern_z1, kern_z2, z)

    def add_prime(p):
        z = _tonelli(p - 3, p)
        rank1, piv1, free1, kern1 = _embed_and_kernel(Ft_rows, p, z, n_rows, n_cols)
        rank2, piv2, free2, kern2 = _embed_and_kernel(Ft_rows, p, p - z, n_rows, n_cols)
        if (rank1, piv1) != (rank2, piv2):
            log(f"    [{label}] mod {p}: conjugate embeddings disagree on pivots -- SKIP prime")
            return
        per_prime[p] = (rank1, piv1, free1, kern1, kern2, z)
        log(f"    [{label}] mod {p}: rank {rank1}, ker dim {len(free1)} (both embeddings)")

    for p in make_primes(4):
        add_prime(p)
    best = max(per_prime.items(), key=lambda kv: kv[1][0])
    rank0, piv0, free0 = best[1][0], best[1][1], best[1][2]
    agree = {p: v for p, v in per_prime.items() if (v[0], tuple(v[1])) == (rank0, tuple(piv0))}
    log(f"    [{label}] consensus: rank {rank0}, ker dim {len(free0)}, primes agreeing {len(agree)}")

    def try_reconstruct():
        basis = []
        inv2 = {p: pow(2, -1, p) for p in agree}
        invz2 = {p: pow(2 * agree[p][5] % p, -1, p) for p in agree}
        for k_idx in range(len(free0)):
            ra, rb = {}, {}
            for p, (_, _, _, k1, k2, z) in agree.items():
                for j in range(n_cols):
                    r1, r2 = k1[k_idx][j], k2[k_idx][j]
                    aa = (r1 + r2) * inv2[p] % p
                    bb = (r1 - r2) * invz2[p] % p
                    for store, val in ((ra, aa), (rb, bb)):
                        if j in store:
                            store[j] = _crt_pair(store[j][0], store[j][1], val, p)
                        else:
                            store[j] = (val, p)
            vec = []
            for j in range(n_cols):
                fa = _rat_recon(*ra[j])
                fb = _rat_recon(*rb[j])
                vec.append((fa, fb))
            basis.append(vec)
        return basis

    while True:
        try:
            pair_basis = try_reconstruct()
            break
        except ValueError:
            if len(agree) >= max_primes:
                raise RuntimeError(f"[{label}] reconstruction failed at {max_primes} primes")
            for p in make_primes(4, start=max(per_prime) + 2):
                add_prime(p)
                if p in per_prime and (per_prime[p][0], tuple(per_prime[p][1])) == (rank0, tuple(piv0)):
                    agree[p] = per_prime[p]
            log(f"    [{label}] reconstruction retry with {len(agree)} agreeing primes")

    K0 = Kclass(0, 0)
    basis_K = [[Kclass(fa, fb) for (fa, fb) in vec] for vec in pair_basis]
    import time as _t
    t0 = _t.time()
    for vi, v in enumerate(basis_K):
        for i, row in enumerate(Ft_rows):
            s = K0
            for j in range(n_cols):
                if not v[j].is_zero():
                    s = s + row[j] * v[j]
            if not s.is_zero():
                raise RuntimeError(f"[{label}] EXACT VERIFY FAILED: vector {vi}, row {i} "
                                   "(kernel may need sqrt(-3) components -- escalate)")
        if vi % 10 == 0:
            log(f"    [{label}] exact-verified {vi + 1}/{len(basis_K)} ({_t.time() - t0:.1f}s)")
    log(f"    [{label}] EXACT VERIFY: all {len(basis_K)} kernel vectors satisfy F^T v = 0 "
        f"over K; completeness: dim ker_Q <= {n_cols} - rank_Fp({rank0}) = {n_cols - rank0} "
        f"= verified count -> basis COMPLETE ({_t.time() - t0:.1f}s)")
    return basis_K


def modular_solve_multi(A_rows, b_vecs, Kclass, log, label, max_primes=60):
    """Solve A.y = b for EACH b in b_vecs (several right-hand sides at once,
    ONE shared augmented-RREF pass per prime -- the pivot structure of A is
    reused across all RHS columns). Returns {rhs_index: (consistent, y_or_None)}
    with y EXACTLY verified (A.y == b entrywise over K) whenever consistent.
    Soundness: same discover-mod-p-then-verify-over-K discipline as
    modular_leftnull; a RHS flagged inconsistent under a modular reduction that
    otherwise matches the rank/pivot consensus is reported as a WARNING (not
    silently dropped) since it should not occur when the caller has already
    established -- via the complete leftnull basis pairing to zero -- that a
    solution must exist over K.
    """
    n_rows = len(A_rows)
    n_cols = len(A_rows[0])
    n_rhs = len(b_vecs)
    per_prime = {}

    def embed_system(p, z):
        Ab = np.empty((n_rows, n_cols + n_rhs), dtype=object)
        for i, row in enumerate(A_rows):
            for j, x in enumerate(row):
                Ab[i, j] = _entry_modp(x, p, z)
            for k, bv in enumerate(b_vecs):
                Ab[i, n_cols + k] = _entry_modp(bv[i], p, z)
        return _gfp_rref_augmented(Ab, p, n_cols)

    def add_prime(p):
        z = _tonelli(p - 3, p)
        r1, piv1, free1, cons1, sol1 = embed_system(p, z)
        r2, piv2, free2, cons2, sol2 = embed_system(p, p - z)
        if (r1, piv1) != (r2, piv2):
            log(f"    [{label}] mod {p}: conjugate embeddings disagree on pivots -- SKIP prime")
            return
        per_prime[p] = (r1, piv1, free1, cons1, sol1, cons2, sol2, z)
        log(f"    [{label}] mod {p}: rank {r1}, per-rhs consistent={cons1}")

    for p in make_primes(4):
        add_prime(p)
    if not per_prime:
        raise RuntimeError(f"[{label}] no usable primes found")
    best = max(per_prime.items(), key=lambda kv: kv[1][0])
    rank0, piv0 = best[1][0], best[1][1]
    agree = {p: v for p, v in per_prime.items() if (v[0], tuple(v[1])) == (rank0, tuple(piv0))}
    log(f"    [{label}] consensus: rank {rank0}, primes agreeing {len(agree)}")

    overall_consistent = [all(v[3][rhs] for v in agree.values()) for rhs in range(n_rhs)]
    for rhs in range(n_rhs):
        if not overall_consistent[rhs]:
            log(f"    [{label}] WARNING: rhs {rhs} appears INCONSISTENT under modular "
                "reduction at consensus-rank primes (unexpected if the leftnull-pairing "
                "already certified vanishing -- treated as UNDECIDED, not SILENT)")

    def try_reconstruct(rhs):
        inv2 = {p: pow(2, -1, p) for p in agree}
        invz2 = {p: pow(2 * agree[p][7] % p, -1, p) for p in agree}
        ra, rb = {}, {}
        for p, (_, _, _, _cons1, sol1, _cons2, sol2, z) in agree.items():
            s1, s2 = sol1[rhs], sol2[rhs]
            for j in range(n_cols):
                r1v, r2v = s1[j], s2[j]
                aa = (r1v + r2v) * inv2[p] % p
                bb = (r1v - r2v) * invz2[p] % p
                for store, val in ((ra, aa), (rb, bb)):
                    if j in store:
                        store[j] = _crt_pair(store[j][0], store[j][1], val, p)
                    else:
                        store[j] = (val, p)
        vec = []
        for j in range(n_cols):
            fa = _rat_recon(*ra[j])
            fb = _rat_recon(*rb[j])
            vec.append((fa, fb))
        return vec

    K0 = Kclass(0, 0)
    results = {}
    for rhs in range(n_rhs):
        if not overall_consistent[rhs]:
            results[rhs] = (False, None)
            continue
        while True:
            try:
                pair_vec = try_reconstruct(rhs)
                break
            except ValueError:
                if len(agree) >= max_primes:
                    raise RuntimeError(f"[{label}] reconstruction failed for rhs {rhs} at {max_primes} primes")
                for p in make_primes(4, start=max(per_prime) + 2):
                    add_prime(p)
                    if p in per_prime and (per_prime[p][0], tuple(per_prime[p][1])) == (rank0, tuple(piv0)):
                        agree[p] = per_prime[p]
                log(f"    [{label}] reconstruction retry (rhs {rhs}) with {len(agree)} agreeing primes")
        y = [Kclass(fa, fb) for (fa, fb) in pair_vec]
        ok = True
        for i, row in enumerate(A_rows):
            s = K0
            for j in range(n_cols):
                if not y[j].is_zero():
                    s = s + row[j] * y[j]
            if not (s - b_vecs[rhs][i]).is_zero():
                ok = False
                break
        if not ok:
            raise RuntimeError(f"[{label}] EXACT VERIFY FAILED for rhs {rhs}: A.y != b at some row")
        results[rhs] = (True, y)
        log(f"    [{label}] rhs {rhs}: EXACT-VERIFIED A.y = b over K (coboundary found)")
    return results
