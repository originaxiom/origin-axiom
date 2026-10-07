#!/usr/bin/env python3
"""Which states of sm:B1550's selection are arithmetic: the minimal polynomial of the trace of squares of a few elements
(they lie in the invariant trace field), recognised by PSLQ at 60 digits from sm:B1527's holonomy. A non-cocompact
Kleinian group of finite covolume is arithmetic exactly when its invariant trace field is imaginary quadratic and every
trace is an algebraic integer (Maclachlan-Reid, The Arithmetic of Hyperbolic 3-Manifolds, Thm 8.3.2). Structure only;
a numerical recognition, not a proof.

    python3 arithmetic.py   ->  arithmetic.json beside this file"""
import json
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent


def _root():
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    import os
    return Path(os.environ["ORIGIN_AXIOM_ROOT"])


import sys
sys.path.insert(0, str(_root() / "frontier" / "B1550_the_three_parities" / "verification"))
import tetra_lib as L  # noqa: E402


def minpoly(z, dmax=6):
    """integer coefficients, leading first, of the least-degree relation found; None if none to degree dmax"""
    for d in range(1, dmax + 1):
        vec = [z ** k for k in range(d + 1)]
        comb = [mp.re(v) + mp.sqrt(2) * mp.im(v) for v in vec]
        rel = mp.pslq(comb, maxcoeff=10 ** 6, maxsteps=10 ** 5)
        if rel and rel[-1] != 0 and abs(mp.fsum(c * v for c, v in zip(rel, vec))) < mp.mpf(10) ** -40:
            rel = rel[::-1]
            if rel[0] < 0:
                rel = [-c for c in rel]
            return rel
    return None


def main():
    FL = L.T.family_lib()
    mp.mp.dps = 60
    out = {}
    for sw in L.STATES:
        A, B, Tt, _ = FL.hyperbolic_sl2(sw[0], sw[1:])
        M = {"a": A, "b": B, "t": Tt}
        rows = {}
        for w in ("aa", "bb", "abab", "aabb", "aBaB"):
            X = FL.sl2_word(w, M)
            rows[w] = minpoly(X[0, 0] + X[1, 1])
        degs = {len(p) - 1 for p in rows.values() if p}
        monic = all(p and abs(p[0]) == 1 for p in rows.values())
        out[sw] = {"minimal polynomials of tr(g^2), leading coefficient first": rows, "degrees": sorted(degs),
                   "monic": monic, "reading": "imaginary quadratic, integral: arithmetic" if degs == {2} and monic
                   else "degree above 2: not arithmetic"}
    (HERE / "arithmetic.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: (v["degrees"], v["monic"], v["reading"]) for k, v in out.items()}))


if __name__ == "__main__":
    main()
