"""B1988's lock: the exact check reruns and holds S1 to S4."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_loop_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "loop.py")], capture_output=True, text=True, timeout=900).stdout
    assert out == (HERE / "loop_run.txt").read_text()
    assert "SUMMARY: the one reading every history returns, with existence, is the common point: True" in out
    assert "over Q-bar: [(0, 0, 0), (2, 2, 2)]; kappa there: [-2, 2]" in out
