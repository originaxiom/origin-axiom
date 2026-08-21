"""B1104 locks — the 4d suspension selection test (L177).

Fast: the stored results' verdict-bearing facts re-asserted. Live: the full
computation re-run (SnapPy m004 symmetry group + exact table arithmetic,
~10 s) and compared to the stored verdicts.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1104_fourd_suspension"


def _res():
    return json.load(open(ARC / "b1104_results.json", encoding="utf-8"))


def test_stored_verdicts():
    r = _res()
    assert r["element_orders"] == [1, 2, 2, 2, 2, 2, 4, 4]
    assert r["cusp_kernel_size"] == 2, "the non-faithfulness finding must stay recorded"
    assert r["hom_certified"] is True
    assert r["conjugacy_class_sizes"] == [1, 1, 2, 2, 2]
    assert r["center_elements"] == 2
    f = r["filters"]
    assert f["theta_center_nontrivial"] == 1
    assert f["tick_or_reversing_involutions"] == 2
    assert f["joint_survivors"] == 0, "the empty joint set IS the no-section witness"
    assert r["C1_escalator_repeat"] is False
    assert r["C2_selection"] == "NO-SECTION"
    assert r["C3_gieseking_analog"] is True


def test_gieseking_analog_rows():
    r = _res()
    ticks = [row for row in r["rows"] if row["det"] == -1 and row["order"] == 2]
    assert len(ticks) == 2
    for row in ticks:
        assert row["suspension_orientable"] is False
        assert row["H1_suspension"] == "Z^2"


def test_live_recompute_matches():
    p = subprocess.run([sys.executable, str(ARC / "b1104_selection.py")],
                       capture_output=True, text=True, cwd=str(ROOT), timeout=300)
    assert p.returncode == 0, p.stderr[-500:]
    out = p.stdout
    assert "C1 False | C2 NO-SECTION | C3 True" in out
    assert "cusp kernel 2" in out
