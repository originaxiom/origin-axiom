"""THE ODD-HALF-DECK CRITERION against the whole law (B1304 addendum, the positive half generalised): a character psi of H_1(Y_n) that
some ODD power of the half-deck Psi maps to psi or to psi-bar carries a class (THEOREM, all characters -- the proof of the positive half
verbatim).  Is the converse true, i.e. is the support EXACTLY that set?  Tested on every character of every level n <= NMAX with the 2x2
criterion (two large primes): it is, at every level except the 2-adic conductors 6 and 12, whose exceptional carriers (the 24 characters
of order 8 at Y_6, the 96 of order 16 at Y_12 -- Carmichael's exceptional Fibonacci indices, F_6 = 8, F_12 = 144) are fixed up to
conjugation by NO odd half-deck power and carry all the same.  Usage: python3 odd_half_deck_criterion.py [NMAX]."""
import sys
from sympy import isprime, primitive_root, Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def fox_h1(p, q0, n, m, qs, zs):
    # presentation (i): phi: a -> a^2 b, b -> a b; P = A(x_{n-1}) ... A(x_0), x_k = psi(a)^{F_{2k+1}} psi(b)^{F_{2k}}; h1 = 1 iff P = I
    vals = []
    for q, z in zip(qs, zs):
        xa, xb = pow(z, p, q), pow(z, q0, q)
        # iterate phi on exponents: (ea, eb) exponents of a, b in the abelianisation of phi^k(a): start (1,0); phi: a->2a+b, b->a+b
        ea, eb = 1, 0
        P = [[1, 0], [0, 1]]
        for k in range(n):
            x = pow(xa, ea, q) * pow(xb, eb, q) % q
            A = [[(1 + x) % q, x * x % q], [1, x]]
            P = [[(A[0][0]*P[0][0] + A[0][1]*P[1][0]) % q, (A[0][0]*P[0][1] + A[0][1]*P[1][1]) % q],
                 [(A[1][0]*P[0][0] + A[1][1]*P[1][0]) % q, (A[1][0]*P[0][1] + A[1][1]*P[1][1]) % q]]
            ea, eb = 2 * ea + eb, ea + eb
        vals.append(P == [[1, 0], [0, 1]])
    assert vals[0] == vals[1]
    return vals[0]

def level(n):
    M = Matrix([[2, 1], [1, 1]]); K = M ** n - Matrix.eye(2)
    S = smith_normal_form(K, domain=ZZ); m = max(abs(int(S[i, i])) for i in range(2))
    qs = []; qq = m * (10 ** 9 // m) + 1
    while len(qs) < 2:
        if isprime(qq) and (qq - 1) % m == 0: qs.append(qq)
        qq += m
    zs = [pow(primitive_root(q), (q - 1) // m, q) for q in qs]
    tot = pos = agree = pred = 0; bad = []
    for p in range(m):
        for q0 in range(m):
            if (p, q0) == (0, 0): continue
            if any((int(K[0, j]) * p + int(K[1, j]) * q0) % m for j in range(2)): continue
            tot += 1
            h = fox_h1(p, q0, n, m, qs, zs)
            # the half-deck on characters: (p, q0) -> (p + q0, p)  [psi o Psi (a) = psi(a) psi(b), psi o Psi (b) = psi(a)]
            a, b = p, q0; found = False
            for k in range(1, 2 * n + 1):
                a, b = (a + b) % m, a
                if k % 2 == 1 and ((a, b) == (p, q0) or (a, b) == ((-p) % m, (-q0) % m)):
                    found = True; break
            pos += h; pred += found; agree += (h == found)
            if h != found and len(bad) < 5: bad.append((p, q0, h, found))
    print(f"n = {n:2d}: m = {m:5d}, {tot:6d} characters; carry {pos:5d}; 'odd half-deck power fixes psi up to conjugation' {pred:5d}; agreement {agree == tot} ({agree}/{tot}) {bad}")
    return agree == tot

if __name__ == "__main__":
    ok = True
    for n in range(2, int(sys.argv[1]) + 1 if len(sys.argv) > 1 else 12):
        ok &= level(n)
    print("ALL LEVELS AGREE:", ok)
