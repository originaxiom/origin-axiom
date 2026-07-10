#!/usr/bin/env sage-python
"""B500 — THE CHILD HUNT (depth 4, all-three-verb words). Streamed to hunt_results.txt.
Target (prereg): the child field Q[x]/(x^4-x-1), d_K=-283. Match = FIELD ISOMORPHISM.
A -283 disc hit = B398 AIRLOCK: print AIRLOCK and stop interpretation."""
import itertools as it, signal, os
from sage.all import PolynomialRing, QQ, NumberField, gp, matrix

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = open(os.path.join(HERE, "hunt_results.txt"), "w")
def log(m):
    print(m, flush=True); OUT.write(m + "\n"); OUT.flush()

R = PolynomialRing(QQ, ['x', 'y', 'z']); x, y, z = R.gens()
F = lambda p: (p[2], p[0], p[0]*p[2] - p[1])
M = lambda p: (p[2], p[2], p[0]*p[1]*p[2] - p[0]**2 - p[1]**2 + 2)
D = lambda p: (p[0]**2 - 2, p[1]**2 - 2, p[0]*p[1]*p[2] - p[0]**2 - p[1]**2 + 2)
GEN = {'F': F, 'M': M, 'D': D}

class TO(Exception): pass
signal.signal(signal.SIGALRM, lambda s, f: (_ for _ in ()).throw(TO()))

CHILD = NumberField(PolynomialRing(QQ, 't')([-1, -1, 0, 0, 1]), 'a')  # t^4 - t - 1
log("B500 child hunt: target d_K=%s" % CHILD.discriminant())

words = [''.join(w) for w in it.product('FMD', repeat=4) if set(w) == set('FMD')]
log("depth-4 all-three-verb words: %d" % len(words))
for w in words:
    p = (x, y, z)
    for c in reversed(w): p = GEN[c](p)
    I = R.ideal([p[0] - x, p[1] - y, p[2] - z])
    signal.alarm(240)
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
        signal.alarm(0)
        hits = []
        for f, m in h.factor():
            d = f.degree()
            if d < 3: continue
            try:
                g = gp.polgalois(str(f).replace('x', 't'))
                order = int(str(g).strip('[]').split(',')[0])
            except Exception:
                order = -1
            tag = "deg%d ord%d" % (d, order)
            if d == 4 and order == 24:
                K = NumberField(f.change_variable_name('t'), 'b')
                dk = K.discriminant()
                tag += " S4 d_K=%s" % dk
                if dk == -283:
                    iso = K.is_isomorphic(CHILD)
                    log("!!!! AIRLOCK CANDIDATE %s: d_K=-283, isomorphic=%s — B398: STOP, CONVENE !!!!" % (w, iso))
                hits.append(tag)
            elif order != d and order > 0:
                hits.append(tag + " NONAB")
        log("%s: eliminant deg %d; wild/notable: %s" % (w, h.degree(), hits if hits else "none"))
    except TO:
        log("%s: TIMEOUT" % w)
    except Exception as e:
        signal.alarm(0); log("%s: ERR %s" % (w, str(e)[:50]))
log("HUNT COMPLETE")
OUT.close()
