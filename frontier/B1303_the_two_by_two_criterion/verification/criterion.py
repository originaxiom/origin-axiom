#!/usr/bin/env python3
"""A 2x2 criterion for h^1(Y_n; psi): if pi_1(Y_n) = <a, b | phi^n(a) = a, phi^n(b) = b> (the fixed quotient of the
monodromy phi: a -> a^2 b, b -> a b of the figure-eight's fibre), then for a non-trivial character psi of H_1(Y_n)
h^1 = 1 - rank(J), J = M_{phi^n}(psi) - I, and by the chain rule M_{phi^n}(psi) = M_phi(psi o Phi^{n-1}) ... M_phi(psi),
M_phi(chi) = [[1 + chi(a), chi(a)^2], [1, chi(a)]].  So h^1 = 1 iff the product of the 2x2 matrices A(x_k),
x_k = (psi o Phi^k)(a), equals the identity.  Computed exactly modulo two primes q = 1 mod m.  Compared level by level
with B1301's support files (counts, orders, deck-eigen structure)."""
import sys, math, json, collections, pathlib, time
import numpy as np
import sympy as sp

Phi = np.array([[2, 1], [1, 1]], dtype=object)      # abelianised monodromy; Delta = det(t - Phi) = t^2 - 3t + 1

def characters(n):
    """characters of coker(Phi^n - I): (x, y) in (Z/m)^2 (exponents of zeta_m) with (Phi^n - I)^T (x, y) = 0 mod m."""
    M = np.linalg.matrix_power(Phi, n) - np.eye(2, dtype=object)
    Mi = sp.Matrix([[int(M[i, j]) for j in range(2)] for i in range(2)])
    from sympy.matrices.normalforms import smith_normal_form
    D = smith_normal_form(Mi, domain=sp.ZZ)
    d1, d2 = abs(int(D[0, 0])), abs(int(D[1, 1]))
    m = d1 * d2 // math.gcd(d1, d2)
    # characters psi of Z^2 trivial on the image of (Phi^n - I): psi(v) = zeta_m^(x v1 + y v2); need x*M[.,0]+... hmm:
    # psi trivial on columns of M: for each column c: x c0 + y c1 = 0 mod m
    X, Y = np.meshgrid(np.arange(m), np.arange(m), indexing='ij')
    X, Y = X.ravel(), Y.ravel()
    ok = np.ones(len(X), dtype=bool)
    for j in range(2):
        c0, c1 = int(M[0, j]), int(M[1, j])
        ok &= ((c0 * X + c1 * Y) % m == 0)
    return X[ok], Y[ok], m, (d1, d2)

def x_sequence(X, Y, n, m):
    """x_k = (psi o Phi^k)(a) as exponents mod m: Phi^k e1 = (p, q) -> x p + y q."""
    seq = []
    P = np.eye(2, dtype=object)
    for k in range(n):
        p, q = int(P[0, 0]), int(P[1, 0])
        seq.append((X * (p % m) + Y * (q % m)) % m)
        P = P.dot(Phi)
    return seq

def primes_1_mod(m, count=2, start=10 ** 9):
    out = []; q = start - (start % m) + 1
    while len(out) < count:
        if sp.isprime(q):
            out.append(q)
        q += m
    return out

def product_is_identity(seq, m, q):
    """the product A(x_{n-1}) ... A(x_0) modulo the prime q (zeta_m -> g^((q-1)/m)); returns a boolean array."""
    g = sp.primitive_root(q); zeta = pow(g, (q - 1) // m, q)
    powz = np.array([pow(zeta, e, q) for e in range(m)], dtype=np.int64)
    N = len(seq[0])
    a = np.ones(N, dtype=np.int64); b = np.zeros(N, dtype=np.int64); c = np.zeros(N, dtype=np.int64); d = np.ones(N, dtype=np.int64)
    for k in range(len(seq)):                      # left-multiply by A(x_k): P <- A(x_k) P, k = 0 first gives A(x_{n-1})...A(x_0)
        x = powz[seq[k]]
        a11 = (1 + x) % q; a12 = (x * x) % q; a21 = np.ones(N, dtype=np.int64); a22 = x
        na = (a11 * a + a12 * c) % q; nb = (a11 * b + a12 * d) % q
        nc = (a21 * a + a22 * c) % q; nd = (a21 * b + a22 * d) % q
        a, b, c, d = na, nb, nc, nd
    return (a == 1) & (b == 0) & (c == 0) & (d == 1)

def deck(X, Y, m):
    """psi -> psi o Phi: (x, y) -> Phi^T (x, y)."""
    return ((2 * X + Y) % m, (X + Y) % m)

def level(n):
    t0 = time.time()
    X, Y, m, tors = characters(n)
    seq = x_sequence(X, Y, n, m)
    qs = primes_1_mod(m)
    ident = product_is_identity(seq, m, qs[0]) & product_is_identity(seq, m, qs[1])
    triv = (X == 0) & (Y == 0)
    pos = ident & ~triv
    order = np.array([m // math.gcd(math.gcd(int(x), int(y)), m) for x, y in zip(X, Y)])
    byord = collections.Counter(order[pos].tolist())
    # deck eigen-structure: psi o Phi = psi^lambda
    dX, dY = deck(X, Y, m)
    eig = collections.Counter()
    idx = {(int(x), int(y)): i for i, (x, y) in enumerate(zip(X, Y))}
    for i in np.where(pos)[0]:
        o = int(order[i]); lam = None
        for l in range(o):
            if (l * X[i] - dX[i]) % m == 0 and (l * Y[i] - dY[i]) % m == 0:
                lam = l; break
        eig[(o, lam)] += 1
    print(f"Y_{n}: H_1 = Z/{tors[0]} + Z/{tors[1]} ({len(X)} characters, exponent {m}); 2x2 criterion: h^1 = 1 on {int(pos.sum())} characters, by order {dict(sorted(byord.items()))}; eigen-structure {dict(sorted(eig.items(), key=str))}  ({time.time() - t0:.1f} s)", flush=True)
    return dict(n=n, count=int(pos.sum()), byord=dict(byord), eig=eig)

if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for n in ns:
        level(n)
