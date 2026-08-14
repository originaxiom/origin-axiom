"""Locks B869 -- G4: the false-positive control.

The point: the cascade rule must NOT be an SM-generator regardless of input, or the
derivation is vacuous. These locks pin the eligibility census, the reproduction of every
banked verdict inside the generic engine, the Georgi funnel, and the two non-SM controls.
"""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B869_false_positive_control"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
C2 = RES["cell2"]
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def _menu(run, at):
    for t in C2[run]["trace"]:
        if t["at"] == at:
            return t["menu"]
    raise AssertionError(f"no node {at} in {run}")


def test_eligibility_census_21_of_31_dead_at_step0():
    c1 = RES["cell1"]
    assert (c1["total"], c1["dead_at_step0"]) == (31, 21)
    assert c1["eligible"] == ["A2", "A3", "A4", "A5", "A6", "A7", "A8", "D5", "D7", "E6"]


def test_E6_is_the_unique_exceptional_chiral_start():
    assert [a for a in RES["cell1"]["eligible"] if a in ("G2", "F4", "E6", "E7", "E8")] == ["E6"]


def test_e6_chain_reproduces_banked_B861():
    run = "E6 27 (via banked step-1 menu)"
    assert C2[run]["step1_winner"] == "SO(10)xU(1)"
    assert C2[run]["steps"] == ["so(10) + 1 u(1)", "su(5) + 2 u(1)",
                                "su(2) + su(3) + 3 u(1)"]
    assert C2[run]["endpoint"] == "su(2) + su(3) + 3 u(1)"


def test_B859_repair_reproduced_so8_top_dim_but_dead():
    """so(8)xu(1) is the max-dim option at the so(10) node and NOT registerable --
    the exact option whose h-vee error broke the handoff's cascade."""
    menu = _menu("E6 27 (via banked step-1 menu)", "so(10) + 1 u(1)")
    so8 = next(m for m in menu if "so(8)" in m["desc"])
    assert so8["dim"] == max(m["dim"] for m in menu)
    assert so8["registerable"] is False


def test_B860_bit_reproduced_su4_top_dim_but_dead():
    menu = _menu("E6 27 (via banked step-1 menu)", "su(5) + 2 u(1)")
    su4 = next(m for m in menu if "su(4)" in m["desc"])
    assert su4["dim"] == max(m["dim"] for m in menu)
    assert su4["registerable"] is False


def test_B863_termination_reproduced_at_the_SM():
    menu = _menu("E6 27 (via banked step-1 menu)", "su(2) + su(3) + 3 u(1)")
    assert menu and all(m["registerable"] is False for m in menu)


def test_georgi_funnel_descends_one_rung_at_a_time():
    assert C2["su(8) Georgi family"]["steps"] == [
        "su(8)", "su(7) + 1 u(1)", "su(6) + 2 u(1)", "su(5) + 3 u(1)",
        "su(2) + su(3) + 4 u(1)"]
    for N in (5, 6, 7, 8):
        end = C2[f"su({N}) Georgi family"]["endpoint"]
        assert end == f"su(2) + su(3) + {N - 4} u(1)", end


def test_so14_control_keeps_an_extra_su2():
    end = C2["so(14) spinor 64"]["endpoint"]
    assert end == "su(2) + su(2) + su(3) + 3 u(1)"
    assert end.count("su(2)") == 2, "NOT the SM: an extra weak factor survives"


def test_sym2_negative_control_has_no_weak_sector():
    end = C2["su(6) Sym2 family [NEGATIVE CONTROL]"]["endpoint"]
    assert end == "su(3) + 3 u(1)"
    assert "su(2)" not in end, "the rule CAN output a world with color and no weak sector"


def test_b864_echo_e6_endpoint_has_exactly_three_u1s():
    """Y + the two anomalous dials psi, chi (B864's ledger)."""
    assert C2["E6 27 (via banked step-1 menu)"]["endpoint"].endswith("3 u(1)")


def test_findings_name_the_prior_art_and_the_decomposition():
    assert "georgi" in _F and "survival hypothesis" in _F
    assert "expected, not a discovery of this arc" in _F
    assert "the cascade never selected e₆ and never needed to" in _F
    assert "not established by the cascade" in _F
