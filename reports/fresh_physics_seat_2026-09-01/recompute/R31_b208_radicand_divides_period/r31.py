#!/usr/bin/env python3
"""R31 — B208's uncommitted numeric claim: squarefree(m^2+4) | P(m)=m(m^2+4)/gcd(m^2+4,4) for m=1..300000.
Reader flag (Phase B, arcs packet): FINDINGS.md claims a re-audit to m=300 000; committed script asserts to m=200.
Here: recomputed with sympy.factorint, plus the 2-adic valuation facts the proof rests on (v2(m^2+4) in {2,3} for m even)."""
from sympy import factorint
from math import gcd
MMAX = 300000
fails, v2set = [], set()
for m in range(1, MMAX + 1):
    n = m * m + 4
    s = 1
    for p, e in factorint(n).items():
        if e % 2: s *= p
    P = m * n // gcd(n, 4)
    if P % s: fails.append(m)
    if m % 2 == 0:
        v = (n & -n).bit_length() - 1; v2set.add(v)
print('m=1..%d  failures: %d  %s' % (MMAX, len(fails), fails[:10]))
print('v2(m^2+4) for even m: %s (proof needs subset of {2,3})' % sorted(v2set))
open('r31_out.txt', 'w').write('m=1..%d failures %d %s\nv2 even-m set %s\n' % (MMAX, len(fails), fails[:10], sorted(v2set)))
