"""B1995's lock: the exact run reruns and holds the commutation, the diagonals and the overlaps."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_charges_rerun():
    out = subprocess.run([sys.executable, "-B", str(HERE / "charges.py")], capture_output=True, text=True, timeout=900).stdout
    assert out == (HERE / "charges_run.txt").read_text()
    assert "U1: W+ commutes with s: False" in out and "U1: W+- commutes with s: False" in out
    assert "(1, [0, 1/2, 1/2])" in out and "U4: W+- top eigenvalue 2; the long-run share of each charge member <c|P_top|c>: [2/3, 2/3, 2/3]" in out
