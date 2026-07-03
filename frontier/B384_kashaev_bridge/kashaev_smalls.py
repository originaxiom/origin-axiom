"""B384 T1 -- Kashaev <4_1>_N: exact Galois components + scaling gate + arithmetic bets.

The sum S_N = sum_k prod_{j<=k}(2 - q^j - q^-j) lives in Q(zeta_N)^+ (NOT rational in
general -- first finding: S_5 = 46 + 2 sqrt5). Extract exactly, by integer trace
arithmetic on the Z[x]/(x^N-1) representative:
  rational part r = Tr(S)/phi(N);  sqrt5 part (for 5|N) c = Tr(S*sqrt5)/(5 phi(N)),
with sqrt5 = zeta5 - zeta5^2 - zeta5^3 + zeta5^4 embedded via zeta5 = zeta_N^{N/5}."""
import json, os
from math import gcd

def phi(n):
    r, m, d = n, n, 2
    while d*d <= m:
        if m % d == 0:
            r -= r//d
            while m % d == 0: m //= d
        d += 1
    if m > 1: r -= r//m
    return r
def mu(n):
    r, m, d = 1, n, 2
    while d*d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0: return 0
            r = -r
        d += 1
    if m > 1: r = -r
    return r

def kashaev_vec(N):
    def mul(a, b):
        out = [0]*N
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y: out[(i+j) % N] += x*y
        return out
    total = [0]*N; prod = [0]*N; prod[0] = 1
    total[0] += 1
    for j in range(1, N):
        f = [0]*N; f[0] = 2; f[j % N] -= 1; f[(-j) % N] -= 1
        prod = mul(prod, f)
        total = [t+p for t, p in zip(total, prod)]
    return total

def tr_of(vec, N, ph):
    """Tr_{Q(zeta_N)/Q} of the element (exact, Ramanujan sums)."""
    s = 0
    for i, ci in enumerate(vec):
        if ci:
            g = gcd(i, N)
            s += ci * mu(N//g) * (ph // phi(N//g))
    return s

def components(N):
    ph = phi(N)
    v = kashaev_vec(N)
    from fractions import Fraction as Fr
    rat = Fr(tr_of(v, N, ph), ph)
    c5 = None
    if N % 5 == 0:
        m = N // 5
        s5 = [0]*N
        for a, sgn in ((1, 1), (2, -1), (3, -1), (4, 1)):
            s5[(a*m) % N] += sgn
        # v * sqrt5
        w = [0]*N
        for i, x in enumerate(v):
            if x:
                for j, y in enumerate(s5):
                    if y: w[(i+j) % N] += x*y
        from fractions import Fraction as Fr
        c5 = Fr(tr_of(w, N, ph), 5*ph)
    return rat, c5

import math
res = {}
for N in (5, 7, 9, 15, 25, 27, 45, 81, 135):
    rat, c5 = components(N)
    # numeric total for the scaling gate
    val = None
    try:
        import mpmath as mp
        mp.mp.dps = 30
        q = mp.e**(2j*mp.pi/N)
        tot = mp.mpf(1); prod = mp.mpf(1)
        for j in range(1, N):
            prod *= abs(1-q**j)**2
            tot += prod
        val = float(tot)
    except Exception:
        pass
    grow = 2*math.pi*math.log(val)/N if val else None
    res[str(N)] = dict(rational_part=str(rat), sqrt5_part=(str(c5) if c5 is not None else None),
                       numeric=val, growth=grow)
    print(f"N={N:4d}: rat={rat}  sqrt5={c5}  numeric={val:.6g}  2pi.log/N={grow:.4f}")
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "kashaev.json"), "w"), indent=1)
print("DONE")
