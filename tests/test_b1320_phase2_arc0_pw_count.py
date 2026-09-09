"""B1320 -- Phase 2 Arc 0: the DESIGN is sealed; the localized-count record is pinned (C_3, C_4 give {0, 4}; the m202 control sees a 3); the run reproduces live under OA_SLOW."""
import hashlib, json, os, subprocess, sys
from pathlib import Path
import pytest
ROOT = Path(__file__).resolve().parents[1]; ARC = ROOT / "frontier" / "B1320_phase2_arc0_pw_count"; V = ARC / "verification"


def test_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_the_record_is_pinned():
    j = json.loads((V / "b1320_arc0_pw_count.json").read_text(encoding="utf-8"))
    assert j["pass"] is True and j["cyclic_values"] == [0, 4]
    cyc = {k: v for k, v in j["covers"].items() if v["type"] == "cyclic"}
    assert sorted(v["H1"] for v in cyc.values()) == ["Z/3 + Z/15 + Z", "Z/4 + Z/4 + Z"]
    assert all(v["values_orientation_preserving"] == [0, 4] and v["cusps"] == 1 for v in cyc.values())
    assert j["control"]["name"] == "m202" and j["control"]["example"]["det_AmI"] == 3 and j["control"]["example"]["order"] == 3
    assert j["base"]["summary"] == {"0|det-1": 4, "4|det+1": 2, "0|det+1": 2}


@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 re-runs the SnapPy scan (about a minute)")
def test_reproduces_by_RUNNING(tmp_path):
    r = subprocess.run([sys.executable, str(V / "b1320_arc0_pw_count.py")], cwd=tmp_path, capture_output=True, text=True, timeout=1800)
    assert r.returncode == 0 and "PASS (subset of {0,2,4}; the control sees a 3)" in r.stdout, r.stdout[-1500:] + r.stderr[-1500:]
