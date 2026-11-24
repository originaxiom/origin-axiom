"""B1978's lock: rerun the orbit reading and hold its counts (8 orbits of 12; 8 of 96 classes kept; 96 aligned and
hierarchical; 4 slow orbits)."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_orbits_rerun():
    out = subprocess.run([sys.executable, "-B", str(HERE / "orbits.py")], capture_output=True, text=True, timeout=300).stdout
    assert out == (HERE / "orbits_run.txt").read_text()
    assert "orbits: 8, sizes [12, 12, 12, 12, 12, 12, 12, 12]" in out and "keeps the rate class at 8 of 96" in out
    assert "SUMMARY: aligned at 96 of 96, hierarchical at 96 of 96; orbits carrying the slow 2-3 mixing: 4 of 8" in out
