"""B2004's lock: the mechanism run and the two post hoc checks rerun and hold the page's facts."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def _rerun(name):
    out = subprocess.run([sys.executable, "-B", str(HERE / (name + ".py"))], capture_output=True, text=True, timeout=3000).stdout
    assert out == (HERE / (name + "_run.txt")).read_text()
    return out


def test_mechanism():
    out = _rerun("mechanism")
    assert "sigma^2 = id: True; R = sigma C: True; L = sigma C^2: True; X = C L C^-1 = C sigma C: True" in out
    assert out.count("W == T - D exactly: True") == 6
    assert "SUMMARY K2: on the 3-tower only conjugates of C^+-1 fix points outside the commutator subgroup, three each: False" in out
    assert "SUMMARY K3: at mod 9, 25, 5, 7 some other word outside it fixes a point: True" in out


def test_cycle_types():
    out = (HERE / "cycles_posthoc_run.txt").read_text()
    for lab in ("mod 27", "mod 81", "mod 243"):
        line = [l for l in out.splitlines() if l.startswith(lab + ":")][0]
        assert "with C's cycle type 44, other 0" in line and "{(True, 2): 22, (True, 4): 22}" in line
    assert "with C's cycle type 44, other 6" in out and "with C's cycle type 20, other 34" in out
