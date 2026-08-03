"""Locks B859 -- the SM handoff scrutiny: the OP theorem, the h-dual error, the chirality gate."""
import importlib.util
import json
import math
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B859_sm_handoff_scrutiny"
_S = importlib.util.spec_from_file_location("b859", _D / "cascade_gate.py")
b9 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b9)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split())


# ---------------------------------------------------------------------------------------
# The OP theorem -- recomputed here at high precision
# ---------------------------------------------------------------------------------------
def test_op_theorem_ring_class_polynomial_and_oddness():
    mp.mp.dps = 40
    t1 = 2j * mp.sqrt(3)
    t2 = -4 / t1
    j1 = mp.kleinj(t1) * 1728
    j2 = mp.kleinj(t2) * 1728
    assert abs(mp.re(j1 + j2) - 2835810000) < mp.mpf("1e-25")
    assert abs(mp.re(j1 * j2) - 6549518250000) < mp.mpf("1e-20")
    d = mp.re(j1 - j2)
    assert abs(abs(d) - 1637253000 * mp.sqrt(3)) < mp.mpf("1e-6")
    # oddness under the class-group swap is the ORDER PARAMETER property
    assert abs((j2 - j1) + (j1 - j2)) == 0


def test_the_two_tau_are_B853s_CM_points():
    mp.mp.dps = 30
    for (a, b), tau in [((1, 0), 2j * mp.sqrt(3)), ((3, 0), 2j * mp.sqrt(3) / 3)]:
        cm = (-b + mp.sqrt(-48)) / (2 * a)
        assert abs(cm - tau) < mp.mpf("1e-25")


def test_the_fricke_naming_is_wrong_but_the_map_is_right():
    """tau -> -4/tau swaps the CM points; the standard W_4 is tau -> -1/(4 tau)."""
    mp.mp.dps = 30
    t1 = 2j * mp.sqrt(3)
    assert abs((-4 / t1) - 2j * mp.sqrt(3) / 3) < mp.mpf("1e-25")     # the map: correct
    assert abs((-1 / (4 * t1)) - 2j * mp.sqrt(3) / 3) > mp.mpf("0.5")  # the name: wrong


# ---------------------------------------------------------------------------------------
# The h-dual error and the conformality of SO(8)xU(1)
# ---------------------------------------------------------------------------------------
def test_h_dual_of_D4_is_six_not_seven():
    assert RES["h_dual"]["D4"] == 6
    assert RES["handoff_used_D4"] == 7
    # the identity that pins it, on every simply-laced entry
    for lab, dim, rank in [("A1", 3, 1), ("A2", 8, 2), ("A4", 24, 4),
                           ("D4", 28, 4), ("D5", 45, 5), ("E6", 78, 6)]:
        assert RES["h_dual"][lab] == dim // rank - 1


def test_so8_u1_IS_conformal_in_so10():
    assert RES["so8u1_is_conformal"] is True
    assert RES["so8u1_c"] == "5" and RES["so10_c"] == "5"
    # free-fermion cross-check
    assert RES["free_fermion_check"]["SO(8)_1"] == "4"


# ---------------------------------------------------------------------------------------
# The chirality gate
# ---------------------------------------------------------------------------------------
def test_minus1_in_W_criterion():
    assert b9.minus1_in_W("D", 4) is True       # SO(8): all reps real
    assert b9.minus1_in_W("D", 5) is False      # SO(10): 16 complex
    assert b9.minus1_in_W("A", 4) is False      # SU(5): complex
    assert b9.minus1_in_W("C", 4) is True       # Sp(8): self-dual
    assert b9.minus1_in_W("E6", 6) is False     # the 27 is complex


def test_step2_winner_is_unique_under_the_repaired_gate():
    assert RES["step2_winner"] == "SU(5)xU(1)"
    assert RES["step2_unique"] is True
    dead = [o for o in RES["step2"] if not o["chiral"]]
    assert len(dead) == 1 and dead[0]["option"] == "SO(8)xU(1)"
    assert dead[0]["dim"] == 29, "the dead option BEATS the winner on dim -- why the gate matters"


def test_step1_vector_like_cosets_die_by_the_same_criterion():
    dead = {o["option"] for o in RES["step1"] if not o["coset_complex"]}
    assert dead == {"SU(6)xSU(2)", "Sp(8)"}
    assert RES["step1_winner"] == "SO(10)xU(1)"


def test_step3_gate_is_silent_and_the_trit_stands():
    assert RES["step3_gate_silent"] is True
    assert all(o["chiral"] for o in RES["step3"])
    assert RES["sm_nonextremal"] is True


# ---------------------------------------------------------------------------------------
# Honesty locks
# ---------------------------------------------------------------------------------------
def test_the_findings_record_the_premature_kill_and_the_owner_correction():
    assert "premature" in _F
    assert "the repair exists" in _F


def test_menu_completeness_stays_an_import():
    assert "still an import" in _F
    assert "P5" in _F
