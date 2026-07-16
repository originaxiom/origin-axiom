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
