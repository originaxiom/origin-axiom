"""Locks B871 -- G5: registering as a B599 pairing datum."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B871_registering_datum"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")
ROWS = {(r["step"], r["option"]): r for r in RES["rows"]}


def test_keystone_equivalence_on_every_row():
    assert RES["keystone_equivalence"] is True
    assert len(RES["rows"]) == 8


def test_the_two_failures_have_all_zero_evaluations():
    for key in (("step1_E6", "Sp(8)"), ("step3_SU5", "SU(4)xU(1)")):
        assert ROWS[key]["register_exists"] is False
        assert ROWS[key]["max_abs_eval"] == 0


def test_the_sm_registers_with_amplitude_two():
    assert ROWS[("step3_SU5", "SM")]["max_abs_eval"] == 2


def test_evaluation_is_odd_under_the_swap():
    assert RES["swap_oddness_all_rows"] is True


def test_b599_parity_even_part_blind_odd_part_carries():
    assert RES["b599_parity_all_rows"] is True


def test_criterion_can_fail_and_can_pass():
    """MB12: the definition is non-vacuous in both directions."""
    assert RES["can_fail"] is True and RES["can_pass"] is True


def test_j6_epsilon_reverified_over_Z():
    assert RES["j6_epsilon_intertwines"] is True


def test_findings_state_the_remaining_refinement():
    assert "the stage-internal refinement remains" in _F
    assert "p5 (menu completeness) alone" in _F
    assert "n = 2, the b593 shape" in _F
