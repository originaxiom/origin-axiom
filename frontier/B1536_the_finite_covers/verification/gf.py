#!/usr/bin/env python3
"""B1536 -- reduction of sm:B1530's exact field K = Q(zeta_24) to GF(p), with every root of unity of order dividing N.
Shared by both routes (it is the input data: the holonomy and the characters mod p).  Nothing is computed on import.

p = 1 mod N with 24 | N.  z is a primitive N-th root of unity mod p; zeta_24 -> z^(N/24) is checked to be a root of the 24th
cyclotomic polynomial x^8 - x^4 + 1, so the reduction K -> GF(p) is a ring map (K = Z[zeta_24] localised)."""
from fractions import Fraction
from math import gcd


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_1_mod(N, below, count, skip=0):
    """the largest primes p < below with p = 1 mod N (the first `skip` of them passed over)"""
    out, k = [], (below - 2) // N
    while len(out) < count + skip and k > 0:
        p = k * N + 1
        if p < below and is_prime(p):
            out.append(p)
        k -= 1
    return out[skip:]


def lcm(*xs):
    out = 1
    for x in xs:
        out = out * x // gcd(out, x)
    return out


class GF:
    def __init__(self, p, N):
        assert N % 24 == 0 and (p - 1) % N == 0 and is_prime(p), (p, N)
        self.p, self.N = p, N
        # a primitive N-th root: g^((p-1)/N) with order exactly N
        primes_N = [q for q in range(2, N + 1) if N % q == 0 and is_prime(q)]
        a = 2
        while True:
            z = pow(a, (p - 1) // N, p)
            if all(pow(z, N // q, p) != 1 for q in primes_N):
                break
            a += 1
        self.z = z
        self.zpow = [1] * N
        for k in range(1, N):
            self.zpow[k] = self.zpow[k - 1] * z % p
        s = N // 24
        z24 = self.zpow[s]
        assert (pow(z24, 8, p) - pow(z24, 4, p) + 1) % p == 0, "zeta_24 is not a root of x^8 - x^4 + 1"
        self.z24 = [self.zpow[(s * k) % N] for k in range(24)]

    def K(self, x):
        """an exact_lib K element (integer coefficients c_0..c_7 on 1, zeta_24, ..., zeta_24^7 over a denominator d)"""
        p = self.p
        num = sum(int(c) * self.z24[k] for k, c in enumerate(x.c)) % p
        return num * pow(int(x.d) % p, -1, p) % p

    def root(self, fr):
        """e^(2 pi i fr) for a rational fr whose denominator divides N"""
        fr = Fraction(fr) % 1
        assert self.N % fr.denominator == 0, (fr, self.N)
        return self.zpow[fr.numerator * (self.N // fr.denominator) % self.N]

    def inv(self, x):
        return pow(int(x) % self.p, -1, self.p)
