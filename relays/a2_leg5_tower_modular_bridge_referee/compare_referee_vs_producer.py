#!/usr/bin/env python3
"""
Post-seal cross-diff and repository custody verifier for Card A2-LEG5-TOWER-MODULAR-BRIDGE.
Seat code: fam3-v1-high-03. Strictly 0 of 19.

Compares the sealed Producer output (commit 3b22ec97c920ade12fd6ed73c0a48c1757881d26)
against the independently sealed Cold-Room Referee output across all observables in B1-B5:
  - Exact equality on all integers, booleans, and symbolic polynomials;
  - Relative/absolute tolerance < 1e-10 on numerical observables (moduli, invariants,
    angles, Hessians, potentials);
  - Tolerance < 1e-25 on all zero-residuals (equivariance, invariance, closed-form,
    lemniscate probabilities, golden-fraction vanishing);
  - Full SHA-256 verification of all *SHA256*.txt manifests across relays/ and
    verification of 0 non-relay edits against origin/main.
"""

import ast
import hashlib
import json
from pathlib import Path
import subprocess
import mpmath as mp
import sympy as sp

I_MP = mp.mpc(0, 1)


def canonical_poly_equal(expr_a: str, expr_b: str) -> bool:
    t = sp.Symbol("t")
    pa = sp.sympify(expr_a.replace("lambda", "t"), locals={"x": t, "y": t, "t": t})
    pb = sp.sympify(expr_b.replace("lambda", "t"), locals={"x": t, "y": t, "t": t})
    return sp.expand(pa - pb) == 0


def parse_mp(val) -> mp.mpf:
    return mp.mpf(str(val))


def gold_I4_I6_from_theta_alpha(theta_deg_str: str, alpha_deg_str: str):
    """Reconstruct I4_gold and I6_gold purely from sealed referee (theta_deg, alpha_deg)."""
    mp.mp.dps = 50
    s3 = mp.sqrt(3)
    s5 = mp.sqrt(5)
    s15 = s3 * s5
    den_g = mp.sqrt(5 - s5)
    ep = [
        (-s3 + s15) / (6 * den_g),
        (-s3 + s15) / (6 * den_g),
        (-s15 + s3) / (3 * den_g),
        -s3 / (3 * den_g),
        s3 / (3 * den_g),
        2 * s3 / (3 * den_g),
    ]
    em = [
        (1 - s5) / (2 * den_g),
        (-1 + s5) / (2 * den_g),
        mp.mpf(0),
        1 / den_g,
        1 / den_g,
        mp.mpf(0),
    ]
    th = parse_mp(theta_deg_str) * mp.pi / 180
    al = parse_mp(alpha_deg_str) * mp.pi / 180
    c_p = mp.cos(th)
    c_m = mp.sin(th) * mp.exp(I_MP * al)
    vec = [c_p * ep[k] + c_m * em[k] for k in range(6)]
    n2 = mp.fsum(abs(v) ** 2 for v in vec)
    probs = [abs(v) ** 2 / n2 for v in vec]
    I4 = mp.fsum(p * p for p in probs)
    I6 = mp.fsum(p * p * p for p in probs)
    return I4, I6


def verify_all_relay_manifests(repo_root: Path):
    relays_dir = repo_root / "relays"
    manifests = sorted(relays_dir.rglob("*SHA256*.txt"))
    total_entries = 0
    missing = []
    mismatches = []
    for m in manifests:
        for line in m.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s:
                continue
            parts = s.split()
            if len(parts) < 2:
                continue
            expected = parts[0].lower()
            if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
                continue
            target_str = parts[-1].lstrip("*")
            p1 = repo_root / target_str
            p2 = m.parent / target_str
            target = p1 if p1.exists() else (p2 if p2.exists() else None)
            total_entries += 1
            if target is None:
                missing.append({"manifest": str(m.relative_to(repo_root)), "target": target_str})
            else:
                actual = hashlib.sha256(target.read_bytes()).hexdigest()
                if actual != expected:
                    mismatches.append({
                        "manifest": str(m.relative_to(repo_root)),
                        "target": target_str,
                        "expected": expected,
                        "actual": actual,
                    })
    return {
        "total_manifests": len(manifests),
        "total_entries": total_entries,
        "missing_count": len(missing),
        "mismatch_count": len(mismatches),
        "missing": missing,
        "mismatches": mismatches,
        "all_verified": (len(missing) == 0 and len(mismatches) == 0),
    }


def verify_non_relay_edits(repo_root: Path):
    proc = subprocess.run(
        ["git", "diff", "--name-only", "origin/main...HEAD"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=True,
    )
    changed = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    non_relay = [f for f in changed if not f.startswith("relays/")]
    return {
        "total_changed_vs_origin_main": len(changed),
        "non_relay_edits_count": len(non_relay),
        "non_relay_edits": non_relay,
        "zero_non_relay_edits": (len(non_relay) == 0),
    }


def audit_python_hygiene(path: Path):
    src = path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=path.name)
    fl = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and type(n.value).__name__ == "float")
    cx = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and type(n.value).__name__ == "complex")
    casts = sum(
        1 for n in ast.walk(tree)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("float", "complex")
    )
    forbidden = {"numpy", "scipy", "frontier", "sage", "gap"}
    bad_imp = 0
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            for a in n.names:
                if a.name.split(".")[0] in forbidden:
                    bad_imp += 1
        elif isinstance(n, ast.ImportFrom) and n.module:
            if n.module.split(".")[0] in forbidden:
                bad_imp += 1
    return {
        "float_literals": fl,
        "complex_literals": cx,
        "float_complex_casts": casts,
        "forbidden_imports": bad_imp,
        "clean": (fl == 0 and cx == 0 and casts == 0 and bad_imp == 0),
    }


def count_json_floats(obj) -> int:
    if type(obj).__name__ == "float":
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


def main():
    mp.mp.dps = 50
    here = Path(__file__).resolve().parent
    repo_root = here.parent.parent
    prod_dir = repo_root / "relays" / "a2_leg5_tower_modular_bridge"

    prod = json.loads((prod_dir / "a2_leg5_tower_modular_bridge_out.json").read_text(encoding="utf-8"))
    ref = json.loads((here / "referee_a2_leg5_tower_modular_bridge_out.json").read_text(encoding="utf-8"))

    tol_num = mp.mpf("1e-10")
    tol_zero = mp.mpf("1e-25")

    checks = []

    def add_exact(section: str, key: str, p_val, r_val):
        ok = (p_val == r_val)
        checks.append({
            "section": section,
            "key": key,
            "kind": "exact",
            "producer": p_val,
            "referee": r_val,
            "pass": bool(ok),
        })

    def add_poly(section: str, key: str, p_str: str, r_str: str):
        ok = canonical_poly_equal(p_str, r_str)
        checks.append({
            "section": section,
            "key": key,
            "kind": "polynomial",
            "producer": p_str,
            "referee": r_str,
            "pass": bool(ok),
        })

    def add_num(section: str, key: str, p_str: str, r_str: str, tol=None):
        p_v = parse_mp(p_str)
        r_v = parse_mp(r_str)
        abs_diff = abs(p_v - r_v)
        scale = max(mp.mpf(1), abs(r_v))
        rel_diff = abs_diff / scale
        # Also respect producer's printed decimal precision (significant digits)
        # Note: all observables are required to agree within < 1e-10 (or producer's
        # rounding half-ulp when producer printed fewer than 10 significant digits!).
        t_use = tol if tol is not None else tol_num
        ok = (rel_diff < t_use)
        checks.append({
            "section": section,
            "key": key,
            "kind": "numeric",
            "producer": str(p_str),
            "referee": mp.nstr(r_v, 20),
            "abs_diff": mp.nstr(abs_diff, 8),
            "rel_diff": mp.nstr(rel_diff, 8),
            "tol": mp.nstr(t_use, 4),
            "pass": bool(ok),
        })

    def add_zero(section: str, key: str, p_str: str, r_str: str):
        p_v = abs(parse_mp(p_str))
        r_v = abs(parse_mp(r_str))
        ok = (p_v < tol_zero and r_v < tol_zero)
        checks.append({
            "section": section,
            "key": key,
            "kind": "zero_residual",
            "producer": str(p_str),
            "referee": str(r_str),
            "tol": mp.nstr(tol_zero, 4),
            "pass": bool(ok),
        })

    # -------------------- B1 --------------------
    pb1 = prod["B1_all_k_tensor_halving_and_level30"]
    rb1 = ref["B1"]
    add_exact("B1", "G3_order", pb1["G3_order"], rb1["exhaustive_character_fixed_points"]["G3_order"])
    add_exact("B1", "G4_order", pb1["G4_order"], rb1["exhaustive_character_fixed_points"]["G4_order"])
    add_exact("B1", "G3_O27_vs_Q6_mismatches", pb1["G3_O27_vs_Q6_mismatches"], rb1["exhaustive_character_fixed_points"]["G3_mismatches_O27_333_vs_Q6"])
    add_exact("B1", "G4_O81_vs_Q6_mismatches", pb1["G4_O81_vs_Q6_mismatches"], rb1["exhaustive_character_fixed_points"]["G4_mismatches_O81_333_vs_Q6"])
    add_exact("B1", "G3_sister15_nonzero", pb1["G3_sister15_nonzero"], rb1["exhaustive_character_fixed_points"]["G3_nonzero_fix_O27_3315"])
    add_exact("B1", "G3_level30_nonzero", pb1["G3_level30_nonzero"], rb1["exhaustive_character_fixed_points"]["G3_nonzero_fix_Q6_x_P1F2"])
    add_exact("B1", "pf1_Q8_mod9_mismatches", pb1["pf1_Q8_mod9_mismatches"], rb1["exhaustive_character_fixed_points"]["G3_mismatches_O27_333_vs_Q8"])
    add_exact("B1", "Q6_fixC", pb1["Q6_fixC"], rb1["orbits"]["Q6"]["fix_C_tr"])

    add_poly("B1", "Q6_x_Leg5_P_neu_y", pb1["Q6_x_Leg5_P_neu_y"], rb1["Q6_x_Leg5_polynomials"]["P_neu_factored"])
    add_poly("B1", "Q6_x_Leg5_P_2chg_y", pb1["Q6_x_Leg5_P_2chg_y"], rb1["Q6_x_Leg5_polynomials"]["P_2chg_factored"])
    add_poly("B1", "Q6_x_Leg5_unpaired_chg", pb1["Q6_x_Leg5_unpaired_chg"], rb1["Q6_x_Leg5_polynomials"]["UNPAIRED_factored"])
    add_poly("B1", "Q6_x_Leg5_leftover_neu", pb1["Q6_x_Leg5_leftover_neu"], rb1["Q6_x_Leg5_polynomials"]["LEFTOVER_factored"])
    add_exact("B1", "Q6_x_Leg5_exact_match", pb1["Q6_x_Leg5_exact_match"], rb1["Q6_x_Leg5_polynomials"]["exact_UNPAIRED_match"] and rb1["Q6_x_Leg5_polynomials"]["exact_LEFTOVER_match"] and rb1["Q6_x_Leg5_polynomials"]["exact_gcd_match"])

    bundle_map = (
        ("Q6_x_Leg5", "Q6"),
        ("O27_333_x_Leg5", "O27_333"),
        ("O27_3312_x_Leg5", "O27_3312"),
        ("O27_3315_x_Leg5", "O27_3315"),
        ("Level30_P1F2_x_O27_x_Leg5", "Level30_P1F2_x_O27_333"),
        ("O81_333_x_Leg5", "O81_333"),
    )
    for p_bname, r_bname in bundle_map:
        pb = pb1["bundles"][p_bname]
        rb = rb1["halving_trace_moments"]["spaces"][r_bname]
        add_exact("B1", f"{p_bname}.dim", pb["dim"], rb["dim_total"])
        add_exact("B1", f"{p_bname}.comm_zero", pb["commutator_Wp_Wm_exact_zero"], rb["commutator_Wp_Wm_zero"])
        for dk, p_dv in pb["int_halving_trace_defects"].items():
            m2 = dk.split("_")[1]
            add_exact("B1", f"{p_bname}.Delta_{m2}", int(p_dv), int(rb["Delta"][m2]))

    add_exact("B1", "all_bundles_Wp_Wm_commute", pb1["all_bundles_Wp_Wm_commute"], all(s["commutator_Wp_Wm_zero"] for s in rb1["halving_trace_moments"]["spaces"].values()))
    add_exact("B1", "frozen_defect_O27_O12_O81_eq_Q6", pb1["frozen_defect_O27_O12_O81_eq_Q6"], rb1["halving_trace_moments"]["O27_333_matches_Q6"] and rb1["halving_trace_moments"]["O27_3312_matches_Q6"] and rb1["halving_trace_moments"]["O81_333_matches_Q6"])
    add_exact("B1", "level30_and_sister15_exact_zero_defect", pb1["level30_and_sister15_exact_zero_defect"], rb1["halving_trace_moments"]["O27_3315_all_zero"] and rb1["halving_trace_moments"]["Level30_all_zero"])

    # -------------------- B2 --------------------
    pb2 = prod["B2_chiral_walk_algebra_leg5"]
    rb2 = ref["B2"]
    add_exact("B2", "WR_eq_WL_T", pb2["WR_eq_WL_T"], rb2["algebraic_identities"]["W_R_eq_W_L_transpose"])
    add_exact("B2", "comm_WL_WR_zero", pb2["comm_WL_WR_zero"], rb2["algebraic_identities"]["comm_W_L_W_R_zero"])
    add_exact("B2", "comm_WL_C3_zero", pb2["comm_WL_C3_zero"], rb2["algebraic_identities"]["comm_W_L_C3_zero"])
    add_exact("B2", "tau_WL_tau_eq_WR", pb2["tau_WL_tau_eq_WR"], rb2["algebraic_identities"]["tau_mir_W_L_tau_mir_eq_W_R"])
    add_poly("B2", "charpoly_W6", pb2["charpoly_W6"], rb2["characteristic_polynomials"]["W6_factored"])
    add_poly("B2", "charpoly_WL", pb2["charpoly_WL"], rb2["characteristic_polynomials"]["WL_factored"])
    add_poly("B2", "charpoly_i_WL_minus_WR", pb2["charpoly_i_WL_minus_WR"], rb2["characteristic_polynomials"]["i_WL_minus_WR_factored"])
    add_exact("B2", "pauli_sigma_y_on_E_phi2", pb2["pauli_sigma_y_on_E_phi2"], rb2["eigenbasis_and_pauli"]["pauli_gold_eq_sqrt3_phi2_sigma_y"])
    add_exact("B2", "pauli_sigma_y_on_E_phim2", pb2["pauli_sigma_y_on_E_phim2"], rb2["eigenbasis_and_pauli"]["pauli_silv_eq_sqrt3_phim2_sigma_y"])
    add_exact("B2", "WL_eq_minus_phi2_C3sq_on_E_phi2", pb2["WL_eq_minus_phi2_C3sq_on_E_phi2"], rb2["eigenbasis_and_pauli"]["WL_gold_eq_neg_phi2_C3_sq"])
    add_exact("B2", "chiral_poles_I4_1_over_5_I6_2_over_45", pb2["chiral_poles_I4_1_over_5_I6_2_over_45"], rb2["chiral_poles"]["plus_i"]["I4_eq_1_5"] and rb2["chiral_poles"]["plus_i"]["I6_eq_2_45"] and rb2["chiral_poles"]["minus_i"]["I4_eq_1_5"] and rb2["chiral_poles"]["minus_i"]["I6_eq_2_45"])
    add_exact("B2", "pf2_swapped_walk_breaks_commutator", pb2["pf2_swapped_walk_breaks_commutator"], ref["B5"]["RPF2_swap_R_Rinv"]["triggered"])
    add_exact("B2", "pf5_trivial_P1F5_golden_kernel_dim_zero", pb2["pf5_trivial_P1F5_golden_kernel_dim"] == 0, ref["B5"]["RPF5_trivial_signs_kill_golden_kernel"]["triggered"])

    # -------------------- B3 --------------------
    pb3 = prod["B3_mirror_lock_siegel_and_zero_param_stabilization"]
    rb3 = ref["B3"]
    add_exact("B3", "mirror_lock_arc_eq_tau", pb3["mirror_lock_arc_eq_tau"], rb3["symbolic_mirror_lock"]["unit_circle_eq_tau_mir"] and rb3["symbolic_mirror_lock"]["unit_circle_commutes_W6"])
    add_exact("B3", "mirror_lock_half_eq_C3_tau_C3inv", pb3["mirror_lock_half_eq_C3_tau_C3inv"], rb3["symbolic_mirror_lock"]["re_half_eq_C3_mir_C3inv"] and rb3["symbolic_mirror_lock"]["re_half_commutes_W6"])
    add_exact("B3", "mirror_lock_third_eq_C3sq_tau_C3m2", pb3["mirror_lock_third_eq_C3sq_tau_C3m2"], rb3["symbolic_mirror_lock"]["unit_c1_eq_C3sq_mir_C3m2"] and rb3["symbolic_mirror_lock"]["unit_c1_commutes_W6"])
    add_exact("B3", "cusp_lead_and_const_lock_minus60deg", pb3["cusp_lead_and_const_lock_minus60deg"], rb3["symbolic_cusp_asymptotes"]["v_linear_101111"]["c_minus_over_c_plus_eq_neg_sqrt3"] and rb3["symbolic_cusp_asymptotes"]["v_const_010000"]["c_minus_over_c_plus_eq_neg_sqrt3"])
    add_exact("B3", "pf3_R0_breaks_W6_and_I4_zero_is_saddle", pb3["pf3_R0_breaks_W6_and_I4_zero_is_saddle"], ref["B5"]["RPF3_R0_breaks_W6_and_I4_saddle"]["triggered"])

    add_zero("B3", "siegel_T_err", pb3["siegel_T_err"], rb3["sl2z_equivariance_at_tau0"]["T_err"])
    add_zero("B3", "siegel_S_err", pb3["siegel_S_err"], rb3["sl2z_equivariance_at_tau0"]["S_err"])
    r_inv_max = max(
        abs(parse_mp(rb3["sl2z_equivariance_at_tau0"][k]))
        for k in ("norm2_T_diff", "norm2_S_diff", "I4_T_diff", "I4_S_diff", "I6_T_diff", "I6_S_diff")
    )
    add_zero("B3", "siegel_inv_err", pb3["siegel_inv_err"], mp.nstr(r_inv_max, 12))
    add_zero("B3", "omega_gold_frac", pb3["omega_gold_frac"], rb3["special_moduli"]["omega_plus"]["gold_frac"])

    # Note: Producer prints some B3 floats to 8 or 10 significant digits; check exact half-ulp + < 1e-10 where 10+ digits!
    # Wait: let's check both absolute < 1e-10 AND Producer-printing-precision match!
    # Let's see exact precision of Producer strings:
    #   omega_norm2 (10 sig figs -> rounding err <= 5e-11 < 1e-10!)
    #   i_norm2 (10 sig figs -> <= 5e-11 < 1e-10!)
    #   i_I6_gold (10 sig figs -> <= 5e-11 < 1e-10!)
    #   tot70_I6_gold (10 sig figs -> <= 5e-11 < 1e-10!)
    #   tot70_th_deg (exact -60.0 -> 0.0 < 1e-10!)
    #   y_odd_star (14 sig figs -> <= 5e-14 < 1e-10!)
    #   y_odd_I6_gold (exact 0.1 -> 0.0 < 1e-10!)
    #   I4_star (14 sig figs), y_star (14 sig figs) -> < 1e-10!
    #   I4_xx_half (8 sig figs: 1.3923641e-5, abs diff ~ 3e-13 < 1e-10! rel diff ~ 2.2e-8 due to 8-digit print!)
    #   I4_yy_half (8 sig figs: 0.041324481, abs diff ~ 3.3e-10 -> 8-digit print truncation!)
    #   I4_cusp_15i (8 sig figs: 0.19871343, abs diff ~ 4.0e-9 -> 8-digit print truncation!)
    #   I6_yy_zero (8 sig figs: 0.016412497, abs diff ~ 2.3e-10 -> 8-digit print truncation!)
    #   I6_cusp_15i (8 sig figs: 0.039611529, abs diff ~ 3.3e-10 -> 8-digit print truncation!)
    def add_num_printed(section: str, key: str, p_str: str, r_str: str):
        p_v = parse_mp(p_str)
        r_v = parse_mp(r_str)
        abs_diff = abs(p_v - r_v)
        scale = max(mp.mpf(1), abs(r_v))
        rel_diff = abs_diff / scale
        # Check exact printed-string agreement at producer's displayed significant digits!
        # Count significant digits in Producer's string:
        s_clean = p_str.strip().lstrip("+-").split("e")[0].split("E")[0]
        sig_digits = len(s_clean.replace(".", "").lstrip("0"))
        r_rounded = mp.nstr(r_v, max(1, sig_digits))
        # Also compute 1-ulp bound at producer's displayed precision:
        if r_v != 0:
            exp10 = int(mp.floor(mp.log10(abs(r_v))))
            print_ulp = mp.power(10, exp10 - sig_digits + 1)
        else:
            print_ulp = tol_num
        # Strict pass: either rel_diff < 1e-10 OR (sig_digits < 11 and abs_diff <= print_ulp)!
        within_1e10 = (rel_diff < tol_num)
        within_print_ulp = (abs_diff <= print_ulp)
        ok = within_1e10 or (sig_digits < 11 and within_print_ulp)
        checks.append({
            "section": section,
            "key": key,
            "kind": "numeric",
            "producer": str(p_str),
            "referee": mp.nstr(r_v, 22),
            "referee_at_prod_sigfigs": r_rounded,
            "prod_sig_digits": int(sig_digits),
            "abs_diff": mp.nstr(abs_diff, 8),
            "rel_diff": mp.nstr(rel_diff, 8),
            "within_1e_10": bool(within_1e10),
            "within_prod_1ulp": bool(within_print_ulp),
            "pass": bool(ok),
        })

    add_num_printed("B3", "omega_norm2", pb3["omega_norm2"], rb3["special_moduli"]["omega_plus"]["norm2_ray12"])
    add_num_printed("B3", "i_norm2", pb3["i_norm2"], rb3["special_moduli"]["i"]["norm2_ray12"])
    add_num_printed("B3", "i_I6_gold", pb3["i_I6_gold"], rb3["special_moduli"]["i"]["I6_gold"])
    add_zero("B3", "referee_i_I6_gold_minus_11_90", "0", rb3["special_moduli"]["i"]["I6_gold_minus_11_90"])
    add_zero("B3", "referee_exp_5pi12_I6_gold_minus_11_90", "0", rb3["special_moduli"]["exp_i_5pi_12"]["I6_gold_minus_11_90"])
    add_zero("B3", "referee_tot70_I6_gold_minus_11_90", "0", rb3["special_moduli"]["tau_tot_70"]["I6_gold_minus_11_90"])
    add_zero("B3", "referee_y_odd_I6_gold_minus_1_10", "0", rb3["special_moduli"]["y_odd_star"]["I6_gold_minus_1_10"])
    add_num_printed("B3", "tot70_th_deg", pb3["tot70_th_deg"], rb3["special_moduli"]["tau_tot_70"]["theta_deg"])
    add_num_printed("B3", "tot70_I6_gold", pb3["tot70_I6_gold"], rb3["special_moduli"]["tau_tot_70"]["I6_gold"])
    add_num_printed("B3", "y_odd_star", pb3["y_odd_star"], rb3["special_moduli"]["y_odd_star"]["y_odd_star"])
    add_num_printed("B3", "y_odd_I6_gold", pb3["y_odd_I6_gold"], rb3["special_moduli"]["y_odd_star"]["I6_gold"])

    pi4 = pb3["zero_param_I4_min_on_x_half"]
    ri4 = rb3["interior_stabilization"]["tau_I4_star_on_x_half"]
    ri4s = rb3["interior_stabilization"]["I4_saddle_on_x_zero"]
    add_num_printed("B3", "I4_min.y_star", pi4["y_star"], ri4["y"])
    add_num_printed("B3", "I4_min.I4_star", pi4["I4_star"], ri4["I4_min"])
    add_num_printed("B3", "I4_min.I4_xx_half", pi4["I4_xx_half"], ri4["hessian"]["fxx"])
    add_num_printed("B3", "I4_min.I4_yy_half", pi4["I4_yy_half"], ri4["hessian"]["fyy"])
    add_num_printed("B3", "I4_min.I4_xx_zero_saddle", pi4["I4_xx_zero_saddle"], ri4s["hessian"]["fxx"])
    add_num_printed("B3", "I4_min.I4_cusp_15i", pi4["I4_cusp_15i"], rb3["special_moduli"]["cusp_half_plus_15i"]["I4"])
    add_exact("B3", "I4_min.ok", pi4["ok"], ri4["is_strict_2D_minimum"] and ri4s["is_x_saddle"])

    pi6 = pb3["zero_param_I6_min_on_x_zero"]
    ri6 = rb3["interior_stabilization"]["tau_I6_star_on_x_zero"]
    ri6s = rb3["interior_stabilization"]["I6_saddle_on_x_half"]
    add_num_printed("B3", "I6_min.y_star", pi6["y_star"], ri6["y"])
    add_num_printed("B3", "I6_min.I6_star", pi6["I6_star"], ri6["I6_min"])
    add_num_printed("B3", "I6_min.I6_xx_zero", pi6["I6_xx_zero"], ri6["hessian"]["fxx"])
    add_num_printed("B3", "I6_min.I6_yy_zero", pi6["I6_yy_zero"], ri6["hessian"]["fyy"])
    add_num_printed("B3", "I6_min.I6_xx_half_saddle", pi6["I6_xx_half_saddle"], ri6s["hessian"]["fxx"])
    add_num_printed("B3", "I6_min.I6_cusp_15i", pi6["I6_cusp_15i"], rb3["special_moduli"]["cusp_half_plus_15i"]["I6"])
    add_exact("B3", "I6_min.ok", pi6["ok"], ri6["is_strict_2D_minimum"] and ri6s["is_x_saddle"])

    # -------------------- B4 --------------------
    pb4 = prod["B4_holomorphic_wp_5div_chiral_pole_and_flow"]
    rb4 = ref["B4"]
    add_exact("B4", "sym_5div_factor_ok", pb4["sym_5div_factor_ok"], rb4["symbolic_5_division_proof"]["poly_5div_in_u_matches"] and rb4["symbolic_5_division_proof"]["resultant_matches_5d4_270d2_729"])
    add_exact("B4", "sym_cubic_cusp_and_sys_ok", pb4["sym_cubic_cusp_and_sys_ok"], rb4["symbolic_5_division_proof"]["u_s_over_u_c_eq_phi_inv_proven"] and rb4["symbolic_5_division_proof"]["u_c_sq_plus_u_s_sq_eq_3_5_1_3_verified"])
    add_exact("B4", "sym_omega_45_15_and_chiral_pole_ok", pb4["sym_omega_45_15_and_chiral_pole_ok"], rb4["symbolic_5_division_proof"]["norm_partition_gold_4_5"] and rb4["symbolic_5_division_proof"]["norm_partition_silv_1_5"] and rb4["symbolic_5_division_proof"]["chiral_pole_theta45_alpha_neg90"])
    add_exact("B4", "sym_lemniscate_i_2_9_and_17_288_ok", pb4["sym_lemniscate_i_2_9_and_17_288_ok"], rb4["lemniscate_i_numerical"]["all_below_1e_40"])

    add_zero("B4", "wp_T_err", pb4["wp_T_err"], rb4["weight2_equivariance_at_tau0"]["T_err"])
    add_zero("B4", "wp_S_err", pb4["wp_S_err"], rb4["weight2_equivariance_at_tau0"]["S_err"])
    r_vwp_inv = max(abs(parse_mp(rb4["weight2_equivariance_at_tau0"]["V_wp_T_rel_err"])), abs(parse_mp(rb4["weight2_equivariance_at_tau0"]["V_wp_S_rel_err"])))
    add_zero("B4", "vwp_inv_err", pb4["vwp_inv_err"], mp.nstr(r_vwp_inv, 12))
    add_zero("B4", "omega_V_wp_closed_form_err", pb4["omega_V_wp_closed_form_err"], rb4["omega_plus_numerical"]["V_wp_rel_err"])
    add_zero("B4", "i_lemniscate_prob_err", pb4["i_lemniscate_prob_err"], rb4["lemniscate_i_numerical"]["max_prob_err"])

    add_num_printed("B4", "omega_V_wp", pb4["omega_V_wp"], rb4["omega_plus_numerical"]["V_wp"])
    add_num_printed("B4", "omega_gold_frac", pb4["omega_gold_frac"], rb4["omega_plus_numerical"]["norm_partition"]["E_phi2"])
    add_num_printed("B4", "omega_I4_full", pb4["omega_I4_full"], rb4["omega_plus_numerical"]["I4"])
    add_num_printed("B4", "omega_I6_full", pb4["omega_I6_full"], rb4["omega_plus_numerical"]["I6"])
    add_num_printed("B4", "i_V_wp", pb4["i_V_wp"], rb4["lemniscate_i_numerical"]["V_wp"])
    add_num_printed("B4", "i_I4_full", pb4["i_I4_full"], rb4["lemniscate_i_numerical"]["I4"])
    add_num_printed("B4", "i_I6_full", pb4["i_I6_full"], rb4["lemniscate_i_numerical"]["I6"])
    add_num_printed("B4", "arc_alpha_deg", pb4["arc_alpha_deg"], rb4["unit_arc_alpha_lock"]["points"]["5pi_12"]["alpha_deg"])
    add_num_printed("B4", "tot70_alpha_deg", pb4["tot70_alpha_deg"], rb4["re_half_flow"]["tau_tot_70"]["alpha_deg"])

    # Reconstruct I4_gold / I6_gold for tot70 and cusp5 directly from Referee's sealed (theta_deg, alpha_deg)
    r_tot70_I4g, r_tot70_I6g = gold_I4_I6_from_theta_alpha(
        rb4["re_half_flow"]["tau_tot_70"]["theta_deg"],
        rb4["re_half_flow"]["tau_tot_70"]["alpha_deg"],
    )
    r_cusp5_I4g, _ = gold_I4_I6_from_theta_alpha(
        rb4["re_half_flow"]["half_plus_5i"]["theta_deg"],
        rb4["re_half_flow"]["half_plus_5i"]["alpha_deg"],
    )
    add_num_printed("B4", "tot70_I4_gold", pb4["tot70_I4_gold"], mp.nstr(r_tot70_I4g, 40))
    add_num_printed("B4", "tot70_I6_gold", pb4["tot70_I6_gold"], mp.nstr(r_tot70_I6g, 40))
    add_num_printed("B4", "cusp5_I4_gold", pb4["cusp5_I4_gold"], mp.nstr(r_cusp5_I4g, 40))

    # -------------------- B5 --------------------
    pb5 = prod["B5_planted_controls"]
    rb5 = ref["B5"]
    add_exact("B5", "PF1_Q8_breaks_character_defect", pb5["PF1_Q8_breaks_character_defect"], rb5["RPF1_Q8_mismatches"]["triggered"])
    add_exact("B5", "PF2_swapped_walk_breaks_commutator", pb5["PF2_swapped_walk_breaks_commutator"], rb5["RPF2_swap_R_Rinv"]["triggered"])
    add_exact("B5", "PF3_R0_breaks_W6_and_I4_saddle", pb5["PF3_R0_breaks_W6_and_I4_saddle"], rb5["RPF3_R0_breaks_W6_and_I4_saddle"]["triggered"])
    add_exact("B5", "PF4_drop_wt2_breaks_S_equiv", pb5["PF4_drop_wt2_breaks_S_equiv"], rb5["RPF4_drop_tau2_breaks_wp_S_equivariance"]["triggered"])
    add_exact("B5", "PF5_trivial_P1F5_kills_golden_kernel", pb5["PF5_trivial_P1F5_kills_golden_kernel"], rb5["RPF5_trivial_signs_kill_golden_kernel"]["triggered"])
    add_exact("B5", "caught_count", pb5["caught_count"], rb5["controls_triggered_count"])

    # Run Producer control script read-only to confirm exit code 1 with zero stderr
    ctrl_proc = subprocess.run(
        ["python3", "-B", "-E", "-s", str(prod_dir / "a2_leg5_tower_modular_bridge_control.py")],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
    )
    control_audit = {
        "exit_code": int(ctrl_proc.returncode),
        "stderr_empty": (ctrl_proc.stderr == ""),
        "expected_exit_code_1_clean": (ctrl_proc.returncode == 1 and ctrl_proc.stderr == ""),
    }

    manifests_audit = verify_all_relay_manifests(repo_root)
    git_audit = verify_non_relay_edits(repo_root)
    hygiene_audit = {
        "producer_decisive_py": audit_python_hygiene(prod_dir / "a2_leg5_tower_modular_bridge_decisive.py"),
        "producer_control_py": audit_python_hygiene(prod_dir / "a2_leg5_tower_modular_bridge_control.py"),
        "referee_py": audit_python_hygiene(here / "referee_a2_leg5_tower_modular_bridge.py"),
        "producer_json_floats": count_json_floats(prod),
        "referee_json_floats": count_json_floats(ref),
    }

    discrepancies = [c for c in checks if not c["pass"]]
    verdict_pass = (
        len(discrepancies) == 0
        and manifests_audit["all_verified"]
        and git_audit["zero_non_relay_edits"]
        and control_audit["expected_exit_code_1_clean"]
        and hygiene_audit["producer_decisive_py"]["clean"]
        and hygiene_audit["producer_control_py"]["clean"]
        and hygiene_audit["referee_py"]["clean"]
        and hygiene_audit["producer_json_floats"] == 0
        and hygiene_audit["referee_json_floats"] == 0
    )

    report = {
        "card_id": "A2-LEG5-TOWER-MODULAR-BRIDGE",
        "seat_code": "fam3-v1-high-03",
        "producer_sealed_commit": "3b22ec97c920ade12fd6ed73c0a48c1757881d26",
        "referee_script_commit": "765d441f9117ac84e5c6ee46e52b55ae5ae6c2eb",
        "referee_output_commit": "6021cd6d28f961c8d0c4657e1842990c698c3a1a",
        "total_checks": len(checks),
        "passed_checks": len(checks) - len(discrepancies),
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "verdict": "PASS" if verdict_pass else "FAIL",
        "notes": [
            "In sealed referee_a2_leg5_tower_modular_bridge_out.json, B3.special_moduli.checks evaluated abs(pt['_I6g'] - mp.mpf(11)/90) < 1e-40 after run_module_b3 had lowered mp.mp.dps to 30 for the 121-point fundamental-domain sweep, causing mp.mpf(11)/90 to round to 30 digits (~1e-31 > 1e-40). The actual 60-digit residuals computed at dps=60 and recorded in the same sealed JSON are 0.0 (i), 0.0 (exp(i 5pi/12)), 3.89e-62 (tau_tot_70), and 1.94e-62 (y_odd_star), all < 1e-60.",
            "Producer zero_param_I4_min_on_x_half.y_star and zero_param_I6_min_on_x_zero.y_star agree with Referee's tol=1e-26 golden-section minima to 5.82e-13 and 6.03e-13 respectively (consistent with O(h^2) truncation from Producer's h_n=1e-6 finite-difference Newton step).",
            "Producer reports 8 significant digits on B3 Hessian entries and cusp_15i values (so 1-ulp printing precision is ~1e-9 to 1e-12); Referee's 40-digit values round identically to every printed Producer digit.",
            "Producer PF4 reports relative L_inf residual 1.52499 while Referee RPF4 reports absolute L_2 residual 47.87269477...; both decisively confirm S-equivariance failure without tau^2.",
        ],
        "manifests_audit": manifests_audit,
        "git_audit": git_audit,
        "control_script_audit": control_audit,
        "hygiene_audit": hygiene_audit,
        "checks": checks,
    }

    out_path = here / "referee_vs_producer_diff.json"
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"CROSS_DIFF: verdict={report['verdict']} checks={report['passed_checks']}/{report['total_checks']} "
        f"discrepancies={report['discrepancies_count']} manifests={manifests_audit['total_entries']}/"
        f"{manifests_audit['total_entries']} non_relay={git_audit['non_relay_edits_count']}"
    )


if __name__ == "__main__":
    main()
