"""Audit of A3's sentence 'all 16 regular-tetrahedral census manifolds in the first 6000 ... CS rational, every denominator
dividing 24 (1:5, 3:1, 4:5, 8:2, 12:2, 24:1)': use SnapPy's TetrahedralOrientableCuspedCensus (manifolds built from regular
ideal tetrahedra), keep those with <= 8 tetrahedra, locate each in OrientableCuspedCensus and keep the first 6000."""
import snappy
from collections import Counter
idx = {}
for i, M in enumerate(snappy.OrientableCuspedCensus):
    if i >= 6000: break
    idx[M.isometry_signature()] = (i, M.name())
print('first 6000 of OrientableCuspedCensus end at', list(idx.values())[-1])
T = snappy.TetrahedralOrientableCuspedCensus
found = []
for M in T:
    if M.num_tetrahedra() > 8: continue
    s = M.isometry_signature()
    if s in idx:
        cs = float(M.chern_simons()) % 0.5
        den = next((d for d in range(1, 97) if abs(cs * d - round(cs * d)) < 1e-9), None)
        found.append((idx[s][1], M.name(), M.num_cusps(), den, round(cs, 9)))
found.sort(key=lambda f: idx[[k for k, v in idx.items() if v[1] == f[0]][0]][0])
print('tetrahedral manifolds among the first 6000:', len(found))
for f in found: print('  ', f)
print('denominators:', dict(sorted(Counter(f[3] for f in found).items())), ' all divide 24:', all(f[3] and 24 % f[3] == 0 for f in found))
