"""B1170 lock -- THE ARENA RESCOPE: cc3 B8143 + codex R019 rescope the gravity charter's G1/E2.
The forcing package is arena-generic (252/222/2, zero object tokens); the object supplies the arena.
Asserts on COMMITTED files only; the enumeration re-runs via the committed independent script.
Gate 5 clean."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1170_arena_rescope"


def _d():
    return json.loads((ARC / "b1170_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1170" and d["verdict"] == "OPEN"
    assert d["instrument"] is False and d["creates_law"] is False
    assert "ARENA" in d["claim_one_line"] and "252" in d["claim_one_line"]


def test_core_finding_252_222_2_zero_tokens():
    c = _d()["the_core_finding"]
    assert "252 contents examined, 222 killed" in c["enumeration"]
    assert "exactly 2" in c["enumeration"]
    assert "(1/6,-2/3,1/3,-1/2,1)" in c["survivors"]
    assert "ZERO object tokens" in c["token_audit"]
    assert "ALPHABET-DEPENDENT" in c["robustness"] and "minimality is NOT" in c["robustness"]


def test_verified_three_ways():
    v = _d()["verified_three_ways"]
    assert "no sympy.solve" in v["leg1_independent"] and "CONFIRMED" in v["leg1_independent"]
    assert "same 2 survivors" in v["leg2_cc3_lane"]
    assert "BYTE-IDENTICAL" in v["leg3_codex_cert"]


def test_rescope_bounded_not_withdrawn():
    r = _d()["the_rescope"]
    assert "STANDS" in r["in_derivation_STANDS"] or "load-bearing" in r["in_derivation_STANDS"]
    assert "arena-generic" in r["in_scope_NEW"]
    assert r["slogan"] == "THE OBJECT SUPPLIES THE ARENA; THE ANOMALIES SUPPLY THE CONTENT"
    assert "bounded, not withdrawn" in r["charter_consequence"]
    assert "B1160 STRENGTHENED" in r["charter_consequence"]


def test_independent_enumeration_runs_and_confirms():
    # the committed own-code enumerator actually re-derives 252/222/2 (fast: ~seconds)
    res = subprocess.run([sys.executable, str(ARC / "verification" / "independent_enumeration.py")],
                         capture_output=True, text=True, timeout=300)
    assert res.returncode == 0, res.stderr[-500:]
    assert "252 examined, 222 su3-killed, exactly 2 survivors" in res.stdout
    assert "REPRODUCES" in res.stdout


def test_reproduce_runner_committed():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in (ARC / "verification" / "independent_enumeration.py").read_text(encoding="utf-8")


def test_no_crossing_gate5_clean():
    d = _d()
    assert "No firewall crossing" in d["fences"] and "Gate 5 clean" in d["fences"]
    assert "NONE claimed" in d["fences"]
