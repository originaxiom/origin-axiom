"""B1018 — locks: the runner exists with the arbiter rule; the classification stays honest."""
import json
import pathlib
import stat

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_the_runner_exists_serial_flagged_and_executable():
    p = ROOT / "scripts" / "run_suite.sh"
    assert p.is_file()
    src = p.read_text()
    assert "--serial" in src and "ARBITER RULE" in src
    assert p.stat().st_mode & stat.S_IXUSR


def test_the_arbiter_rule_is_in_practices():
    t = (ROOT / "docs" / "PRACTICES.md").read_text()
    flat = " ".join(t.lower().replace("*", "").split())
    assert "serial" in flat and "certificate of record" in flat
    assert "never shipped" in flat


def test_the_baseline_delta_classification_is_recorded():
    v = json.loads((ROOT / "frontier" / "B1018_xdist_qualification" /
                    "arc_verdict.json").read_text())
    c = v["claim_one_line"]
    assert "BASELINE-DELTA" in c and "NOT PARALLEL-UNSAFE" in c
    assert "ZERO PARALLEL-UNSAFE LOCKS" in c
    assert "bench-specific" in c, "the qualification's scope must stay bench-bound"
