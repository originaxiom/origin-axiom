"""B1857 -- the read-out-by-a-state checks reproduce on main's code."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_the_checks_reproduce():
    out = subprocess.run([sys.executable, "-B", str(HERE / "state_readout_check.py")], capture_output=True, text=True, check=True, timeout=900).stdout
    lines = [l for l in out.splitlines() if l.strip() and "tkinter" not in l.lower()]
    want = [l for l in (HERE / "state_readout_check_run.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert lines == want
    assert "(6,)                         apex height 3.618034 attained at 1 position(s): unique" in out
    assert out.count("degenerate (mirror)") == 2 and "excess volume 1.5714" in out
