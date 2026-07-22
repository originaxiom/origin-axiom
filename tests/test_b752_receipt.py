"""Locks for B752 -- the qualia-handoff receipt."""
import os

import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "frontier", "B752_qualia_handoff_receipt", "output.txt")


def test_cayley_hamilton_universal_collapse():
    a, b, c, d = sp.symbols("a b c d")
    A = sp.Matrix([[a, b], [c, d]])
    adjA = sp.Matrix([[d, -b], [-c, a]])
    assert sp.simplify(A + adjA - (a + d) * sp.eye(2)) == sp.zeros(2, 2)


def test_fixed_points_and_stability():
    x = sp.symbols("x")
    f = 3 - x - 1 / x
    fps = set(sp.solve(sp.Eq(f, x), x))
    assert fps == {sp.Rational(1, 2), sp.Integer(1)}
    df = sp.diff(f, x)
    assert df.subs(x, sp.Rational(1, 2)) == 3      # repelling
    assert df.subs(x, 1) == 0                       # superattracting


def test_corrected_holonomy_gives_one():
    A = sp.Matrix([[1, 1], [0, 1]])                 # B285 banked meridian, trace 2
    assert sp.trace(A) == 2
    assert -A + 3 * sp.eye(2) - A.inv() == sp.eye(2)


def test_banked_output_verdicts():
    text = open(OUT, encoding="utf-8").read()
    assert "window 0.1% (the handoff's rule): HITS = 1" in text
    assert "window 1% (B751's rule): HITS = 4" in text
    assert "CELL 2 VERDICT: UNIVERSAL" in text
    assert "{'1/2': 3, '1': 0}" in text
