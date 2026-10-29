"""Which cyclic isogenies of the fibre extend over the figure-eight complement (data-free; exact integer arithmetic).
A cyclic degree-k isogeny of the fibre torus is an index-k sublattice L of Z^2 with Z^2/L cyclic, i.e. a point of the
projective line P^1(Z/k) (a vector v of order k in (Z/k)^2, up to units).  It extends over the mapping torus of the
monodromy M (LR or its conjugate RL) exactly when M fixes that point: M v = lam v for a unit lam mod k.  This counts the
fixed points of M on P^1(Z/k) for k = 2..60, and compares the primes with the splitting of x^2 - 3x + 1 (M's
characteristic polynomial; discriminant 5) mod p: split (p = +-1 mod 5), ramified (p = 5) or inert (p = +-2 mod 5).
No measured number is read.   python3 -B isogeny_lemma.py > isogeny_lemma_out.txt"""
from math import gcd
from itertools import product

L, R = ((1, 0), (1, 1)), ((1, 1), (0, 1))
def mul(A, B): return tuple(tuple(sum(A[i][t] * B[t][j] for t in range(2)) for j in range(2)) for i in range(2))
LR, RL = mul(L, R), mul(R, L)

def points(k):
    """representatives of P^1(Z/k): vectors of order k (gcd(a, b, k) = 1) up to units"""
    seen, reps = set(), []
    units = [u for u in range(1, k) if gcd(u, k) == 1] if k > 1 else [0]
    for a, b in product(range(k), repeat=2):
        if gcd(gcd(a, b), k) != 1 or (a, b) in seen: continue
        orbit = {((u * a) % k, (u * b) % k) for u in units}
        seen |= orbit; reps.append((a, b))
    return reps, units

def fixed(M, k):
    reps, units = points(k); out = []
    for a, b in reps:
        w = ((M[0][0] * a + M[0][1] * b) % k, (M[1][0] * a + M[1][1] * b) % k)
        if any(((u * a) % k, (u * b) % k) == w for u in units): out.append((a, b))
    return len(reps), out

def kind(p):
    roots = [x for x in range(p) if (x * x - 3 * x + 1) % p == 0]
    return "ramified" if p == 5 else ("split" if len(roots) == 2 else ("inert" if not roots else "double root"))

def primes(n): return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]

print("M = LR =", LR, " RL =", RL, " trace", LR[0][0] + LR[1][1], " det", LR[0][0] * LR[1][1] - LR[0][1] * LR[1][0])
print("\nprimes <= 60: x^2 - 3x + 1 mod p, and fixed points of LR on P^1(F_p)")
for p in primes(60):
    n, fx = fixed(LR, p)
    print("  p = %2d (%s mod 5 = %d): %-8s  |P^1| = %2d  fixed: %d" % (p, "", p % 5, kind(p), n, len(fx)))
print("\nk = 2..60: the number of LR-invariant cyclic isogenies of degree k (RL gives the same: %s)" %
      all(len(fixed(LR, k)[1]) == len(fixed(RL, k)[1]) for k in range(2, 61)))
for k in range(2, 61):
    n, fx = fixed(LR, k)
    if fx: print("  k = %2d: %d of %d  %s" % (k, len(fx), n, fx[:4]))
print("\ndegrees k <= 60 with none:", [k for k in range(2, 61) if not fixed(LR, k)[1]])
