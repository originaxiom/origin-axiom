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
