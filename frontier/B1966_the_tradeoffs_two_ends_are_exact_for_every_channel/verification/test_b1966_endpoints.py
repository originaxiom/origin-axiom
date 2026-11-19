"""B1966's lock: the exact identities and the reduction to B1727's form, re-run, equal the kept run."""
import sys, pathlib, subprocess
HERE = pathlib.Path(__file__).resolve().parent


def test_the_endpoints_rerun_equal_the_kept_run():
    out = subprocess.run([sys.executable, str(HERE / "endpoints.py")], capture_output=True, text=True, cwd=HERE).stdout
    assert out.strip() == (HERE / "endpoints_run.txt").read_text().strip()
    assert "E1: Y h - (h.h) u = Matrix([[0, 0, 0]]); h^T Y - (h.h) u^T = Matrix([[0, 0, 0]])" in out
    assert "for a rotation R: True" in out and "its symmetric part is a multiple of 1: True" in out
    assert out.count("ratio 2.000000000000") == 5
