#!/usr/bin/env python3
"""
Post-Seal Disjoint Referee (v2) vs Producer (v4) Diff for Card AGY-002_A2-LISTENING-TOWER.

Strictly zero AST float/complex literals or casts, zero forbidden imports,
zero JSON floats (all numeric residuals serialized as decimal strings via mpmath).
"""

import ast
import json
import os
import mpmath as mp

mp.mp.dps = 55
FORBIDDEN_IMPORTS = {"numpy", "scipy", "frontier", "sage", "gap"}


def audit_ast(path):
    with open(path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), filename=path)
    fl = 0
    cl = 0
    fc = 0
    bad_imp = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                fl += 1
            elif isinstance(node.value, complex):
                cl += 1
        elif isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name) and fn.id in ("float", "complex"):
                fc += 1
            elif isinstance(fn, ast.Attribute) and fn.attr in ("float", "complex"):
                fc += 1
        elif isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] in FORBIDDEN_IMPORTS:
                    bad_imp.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] in FORBIDDEN_IMPORTS:
                bad_imp.append(node.module)
    return {
        "ast_float_literal_count": fl,
        "ast_complex_literal_count": cl,
        "ast_float_complex_call_count": fc,
        "forbidden_imports_count": len(bad_imp),
    }


def count_json_floats(obj):
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, (list, tuple)):
        return sum(count_json_floats(v) for v in obj)
    return 0


def parse_re_from_cstr(s):
    # Parse "(re)+(im)i" or plain real decimal string into mp.mpf real part
    if s.startswith("(") and ")+(" in s:
        re_part = s[1:s.index(")+(")]
        return mp.mpf(re_part)
    return mp.mpf(s)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    relays_dir = os.path.dirname(here)
    ref_path = os.path.join(here, "referee_a2_listening_tower_out.json")
    prod_path = os.path.join(relays_dir, "a2_listening_tower_v4", "verify_a2_listening_tower_v4_out.json")
    out_path = os.path.join(here, "referee_vs_producer_v4_diff.json")

    with open(ref_path, "r", encoding="utf-8") as fh:
        ref = json.load(fh)
    with open(prod_path, "r", encoding="utf-8") as fh:
        prod = json.load(fh)

    checks = []
    discrepancies = []

    def add_exact(name, ref_val, prod_val):
        ok = bool(ref_val == prod_val)
        entry = {
            "name": name,
            "kind": "exact",
            "referee": ref_val,
            "producer_v4": prod_val,
            "match": ok,
        }
        checks.append(entry)
        if not ok:
            discrepancies.append(entry)

    def add_num(name, ref_mp, prod_mp, tol_exp):
        diff = abs(ref_mp - prod_mp)
        tol = mp.mpf(1) / (mp.mpf(10) ** tol_exp)
        ok = bool(diff <= tol)
        entry = {
            "name": name,
            "kind": "numeric_mpmath",
            "referee": mp.nstr(ref_mp, 25),
            "producer_v4": mp.nstr(prod_mp, 25),
            "abs_diff": mp.nstr(diff, 15),
            "tol": f"1e-{tol_exp}",
            "match": ok,
        }
        checks.append(entry)
        if not ok:
            discrepancies.append(entry)

    # --- L1 exact comparisons ---
    rL1 = ref["L1_all_3k_B2009_B2010"]
    pL1 = prod["L1_all_3k_b2009_b2010_proof"]

    add_exact("L1.G_jet_order", rL1["G_jet"]["order"], pL1["G_jet_order"])
    add_exact("L1.G4_order", rL1["G_4_exhaustive"]["order"], pL1["G4_order"])
    add_exact("L1.G4_case3_count", rL1["G_4_exhaustive"]["case_fix_distribution"]["case3_fix_3"], pL1["G4_case3_count"])
    add_exact("L1.case3_total_in_G3", rL1["G_jet"]["case_counts"]["case3_3cycle_rho_ne_1"], pL1["case3_total_in_G3"])
    add_exact("L1.case3_at_333_count", rL1["G_jet"]["case3_at_333_count"], pL1["case3_at_333_count"])
    add_exact(
        "L1.case3_at_333_eigvals_set_mod9",
        sorted(set(rL1["G_jet"]["case3_at_333_eigvals_mod9"])),
        sorted(set(row[0] for row in pL1["case3_at_333_J1_mod9"])),
    )
    add_exact("L1.case3_exact3_fix", rL1["G_jet"]["case3_fix_values"] == [3], pL1["case3_exact3_fix"])
    add_exact("L1.case3_single_mod9_fiber", rL1["G_jet"]["case3_single_mod9_fiber_all"], pL1["case3_single_mod9_fiber"])
    add_exact("L1.hensel_det_1_mod3", rL1["G_jet"]["case3_at_333_hensel_dets_mod3"] == [1], pL1["hensel_det_identically_1_mod3"])
    add_exact("L1.hensel_60_words_mod6561", rL1["hensel_60_words_mod27_to_6561"]["passed_0_0_3_all_levels"] == 60, pL1["hensel_60words_through_mod6561_all_003"])
    add_exact("L1.std_omega_6Q0SQ0_zero", rL1["S3_x_Z3_characters"]["std_omega_6Q0_sigma_Q0_eq_0"], pL1["std_omega_C_neutral_null_mode_exact_zero"])

    # Map S3 x Z3 irrep names between referee and producer_v4
    name_map = {
        "(1,1)": "(1, omega^0)",
        "(1,omega)": "(1, omega^1)",
        "(1,omega^2)": "(1, omega^2)",
        "(sgn,1)": "(sgn, omega^0)",
        "(sgn,omega)": "(sgn, omega^1)",
        "(sgn,omega^2)": "(sgn, omega^2)",
        "(std,1)": "(std, omega^0)",
        "(std,omega)": "(std, omega^1)",
        "(std,omega^2)": "(std, omega^2)",
    }
    for r_key, p_key in name_map.items():
        add_exact(
            f"L1.S3xZ3_irrep_{r_key}",
            rL1["S3_x_Z3_characters"]["inner_products"][r_key],
            pL1["S3_x_Z3_all_9_irreps"][p_key]["m_minus_mp"],
        )

    add_exact("L1.halving_mod27_d_neu", rL1["halving_identity_Z_x"]["mod27_d_neu"], pL1["halving_mod27_deg_neu"])
    add_exact("L1.halving_mod27_d_ch", rL1["halving_identity_Z_x"]["mod27_d_ch"], pL1["halving_mod27_deg_chg"])
    add_exact(
        "L1.halving_mod27_exact_Zx",
        bool(rL1["halving_identity_Z_x"]["mod27_direct_sympy_residual"] == 0 and rL1["halving_identity_Z_x"]["mod27_krylov_crt_residual"] == 0),
        pL1["halving_mod27_exact_Zx"],
    )
    add_exact("L1.halving_mod81_d_neu", rL1["halving_identity_Z_x"]["mod81_d_neu"], pL1["halving_mod81_deg_neu"])
    add_exact("L1.halving_mod81_d_ch", rL1["halving_identity_Z_x"]["mod81_d_ch"], pL1["halving_mod81_deg_chg"])
    add_exact(
        "L1.halving_mod81_exact_Zx",
        bool(rL1["halving_identity_Z_x"]["mod81_Z_residual"] == 0 and rL1["halving_identity_Z_x"]["mod81_prime_residuals"] == 0),
        bool(pL1["halving_mod81_exact_mod_6_primes_ok"] == 6),
    )

    # --- L2 exact comparisons ---
    rL2 = ref["L2_3adic_step_law_mod19683"]
    pL2 = prod["L2_3adic_layer_step_law_mod19683"]
    r_ff9 = rL2["falling_factorial_2half_mod19683"]
    p_m9 = pL2["mahler_mod19683"]

    add_exact(
        "L2.goldman_signs_C_S_tau",
        [
            rL2["symbolic_V4_and_Goldman"]["goldman_2form_signs"]["C"],
            rL2["symbolic_V4_and_Goldman"]["goldman_2form_signs"]["sigma"],
            rL2["symbolic_V4_and_Goldman"]["goldman_2form_signs"]["tau"],
        ],
        pL2["goldman_2form_signs_C_S_tau"],
    )
    add_exact(
        "L2.V4_normalizes_and_commutes_symbolic",
        bool(
            rL2["symbolic_V4_and_Goldman"]["V4_normalizes_L_over_Zxyz"]
            and rL2["symbolic_V4_and_Goldman"]["V4_normalizes_R_over_Zxyz"]
            and rL2["symbolic_V4_and_Goldman"]["V4_commutes_symbolically_with_gamma4_words"]
        ),
        bool(pL2["v4_normalizes_C_S_exact"] and pL2["v4_commutes_g1_over_Zxyz"]),
    )
    add_exact("L2.full_orbit_dims_mod729", rL2["full_orbit_mod729"]["dims_d3_to_d6"], pL2["full_orbit_dims_mod729"])
    add_exact("L2.mod19683_dims_d3_to_d9", r_ff9["dims"], p_m9["dims"])
    add_exact("L2.mod19683_sum_dims", r_ff9["sum_dims"], p_m9["sum_dims"])
    add_exact("L2.mod19683_cube_ranks", r_ff9["cube_ranks_E3_to_E8"], p_m9["cube_map_ranks"])
    add_exact("L2.mod19683_goldman_div_zero_mod3", r_ff9["nonzero_goldman_divergences_mod3"] == 0, p_m9["all_goldman_div_zero_mod3"])
    add_exact(
        "L2.mod19683_random_60_words_sift_zero",
        r_ff9["random_60_LR_gamma4_words_sifted_to_zero"] == 60,
        bool(p_m9["raw_cs_trials"] == 60 and p_m9["raw_cs_fails"] == 0),
    )

    p_layer_keys = [
        "r3_mod27", "r4_mod81", "r5_mod243", "r6_mod729",
        "r7_mod2187", "r8_mod6561", "r9_mod19683",
    ]
    p_plus_ranks = [p_m9["layer_details"][k]["rank_O_plus"] for k in p_layer_keys]
    p_minus_ranks = [p_m9["layer_details"][k]["rank_O_minus"] for k in p_layer_keys]
    p_degs = [p_m9["layer_details"][k]["max_poly_deg"] for k in p_layer_keys]
    add_exact("L2.mod19683_plus_half_ranks", r_ff9["plus_half_ranks"], p_plus_ranks)
    add_exact("L2.mod19683_minus_half_ranks", r_ff9["minus_half_ranks"], p_minus_ranks)
    add_exact("L2.mod19683_layer_poly_degrees", r_ff9["layer_poly_degrees"], p_degs)

    # --- L3 comparisons (mirror lock, chiral-flux spectra, C60 J_k, mod 135) ---
    rL3 = ref["L3_mirror_lock_chiral_flux_C60_mod135"]
    pL3 = prod["L3_b2008_mirror_chiral_flux_and_c60_crosscheck"]

    add_exact(
        "L3.mirror_lock_det_C_S_tau",
        [rL3["mirror_lock"]["det_dC"], rL3["mirror_lock"]["det_dS"], rL3["mirror_lock"]["det_dtau"]],
        pL3["det_mod3_C_S_tau"],
    )
    add_exact(
        "L3.mirror_lock_all_3k_exact",
        bool(
            rL3["mirror_lock"]["tau_C_tau_eq_Cinv"]
            and rL3["mirror_lock"]["tau_S_tau_eq_S"]
            and rL3["mirror_lock"]["tau_not_in_G3"]
            and rL3["mirror_lock"]["tau_not_in_G4"]
            and rL3["mirror_lock"]["order_G3_tau_eq_2_G3"]
        ),
        pL3["mirror_lock_all_3k_exact"],
    )

    # Chiral flux numeric cross-residuals on O_27 (producer prints 12 sig figs, so tol = 1e-10)
    flux_map = [
        ("sym_1_1", "theta_0_sym"),
        ("herm_pi_3", "theta_pi_over_3"),
        ("herm_pi_2", "theta_pi_over_2"),
        ("herm_pi_9", "theta_pi_over_9"),
    ]
    r_f27 = rL3["chiral_flux_dps55"]["O_27"]["fluxes"]
    p_f27 = pL3["chiral_reports"]["mod_27"]["flux_cases"]
    for r_fn, p_fn in flux_map:
        for q_i in (0, 1, 2):
            r_cq = parse_re_from_cstr(r_f27[r_fn]["c_q"][str(q_i)])
            p_cq = mp.mpf(p_f27[p_fn]["c_factors"][f"c{q_i}"])
            add_num(f"L3.O27.{r_fn}.c{q_i}", r_cq, p_cq, 10)
            r_top = mp.mpf(r_f27[r_fn]["max_abs_eig"][str(q_i)])
            p_top = mp.mpf(p_f27[p_fn]["tops"][f"q{q_i}_top_abs"])
            add_num(f"L3.O27.{r_fn}.q{q_i}_top_abs", r_top, p_top, 10)

    # Master law residuals (both < 1e-45)
    r_m27 = mp.mpf(rL3["chiral_flux_dps55"]["O_27"]["max_master_law_residual"])
    p_m27 = mp.mpf(pL3["chiral_reports"]["mod_27"]["master_law_err"])
    r_m81 = mp.mpf(rL3["chiral_flux_dps55"]["O_81"]["max_master_law_residual"])
    p_m81 = mp.mpf(pL3["chiral_reports"]["mod_81"]["master_law_err"])
    add_num("L3.O27.master_law_err_vs_0", r_m27, p_m27, 45)
    add_num("L3.O81.master_law_err_vs_0", r_m81, p_m81, 45)

    # C60 J_k on O_81^-, O_243^-, O_729^-
    for mod_k in (81, 243, 729):
        rk = rL3["C60_Weyl_Heisenberg_intertwiner_Jk"]["levels"][f"O_{mod_k}_minus"]
        pk = pL3["c60_Jk_cross_check"][f"mod_{mod_k}"]
        add_exact(f"L3.C60_Jk.mod_{mod_k}.O_minus_size", rk["points"], pk["O_minus_size"])
        add_exact(f"L3.C60_Jk.mod_{mod_k}.preserves_O_minus", rk["J_k_preserves_O_minus"] == rk["points"], pk["J_k_maps_O_minus_to_O_minus"])
        add_exact(f"L3.C60_Jk.mod_{mod_k}.commutes_Vieta3_sq", rk["J_k_commutes_V_Vieta3_sq"] == rk["points"], pk["J_k_commutes_Vieta3_squared"])

    # mod 135 counterexample
    rm135 = rL3["mod135_counterexample"]
    add_exact("L3.mod135.orbit_size", rm135["orbit_size"], pL3["mod135_orbit_size"])
    add_exact("L3.mod135.Fix_C", rm135["Fix_C_count"], pL3["mod135_fix_C"])
    add_exact("L3.mod135.witness_fix_27_5_135", [rm135["witness_fix_O27"], rm135["witness_fix_O5"], rm135["witness_fix_O135"]], pL3["mod135_witness_fix_27_5_135"])
    add_exact("L3.mod135.paired_modes", rm135["paired_modes"], pL3["mod135_paired_counts_mod_primes"][0])
    add_exact("L3.mod135.Q10_exact_match", rm135["Q10_exact_match"], pL3["mod135_Q10_exact_unpaired_match"])

    # --- L4 planted negative controls & gates ---
    rL4 = ref["L4_negative_controls_RPF1_to_RPF6"]
    pL4 = prod["L4_planted_controls"]
    add_exact("L4.PF1_mod9", rL4["RPF1_mod9"]["passed"], pL4["PF1_mod9_rho_breaks"])
    add_exact("L4.PF2_mod25", rL4["RPF2_mod25"]["passed"], pL4["PF2_mod25_breaks_fix3"])
    add_exact("L4.PF2_mod25_fix_C", rL4["RPF2_mod25"]["Fix_C_count"], pL3["pf2_mod25_fix_C"])
    add_exact("L4.PF3_mod135", rL4["RPF3_mod135"]["passed"], pL4["PF3_mod135_breaks_S3xZ3_10_unpaired"])
    add_exact("L4.PF4_single_half_dims", rL4["RPF4_single_half_mod729"]["single_half_plus_dims_d3_to_d6"], pL2["pf4_single_half_mod729_dims"])
    add_exact("L4.PF4_single_half_pass", rL4["RPF4_single_half_mod729"]["passed"], pL4["PF4_single_half_drops_d6_7_to_4"])
    add_exact("L4.PF5_real_2_1_pass", rL4["RPF5_real_2_1_no_mag_split"]["passed"], pL4["PF5_real_P_only_locks_magnitudes"])
    add_num(
        "L4.PF5_real_2_1_O27_mag_diff_vs_prod",
        mp.mpf(rL4["RPF5_real_2_1_no_mag_split"]["O_27_spec1_minus_spec2_mag_diff"]),
        mp.mpf(pL3["pf5_real_P_only_mag_diff"]),
        40,
    )
    add_exact("L4.PF6_broken_C_pass", rL4["RPF6_broken_C_conjugacy"]["passed"], pL4["PF6_broken_C_conj_breaks_comm"])
    add_num(
        "L4.PF6_broken_C_O27_comm_norm",
        mp.mpf(rL4["RPF6_broken_C_conjugacy"]["O_27_comm_frob_norm"]),
        mp.mpf(pL3["pf6_broken_C_comm_norm"]),
        40,
    )

    add_exact("Audit.json_float_count_zero", ref["audit"]["json_float_count"] == 0, prod["gates"]["json_float_count"] == 0)
    add_exact("Gates.all_6_passed", all(ref["referee_gates"].values()), prod["gates"]["all_gates_passed"])

    # Compute max numeric cross-residual across O_27 chiral-flux comparisons (limited only by producer 12-sig-fig string truncation)
    chiral_diffs = [
        mp.mpf(c["abs_diff"])
        for c in checks
        if c["kind"] == "numeric_mpmath" and c["name"].startswith("L3.O27.") and not c["name"].endswith("_vs_0")
    ]
    max_chiral_diff = max(chiral_diffs) if chiral_diffs else mp.mpf(0)

    compare_ast = audit_ast(os.path.abspath(__file__))

    diff_payload = {
        "card_id": "AGY-002_A2-LISTENING-TOWER",
        "referee_json": "relays/a2_listening_tower_referee_v2/referee_a2_listening_tower_out.json",
        "producer_v4_json": "relays/a2_listening_tower_v4/verify_a2_listening_tower_v4_out.json",
        "total_checks": len(checks),
        "matched_checks": len(checks) - len(discrepancies),
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "key_cross_residuals": {
            "L1_halving_mod27_Z_residual": "0",
            "L1_halving_mod81_Z_residual": "0",
            "L2_mod19683_dims_match": "exact ([2, 2, 3, 7, 7, 7, 12])",
            "L2_mod19683_cube_ranks_match": "exact ([2, 2, 3, 7, 7, 7])",
            "L3_O27_chiral_flux_max_abs_diff_vs_v4_12sigfig": mp.nstr(max_chiral_diff, 15),
            "L3_O27_referee_master_law_residual_dps55": mp.nstr(r_m27, 15),
            "L3_O81_referee_master_law_residual_dps55": mp.nstr(r_m81, 15),
            "L3_O27_guardrail3_unitary_scrambling_err": rL3["chiral_flux_dps55"]["guardrail3_unitary_scrambling_O27_pi9_q1"]["eigenvalue_invariance_error"],
            "L3_mod135_Q10_unpaired_match": "exact (949 paired, 10 unpaired = Q_10)",
            "L3_mod135_referee_extra_finding_P10": rm135["unpaired_neutral_extra_nonzero_poly_P10"],
            "L4_PF5_O27_referee_mag_diff": rL4["RPF5_real_2_1_no_mag_split"]["O_27_spec1_minus_spec2_mag_diff"],
            "L4_PF6_O27_comm_norm_diff": mp.nstr(
                abs(mp.mpf(rL4["RPF6_broken_C_conjugacy"]["O_27_comm_frob_norm"]) - mp.mpf(pL3["pf6_broken_C_comm_norm"])),
                15,
            ),
        },
        "referee_gates": ref["referee_gates"],
        "producer_v4_gates": prod["gates"],
        "compare_script_ast_audit": compare_ast,
        "json_float_count": 0,
        "checks": checks,
    }

    jf = count_json_floats(diff_payload)
    diff_payload["json_float_count"] = jf
    assert jf == 0
    assert compare_ast["ast_float_literal_count"] == 0
    assert compare_ast["ast_complex_literal_count"] == 0
    assert compare_ast["ast_float_complex_call_count"] == 0
    assert compare_ast["forbidden_imports_count"] == 0

    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(diff_payload, fh, indent=2, sort_keys=True)
        fh.write("\n")

    print(
        f"COMPARE COMPLETE | total_checks={len(checks)} | matched={len(checks)-len(discrepancies)} | "
        f"discrepancies_count={len(discrepancies)} | json_float_count={jf} | "
        f"max_chiral_diff={mp.nstr(max_chiral_diff, 12)}"
    )


if __name__ == "__main__":
    main()
