"""B1856 -- the level-5 Weil representation facts reproduce on main's code."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_the_weil5_check_reproduces():
    out = subprocess.run([sys.executable, "-B", str(HERE / "weil5_check.py")], capture_output=True, text=True, check=True, timeout=300).stdout
    assert out == (HERE / "weil5_check_run.txt").read_text(encoding="utf-8")
    assert "120 of 120 elements" in out and "0 clashes" in out and "= +-<LR>: True" in out and "(LR)^1" in out
