#!/usr/bin/env python3
"""B498 Q2 — the golden monopoly at depth 3 + period-2 points (the decisive refutable test).

For each of the 27 length-3 words W in {F,M,D}: solve W(p)=p exactly; for every isolated fixed
point, test whether each coordinate lies in Q or Q(sqrt5). ANY provably-other field REFUTES the
monopoly. Then the period-2 points of the generators. Results stream to q2_results.txt
(flushed per word) and q2_results.json.

  python3 q2_depth3.py
"""
import itertools as it
import json
import signal
import sys
import os

import sympy as sp
from sympy import (symbols, solve, sqrt, minimal_polynomial, nsimplify,
                   degree, discriminant)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_TXT = os.path.join(HERE, "q2_results.txt")
OUT_JSON = os.path.join(HERE, "q2_results.json")

x, y, z = symbols('x y z')
F = lambda p: (p[2], p[0], p[0]*p[2] - p[1])
M = lambda p: (p[2], p[2], p[0]*p[1]*p[2] - p[0]**2 - p[1]**2 + 2)
D = lambda p: (p[0]**2 - 2, p[1]**2 - 2, p[0]*p[1]*p[2] - p[0]**2 - p[1]**2 + 2)
GEN = {'F': F, 'M': M, 'D': D}


def word(w):
    def f(p):
        for c in reversed(w):
            p = GEN[c](p)
        return p
    return f


class TO(Exception):
    pass


def _alarm(s, f):
    raise TO()


signal.signal(signal.SIGALRM, _alarm)


def field_ok(v):
    """True: in Q or Q(sqrt5). False: provably another field. None: undecided."""
    try:
        vv = nsimplify(v, [sqrt(5)])
        mp_ = minimal_polynomial(vv, x)
        d = degree(mp_, x)
        if d == 1:
            return True
        if d == 2:
            q = sp.simplify(discriminant(mp_, x)/5)
            return bool(q.is_positive and sp.sqrt(q).is_rational)
        return False
    except Exception:
        return None


def log(msg, fh):
    print(msg, flush=True)
    fh.write(msg + "\n")
    fh.flush()


def analyze(eqs, tag, fh, results, timeout):
    signal.alarm(timeout)
    try:
        sols = solve(eqs, [x, y, z], dict=True)
        signal.alarm(0)
    except TO:
        results[tag] = {"status": "TIMEOUT"}
        log("  %-6s TIMEOUT" % tag, fh)
        return
    except Exception as e:
        signal.alarm(0)
        results[tag] = {"status": "ERR", "err": str(e)[:60]}
        log("  %-6s ERR %s" % (tag, str(e)[:60]), fh)
        return
    iso = [[s.get(v, v) for v in (x, y, z)] for s in sols
           if not any(s.get(v, v).free_symbols for v in (x, y, z))]
    nbad = nund = 0
    refuters = []
    for pt in iso:
        verd = [field_ok(c) for c in pt]
        if any(v is False for v in verd):
            nbad += 1
            try:
                mps = [str(minimal_polynomial(nsimplify(c, [sqrt(5)]), x)) for c in pt]
            except Exception:
                mps = ["?"]
            refuters.append({"pt": [str(c) for c in pt], "minpolys": mps})
        elif any(v is None for v in verd):
            nund += 1
    results[tag] = {"status": "OK", "isolated": len(iso), "non_Qsqrt5": nbad,
                    "undecided": nund, "refuters": refuters}
    log("  %-6s solved: %2d isolated, %d NON-Q(sqrt5), %d undecided%s"
        % (tag, len(iso), nbad, nund, "  REFUTERS: %s" % refuters if refuters else ""), fh)


def main():
    results = {}
    with open(OUT_TXT, "w") as fh:
        log("Q2 - golden monopoly at depth 3 (27 words, 120s each):", fh)
        for w in [''.join(t) for t in it.product('FMD', repeat=3)]:
            W = word(w)((x, y, z))
            analyze([sp.Eq(W[i], (x, y, z)[i]) for i in range(3)], w, fh, results, 120)
        log("\nperiod-2 points of the generators (300s each):", fh)
        for name, g in [('F', F), ('M', M), ('D', D)]:
            p2 = g(g((x, y, z)))
            analyze([sp.Eq(p2[i], (x, y, z)[i]) for i in range(3)], name + "^2", fh, results, 300)
        solved = sum(1 for v in results.values() if v.get("status") == "OK")
        bad = [k for k, v in results.items() if v.get("non_Qsqrt5")]
        und = [k for k, v in results.items() if v.get("undecided")]
        to = [k for k, v in results.items() if v.get("status") == "TIMEOUT"]
        log("\nSUMMARY: %d/30 solved; REFUTING words: %s; undecided: %s; timeouts: %s"
            % (solved, bad or "NONE", und or "NONE", to or "NONE"), fh)
    with open(OUT_JSON, "w") as jf:
        json.dump(results, jf, indent=1, default=str)


if __name__ == "__main__":
    main()
