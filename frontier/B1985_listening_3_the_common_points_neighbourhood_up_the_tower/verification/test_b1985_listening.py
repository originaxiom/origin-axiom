"""B1985's lock: the tower run and the cone check rerun exactly and hold the page's facts."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_reruns_and_facts():
    for name in ("listen3", "cone_posthoc"):
        out = subprocess.run([sys.executable, "-B", str(HERE / (name + ".py"))], capture_output=True, text=True, timeout=900).stdout
        t = (HERE / (name + "_run.txt")).read_text()
        assert [l.split("  [")[0] for l in out.splitlines()] == [l.split("  [")[0] for l in t.splitlines()]
    t = (HERE / "listen3_run.txt").read_text()
    assert "mod 9): 27 points over the common point, 4 orbits; sizes [(12, 1), (8, 1), (6, 1), (1, 1)]" in t
    assert "(1, 4, (1, 6, 8, 12), 1)" in t and "(8, 3, (72, 72, 72), 1)" in t and "(6, 0, (), 1)" in t
    c = (HERE / "cone_posthoc_run.txt").read_text()
    assert c.count("equal sets: True") == 3 and "exactly the 8 cube vertices (+-1, +-1, +-1): True" in c and "a cube vertex: True" in c
