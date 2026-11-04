"""B1834 lock -- the total-inputs scoreboard (P-418, P-661): the page is current, the counts are the checker's, the
data carries no value, and an earned joint must name an existing row."""
import json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "scripts" / "checks" / "inputs_scoreboard.py"


def _run(*a):
    return subprocess.run([sys.executable, str(SCRIPT), *a], cwd=ROOT, capture_output=True, text=True, timeout=120)


def test_the_page_is_current_and_the_selftest_catches_its_planted_defects():
    r = _run("--check"); assert r.returncode == 0, r.stdout + r.stderr
    s = _run("--selftest"); assert s.returncode == 0 and "4 planted defects caught" in s.stdout, s.stdout + s.stderr


def test_the_headline_counts_are_the_checkers():
    line = _run().stdout
    assert "0 of 19 earned" in line and "identification price 13" in line
    assert "10 rows claimed, 14 borrowed joints" in line and "23 rows claimed, 45 borrowed joints" in line


def test_no_value_is_recorded():
    rx = re.compile(r"(?<![\w.^-])\d+\.\d+")
    assert rx.findall("a value 3.14 planted") == ["3.14"], "the pattern cannot see a decimal (a vacuous check)"
    for p in (ROOT / "docs" / "total_inputs_scoreboard.json", ROOT / "docs" / "TOTAL_INPUTS_SCOREBOARD.md"):
        t = p.read_text(encoding="utf-8")
        decimals = rx.findall(t)
        assert not decimals, (p.name, decimals[:5])


def test_the_mirror_joint_is_verified_not_forced():
    d = json.loads((ROOT / "docs" / "total_inputs_scoreboard.json").read_text(encoding="utf-8"))
    f7 = [j for j in d["frames"]["B"]["joints"] if j["id"] == "F7"][0]
    assert f7["type"] == "VERIFIED-BY-MAIN" and "T-FRAME-MIRROR-MATRIX" not in f7["basis"].replace("does not exist", "")


def test_the_new_sealed_ranges_are_pinned():
    ex = json.loads((ROOT / "frontier" / "B1832_the_agy_lanes_digested" / "verification" / "SEALED_EXHIBITS.json").read_text(encoding="utf-8"))
    assert len(ex) >= 52
    assert any(x["path"].endswith("toe_closure.py") and x["lines"] == "5473-5485" for x in ex)
