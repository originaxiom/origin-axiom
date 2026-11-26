# s06_modp_explained.py -- for primes p, every leaf k != 4 mod p: which orbits are reductions of the
# characteristic-0 finite orbits (two-zero orbits, the 16 at k=2, 36 at k=3 [Q(sqrt2)], 72 at k=3 [Q(sqrt5)],
# 40 at k=(5-+sqrt5)/2 [Q(sqrt5)], the origin), and what is left over.  Also checks the point-count formula
# #X_k(F_p) = p^2 + p(3 chi(k-4) + chi(k(k-4))) + 1.
import sys
import numpy as np
from fractions import Fraction as Fr
from modn import orbits
from common import QD, orbit

def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def sqrtmod(a, p):
    a %= p
    for r in range(p):
        if r*r % p == a: return r
    return None

# characteristic-0 exceptional orbits, exact
r2 = QD(0, 1, 2); phi = QD(Fr(1, 2), Fr(1, 2), 5); phii = QD(Fr(-1, 2), Fr(1, 2), 5)
EXC = {
    "16@k=2": orbit((QD(1, 0, 2), QD(1, 0, 2), QD(1, 0, 2)))[0],
    "36@k=3": orbit((r2, QD(1, 0, 2), QD(0, 0, 2)))[0],
    "72@k=3": orbit((phi, phii, QD(0, 0, 5)))[0],
    "40@k=(5-r5)/2": orbit((QD(1, 0, 5), phii, QD(0, 0, 5)))[0],
    "40@k=(5+r5)/2": orbit((QD(1, 0, 5), phi, QD(0, 0, 5)))[0],
}
def reduce_pt(c, p, s):
    # c in Q(sqrt d) -> F_p with sqrt d -> s
    def red(q):
        return (q.numerator % p) * pow(q.denominator % p, -1, p) % p
    return (red(c.a) + red(c.b)*s) % p

primes = [int(a) for a in sys.argv[1:]]
for p in primes:
    x, y, z, Li, Ri, k, nc, lab = orbits(p)
    sizes = np.bincount(lab)
    idx = lambda a, b, c: (a*p + b)*p + c
    explained = {}  # orbit label -> name
    # two-zero orbits
    for t in range(1, p):
        explained.setdefault(lab[idx(t, 0, 0)], "6:two-zero(t=%d)" % min(t, p-t))
    explained.setdefault(lab[0], "origin")
    for name, pts in EXC.items():
        d = pts[0][0].d
        rational = all(c.b == 0 for P in pts for c in P)
        s0 = 0 if rational else sqrtmod(d, p)
        if s0 is None: continue
        for s in {s0, (-s0) % p}:
            red = set(idx(*[reduce_pt(c, p, s) for c in P]) for P in pts)
            labs = set(lab[i] for i in red)
            for l in labs:
                tag = "%s(sqrt%d->%d)%s" % (name, d, s, "" if (len(labs) == 1 and sizes[l] == len(red)) else "[reduction has %d pts, lands in %d orbit(s) of sizes %s]" % (len(red), len(labs), sorted(int(sizes[m]) for m in labs)))
                explained[l] = explained.get(l, "") + ("" if l not in explained else "+") + tag if l in explained else tag
    bad_count = []
    for kv in range(p):
        npts = int((k == kv).sum())
        pred = p*p + p*(3*legendre(kv-4, p) + legendre(kv*(kv-4), p)) + 1
        if npts != pred: bad_count.append((kv, npts, pred))
        if kv == 4: continue
        labs = np.unique(lab[k == kv])
        rest = [l for l in labs if l not in explained]
        desc = ", ".join("%d[%s]" % (sizes[l], explained[l]) for l in labs if l in explained)
        print("p=%d k=%d #pts=%d  unexplained orbits: %s   explained: %s" % (p, kv, npts, sorted((int(sizes[l]) for l in rest), reverse=True), desc))
    print("p=%d point-count formula failures (k, actual, predicted): %s" % (p, bad_count))
    sys.stdout.flush()
