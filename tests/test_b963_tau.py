"""B963 locks — tau's double duty, the rejected analogy, and the scope correction."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B963_tau_double_duty"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_computed_half_is_recorded_separately_from_the_cited_half():
    r = _res()
    assert r["computed_here"]["tau_nontrivial"] is True
    assert r["computed_here"]["inner_sign_gradings_tested"] == 63
    assert len(r["cited_not_verified"]) == 3


def test_the_uncertainty_analogy_is_REJECTED():
    r = _res()
    assert r["is_it_an_uncertainty_principle"] is False
    assert "no continuous amount of chirality" in r["why_not"]["reality_type_is_discrete"]


def test_the_scope_correction_is_the_load_bearing_content():
    """The claim nearly banked, and why it was wrong."""
    r = _res()["THE_SCOPE_CORRECTION"]
    assert "NO INTERMEDIATE REGIME" in r["what_I_nearly_banked"]
    assert "PRINCIPAL sl2" in r["what_B576_actually_supports"]
    assert any("FINITE-image" in x for x in r["NOT_established_for"])
    assert r["does_the_conclusion_survive"] is True
    assert "B959" in r["why"]


def test_it_does_not_claim_to_solve_the_SM():
    r = _res()
    assert r["does_it_solve_the_SM_problem"] is False
    d = r["what_it_does_and_does_not"]
    assert "unreachable" in d["does_not_2"] and "standard" in d["does_not_2"]
    assert "crossings" in d["does_not_3"] and "retrofit excuse" in d["does_not_3"]


def test_the_false_unification_risk_is_named():
    assert contains(CELL / "FINDINGS.md",
                    "two arguments, not one",
                    "false unification",
                    "rejected rather than banked",
                    "it solves a meta-problem")
