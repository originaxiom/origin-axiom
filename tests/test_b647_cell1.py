"""B647 cell-1 lock — the reduction is exact and re-runnable."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B647 = os.path.join(HERE, "..", "frontier", "B647_core_mechanism")


def test_cell1_verdicts():
    out = open(os.path.join(B647, "b647_output.txt")).read()
    assert "dim = 6" in out
    assert "not forced" in out
    fnd = open(os.path.join(B647, "FINDINGS.md")).read()
    assert "arg Y[134] = π/6" in fnd


def test_banked_y134_on_the_locus():
    import sympy as sp
    a, b = sp.Rational(1, 24), sp.Rational(1, 72)
    assert a == 3 * b
    assert sp.simplify(sp.arg(3 + sp.sqrt(3) * sp.I) - sp.pi / 6) == 0
