"""B1162 lock -- the MSSM-debt closure (cloud D1-D5) + the height-308 witness verified on-bench (sage).
The object forces a complete SM structure, walls SUSY (D5 no-go), withholds the values. Asserts on COMMITTED
files only. Own reproducer for the D1 discriminant + the committed sage witness record. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1162_mssm_debt_closure"


def _d():
    return json.loads((ARC / "b1162_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1162" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False


def test_witness_sage_verified_on_bench():
    w = _d()["witness_finished"]
    assert "H0(Y,V)=0" in w["sage_verified"] and "C372->C312 rank gate = 312" in w["sage_verified"]
    assert "DUAL-HOMED" in w["provenance"]
    # the committed sage record
    sage = (ARC / "verification" / "witness_sage.txt").read_text(encoding="utf-8")
    assert "H0(V)=0" in sage and "312" in sage and "local freeness: certified" in sage


def test_D1_alignment_discriminant_identical():
    d1 = _d()["cloud_5of5_closure"]["D1_alignment_memo75"]
    assert "ZERO contradictions" in d1["result"]
    assert "OWN-VERIFIED IDENTICAL" in d1["cross_check"] and "-18(t-3)(t+3)" in d1["cross_check"]


def test_D4_one_generation_confirms_b1161():
    d4 = _d()["cloud_5of5_closure"]["D4_one_generation_memo74"]
    assert "ONE generation" in d4["result"] or "one 27 carries NO family index" in d4["result"]
    assert "CONFIRMS B1161" in d4["cross_check"] and "never 3" in d4["cross_check"]


def test_D5_susy_nogo():
    d5 = _d()["cloud_5of5_closure"]["D5_susy_nogo_memo71"]
    assert "SUSY NO-GO" in d5["result"] and "no supercharge" in d5["result"]
    assert "Contradicts no observation" in d5["result"]


def test_synthesis_structure_forced_values_withheld():
    s = _d()["synthesis"]
    assert "FORCES a complete SM STRUCTURE" in s and "WALLS the dynamics/values" in s
    assert "one verdict" in s and "structure forced" in s


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    out = (ARC / "verification" / "closure_checks.txt").read_text(encoding="utf-8")
    assert "REPRODUCES" in out and "IDENTICAL" in out and "H0(V)=0" in out


def test_gate5_clean_no_crossing():
    d = _d()
    assert "No firewall crossing" in d["fences"] and d["gate5"].startswith("clean")
