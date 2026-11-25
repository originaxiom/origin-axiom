"""B1983's lock: the listening run and its post hoc reading rerun exactly and hold their summaries."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_reruns():
    for name in ("listen1", "leaves_posthoc"):
        out = subprocess.run([sys.executable, "-B", str(HERE / (name + ".py"))], capture_output=True, text=True, timeout=600).stdout
        assert out == (HERE / (name + "_run.txt")).read_text()
    t = (HERE / "listen1_run.txt").read_text()
    assert "SUMMARY (L, R) E1: primes p >= 5 whose cusp leaf has exactly one orbit of size > 1: 13 of 13 []" in t
    assert "SUMMARY (L, R, P) E1: primes p >= 5 whose cusp leaf has exactly one orbit of size > 1: 13 of 13 []" in t
    assert "p =  3: cusp leaf (kappa = -2) orbit sizes [1];" in t
    assert "SUMMARY (wider): integer leaves kappa in -40..40 connected at every prime 5 <= p <= 47: [-2]" in (HERE / "leaves_posthoc_run.txt").read_text()
