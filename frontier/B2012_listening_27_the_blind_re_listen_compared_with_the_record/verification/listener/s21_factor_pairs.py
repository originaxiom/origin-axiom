# s21_factor_pairs.py -- the irreducible factors of degree >= 2 of charpoly(T) on two big orbits (s20 cases), printed,
# with a test of whether paired factors are related by x -> -x, and the split of the spectrum between N-invariant
# functions and their complement (exact: charpoly of T restricted via integer block matrices).
import numpy as np, flint
from modn import orbits
for p, kv in ((7, 1), (7, 5)):
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
    X = flint.fmpz_poly([0, 1])
    big_f = [f for f, e in facs if f.degree() >= 2]
    print("p=%d k=%d: factors of degree>=2:" % (p, kv))
    for f in big_f:
        fm = flint.fmpz_poly([(-1)**i * int(cf) for i, cf in enumerate(f.coeffs())])
        if f.degree() % 2: fm = -fm
        print("    ", f, "   f(-x) is also a factor:", any(fm == g for g in big_f))
    # N-invariant part: functions on blocks; quotient matrix = block-to-block adjacency (exact)
    def nimg(m, s):
        a, b, cc = int(x[m]), int(y[m]), int(z[m])
        if s == 0: a, b = -a, -b
        elif s == 1: a, cc = -a, -cc
        else: b, cc = -b, -cc
        return ((a % p)*p + (b % p))*p + (cc % p)
    blk = {}; blocks = []
    for m in mem:
        m = int(m)
        if m in blk: continue
        B = sorted(set([m] + [nimg(m, s) for s in range(3)]))
        for q in B: blk[q] = len(blocks)
        blocks.append(B)
    mb = len(blocks)
    Q = np.zeros((mb, mb), dtype=np.int64)
    for i, B in enumerate(blocks):
        q = B[0]
        for t in (blk[int(Li[q])], blk[int(Ri[q])]): Q[t, i] += 1; Q[i, t] += 1
    cq = flint.fmpz_mat(mb, mb, [int(v) for v in Q.ravel()]).charpoly()
    cq_c, cq_f = cq.factor()
    print("   N-invariant part (functions on the %d blocks): factors (degree,mult):" % mb, sorted(((f.degree(), e) for f, e in cq_f), reverse=True))
    rest = cp // cq
    assert rest * cq == cp
    rc, rf = rest.factor()
    print("   complement (dim %d): factors (degree,mult):" % (n - mb), sorted(((f.degree(), e) for f, e in rf), reverse=True))
