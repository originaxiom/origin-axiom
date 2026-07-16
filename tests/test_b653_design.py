"""B653 locks — the C2 seal's arithmetic."""
import hashlib
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B653 = os.path.join(HERE, "..", "frontier", "B653_phase_c_probe")


def test_seal_hash_live():
    h = hashlib.sha256(open(os.path.join(
        B653, "COMPARISON_DESIGN_C2.md"), "rb").read()).hexdigest()
    rec = open(os.path.join(B653, "ARTIFACT_HASHES.txt")).read()
    assert h in rec


def test_prediction_arithmetic_exact():
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(1 / (2 * phi) - (sp.sqrt(5) - 1) / 4) == 0
    # the C-prime branch fix: the Galois image is out of range
    galois = sp.simplify((1 / (2 * phi)).subs(sp.sqrt(5), -sp.sqrt(5)))
    assert sp.N(galois) < 0  # = -phi/2, unphysical for sin^2
    # the printed 20-digit value in the seal
    assert str(sp.N(1 / (2 * phi), 20)).startswith("0.3090169943749474241")


def test_design_pins_the_essentials():
    d = open(os.path.join(B653, "COMPARISON_DESIGN_C2.md")).read()
    for req in ("C′", "zero-calibration", "|z| > 4", "|z| ≤ 2",
                "FIRST published", "one-shot", "FAILS the held-out-provenance",
                "5–6%", "4/13"):
        assert req in d, req


def test_adjudication_banked():
    a = open(os.path.join(B653, "ADJUDICATION.md")).read()
    assert "OUTCOME A — CONSISTENCY" in a
    assert "≈ 32%" in a and "LOW EVIDENTIAL WEIGHT" in a
    assert "license is SPENT" in a
    assert "FACTUALLY WRONG" in a  # the provenance erratum, owned
    # z re-verified exactly
    import sympy as sp
    z = (sp.Rational("0.3092") - (sp.sqrt(5) - 1) / 4) / sp.Rational("0.0087")
    assert abs(float(sp.N(z)) - 0.021035) < 1e-5
    # the archived prediction hash matches the sealed one
    import hashlib
    h = hashlib.sha256(open(os.path.join(
        B653, "packets", "PREDICTION.md"), "rb").read()).hexdigest()
    assert h == ("4392e2718af05bb78975c5d8c224a9280167e4bc"
                 "144416080cea4ac66c35e6b3")


def test_addendum_reconciliation():
    a = open(os.path.join(B653, "ADJUDICATION_ADDENDUM.md")).read()
    assert "VOID-AS-HELD-OUT-CONFIRMATION" in a
    assert "SPENT as banked" in a
    assert "0.88σ" in a  # cc2's ~9σ corrected
    import sympy as sp
    gap = (sp.sqrt(5) - 1) / 4 - sp.Rational(4, 13)
    assert abs(float(sp.N(gap)) / 0.0015 - 0.88) < 0.01
