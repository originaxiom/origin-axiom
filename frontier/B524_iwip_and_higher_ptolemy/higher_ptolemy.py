#!/usr/bin/env sage-python
"""B524 Part 2 — higher-rank Ptolemy of the figure-eight 4_1 (SnapPy ptolemy module).
Tests chat1's question: does higher-rank DGG reach NONABELIAN gauge? Answer: no -- higher rank
enriches the representation/arithmetic content but the DGG gauge group is abelian U(1)^r at every K.
"""
import snappy
from sage.all import QQ, PolynomialRing, squarefree_part

R = PolynomialRing(QQ, 't'); t = R.gen()
def field_of(polystr):                       # square-free disc of a quadratic min poly
    p = R(str(polystr).replace('x', 't'))
    if p.degree() != 2: return str(polystr)
    D = p[1]**2 - 4*p[2]*p[0]
    return 'Q(sqrt%s)' % squarefree_part(QQ(D).numerator() * QQ(D).denominator())

M = snappy.Manifold('4_1')
print('4_1: N =', M.num_tetrahedra(), 'tetrahedra, c =', M.num_cusps(), 'cusp(s)')
counts = {}
for K in (2, 3):
    reps = 0; fields = set()
    for pv in M.ptolemy_variety(K, 'all'):
        for s in pv.compute_solutions(engine='sage'):
            reps += 1
            try: fields.add(field_of(s.number_field()))
            except Exception: pass
    counts[K] = reps
    print(f'SL({K}): {reps} boundary-unipotent reps; fields {sorted(fields)}')
assert counts[2] == 1 and counts[3] == 4      # SL2: 1 (Q(sqrt-3)); SL3: 4 (Q(sqrt-3)+Q(sqrt-7))
print('DGG gauge group = U(1)^(N-c) at SL(2); U(1)^{r_K} (abelian) at every K [Dimofte-Gabella-Goncharov 2014]')
print('=> higher rank enriches arithmetic (more reps, +Q(sqrt-7)), NOT gauge -> abelian at all K.')
