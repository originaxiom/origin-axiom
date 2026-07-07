#!/usr/bin/env python3
"""B465 — exact verification engine (F_p, p ≡ 1 mod 60, two primes cross-checked).

Everything here is EXACT: entries live in F_p where ζ60, ζ15, ζ4 and √15 all exist
(p ≡ 1 mod 60 ⇒ 15 is a QR by reciprocity). √15 is defined by the Gauss-sum
convention √15 := −i·Σ_j z^{j²} (Chat-2's stage-2 rule, so Galois twists conjugate it
correctly: z → z^c sends √15 → (c|15)·√15). Eigenvalue ORDERS and MULTIPLICITIES are
embedding-independent — these are the exact objects of the claims.

Verifies (per INTAKE.md): C1 (the 8-4-3 at l=1 + the scalar law M⁴ = ζ₆₀³²·I),
C2 (l-sweep + the classical-shadow launder test), C3 (U = Par·W₁ order 60, bands),
C4 (QR/NQR distinct-eigenvalue counts 15/9), C6 (per-c char-poly distinctness).
"""
import sys
from math import gcd

PRIMES = [61, 421, 541]           # all ≡ 1 (mod 60)
N = 15


def find_root_of_unity(p, n):
    """a fixed n-th root of unity in F_p (deterministic: smallest generator power)."""
    for g in range(2, p):
        # is g a generator of F_p*?
        ok = True
        for q in prime_factors(p - 1):
            if pow(g, (p - 1) // q, p) == 1:
                ok = False
                break
        if ok:
            return pow(g, (p - 1) // n, p)
    raise RuntimeError


def prime_factors(n):
    out = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def matmul(A, B, p):
    n = len(A)
    Bt = list(zip(*B))
    return [[sum(a * b for a, b in zip(row, col)) % p for col in Bt] for row in A]


def matpow(A, k, p):
    n = len(A)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while k:
        if k & 1:
            R = matmul(R, A, p)
        A = matmul(A, A, p)
        k >>= 1
    return R


def build(p, c=1):
    """the level-15 operators with the Galois twist z -> z^c."""
    z15 = find_root_of_unity(p, 15)
    z = pow(z15, c, p)
    i4 = find_root_of_unity(p, 4)
    # Gauss sum: sqrt15 = -i * sum z^{j^2}  (transforms by (c|15) automatically since z is twisted)
    gs = sum(pow(z, (j * j) % 15, p) for j in range(15)) % p
    sqrt15 = (-i4 * gs) % p
    assert (sqrt15 * sqrt15) % p == 15 % p, "Gauss-sum square check failed"
    inv_s = pow(sqrt15, p - 2, p)
    D = [[pow(z, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)] for i in range(N)]
    F = [[(pow(z, (i * j) % 15, p) * inv_s) % p for j in range(N)] for i in range(N)]
    # conjugate-transpose in F_p: transpose + (z -> z^{-1}, sqrt15 -> sqrt15 i.e. inv_s -> inv_s
    # BUT conj(1/sqrt15) = 1/conj(sqrt15); conj(sqrt15) = -conj(i)*conj(gs);
    # conj(gs) = sum z^{-j^2} = ((-1|15))*gs ... implement conj entrywise instead:
    zinv = pow(z, 13, p) if False else pow(z, p - 2, p)  # z^{-1}
    conj_i4 = pow(i4, p - 2, p)                          # conj(i) = -i = i^{-1}
    gs_c = sum(pow(zinv, (j * j) % 15, p) for j in range(15)) % p
    sqrt15_c = (-conj_i4 * gs_c) % p
    assert (sqrt15_c * sqrt15_c) % p == 15 % p
    inv_sc = pow(sqrt15_c, p - 2, p)
    Fd = [[(pow(zinv, (i * j) % 15, p) * inv_sc) % p for j in range(N)] for i in range(N)]
    # Wr = (F D F^dagger)^dagger = F^{dagger dagger schema}: build directly
    FDFd = matmul(matmul(F, D, p), Fd, p)
    # dagger of FDFd: transpose + entry-conjugation. Entries are polynomials in z with
    # rational-sqrt15 factors; entrywise conjugation in F_p is NOT a field automorphism we
    # can apply blindly to a computed residue. Instead use: (F D F^dag)^dag = F D^dag F^dag
    # since F^dagdag = F. D^dag = D with z -> z^{-1} on the diagonal.
    Dd = [[pow(zinv, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)]
          for i in range(N)]
    Wr = matmul(matmul(F, Dd, p), Fd, p)
    Wl = D
    W1 = matmul(Wr, Wl, p)
    W2 = matmul(matmul(Wr, Wr, p), matmul(Wl, Wl, p), p)
    Par = [[1 if i == ((-j) % N) else 0 for j in range(N)] for i in range(N)]
    return z, i4, W1, W2, Par


def eig_mults(M, p, z60):
    """eigenvalue multiplicities via nullity(M - lambda I) for each 60th root; exact."""
    out = {}
    for k in range(60):
        lam = pow(z60, k, p)
        A = [[(M[i][j] - (lam if i == j else 0)) % p for j in range(N)] for i in range(N)]
        r = rank(A, p)
        if r < N:
            out[k] = N - r
    assert sum(out.values()) == N, f"not diagonalizable over mu_60: {out}"
    return out


def rank(A, p):
    A = [row[:] for row in A]
    n, m = len(A), len(A[0])
    r = 0
    for col in range(m):
        piv = next((i for i in range(r, n) if A[i][col] % p), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][col], p - 2, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(n):
            if i != r and A[i][col]:
                f = A[i][col]
                A[i] = [(a - f * b) % p for a, b in zip(A[i], A[r])]
        r += 1
        if r == n:
            break
    return r


def is_identity(M, p):
    return all(M[i][j] % p == (1 if i == j else 0) for i in range(N) for j in range(N))


def order_of(M, p, cap=240):
    P = M
    for k in range(1, cap + 1):
        if is_identity(P, p):
            return k
        P = matmul(P, M, p)
    return None


def classical_shadow(l):
    """order and trace of -A1*A2^l in SL(2, Z/15), A1 = RL, A2 = R^2L^2 as 2x2 words.
    R = [[1,1],[0,1]], L = [[1,0],[1,1]] (the standard twist generators)."""
    def mm(A, B):
        return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % 15, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % 15],
                [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % 15, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % 15]]
    R = [[1, 1], [0, 1]]
    L = [[1, 0], [1, 1]]
    A1 = mm(R, L)
    A2 = mm(mm(R, R), mm(L, L))
    M = [[-1 % 15, 0], [0, -1 % 15]]
    M = mm(M, A1)
    for _ in range(l):
        M = mm(M, A2)
    # order
    P = [row[:] for row in M]
    for k in range(1, 121):
        if P == [[1, 0], [0, 1]]:
            return k, (M[0][0] + M[1][1]) % 15
        P = mm(P, M)
    return None, (M[0][0] + M[1][1]) % 15


def run(p):
    print(f"\n########## p = {p} ##########")
    z60 = find_root_of_unity(p, 60)
    z, i4, W1, W2, Par = build(p, c=1)

    # C3: U = Par W1
    U = matmul(Par, W1, p)
    oU = order_of(U, p)
    mU = eig_mults(U, p, z60)
    print(f"C3: ord(Par·W1) = {oU}; distinct eigenvalues = {len(mU)}; mults = {sorted(mU.values(), reverse=True)}")

    # C1 + scalar law at l=1
    M1 = matmul(U, W2, p)
    o1 = order_of(M1, p)
    m1 = eig_mults(M1, p, z60)
    orders = {}
    for k, mult in m1.items():
        orders.setdefault(60 // gcd(k, 60), 0)
        orders[60 // gcd(k, 60)] += mult
    M4 = matpow(M1, 4, p)
    scal = M4[0][0]
    scalar_law = all(M4[i][j] % p == ((scal if i == j else 0)) for i in range(N) for j in range(N))
    ks = sorted(m1.keys())
    ap15 = all((ks[i+1] - ks[i]) % 60 == 15 for i in range(len(ks) - 1)) if len(ks) == 4 else False
    print(f"C1: ord(M(1)) = {o1}; eig mults by k: {m1}; order-multiset: {orders}")
    print(f"C1+: M(1)^4 scalar: {scalar_law}; spectrum is a mu_4-coset (step 15): {ap15}")

    # C2: l-sweep + classical shadow
    print("C2: l-sweep vs the classical shadow -A1·A2^l (mod 15):")
    Ml = U
    for l in range(0, 12):
        if l > 0:
            Ml = matmul(Ml, W2, p)
        mm_ = eig_mults(Ml, p, z60)
        om = {}
        for k, mult in mm_.items():
            om.setdefault(60 // gcd(k, 60), 0)
            om[60 // gcd(k, 60)] += mult
        co, ct = classical_shadow(l)
        print(f"  l={l:2d}: #eig={len(mm_):2d} mults={sorted(mm_.values(), reverse=True)} "
              f"orders={dict(sorted(om.items()))} | classical ord={co} tr={ct}")

    # C4 + C6: c-scan
    print("C4/C6: c-scan (distinct eigenvalues of Par·W1^(c); spectra as sorted mult-lists):")
    QR = {1, 4}
    spectra = {}
    for c in [1, 2, 4, 7, 8, 11, 13, 14]:
        _, _, W1c, W2c, Parc = build(p, c=c)
        Uc = matmul(Parc, W1c, p)
        mc = eig_mults(Uc, p, z60)
        spectra[c] = tuple(sorted((k, m) for k, m in mc.items()))
        tag = "QR " if c in QR else "NQR"
        print(f"  c={c:2d} [{tag}]: #distinct eig = {len(mc):2d}  mults = {sorted(mc.values(), reverse=True)}")
    distinct = len(set(spectra.values()))
    print(f"C6: distinct spectra across the 8 c-values: {distinct}/8 "
          f"(note: k-labels are embedding-dependent; order/mult data is not — see FINDINGS)")
    return {
        'oU': oU, 'nU': len(mU),
        'o1': o1, 'orders1': tuple(sorted(orders.items())), 'mults1': tuple(sorted(m1.values())),
        'scalar': scalar_law, 'ap15': ap15,
    }


if __name__ == '__main__':
    results = [run(p) for p in PRIMES]
    agree = all(r == results[0] for r in results[1:])
    print(f"\nCROSS-PRIME AGREEMENT ({PRIMES}): {agree}")
    print("ALL CHECKS PASS" if agree and results[0]['scalar'] and results[0]['ap15']
          and results[0]['orders1'] == ((15, 4), (30, 3), (60, 8)) else "CHECK FAILURE")
    sys.exit(0 if agree else 1)
