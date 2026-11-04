"""B1836 lock -- the mirror proved (T-FRAME-MIRROR), T's symmetry, the slope criterion, the theta branch, the cohomology and
the torsion, each from a committed run on main's code (main re-ran the readers' checks; outputs identical)."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent


def _t(rel):
    return (HERE / rel).read_text(encoding="utf-8")


def test_the_mirror_proof_steps_hold_and_its_controls_fail():
    out = _t("readers/C/c3_f7_mirror_proof_steps_run.txt")
    assert "basis pairs violating the identity 0 of 16" in out and "control (no channel signs) violations 8 of 16" in out
    worst = [float(x) for x in re.findall(r"a0 = 0: ([0-9.e+-]+)", out)]
    assert worst and max(worst) < 1e-12
    ctrl = re.search(r"per-sector \(b kept\) ([0-9.e+-]+); direction x e\^\{0.3i\} ([0-9.e+-]+); r = 1\+0.5i ([0-9.e+-]+)", out)
    assert ctrl and min(float(x) for x in ctrl.groups()) > 1e-2


def test_t_is_a_symmetry_of_the_outputs():
    m = re.search(r"max \|difference\| = ([0-9.e+-]+)", _t("main/t_symmetry_compute_run.txt"))
    assert m and float(m.group(1)) < 1e-10


def test_the_slope_criterion_reads_no_held_out_quantity_and_picks_two_fifths():
    out = _t("main/slope_gaps_exact_run.txt")
    assert "gaps not all equal: ['2/5']" in out and "'up': '3/20'" in out


def test_the_theta_branch_defect_is_real_and_bounded():
    out = _t("main/theta2_branch_run.txt")
    inside = [float(x) for x in re.findall(r"Re tau 0\.\d: relative deviation ([0-9.e+-]+)", out)]
    outside = [float(x) for x in re.findall(r"Re tau [12]\.\d: relative deviation ([0-9.e+-]+)", out)]
    assert inside and max(inside) < 1e-25 and outside and min(outside) > 1


def test_no_cuspidal_cohomology_at_weights_zero_to_three_and_the_torsion():
    c5 = _t("readers/C/c5_cuspidal_cohomology_run.txt")
    assert c5.count("dim H^1_cusp = 0") == 4 and c5.count("dim H^1 = 1") == 4
    c4 = _t("readers/C/c4_torsion_m004_run.txt")
    assert "|T| at t = omega = 5" in c4 and "|T| at t = -1 = 6" in c4
