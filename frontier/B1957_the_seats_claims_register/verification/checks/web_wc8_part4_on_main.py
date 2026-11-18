"""B1957: the web seat's W-C8 part 4, its three checks, on main.  Data-free; exact integers.
 S1  for a hyperbolic act of trace t and determinant 1, the eigenvalue field Q(sqrt(t^2 - 4)) equals Q(sqrt(N)),
     N = det(A + 1) = t + 2, exactly when t - 2 is a square: every t from 3 to 20,000; the control with t + 2.
 S2  A_m = [[m^2 + 1, m], [m, 1]]: the Smith form of A_m - 1 is diag(m, m), m = 1 to 200 (so |det| = m^2).
 S3  -1 is a square mod N = m^2 + 4 exactly for odd m, m = 1 to 200.
 S4  the note's example: [[5, 4], [1, 1]] = L^4 R has trace 6 = 2^2 + 2 and is not conjugate in GL(2, Z) to A_2 = L^2 R^2
     (their cyclic words differ under rotation, exchange and reversal)."""
from math import isqrt, gcd
def sqfree(n):
    n = abs(n); s = 1; p = 2
    while p * p <= n:
        k = 0
        while n % p == 0: n //= p; k += 1
        if k % 2: s *= p
        p += 1
    return s * n
issq = lambda n: n >= 0 and isqrt(n) ** 2 == n
if __name__ == "__main__":
    bad = [t for t in range(3, 20001) if (sqfree(t * t - 4) == sqfree(t + 2)) != issq(t - 2)]; ctrl = [t for t in range(3, 20001) if (sqfree(t * t - 4) == sqfree(t + 2)) != issq(t + 2)]
    print("S1: t = 3 to 20,000: the two fields agree exactly when t - 2 is a square: %s (exceptions %d; the metallic traces among them: %d); the control with t + 2 fails first at t = %d" % (not bad, len(bad), sum(issq(t - 2) for t in range(3, 20001)), ctrl[0]))
    print("S2: m = 1 to 200: A_m - 1 = [[m^2, m], [m, 0]] has gcd of entries m and determinant -m^2, so Smith form diag(m, m): %s" % all(gcd(gcd(m * m, m), m) == m and (m * m * 0 - m * m) == -m * m for m in range(1, 201)))
    print("S3: m = 1 to 200: -1 is a square mod m^2 + 4 exactly for odd m: %s" % all((any((x * x + 1) % (m * m + 4) == 0 for x in range(m * m + 4))) == (m % 2 == 1) for m in range(1, 201)))
    rot = lambda w: {w[i:] + w[:i] for i in range(len(w))}; sw = lambda w: w.translate(str.maketrans("LR", "RL")); cls = lambda w: rot(w) | rot(sw(w)) | rot(w[::-1]) | rot(sw(w[::-1]))
    print("S4: L^4 R = [[5, 4], [1, 1]] (trace 6) and L^2 R^2 = [[5, 2], [2, 1]] (trace 6): the same class of cyclic words under rotation, exchange and reversal: %s" % ("LLLLR" in cls("LLRR")))
