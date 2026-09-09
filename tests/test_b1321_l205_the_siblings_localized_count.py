"""B1321 -- L205: the DESIGN is sealed; the class search (six members, zero golden) and m202's count (3 on both cusps) are pinned; reproduces live under OA_SLOW."""
import hashlib, json, os, subprocess, sys
from pathlib import Path
import pytest
ROOT = Path(__file__).resolve().parents[1]; ARC = ROOT / "frontier" / "B1321_l205_the_siblings_localized_count"; V = ARC / "verification"


def test_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_the_class_and_the_count_are_pinned():
    j = json.loads((V / "b1321_class_search.json").read_text(encoding="utf-8"))
    assert [r["name"] for r in j["klass"]] == ["m202", "s959", "v3461", "v3551", "o9_40999", "o9_43931"] and j["golden"] == [] and j["untested"] == []
    assert j["two_cusped"] == 2750 and j["controls"]["m202_in_class_no_golden"] and j["controls"]["planted_detected"]
    assert all(r["cusps_with_3"] == [0, 1] and r.get("golden_hits") == [] for r in j["klass"])
    m = json.loads((V / "b1321_m202_count.json").read_text(encoding="utf-8"))
    assert m["localized_count_on_a_fixed_cusp"] == 3 and m["both_cusps_carry_it"] and m["equal_signs_forced_in_PW_frame"] and m["cusp_swaps"] == 0


@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 re-runs the census scan")
def test_reproduces_by_RUNNING(tmp_path):
    r = subprocess.run([sys.executable, str(V / "b1321_class_search.py")], cwd=tmp_path, capture_output=True, text=True, timeout=3600)
    assert r.returncode == 0 and "class size 6" in r.stdout and "golden-face members 0" in r.stdout, r.stdout[-1500:] + r.stderr[-1500:]
