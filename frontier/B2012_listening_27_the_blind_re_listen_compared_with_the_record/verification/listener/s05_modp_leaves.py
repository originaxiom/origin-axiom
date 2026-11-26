# s05_modp_leaves.py -- for each modulus n given, each leaf k mod n: number of points and the orbit sizes.
import sys
from modn import leaf_summary, fmt
for n in map(int, sys.argv[1:]):
    out, _ = leaf_summary(n)
    print("##### n = %d" % n)
    for kv in range(n):
        sz = out[kv]
        print("n=%d k=%d  #points=%d  #orbits=%d  sizes: %s" % (n, kv, sum(sz), len(sz), fmt(sz)))
    sys.stdout.flush()
