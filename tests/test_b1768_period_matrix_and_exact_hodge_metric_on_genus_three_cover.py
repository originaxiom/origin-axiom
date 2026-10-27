"""Lock test for B1768: Period Matrix and Exact Hodge Metric on Genus-3 Quaternion Cover."""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ARC = ROOT / "frontier" / "B1768_period_matrix_and_exact_hodge_metric_on_genus_three_cover"
VER = ARC / "verification"


def test_b1768_files_and_verdict():
    assert (ARC / "FINDINGS.md").is_file()
    assert (ARC / "arc_verdict.json").is_file()
    assert (VER / "period_matrix_and_hodge_metric.py").is_file()
    assert (VER / "period_matrix_and_hodge_metric.json").is_file()
    assert (VER / "period_matrix_and_hodge_metric_run.txt").is_file()

    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["arc"] == "B1768"
    assert verdict["status"] == "VERIFIED"
    assert verdict["creates_law"] is False
    assert set(verdict["points"]) == {"P-395"}


def test_b1768_period_matrix_and_roots():
    data = json.loads((VER / "period_matrix_and_hodge_metric.json").read_text())
    roots = data["branch_roots"]

    # e1 is positive real ~ 6.5797
    assert abs(roots["e1"]["real"] - 6.5797) < 0.01
    # e2 and e3 are conjugate roots near -3.2899
    assert abs(roots["e2"]["real"] - (-3.2925)) < 0.01
    assert abs(roots["e3"]["real"] - (-3.2872)) < 0.01
    assert abs(roots["e2"]["imag"] + roots["e3"]["imag"]) < 1e-5

    # Period matrix determinant |det(M)| > 0
    det_abs = data["det_M"]["abs"]
    assert abs(det_abs - 6.4276) < 0.05
    assert det_abs > 1.0


def test_b1768_exact_hodge_metric():
    data = json.loads((VER / "period_matrix_and_hodge_metric.json").read_text())

    # Elliptic A-period is 1.0
    assert abs(data["elliptic_A_period"] - 1.0) < 1e-6

    # K_11 is identically 2 Im(tau_*) = 6.1101
    two_im_tau = data["two_im_tau"]
    assert abs(two_im_tau - 6.1101) < 0.001
    assert data["hodge_K_11"] == two_im_tau

    # Off-diagonals vanish identically
    assert data["hodge_K_12"] == 0.0
    assert data["hodge_K_13"] == 0.0

    # Singlet normalization factor N_1 = (2 Im tau_*)^(-1/2) = 0.404553
    singlet_norm = data["singlet_normalization"]
    assert abs(singlet_norm - 0.404553) < 1e-4
