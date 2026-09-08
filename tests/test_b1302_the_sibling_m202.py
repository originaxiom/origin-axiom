"""B1302 -- THE SIBLING m202: the DESIGN is sealed; the exact holonomy, the census, the two-cusp index, the cusp maps and the Alexander
check reproduce by RUNNING; the signs table is pinned from its JSON; the five seat receipts are present."""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1302_the_sibling_m202"; VER = ARC / "verification"


def _run(script, cwd):
    r = subprocess.run([sys.executable, str(VER / script)], capture_output=True, text=True, cwd=str(cwd))
    assert r.returncode == 0, r.stdout[-2500:] + r.stderr[-2500:]
    return r.stdout


def test_the_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_the_exact_holonomy_census_cusp_maps_and_faces_reproduce_by_RUNNING(tmp_path):
    out = _run("m202_exact.py", tmp_path); assert out.rstrip().endswith("m202 EXACT: OK") and "tr ab = (-1 + 2*z^2)" in out
    out = _run("m202_census.py", tmp_path); assert "census: 180 word pairs (length <= 5), 12 distinct H1 actions" in out
    out = _run("b1302_cuspmaps.py", tmp_path); assert out.rstrip().endswith("Q3: PASS") and "{6: [(1, 1)], 2: [(4, 4)], 3: [(3, 3)], 1: [(0, 0)]}" in out
    out = _run("b1302_faces.py", tmp_path); assert out.rstrip().endswith("Q4: PASS") and "monomials: 7" in out and "divisible by t^2 - 3t + 1: []" in out


def test_the_two_cusp_index_has_no_twist_sector_and_half_lives_half_dies(tmp_path):
    (tmp_path / "m202_exact.json").write_text((VER / "m202_exact.json").read_text(encoding="utf-8"), encoding="utf-8")
    import shutil; shutil.copy(VER / "d2multi.py", tmp_path / "d2multi.py")
    r = subprocess.run([sys.executable, str(VER / "b1302_index.py")], capture_output=True, text=True, cwd=str(tmp_path))
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "peripheral sublattice: elementary divisors [1, 1]  index 1" in r.stdout and r.stdout.rstrip().endswith("Q2: PASS")


def test_the_signs_table_is_pinned_from_the_exact_run():
    j = json.loads((VER / "b1302_signs.json").read_text(encoding="utf-8"))
    for k in range(0, 23, 2):
        inv = j["inversion"]["k"][str(k)]; assert inv["h1"] == 2 and inv["scalar"] == ("(1)" if (k // 2 + 1) % 2 == 0 else "(-1)"), k
        r3 = j["order3"]["k"][str(k)]
        if k % 6 == 4: assert r3["scalar"] == "(1)", k
        else: assert r3["tr"] == "(-1)" and r3["det"] == "(1)" and r3["scalar"] is None, k
    out = (VER / "b1302_signs.out").read_text(encoding="utf-8"); assert "Q1: PASS" in out and out.rstrip().endswith("RC=0")


def test_the_seat_receipts_and_ledger_rows_are_present():
    for name in ("sm_b1282_siblings_faces_rerun.txt", "fc_r72_m202_snappy_rerun.txt", "fc_r72b_m202_lines_rerun.txt", "fc_r72d_census_menu_rerun.txt"):
        t = (VER / name).read_text(encoding="utf-8"); assert "SELFTEST: PASS" in t and t.rstrip().endswith("RC=0"), name
    t = (VER / "sm_b1282_sibling_germ_rerun.txt").read_text(encoding="utf-8"); assert "AssertionError" in t   # recorded as VERIFIED-DIFFERS (script)
    hl = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8"); assert hl.count("| B1302 |") >= 6
