"""B1719 -- W122 on main (P-269). Stored: main's isometry check (Weeks from b+-LR only; Meyerhoff from both). Live: the
check re-run (SnapPy) without writing."""
import json, pathlib, subprocess, sys
import pytest
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1719_w122_on_main" / "verification"


def test_stored():
    d = json.loads((A / "main_check.json").read_text(encoding="utf-8"))
    m3, m4 = d["b+-LR"]["least_four"], d["b++LR"]["least_four"]
    assert [x["is"] for x in m3[:2]] == ["Weeks", "Weeks"] and abs(m3[0]["vol"] - 0.9427073628) < 1e-9
    assert m4[0]["is"] == "Meyerhoff" and all(x["is"] != "Weeks" for x in m4)
    assert "R1 0.942707363 ['b+-LR'] ['m003(-3,1)'] -> True" in (A / "reproduce" / "the_closed_universes_run.txt").read_text(encoding="utf-8")


def test_live():
    pytest.importorskip("snappy")
    r = subprocess.run([sys.executable, "-B", str(A / "main_check.py"), "--check"], capture_output=True, text=True, cwd=str(A), timeout=900)
    assert r.returncode == 0, r.stderr[-400:]
    out = json.loads(r.stdout[r.stdout.index("{"):])
    assert out["b+-LR"]["least_four"][0]["is"] == "Weeks" and out["b++LR"]["least_four"][0]["is"] == "Meyerhoff"
