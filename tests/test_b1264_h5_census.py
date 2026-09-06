"""B1264 — the H5 census and I-14's recomputed status."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1264_h5_census" / "verification" / "h5_census.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import h5_census as H
    return H


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_trinification_gradings_measured():
    H = _mod()
    lab, col = H.trinification_gradings()
    assert lab == 170 and len(col) == 85


def test_the_census_has_eight_instances_and_marks_what_is_measured():
    H = _mod()
    assert len(H.CENSUS) == 8
    measured = [c for c in H.CENSUS if c[2] is not None]
    assert len(measured) == 5, "measured vs banked-unmeasured must stay distinguished"
