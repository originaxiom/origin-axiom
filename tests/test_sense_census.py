"""B1307 lock -- the adopted sense census: the three planted MB12 controls pass (`--selftest`), the self-naming exclusion is a
run-time computation (a file naming the instrument is dropped; one that does not is kept), and the two pre-registered routes'
receipts are pinned (Route A PASS on HEAD, Route B PASS at 31dd52b9)."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SC = ROOT / "scripts" / "checks" / "sense_census.py"
V = ROOT / "frontier" / "B1307_the_harvest_gate" / "verification"


def test_selftest_planted_controls():
    r = subprocess.run([sys.executable, str(SC), "--selftest"], capture_output=True, text=True, timeout=900)
    assert r.returncode == 0 and "-> PASS" in r.stdout, r.stdout + r.stderr


def test_self_naming_exclusion_is_computed(tmp_path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("sense_census", SC); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    (tmp_path / "docs").mkdir(); (tmp_path / "frontier").mkdir(); (tmp_path / "papers").mkdir()
    (tmp_path / "docs" / "A.md").write_text("the sense census says logarithmic CFT here", encoding="utf-8")
    (tmp_path / "docs" / "B.md").write_text("a logarithmic CFT appears in this file", encoding="utf-8")
    res = m.census(str(tmp_path))
    assert res["excluded"] == ["docs/A.md"] and res["files"] == 1
    assert res["terms"]["logarithmic"]["occurrences"] == 1 and res["terms"]["logarithmic"]["technical"] == 1


def test_the_two_routes_are_pinned():
    a = json.loads((V / "sense_census_routeA.json").read_text(encoding="utf-8"))
    assert a["verdict"] == "PASS" and a["two_sided"] is True and a["planted"]["ok"] is True
    assert a["census"]["terms"]["logarithmic"]["technical"] == 0 and a["census"]["terms"]["Chern-Simons"]["verdict"] == "genuine"
    b = (V / "sense_census_routeB.txt").read_text(encoding="utf-8")
    assert "TWO-SIDED: PASSED" in b and "-> PASS" in b and "oa-31dd52b9" in b
