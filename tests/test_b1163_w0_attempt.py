"""B1163 lock -- the W0 construction attempt (owner: specialize + do the archimedean W). SEAL PARTIAL: the
obstruction is ONE datum (an object-canonical orientation of m004 = +Vol over -Vol), the object is
amphichiral so it refuses to supply it; a scale wall not a value wall; the exact bar is DEFINITIONAL (is
Mostow-canonical structure object or observer?). Firewall clean, no W0-CONSTRUCTED claimed. Committed files
only; own reproducer for the {+Vol,-Vol} orbit + Kashaev asymptotic + a1 correction. Gate 5 clean."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1163_w0_attempt"


def _d():
    return json.loads((ARC / "b1163_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_open_seal_partial():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1163" and d["verdict"] == "OPEN"
    assert _d()["seal"] == "PARTIAL"
    assert d["instrument"] is False and d["creates_law"] is False


def test_one_datum_orientation():
    d = _d()
    assert "ONE missing datum" in d["the_one_datum"] and "ORIENTATION of m004" in d["the_one_datum"]
    assert "SMUGGLES" in d["the_one_datum"] and "provably refuses" in d["the_one_datum"]


def test_one_obstruction_three_views():
    v = _d()["one_obstruction_three_views"]
    assert "free-orbit theorem" in v["arithmetic"]
    assert "-Vol exactly" in v["analytic_own_verified"] and "TWO-VALUED" in v["analytic_own_verified"]
    assert "AMPHICHIRAL" in v["geometric"] and "CS=0" in v["geometric"]


def test_validates_meditation():
    m = _d()["validates_the_meditation"]
    assert "OBSERVER's" in m["A_absence_is_observer"] and "correctly refuses" in m["A_absence_is_observer"]
    assert "SCALE wall, not a VALUE wall" in m["B_scale_not_value"]


def test_exact_bar_definitional():
    bar = _d()["the_exact_bar_DEFINITIONAL"]
    assert "DEFINITIONAL admission" in bar
    assert "OBJECT-data or OBSERVER-data" in bar
    assert "collapses onto the same admission" in bar


def test_firewall_clean_no_w0_claimed():
    f = _d()["firewall_gate5"]
    assert f.startswith("CLEAN") and "NO W0-CONSTRUCTED claimed" in f
    assert "R1 REFUTED-OBSERVER-SUPPLIED" in f


def test_r3_correction_contained():
    c = _d()["bank_grade_own_verified"]["R3_correction"]
    assert "a1 = -(11/216) sqrt-3" in c and "11/2" in c
    assert "stays in Q(sqrt-3)" in c and "survives" in c


def test_reproduce_runner_committed_and_reproduces():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")
    out = (ARC / "verification" / "w0_checks.txt").read_text(encoding="utf-8")
    assert "REPRODUCES" in out and "-2.029883212819307" in out
    assert "11/2" in out
