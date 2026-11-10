"""B1221, the correction of 2026-11-10 (P-604): the kernel under rescaled charges is Z_(6k), exactly."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_the_kernel_is_cyclic_of_order_6k():
    out = subprocess.run([sys.executable, "-B", str(HERE / "kernel_under_rescaling.py")], capture_output=True, text=True,
                         check=True, timeout=600).stdout
    assert out == (HERE / "kernel_under_rescaling_run.txt").read_text(encoding="utf-8")
    lines = out.splitlines()
    assert "exact kernel order  30" in lines[4] and "6 = 6 gcd(k, 12)" in lines[4]      # k = 5: the group 30, the grid 6
    assert "only at k = 1" in lines[-3] and "row for row" in lines[-2]
