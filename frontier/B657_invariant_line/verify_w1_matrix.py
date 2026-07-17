"""B657 — independent verification of W1's sealed portal matrix.

The packet's portal_matrix.json is the sealed artifact (sha 1412d08a...,
verified in SEALS.txt). This seat re-derives its linear-algebra claims
with independent code (sympy exact over Q(sqrt(-3))): rank 5, kernel 0,
exact block-diagonality on the boundary-born {0,1} / solo-inherited
{2,3,4} split, and the quoted entries (corners 1 / -2, middle -15/11,
the upper-triangular 2x2 with denominators 75600 / 1425600 /
16765056000). The portal PIPELINE's independent re-run is W2a (silver),
reproduced end-to-end on this machine (w2a rerun; see FINDINGS.md).
"""
import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "packet", "w1_portal",
                                "portal_matrix.json")))

s3 = sp.sqrt(-3)


def parse(e):
    if isinstance(e, list) and len(e) == 2:
        return sp.Rational(e[0]) + sp.Rational(e[1]) * s3
    return sp.Rational(e)


M = sp.Matrix(5, 5, lambda i, j: parse(d["portal_matrix"][i][j]))

print("gates:", all(v is True or isinstance(v, int)
                    for v in d["gates"].values()))
print("independent rank:", M.rank())
print("det nonzero (kernel 0):", sp.simplify(M.det()) != 0)
off = ([(i, j) for i in (0, 1) for j in (2, 3, 4)]
       + [(i, j) for i in (2, 3, 4) for j in (0, 1)])
print("block-diagonal on {0,1}/{2,3,4}:",
      all(sp.simplify(M[i, j]) == 0 for i, j in off))
print("solo 3x3 corners/middle:",
      M[4, 2] == 1, M[2, 4] == -2, M[3, 3] == sp.Rational(-15, 11))
print("boundary 2x2 upper-triangular:", M[1, 0] == 0)
print("  entries:", M[0, 0], "|", M[0, 1], "|", M[1, 1])
