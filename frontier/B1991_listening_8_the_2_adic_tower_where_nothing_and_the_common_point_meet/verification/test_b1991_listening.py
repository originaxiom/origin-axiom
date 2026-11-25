"""B1991's lock: the 2-adic run reruns and holds Q1, Q2 and the levels' parting."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "listen8.py")], capture_output=True, text=True, timeout=900).stdout
    assert out == (HERE / "listen8_run.txt").read_text()
    assert "has order 6; every element a permutation matrix of the three coordinates: True" in out
    assert out.count("the same orbit: False") == 5
    assert "orbits per leaf (kappa mod 4): [(2, 4)]" in out and "orbits per leaf (kappa mod 8): [(2, 7), (6, 5)]" in out
