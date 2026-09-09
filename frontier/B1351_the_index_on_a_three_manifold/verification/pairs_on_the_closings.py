#!/usr/bin/env python3
"""B1351 -- the check behind the closed-manifold half of the statement: on every closing Y_n the Wilson-line spectrum pairs
weight with mirror weight, h^1(Y_n; psi) = h^1(Y_n; psi-bar) for EVERY character psi (Poincare duality on a closed 3-manifold with
h^0 = h^3 = 0 for a non-trivial character), so any abelian Wilson-line vacuum on the tower is vector-like -- exactly, not by
inspection.  Verified with the 2x2 criterion at every character of every level n <= NMAX modulo two primes."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'B1303_the_two_by_two_criterion', 'verification'))
from sympy import isprime, primitive_root, Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ

def h1(p, q0, m, qs, zs):
    """h^1(Y_n; psi) for psi(a) = z^p, psi(b) = z^q0 by the criterion product P = A(x_{n-1}) ... A(x_0), P = I iff h^1 = 1."""
    vals = []
    for q, z in zip(qs, zs):
        x, y = pow(z, p, q), pow(z, q0, q)
        P = [[1, 0], [0, 1]]
        # x_k = psi(a)^{F_{2k+1}} psi(b)^{F_{2k}}; iterate via the deck: (psi(a), psi(b)) -> (psi(a)^2 psi(b), psi(a) psi(b))
        xa, xb = x, y
        for k in range(NN):
            A = [[(1 + xa) % q, xa * xa % q], [1, xa]]
            P = [[(A[0][0]*P[0][0] + A[0][1]*P[1][0]) % q, (A[0][0]*P[0][1] + A[0][1]*P[1][1]) % q],
                 [(A[1][0]*P[0][0] + A[1][1]*P[1][0]) % q, (A[1][0]*P[0][1] + A[1][1]*P[1][1]) % q]]
            xa, xb = xa * xa * xb % q, xa * xb % q
        vals.append(1 if P == [[1, 0], [0, 1]] else 0)
    assert vals[0] == vals[1]
    return vals[0]

def level(n):
    global NN
    NN = n
    M = Matrix([[2, 1], [1, 1]]); K = M ** n - Matrix.eye(2)
    S = smith_normal_form(K, domain=ZZ); m = max(abs(int(S[i, i])) for i in range(2))
    qs = []; qq = m * (10 ** 9 // m) + 1
    while len(qs) < 2:
        if isprime(qq) and (qq - 1) % m == 0: qs.append(qq)
        qq += m
    zs = [pow(primitive_root(q), (q - 1) // m, q) for q in qs]
    total = carry = paired = 0
    for p in range(m):
        for q0 in range(m):
            if (p, q0) == (0, 0) or any((int(K[0, j]) * p + int(K[1, j]) * q0) % m for j in range(2)): continue
            total += 1
            a = h1(p, q0, m, qs, zs); b = h1((-p) % m, (-q0) % m, m, qs, zs)
            carry += a; paired += (a == b)
    return total, carry, paired

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    ok = True
    for n in range(2, NMAX + 1):
        total, carry, paired = level(n)
        print(f"n = {n:2d}: {total:6d} characters, {carry:5d} carry a class, h1(psi) == h1(psi-bar) for {paired}/{total}: {'all paired' if paired == total else 'UNPAIRED'}")
        ok &= (paired == total)
    print("SELFTEST:", "PASS" if ok else "FAIL")
