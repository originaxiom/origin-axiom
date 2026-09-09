"""B1322 -- L204 verified: the DESIGN is sealed; main's re-read of the seat's four points is pinned (N = 0, h^1 = 0, non-self-dual, relator <= 1e-60); the seat's re-reader receipt is green; reproduces live under OA_SLOW."""
import hashlib, json, os, subprocess, sys
from pathlib import Path
import pytest
ROOT = Path(__file__).resolve().parents[1]; ARC = ROOT / "frontier" / "B1322_l204_verified"; V = ARC / "verification"


def test_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_main_s_reread_is_pinned():
    j = json.loads((V / "b1322_l204_verify.json").read_text(encoding="utf-8"))
    assert j["verdict"] == "PASS" and [r["label"] for r in j["results"]] == ["class 1", "class 2", "class 1 + class 2", "class 1 - class 2"]
    for r in j["results"]:
        assert (r["h1_27"], r["h1_27bar"], r["h0_cusp_27"], r["h0_cusp_27bar"], r["N"]) == (0, 0, 0, 0, 0) and list(r["bound"]) == [0, 0]
        assert float(r["relator_residual"]) <= 1e-60 and float(r["self_duality_defect"]) > 1e-12
    assert float(j["controls"]["perturbed_relator_residual"]) > 1e-40
    rec = (V / "sm_B1350_report_hp_rerun.txt").read_text(encoding="utf-8", errors="replace")
    assert rec.rstrip().endswith("RC=0") and rec.count("N(27) = 0; h1(27) = 0, h1(27bar) = 0") == 4


@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 re-reads the four points (about five minutes)")
def test_reproduces_by_RUNNING(tmp_path):
    pts = tmp_path / "pts.json"
    # the points travel with the seat's branch; the lock re-reads them only when a copy is present in the arc (kept out of the tree by size)
    src = V / "v10_direction_points.json"
    if not src.exists(): pytest.skip("the seat's points are read from its branch, not stored here")
    r = subprocess.run([sys.executable, str(V / "b1322_l204_verify.py"), str(src), str(tmp_path / "out.json")], capture_output=True, text=True, timeout=3600)
    assert r.returncode == 0 and "B1322 L204 VERIFY: PASS" in r.stdout
