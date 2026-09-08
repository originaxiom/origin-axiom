#!/usr/bin/env python3
"""The 2x2 criterion at scale: characters of H_1(Y_n) = coker(Phi^n - I) parametrised by the Smith form (no filtering),
processed in chunks; h^1 = 1 iff A(x_{n-1}) ... A(x_0) = I (modulo two primes = 1 mod m), x_k = F_{2k+1} w1 + F_{2k} w2.
For the positives: order, Psi-eigenvalue u (Psi = [[1,1],[1,0]], Phi = Psi^2), the refined-law classification, the family
characters (order-2 positives, 3 | n), closure under the family group, the alphabet K3 and K2.  Writes support_mt_Y{n}.json."""
import sys, math, json, time, collections, pathlib
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path('.')
Phi = sp.Matrix([[2, 1], [1, 1]])

def smith(n):
    M = Phi ** n - sp.eye(2)
    D, U, V = smith_normal_decomp(M, domain=sp.ZZ)
    D, U, V = sp.Matrix(D), sp.Matrix(U), sp.Matrix(V)
    assert U * M * V == D
    d1, d2 = abs(int(D[0, 0])), abs(int(D[1, 1]))
    m = d1 * d2 // math.gcd(d1, d2)
    return d1, d2, m, [[int(U[i, j]) for j in range(2)] for i in range(2)]

def fib_pairs(n, m):
    F = [0, 1]
    while len(F) < 2 * n + 2:
        F.append(F[-1] + F[-2])
    return [(F[2 * k + 1] % m, F[2 * k] % m) for k in range(n)]

def primes_1_mod(m, count=2, start=10 ** 9):
    out = []; q = start - (start % m) + 1
    while len(out) < count:
        if sp.isprime(q):
            out.append(q)
        q += m
    return out

def identity_test(w1, w2, n, m, q, fib):
    g = sp.primitive_root(q); zeta = pow(g, (q - 1) // m, q)
    powz = np.array([pow(zeta, e, q) for e in range(m)], dtype=np.int64)
    N = len(w1)
    a = np.ones(N, dtype=np.int64); b = np.zeros(N, dtype=np.int64); c = np.zeros(N, dtype=np.int64); d = np.ones(N, dtype=np.int64)
    for k in range(n):
        p, r = fib[k]
        x = powz[(p * w1 + r * w2) % m]
        a11 = (1 + x) % q; a12 = (x * x) % q; a22 = x
        na = (a11 * a + a12 * c) % q; nb = (a11 * b + a12 * d) % q
        nc = (a + a22 * c) % q; nd = (b + a22 * d) % q
        a, b, c, d = na, nb, nc, nd
    return (a == 1) & (b == 0) & (c == 0) & (d == 1)

def level(n, chunk=6_000_000):
    t0 = time.time()
    d1, d2, m, U = smith(n)
    total = d1 * d2
    fib = fib_pairs(n, m)
    qs = primes_1_mod(m)
    rows_per = max(1, chunk // d2)
    positives = []
    c2 = np.arange(d2, dtype=np.int64)
    for c1s in range(0, d1, rows_per):
        c1 = np.arange(c1s, min(d1, c1s + rows_per), dtype=np.int64)
        C1, C2 = np.meshgrid(c1, c2, indexing='ij'); C1, C2 = C1.ravel(), C2.ravel()
        e1 = (C1 * (m // d1)) % m; e2 = (C2 * (m // d2)) % m
        w1 = (U[0][0] * e1 + U[1][0] * e2) % m; w2 = (U[0][1] * e1 + U[1][1] * e2) % m     # w = U^T (e1, e2)
        ok = identity_test(w1, w2, n, m, qs[0], fib)
        if ok.any():
            idx = np.where(ok)[0]
            ok2 = identity_test(w1[idx], w2[idx], n, m, qs[1], fib)
            for i, j in enumerate(idx):
                if ok2[i] and not (w1[j] == 0 and w2[j] == 0):
                    positives.append((int(w1[j]), int(w2[j])))
    pos = sorted(set(positives))
    order = lambda w: m // math.gcd(math.gcd(w[0], w[1]), m)
    byord = collections.Counter(order(w) for w in pos)
    # Psi-eigenvalue: Psi^T w = (w1 + w2, w1) = u w mod m
    def eigen(w):
        N = order(w); pw = ((w[0] + w[1]) % m, w[0] % m)
        for u in range(N):
            if (u * w[0] - pw[0]) % m == 0 and (u * w[1] - pw[1]) % m == 0:
                return u
        return None
    law = collections.Counter()
    for w in pos:
        N = order(w)
        if N % 2 == 0:
            law[('even order', N)] += 1; continue
        u = eigen(w)
        if u is None:
            law[('odd, not eigen',)] += 1; continue
        lam = u * u % N
        ok2 = all(sp.n_order(lam % p, p) >= 3 if lam % p != 1 else False for p in sp.factorint(N))
        s = pow(u, n, N)
        law[('odd eigen', 'lam_ord>=3' if ok2 else 'lam_ord<3', 'u^n=+-1' if s in (1, N - 1) else 'u^n mixed')] += 1
    S = set(pos)
    chis = [w for w in pos if order(w) == 2]
    add = lambda a, b: ((a[0] + b[0]) % m, (a[1] + b[1]) % m)
    closed = all(add(w, c) in S or add(w, c) == (0, 0) for w in pos for c in chis) if chis else None
    K3 = K2 = None
    if len(chis) == 3:
        cands = {add(w, c) for w in pos + [(0, 0)] for c in chis + [(0, 0)]}
        G = {w: sum(1 for c in chis if add(w, c) in S) for w in cands}
        K3 = sorted(w for w, g in G.items() if g >= 3); K2 = sorted(w for w, g in G.items() if g == 2)
    print(f"Y_{n}: H_1 = Z/{d1} + Z/{d2} ({total} characters, exponent {m}); support {len(pos)}, by order {dict(sorted(byord.items()))}; "
          f"law {dict(sorted(law.items(), key=str))}; family {len(chis)}; closed under family: {closed}; K3 {len(K3) if K3 is not None else '-'}, K2 {len(K2) if K2 is not None else '-'}  ({time.time() - t0:.0f} s)", flush=True)
    data = dict(n=n, d1=d1, d2=d2, m=m, U=U, positives=pos, chis=chis, K3=K3, K2=K2, byord={str(k): v for k, v in byord.items()},
                law={str(k): v for k, v in law.items()})
    (OUT / f"support_mt_Y{n}.json").write_text(json.dumps(data))
    return data

if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[2:]]:
        level(n)
