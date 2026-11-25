"""B2002's lock: both runs rerun exactly (FLINT; about 25 s each) and hold the identity and the pairing facts."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_identity_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "identity_posthoc.py")], capture_output=True, text=True, timeout=1800).stdout
    assert out == (HERE / "identity_posthoc_run.txt").read_text()
    assert out.count(": True") == 2 and out.count(": False") == 2
    assert "mod 27: neutral degree 26, charged-sector degree 23" in out and "mod 81: neutral degree 218, charged-sector degree 215" in out


def test_halving_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "halving.py")], capture_output=True, text=True, timeout=1800).stdout
    strip = lambda s: [l.split("  [")[0] for l in s.splitlines()]
    assert strip(out) == strip((HERE / "halving_run.txt").read_text())
    assert "of the neutral non-top degree 216, paired by halving: 216" in out and "of the neutral non-top degree 13, paired by halving: 0" in out
    assert "[-4672, 0, 1008, 0, -60, 0, 1]" in out and "['6', '1', '[2,', '6;', '3,', '8;', '73,', '1]']" in out
