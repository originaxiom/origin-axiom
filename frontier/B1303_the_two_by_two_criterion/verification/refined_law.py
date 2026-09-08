#!/usr/bin/env python3
"""The refined law on Y_15 (and any n): H_1(Y_n) = Z[phi]/(L_n) (n odd) or Z[phi]/(sqrt5 F_n) (n even); the deck t acts
as phi^2 and Psi = [[1,1],[1,0]] (Phi = Psi^2) acts as phi.  Test: an odd-order character is in the 2x2-criterion support
iff it is a Psi-eigencharacter (eigenvalue u, a root of x^2 - x - 1 mod its order N) with u^2 of order >= 3 at every
prime of N and u^n = +-1 mod N (a global sign)."""
import sys, math, collections, time
import numpy as np
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
import criterion as F
import sympy as sp

def test(n):
    X, Y, m, tors = F.characters(n)
    seq = F.x_sequence(X, Y, n, m)
    qs = F.primes_1_mod(m)
    ident = F.product_is_identity(seq, m, qs[0]) & F.product_is_identity(seq, m, qs[1])
    order = np.array([m // math.gcd(math.gcd(int(x), int(y)), m) for x, y in zip(X, Y)])
    # Psi-eigen: psi o Psi = psi^u, (x, y) -> Psi^T (x, y) = (x + y, x)
    pX, pY = (X + Y) % m, X % m
    odd = (order % 2 == 1) & (order > 1)
    tab = collections.Counter()
    for i in np.where(odd)[0]:
        N = int(order[i]); x, y = int(X[i]), int(Y[i])
        u = None
        for cand in range(N):
            if (cand * x - pX[i]) % m == 0 and (cand * y - pY[i]) % m == 0:
                u = cand; break
        if u is None:
            tab[('not-eigen', bool(ident[i]))] += 1; continue
        lam = u * u % N
        # order of lam at every prime of N
        ok2 = True
        for p in sp.factorint(N):
            o = 1; v = lam % p
            while v != 1:
                v = v * lam % p; o += 1
            if o < 3:
                ok2 = False
        sign = pow(u, n, N)
        glob = sign in (1, N - 1)
        tab[('eigen', 'lam_ord>=3' if ok2 else 'lam_ord<3', 'u^n=+-1' if glob else 'u^n mixed', bool(ident[i]))] += 1
    print(f"Y_{n}: odd-order characters by (eigen?, lambda-order condition, global-sign condition, h^1=1?) -> count:")
    for k, v in sorted(tab.items(), key=str):
        print(f"    {k}: {v}")
    return tab

if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]] or (10, 15):
        test(n)
