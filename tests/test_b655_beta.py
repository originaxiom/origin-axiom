"""B655 locks — the beta adjudication."""
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B655 = os.path.join(HERE, "..", "frontier", "B655_beta_adjudication")


def test_c1_arithmetic():
    assert sp.Rational(-11) + sp.Rational(4, 3) * 3 == -7
    assert sp.Rational(-22, 3) + 4 + sp.Rational(1, 6) == sp.Rational(-19, 6)
    assert sp.Rational(-11, 3) * 12 + 6 == -38


def test_c2_kills():
    As = sp.Matrix([[5, 2], [2, 1]])
    assert (As + sp.eye(2)).det() == 8          # not 7
    assert As.trace() ** 2 - 4 == 32            # not 23
    assert not any(t * t - 4 == 23 for t in range(-100, 101))


def test_c4_base_rate_and_verdict():
    anchors = {2, 3, 5, 6, 7, 8, 11, 12, 13, 19, 23, 24, 27, 32, 60, 120, 360}
    hits = sum(1 for n in range(1, 61)
               if n in anchors or 2 * n in anchors
               or (n % 2 == 0 and n // 2 in anchors))
    assert hits == 27                            # 45%, below the sealed bar
    fnd = open(os.path.join(B655, "FINDINGS.md")).read()
    assert "THREE KILLS" in fnd
    assert "does NOT fire by criterion" in fnd or "does NOT fire" in fnd
    assert "Nothing banks" in fnd
