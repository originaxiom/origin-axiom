# s13_mixed.py -- mixed moduli n = m1*m2 (coprime): on each leaf k mod n, compare the number of orbits with the
# number of pairs (orbit mod m1, orbit mod m2) on the leaves k mod m1, k mod m2. If every product O1 x O2 were one
# orbit the two numbers would agree; print every leaf where they differ, with the splitting.
import sys
import numpy as np
from collections import Counter, defaultdict
from modn import orbits
def fmt(sz):
    c = Counter(sz)
    return " ".join(("%d" % s) if m == 1 else ("%dx%d" % (s, m)) for s, m in sorted(c.items(), reverse=True))
for arg in sys.argv[1:]:
    m1, m2 = map(int, arg.split('x')); n = m1*m2
    x, y, z, Li, Ri, k, nc, lab = orbits(n); sizes = np.bincount(lab)
    r = {}
    for m in (m1, m2):
        xm, ym, zm, Lm, Rm, km, ncm, labm = orbits(m)
        r[m] = (labm[((x % m)*m + (y % m))*m + (z % m)], np.bincount(labm))
    trip = np.unique(np.stack([k, r[m1][0], r[m2][0], lab], axis=1), axis=0)
    per = defaultdict(list)
    for kk, a, b, l in trip: per[(int(kk), int(a), int(b))].append(int(sizes[l]))
    nsplit = 0; npairs = len(per)
    lines = []
    for (kk, a, b), v in sorted(per.items()):
        if len(v) > 1:
            nsplit += 1
            lines.append("   leaf k=%d mod %d: O1 (size %d mod %d) x O2 (size %d mod %d) -> %d orbits: %s" % (kk, n, r[m1][1][a], m1, r[m2][1][b], m2, len(v), fmt(v)))
    print("n=%d=%dx%d: pairs (leaf, O1, O2) = %d; pairs splitting into >1 orbit: %d" % (n, m1, m2, npairs, nsplit), flush=True)
    for l in lines: print(l)

