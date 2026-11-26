"""B1993's lock: the committed runs hold M1, M2 and the two orbits; integers.py (about 25 s) is rerun and must reproduce its
committed run (added at Review 87, 2026-11-26: a reader found the lock read text only)."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_integers():
    t = (HERE / "integers_run.txt").read_text()
    assert "M1: every solution has all entries = 0 mod 3: True" in t
    assert "reached from (3, 3, 3) by L, R, L^-1, R^-1 within the box: 70; all: True" in t
    s = (HERE / "signs_posthoc_run.txt").read_text()
    assert "the other 210 readings fall into 1 orbit(s) of sizes [210]; each mixes the three patterns with two negatives: True" in s


def test_integers_rerun():
    out = subprocess.run([sys.executable, "-B", str(HERE / "integers.py")], capture_output=True, text=True, timeout=300).stdout
    assert out == (HERE / "integers_run.txt").read_text()
