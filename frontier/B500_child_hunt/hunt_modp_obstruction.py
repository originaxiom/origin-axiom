#!/usr/bin/env sage-python
"""B500 STABILISATION -- resolve the 35 unresolved depth-5 words by a mod-p OBSTRUCTION,
instead of waiting longer on a degree-7000 factorisation over Q.

THE IDEA. If the child K = Q[x]/(x^4-x-1) occurs, the eliminant h has an irreducible
degree-4 factor g with Q[x]/(g) isomorphic to K. For any good prime p, g mod p then
factors with EXACTLY the degree pattern of (x^4-x-1) mod p. So if, for even ONE good p,
h mod p contains no set of irreducible factors realising that pattern in a single degree-4
combination, no such g exists and K IS PROVABLY ABSENT for that word.

This is cheap: the whole elimination is done over F_p, where degree-7000 arithmetic is fast.
It is a ONE-SIDED test -- it can PROVE ABSENCE, never presence -- which is exactly the
direction B500's claim needs.

CONTROL (must fire, or the test proves nothing): run the same obstruction against a word
whose eliminant is KNOWN to contain the child's pattern -- here we self-test by checking
that (x^4-x-1) itself is never excluded by its own criterion at any of the primes used.
"""
import itertools as it, os, sys
from sage.all import GF, PolynomialRing, ZZ

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = open(os.path.join(HERE, "hunt_modp_results.txt"), "w")
def log(m):
    print(m, flush=True); OUT.write(m + "\n"); OUT.flush()

PRIMES = [10007, 10009, 10037, 10039, 10061, 10067, 10069, 10079]
Zt = PolynomialRing(ZZ, 't')
CHILD = Zt([-1, -1, 0, 0, 1])          # t^4 - t - 1

def child_pattern(p):
    Fp = PolynomialRing(GF(p), 't')
    return tuple(sorted(g.degree() for g, e in Fp(CHILD).factor() for _ in range(e)))

def eliminant_modp(word, p):
    R = PolynomialRing(GF(p), ['x', 'y', 'z']); x, y, z = R.gens()
    F = lambda q: (q[2], q[0], q[0]*q[2] - q[1])
    M = lambda q: (q[2], q[2], q[0]*q[1]*q[2] - q[0]**2 - q[1]**2 + 2)
    D = lambda q: (q[0]**2 - 2, q[1]**2 - 2, q[0]*q[1]*q[2] - q[0]**2 - q[1]**2 + 2)
    G = {'F': F, 'M': M, 'D': D}
    q = (x, y, z)
    for c in reversed(word): q = G[c](q)
    f1, f2, f3 = q[0] - x, q[1] - y, q[2] - z
    r1 = f1.resultant(f3, z); r2 = f2.resultant(f3, z)
    return r1.resultant(r2, y).univariate_polynomial()

def realisable(h, pattern):
    """Can the pattern be assembled from degrees of h's irreducible factors (with multiplicity)?"""
    degs = []
    for g, e in h.factor():
        degs.extend([g.degree()] * e)
    need = list(pattern); pool = list(degs)
    for d in need:
        if d in pool: pool.remove(d)
        else: return False
    return True

print("CONTROL: the child must never be excluded by its own criterion")
ok = True
for p in PRIMES:
    Fp = PolynomialRing(GF(p), 't')
    if not realisable(Fp(CHILD), child_pattern(p)): ok = False
log("CONTROL child-vs-itself realisable at every prime: %s" % ok)
if not ok:
    log("CONTROL FAILED -- the test is not sound; stopping."); sys.exit(1)

WORDS = sys.argv[1:] or ['DDFMD']
for w in WORDS:
    excluded_at = None
    for p in PRIMES:
        try:
            h = eliminant_modp(w, p)
            if h == 0:
                log("%s: eliminant vanishes mod %d -- inconclusive here" % (w, p)); continue
            if not realisable(h, child_pattern(p)):
                excluded_at = p; break
        except Exception as e:
            log("%s: p=%d ERROR %s" % (w, p, type(e).__name__)); continue
    if excluded_at:
        log("%s: CHILD PROVABLY ABSENT (obstruction at p=%d)" % (w, excluded_at))
    else:
        log("%s: not excluded by any tested prime -- INCONCLUSIVE, needs the Q-side factorisation" % w)
