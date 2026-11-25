"""B2000's lock: the run reruns and holds the split at (3,3,3) and the fusion fractions."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_native_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "native.py")], capture_output=True, text=True, timeout=1800).stdout
    t = (HERE / "native_run.txt").read_text()
    strip = lambda s: [l.split("; max residual")[0] for l in s.splitlines()]
    assert strip(out) == strip(t)
    assert "S6 = sum_k C^k S2 C^-k: charge-basis diagonal (q = 0, 1, 2) [14, 5, 5]" in t
    assert "S12 = sum_k C^k S4 C^-k: charge-basis diagonal (q = 0, 1, 2) [28, 10, 10]" in t
    assert "S6 = sum_k C^k S2 C^-k: charge-basis diagonal (q = 0, 1, 2) [2, 2, 2]" in t
    assert "[14/3, 5/3, 5/3]" in t and "[2/3, 2/3, 2/3]" in t
    assert "= [18, 12, 6, 41, 38, 12, 51, 41, 6]/225" in t
    assert "'-2': Fraction(1, 15), '-1/phi': Fraction(2, 15), '0': Fraction(2, 15), '1': Fraction(2, 5), 'phi': Fraction(2, 15), '2': Fraction(2, 15)" in t
