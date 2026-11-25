"""B1986's lock: the irreducible eigenvalues and the post hoc irreducible content rerun and hold the page's table."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_irreducibles():
    t = (HERE / "listen4_run.txt").read_text()
    assert "the sign                         W+ eigenvalues -2.0000" in t
    assert "the rotation triplet 3           W+ eigenvalues 0.5000+1.3229i, 0.5000-1.3229i, 1.0000" in t
    assert "the doublet 2 (via the 3 axes)   W+ eigenvalues -1.0000, 1.0000" in t


def test_posthoc_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "irreps_posthoc.py")], capture_output=True, text=True, timeout=900).stdout
    assert out == (HERE / "irreps_posthoc_run.txt").read_text()
    assert "(8, (('1', 1), ('sign', 1), ('3', 1), (\"3'\", 1)))" in out and "(6, (('1', 1), ('2', 1), ('3', 1)))" in out
