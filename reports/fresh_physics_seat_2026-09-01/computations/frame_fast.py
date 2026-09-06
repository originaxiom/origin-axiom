"""Fast loader: the icosian E8/E6 data of R64 and R68's two-sided trinification frame, without the 40-triple enumeration."""
import io, contextlib, itertools, collections
from fractions import Fraction as Fr
_src = open(__file__.replace('frame_fast.py', 'r64_founding_ratio_type.py')).read().split("# ---- E8 conjugacy type")[0]
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf): exec(_src)
E6r = E6
one = (ONE5, ZERO5, ZERO5, ZERO5)
# 12 left-g planes
_orbits, _seen = [], set()
for r in E6r:
    if r in _seen: continue
    o = [r, qmul(g, r), qmul(g, qmul(g, r))]; _seen |= set(o); _orbits.append(o)
planes = []
for o in _orbits:
    six = frozenset(o + [tuple(fneg(c) for c in r) for r in o])
    if six not in planes: planes.append(six)
def orth(P, Q): return all(B(p, q) == 0 for p in P for q in Q)
triples = [(i, j, k) for i, j, k in itertools.combinations(range(len(planes)), 3) if orth(planes[i], planes[j]) and orth(planes[i], planes[k]) and orth(planes[j], planes[k])]
def _stable_right(t):
    S = frozenset().union(*[planes[i] for i in t]); return frozenset(qmul(r, g) for r in S) == S
two_sided = [t for t in triples if _stable_right(t)]
assert len(planes) == 12 and len(triples) == 4 and len(two_sided) == 1, (len(planes), len(triples), len(two_sided))
frame = [planes[i] for i in two_sided[0]]
S_sel = frozenset().union(*frame)
if __name__ == "__main__":
    print("planes", len(planes), "left-frames", len(triples), "two-sided", len(two_sided), "| frame roots", len(S_sel))
