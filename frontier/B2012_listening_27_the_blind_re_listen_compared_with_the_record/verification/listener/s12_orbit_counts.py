# s12_orbit_counts.py -- number of orbits on the leaf k mod n, for each modulus n given and k = 0..KMAX (k taken mod n).
import sys, os
import numpy as np
from modn import orbits
from collections import Counter
def fmt(sz):
    c = Counter(sz)
    return " ".join(("%d" % s) if m == 1 else ("%dx%d" % (s, m)) for s, m in sorted(c.items(), reverse=True))
KMAX = int(os.environ.get('KMAX', '12'))
for n in map(int, sys.argv[1:]):
    x, y, z, Li, Ri, k, nc, lab = orbits(n)
    sizes = np.bincount(lab)
    for kv in range(KMAX+1):
        labs = np.unique(lab[k == kv % n])
        print("n=%d k=%d #orbits=%d sizes: %s" % (n, kv, len(labs), fmt([int(sizes[l]) for l in labs])), flush=True)
