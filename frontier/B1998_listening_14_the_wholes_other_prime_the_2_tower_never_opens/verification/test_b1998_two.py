"""B1998's lock: both runs rerun exactly and hold the closed 2-tower and the parity classes."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_reruns():
    for name in ("two_tower", "parity_posthoc"):
        out = subprocess.run([sys.executable, "-B", str(HERE / (name + ".py"))], capture_output=True, text=True, timeout=900).stdout
        t = (HERE / (name + "_run.txt")).read_text()
        assert [l.split("  [")[0] for l in out.splitlines()] == [l.split("  [")[0] for l in t.splitlines()]
    t = (HERE / "two_tower_run.txt").read_text()
    assert t.count("largest orbit     24") == 5 and t.count("slowest decay ratio 0.707107") == 6
    p = (HERE / "parity_posthoc_run.txt").read_text()
    assert "over the common point mod 2 (every entry even): 0 of 34" in p and "[(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]" in p
