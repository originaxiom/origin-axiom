# s20_exact_spectra.py -- exact characteristic polynomial of T on the largest orbit of some leaves mod p (python-flint),
# its factorisation, and the check of the bound mult(2)+mult(-2) >= 2*dim(V_omega) - n = n/3 - 4*e3/3, which follows
# from T = S J + J S with J = C + C^2 (L = S C^2, L^-1 = C S, R = S C, R^-1 = C^2 S; see s01 for S, C).
import numpy as np, flint
from modn import orbits
from orbinv import invariants
for p, kv in ((7, 5), (7, 1), (11, 6), (13, 9), (11, 2)):
    x, y, z, Li, Ri, k, nc, lab = orbits(p); sizes = np.bincount(lab)
    labs = np.unique(lab[k == kv]); big = max(labs, key=lambda l: sizes[l])
    mem = np.nonzero(lab == big)[0]; n = len(mem)
    pos = {int(m): i for i, m in enumerate(mem)}
    pL = [pos[int(Li[m])] for m in mem]; pR = [pos[int(Ri[m])] for m in mem]
    M = np.zeros((n, n), dtype=np.int64)
    for pm in (pL, pR):
        for a, b in enumerate(pm): M[b, a] += 1; M[a, b] += 1
    cp = flint.fmpz_mat(n, n, [int(v) for v in M.ravel()]).charpoly()
    c, facs = cp.factor()
    inv = invariants(pL, pR)
    m2 = sum(e for f, e in facs if str(f) == "x + (-2)")
    mm2 = sum(e for f, e in facs if str(f) == "x + 2")
    degs = sorted(((f.degree(), e) for f, e in facs), reverse=True)
    print("p=%d k=%d n=%d e2=%d e3=%d : mult(+2)=%d mult(-2)=%d sum=%d  bound n/3-4e3/3=%.2f ; factor (degree,multiplicity) list: %s" % (
        p, kv, n, inv['e2'], inv['e3'], m2, mm2, m2+mm2, n/3 - 4*inv['e3']/3, degs), flush=True)
    print("     linear factors:", [(str(f), e) for f, e in facs if f.degree() == 1])
