"""B1164 lock -- cc's part of the A-E masterplan: MA2 (observer freedom = 2 discrete + 1 continuous bits, all
archimedean; the sqrt5->sqrt3 correction), MD1 (the firewall pin, principled+falsifiable, sec-D settled), ME3
(the phase route to W0 is closed -- pruned to modulus-only), + the sec-E gravity placement. Committed files
only; own reproducer for the V4 count + sqrt3 correction + ME3 phase. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1164_cc_masterplan"


def _d():
    return json.loads((ARC / "b1164_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1164" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False


def test_MA2_two_discrete_one_continuous():
    m = _d()["MA2_observer_bit_census"]
    assert m["count"].startswith("2 DISCRETE + 1 CONTINUOUS")
    assert "sqrt-3" in m["bit1_orientation"] and "sqrt3" in m["bit2_sqrt3"]
    assert "UNDERCOUNT" in m["correction_to_meditation"] and "ONE LEG" in m["correction_to_meditation"]


def test_MA2_sqrt5_corrected_to_sqrt3():
    c = _d()["MA2_observer_bit_census"]["correction_to_workflow"]
    assert "sqrt5" in c and "WRONG" in c
    assert "sqrt5 is NOT among them" in c and "bit2 = sqrt3" in c


def test_MD1_firewall_principled_falsifiable():
    m = _d()["MD1_firewall_pin"]
    assert "STRUCTURE iff dim=dimensionless AND prov=forced" in m["classifier"]
    assert "PROVENANCE" in m["discriminator"]
    assert "ZERO exceptions" in m["corpus_test"]
    assert "16sigma" in m["outcome_independent"] and "B915" in m["outcome_independent"]
    assert "PRINCIPLED" in m["falsifier"] and "DISCHARGES meditation sec-D" in m["falsifier"]


def test_ME3_phase_does_not_break_orbit():
    m = _d()["ME3_phase_orbit_split"]
    assert m["verdict"].startswith("does-NOT-break-orbit")
    assert "Galois-INVARIANT" in m["arithmetic"] and "zero selectivity" in m["arithmetic"]
    assert "modulus-only" in m["relay_to_cloud"]


def test_secE_gravity_placement_not_identification():
    e = _d()["secE_gravity_placement"]
    assert "ARCHIMEDEAN" in e["signal"] and "gravity live" in e["signal"]
    assert "PLACEMENT established" in e["conclusion"]
    assert "NOT a banked result" in e["not_banked"] and "HYPOTHESIS" in e["not_banked"]


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    out = (ARC / "verification" / "masterplan_checks.txt").read_text(encoding="utf-8")
    assert "REPRODUCES" in out
    assert "V4 = (Z/2)^2 => 2 DISCRETE bits" in out and "sqrt5 is NOT a subfield" in out


def test_gate5_clean_residues_flagged():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 clean" in d["fences"]
    assert "UNPROVEN residues" in d["fences"]
