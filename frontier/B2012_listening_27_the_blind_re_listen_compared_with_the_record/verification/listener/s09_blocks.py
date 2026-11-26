# s09_blocks.py -- the largest orbit on a leaf mod p, seen through its blocks.
# The sign changes N = {1, s12, s13, s23} are normalised by L and R (s01), so N-orbits are blocks.
# We compute: Q = action on blocks (natural Alt/Sym?), |G|, |G|/|Q| (kernel order), its 2-adic valuation,
# the image of G in Sym(3) acting on N by conjugation (computed from the moves on N, independent of the point),
# and the parity of L and R on the orbit and on the blocks.
import sys, time
import numpy as np
from modn import orbits
from sage.all import libgap
import os
MAXN = int(os.environ.get('MAXN', '230'))

def analyse(p, kv, verbose=True):
    x, y, z, Li, Ri, k, nc, lab = orbits(p)
    sizes = np.bincount(lab)
    labs = np.unique(lab[k == kv])
    big = max(labs, key=lambda l: sizes[l])
    mem = np.nonzero(lab == big)[0]
    pos = {int(m): i for i, m in enumerate(mem)}
    n = len(mem)
    pL = [pos[int(Li[m])] for m in mem]; pR = [pos[int(Ri[m])] for m in mem]
    # blocks
    def nimg(m, s):
        a, b, c = int(x[m]), int(y[m]), int(z[m])
        if s == 0: a, b = -a, -b
        elif s == 1: a, c = -a, -c
        else: b, c = -b, -c
        return ((a % p)*p + (b % p))*p + (c % p)
    blk = {}
    blocks = []
    for m in mem:
        m = int(m)
        if m in blk: continue
        B = sorted(set([m] + [nimg(m, s) for s in range(3)]))
        for q in B: blk[q] = len(blocks)
        blocks.append(B)
    bsz = set(len(B) for B in blocks)
    qL = [blk[int(Li[B[0]])] for B in blocks]; qR = [blk[int(Ri[B[0]])] for B in blocks]
    # consistency: blocks map to blocks
    ok = all(blk[int(Li[q])] == qL[i] and blk[int(Ri[q])] == qR[i] for i, B in enumerate(blocks) for q in B)
    t0 = time.time()
    gL = libgap.PermList([i+1 for i in pL]); gR = libgap.PermList([i+1 for i in pR])
    G = libgap.Group([gL, gR])
    hL = libgap.PermList([i+1 for i in qL]); hR = libgap.PermList([i+1 for i in qR])
    Q = libgap.Group([hL, hR])
    m = len(blocks)
    qa = bool(libgap.IsNaturalAlternatingGroup(Q)); qs = bool(libgap.IsNaturalSymmetricGroup(Q))
    qprim = bool(Q.IsPrimitive(libgap.eval("[1..%d]" % m)))
    t1 = time.time()
    oG = int(G.Size()) if n <= MAXN else None; t2 = time.time()
    from math import factorial
    oQ = factorial(m)//(2 if qa else 1) if (qa or qs) else int(Q.Size())
    if oG is None:
        ker, v2, kk = -1, -1, -1
    else:
        ker = oG // oQ
        v2 = 0; kk = ker
        while kk % 2 == 0: kk //= 2; v2 += 1
    print("p=%d k=%d n=%d blocks=%d (sizes %s, consistent=%s) Q=%s primitive=%s  |G|/|Q| = %d = 2^%d * %d   sign L on orbit=%d, on blocks=%d  [%.1fs,%.1fs]" % (
        p, kv, n, m, sorted(bsz), ok, ("Alt(%d)" % m) if qa else (("Sym(%d)" % m) if qs else "order %d" % oQ), qprim,
        ker, v2, kk, int(libgap.SignPerm(gL)), int(libgap.SignPerm(hL)), t1-t0, t2-t1), flush=True)

if __name__ == "__main__":
    p = int(sys.argv[1])
    ks = [int(a) for a in sys.argv[2:]] if len(sys.argv) > 2 else [kv for kv in range(p) if kv != 4 % p]
    for kv in ks:
        analyse(p, kv)
