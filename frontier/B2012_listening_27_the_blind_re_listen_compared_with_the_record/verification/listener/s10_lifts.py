# s10_lifts.py -- for modulus n and a divisor d of n: how the orbits mod n sit over the orbits mod d.
# usage: python3 s10_lifts.py n d1 [d2]
#   with one divisor d: for every orbit O mod d (grouped by leaf k mod d), the number and sizes of orbits mod n over it.
#   with two coprime divisors d1*d2 = n: for every pair (O1 mod d1, O2 mod d2) the number of orbits mod n inside O1 x O2.
import sys
import numpy as np
from collections import Counter, defaultdict
from modn import orbits

def fmt(sz):
    c = Counter(sz)
    return " ".join(("%d" % s) if m == 1 else ("%dx%d" % (s, m)) for s, m in sorted(c.items(), reverse=True))

n = int(sys.argv[1]); ds = [int(a) for a in sys.argv[2:]]
x, y, z, Li, Ri, k, nc, lab = orbits(n)
sizes = np.bincount(lab)
reps = {}
def red_labels(d):
    xd, yd, zd, Lid, Rid, kd, ncd, labd = orbits(d)
    idx = ((x % d)*d + (y % d))*d + (z % d)
    return labd[idx], np.bincount(labd), kd
if len(ds) == 1:
    d = ds[0]
    rl, sd, kd = red_labels(d)
    over = defaultdict(set)
    for l, r in zip(lab, rl): pass
    # vectorised: pairs (orbit mod n, orbit mod d)
    pairs = np.unique(np.stack([lab, rl], axis=1), axis=0)
    for a, b in pairs: over[int(b)].add(int(a))
    kd_of = {}
    xd, yd, zd, Lid, Rid, kdd, ncd, labd = orbits(d)
    for b in over:
        kd_of[b] = int(kdd[np.nonzero(labd == b)[0][0]])
    for b in sorted(over, key=lambda b: (kd_of[b], -sd[b])):
        szs = [int(sizes[a]) for a in over[b]]
        ratio = sum(szs) / sd[b]
        print("n=%d over d=%d: leaf k=%d mod %d, orbit of size %d -> %d orbit(s) mod %d, sizes %s (total/size = %g)" % (
            n, d, kd_of[b], d, sd[b], len(szs), n, fmt(szs), ratio))
else:
    d1, d2 = ds
    assert d1*d2 == n
    r1, s1, k1 = red_labels(d1); r2, s2, k2 = red_labels(d2)
    trip = np.unique(np.stack([lab, r1, r2], axis=1), axis=0)
    cnt = defaultdict(list)
    for a, b, c in trip: cnt[(int(b), int(c))].append(int(sizes[a]))
    split = {key: v for key, v in cnt.items() if len(v) > 1}
    print("n=%d = %d x %d: pairs of orbits (O1,O2): %d; pairs whose product splits into >1 orbit: %d" % (n, d1, d2, len(cnt), len(split)))
    hist = Counter()
    for (b, c), v in split.items():
        hist[(int(s1[b]), int(s2[c]), tuple(sorted(v, reverse=True)))] += 1
    for (a, b, v), m in sorted(hist.items()):
        print("   |O1|=%d |O2|=%d -> orbits of sizes %s   (%d such pairs)" % (a, b, list(v), m))
