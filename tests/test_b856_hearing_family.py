"""Locks B856 -- the period-5 hearing law across the metallic family.

The locks that matter: that the period collapse is NONTRIVIAL (the generators have order 15, so
period 5 is not automatic), that B593's banked m=1 value is reproduced, and that the sin^2(theta_12)
reading is recorded as refuted ON KIND rather than quietly dropped.
"""
import importlib.util
import json
import math
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B856_hearing_family_law"
_SPEC = importlib.util.spec_from_file_location("b856", _D / "hearing_family.py")
b6 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(b6)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F_RAW = (_D / "FINDINGS.md").read_text(encoding="utf-8")
# Markdown wraps lines mid-sentence, so a prose lock must collapse whitespace or it fails on
# text that says exactly what it should. Third time this pattern has bitten in one session.
_F = " ".join(_F_RAW.split())

PHI = (1 + math.sqrt(5)) / 2


def test_b593_golden_value_is_reproduced():
    """If m=1 does not reproduce the banked value, nothing else here is interpretable."""
    target = 1 / (2 * PHI) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
    assert abs(b6.h(1) - target) < 1e-12
    assert RES["b593_m1_reproduced"] is True


def test_the_period_collapse_is_NONTRIVIAL():
    """THE POINT. ord(R)=ord(L)=15 and the matrix has period 15, but the form has period 5.
    Had the generators had order 5 the periodicity would be automatic and empty."""
    assert RES["order_R"] == 15 and RES["order_L"] == 15
    assert RES["matrix_period"] == 15
    assert RES["form_period"] == 5
    assert RES["period_collapse_factor"] == 3
    assert RES["collapse_is_nontrivial"] is True


def test_the_five_values_are_exact_and_golden():
    vals = RES["abs2_values"]
    assert len(vals) == 3
    assert any(abs(v - 1 / (PHI * math.sqrt(5))) < 1e-11 for v in vals)
    assert any(abs(v - PHI / math.sqrt(5)) < 1e-11 for v in vals)
    assert any(abs(v - 1.0) < 1e-11 for v in vals)
    assert RES["golden_pair_sums_to_one"] is True


def test_h_at_five_is_exactly_minus_one():
    assert RES["h_at_5_is_minus_one"] is True
    assert abs(b6.h(5) + 1) < 1e-12


def test_the_two_theta_odd_directions_are_conjugate_at_every_m():
    assert all(r["conj_of_u6"] for r in RES["rows"])


def test_Re_h_is_invariant_across_listener_directions():
    """The observer moves the phase, not the real part -- this is what 'forced' means here."""
    assert RES["Re_h_spread_over_listener_directions"] < 1e-12


def test_the_metallic_word_has_the_banked_monodromy_trace():
    """R^m L^m must be the metallic bundle monodromy: SL(2,Z) trace m^2+2 (B179)."""
    for r in RES["rows"]:
        assert r["sl2_trace"] == r["m"] ** 2 + 2
    assert RES["rows"][0]["sl2_trace"] == 3       # golden
    assert RES["rows"][1]["sl2_trace"] == 6       # silver


# ---------------------------------------------------------------------------------------
# The refutation must not be quietly dropped
# ---------------------------------------------------------------------------------------
def test_the_neutrino_reading_is_refuted_on_kind():
    """sin^2(theta) is a probability = |amplitude|^2. The kind-correct quantity is EXCLUDED."""
    s12, sig = 0.307, 0.013
    kind_correct = 1 / (PHI * math.sqrt(5))
    kind_wrong = 1 / (2 * PHI)
    assert (kind_correct - s12) / sig < -2.0, "|h|^2 must be excluded at >2 sigma"
    assert abs((kind_wrong - s12) / sig) < 0.5, "Re h is the one that matches"
    assert "REFUTED ON KIND" in _F
    assert "Computed and mistyped is still mistyped" in _F


def test_the_look_elsewhere_count_is_recorded():
    assert "at least 17" in _F
    assert "4/13" in _F and "1/π" in _F


def test_the_arc_states_it_has_no_dictionary():
    assert "No dictionary" in _F
    assert "No row waits on JUNO" in _F
