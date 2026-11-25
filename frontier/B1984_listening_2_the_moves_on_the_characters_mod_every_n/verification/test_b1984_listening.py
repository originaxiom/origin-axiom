"""B1984's lock: the listening run's summaries and the post hoc readings rerun exactly."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_post_hoc_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "common_point_posthoc.py")], capture_output=True, text=True, timeout=900).stdout
    assert out == (HERE / "common_point_posthoc_run.txt").read_text()
    assert out.count("every orbit is a CRT product of prime-power orbits: True") == 6
    assert out.count("has order 24") == 3 and out.count("correspond one to one: True") == 3
    assert "orbits by cube type: [(1, ['centre']), (6, ['face']), (8, ['vertex']), (12, ['edge'])]" in out


def test_run_summaries():
    t = (HERE / "listen2_run.txt").read_text()
    assert "SUMMARY C1: primes 5..47 connected: True; N = 3 cusp leaf [1]" in t
    assert "not: [25, 35, 49, 55]" in t
