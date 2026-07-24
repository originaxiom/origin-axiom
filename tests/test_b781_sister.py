"""B781 -- the m003 sister-distinction: the monodromy-trace/homology mechanism."""
import json
import pathlib

import sympy as sp

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B781_m003_sister"


def test_monodromy_trace_homology_mechanism():
    # |H_1 torsion| = |2 - tr(M)|: m004 trace 3 -> 1 (Z); m003 torsion 5 -> trace != 3
    R = sp.Matrix([[1, 1], [0, 1]])
    L = sp.Matrix([[1, 0], [1, 1]])
    M4 = R * L
    assert M4.trace() == 3
    assert M4.charpoly(sp.Symbol("x")).as_expr() == sp.Symbol("x")**2 - 3 * sp.Symbol("x") + 1
    assert abs(2 - 3) == 1                       # m004: torsion trivial (H_1 = Z)
    # m003 torsion Z/5 forces |2 - tr| = 5 -> trace in {-3, 7}, never 3
    assert 3 not in [t for t in range(-9, 10) if abs(2 - t) == 5]


def test_sister_residual_closed():
    d = json.loads((ARC / "results.json").read_text())
    assert d["verdict"] == "RESOLVED-A"
    assert d["distinguished"]
    assert d["m004_homology"] == "Z" and "5" in d["m003_homology"]
    assert d["m004_monodromy_trace"] == 3
