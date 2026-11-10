"""Pytest locks for P-753 / R77-2 (B1861 WP-2.2 & WP-3.2): Register-to-Field & Weave-Triplet Join.

Enforces:
1. Exact numerical (< 1e-12) and integer invariants of src/origin_axiom/p753_register_field_join.py.
2. Guardrail 2 (no hard-coded boolean/zero verdicts) and Guardrail 3 (Haar unitary basis-scrambling invariance).
3. Guardrail 6 (independent zero-trust referee script with zero imports from producer + tracked receipts).
4. Strict 0-of-19 data firewall and B1832 sealed-mask immunity on the relay document when present.
"""
from __future__ import annotations

import ast
import importlib.util
import json
from pathlib import Path
import re

import pytest

from origin_axiom.p753_register_field_join import TOL, run_full_p753_join


ROOT = Path(__file__).resolve().parents[1]
PRODUCER_PATH = ROOT / "src" / "origin_axiom" / "p753_register_field_join.py"
REFEREE_PATH = ROOT / "scripts" / "referee_p753_register_field_join.py"
RECEIPT_JSON = ROOT / "relays" / "p753_verification" / "p753_referee_receipt.json"
RECEIPT_TXT = ROOT / "relays" / "p753_verification" / "p753_referee_run.txt"
RELAY_MD = ROOT / "relays" / "AGY_TO_CC_2026-11-10_P753_REGISTER_TO_FIELD_JOIN.md"


@pytest.fixture(scope="module")
def p753_results() -> dict:
    return run_full_p753_join()


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
    assert bg["order_2O"] == 48
    assert bg["order_St"] == 16
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


def test_wp32_zero_mode_bundles_filtrations_and_scrambling(p753_results: dict) -> None:
    zm = p753_results["zero_mode_bundles"]
    assert zm["slot_off_block_norm"] == 0.0
    assert zm["slots_strictly_block_diagonal"] is True
    assert zm["outcome_1_irreducible_on_fixed_bg"] is False
    assert zm["all_lifts_and_signs_have_opposite_alpha_sectors"] is True
    assert zm["pole_filtration_splits_128_under_E_theta"] is True
    assert zm["szego_chi11_gamma_theta_invariance_err"] < TOL
    assert zm["vector_six_a_slot_irreducible_2_under_E_theta"] is True
    assert zm["vector_six_S_theta_swap_err"] < TOL
    assert zm["order_3branch_pure_permutation"] == 6
    assert zm["order_3branch_128_active_1form"] == 24
    assert zm["projective_order_3branch_128_active_1form"] == 24
    assert zm["braid_err_3branch_128_active_1form"] < TOL
    assert zm["order_3branch_128_spinor_fiber"] == 6
    assert zm["projective_order_3branch_128_spinor_fiber"] == 6
    assert zm["braid_err_3branch_128_spinor_fiber"] < TOL

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

    receipt = json.loads(RECEIPT_JSON.read_text(encoding="utf-8"))
    assert receipt["zero_producer_imports"] is True
    assert receipt["all_independent_checks_pass"] is True
    assert receipt["check1_e8_root_lattice_coroot"]["n_roots"] == 240
    assert receipt["check1_e8_root_lattice_coroot"]["total_e8_dim"] == 248
    assert receipt["check1_e8_root_lattice_coroot"]["coroot_phase_equivalence_max_err"] < TOL
    assert receipt["check1_e8_root_lattice_coroot"]["singlet_over_triplet_h4_ratio_set"] == [-1.0]
    assert receipt["check2_pauli_clifford_scrambled_e_theta"]["kpi_minus_total"] == 112
    assert receipt["check2_pauli_clifford_scrambled_e_theta"]["klein4_totals"] == {
        "00": 37,
        "10": 33,
        "01": 33,
        "11": 33,
    }
    assert receipt["check3_qseries_and_scrambled_cocycle"]["qseries_leading_coeff_quadrature_err"] < TOL
    assert receipt["check3_qseries_and_scrambled_cocycle"]["scrambled_order_G_T"] == 96
    assert receipt["check3_qseries_and_scrambled_cocycle"]["untwisted_Sym2_Weil2_order"] == 48
    assert receipt["check3_qseries_and_scrambled_cocycle"]["even_Z24_twist_orders"] == [24, 48, 72, 144]
    assert receipt["check3_qseries_and_scrambled_cocycle"]["odd_m3_Sym2_Weil2_bar_intertwiner_err"] < TOL
    assert receipt["check4_cauchy_contour_pole_filtration"]["filtration_and_swap_verified"] is True

    # Also execute referee's check1 + check4 live to confirm reproducibility
    spec = importlib.util.spec_from_file_location("referee_p753_mod", REFEREE_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.check_e8_root_lattice_coroot_identity()["coroot_phase_equivalence_max_err"] < TOL
    assert mod.check_elliptic_contour_pole_filtration()["filtration_and_swap_verified"] is True


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
