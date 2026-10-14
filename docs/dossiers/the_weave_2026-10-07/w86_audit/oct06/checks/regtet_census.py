"""Audit of A3's supporting sentence: 'the regular-tetrahedral class (all 16 in the first 6000 census manifolds): CS rational
on 16 of 16, every denominator dividing 24'; and '2 of X_gen's 74 states to length 8 are regular-tetrahedral (+LR, -LR)'.
Regular-tetrahedral = SnapPy's canonical triangulation consists of regular ideal tetrahedra (all shapes e^{i pi/3})."""
import snappy, cmath, itertools
from fractions import Fraction
REG = cmath.exp(1j * cmath.pi / 3)
def regular(M):
    try:
        C = M.copy(); C.canonize()
        sh = [complex(z) for z in C.tetrahedra_shapes('rect')]
        return C.solution_type() == 'all tetrahedra positively oriented' and all(abs(z - REG) < 1e-9 for z in sh)
    except Exception: return None
def den(cs):
    x = cs % 0.5
    for d in range(1, 97):
        if abs(x * d - round(x * d)) < 1e-9: return d
    return None
found = []; errs = 0
for i, M in enumerate(snappy.OrientableCuspedCensus):
    if i >= 6000: break
    r = regular(M)
    if r is None: errs += 1; continue
    if r: found.append((M.name(), M.num_tetrahedra(), M.num_cusps(), den(float(M.chern_simons())), round(float(M.chern_simons()), 9)))
print('regular-tetrahedral in the first 6000:', len(found), ' errors:', errs)
for f in found: print('  ', f)
print('denominators:', sorted(set(f[3] for f in found)), ' all divide 24:', all(f[3] and 24 % f[3] == 0 for f in found))
def canon(w):
    sw = w.translate(str.maketrans('LR', 'RL')); return min([w[i:] + w[:i] for i in range(len(w))] + [sw[i:] + sw[:i] for i in range(len(sw))])
prim = lambda w: not any(w == w[:d] * (len(w) // d) for d in range(1, len(w)) if len(w) % d == 0)
words = sorted({canon(''.join(t)) for n in range(2, 9) for t in itertools.product('LR', repeat=n) if 'L' in t and 'R' in t}, key=lambda x: (len(x), x))
states = [sg + w for w in words if prim(w) for sg in ('b++', 'b+-')]
reg = [s for s in states if regular(snappy.Manifold(s))]
print('X_gen states to length 8:', len(states), ' regular-tetrahedral:', reg)
