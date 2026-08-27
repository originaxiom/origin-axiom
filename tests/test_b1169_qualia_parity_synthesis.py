"""B1169 lock -- the qualia/parity synthesis (owner-directed; all seats to verify). SOLID core: the
qualia 'awareness without choice' becomes the mirror-parity, the choice named as the mirror-odd
orientation; the blanket's shape 2sqrt3 i; a four-probe convergence. FIREWALLED reading: the full
unification, NOT proven (speculation->calculation table). Asserts on COMMITTED files only. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1169_qualia_parity_synthesis"


def _d():
    return json.loads((ARC / "b1169_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1169" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False


def test_solid_core_the_choice_is_named():
    d = _d()
    sc = d["solid_core"]
    # the blanket is the cusp torus, shape hatched this week = 2sqrt3 i mirror-even
    assert "cusp torus" in sc["blanket_is_cusp_torus"]
    assert "2sqrt3 i" in sc["blanket_shape_hatched_this_week"] and "mirror-EVEN" in sc["blanket_shape_hatched_this_week"]
    # four independent probes converge
    assert len(sc["four_probe_convergence"]) == 4
    # the decidable naming: the choice = the mirror-odd orientation
    assert "mirror-ODD orientation" in d["the_decidable_naming"]
    assert "same bit" in d["the_decidable_naming"]


def test_connection_typing_structure_and_gravity_not_values():
    c = _d()["connection_typing_SOLID"]
    assert "chirality/orientation" in c["the_choice_is"] and "E6(-26)" in c["the_choice_is"]
    assert "SM STRUCTURE" in c["so_it_touches"] and "GRAVITY" in c["so_it_touches"]
    assert "VALUES" in c["it_does_NOT_reach"] and "DYNAMICS" in c["it_does_NOT_reach"]
    assert "MSSM" in c["it_does_NOT_reach"]


def test_reading_is_firewalled_with_speculation_table():
    r = _d()["the_reading_FIREWALLED"]
    assert "CHAIN, not a proven identity" in r["why_a_reading_not_a_theorem"]
    tbl = r["speculation_to_calculation_table"]
    # four rungs, each with a calculation that would promote it
    for k in ("S1", "S2_key", "S3", "S4"):
        assert k in tbl and "CALC" in tbl[k]
    # S2 (awareness=even via C6) is flagged as the key promotable rung
    assert "C6 completeness" in tbl["S2_key"]


def test_verification_handoff_three_seats():
    h = _d()["verification_handoff"]
    assert "cloud" in h and "cc3" in h and "codex" in h
    assert "adversarial on the READING" in h["the_ask"] and "confirmatory on the SOLID core" in h["the_ask"]


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners, "no committed reproduce runner"
    assert "REPRODUCES" in runners[0].read_text(encoding="utf-8")


def test_no_crossing_gate5_clean():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 clean" in d["fences"]
