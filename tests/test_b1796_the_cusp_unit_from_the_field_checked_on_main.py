"""B1796 -- the cusp unit from the field, checked on main.  The committed runs: (3, 3, 3) is a Fuchsian
character with commutator [[-1, 0], [-6, -1]] and is not unitary; Hitchin's equation gives |Phi| = 1/2 and the integral
pi/2; the weight-3/2 Higgs space with n uniform units is 3n (n = 0..4); the per-line table is max(0, sum m) on all 64
vectors and agrees with the seat's output."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1796_the_cusp_unit_from_the_field_checked_on_main" / "verification"


def test_w130():
    run = (V / "w130_check_run.txt").read_text(encoding="utf-8")
    assert "tr[A,B] at (3,3,3): -2" in run and "[A,B] = [[-1, 0], [-6, -1]] tr -2" in run
    assert "mu = c/v^2 solves it for c = [1/4]" in run and "curvature of mu|dz|^2: -4" in run
    assert "-> |Phi| = 1/2" in run and "= pi(-chi/2): True" in run and "w130_check exit 0" in run


def test_w123():
    run = (V / "w123_check_run.txt").read_text(encoding="utf-8")
    for n in range(5):
        assert "-> dim %d (3n = %d)" % (3 * n, 3 * n) in run
    assert "W123 (dim = 3n) holds for n = 0..4: True" in run
    assert "main's d(m) = max(0, sum m) for all: True" in run and "64 of 64" in run
    assert "d(1,0,0), d(0,1,0), d(0,0,1) = 1 1 1 | uniform: d(1,1,1) = 3" in run and "w123_check per-line exit 0" in run


def test_the_referee_routes():
    fm = (V / "referee" / "fm_route_run.txt").read_text(encoding="utf-8")
    assert "uniform n=6: d=18" in fm and "range -4..5: 1000 vectors; d(m) != max(0, sum m) at 0: []" in fm
    th = (V / "referee" / "theta_poly_run.txt").read_text(encoding="utf-8")
    assert "mismatches with max(0, sum m): []" in th and "n=2: dim=6 (3n=6)" in th
    ctl = (V / "referee" / "theta_poly_control_run.txt").read_text(encoding="utf-8")
    assert "agree: True" in ctl and "differs: True" in ctl
    ref = (V / "referee" / "w130_ref_run.txt").read_text(encoding="utf-8")
    assert "A^* H A == H: True" in ref and "w130_ref exit 0" in ref
