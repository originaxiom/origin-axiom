#!/usr/bin/env python3
"""THE LAW IN CONDUCTOR FORM (B1304 addendum).  For a character psi of H_1(Y_n) let d(psi) = the smallest d | n with
psi Phi^d-invariant (its conductor: psi is pulled back from Y_d and from no smaller level).  By Lemma 1 (pullback
exactness) h^1(Y_n; psi) = h^1(Y_d; psi), so the law needs only the NEW characters of each level, and for those:

    h^1 = 1  iff  d is odd, psi is a Psi-eigencharacter, its order is prime to 5, and u^d = +-1 modulo the order
    (a global sign; u the Psi-eigenvalue).  New characters at even levels never carry a class.

Every odd-order Psi-eigencharacter of every level 2..30 is constructed (eigen_census's construction), its conductor and
the sign of u^d computed, and the criterion applied; the table (d parity, ramified?, global sign of u^d, h^1) must have
h^1 = 1 exactly on the rows (odd, unramified, +-).  Y_30's 1 200 mixed 11.31 characters of conductor 15 are the case
the n-sign form of B1303 could not separate (600 at h^1 = 1, 600 at 0, by the sign of u^15)."""
import sys, math, itertools, collections, time, pathlib
import numpy as np
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'B1303_the_two_by_two_criterion' / 'verification'))
import criterion_at_scale as S
import eigen_census as EC

PHI = sp.Matrix([[2, 1], [1, 1]])

_POW = {}
def conductor(w, m, n):
    if (m, n) not in _POW:
        _POW[(m, n)] = [(d, [[int(x) % m for x in row] for row in (PHI ** d).tolist()]) for d in sorted(sp.divisors(n))]
    for d, M in _POW[(m, n)]:
        if ((M[0][0] * w[0] + M[1][0] * w[1] - w[0]) % m == 0) and ((M[0][1] * w[0] + M[1][1] * w[1] - w[1]) % m == 0):
            return d
    raise AssertionError

def level(n):
    t0 = time.time()
    d1, d2, m, U = S.smith(n)
    fib = S.fib_pairs(n, m); qs = S.primes_1_mod(m)
    fac = sp.factorint(m); odd_primes = [p for p in fac if p != 2]
    order = lambda w: m // math.gcd(math.gcd(w[0], w[1]), m)
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
            # brute force over the p-primary subgroup
            out = []
            for i in range(p ** k1):
                for j in range(p ** k2):
                    c1 = i * (d1 // p ** k1) if k1 else 0; c2 = j * (d2 // p ** k2) if k2 else 0
                    e1 = (c1 * (m // d1)) % m; e2 = (c2 * (m // d2)) % m
                    w = ((U[0][0] * e1 + U[1][0] * e2) % m, (U[0][1] * e1 + U[1][1] * e2) % m)
                    if w != (0, 0):
                        u = eigen(w)
                        if u is not None:
                            out.append((w, u))
            per_prime[p] = out
        else:
            roots = [u for u in range(p) if (u * u - u - 1) % p == 0]
            out = []
            for u in roots:
                for c in range(1, p):
                    out.append(((((u * c) % p) * (m // p)) % m, (c * (m // p)) % m))
            per_prime[p] = [(w, eigen(w)) for w in out]
    chars = []
    from sympy.ntheory.modular import crt
    for r in range(1, len(odd_primes) + 1):
        for ps in itertools.combinations(odd_primes, r):
            for combo in itertools.product(*[per_prime[p] for p in ps]):
                w = (sum(c[0][0] for c in combo) % m, sum(c[0][1] for c in combo) % m)
                # the Psi-eigenvalue of the product by CRT from the per-prime eigenvalues (each defined modulo its part's order)
                mods = [order(c[0]) for c in combo]; res = [c[1] for c in combo]
                uN = int(crt(mods, res)[0]) if len(combo) > 1 else res[0]
                chars.append((w, ps, uN))
    if not chars:
        print(f"Y_{n}: no odd eigencharacters", flush=True); return collections.Counter()
    W1 = np.array([c[0][0] for c in chars], dtype=np.int64); W2 = np.array([c[0][1] for c in chars], dtype=np.int64)
    ok = S.identity_test(W1, W2, n, m, qs[0], fib) & S.identity_test(W1, W2, n, m, qs[1], fib)
    tab = collections.Counter()
    for (w, ps, u), h in zip(chars, ok.tolist()):
        N = order(w); d = conductor(w, m, n)
        unram = 5 not in ps
        s = pow(u, d, N)
        gs = '+' if s == 1 else ('-' if s == N - 1 else 'mixed')
        tab[(d % 2, 'unramified' if unram else 'ramified', gs, int(h))] += 1
    print(f"Y_{n}: {len(chars)} odd eigencharacters (primes {odd_primes}); (conductor parity, ramified?, sign of u^d, h^1) -> count: {dict(sorted(tab.items(), key=str))}  ({time.time() - t0:.0f} s)", flush=True)
    return tab

def law(key):
    par, ram, gs, h = key
    return h == int(par == 1 and ram == 'unramified' and gs in ('+', '-'))

if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or list(range(2, 31))
    ok = True
    for n in ns:
        tab = level(n)
        ok &= all(law(k) for k in tab)
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
