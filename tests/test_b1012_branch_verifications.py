"""B1012 — locks: the two exact verifications stay true, and the k-blindness equivalence holds."""
import json
import pathlib
import sys

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1012_branch_verifications"
sys.path.insert(0, str(ARC))


def test_k_blindness_is_an_equivalence():
    """dS/dk = -CS identically: blind-to-k <=> CS = 0 <=> amphichirality (B303)."""
    from b1012_verify import k_blindness
    r = k_blindness()
    assert r["S_equals_minus_CSk_minus_Vol_sigma"] is True
    assert sp.simplify(r["dS_dk"] + sp.Symbol("CS", real=True)) == 0
    assert r["dS_dk_at_CS0"] == 0


def test_the_normalisation_closure_holds():
    """R4's discharge: three independent entries close; c = 6*sigma forced."""
    from b1012_verify import normalisation_closure
    assert all(normalisation_closure().values())


def test_the_register_keeps_the_owed_items_owed():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    c = v["claim_one_line"]
    assert "OWED a verification cell" in c, "the rank-wall claims must stay owed until verified"
    assert "STILL REFUSED per B1009" in c, "theta_QCD stays functor-gated"
    assert "TERMINOLOGY HAZARD" in c
