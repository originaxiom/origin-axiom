"""Lock test for B1762: Zero-Parameter Two-Doublet Law and 10-Observable Flavour Readout."""

import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ARC = ROOT / "frontier" / "B1762_zero_parameter_two_doublet_law_and_ten_observables"
VER = ARC / "verification"


def test_b1762_files_and_verdict():
    assert (ARC / "FINDINGS.md").is_file()
    assert (ARC / "arc_verdict.json").is_file()
    assert (VER / "zero_param_two_doublets.py").is_file()
    assert (VER / "zero_param_two_doublets.json").is_file()
    assert (VER / "zero_param_two_doublets_run.txt").is_file()

    verdict = json.loads((ARC / "arc_verdict.json").read_text())
    assert verdict["arc"] == "B1762"
    assert verdict["status"] == "VERIFIED"
    assert verdict["creates_law"] is False
    assert set(verdict["points"]) == {"P-329", "P-357", "P-363", "P-366", "P-377"}


def test_b1762_yukawa_gram_invariants():
    data = json.loads((VER / "zero_param_two_doublets.json").read_text())
    yg = data["yukawa_gram_invariants"]
    # Sigma^(up) off-block Frobenius norm is identically 0.0
    assert yg["max_up_gram_offblock_norm"] < 1e-14
    # Sigma^(lep) is exact parity reflection P_e1 Sigma^(down) P_e1
    assert yg["max_down_lep_parity_diff"] < 1e-14


def test_b1762_full_inverse_vs_decoupled_schur_block():
    data = json.loads((VER / "zero_param_two_doublets.json").read_text())
    # Test primary strip point tau = 0.3145 + 3.0345i
    rec = [r for r in data["strip_records"] if abs(r["tau"][0] - 0.3145) < 1e-4 and abs(r["tau"][1] - 3.0345) < 1e-4][0]
    laws = rec["laws"]

    # Full 3x3 inverse Hd gives chi2_six = 20.10, while decoupled 2x2 block degrades to 249.73 (> 12x worse!)
    assert laws["L1_boost_p1"]["chi2_six_MZ"] < 25.0
    assert laws["L1_decoupled_block_hd"]["chi2_six_MZ"] > 200.0


def test_b1762_zero_param_readout_at_geodesic_apex():
    data = json.loads((VER / "zero_param_two_doublets.json").read_text())
    # Arithmetic geodesic apex tau_* = (1 + i*sqrt(84))/3
    apex_rec = [r for r in data["strip_records"] if r["is_geodesic_apex"]][0]
    assert abs(apex_rec["tau"][0] - 1.0 / 3.0) < 1e-5
    assert abs(apex_rec["tau"][1] - math.sqrt(84.0) / 3.0) < 1e-4

    laws = apex_rec["laws"]
    floor_pnat = apex_rec["floor_2dof_pnat"]

    # Single-Higgs baseline B0 is severely excluded
    assert laws["B0_single_higgs_vdr"]["chi2_nine_MZ"] > 800.0
    assert laws["B0_single_higgs_vdr"]["pull_J_CKM"] < -20.0

    # Zero-parameter Law L3p (Schur imaginary dressing + anomalous power p_nat)
    l3p = laws["L3p_schur_im_pnat"]
    assert l3p["chi2_nine_MZ"] < 26.5
    assert l3p["chi2_nine_GUT"] < 25.5
    assert l3p["chi2_ten_GUT"] < 33.0
    # Jarlskog CP invariant within 3 sigma of PDG
    assert 2.0e-5 < l3p["abs_J_CKM"] < 3.0e-5
    assert abs(l3p["pull_J_CKM"]) < 3.0

    # L3p matches the unconstrained 2-parameter numerical floor within Delta chi2 < 0.30!
    delta_chi2_mz = l3p["chi2_nine_MZ"] - floor_pnat["chi2_nine_MZ"]
    assert 0.0 <= delta_chi2_mz < 0.30

    # Pure anomalous up-singlet dressing L2p (0 DOFs)
    l2p = laws["L2p_anomalous_up_pnat"]
    assert l2p["chi2_nine_MZ"] < 28.5
    assert l2p["chi2_nine_GUT"] < 27.5
    assert l2p["chi2_ten_GUT"] < 34.0
    assert abs(l2p["pull_J_CKM"]) < 2.6


def test_b1762_jarlskog_invariant_restoration_across_strip():
    data = json.loads((VER / "zero_param_two_doublets.json").read_text())
    for rec in data["strip_records"]:
        laws = rec["laws"]
        # Single-Higgs Jarlskog is always < 0.02e-5 (pull < -20 sigma)
        assert laws["B0_single_higgs_vdr"]["abs_J_CKM"] < 0.02e-5
        assert laws["B0_single_higgs_vdr"]["pull_J_CKM"] < -20.0

        # All zero-parameter two-doublet laws restore Jarlskog to physical (1.8-3.7)e-5
        for law_key in ("L1p_boost_pnat", "L2p_anomalous_up_pnat", "L3p_schur_im_pnat"):
            assert 1.8e-5 <= laws[law_key]["abs_J_CKM"] <= 3.7e-5

        # At im_tau = 2.95, L1p matches PDG within 0.1 sigma and L3 matches within 0.4 sigma!
        if abs(rec["tau"][1] - 2.95) < 1e-4:
            assert abs(laws["L1p_boost_pnat"]["pull_J_CKM"]) < 0.20
            assert abs(laws["L3_schur_im_p1"]["pull_J_CKM"]) < 0.50
