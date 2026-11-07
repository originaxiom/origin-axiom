"""POST HOC (written after conservation_out.txt was read; disclosed as such; changes no verdict): at which finite rungs
N = 2..5 does the object's dynamics LR have an invariant line, i.e. a fixed point on P^1(Z/N)? Also its characteristic
polynomial x^2 - 3x + 1 mod N and its roots. Pure arithmetic.
    python3 post_hoc_invariant_lines.py"""
from math import gcd

LR = ((2, 1), (1, 1))


def p1(n):
    pts = set()
    for a in range(n):
        for b in range(n):
            if gcd(gcd(a, b), n) == 1:
                # normalise the projective point (a : b) by the units of Z/n
                pts.add(min(((u * a) % n, (u * b) % n) for u in range(1, n) if gcd(u, n) == 1))
    return sorted(pts)


def act(M, v, n):  # column vector
    return ((M[0][0] * v[0] + M[0][1] * v[1]) % n, (M[1][0] * v[0] + M[1][1] * v[1]) % n)


for n in (2, 3, 4, 5):
    P = p1(n)
    fixed = []
    for v in P:
        w = act(LR, v, n)
        if any(((u * v[0]) % n, (u * v[1]) % n) == w for u in range(1, n) if gcd(u, n) == 1):
            fixed.append(v)
    roots = [x for x in range(n) if (x * x - 3 * x + 1) % n == 0]
    print("N = %d: |P^1(Z/%d)| = %d; lines fixed by LR: %s; roots of x^2 - 3x + 1 mod %d: %s" % (n, n, len(P), fixed, n, roots))
print("post_hoc_invariant_lines exit 0")
