"""B1854 -- the extrapolation reproduces from the committed run files; the control's basis invariance."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_the_extrapolation_reproduces():
    out = subprocess.run([sys.executable, "-B", str(HERE / "tube_extrapolation.py")], capture_output=True, text=True, check=True,
                         timeout=120, cwd=str(HERE)).stdout
    assert out == (HERE / "tube_extrapolation_run.txt").read_text(encoding="utf-8")
    assert "three-point 6.1491" in out and "three-point 6.0696" in out


def test_the_control_and_the_core_levels():
    c = (HERE / "driver_k1_control.log").read_text(encoding="utf-8")
    assert "covariant root: reduced -0.378771+6.147181i" in c
    assert "s0 = 0.534940" in (HERE / "driver_k2.log").read_text(encoding="utf-8")
    assert "s0 = 0.755893" in (HERE / "driver_k3.log").read_text(encoding="utf-8")
