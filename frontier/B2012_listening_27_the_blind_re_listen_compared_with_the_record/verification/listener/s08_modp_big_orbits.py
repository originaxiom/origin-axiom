# s08_modp_big_orbits.py -- the largest orbit on each leaf k != 4 mod p: group generated (GAP), signs, genus data.
import sys
import numpy as np
from modn import orbits
from orbinv import invariants, gap_info
primes = [int(a) for a in sys.argv[1:]]
for p in primes:
    x, y, z, Li, Ri, k, nc, lab = orbits(p)
    sizes = np.bincount(lab)
    for kv in range(p):
        if kv == 4 % p: continue
        labs = np.unique(lab[k == kv])
        big = max(labs, key=lambda l: sizes[l])
        members = np.nonzero(lab == big)[0]
        if len(members) < 50:
            print("p=%d k=%d largest orbit has only %d points; skipped" % (p, kv, len(members))); continue
        pos = {int(m): i for i, m in enumerate(members)}
        pL = [pos[int(Li[m])] for m in members]; pR = [pos[int(Ri[m])] for m in members]
        inv = invariants(pL, pR)
        gi = gap_info(pL, pR, congruence=False)
        print("p=%d k=%d n=%d group=%s primitive=%s sign(L)=%d e2=%d e3=%d cusps=%d genus=%s level=%d" % (
            p, kv, inv['n'], gi['natural'] or ("order %d" % gi['order']), gi['primitive'], gi['sign_L'], inv['e2'], inv['e3'], inv['cusps'], inv['genus'], inv['level']), flush=True)
