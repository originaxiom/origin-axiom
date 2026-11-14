#!/usr/bin/env python3
"""W-C8, part 4: main's tagged speculation (M19) tested, and the golden act's uniqueness among the metallic acts.

Data-free; integers only.

    python3 -I -u wc8_part4_checks.py

DEFINITIONS
  A hyperbolic A in SL2(Z) with trace t >= 3: its eigenvalue field is Q(sqrt(t^2 - 4)); N = det(A + I) = t + 2.
  Two quadratic fields Q(sqrt x), Q(sqrt y) (x, y > 0, not squares) are equal exactly when x y is a square; Q(sqrt N) = Q
  when N is a square. The metallic act A_m = J_m^2 has trace m^2 + 2; J_m = [[m, 1], [1, 0]].

EXPECTATIONS, written before the run (derived by hand by this seat):
  S1  For every t from 3 to 20000: Q(sqrt(t^2 - 4)) = Q(sqrt(t + 2)) exactly when t - 2 is a perfect square.
      (t^2 - 4 = (t - 2)(t + 2), so equality needs t - 2 to be a square class, and for t - 2 = m^2 with m >= 1, t + 2 =
      m^2 + 4 is never a square.) So main's speculation holds for every trace, by this argument.
  S2  For m from 1 to 200: |det(A_m - I)| = m^2 and |det(J_m - I)| = m, so H1 of the metallic root and of its tick bundle
      is torsion-free exactly at m = 1 (SE1 singles out the golden act among the metallic acts).
  S3  For m from 1 to 200: a square root of -1 mod N = m^2 + 4 exists exactly for odd m (for even m, 4 | N).
  Control: S1 with "t + 2 a square" in place of "t - 2 a square" fails for some t.
"""
from math import isqrt


def sqfree(x):
    r, d = 1, 2
    while d * d <= x:
        while x % (d * d) == 0:
            x //= d * d
        if x % d == 0:
            r *= d
            x //= d
        d += 1
    return r * x


def is_sq(x):
    return x >= 0 and isqrt(x) ** 2 == x


s1 = ctrl = True
bad = []
for t in range(3, 20001):
    a, n = t * t - 4, t + 2
    equal = (not is_sq(n)) and sqfree(a) == sqfree(n)
    s1 &= equal == is_sq(t - 2)
    if equal != is_sq(t - 2):
        bad.append(t)
    ctrl &= equal == is_sq(t + 2)
print("S1 for t = 3..20000, field equality exactly when t - 2 is a square:", s1, "; exceptions:", bad[:5],
      "; control (t + 2 a square) holds for all:", ctrl, flush=True)

s2 = all(abs(1 - (m * m + 2) + 1) == m * m and abs(-1 - m + 1) == m for m in range(1, 201))
print("S2 |det(A_m - I)| = m^2 and |det(J_m - I)| = m for m = 1..200:", s2, "; torsion-free only at m = 1:",
      [m for m in range(1, 201) if m * m == 1], flush=True)

s3 = True
for m in range(1, 201):
    N = m * m + 4
    has = any((x * x + 1) % N == 0 for x in range(N))
    s3 &= has == (m % 2 == 1)
print("S3 a square root of -1 mod m^2 + 4 exists exactly for odd m (m = 1..200):", s3, flush=True)
print("all hold:", s1 and s2 and s3 and not ctrl)
