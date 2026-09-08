"""B1299 -- THE PERIOD-2 DUALITY, VERIFIED, AND ITS ONE HOLE: the DESIGN is sealed, the subregular mismatch reproduces by RUNNING,
main's own W1/W2 points satisfy c = 1 and index 0, the seat's probe receipt is present, L204 and the B1267 correction are on main."""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1299_the_period_2_duality"; VER = ARC / "verification"


def _run(script, cwd):
    r = subprocess.run([sys.executable, str(VER / script)], capture_output=True, text=True, cwd=str(cwd))
    assert r.returncode == 0, r.stdout[-2500:] + r.stderr[-2500:]
    return r.stdout


def test_the_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")
    d = (ARC / "DESIGN.md").read_text(encoding="utf-8"); assert "Q1:" in d and "Q2:" in d and "FAIL" in d


def test_the_subregular_hole_is_exactly_one_direction_by_RUNNING(tmp_path):
    out = _run("b1299_subregular.py", tmp_path)
    assert out.rstrip().endswith("Q2: PASS"), out[-600:]
    j = json.loads((tmp_path / "b1299_subregular.json").read_text(encoding="utf-8"))
    assert j["labels"] == [2, 2, 2, 0, 2, 2] and j["e6"] == [16, 14, 10, 10, 8, 6, 4, 2] and j["w27"] == [12, 8, 4]
    assert j["sp8"] == [2, 6, 10, 14] and sorted(j["rest"]) == [4, 8, 10, 16] and j["mismatch"] == [[10, "42"]]


def test_main_s_own_W1_W2_points_satisfy_c_equals_1_and_index_0():
    rows = json.loads((VER / "b1299_w1w2_main.json").read_text(encoding="utf-8"))
    assert len(rows) >= 40 and {r["comp"] for r in rows} == {"W1", "W2"}
    assert all(abs(complex(*r["c"]) - 1) < 1e-9 and r["ninth"] < 1e-9 for r in rows)   # the DESIGN's criterion: the scalar c = 1 to 1e-9 and the ninth-trace identity; the non-scalar part is reported in the JSON (c_dev), not pinned
    assert all(r["a"][1] == 0 and r["t"][0] == 0 and r["I"] == 0 for r in rows)
    out = (VER / "b1299_w1w2_main.out").read_text(encoding="utf-8"); assert "Q1: PASS" in out and out.rstrip().endswith("RC=0")


def test_the_seat_probe_was_rerun_here_and_the_ledgers_carry_the_result():
    t = (VER / "sm_b1280_chirality_probe_w1w2_rerun.txt").read_text(encoding="utf-8")
    assert "SELFTEST: PASS" in t and t.rstrip().endswith("RC=0")
    hl = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8"); assert hl.count("| B1299 |") >= 3
    ol = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8"); assert "## L204 — THE SUBREGULAR POINT" in ol and "ONE UNPAIRED DIRECTION" in ol
    f = (ROOT / "frontier" / "B1267_the_deciding_computation" / "FINDINGS.md").read_text(encoding="utf-8"); assert "ADDENDUM 2026-09-08 (B1299" in f
