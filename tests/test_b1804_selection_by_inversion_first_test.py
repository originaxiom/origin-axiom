"""B1804 -- selection by inversion, first test (P-419).  The committed runs: the split frame's invariant classes (curves
only: det-form signature (1, 1), no pair of curves meeting in H); the holomorphic frame's conjugacy to the same lattice
action, its signature (2, 2) and its isolated CM points (one with CM by Q(sqrt5, sqrt-3))."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1804_selection_by_inversion_first_test" / "verification"


def test_the_split_frame_gives_curves_only():
    run = (V / "c1_run.txt").read_text(encoding="utf-8")
    assert run.count("Im tau = 0, Im tau' = 0") == 8 and "c1 exit 0" in run
    r3 = (V / "referee" / "r3_run.txt").read_text(encoding="utf-8")
    assert "signature (+,-,0) (1, 1, 2) -> at most a curve per flux, no point" in r3
    r4 = (V / "referee" / "r4_run.txt").read_text(encoding="utf-8")
    assert r4.count("pairs of these curves meeting at a point of H (needs M_b^-1 M_a elliptic): 0 of 28") == 2


def test_the_holomorphic_frame_is_the_same_action_and_forces_cm_points():
    r6 = (V / "referee" / "r6_run.txt").read_text(encoding="utf-8")
    assert "P*diag(A - I, I) [A - I = golden unit, det -1, commutes with A]: det 1, conjugates diag to factor-index: True" in r6
    r3 = (V / "referee" / "r3_run.txt").read_text(encoding="utf-8")
    assert "(factor-index action) inv H^2 dim 4, mixed rank 4" in r3 and "signature (+,-,0) (2, 2, 0) -> POINT possible" in r3
    r7 = (V / "referee" / "r7_run.txt").read_text(encoding="utf-8")
    assert "negative-definite pairs solved; isolated points with tau1, tau2 non-real: 18" in r7
    assert "sqrt(15)*I" in r7 and "sqrt(3)*I" in r7          # the point with CM by Q(sqrt5, sqrt-3)
