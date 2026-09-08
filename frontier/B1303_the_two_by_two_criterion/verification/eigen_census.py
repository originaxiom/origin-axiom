#!/usr/bin/env python3
"""The odd-order eigencharacters of every level, constructed directly, and the criterion on each of them: for every odd
prime power q | exponent, the q-primary subgroup of the character group is searched for the eigenlines of the half-deck
Psi (Psi^T w = u w), the eigencharacters of composite odd order are the products, and for each the criterion decides h^1.
Tabulated by (n parity, the signs of u^n at each prime, whether the character is new at this level).  This is where the
law is read off: h^1 = 1 iff eigen, unramified (5 excluded), and Psi^n psi in {psi, psi^-1} with Psi^n psi = psi when n is
even."""
import sys, math, itertools, collections, time, pathlib
import numpy as np
import sympy as sp
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import criterion_at_scale as S

def level(n):
    t0 = time.time()
    d1, d2, m, U = S.smith(n)
    fib = S.fib_pairs(n, m); qs = S.primes_1_mod(m)
    # the odd part of the character group: coordinates (c1, c2) with odd order
    fac = sp.factorint(m)
    odd_primes = [p for p in fac if p != 2]
    # q-primary eigencharacters: enumerate the q-primary subgroup (c1 in multiples of d1/q^k1, c2 of d2/q^k2)
    def primary(p):
        k1 = 0
        while d1 % p ** (k1 + 1) == 0: k1 += 1
        k2 = 0
        while d2 % p ** (k2 + 1) == 0: k2 += 1
        out = []
        for i in range(p ** k1):
            for j in range(p ** k2):
                c1 = i * (d1 // p ** k1) if k1 else 0; c2 = j * (d2 // p ** k2) if k2 else 0
                e1 = (c1 * (m // d1)) % m; e2 = (c2 * (m // d2)) % m
                w = ((U[0][0] * e1 + U[1][0] * e2) % m, (U[0][1] * e1 + U[1][1] * e2) % m)
                if w != (0, 0):
                    out.append(w)
        return out
    def order(w): return m // math.gcd(math.gcd(w[0], w[1]), m)
    def eigen(w):
        N = order(w); pw = ((w[0] + w[1]) % m, w[0] % m)
        for u in range(N):
            if (u * w[0] - pw[0]) % m == 0 and (u * w[1] - pw[1]) % m == 0:
                return u
        return None
    per_prime = {}
    for p in odd_primes:
        k1 = 0
        while d1 % p ** (k1 + 1) == 0: k1 += 1
        k2 = 0
        while d2 % p ** (k2 + 1) == 0: k2 += 1
        if p ** (k1 + k2) <= 200000:
            eig = [(w, eigen(w)) for w in primary(p)]
            eig = [(w, u) for w, u in eig if u is not None]
        else:
            # a large squarefree p-part (Z/p)^2: the eigenlines are {(u c, c)} for the roots u of x^2 - x - 1 mod p,
            # scaled into (Z/m)^2 by m/p (Psi^T (u c, c) = (u c + c, u c) = u (u c, c) since u^2 = u + 1)
            assert k1 + k2 == 2 and k1 <= 1 and k2 <= 1, (p, k1, k2)
            roots = [u for u in range(p) if (u * u - u - 1) % p == 0]
            assert len(roots) == 2, p
            eig = []
            for u in roots:
                for c in range(1, p):
                    w = (((u * c) % p) * (m // p) % m, (c * (m // p)) % m)
                    assert ((w[0] + w[1]) % m, w[0] % m) == ((u * w[0]) % m, (u * w[1]) % m)
                    eig.append((w, u))
        per_prime[p] = eig
    # all products over subsets of primes (one eigencharacter per chosen prime)
    chars = []
    for r in range(1, len(odd_primes) + 1):
        for ps in itertools.combinations(odd_primes, r):
            for combo in itertools.product(*[per_prime[p] for p in ps]):
                w = (sum(c[0][0] for c in combo) % m, sum(c[0][1] for c in combo) % m)
                chars.append((w, ps, tuple(c[1] for c in combo)))
    if not chars:
        print(f"Y_{n}: no odd-order eigencharacters", flush=True); return {}
    W1 = np.array([c[0][0] for c in chars], dtype=np.int64); W2 = np.array([c[0][1] for c in chars], dtype=np.int64)
    ok = S.identity_test(W1, W2, n, m, qs[0], fib) & S.identity_test(W1, W2, n, m, qs[1], fib)
    tab = collections.Counter()
    for (w, ps, us), h in zip(chars, ok.tolist()):
        N = order(w)
        # per-prime data: ramified (5), the sign of u^n mod p, the order of u^2 mod p
        signs = []
        unram = True
        for p, u in zip(ps, us):
            if p == 5:
                unram = False
            s = pow(u, n, p)
            signs.append('+' if s == 1 else ('-' if s == p - 1 else '?'))
        glob = pow(us[0], n, N) if len(ps) == 1 else None
        # the global sign of u^n modulo N for the product character: u_N = CRT(us)
        uN = int(sp.ntheory.modular.crt([p ** 1 for p in ps], list(us))[0]) if len(ps) > 1 else us[0]
        # (the primary parts here are of order p^k; use the order N itself for the global test)
        gN = pow(uN, n, N) if all(N % p == 0 for p in ps) else None
        gsign = '+' if gN == 1 else ('-' if gN == N - 1 else 'mixed')
        tab[(n % 2, 'unramified' if unram else 'ramified', ''.join(signs), gsign, int(h))] += 1
    print(f"Y_{n}: odd eigencharacters {len(chars)} (primes {odd_primes}); (n parity, ramified?, signs of u^n per prime, global sign, h^1) -> count:", flush=True)
    for k, v in sorted(tab.items(), key=str):
        print(f"    {k}: {v}", flush=True)
    print(f"  ({time.time() - t0:.0f} s)", flush=True)
    return tab

if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]] or range(2, 22):
        level(n)
