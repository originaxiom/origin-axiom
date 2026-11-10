"""B1854 -- the extrapolation reproduces from the committed run files; the control's basis invariance."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent


def test_the_extrapolation_reproduces():
    out = subprocess.run([sys.executable, "-B", str(HERE / "tube_extrapolation.py")], capture_output=True, text=True, check=True,
                         timeout=120, cwd=str(HERE)).stdout
    assert out == (HERE / "tube_extrapolation_run.txt").read_text(encoding="utf-8")
    assert "three-point 6.1491" in out and "three-point 6.0696" in out


def test_the_control_and_the_core_levels():
    # the drivers' logs, sealed as *_run.txt: the repository ignores *.log, so the three files this lock first read were never
    # committed and it failed on a fresh clone (found by Review 77's fresh-clone suite, 2026-11-10; E94). The tracked-deps gate now
    # reads every lock's own-directory paths (tests/test_tracked_deps_locks.py)
    c = (HERE / "driver_k1_control_run.txt").read_text(encoding="utf-8")
    assert "covariant root: reduced -0.378771+6.147181i" in c
    assert "s0 = 0.534940" in (HERE / "driver_k2_run.txt").read_text(encoding="utf-8")
    k3 = (HERE / "driver_k3_run.txt").read_text(encoding="utf-8")
    assert "s0 = 0.755893" in k3
    # every k = 3 point stopped at the mesher's check: no value at k = 3
    assert k3.count("FAILED: AssertionError()") == 6

