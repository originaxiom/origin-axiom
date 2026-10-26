"""Lock test for B1761: Data-Free 2-Torsion Line-Selection Theorem and Yukawa-Gram Higgs Dressing Probe."""

import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ARC = ROOT / "frontier" / "B1761_two_torsion_line_selection_and_schur_higgs_probe"
VER = ARC / "verification"


def test_b1761_files_and_verdict():
    assert (ARC / "FINDINGS.md").is_file()
    assert (ARC / "arc_verdict.json").is_file()
    assert (VER / "two_torsion_and_schur_higgs.py").is_file()
    assert (VER / "two_torsion_and_schur_higgs.json").is_file()
    assert (VER / "two_torsion_and_schur_higgs_run.txt").is_file()

    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["arc"] == "B1761"
    assert verdict["status"] == "VERIFIED"
    assert set(verdict["points"]) == {"P-349", "P-357", "P-366", "P-373", "P-377", "P-384"}


def test_b1761_attack2_line_selection_across_662_lines():
    data = json.loads((VER / "two_torsion_and_schur_higgs.json").read_text())
    a2 = data["attack2_line_selection"]
    assert a2["total_lines_tested"] == 662
    assert a2["n_lines_N_le_12"] == 266
    assert a2["n_lines_N_13_to_20"] == 396

    # Condition C1 alone (asymmetric 2-torsion e1-kernel) selects exclusively 10 lines out of 662, all of order N=10
    assert a2["c1_survivor_count"] == 10
    for row in a2["c1_survivors"]:
        assert row["group"] == "N<=12"
        assert row["N"] == 10
        assert row["a"] in ("1/5", "2/5")
        assert row["b"] in ("1/10", "3/10", "1/2", "7/10", "9/10")
        assert row["abs_R_u_i"] < 1e-12
        assert row["abs_R_d_i"] > 1e-4

    # Condition C1 + C2 (up-sector isotropic proximity I(u_up) < 0.05) uniquely selects the 5-line T-orbit a = 2/5, 10b odd
    assert a2["c1_c2_survivor_count"] == 5
    b_vals = []
    for row in a2["c1_c2_survivors"]:
        assert row["a"] == "2/5"
        assert row["N"] == 10
        assert row["up_off_cone_invariant_I"] < 0.007
        assert row["up_doublet_over_scalar"] > 12.0
        b_vals.append(row["b"])
    assert sorted(b_vals) == sorted(["1/10", "3/10", "1/2", "7/10", "9/10"])


def test_b1761_attack1_yukawa_gram_and_schur_higgs_strip():
    data = json.loads((VER / "two_torsion_and_schur_higgs.json").read_text())
    a1 = data["attack1_schur_gram_strip"]
    assert len(a1) == 4

    for pt in a1:
        # Exact 1+2 block-diagonalization of Sigma^(up) and exact e1-parity between Sigma^(down) and Sigma^(lep)
        assert pt["up_off_block_norm"] < 1e-15
        assert pt["down_lep_parity_diff"] < 1e-14
        # Stable 2-DOF zeta_u branch across the strip
        assert 0.09 < pt["zeta_u_2dof_abs"] < 0.12
        assert 34.0 < pt["zeta_u_2dof_arg_deg"] < 39.0
        assert pt["chi2_2dof_zeta_u_with_inv_gram_hd"] < 42.0
        assert pt["chi2_3dof_beta_zeta_u"] < 28.0

    # At primary census point tau = 0.3145 + 3.0345i:
    pt0 = a1[0]
    assert pt0["tau"] == [0.3145, 3.0345]
    assert pt0["overlap_hd_opt_vs_inv_gram"] > 0.99996
    assert pt0["angle_hd_opt_vs_inv_gram_deg"] < 0.5
    assert pt0["chi2_hu_opt_with_schur0_hd12"] < 20.0
    # At tau = 0.3145 + 3.10i, 3-DOF Gram-dressed fit beats B1757's 8-DOF fit (23.82 < 29.17)
    pt2 = a1[2]
    assert pt2["tau"] == [0.3145, 3.1]
    assert pt2["chi2_3dof_beta_zeta_u"] < pt2["chi2_8dof_b1757"]
