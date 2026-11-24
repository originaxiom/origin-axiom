#!/usr/bin/env python3
"""Post hoc, labelled: written after chk_others.py's output showed a root of modulus 1 in P3. It tests the physical
lane's actual claim, that no root of z^3 - 2 s^2 z^2 - 2 z + s^2 is a root of unity. A root of unity of order n that
solves a cubic over Q(omega) has phi(n) <= 6, so n <= 18; orders up to 120 are tested. Data-free.

A root of modulus 1 is forced: the Hermitian-form symmetry pairs roots z <-> 1 / conj(z), and the degree is odd.
"""
import math

import mpmath as mp

mp.mp.dps = 40
w = mp.exp(2j * mp.pi / 3)
for name, s in (("omega^2", w ** 2), ("omega", w)):
    c = [1, -2 * s ** 2, -2, s ** 2]
    for r in mp.polyroots(c, maxsteps=200, extraprec=80):
        if abs(abs(r) - 1) < 1e-20:
            print("%s: unit root, |z| - 1 = %s, arg / 2 pi = %s" % (name, mp.nstr(abs(r) - 1, 3),
                                                                  mp.nstr(mp.arg(r) / (2 * mp.pi), 25)))
    hits = [(n, k) for n in range(1, 121) for k in range(n)
            if math.gcd(k, n) == 1 and abs(mp.polyval(c, mp.exp(2j * mp.pi * k / n))) < 1e-25]
    print("%s: roots of unity of order <= 120 among the roots: %s" % (name, hits))
