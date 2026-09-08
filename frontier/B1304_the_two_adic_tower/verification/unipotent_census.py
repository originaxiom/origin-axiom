#!/usr/bin/env python3
"""THE UNIPOTENT STRUCTURE (B1304): for every character of H_1(Y_n) the product P = A(x_{n-1}) ... A(x_0) has det P =
prod x_k (= 1 for a character of the branched cover?) and its trace is computed exactly modulo two primes; the census of
(trace = 2 and det = 1, i.e. P unipotent) against h^1 = 1 (P = I) and against the Psi-eigencharacters.  Question: is
P unipotent exactly on the eigencharacters (then the law is about the vanishing of a nilpotent part)?"""
import sys, math, time, collections, pathlib
import numpy as np
import sympy as sp
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'B1303_the_two_by_two_criterion' / 'verification'))
import criterion_at_scale as S

def product_mod(w1, w2, n, m, q, fib):
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
    tr = (a + d) % q; det = (a * d - b * c) % q
    ident = (a == 1) & (b == 0) & (c == 0) & (d == 1)
    return tr, det, ident

def level(n, chunk=6_000_000):
    t0 = time.time()
    d1, d2, m, U = S.smith(n)
    fib = S.fib_pairs(n, m); qs = S.primes_1_mod(m)
    rows_per = max(1, chunk // d2)
    c2 = np.arange(d2, dtype=np.int64)
    cls = collections.Counter()
    unip = []
    for c1s in range(0, d1, rows_per):
        c1 = np.arange(c1s, min(d1, c1s + rows_per), dtype=np.int64)
        C1, C2 = np.meshgrid(c1, c2, indexing='ij'); C1, C2 = C1.ravel(), C2.ravel()
        e1 = (C1 * (m // d1)) % m; e2 = (C2 * (m // d2)) % m
        w1 = (U[0][0] * e1 + U[1][0] * e2) % m; w2 = (U[0][1] * e1 + U[1][1] * e2) % m
        tr1, det1, id1 = product_mod(w1, w2, n, m, qs[0], fib)
        tr2, det2, id2 = product_mod(w1, w2, n, m, qs[1], fib)
        u = (tr1 == 2) & (det1 == 1) & (tr2 == 2) & (det2 == 1)
        d_one = (det1 == 1) & (det2 == 1)
        ident = id1 & id2
        triv = (w1 == 0) & (w2 == 0)
        for key, cnt in zip(*np.unique(np.stack([u, d_one, ident, triv], axis=1), axis=0, return_counts=True)):
            cls[tuple(bool(x) for x in key)] += int(cnt)
        for j in np.where(u & ~triv)[0]:
            unip.append((int(w1[j]), int(w2[j])))
    order = lambda w: m // math.gcd(math.gcd(w[0], w[1]), m)
    # which unipotent characters are Psi-eigencharacters?
    def eigen(w):
        N = order(w); pw = ((w[0] + w[1]) % m, w[0] % m)
        for uu in range(N):
            if (uu * w[0] - pw[0]) % m == 0 and (uu * w[1] - pw[1]) % m == 0:
                return uu
        return None
    eig_u = sum(1 for w in unip if eigen(w) is not None)
    byord = collections.Counter(order(w) for w in unip)
    print(f"Y_{n}: {d1 * d2} characters; (unipotent, det = 1, identity, trivial) -> count: {dict(sorted(cls.items()))}", flush=True)
    print(f"  non-trivial unipotent characters: {len(unip)}, of which Psi-eigencharacters {eig_u}; by order {dict(sorted(byord.items()))}  ({time.time() - t0:.0f} s)", flush=True)
    return dict(n=n, cls={str(k): v for k, v in cls.items()}, unip=len(unip), eig_u=eig_u, byord=dict(byord))

if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]] or (5, 9, 10, 12, 15, 20):
        level(n)
