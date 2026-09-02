#!/usr/bin/env python3
"""R40 — B516: under x -> x(1+sqrt x), among the metallic means only the golden one gives a Pisot number.
PARI: minimal polynomial by algdep, all conjugates by polroots, Pisot iff every other conjugate has |.| < 1."""
from snappy import pari
pari.set_real_precision(60)
lines = []
for m in range(1, 5):
    x = (m + pari(m * m + 4).sqrt()) / 2
    beta = x * (1 + x.sqrt())
    p = pari.algdep(beta, 8)
    for f, _ in zip(*pari.factor(p)):
        if pari.poldegree(f) >= 1 and abs(pari.subst(f, 'x', beta)) < 1e-40: break
    roots = list(pari.polroots(f))
    roots.sort(key=lambda r: abs(r - beta))
    others = [abs(r) for r in roots[1:]]
    s = 'm=%d  beta=%.6f  minpoly %s  |other conjugates| = %s  Pisot: %s' % (m, beta, f, [float('%.4f' % o) for o in others], all(o < 1 for o in others))
    print(s); lines.append(s)
open('r40_out.txt', 'w').write('\n'.join(lines) + '\n')
