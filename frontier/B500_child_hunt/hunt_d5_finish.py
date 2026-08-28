#!/usr/bin/env sage-python
"""B500 STABILISATION (L187 item 2) -- finish the depth-5 sweep.

The banked run reached 141 of 150 all-three-verb depth-5 words: 115 completed and
26 TIMED OUT, and 9 WERE NEVER REACHED at all -- the run stopped early. The arc's
claim ("absent from 115 of 150") is accurate about what was checked, but a negative
resting on an unfinished sweep is underproved, which is why L187 lists it EXPOSED.

This finishes the 9 never-reached words. Same maps, same target, same AIRLOCK rule.
Timeout raised to 1800s; anything still timing out is reported as such rather than
silently dropped.
"""
import itertools as it, signal, os, sys
from sage.all import PolynomialRing, QQ, NumberField, matrix

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = open(os.path.join(HERE, "hunt_results_d5_finish.txt"), "w")
def log(m):
    print(m, flush=True); OUT.write(m + "\n"); OUT.flush()

R = PolynomialRing(QQ, ['x', 'y', 'z']); x, y, z = R.gens()
F = lambda p: (p[2], p[0], p[0]*p[2] - p[1])
M = lambda p: (p[2], p[2], p[0]*p[1]*p[2] - p[0]**2 - p[1]**2 + 2)
D = lambda p: (p[0]**2 - 2, p[1]**2 - 2, p[0]*p[1]*p[2] - p[0]**2 - p[1]**2 + 2)
GEN = {'F': F, 'M': M, 'D': D}

class TO(Exception): pass
signal.signal(signal.SIGALRM, lambda s, f: (_ for _ in ()).throw(TO()))

CHILD = NumberField(PolynomialRing(QQ, 't')([-1, -1, 0, 0, 1]), 'a')   # t^4 - t - 1
DK = CHILD.discriminant()
log("B500 stabilisation: target d_K=%s" % DK)

NEVER = ['DDFMD','DDFDM','DDMFF','DDMFM','DDMFD','DDMMF','DDMDF','DDDFM','DDDMF']
log("never-reached depth-5 words: %d" % len(NEVER))

hits = []
for w in NEVER:
    p = (x, y, z)
    for c in reversed(w): p = GEN[c](p)
    I = R.ideal([p[0] - x, p[1] - y, p[2] - z])
    signal.alarm(1800)
    try:
        f1, f2, f3 = p[0] - x, p[1] - y, p[2] - z
        r1 = f1.resultant(f3, z); r2 = f2.resultant(f3, z)
        h = r1.resultant(r2, y).univariate_polynomial()
        if h == 0:
            J = matrix(3, 3, lambda i, j: (p[i] - (x, y, z)[i]).derivative((x, y, z)[j])).det()
            S = I.saturation(R.ideal(J))[0]
            if S.dimension() != 0:
                log("%s: positive-dim after saturation - SKIP" % w); signal.alarm(0); continue
            h = S.elimination_ideal([y, z]).gens()[0].univariate_polynomial()
        notable = []
        for g, _ in h.factor():
            if g.degree() < 2: continue
            if g.degree() == 4:
                K = NumberField(g, 'b')
                if K.discriminant() == DK and K.is_isomorphic(CHILD):
                    log("%s: *** AIRLOCK -- CHILD FOUND, deg4 factor isomorphic to Q[x]/(x^4-x-1) ***" % w)
                    hits.append(w)
            if g.degree() <= 12:
                notable.append("deg%d" % g.degree())
        signal.alarm(0)
        log("%s: eliminant deg %d; small factors: %s" % (w, h.degree(), notable[:6] or "none"))
    except TO:
        signal.alarm(0); log("%s: TIMEOUT at 1800s" % w)
    except Exception as e:
        signal.alarm(0); log("%s: ERROR %s" % (w, type(e).__name__))
log("DONE. child hits: %s" % (hits or "NONE"))
