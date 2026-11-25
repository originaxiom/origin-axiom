"""B2008's lock: the mirror run reruns exactly (it rewrites mirror_perms.json, removed after); the committed GAP run holds P3."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_mirror_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "mirror.py")], capture_output=True, text=True, timeout=1800).stdout
    (HERE / "mirror_perms.json").unlink(missing_ok=True)
    assert out == (HERE / "mirror_run.txt").read_text()
    assert "tau C tau = C^-1: True; tau sigma tau = sigma: True" in out and "all among the six: True" in out
    assert out.count("tau preserves the orbit: True; [P_tau, W] = 0.0") == 5


def test_gap_p3():
    t = (HERE / "mirror_gap_run.txt").read_text()
    assert t.count("tau in G_k: False") == 3 and t.count("(= 2 |G_k|: True); abelian invariants of <G_k, tau>: [2, 2]") == 3
