"""B1166 lock -- cc's attack on cloud's GRAVITY_CHARTER, the two cc-assigned sub-claims.
C3 (one dilaton, not two moduli) VERIFIED; C4 (three (Z/2)^2 one torsor) REFUTATION-CANDIDATE
(free-orbit sqrt3-flavored vs being x hearing sqrt5-flavored). Asserts on COMMITTED files only;
the Galois/rigidity anchors via the committed reproduce runner. Gate 5 clean (no SM value)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1166_charter_attack"


def _d():
    return json.loads((ARC / "b1166_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1166" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False
    assert "C3" in d["claim_one_line"] and "C4" in d["claim_one_line"]


def test_c3_verified_one_dilaton():
    c3 = _d()["C3"]
    assert c3["verdict"] == "VERIFIED"
    # the phase pin: CS=0 => no free U(1); residual is the discrete mu_6
    assert "CS(m004)=0" in c3["fact1_phase_pin"] and "mu_6" in c3["fact1_phase_pin"]
    # no second modulus: Mostow rigidity
    assert "Mostow rigidity" in c3["fact2_no_second_modulus"]
    assert "R+ alone" in c3["conclusion"]


def test_c4_refutation_candidate_sqrt3_vs_sqrt5():
    c4 = _d()["C4"]
    assert c4["verdict"] == "REFUTATION-CANDIDATE"
    # free-orbit toggles sqrt3 (disc 144, only 2,3 ramify); being x hearing toggles sqrt5
    assert "sqrt3" in c4["free_orbit_is_sqrt3"] and "disc 144" in c4["free_orbit_is_sqrt3"]
    assert "sqrt5" in c4["being_hearing_is_sqrt5"] and "hearing=Q(sqrt5)" in c4["being_hearing_is_sqrt5"]
    # the discriminating fact: sqrt5 not in Q(zeta_12)
    assert "sqrt5 NOT in Q(zeta_12)" in c4["discriminating_fact"]
    assert "REFUTED for that pair" in c4["conclusion"]
    # held at candidate pending cloud's intent + the B1024 leg
    assert "cloud's intent" in c4["held_at_candidate_because"]


def test_c5_owner_c6_cloud_unchanged():
    d = _d()
    assert "terminal fork" in d["C5_owner"]
    assert "completeness check" in d["C6_cloud"] and "B1165" in d["C6_cloud"]


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners, "no committed reproduce runner"
    assert "REPRODUCES" in runners[0].read_text(encoding="utf-8")


def test_no_crossing_gate5_clean():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 clean" in d["fences"]
    assert "Not kill_graph-routed" in d["fences"]
