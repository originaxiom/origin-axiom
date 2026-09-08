"""B1305 slice A -- THE CLOUD 156-182: the DESIGN is sealed; the cover census (2..12), the partial-filling loop and the Klein check reproduce by
RUNNING (SnapPy); the sense census's planted controls run on main's docs and its two tree runs are pinned from JSON; the cloud receipts are present."""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1305_the_cloud_156_178"; VER = ARC / "verification"


def _run(script, cwd, args=(), timeout=1200):
    r = subprocess.run([sys.executable, str(VER / script), *args], capture_output=True, text=True, cwd=str(cwd), timeout=timeout)
    return r


def test_the_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_the_cover_census_to_degree_12_reproduces_by_RUNNING(tmp_path):
    r = _run("b1305_covers_11_12.py", tmp_path); assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "degree 11:  26 covers" in r.stdout and "degree 12:  62 covers" in r.stdout and "covers with >= 6 cusps to degree 12: 0" in r.stdout and r.stdout.rstrip().endswith("Q2(b): PASS")


def test_the_partial_filling_witness_and_27_triples_reproduce_by_RUNNING(tmp_path):
    r = _run("b1305_partial_fillings.py", tmp_path); assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "27 distinct (degree, cusps, slope) triples" in r.stdout and "CS = +0.157590041" in r.stdout and r.stdout.rstrip().endswith("Q2(c): PASS")


def test_the_klein_check_runs_and_finds_no_asserted_identity(tmp_path):
    r = _run("b1305_klein_check.py", tmp_path); assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    j = json.loads((VER / "b1305_klein_check.json").read_text(encoding="utf-8"))
    assert j["faces"] == [-15, -3, 5] and j["z12"] == [-3, -1, 3] and len(j["hits"]) == 3


def test_the_sense_census_planted_controls_pass_on_main_and_the_tree_runs_are_pinned(tmp_path):
    r = _run("b1305_sense_census.py", tmp_path, args=(str(ROOT), "--planted"), timeout=1200); assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "PLANTED CONTROLS: +1 technical with marker: 1; no marker: +0; marker outside window: +0  -> PASS" in r.stdout
    cloud = json.loads((VER / "b1305_sense_census_cloud-seat-ec15923d.json").read_text(encoding="utf-8"))["census"]["terms"]
    assert (cloud["character"]["occurrences"], cloud["character"]["technical"]) == (3474, 12) and (cloud["Chern-Simons"]["occurrences"], cloud["Chern-Simons"]["technical"]) == (73, 34)
    main = json.loads((VER / "b1305_sense_census_origin-axiom.json").read_text(encoding="utf-8"))
    assert main["two_sided"] is False and main["census"]["terms"]["logarithmic"]["technical"] == 7     # the pre-registered FAIL, pinned


def test_the_cloud_receipts_are_present():
    for f in ("cloud_memo172_sense_census_rerun_cloudtree.txt", "cloud_memo170_six_cusp_reachability_rerun.txt", "cloud_memo170_partial_filling_strict_rerun.txt", "cloud_memo170_partial_filling_repro_rerun.txt"):
        assert (VER / f).read_text(encoding="utf-8", errors="replace").rstrip().endswith("RC=0"), f
    assert "TWO-SIDED CONTROL: PASSED" in (VER / "cloud_memo172_sense_census_rerun_cloudtree.txt").read_text()


# ---------------- slice B ----------------
SB = VER / "sliceB"


def test_slice_b_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN_B.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN_B.md" in (ARC / "DESIGN_B.sha256").read_text(encoding="utf-8")


def test_the_two_ends_and_the_ratio_reproduce_by_RUNNING(tmp_path):
    r = subprocess.run([sys.executable, str(SB / "b1305_ends.py")], capture_output=True, text=True, cwd=str(tmp_path), timeout=900)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "the R-matrix route and the Habiro route agree exactly at n = 3 and n = 4" in r.stdout and "R(4_1) = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" in r.stdout
    assert "R(3_1) = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56]" in r.stdout and r.stdout.rstrip().endswith("Q1: PASS")


def test_the_blocks_growth_rates_and_census_are_pinned_from_their_runs():
    b = json.loads((SB / "b1305_blocks.json").read_text(encoding="utf-8")); assert b["ok"] and b["N"] == 20 and all(r["palindromic"] and r["lo"] == -r["expected"] and r["hi"] == r["expected"] for r in b["rows"])
    m = json.loads((SB / "b1305_mock_theta.json").read_text(encoding="utf-8")); assert m["fails"] == [] and abs(m["F0"]["c_eff"] - 1 / 7) < 5e-4 and abs(m["chi0"]["c_eff"] - 0.2) < 5e-4
    assert m["F0_first"] == [1, 1, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2, 1, 3]
    c = json.loads((SB / "b1305_sense_census_origin-axiom_excluded.json").read_text(encoding="utf-8")); assert c["two_sided"] is False   # the pre-registered second FAIL, pinned
    for f in ("cloud_trefoil_ends_rerun.txt", "cloud_table10_control_rerun.txt", "cloud_mock_theta_ceff_rerun.txt", "cloud_ceff_scaling_law_rerun.txt", "cloud_xi_recursion_fast_rerun.txt", "cloud_torus_arm_rerun.txt"):
        assert (SB / f).read_text(encoding="utf-8", errors="replace").rstrip().endswith("RC=0"), f
    assert (SB / "cloud_park_52_blocks_rerun.txt").read_text(encoding="utf-8", errors="replace").rstrip().endswith("RC=1")   # the seat's scratch dependency, recorded as such
