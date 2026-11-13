"""Pytest locks for P-753 / R77-2 (B1861 WP-2.2 & WP-3.2): Register-to-Field & Weave-Triplet Join.

Enforces:
1. Exact numerical (< 1e-12) and integer invariants of src/origin_axiom/p753_register_field_join.py.
2. Guardrail 2 (no hard-coded boolean/zero verdicts) and Guardrail 3 (Haar unitary basis-scrambling invariance).
3. Guardrail 6 (independent zero-trust referee script with zero imports from producer + tracked receipts).
4. Strict 0-of-19 data firewall and B1832 sealed-mask immunity on the relay document when present.
"""
from __future__ import annotations

import ast
import hashlib
import os
from pathlib import Path
import re
import subprocess
import sys

import pytest

from origin_axiom.p753_register_field_join import TOL, run_full_p753_join
from origin_axiom.stage1_curved_action_cusp_orbit import (
    audit_source_zero_empirical_constants,
    check_guardrail2_ast_no_literal_bool_verdicts,
)


ROOT = Path(__file__).resolve().parents[1]
PRODUCER_PATH = ROOT / "src" / "origin_axiom" / "p753_register_field_join.py"
REFEREE_PATH = ROOT / "scripts" / "referee_p753_register_field_join.py"
TEST_P753_PATH = Path(__file__).resolve()
RECEIPT_JSON = ROOT / "relays" / "p753_verification" / "p753_referee_receipt.json"
RECEIPT_TXT = ROOT / "relays" / "p753_verification" / "p753_referee_run.txt"
RELAY_MD = ROOT / "relays" / "AGY_TO_CC_2026-11-10_P753_REGISTER_TO_FIELD_JOIN.md"


@pytest.fixture(scope="module")
def p753_results() -> dict:
    return run_full_p753_join()


def test_p753_ast_firewall_and_guardrail2_locks() -> None:
    assert audit_source_zero_empirical_constants(PRODUCER_PATH) is True
    assert audit_source_zero_empirical_constants(REFEREE_PATH) is True
    assert audit_source_zero_empirical_constants(TEST_P753_PATH) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(PRODUCER_PATH.read_text(encoding="utf-8")) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(REFEREE_PATH.read_text(encoding="utf-8")) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(TEST_P753_PATH.read_text(encoding="utf-8")) is True


def test_wp32_weave_triplet_vs_sym2_weil2(p753_results: dict) -> None:
    w = p753_results["weave_triplet_and_sym2"]
    assert w["order_G_V_6D"] == 96
    assert w["order_G_T_3D"] == 96
    assert w["order_center_G_T"] == 4
    assert w["projective_order_G_T"] == 24
    assert w["order_G_M0_2D"] == 8
    assert w["order_G_Sym2_M0_3D"] == 4
    assert w["order_Weil2_2D"] == 96
    assert w["order_untwisted_Sym2_Weil2"] == 48
    assert w["untwisted_Sym2_equals_96"] is False
    assert w["even_Mp2Z_twist_orders"] == [24, 48, 72, 144]
    assert w["any_even_Mp2Z_twist_equals_96"] is False
    assert w["universal_s4_sym2_no_go_proven"] is True
    assert w["exact_cyc24_algebra_verified"] is True
    assert w["exact_f2_cocycle_and_intertwiners_verified"] is True
    assert w["b1879_exchange_doubles_96_to_192_exact"] is True

    odd_t = {(fam, m): err for fam, m, err in w["matching_odd_twists_for_T"]}
    assert set(odd_t.keys()) == {("Sym2(Weil2)", 15), ("Sym2(Weil2_bar)", 3)}
    assert all(err < TOL for err in odd_t.values())

    odd_tb = {(fam, m): err for fam, m, err in w["matching_odd_twists_for_Tbar"]}
    assert set(odd_tb.keys()) == {("Sym2(Weil2)", 21), ("Sym2(Weil2_bar)", 9)}
    assert all(err < TOL for err in odd_tb.values())

    assert w["hodge_riemann_hermitian_err"] < TOL
    assert list(w["hodge_riemann_signature"]) == [3, 3]
    assert w["subspace_invariance_err"] < TOL
    assert w["braid_holds_on_T"] is True
    assert w["braid_relation_err"] < TOL
    assert w["S_T_sq_minus_iI_err"] < TOL
    assert w["factors_through_SL2Z"] is False
    assert w["factors_through_Mp2Z"] is True
    assert w["jacobi_dedekind_covariance_err"] < TOL
    assert w["jacobi_dedekind_monomial_err"] < TOL
    assert w["jacobi_dedekind_all96_intertwiner_err"] < TOL
    assert w["monomial_T_generators_intertwine_B1611"] is True


def test_wp22_e8_background_orbit_and_coherent_lifts(p753_results: dict) -> None:
    bg = p753_results["e8_background_orbit"]
    assert bg["total_e8_dim"] == 248
    assert bg["z4_global_kernel_order"] == 4
    assert bg["z4_global_kernel_pairs"] == [(0, 0), (1, 1), (2, 2), (3, 3)]
    assert bg["spin10_spin6_mod_z4_exact"] is True
    assert bg["unbroken_u3_dim_h4"] == 9
    assert bg["unbroken_so5_dim_h1_disconnected"] == 10
    assert bg["even_spin_orbit_size"] == 3
    assert bg["x_flat_moduli_dim_h4"] == 2
    assert bg["x_flat_moduli_dim_h1"] == 0
    assert bg["x_flat_continuous_u1_sq_open"] is True
    assert bg["order_2O"] == 48
    assert bg["order_St"] == 16
    assert bg["order_2O_float_matches_exact"] is True
    assert bg["index_2O_St"] == 3
    assert bg["gL_in_St"] is False
    assert bg["gR_in_St"] is False
    assert bg["gL2_in_St"] is True
    assert bg["gS_theta_in_St"] is True
    assert bg["distinct_quartic_orbit_vectors"] == 3
    assert bg["fiber_and_holonomy_stabilizers_coincide"] is True
    assert bg["single_moves_preserve_background"] is False
    assert bg["E_theta_preserves_full_248D_background"] is True
    assert bg["X_fourth_power_identity_err"] < TOL
    assert bg["compensator_err_L2"] < TOL
    assert bg["compensator_err_S_theta"] < TOL
    assert bg["compensator_err_neg_I2"] < TOL
    assert bg["compensator_err_inn_a"] < TOL
    assert bg["compensator_err_inn_b"] < TOL
    assert bg["compensator_commutes_su3_err"] < TOL
    assert bg["kpi_minus_total"] == 112
    assert bg["klein4_totals"] == {"00": 37, "10": 33, "01": 33, "11": 33}
    assert bg["coherent_lift_equals_spin10_center_err"] < TOL
    assert bg["coherent_lifts_related_by_spin10_center"] is True

    # Independent zero-trust verification of (Spin(10) x Spin(6)) / Z_4 action on all 5 summands
    # (45 = Lambda^2(10): 2*k10 + 2*k10; 15 = 4 x bar4: 3*k6 + k6; (10,6): 2*k10 + 2*k6;
    #  (16,4): k10 + 3*k6; (bar16,bar4): 3*k10 + k6 mod 4) and centralizer dims on h_4 vs h_1:
    z4_indep = [
        (k10, k6)
        for k10 in range(4)
        for k6 in range(4)
        if ((2 * k10 + 2 * k10) % 4 == 0)
        and ((3 * k6 + k6) % 4 == 0)
        and ((2 * k10 + 2 * k6) % 4 == 0)
        and ((k10 + 3 * k6) % 4 == 0)
        and ((3 * k10 + k6) % 4 == 0)
    ]
    assert z4_indep == bg["z4_global_kernel_pairs"]
    h1_diag = [-1, 1, 1, 1, 1, 1]
    indep_so5_dim = sum(1 for i in range(6) for j in range(i + 1, 6) if h1_diag[i] * h1_diag[j] == 1)
    assert indep_so5_dim == bg["unbroken_so5_dim_h1_disconnected"]


def test_wp32_zero_mode_bundles_filtrations_and_scrambling(p753_results: dict) -> None:
    zm = p753_results["zero_mode_bundles"]
    assert zm["slot_off_block_norm"] < TOL
    assert zm["off_condensate_mixing_norm"] > (1 / 64)
    assert zm["slots_strictly_block_diagonal"] is True
    assert zm["outcome_1_irreducible_on_fixed_bg"] is False
    assert zm["all_lifts_and_signs_have_opposite_alpha_sectors"] is True
    assert zm["pole_filtration_splits_128_under_E_theta"] is True
    assert zm["szego_chi11_gamma_theta_invariance_err"] < TOL
    assert zm["aslot_128_etheta_shear_err"] < TOL
    assert zm["aslot_128_etheta_snap_err"] < TOL
    assert zm["aslot_128_chi11_joint_commutant_dim"] == 2
    assert zm["aslot_128_chi00_joint_commutant_dim"] == 2
    assert zm["aslot_128_chi11_l2_eigs_exact"] is True
    assert zm["aslot_128_chi00_l2_pullback_eigs_exact"] is True
    assert zm["vector_six_aslot_joint_commutant_dim"] == 1
    assert zm["vector_six_bare_swap_commutant_dim"] == 2
    assert zm["vector_six_a_slot_irreducible_2_under_E_theta"] is True
    assert zm["vector_six_S_theta_swap_err"] < TOL
    assert zm["order_3branch_pure_permutation"] == 6
    assert zm["order_3branch_s3_float_matches_exact"] is True
    assert zm["proxy_1form_b3_stabilizer_L2_S"] == (-1, -1)
    assert zm["order_3branch_128_proxy_1form_no_S3"] == 24
    assert zm["projective_order_3branch_128_proxy_1form_no_S3"] == 24
    assert zm["order_3branch_128_physical_phi_sp_S5"] == 96
    assert zm["order_3branch_128_physical_a_sp_S_minus3"] == 96
    assert (zm["order_3branch_128_physical_a_dp_S_minus3"] // 12, zm["order_3branch_128_physical_a_dp_S_minus3"] % 12) == (24, 0)
    assert zm["order_3branch_128_physical_psi_spin_S1"] == 72
    assert zm["projective_order_3branch_128_spinor_fiber"] == 6
    assert zm["mode_s4_signs"] == {
        "proxy_1form_no_S3": 1,
        "phi_sp_conj_weyl": -1,
        "a_sp_left_weyl": -1,
        "a_dp_left_weyl": -1,
        "psi_spin_left_weyl": -1,
    }
    assert zm["mode_commutant_dims"] == {
        "proxy_1form_no_S3": 1,
        "phi_sp_conj_weyl": 1,
        "a_sp_left_weyl": 1,
        "a_dp_left_weyl": 1,
        "psi_spin_left_weyl": 2,
    }
    assert zm["hom_weave_to_a_sp"] == 0
    assert zm["hom_weave_conj_to_a_sp"] == 1
    assert zm["hom_weave_to_phi_sp"] == 1
    assert zm["exact_cyc24_intertwiners_verified"] is True
    assert zm["pairwise_hom_dims"] == {
        "a_sp_vs_a_dp": 0,
        "a_sp_vs_psi_spin": 0,
        "a_dp_vs_psi_spin": 0,
    }
    assert zm["end_9d_commutant_dim"] == 4
    assert zm["eta3_supplies_odd_metaplectic_char_exact"] is True
    assert zm["second_lift_control_h4_minus"]["top_hol_b3"] == (1, 1)
    assert zm["b1866_physical_join_resolved_and_verified"] is True

    sc = p753_results["haar_basis_scrambling"]
    assert sc["scrambled_orders"] == [96]
    assert sc["max_trace_and_form_drift"] < TOL
    assert sc["signature_drift_count"] == 0
    assert sc["e8_spinor_colour_scramble_err"] < TOL
    assert sc["basis_scrambling_invariant"] is True


def test_independent_zero_trust_referee_and_tracked_receipts() -> None:
    assert PRODUCER_PATH.is_file()
    assert REFEREE_PATH.is_file()
    assert RECEIPT_JSON.is_file()
    assert RECEIPT_TXT.is_file()

    # Guardrail 6 AST check: referee script must not import anything from origin_axiom
    tree = ast.parse(REFEREE_PATH.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert not alias.name.startswith("origin_axiom"), f"Forbidden producer import: {alias.name}"
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            assert not mod.startswith("origin_axiom"), f"Forbidden producer import-from: {mod}"

    receipt_text = RECEIPT_JSON.read_text(encoding="utf-8")
    prod_sha = hashlib.sha256(PRODUCER_PATH.read_bytes()).hexdigest()
    ref_sha = hashlib.sha256(REFEREE_PATH.read_bytes()).hexdigest()
    assert f'"producer_sha256": "{prod_sha}"' in receipt_text
    assert f'"referee_sha256": "{ref_sha}"' in receipt_text
    assert '"zero_producer_imports": true' in receipt_text
    assert '"all_independent_checks_pass": true' in receipt_text

    # F6: Execute the ENTIRE independent referee suite live (all 5 checks) in an isolated
    # Python process with PYTHONPATH="" (zero access to src/origin_axiom) AND verify every
    # tracked receipt invariant against both the tracked JSON file and live execution:
    clean_env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    code = (
        "import importlib.util, json, pathlib;\n"
        f"p = pathlib.Path({str(REFEREE_PATH)!r});\n"
        f"rj = pathlib.Path({str(RECEIPT_JSON)!r});\n"
        "receipt = json.loads(rj.read_text(encoding='utf-8'));\n"
        "spec = importlib.util.spec_from_file_location('referee_p753_mod', p);\n"
        "mod = importlib.util.module_from_spec(spec);\n"
        "spec.loader.exec_module(mod);\n"
        "out = mod.run_independent_referee_suite();\n"
        "for d in (receipt, out):\n"
        "    assert d['zero_producer_imports'] is True\n"
        "    assert d['all_independent_checks_pass'] is True\n"
        "    assert d['check1_e8_root_lattice_coroot']['n_roots'] == 240\n"
        "    assert d['check1_e8_root_lattice_coroot']['total_e8_dim'] == 248\n"
        "    assert d['check1_e8_root_lattice_coroot']['coroot_phase_equivalence_max_err'] < 1e-12\n"
        "    assert d['check1_e8_root_lattice_coroot']['singlet_over_triplet_h4_ratio_set'] == [-1.0]\n"
        "    assert d['check2_pauli_clifford_scrambled_e_theta']['kpi_minus_total'] == 112\n"
        "    assert d['check2_pauli_clifford_scrambled_e_theta']['klein4_totals'] == {'00': 37, '10': 33, '01': 33, '11': 33}\n"
        "    assert d['check3_qseries_and_scrambled_cocycle']['qseries_leading_coeff_quadrature_err'] < 1e-12\n"
        "    assert d['check3_qseries_and_scrambled_cocycle']['scrambled_order_G_T'] == 96\n"
        "    assert d['check3_qseries_and_scrambled_cocycle']['untwisted_Sym2_Weil2_order'] == 48\n"
        "    assert d['check3_qseries_and_scrambled_cocycle']['even_Z24_twist_orders'] == [24, 48, 72, 144]\n"
        "    assert d['check3_qseries_and_scrambled_cocycle']['odd_m3_Sym2_Weil2_bar_intertwiner_err'] < 1e-12\n"
        "    assert d['check4_cauchy_contour_pole_filtration']['szego_odd_parity_err'] < 1e-12\n"
        "    assert d['check4_cauchy_contour_pole_filtration']['physical_s_minus3_offdiag_shear_err'] < 1e-12\n"
        "    assert d['check4_cauchy_contour_pole_filtration']['chi11_aslot_joint_commutant_dim'] == 2\n"
        "    assert d['check4_cauchy_contour_pole_filtration']['chi00_aslot_joint_commutant_dim'] == 2\n"
        "    assert d['check4_cauchy_contour_pole_filtration']['vector_six_aslot_joint_commutant_dim'] == 1\n"
        "    assert d['check4_cauchy_contour_pole_filtration']['filtration_and_swap_verified'] is True\n"
        "    c5 = d['check5_z4_so5_and_3branch_half_form_orders']\n"
        "    assert c5['z4_kernel_order'] == 4\n"
        "    assert c5['exact_cyc24_orders_match_float'] is True\n"
        "    assert c5['unbroken_so5_dim_h1'] == 10\n"
        "    assert c5['proxy_b3_stabilizer_L2_S'] == [-1, -1]\n"
        "    assert c5['hom_weave_to_a_sp'] == 0\n"
        "    assert c5['hom_weave_conj_to_a_sp'] == 1\n"
        "    assert c5['hom_weave_to_phi_sp'] == 1\n"
        "    assert c5['hom_phi_sp_to_a_sp'] == 0\n"
        "    assert c5['exact_cyc24_intertwiners_verified'] is True\n"
        "    assert c5['mode_commutant_dims'] == {'a_sp_S_minus3': 1, 'a_dp_S_minus3': 1, 'psi_spin_S1': 2}\n"
        "    assert c5['pairwise_hom_dims'] == {'a_sp_vs_a_dp': 0, 'a_sp_vs_psi_spin': 0, 'a_dp_vs_psi_spin': 0}\n"
        "    assert c5['end_9d_commutant_dim'] == 4\n"
        "    om = c5['orders_3branch_by_mode']\n"
        "    assert om == {'proxy_1form': 24, 'phi_sp_S5': 96, 'a_sp_S_minus3': 96, 'a_dp_S_minus3': 288, 'psi_spin_S1': 72}\n"
        "print('P753_ISOLATED_REFEREE_AND_RECEIPT_VERIFIED')"
    )
    proc = subprocess.run([sys.executable, "-c", code], env=clean_env, capture_output=True, text=True, check=True)
    assert proc.stdout.strip().splitlines()[-1] == "P753_ISOLATED_REFEREE_AND_RECEIPT_VERIFIED"


def test_relay_sealed_mask_and_hygiene_when_present() -> None:
    if not RELAY_MD.is_file():
        return
    text = RELAY_MD.read_text(encoding="utf-8")
    # 1. Seen first, E96 weave/thread tags, and 0 of 19 footer
    assert "Seen first" in text
    assert "[weave]" in text and "[thread]" in text
    assert "0 of 19." in text

    # 2. B1832 strict sealed-mask simulation:
    # "every digit hidden near a trigger word, every decimal everywhere"
    # Assert ZERO floating-point decimals (\d+\.\d+) anywhere in the relay prose!
    decimals = re.findall(r"\b\d+\.\d+\b", text)
    assert decimals == [], f"Decimals in relay would be redacted by B1832 strict mask: {decimals}"

    # Assert ZERO matches against B1832 c4_spin10_compensators.py's exact FW regex!
    b1832_fw = re.findall(
        r"y_?b\b|y_?t\b|y_?tau|m_?b\b|m_?t\b|m_?tau|tan|bottom|pdg|measur|held|level|inter|sigma_?3|ratio",
        text,
        flags=re.IGNORECASE,
    )
    assert b1832_fw == [], f"B1832 c4 FW substring found in relay: {b1832_fw}"

    # Assert ZERO SM / physics trigger words that trigger digit redaction in B1832's sealed mask!
    forbidden_triggers = re.findall(
        r"\b("
        r"quark|quarks|lepton|leptons|electron|muon|neutrino|neutrinos|"
        r"top|bottom|charm|strange|higgs|yukawa|ckm|pmns|cabibbo|weinberg|jarlskog|"
        r"gev|mev|tev|pdg|fermion|fermions|boson|bosons|mass|masses|hierarchy"
        r")\b",
        text,
        flags=re.IGNORECASE,
    )
    assert forbidden_triggers == [], f"Trigger words found in relay: {forbidden_triggers}"
