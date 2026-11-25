"""B2006's lock: the layer run reruns exactly (about 10 s) and holds the table."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_layer_reruns():
    out = subprocess.run([sys.executable, "-B", str(HERE / "layer.py")], capture_output=True, text=True, timeout=1800).stdout
    strip = lambda s: [l.split("  [")[0] for l in s.splitlines()]
    assert strip(out) == strip((HERE / "layer_run.txt").read_text())
    assert out.count("onto: True; C- and sigma-equivariant: True") == 3
    assert "kernel order 9 " in out and "kernel order 81 " in out and "kernel order 2187 " in out
    assert out.count("(trivial: True)") == 3
    assert "abelian: True; element orders {1: 1, 3: 8}" in out and "abelian: True; element orders {1: 1, 3: 8, 9: 72}" in out and "abelian: False; element orders {1: 1, 3: 26, 9: 216, 27: 1944}" in out
