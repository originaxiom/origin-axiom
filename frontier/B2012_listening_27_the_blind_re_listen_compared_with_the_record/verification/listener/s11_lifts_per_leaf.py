# s11_lifts_per_leaf.py -- for modulus n and divisor d: for every orbit O mod d and every leaf k' mod n lying over
# O's leaf, the orbits mod n on leaf k' inside the preimage of O.  "full" = one orbit containing every lift.
# Prints a summary line per (n,d) and the non-full cases.
import sys
import numpy as np
from collections import Counter, defaultdict
from modn import orbits
def fmt(sz):
    c = Counter(sz)
    return " ".join(("%d" % s) if m == 1 else ("%dx%d" % (s, m)) for s, m in sorted(c.items(), reverse=True))
n, d = int(sys.argv[1]), int(sys.argv[2])
x, y, z, Li, Ri, k, nc, lab = orbits(n)
sizes = np.bincount(lab)
xd, yd, zd, Lid, Rid, kd, ncd, labd = orbits(d)
sd = np.bincount(labd)
rl = labd[((x % d)*d + (y % d))*d + (z % d)]
trip = np.unique(np.stack([rl, k, lab], axis=1), axis=0)
over = defaultdict(list)
for b, kk, a in trip: over[(int(b), int(kk))].append(int(sizes[a]))
lifts_per_point = (n//d)**2
full = 0; nonfull = []
for (b, kk), v in sorted(over.items(), key=lambda t: (t[0][1], -sd[t[0][0]])):
    if len(v) == 1 and v[0] == sd[b]*lifts_per_point: full += 1
    else: nonfull.append((kk, int(sd[b]), v))
print("n=%d over d=%d: (orbit mod d, leaf mod n) pairs: %d; full lifts: %d; not full: %d" % (n, d, len(over), full, len(nonfull)))
for kk, s, v in nonfull:
    print("   leaf k=%d mod %d over an orbit of size %d mod %d (lifts %d): orbits %s" % (kk, n, s, d, s*lifts_per_point, fmt(v)))
