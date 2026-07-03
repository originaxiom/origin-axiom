"""B394 -- identify the three 405-single values exactly in Q(zeta9)+ = <1, c1, c2>."""
import json, os
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "singles_405.json")))

import sys
sys.path.insert(0, os.path.join(HERE, "..", "B391_existence_general"))
from census_big import primitive_root

def crt_pair(v1, p1, v2, p2):
    M = p1 * p2
    m1 = p2 * pow(p2, -1, p1) % M
    m2 = p1 * pow(p1, -1, p2) % M
    return (v1 * m1 + v2 * m2) % M, M

def ratrec(r, M):
    a, b = M, r
    x0, x1 = 0, 1
    import math
    bound = math.isqrt(M // 2)
    while b > bound:
        q = a // b
        a, b = b, a - q*b
        x0, x1 = x1, x0 - q*x1
    den = abs(x1)
    num = b if x1 > 0 else -b
    if den == 0 or math.gcd(den, M) != 1: return None
    return Fr(num, den)

primes = sorted(map(int, R))
p1, p2 = primes
def cvals(p):
    g = primitive_root(p)
    z9 = pow(g, (p-1)//9, p)
    return ((z9 + pow(z9, 8, p)) % p, (pow(z9, 2, p) + pow(z9, 7, p)) % p)

c1p, c2p = cvals(p1), cvals(p2)
# per residue class mod 135 solve v = x + y c1 + z c2 with a SECOND relation: the three
# classes should be the Galois orbit; simplest: solve x,y,z from the three class-values
# per prime (Galois-conjugate system: v_k = x + y*sigma^k(c1) + z*sigma^k(c2)) --
# sigma: c1 -> c2 -> c4 = -c1-c2.
out = {}
for cls_idx, base in enumerate((31, 121, 76)):
    vs = {p: int(R[str(p)][str(base)].split("(")[1].rstrip(")")) for p in primes}
    out[str(base)] = vs
# solve per prime the 3x3: rows = the three classes as Galois conjugates
def solve3(p, c1, c2):
    c4 = (-c1 - c2) % p
    rows = [(1, c1, c2), (1, c2, c4), (1, c4, c1)]
    v = [out[str(b)][p] for b in (31, 121, 76)]
    # Gaussian elim mod p
    A = [list(r) + [vv] for r, vv in zip(rows, v)]
    n = 3
    for c in range(n):
        piv = next(i for i in range(c, n) if A[i][c] % p)
        A[c], A[piv] = A[piv], A[c]
        inv = pow(A[c][c], p-2, p)
        A[c] = [x * inv % p for x in A[c]]
        for i in range(n):
            if i != c and A[i][c]:
                f = A[i][c]
                A[i] = [(x - f*y) % p for x, y in zip(A[i], A[c])]
    return [A[i][3] for i in range(3)]

s1 = solve3(p1, *c1p)
s2 = solve3(p2, *c2p)
coeffs = []
for i in range(3):
    r, M = crt_pair(s1[i], p1, s2[i], p2)
    coeffs.append(ratrec(r, M))
print("triple = x + y*c1 + z*c2 with (x,y,z) =", [str(c) for c in coeffs])
json.dump(dict(xyz=[str(c) for c in coeffs]),
          open(os.path.join(HERE, "triple.json"), "w"), indent=1)
print("DONE")
