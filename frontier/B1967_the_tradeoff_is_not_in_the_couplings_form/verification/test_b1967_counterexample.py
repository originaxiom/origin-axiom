"""B1967's lock: the saved channels, recomputed at 50 digits, give an aligned mixing (smallest diagonal >= 0.9) with both
heavy-pair ratios below 1e-2 and both m1/m2 at most 0.5, at reality 0.003, under the charge rule."""
import sys, pathlib, subprocess, re
HERE = pathlib.Path(__file__).resolve().parent


def test_the_example_holds_at_50_digits():
    out = subprocess.run([sys.executable, str(HERE / "verify_counterexample.py")], capture_output=True, text=True, cwd=HERE).stdout
    assert out.strip() == (HERE / "verify_counterexample_run.txt").read_text().strip()
    assert "r = |h.h| = 0.003" in out
    ratios = [(float(a), float(b)) for a, b in re.findall(r"m1/m2 = ([0-9.e-]+), m2/m3 = ([0-9.e-]+)", out)]
    assert len(ratios) == 2 and all(a <= 0.5 + 1e-9 and 1e-6 <= b <= 1e-2 for a, b in ratios)
    assert float(re.search(r"smallest diagonal \|V\| = ([0-9.]+)", out).group(1)) >= 0.9
