#!/usr/bin/env python3
"""The status page's sections 9 and 10: two facts this seat offers main where a VERIFIED record of its rests on
nothing main computed. Data-free, exact or to 40 digits. Computed once, post hoc.

    python3 -I -u rv48_hand.py

H1  W-C1's line 29 (web-wc1-01): [PSL(2, O) : G] = vol(m004) / (3^(3/2) zeta_K(2) / (4 pi^2)), K = Q(sqrt -3),
    zeta_K(2) = zeta(2) L(2, chi_-3), with vol(m004) = 3 Cl_2(2 pi / 3). Expected 12.
H2  The session relay's lines 147 and 155 (web-sr-02): every A in SL(2, Z) with entries in [-6, 6] and A^3 = 1, A != 1
    has trace -1 and det(A - 1) = 3; the only A with A^2 = 1, A != 1 is -1, with det(A - 1) = 4. (Out(E6) = Z/2 and
    gcd(3, 2) = 1 are not computed here.)
"""
import itertools
import mpmath as mp

mp.mp.dps = 40
vol = 3 * mp.clsin(2, 2 * mp.pi / 3)
L2 = mp.nsum(lambda n: mp.mpf(1) / (3 * n + 1) ** 2 - mp.mpf(1) / (3 * n + 2) ** 2, [0, mp.inf])
cov = mp.mpf(3) ** mp.mpf(1.5) * mp.zeta(2) * L2 / (4 * mp.pi ** 2)
print("H1: vol(m004) = %s; the Bianchi covolume = %s; the ratio - 12 = %s" % (mp.nstr(vol, 20), mp.nstr(cov, 20),
                                                                         mp.nstr(vol / cov - 12, 3)))
r = range(-6, 7)
o3, o2 = [], []
for a, b, c, d in itertools.product(r, r, r, r):
    if a * d - b * c != 1 or (a, b, c, d) == (1, 0, 0, 1):
        continue
    sq = (a * a + b * c, a * b + b * d, c * a + d * c, c * b + d * d)
    cube = (sq[0] * a + sq[1] * c, sq[0] * b + sq[1] * d, sq[2] * a + sq[3] * c, sq[2] * b + sq[3] * d)
    dm1 = (a - 1) * (d - 1) - b * c
    if cube == (1, 0, 0, 1):
        o3.append((a + d, dm1))
    if sq == (1, 0, 0, 1):
        o2.append(((a, b, c, d), dm1))
print("H2: elements of order 3 found: %d; their (trace, det(A - 1)): %s" % (len(o3), sorted(set(o3))))
print("H2: elements of order 2 found: %s" % o2)
