#!/usr/bin/env python3
"""P-739 (Review 80's item R80-9): the monodromy on H_1 of the fibre, SOLVED from the relators instead of searched for.

WHY.  B1847's fibre_faces.monodromy_from_relators searches integer matrices [[p, q], [r, s]] of determinant 1 with
p, q, r in -40..40 (s follows from the determinant).  In the basis of the presentation's two fibre letters the
monodromy of b++L^6 R (LR)^k is [[-1, -3], [8, 23]] at k = 1, [[15, -28], [-23, 43]] at k = 2 and
[[109, -71], [-66, 43]] at k = 3 (traces 22, 58, 152, the traces of the word's own matrix).  At k = 3 the entries
p, q, r are all beyond 40, so the search finds nothing, and the mesher stops at `assert len(sols) == 1`, a check with
no message.
WHAT THIS DOES.  The same unknowns and the same equations: the class of a word is sum over its fibre letters of
sign * M^h e, h the height at that letter; every relator's class is zero.  With M^-1 the adjugate (determinant 1) the
equations are polynomial in p, q, r, s; sympy solves them with p s - q r = 1.  Returned in the form the mesher uses.
CONTROL: at k = 1 and k = 2 it must give exactly the matrix the search gives (run this file)."""
import sympy as sp
import numpy as np


def monodromy_from_relators(gens, rels, chi):
    fib = [g for g in gens if chi[g] == 0]
    cg = [g for g in gens if chi[g] != 0]
    assert len(fib) == 2 and len(cg) == 1 and chi[cg[0]] == 1, "the presentation is not two fibre letters and one stable letter of height 1: %s" % ({g: chi[g] for g in gens},)
    c = cg[0]
    def cls(word, M, Minv):
        v = np.zeros(2, dtype=object); h = 0
        for ch in word:
            low = ch.lower(); sgn = 1 if ch.islower() else -1
            if low == c:
                h += sgn; continue
            e = np.array([1, 0] if low == fib[0] else [0, 1], dtype=object)
            P = np.eye(2, dtype=object)
            for _ in range(abs(h)):
                P = P.dot(M if h > 0 else Minv)
            v = v + sgn * P.dot(e)
        return v
    p, q, r, s = sp.symbols("p q r s")
    Ms = sp.Matrix([[p, q], [r, s]]); Mi = sp.Matrix([[s, -q], [-r, p]])
    def cls_sym(word):
        v = sp.zeros(2, 1); h = 0
        for ch in word:
            low = ch.lower(); sgn = 1 if ch.islower() else -1
            if low == c:
                h += sgn; continue
            e = sp.Matrix([1, 0]) if low == fib[0] else sp.Matrix([0, 1])
            v = v + sgn * ((Ms ** h) if h >= 0 else (Mi ** (-h))) * e
        return v
    eqs = [sp.expand(x) for w in rels for x in cls_sym(w)] + [p * s - q * r - 1]
    eqs = [e for e in eqs if e != 0]
    found = sp.solve(eqs, [p, q, r, s], dict=True)
    sols = []
    for d in found:
        vals = [d.get(x, x) for x in (p, q, r, s)]
        if all(v.is_Integer for v in vals):
            M = np.array([[int(vals[0]), int(vals[1])], [int(vals[2]), int(vals[3])]], dtype=object)
            Minv = np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]], dtype=object)
            assert all(not any(cls(w, M, Minv)) for w in rels), "a solution does not satisfy a relator"
            if not any((M == X).all() for X in sols): sols.append(M)
    return fib, c, sols, cls


if __name__ == "__main__":
    import sys, os, time
    ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")   # verification -> the arc -> frontier -> the root
    sys.path.insert(0, os.path.join(ROOT, "frontier", "B1847_the_level_surfaces_own_modulus", "verification")); sys.path.insert(0, os.path.join(ROOT, "frontier", "B1846_the_metrics_read_out", "verification"))
    import snappy
    from oa_harm import _chi_vector
    import fibre_faces as FF
    L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
    for k in (1, 2, 3, 4, 5):
        name = "b++LLLLLLR" + "LR" * k
        G = snappy.Manifold(name).fundamental_group(); gens = G.generators(); rels = G.relators(); chi = _chi_vector(gens, rels)
        t0 = time.time(); fib, c, sols, cls = monodromy_from_relators(gens, rels, chi); t1 = time.time() - t0
        W = (L ** 6) * R * ((L * R) ** k)
        line = "k = %d: %d generators, %d relators (lengths %s); exact: %d solution(s) %s, trace %s, in %.1fs; the word's own matrix has trace %d" % (
            k, len(gens), len(rels), [len(w) for w in rels], len(sols), [m.tolist() for m in sols], [int(m[0, 0] + m[1, 1]) for m in sols], t1, W.trace())
        if k <= 2:
            t0 = time.time(); _, _, old, _ = FF.monodromy_from_relators(gens, rels, chi)
            line += "; the search: %d solution(s) %s, in %.0fs; the same: %s" % (len(old), [m.tolist() for m in old], time.time() - t0, len(old) == len(sols) and all((a == b).all() for a, b in zip(old, sols)))
        print(line, flush=True)
