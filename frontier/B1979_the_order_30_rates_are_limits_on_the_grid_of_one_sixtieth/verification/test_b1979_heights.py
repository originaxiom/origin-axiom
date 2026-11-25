"""B1979's lock: the class reading reruns from the committed json and holds its counts; the committed run holds the
convergence and the 12 classes. Fails if a residual rises, a class count moves, or the lepton rate leaves 2/5."""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
T = (HERE / "heights_run.txt").read_text()


def test_convergence_and_classes():
    res = [float(x) for x in re.findall(r"grid of 1/60, \d0-\d0 at 0\.13: 864 rates; largest residual ([\d.e-]+)", T)]
    assert len(res) == 3 and res[0] > res[1] > res[2] and res[2] < 1e-4, res
    assert "R1 (20-30 at 0.13 reproduces B1977's json): largest difference 0.0e+00 over 864 rates" in T
    assert "CLASSES (rates snapped to the grid of 1/60, from 40-50): 12" in T
    assert "SUMMARY: the grid class of a point is the same on 30-40 and 40-50 at 96 of 96" in T
    sizes = sorted(int(m) for m in re.findall(r"^\s+(\d+) points:", T, re.M))
    assert sizes == [4, 4, 6, 6, 6, 6, 8, 8, 12, 12, 12, 12]
    assert "aligned (least diagonal >= 0.9) at height 40: 96 of 96; at 50: 96 of 96" in T


def test_orbit_reading_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "orbits_classes.py")], capture_output=True, text=True, timeout=300).stdout
    assert out == (HERE / "orbits_classes_run.txt").read_text()
    assert "lepton m2/m3 rate over the 96 points: [Fraction(2, 5)]" in out and "the act keeps the converged class at 8 of 96" in out
