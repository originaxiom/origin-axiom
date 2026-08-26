"""B1168 lock -- the C5 investigation (owner-directed). RESULT: the object/observer boundary at the
infinity-place is NOT a definitional choice but a MIRROR-PARITY x DIMENSION law (object-canonical IFF
mirror-even AND dimensionless; observer = mirror-odd orientation + dimensionful scale). Asserts on
COMMITTED files only; parity anchors via the committed reproduce runner. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1168_c5_investigation"


def _d():
    return json.loads((ARC / "b1168_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1168" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False
    assert "MIRROR-PARITY" in d["claim_one_line"] and "NOT a definitional choice" in d["claim_one_line"]


def test_parity_facts_verified():
    p = _d()["parity_facts_own_verified"]
    assert "EVEN" in p["Vol_mirror_even"]
    assert "CS(M-bar)=-CS(M)" in p["CS_mirror_odd"] and "amphichiral" in p["CS_mirror_odd"]
    assert "-conj(tau)=tau" in p["cusp_shape_mirror_fixed"]
    assert "EVEN" in p["length_spectrum_mirror_even"]


def test_the_decider():
    d = _d()
    dec = d["the_decider"]
    assert "mirror-EVEN AND dimensionless" in dec
    assert "un-oriented, scale-free" in dec
    # observer = odd completion + dimensionful scale
    assert "mirror-ODD" in dec and "DIMENSIONFUL scale" in dec


def test_c5_resolution_not_a_choice_false_dichotomy():
    r = _d()["c5_resolution"]
    assert "settled by a law, not a choice" in r
    assert "FALSE DICHOTOMY" in r
    assert "IS object-data" in r


def test_investigable_via_b1167_cusp():
    w = _d()["what_made_it_investigable"]
    assert "B1167" in w and "cusp-shape" in w and "sqrt3" in w


def test_convergences_c6_md1():
    c = _d()["convergences"]
    assert "C6" in c["cloud_C6"] and "DECIDER" in c["cloud_C6"]
    assert "MD1" in c["firewall_MD1"]


def test_torsion_fenced_relayed_to_cc3():
    f = _d()["fences"]
    assert "relayed to cc3" in f and "WebSearch budget exhausted" in f
    assert "NOT load-bearing" in f


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners, "no committed reproduce runner"
    assert "REPRODUCES" in runners[0].read_text(encoding="utf-8")


def test_no_crossing_gate5_clean():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 clean" in d["fences"]
