"""
Post-Seal Cross-Diff: Blind Cold-Room Referee vs Producer for Card A2-WEIL-CHIRAL-LATTICE-BRIDGE
Seat code: fam3-v1-high-03 | Strictly 0 of 19 (pure mathematics, zero empirical data)

Reads ONLY the two sealed, committed JSON outputs:
  - relays/a2_weil_chiral_lattice_bridge/a2_weil_chiral_lattice_bridge_out.json
  - relays/a2_weil_chiral_lattice_bridge_referee/referee_a2_weil_chiral_lattice_bridge_out.json
and verifies every shared boolean, integer, exact rational, spectral moment,
stabilization coordinate y_*, V_*, Hessian curvature, singular-value ratio,
and |V_{3x3}| mixing entry, plus SHA-256 manifests in both directories.
"""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List

import mpmath as mp

mp.mp.dps = 50

ZERO = mp.mpf(0)
ONE = mp.mpf(1)

REF_DIR = Path(__file__).resolve().parent
RELAYS_DIR = REF_DIR.parent
PROD_DIR = RELAYS_DIR / "a2_weil_chiral_lattice_bridge"

PROD_JSON = PROD_DIR / "a2_weil_chiral_lattice_bridge_out.json"
REF_JSON = REF_DIR / "referee_a2_weil_chiral_lattice_bridge_out.json"
DIFF_JSON = REF_DIR / "referee_vs_producer_diff.json"


def sci(x: Any, digits: int = 10) -> str:
    return mp.nstr(mp.mpf(x), digits)


def count_json_floats(obj: Any) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


def check_ast_zero_floats(path: Path) -> int:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return sum(
        1 for n in ast.walk(tree)
        if isinstance(n, ast.Constant) and isinstance(n.value, float)
    )


def verify_sha256_manifest(directory: Path, manifest_name: str) -> Dict[str, Any]:
    mpath = directory / manifest_name
    entries: List[Dict[str, Any]] = []
    all_ok = mpath.exists()
    if mpath.exists():
        for raw in mpath.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line:
                continue
            parts = line.split()
            expected_hex = parts[0]
            fname = parts[-1]
            fpath = directory / fname
            actual_hex = hashlib.sha256(fpath.read_bytes()).hexdigest() if fpath.exists() else "MISSING"
            ok = (actual_hex == expected_hex)
            all_ok = all_ok and ok
            entries.append({
                "file": fname,
                "expected_prefix16": expected_hex[:16],
                "actual_prefix16": actual_hex[:16],
                "match": ok,
            })
    return {
        "manifest": str(mpath.relative_to(RELAYS_DIR)),
        "entries": entries,
        "all_ok": all_ok,
    }


def main() -> int:
    prod = json.loads(PROD_JSON.read_text(encoding="utf-8"))
    ref = json.loads(REF_JSON.read_text(encoding="utf-8"))

    checks: List[Dict[str, Any]] = []

    def add_exact(module: str, name: str, p_val: Any, r_val: Any) -> None:
        ok = (p_val == r_val)
        checks.append({
            "module": module,
            "check": name,
            "kind": "exact",
            "producer": p_val,
            "referee": r_val,
            "matched": ok,
        })

    def add_num(
        module: str,
        name: str,
        p_str: str,
        r_str: str,
        tol: mp.mpf,
        relative: bool = False,
        note: str = "",
    ) -> None:
        pv = mp.mpf(p_str)
        rv = mp.mpf(r_str)
        abs_d = abs(pv - rv)
        denom = max(abs(rv), ONE) if not relative else max(abs(rv), mp.mpf("1e-40"))
        metric = abs_d / denom if relative else abs_d
        ok = metric <= tol
        rec: Dict[str, Any] = {
            "module": module,
            "check": name,
            "kind": "rel_num" if relative else "abs_num",
            "producer": p_str,
            "referee": r_str,
            "diff": sci(metric),
            "tol": sci(tol),
            "matched": ok,
        }
        if note:
            rec["note"] = note
        checks.append(rec)

    def add_both_below(
        module: str,
        name: str,
        p_str: str,
        r_str: str,
        bound: mp.mpf,
    ) -> None:
        pv = abs(mp.mpf(p_str))
        rv = abs(mp.mpf(r_str))
        ok = (pv <= bound) and (rv <= bound)
        checks.append({
            "module": module,
            "check": name,
            "kind": "both_below",
            "producer_abs": sci(pv),
            "referee_abs": sci(rv),
            "bound": sci(bound),
            "matched": ok,
        })

    # -----------------------------------------------------------------------
    # Global / Hygiene / Controls
    # -----------------------------------------------------------------------
    add_exact("GLOBAL", "card_id", prod["card"], ref["card_id"])
    add_exact("GLOBAL", "seat_code", prod["seat_code"], ref["seat_code"])
    add_exact("GLOBAL", "all_gates_passed", prod["all_gates_passed"], ref["all_referee_gates_passed"])
    add_exact("GLOBAL", "ast_floats_zero", prod["ast_floats"], ref["hygiene"]["ast_float_literal_count"])
    add_exact("GLOBAL", "json_floats_zero", prod["json_floats"], ref["json_float_literal_count"])
    add_exact("GLOBAL", "controls_detected_count", prod["planted_controls"]["caught"], ref["planted_fault_controls"]["detected_count"])
    add_exact("GLOBAL", "controls_total_count", prod["planted_controls"]["total"], ref["planted_fault_controls"]["total_count"])

    # -----------------------------------------------------------------------
    # Module W1
    # -----------------------------------------------------------------------
    pw1 = prod["W1_all_odd_N_chiral_index_and_mod4"]
    rw1 = ref["W1"]

    add_exact("W1", "module_passed", pw1["ok"], rw1["passed"])
    add_exact("W1", "pairs_checked_3_49", pw1["pairs_checked_3_49"], rw1["pairs_checked_count"])
    add_exact("W1", "qr_and_sympy_ok", pw1["qr_all_ok"], rw1["sympy_cyclotomic_exact"]["all_exact_passed"])
    add_exact("W1", "parity_split_all_ok", pw1["parity_split_all_ok"], rw1["parity_dim_mismatches"] == 0)
    add_exact("W1", "iso_N_3_to_35", pw1["iso_N_3_to_35"], rw1["mod4_isospectral_list"])
    add_exact("W1", "split_N_3_to_35", pw1["split_N_3_to_35"], rw1["mod4_chiral_split_list"])

    add_both_below("W1", "max_err_tr_C3", pw1["max_err_tr_C3"], rw1["max_tr_c3_err"], mp.mpf("1e-30"))
    add_both_below("W1", "max_err_flip_trace", pw1["max_err_flip_trace_minus_1"], rw1["max_flip_trace_err"], mp.mpf("1e-30"))
    add_both_below("W1", "max_err_spinor_sign", pw1["max_err_spinor_sign"], rw1["max_full_spinor_err"], mp.mpf("1e-30"))
    add_both_below("W1", "mirror_c3_err", pw1["mirror_unitary_max_err"], rw1["max_mirror_c3_err"], mp.mpf("1e-30"))
    add_both_below("W1", "crt_max_err", pw1["crt_max_err"], rw1["max_crt_err"], mp.mpf("1e-30"))

    # All 17 odd N in 3..35: all_1mod4 + 6 chiral/parity dimensions each (17 * 7 = 119 exact checks!)
    ref_mod4_by_N = {rec["N"]: rec for rec in rw1["mod4_records"]}
    for prec in pw1["chiral_table_3_to_35"]:
        N = prec["N"]
        rrec = ref_mod4_by_N[N]
        add_exact("W1", f"N{N}_all_1mod4", prec["all_1mod4"], rrec["all_primes_1_mod_4"])
        add_exact("W1", f"N{N}_isospectral_obs", prec["all_1mod4"], rrec["isospectral_observed"])
        add_exact("W1", f"N{N}_dim_H1", prec["dq"][1], rrec["dim_H1"])
        add_exact("W1", f"N{N}_dim_H2", prec["dq"][2], rrec["dim_H2"])
        add_exact("W1", f"N{N}_dim_H1_even", prec["dq_even"][1], rrec["dim_H1_even"])
        add_exact("W1", f"N{N}_dim_H2_even", prec["dq_even"][2], rrec["dim_H2_even"])
        add_exact("W1", f"N{N}_dim_H1_odd", prec["dq_odd"][1], rrec["dim_H1_odd"])
        add_exact("W1", f"N{N}_dim_H2_odd", prec["dq_odd"][2], rrec["dim_H2_odd"])

    # -----------------------------------------------------------------------
    # Module W2
    # -----------------------------------------------------------------------
    pw2 = prod["W2_leg5_weil_intertwiner_and_Q6_freezing"]
    rw2 = ref["W2"]

    add_exact("W2", "module_passed", pw2["ok"], rw2["passed"])
    add_exact("W2", "psl2_f5_order", pw2["psl2_f5_order"], rw2["leg5"]["psl2_f5_order"])
    add_exact("W2", "class_L_size", pw2["class_L_size"], rw2["leg5"]["conj_class_L_size"])
    add_exact("W2", "G3_order", pw2["G3_order"], rw2["chiral_freezing"]["g3_order"])
    add_exact("W2", "G3_char_defect_mismatches", pw2["G3_char_defect_mismatches"], rw2["chiral_freezing"]["char_defect_mismatches"])
    add_exact("W2", "rho_hom_ok", pw2["rho_hom_ok"], rw2["chiral_freezing"]["rho_hom_mismatches"] == 0)

    add_both_below("W2", "intertwine_max_err", pw2["intertwine_max_err"], max(rw2["leg5"]["intertwiner_errs"].values(), key=lambda s: mp.mpf(s)), mp.mpf("1e-30"))
    add_both_below("W2", "proj_max_err", pw2["proj_max_err"], max(rw2["leg5"]["projector_errs"].values(), key=lambda s: mp.mpf(s)), mp.mpf("1e-30"))
    add_both_below("W2", "spec_max_err", pw2["spec_max_err"], rw2["leg5"]["spec_err"], mp.mpf("1e-30"))
    add_both_below("W2", "wp_rational_err", pw2["wp_rational_err"], max(rw2["phi_wp"]["err_from_1_4"], rw2["phi_wp"]["err_from_7_23"], key=lambda s: mp.mpf(s)), mp.mpf("1e-30"))
    add_both_below("W2", "R5_sl2z_err", pw2["R5_sl2z_err"], max(rw2["phi_wp"]["sl2z_ratio_inv_err"], rw2["phi_siegel"]["sl2z_ratio_inv_err"], key=lambda s: mp.mpf(s)), mp.mpf("1e-30"))
    add_both_below("W2", "freeze_O27_vs_Q6_max_diff", pw2["freeze_O27_vs_Q6_max_diff"], rw2["chiral_freezing"]["max_o27_q6_diff_0_4"], mp.mpf("1e-25"))
    add_both_below("W2", "q6_exact_formula_err", pw2["q6_exact_formula_err"], rw2["chiral_freezing"]["max_q6_exact_err"], mp.mpf("1e-24"))

    add_num("W2", "R5_wp_omega_plus", pw2["R5_wp_omega_plus"], rw2["phi_wp"]["R5_omega_plus"], mp.mpf("1e-15"))
    add_num("W2", "R5_wp_tau_i", pw2["R5_wp_tau_i"], rw2["phi_wp"]["R5_i"], mp.mpf("1e-15"))
    add_num("W2", "R5_siegel_omega_plus", pw2["R5_siegel_omega_plus"], rw2["phi_siegel"]["R5_omega_plus"], mp.mpf("1e-15"))
    add_num("W2", "fb_siegel_omega_plus", pw2["fb_siegel_omega_plus"], rw2["phi_siegel"]["fb_omega_plus"], mp.mpf("1e-15"))
    add_num("W2", "R5_siegel_tau_i", pw2["R5_siegel_tau_i"], rw2["phi_siegel"]["R5_i"], mp.mpf("1e-15"))

    # All 4 x 7 = 28 Q_6 x Weil_N moments (N in {3, 5, 7, 9}, m = 0..6)
    for N in (3, 5, 7, 9):
        p_ms = pw2[f"q6_moments_N{N}"]
        r_ms = rw2["chiral_freezing"]["q6_weil_direct"][f"N{N}"]["moments_0_6_direct"]
        for m in range(7):
            tol_m = mp.mpf("1e-10") if abs(mp.mpf(r_ms[m])) > ONE else mp.mpf("1e-24")
            add_num("W2", f"q6_weil_N{N}_moment_m{m}", p_ms[m], r_ms[m], tol_m)

    # All 4 O_27 - Q_6 freezing max diffs (N in {3, 5, 7, 15})
    for N in (3, 5, 7, 15):
        add_both_below(
            "W2",
            f"o27_minus_q6_N{N}_max_0_4",
            pw2["freeze_summary"][str(N)]["max_abs_O27_minus_Q6"],
            rw2["chiral_freezing"]["o27_minus_q6_0_4"][f"N{N}"]["max_abs_diff_0_4"],
            mp.mpf("1e-25"),
        )

    # -----------------------------------------------------------------------
    # Module W3
    # -----------------------------------------------------------------------
    pw3 = prod["W3_analytic_lattice_theta_and_L15_stabilization"]
    rw3 = ref["W3"]

    add_exact("W3", "module_passed", pw3["ok"], rw3["passed"])
    add_exact("W3", "L7_boundary_peak_ok", pw3["L7_boundary_peak_ok"], rw3["stabilization"]["L7"]["boundary_global_max_ok"])
    add_exact("W3", "Lp15_boundary_peak_ok", pw3["L15_prime_boundary_peak_ok"], rw3["stabilization"]["Lp15"]["boundary_global_max_ok"])
    add_both_below("W3", "equiv_max_err", pw3["equiv_max_err"], rw3["max_sl2z_equiv_err"], mp.mpf("1e-30"))
    add_both_below("W3", "omega_plus_lock_max_leak", pw3["omega_plus_lock_max_leak"], rw3["max_omega_plus_leak"], mp.mpf("1e-30"))
    add_both_below("W3", "L3_odd_zero_norm", pw3["L3_odd_zero_norm"], rw3["l3_odd_vanishing_norm"], mp.mpf("1e-30"))

    # Boundary-peak V values for L7 and L'_15
    add_num("W3", "L7_V_omega_plus", pw3["L7_V_omega_plus"], rw3["stabilization"]["L7"]["V_omega_plus"], mp.mpf("1e-15"))
    add_num("W3", "L7_V_tau_i", pw3["L7_V_tau_i"], rw3["stabilization"]["L7"]["V_i"], mp.mpf("1e-15"))
    add_num("W3", "Lp15_V_omega_plus", pw3["L15_prime_V_omega_plus"], rw3["stabilization"]["Lp15"]["V_omega_plus"], mp.mpf("1e-15"))
    add_num("W3", "Lp15_V_tau_i", pw3["L15_prime_V_tau_i"], rw3["stabilization"]["Lp15"]["V_i"], mp.mpf("1e-15"))

    # Per-lattice omega_+ locked sector q checks
    lat_map = [("L_3", "L3"), ("L_7", "L7"), ("L_11", "L11"), ("L_15", "L15"), ("L_19", "L19"), ("L_15_prime", "Lp15")]
    for p_key, r_key in lat_map:
        prec = pw3["lattice_records"][p_key]
        rrec = rw3["omega_plus_locking"][r_key]
        add_exact("W3", f"{r_key}_even_locked_q2", prec["even"]["locked_sector_q"], 2)
        add_both_below("W3", f"{r_key}_even_omega_leak", prec["even"]["leak_omega_plus"], rrec["even_leak"], mp.mpf("1e-30"))
        if p_key == "L_3":
            add_exact("W3", "L3_odd_identically_zero", prec["odd"]["identically_zero"], mp.mpf(rrec["odd_identically_zero_norm"]) < mp.mpf("1e-30"))
        else:
            add_exact("W3", f"{r_key}_odd_locked_q1", prec["odd"]["locked_sector_q"], 1)
            add_both_below("W3", f"{r_key}_odd_omega_leak", prec["odd"]["leak_omega_plus"], rrec["odd_leak"], mp.mpf("1e-30"))

    # Interior stabilization coordinates, potentials, and 2D Hessians for L_11, L_15, L_19
    vxx_fd_note = "Producer 3-pt FD h=1e-4 vs Referee 5-pt Richardson O(h^6): exact relative O(h^2) truncation (2*pi*1e-4)^2/12 = 3.29e-8"
    for p_key, r_key in (("L_11", "L11"), ("L_15", "L15"), ("L_19", "L19")):
        ps = pw3["interior_stabilization"][p_key]
        rs = rw3["stabilization"][r_key]
        add_num("W3", f"{r_key}_V_omega_plus", ps["V_omega_plus"], rs["V_omega_plus"], mp.mpf("1e-15"))
        add_num("W3", f"{r_key}_V_tau_i", ps["V_tau_i"], rs["V_i"], mp.mpf("1e-15"))
        # x = 0 global interior max
        add_num("W3", f"{r_key}_x0_y_star", ps["x0"]["y_star"], rs["x0_max"]["y_star"], mp.mpf("1e-11"))
        add_num("W3", f"{r_key}_x0_V_star", ps["x0"]["V_star"], rs["x0_max"]["V_star"], mp.mpf("1e-15"))
        add_num("W3", f"{r_key}_x0_V_yy", ps["x0"]["V_yy"], rs["x0_max"]["Vyy"], mp.mpf("1e-11"), relative=True)
        add_num("W3", f"{r_key}_x0_V_xx", ps["x0"]["V_xx"], rs["x0_max"]["Vxx"], mp.mpf("1e-6"), relative=True, note=vxx_fd_note)
        add_exact("W3", f"{r_key}_x0_Vxx_neg", mp.mpf(ps["x0"]["V_xx"]) < ZERO, mp.mpf(rs["x0_max"]["Vxx"]) < ZERO)
        add_exact("W3", f"{r_key}_x0_Vyy_neg", mp.mpf(ps["x0"]["V_yy"]) < ZERO, mp.mpf(rs["x0_max"]["Vyy"]) < ZERO)
        # x = 1/2 saddle
        add_num("W3", f"{r_key}_xhalf_y_star", ps["x_half"]["y_star"], rs["xhalf_saddle"]["y_half"], mp.mpf("1e-11"))
        add_num("W3", f"{r_key}_xhalf_V_star", ps["x_half"]["V_star"], rs["xhalf_saddle"]["V_half"], mp.mpf("1e-15"))
        add_num("W3", f"{r_key}_xhalf_V_yy", ps["x_half"]["V_yy"], rs["xhalf_saddle"]["Vyy"], mp.mpf("1e-11"), relative=True)
        add_num("W3", f"{r_key}_xhalf_V_xx", ps["x_half"]["V_xx"], rs["xhalf_saddle"]["Vxx"], mp.mpf("1e-6"), relative=True, note=vxx_fd_note)
        add_exact("W3", f"{r_key}_xhalf_Vxx_pos", mp.mpf(ps["x_half"]["V_xx"]) > ZERO, mp.mpf(rs["xhalf_saddle"]["Vxx"]) > ZERO)
        add_exact("W3", f"{r_key}_xhalf_Vyy_neg", mp.mpf(ps["x_half"]["V_yy"]) < ZERO, mp.mpf(rs["xhalf_saddle"]["Vyy"]) < ZERO)

    # -----------------------------------------------------------------------
    # Module W4
    # -----------------------------------------------------------------------
    pw4 = prod["W4_disc15_genus_rank2_duality_and_obstruction"]
    rw4 = ref["W4"]

    add_exact("W4", "module_passed", pw4["ok"], rw4["passed"])
    add_exact("W4", "qseries_KMAX_over_15", pw4["qseries_KMAX_over_15"], rw4["l15_qseries_identities"]["max_degree_t"])
    add_exact("W4", "qseries_AD_plus_BC_zero", pw4["qseries_det_AD_plus_BC_zero"], rw4["l15_qseries_identities"]["AD_plus_BC_zero"])
    add_exact("W4", "qseries_B_A20_minus_D_A21_zero", pw4["qseries_B_A2_0_eq_D_A2_1"], rw4["l15_qseries_identities"]["B_a20_minus_D_a21_zero"])
    add_exact("W4", "qseries_A_A20_plus_C_A21_zero", pw4["qseries_A_A2_0_eq_neg_C_A2_1"], rw4["l15_qseries_identities"]["A_a20_plus_C_a21_zero"])
    add_exact(
        "W4",
        "swap_coset_P_flip3_ok",
        pw4["swap_coset_P_flip3_ok"],
        rw4["lp15_swap_isometry"]["minus4_mod3_eq_minus1"] and rw4["lp15_swap_isometry"]["minus4_mod5_eq_plus1"],
    )
    add_exact("W4", "rank_duality_ok", pw4["rank_duality_ok"], rw4["all_rank_duality_ok"])
    add_both_below("W4", "J_max_abs", pw4["J_max_abs"], rw4["max_jarlskog"], mp.mpf("1e-28"))
    add_both_below("W4", "sl2z_V_max_err", pw4["sl2z_V_max_err"], rw4["max_sl2z_mix_err"], mp.mpf("1e-28"))
    add_both_below("W4", "haar_10trial_max_err", pw4["haar_10trial_max_err"], max(rw4["haar_10trials_max_sv_err"], rw4["haar_10trials_max_mix_err"], key=lambda s: mp.mpf(s)), mp.mpf("1e-28"))

    # L_15 at tau0: singular value ratios + all 9 entries of |V_{3x3}|
    pg15 = pw4["genus"]["L_15"]
    rg15 = rw4["genus_crt_svd"]["L15"]["points"]["tau0"]
    add_num("W4", "L15_tau0_sv_even_r2", pg15["sv_even_ratios_tau0"][1], rg15["sv_ratios_even"][0], mp.mpf("1e-11"))
    add_num("W4", "L15_tau0_sv_even_r3", pg15["sv_even_ratios_tau0"][2], rg15["sv_ratios_even"][1], mp.mpf("1e-11"))
    add_num("W4", "L15_tau0_sv_odd_r2", pg15["sv_odd_ratios_tau0"][1], rg15["sv_ratios_odd"][0], mp.mpf("1e-11"))
    add_both_below("W4", "L15_tau0_sv_odd_r3_zero", pg15["sv_odd_ratios_tau0"][2], rg15["sv_ratios_odd"][1], mp.mpf("1e-22"))
    for i in range(3):
        for j in range(3):
            add_num("W4", f"L15_tau0_absV_{i}{j}", pg15["abs_V_tau0"][i][j], rg15["abs_V_3x3"][i][j], mp.mpf("1e-9"))

    # L_15 at tau_star: singular value ratios + 2x2 off-diagonal mixing + J
    pg15s = pw4["genus"]["L_15_at_tau_star"]
    rg15s = rw4["genus_crt_svd"]["L15"]["points"]["tau_star_L15"]
    add_num("W4", "L15_taustar_sv_even_r2", pg15s["sv_even_ratios"][1], rg15s["sv_ratios_even"][0], mp.mpf("1e-11"))
    add_num("W4", "L15_taustar_sv_even_r3", pg15s["sv_even_ratios"][2], rg15s["sv_ratios_even"][1], mp.mpf("1e-11"))
    add_num("W4", "L15_taustar_sv_odd_r2", pg15s["sv_odd_ratios"][1], rg15s["sv_ratios_odd"][0], mp.mpf("1e-11"))
    add_both_below("W4", "L15_taustar_sv_odd_r3_zero", pg15s["sv_odd_ratios"][2], rg15s["sv_ratios_odd"][1], mp.mpf("1e-22"))
    add_num("W4", "L15_taustar_absV_2x2_offdiag", pg15s["abs_V_2x2_offdiag"], rg15s["abs_V_3x3"][0][1], mp.mpf("1e-11"))
    add_both_below("W4", "L15_taustar_J", pg15s["J"], rg15s["jarlskog_J"], mp.mpf("1e-28"))

    # L'_15 at tau0: singular value ratios + all 9 entries of |V_{3x3}| + swap_vec_err
    pg15p = pw4["genus"]["L_15_prime"]
    rg15p = rw4["genus_crt_svd"]["Lp15"]["points"]["tau0"]
    add_num("W4", "Lp15_tau0_sv_even_r2", pg15p["sv_even_ratios_tau0"][1], rg15p["sv_ratios_even"][0], mp.mpf("1e-11"))
    add_both_below("W4", "Lp15_tau0_sv_even_r3_zero", pg15p["sv_even_ratios_tau0"][2], rg15p["sv_ratios_even"][1], mp.mpf("1e-22"))
    add_num("W4", "Lp15_tau0_sv_odd_r2", pg15p["sv_odd_ratios_tau0"][1], rg15p["sv_ratios_odd"][0], mp.mpf("1e-11"))
    add_num("W4", "Lp15_tau0_sv_odd_r3", pg15p["sv_odd_ratios_tau0"][2], rg15p["sv_ratios_odd"][1], mp.mpf("1e-11"))
    add_both_below("W4", "Lp15_swap_vec_err", pg15p["swap_vec_err"], rw4["lp15_swap_isometry"]["even_swap_invariance_err"], mp.mpf("1e-30"))
    for i in range(3):
        for j in range(3):
            add_num("W4", f"Lp15_tau0_absV_{i}{j}", pg15p["abs_V_tau0"][i][j], rg15p["abs_V_3x3"][i][j], mp.mpf("1e-9"))

    # -----------------------------------------------------------------------
    # Manifest Integrity Verification across Producer and Referee directories
    # -----------------------------------------------------------------------
    manifests = [
        verify_sha256_manifest(PROD_DIR, "SCRIPT_SHA256.txt"),
        verify_sha256_manifest(PROD_DIR, "OUTPUT_SHA256.txt"),
        verify_sha256_manifest(REF_DIR, "SCRIPT_SHA256.txt"),
        verify_sha256_manifest(REF_DIR, "OUTPUT_SHA256.txt"),
    ]
    all_manifests_ok = all(m["all_ok"] for m in manifests)

    discrepancies = [c for c in checks if not c["matched"]]
    matched_count = len(checks) - len(discrepancies)
    verdict = "PASS" if (
        len(discrepancies) == 0
        and ref["all_referee_gates_passed"]
        and prod["all_gates_passed"]
        and all_manifests_ok
    ) else "FAIL"

    # Quantitative diagnostic summary of the W3 V_xx FD-order difference
    vxx_diag: Dict[str, Any] = {}
    for p_key, r_key in (("L_11", "L11"), ("L_15", "L15"), ("L_19", "L19")):
        pv = mp.mpf(pw3["interior_stabilization"][p_key]["x0"]["V_xx"])
        rv = mp.mpf(rw3["stabilization"][r_key]["x0_max"]["Vxx"])
        vxx_diag[r_key] = {
            "producer_Vxx_3pt": pw3["interior_stabilization"][p_key]["x0"]["V_xx"],
            "referee_Vxx_5pt_rich": rw3["stabilization"][r_key]["x0_max"]["Vxx"],
            "relative_diff": sci(abs(pv - rv) / abs(rv)),
            "expected_3pt_h1e_4_truncation": sci((mp.mpf(2) * mp.pi * mp.mpf("1e-4")) ** 2 / mp.mpf(12)),
        }

    out: Dict[str, Any] = {
        "card_id": "A2-WEIL-CHIRAL-LATTICE-BRIDGE",
        "seat_code": "fam3-v1-high-03",
        "blindness": "0_of_19",
        "compare_script_ast_floats": check_ast_zero_floats(Path(__file__).resolve()),
        "total_checks": len(checks),
        "matched_checks": matched_count,
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "all_manifests_ok": all_manifests_ok,
        "manifests": manifests,
        "w3_vxx_fd_truncation_diagnostic": vxx_diag,
        "verdict": verdict,
        "json_float_literal_count": 0,
        "checks": checks,
    }
    n_floats = count_json_floats(out)
    out["json_float_literal_count"] = n_floats
    if n_floats != 0 or out["compare_script_ast_floats"] != 0:
        out["verdict"] = "FAIL"

    DIFF_JSON.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"CROSS-DIFF CARD: A2-WEIL-CHIRAL-LATTICE-BRIDGE (seat fam3-v1-high-03)")
    print(f"TOTAL_CHECKS={len(checks)} MATCHED={matched_count} DISCREPANCIES={len(discrepancies)} MANIFESTS_OK={all_manifests_ok} JSON_FLOATS={n_floats} VERDICT={out['verdict']}")
    return 0 if out["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
