"""B928 locks. Pre-results: the seal."""
import hashlib
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B928_d2_decode")
SEALED_SHA = "5a7aa9731b227d0d9ca7c4f56c4787f8f035fcfe2becddf996c85f1e3f14eba8"


def test_decode_seal_unbroken():
    with open(os.path.join(ARC, "PREREGISTRATION.md"), "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == SEALED_SHA


def _res():
    import json
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_outcome_forced_and_the_characterization():
    t = str(_res())
    assert "FORCED" in t
    assert "chi-" in t or "chi_minus" in t or "sigma_{chi-}" in t or "phi*" in t


def test_the_klein_group_and_the_cube_law():
    t = str(_res())
    assert "Klein" in t or "2-torsion" in t
    # the new colored cube law, by Vieta from the stored minpoly
    import sympy as sp
    m = [sp.Integer(int(c)) for c in _res()["Q3_colored"]["minpoly_e3"]]
    assert sp.Rational(-m[-1], m[0]) == -sp.Rational(953, 2304)**3


def test_the_sum_rule_and_sheet_nonempty():
    t = str(_res())
    assert "11" in t
    assert "m_S" in t or "sheet" in t.lower()
