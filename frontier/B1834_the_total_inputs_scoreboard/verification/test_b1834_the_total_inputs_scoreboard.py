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
    # 2026-11-04 (S301, B1836): B47's torsion verified on main (VERIFIED-BY-MAIN), frame B 45 -> 44
    assert "10 rows claimed, 14 borrowed joints" in line and "23 rows claimed, 44 borrowed joints" in line


def test_no_value_is_recorded():
    rx = re.compile(r"(?<![\w.^-])\d+\.\d+")
    assert rx.findall("a value 3.14 planted") == ["3.14"], "the pattern cannot see a decimal (a vacuous check)"
    for p in (ROOT / "docs" / "total_inputs_scoreboard.json", ROOT / "docs" / "TOTAL_INPUTS_SCOREBOARD.md"):
        t = p.read_text(encoding="utf-8")
        decimals = rx.findall(t)
        assert not decimals, (p.name, decimals[:5])


def test_the_mirror_joint_is_proved_on_main():
    """S300c: the reader cited a theorem row that did not exist, so F7 was typed VERIFIED-BY-MAIN; S301 (B1836) proved it:
    T-FRAME-MIRROR, an existing registry row, so F7 is FORCED-BY-MAIN"""
    d = json.loads((ROOT / "docs" / "total_inputs_scoreboard.json").read_text(encoding="utf-8"))
    f7 = [j for j in d["frames"]["B"]["joints"] if j["id"] == "F7"][0]
    assert f7["type"] == "FORCED-BY-MAIN" and "T-FRAME-MIRROR" in f7["basis"]
    assert "| T-FRAME-MIRROR |" in (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")


def test_the_new_sealed_ranges_are_pinned():
    ex = json.loads((ROOT / "frontier" / "B1832_the_agy_lanes_digested" / "verification" / "SEALED_EXHIBITS.json").read_text(encoding="utf-8"))
    assert len(ex) >= 52
    assert any(x["path"].endswith("toe_closure.py") and x["lines"] == "5473-5485" for x in ex)
