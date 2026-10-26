"""Lock for B1759 — Sector-Universal Puncture Norm Theorem and Higgs dressing probe."""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1759_sector_universal_puncture_norm_and_higgs_dressing"
VER = ARC / "verification"


def test_b1759_theorem1_and_strip_probe():
    data = json.loads((VER / "sector_universal_puncture_norm.json").read_text())
    assert data["arc"] == "B1759"
    t1 = data["theorem1_sector_universal_puncture_norm"]
    assert len(t1) == 4
    for row in t1:
        assert row["max_abs_diff_c_j_across_sectors"] < 1e-11
        assert row["max_abs_diff_c_k_across_sectors"] < 1e-11
        assert row["max_abs_diff_c_1_across_sectors"] < 1e-11
        assert row["abs_diff_c_i_down_lep"] < 1e-11
        assert row["max_abs_diff_K_down_lep"] < 1e-12
        assert row["max_abs_diff_mod_K_up_vs_down_neg"] < 1e-12
        assert row["abs_R_up_i_two_torsion"] < 1e-14
        assert 0.03 < row["c_j_minus_c_k"] < 0.05

    comps = data["strip_comparisons"]
    assert len(comps) == 4
    for row in comps:
        fit = row["b1757_fitted_L_max"]
        assert fit["overlap_hu_with_null_same"] > 0.99
        assert fit["overlap_hd_with_null_same"] > 0.99
        assert 0.009 < fit["I_u"] < 0.015
        assert 0.017 < fit["I_d"] < 0.031

        dr_half = row["boundary_dressed_DR"]["alpha_+0.5"]
        dr_one = row["boundary_dressed_DR"]["alpha_+1.0"]
        assert 0.009 < dr_half["I_off_cone"] < 0.016
        assert 0.018 < dr_one["I_off_cone"] < 0.030

        u_up = row["matter_vectors"]["up"]
        u_dn = row["matter_vectors"]["down"]
        assert u_up["abs_u_i"] < 1e-14
        assert 0.006 < u_up["I_off_cone"] < 0.009
        assert u_dn["abs_u_i"] > 0.93


def test_b1759_clean_run_log():
    txt = (VER / "sector_universal_puncture_norm_run.txt").read_text()
    assert "Traceback" not in txt
    assert "/Users/" not in txt
    assert "Wrote verification/sector_universal_puncture_norm.json successfully." in txt
