"""B1506 -- checks run after the sealed census, on the same code (`the_level.py`); none of them is a prediction.

(1) The fence.  For every generation-shaped background: its root-deck orbit, how many different extension characters the orbit
    carries, and the order of tau^j lam / lam.  On s961 the three are lam, tau lam, tau^2 lam, pairwise different by a character of
    order 4 (phi - 1 is invertible on H_1, det(phi - 1) = -1): the blocks of an orbit are three different vacua.
(2) The singlet, read against the orbits.  Per (orbit size, lifted, nu^c count times the generation's sign): the backgrounds and
    B1375's lift data.  On M6 B1375's 9 600 (nu^c with the generation's sign) and 57 600 (no nu^c) are split by the orbits.
(3) The level law beyond D0 (T7's proof, any background): the root object Ind_{M_k}^{m004} B of a background B on M_k counts
    gcd(n, k) I(B) on M_n.  Checked on two backgrounds of every orbit size on M3..M6, every sector, three primes."""
import importlib.util
import json
import os
import sys
import time
from collections import Counter
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("b1506_the_level", os.path.join(HERE, "the_level.py"))
T = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(T)


def order(P, c):
    g = P.N
    for x in c:
        g = gcd(g, x)
    return P.N // g


def fence(C, classes):
    """per background: (orbit size, distinct lam in the orbit, orders of tau^j lam / lam for j = 1..size-1)"""
    P = C.P
    out = Counter()
    for key in classes:
        k = C.orbit(key)
        lams = [P.pull(key[0], j) for j in range(k)]
        out[(k, len(set(lams)), tuple(order(P, P.add(l, lams[0], coeffs=[1, -1])) for l in lams[1:]))] += 1
    return {str(k): v for k, v in sorted(out.items())}


def singlets(C, classes):
    """per (orbit size, lifted, nu^c count times the generation's sign): backgrounds and B1375's lift data"""
    P = C.P
    n, lifts = Counter(), Counter()
    for key, Is in classes.items():
        row = (C.orbit(key), key[0] in P.squares, Is[5] * Is[0])
        n[row] += 1
        lifts[row] += C.lift_data(key) if key[0] in P.squares else 0
    return {str(k): dict(backgrounds=n[k], lift_data=lifts[k]) for k in sorted(n)}


def root_objects(C, classes, per_orbit=2):
    """two backgrounds of each orbit size: Ind to m004 of every sector module, restricted to M1..M6, at every prime"""
    P = C.P
    picks = {}
    for key in sorted(classes):
        k = C.orbit(key)
        if len(picks.setdefault(k, [])) < per_orbit:
            picks[k].append(key)
    out = {}
    for k, keys in sorted(picks.items()):
        rows = []
        for key in keys:
            lam, als = key
            per_prime = []
            for q, (F, z) in enumerate(C.fields):
                counts = []
                for a in als:
                    R = T.rs_induce(F, C.module(lam, a, q), P.n, 1)
                    assert R.check_relators([T.RS_RELATOR])
                    row = [T.IL.index(R, [T.RS_RELATOR], "a", T.RS_LONGITUDE)[0]]
                    for m in range(2, 7):
                        Rm, rels_m, mu_m, lam_m = T.rs_restrict_from_root(F, R, m)
                        assert Rm.check_relators(rels_m)
                        row.append(T.IL.index(Rm, rels_m, mu_m, lam_m)[0])
                    counts.append(tuple(row))
                per_prime.append(tuple(counts))
            assert len(set(per_prime)) == 1, per_prime
            I = classes[key]
            law = all(per_prime[0][s][m - 1] == gcd(m, P.n) * I[s] for s in range(len(T.SECTORS)) for m in range(1, 7))
            rows.append(dict(lifted=lam in P.squares, background=I, counts_M1_to_M6=per_prime[0], gcd_law=law))
        out[str(k)] = rows
    return out


def main(levels):
    out = {}
    for n in levels:
        t0 = time.time()
        P = T.Pres("RS", n, N=(T.N6 if n == 3 else None))
        C = T.Census(P, verbose=False)
        row, classes = T.census_summary(C)
        out[f"RS{n}"] = dict(generation_shaped=len(classes), fence=fence(C, classes), singlets=singlets(C, classes),
                             root_objects=root_objects(C, classes))
        out[f"RS{n}"]["seconds"] = round(time.time() - t0, 1)
        print(f"RS M_{n}:", json.dumps(out[f"RS{n}"]), flush=True)
    return out


if __name__ == "__main__":
    levels = [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6]
    res = main(levels)
    if levels == [3, 4, 5, 6]:
        json.dump(res, open(os.path.join(HERE, "post_run_checks.json"), "w"), indent=1)
    print("DONE")
