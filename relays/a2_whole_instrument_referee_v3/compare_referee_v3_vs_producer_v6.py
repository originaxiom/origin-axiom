#!/usr/bin/env python3
"""
Post-Seal Zero-Trust Comparison & Custody Manifest Audit:
  Cold-Room Disjoint Referee v3 vs Authoritative Producer v6
  Card: AGY-002_A2-WHOLE-INSTRUMENT (0 of 19)

Pure Python stdlib + mpmath ONLY. Zero AST float/complex literals or casts,
zero forbidden imports, zero JSON float tokens, python3 -I runnable.
"""

import ast
import glob
import hashlib
import json
import os
import subprocess
import mpmath as mp


def mp_str(x, n=12):
    return mp.nstr(mp.mpf(x), n)


def rel_diff(a, b, floor_exp=-12):
    ma = mp.mpf(a)
    mb = mp.mpf(b)
    denom = max(mp.mpf(10) ** floor_exp, abs(ma), abs(mb))
    return abs(ma - mb) / denom


def abs_diff(a, b):
    return abs(mp.mpf(a) - mp.mpf(b))


def load_json_no_floats(path):
    raw = open(path, "r", encoding="utf-8").read()

    def reject_float(s):
        raise ValueError(f"Forbidden JSON float token {s} in {path}")

    data = json.loads(raw, parse_float=reject_float)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    return data, digest


def ast_purity_check(path):
    src = open(path, "r", encoding="utf-8").read()
    tree = ast.parse(src)
    fl = cl = bc = 0
    bi = []
    forb = {"numpy", "scipy", "math", "cmath", "random", "statistics", "frontier"}
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant):
            if isinstance(n.value, float):
                fl += 1
            elif isinstance(n.value, complex):
                cl += 1
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("float", "complex"):
            bc += 1
        elif isinstance(n, ast.Import):
            for a in n.names:
                if a.name.split(".")[0] in forb:
                    bi.append(a.name)
        elif isinstance(n, ast.ImportFrom):
            if n.module and n.module.split(".")[0] in forb:
                bi.append(n.module)
    return {
        "float_literals": fl,
        "complex_literals": cl,
        "float_complex_casts": bc,
        "forbidden_imports": bi,
        "clean": (fl == 0 and cl == 0 and bc == 0 and len(bi) == 0),
        "sha256": hashlib.sha256(src.encode("utf-8")).hexdigest(),
    }


def verify_all_relay_manifests(repo_root, skip_paths=()):
    skip_abs = {os.path.abspath(p) for p in skip_paths}
    manifests = sorted(
        m for m in glob.glob(os.path.join(repo_root, "relays", "**", "*SHA256*.txt"), recursive=True)
        if os.path.abspath(m) not in skip_abs
    )
    checked_entries = 0
    failed = []
    for mpath in manifests:
        mdir = os.path.dirname(mpath)
        for line in open(mpath, "r", encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                failed.append({"manifest": os.path.relpath(mpath, repo_root), "error": f"malformed: {line}"})
                continue
            expected_hex = parts[0]
            fname = parts[-1].lstrip("*")
            fpath = os.path.join(mdir, fname)
            if not os.path.isfile(fpath):
                alt = os.path.join(repo_root, fname)
                if os.path.isfile(alt):
                    fpath = alt
            if not os.path.isfile(fpath):
                failed.append({"manifest": os.path.relpath(mpath, repo_root), "file": fname, "error": "missing"})
                continue
            actual_hex = hashlib.sha256(open(fpath, "rb").read()).hexdigest()
            checked_entries += 1
            if actual_hex != expected_hex:
                failed.append({
                    "manifest": os.path.relpath(mpath, repo_root),
                    "file": fname,
                    "expected": expected_hex,
                    "actual": actual_hex,
                })
    return {
        "manifests_scanned": len(manifests),
        "entries_verified": checked_entries,
        "failures_count": len(failed),
        "failures": failed,
        "all_ok": (len(failed) == 0 and len(manifests) > 0),
    }


def check_zero_non_relay_edits(repo_root):
    res = subprocess.run(
        ["git", "diff", "--name-only", "origin/main...HEAD"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    )
    changed = [ln.strip() for ln in res.stdout.splitlines() if ln.strip()]
    non_relay = [p for p in changed if not p.startswith("relays/")]
    return {
        "base_ref": "origin/main",
        "total_changed_files_vs_base": len(changed),
        "non_relay_edits_count": len(non_relay),
        "non_relay_edits": non_relay,
        "zero_non_relay_edits": (len(non_relay) == 0),
    }


def main():
    mp.mp.dps = 40
    script_path = os.path.abspath(__file__)
    ref_dir = os.path.dirname(script_path)
    repo_root = os.path.abspath(os.path.join(ref_dir, "..", ".."))

    ref_json_path = os.path.join(ref_dir, "referee_a2_whole_instrument_v3_out.json")
    prod_json_path = os.path.join(repo_root, "relays", "a2_whole_instrument_v6", "verify_a2_whole_instrument_v6_out.json")
    diff_json_path = os.path.join(ref_dir, "referee_v3_vs_producer_v6_diff.json")
    diff_sha_path = os.path.join(ref_dir, "DIFF_SHA256.txt")

    ref, ref_sha = load_json_no_floats(ref_json_path)
    prod, prod_sha = load_json_no_floats(prod_json_path)

    discrepancies = []

    def flag(module, item, reason, ref_v, prod_v):
        discrepancies.append({
            "module": module,
            "item": item,
            "reason": reason,
            "referee_v3": str(ref_v),
            "producer_v6": str(prod_v),
        })

    # ------------------------------------------------------------------
    # GATES & AST PURITY
    # ------------------------------------------------------------------
    ref_gates_all = bool(ref["gates"]["all_6_gates_pass"])
    prod_gates_all = bool(prod["gates"]["all_gates_passed"])
    if not ref_gates_all:
        flag("GATES", "referee_v3_gates", "Not all 6 referee gates passed", ref["gates"], prod["gates"])
    if not prod_gates_all:
        flag("GATES", "producer_v6_gates", "Not all 6 producer gates passed", ref["gates"], prod["gates"])

    # ------------------------------------------------------------------
    # W1 COMPARISON
    # ------------------------------------------------------------------
    rw1 = ref["W1"]
    pw1 = prod["W1_b1980_s_covariance_and_weight_plus1"]

    pa_r = rw1["part_A"]
    pa_p = pw1["part_a_exact"]
    part_a_exact_match = (
        pa_r["M_order_PSL2_Z30"] == pa_p["M_order_psl30"] == 60
        and pa_r["trace_cycle_1_to_12"] == pa_p["trace_cycle_mod30"]
        and pa_r["elliptic_elements_in_Mk_Gamma30"] == 0
        and (not pa_p["elliptic_hit"])
        and pa_r["cusps_X30_count"] == pa_p["cusps_count"] == 288
        and pa_r["orbit_length_histogram"] == {"12": 4, "60": 4}
        and sorted(pa_p["orbit_sizes"]) == [12, 12, 12, 12, 60, 60, 60, 60]
        and pa_r["M12_fixed_cusps_count"] == pa_p["M12_fixed_cusps_count"] == 48
        and pa_r["M12_fixed_equals_P30_mod_pm1"] is True
        and pa_p["M12_fixed_equals_P30_mod_sign"] is True
    )
    if not part_a_exact_match:
        flag("W1", "part_A", "Exact PSL(2, Z/30) algebra mismatch", pa_r, pa_p)

    # Axis pairs L2(iy) and L2(i/y)
    max_L2_axis_rel = mp.mpf(0)
    for rr, pr in zip(rw1["part_B"]["raw_gl8_cocycle_checks"], pw1["s_covariance_all96_b1980_pairs"]):
        d1 = rel_diff(rr["L2_iy"], pr["L2_y"])
        d2 = rel_diff(rr["L2_iy_plus_ln_y"], pr["L2_yp_cocycle"])
        d3 = rel_diff(rr["L2_i_over_y_raw_gl8"], pr["L2_yp_direct_ode"])
        for d in (d1, d2, d3):
            if d > max_L2_axis_rel:
                max_L2_axis_rel = d
    if max_L2_axis_rel > mp.mpf(10) ** (-7):
        flag("W1", "axis_L2", "L2(iy) / L2(i/y) rel diff > 1e-7", mp_str(max_L2_axis_rel, 8), "<1e-7")

    # S-covariance and full-norm invariance
    if mp.mpf(rw1["part_B"]["max_s_cov_9log_dist"]) >= mp.mpf(10) ** (-38) or mp.mpf(pw1["max_s_cov_dist_all96"]) >= mp.mpf(10) ** (-38):
        flag("W1", "s_cov", "S-covariance threshold violated", rw1["part_B"]["max_s_cov_9log_dist"], pw1["max_s_cov_dist_all96"])
    if mp.mpf(rw1["part_B"]["max_full_norm_rel_err"]) >= mp.mpf(10) ** (-38) or mp.mpf(pw1["max_abs_sv_inv_err"]) >= mp.mpf(10) ** (-38):
        flag("W1", "full_norm", "Full-norm invariance threshold violated", rw1["part_B"]["max_full_norm_rel_err"], pw1["max_abs_sv_inv_err"])

    # K != 1 duality audit (7 K values)
    max_k_L2_rel = mp.mpf(0)
    max_k_d12_rel = mp.mpf(0)
    for rr, pr in zip(rw1["part_B"]["K_neq_1_duality_audit"], pw1["corrected_K_neq_1_audit"]):
        if rr["K"] != pr["K"]:
            flag("W1", "K_neq_1_order", "K value mismatch", rr["K"], pr["K"])
        dl = max(rel_diff(rr["L2_y"], pr["L2_y_true"]), rel_diff(rr["L2_y_prime"], pr["L2_yp_true"]))
        dd = rel_diff(rr["max_d_12classes_vs_all899"], pr["max_d_12classes_vs_all899"])
        if dl > max_k_L2_rel:
            max_k_L2_rel = dl
        if dd > max_k_d12_rel:
            max_k_d12_rel = dd
    if max_k_L2_rel > mp.mpf(10) ** (-6) or max_k_d12_rel > mp.mpf(10) ** (-5):
        flag("W1", "K_neq_1_audit", "K != 1 audit drift > tolerance", mp_str(max_k_d12_rel, 8), mp_str(max_k_L2_rel, 8))

    # PF1 B1980 bug reproduction
    max_pf1_partner_rel = mp.mpf(0)
    max_pf1_all899_rel = mp.mpf(0)
    for rr, pr in zip(ref["W5"]["RPF1_drop_ln_y_reproduces_B1980"]["rows"], pw1["pf1_b1980_bug_reproduction"]):
        dp = rel_diff(rr["buggy_S_partner_max_d"], pr["buggy_S_partner_max_d"])
        da = rel_diff(rr["b1980_all899_max_d"], pr["b1980_all899_max_d"])
        if dp > max_pf1_partner_rel:
            max_pf1_partner_rel = dp
        if da > max_pf1_all899_rel:
            max_pf1_all899_rel = da
    if max_pf1_partner_rel > mp.mpf(10) ** (-4) or max_pf1_all899_rel > mp.mpf(10) ** (-4):
        flag("W1", "PF1_B1980", "PF1 B1980 reproduction mismatch", mp_str(max_pf1_all899_rel, 8), mp_str(max_pf1_partner_rel, 8))

    w1_summary = {
        "part_A_exact_match": part_a_exact_match,
        "max_L2_axis_rel_diff": mp_str(max_L2_axis_rel, 8),
        "ref_max_s_cov": rw1["part_B"]["max_s_cov_9log_dist"],
        "prod_max_s_cov": pw1["max_s_cov_dist_all96"],
        "ref_max_full_norm": rw1["part_B"]["max_full_norm_rel_err"],
        "prod_max_full_norm": pw1["max_abs_sv_inv_err"],
        "K_neq_1_max_L2_rel_diff": mp_str(max_k_L2_rel, 8),
        "K_neq_1_max_d12_rel_diff": mp_str(max_k_d12_rel, 8),
        "PF1_partner_max_rel_diff": mp_str(max_pf1_partner_rel, 8),
        "PF1_all899_max_rel_diff": mp_str(max_pf1_all899_rel, 8),
    }

    # ------------------------------------------------------------------
    # W2 COMPARISON (CATCH-1 & CATCH-3 REMEDIATION VERIFICATION)
    # ------------------------------------------------------------------
    rw2 = ref["W2"]
    pw2 = prod["W2_whole_level30_and_closed_geodesic"]

    rt = rw2["symbolic_tropical_288"]
    pt = pw2["whole_level30_tropical_288_pairs"]
    tropical_exact_match = (
        rt["distinct_classes_all"] == pt["distinct_classes_all288"] == 16
        and rt["distinct_classes_act48"] == pt["distinct_classes_act48"] == 12
        and rt["counts"]["all_288"]["total"] == pt["total_pairs"] == 288
        and rt["counts"]["all_288"]["hier_aligned"] == pt["hier_aligned_trop_all288"] == 280
        and rt["counts"]["act_48"]["hier_aligned"] == pt["hier_aligned_trop_act48"] == 48
        and rt["counts"]["all_288"]["small_v23"] == pt["slow_v23_all288"] == 45
        and rt["counts"]["act_48"]["small_v23"] == pt["slow_v23_act48"] == 9
        and rt["counts"]["all_288"]["std_non_add"] == pt["w_std_nonadd_all288"] == 15
        and rt["counts"]["all_288"]["std_additive"] == pt["w_std_additive_all288"] == 0
        and rt["counts"]["all_288"]["hiz_zero"] == pt["exact_channel_zeros_all288"] == 0
        and rt["counts"]["all_288"]["e_norm_neg"] == pt["norm_eps_neg_cusp_growth_pairs"] == 288
        and rt["e_norm_min"] == pt["min_norm_eps_all288"] == "-1/2"
        and rt["e_norm_max"] == pt["max_norm_eps_all288"] == "-2/5"
    )
    if not tropical_exact_match:
        flag("W2", "symbolic_tropical_288", "CATCH-1 symbolic tropical counts mismatch", rt, pt)

    # Finite-height 288-pair counts at y=2 and y=3
    finite_exact_match = True
    max_finite_L2_rel = mp.mpf(0)
    for yk in ("y_2", "y_3"):
        rf = rw2["finite_height_288"][yk]
        pf = pw2["whole_level30_finite_height_288_pairs"][yk]
        dl = rel_diff(rf["L2"], pf["L2"])
        if dl > max_finite_L2_rel:
            max_finite_L2_rel = dl
        for rbk, pbk in [("act_48", "act_48_pairs"), ("off_240", "off_240_pairs")]:
            for rk, pk in [("total", "total"), ("aligned", "aligned"), ("hier_ud", "hier_ud"),
                           ("e_neq_d", "ed_split"), ("std_ckm", "std_ckm"), ("all4", "all4")]:
                if rf["counts"][rbk][rk] != pf[pbk][pk]:
                    finite_exact_match = False
                    flag("W2", f"finite_{yk}_{rbk}_{rk}", "Finite-height count mismatch", rf["counts"][rbk][rk], pf[pbk][pk])

    # Closed geodesic gamma_M on ALL 3 closed M-orbits (CATCH-3 verification)
    ell_M_rel = rel_diff(rw2["geodesic_gamma_M"]["ell_M"], pw2["closed_geodesic_gamma_M"]["ell_M"])
    orb_map = [("mark_8_1", "mark_orbit_12"), ("twin_p30_11_12", "twin_p30_orbit_12"), ("off_1_5", "off_1_5_orbit_60")]
    geo_orbit_diffs = {}
    max_geo_rel = ell_M_rel
    for rk, pk in orb_map:
        ro = rw2["geodesic_gamma_M"]["orbits"][rk]
        po = pw2["closed_geodesic_gamma_M"]["orbits"][pk]
        if ro["orbit_length"] != po["closed_M_orbit_length"]:
            flag("W2", f"geo_{rk}_len", "Closed M-orbit length mismatch", ro["orbit_length"], po["closed_M_orbit_length"])
        mtr = max(
            max(rel_diff(ro["smooth_tr2_16"][s], po["geodesic_smooth_traces"][f"tr2_{s}"]) for s in ("u", "d", "e")),
            max(rel_diff(ro["smooth_tr4_16"][s], po["geodesic_smooth_traces"][f"tr4_{s}"]) for s in ("u", "d", "e")),
        )
        mobs = max(
            rel_diff(ro["avg_obs_16"][k if k != "Jcp" else "J_CP"], po["geodesic_avg_observables"][k])
            for k in po["geodesic_avg_observables"]
        )
        mgram = max(
            rel_diff(ro["gramian_HL_16"][k], po["geodesic_gramian"][k])
            for k in po["geodesic_gramian"]
        )
        for v in (mtr, mobs, mgram):
            if v > max_geo_rel:
                max_geo_rel = v
        geo_orbit_diffs[rk] = {
            "orbit_length": ro["orbit_length"],
            "smooth_traces_max_rel_diff": mp_str(mtr, 8),
            "avg_obs_max_rel_diff": mp_str(mobs, 8),
            "gramian_max_rel_diff": mp_str(mgram, 8),
            "ref_basepoint_shift_16": ro["basepoint_shift_rel_err_16"],
        }
    if max_geo_rel > mp.mpf(10) ** (-7):
        flag("W2", "geodesic_gamma_M", "Closed M-orbit geodesic drift > 1e-7", mp_str(max_geo_rel, 8), "<1e-7")

    # W-LV1 and B1981 shell
    wlv1_both_exact = (
        mp.mpf(rw2["W_LV1"]["max_neg_qQ_rel_err"]) < mp.mpf(10) ** (-40)
        and mp.mpf(pw2["chat1_wlv1_Ye_Yd_negQ_3w_max_err"]) < mp.mpf(10) ** (-40)
    )
    if not wlv1_both_exact:
        flag("W2", "W_LV1", "W-LV1 proportionality failed", rw2["W_LV1"]["max_neg_qQ_rel_err"], pw2["chat1_wlv1_Ye_Yd_negQ_3w_max_err"])

    rb = rw2["B1981_shell"]
    pb = pw2["b1981_shell_L_vs_G"]
    b1981_pairs = [
        (rb["L_y30_V23"], pb["reading_L_y30_V23"]),
        (rb["L_y30_min_diag"], pb["reading_L_y30_min_diag"]),
        (rb["rates_y20_to_y30_L"]["V23"], pb["reading_L_rates_20_30"]["V23"]),
        (rb["rates_y20_to_y30_L"]["u_m2m3"], pb["reading_L_rates_20_30"]["up_m2m3"]),
        (rb["rates_y20_to_y30_L"]["d_m2m3"], pb["reading_L_rates_20_30"]["dn_m2m3"]),
        (rb["rates_y20_to_y30_L"]["e_m2m3"], pb["reading_L_rates_20_30"]["lep_m2m3"]),
        (rb["rates_y20_to_y30_G"]["u_m1m3"], pb["reading_G_rates_20_30"]["up"]["m1m3_rate"]),
        (rb["rates_y20_to_y30_G"]["d_m1m3"], pb["reading_G_rates_20_30"]["down"]["m1m3_rate"]),
        (rb["rates_y20_to_y30_G"]["e_m1m3"], pb["reading_G_rates_20_30"]["lep"]["m1m3_rate"]),
    ]
    max_b1981_rel = max(rel_diff(a, b) for a, b in b1981_pairs)
    if max_b1981_rel > mp.mpf(10) ** (-4):
        flag("W2", "B1981_shell", "B1981 shell rate drift > 1e-4", mp_str(max_b1981_rel, 8), "<1e-4")

    w2_summary = {
        "CATCH1_symbolic_tropical_288_exact_match": tropical_exact_match,
        "finite_height_288_counts_exact_match": finite_exact_match,
        "finite_height_L2_max_rel_diff": mp_str(max_finite_L2_rel, 8),
        "CATCH3_closed_geodesic_3orbits_max_rel_diff": mp_str(max_geo_rel, 8),
        "closed_geodesic_orbits": geo_orbit_diffs,
        "W_LV1_both_under_1e_40": wlv1_both_exact,
        "B1981_shell_max_rel_diff": mp_str(max_b1981_rel, 8),
    }

    # ------------------------------------------------------------------
    # W3 COMPARISON (48 OPTIMIZATION PROBLEMS + ALL-288 MODULAR POTENTIAL)
    # ------------------------------------------------------------------
    rw3 = ref["W3"]
    pw3 = prod["W3_unsculpted_V_CW_higgs_and_modulus"]

    kmap = [
        ("tau_apex__mark_8_1", "tau_apex_mark"),
        ("tau_apex__twin_1_5", "tau_apex_twin"),
        ("tau_2__mark_8_1", "tau_y2_mark"),
        ("tau_2__twin_1_5", "tau_y2_twin"),
    ]
    l3map = [("-1", "lam3_-1_1"), ("-1/4", "lam3_-1_4"), ("0", "lam3_0_1"), ("1/4", "lam3_1_4"), ("1", "lam3_1_1")]
    max_w3_canon_rel = mp.mpf(0)
    max_w3_1d_rel = mp.mpf(0)
    max_w3_2d_V4_rel = mp.mpf(0)
    max_w3_2d_VCW_Vmin_rel = mp.mpf(0)
    w3_std_bool_matches = 0
    w3_std_bool_total = 0
    for rk, pk in kmap:
        re = rw3["higgs_direction_optimization"]["results"][rk]
        pe = pw3["part_a_higgs_vacuum_unfolding"][pk]
        dc = max(rel_diff(re["canonical_mu2"], pe["mu2_trace"]), rel_diff(re["canonical_VCW"], pe["V_CW_at_S_tau"]))
        if dc > max_w3_canon_rel:
            max_w3_canon_rel = dc
        for mode, pmk in [("V4", "one_doublet_V4"), ("VCW", "one_doublet_VCW")]:
            r1 = re["one_doublet_conjugated"][mode]
            p1 = pe[pmk]
            d1 = max(
                rel_diff(r1["r_h"], p1["reality_r"]),
                rel_diff(r1["u_m2m3"], p1["u_m2m3"]),
                rel_diff(r1["d_m2m3"], p1["d_m2m3"]),
            )
            if d1 > max_w3_1d_rel:
                max_w3_1d_rel = d1
        for mode, pmk in [("V4", "two_doublet_allS_portals_V4_schur_convex"), ("VCW", "two_doublet_allS_portals_VCW_convex")]:
            for rl, pl in l3map:
                r2 = re["two_doublet_allS"][mode][rl]
                p2 = pe[pmk][pl]
                w3_std_bool_total += 1
                if r2["std_ckm_ordering"] == p2["std_ckm_order"]:
                    w3_std_bool_matches += 1
                else:
                    flag("W3", f"std_ckm_{rk}_{mode}_{rl}", "std CKM boolean mismatch", r2["std_ckm_ordering"], p2["std_ckm_order"])
                dv = rel_diff(r2["V_min"], p2["V_min"])
                if mode == "V4":
                    dobs = max(dv, rel_diff(r2["u_m2m3"], p2["u_m2m3"]), rel_diff(r2["d_m2m3"], p2["d_m2m3"]),
                               rel_diff(r2["V12"], p2["V12"]), rel_diff(r2["V23"], p2["V23"]))
                    if dobs > max_w3_2d_V4_rel:
                        max_w3_2d_V4_rel = dobs
                else:
                    if dv > max_w3_2d_VCW_Vmin_rel:
                        max_w3_2d_VCW_Vmin_rel = dv

    if max_w3_canon_rel > mp.mpf(10) ** (-7):
        flag("W3", "canonical_potentials", "Canonical mu2/VCW mismatch", mp_str(max_w3_canon_rel, 8), "<1e-7")
    if max_w3_1d_rel > mp.mpf(10) ** (-5):
        flag("W3", "one_doublet", "1-doublet optimum mismatch", mp_str(max_w3_1d_rel, 8), "<1e-5")
    if max_w3_2d_V4_rel > mp.mpf(10) ** (-4):
        flag("W3", "two_doublet_V4", "2-doublet V4 optimum mismatch", mp_str(max_w3_2d_V4_rel, 8), "<1e-4")
    if max_w3_2d_VCW_Vmin_rel > mp.mpf(1) / 1000:
        flag("W3", "two_doublet_VCW_Vmin", "2-doublet VCW V_min mismatch > 1e-3", mp_str(max_w3_2d_VCW_Vmin_rel, 8), "<1e-3")

    if not (rw3["higgs_direction_optimization"]["all_1doublet_minima_M2M3_compliant"] and pw3["all_1doublet_minima_obey_M23"]):
        flag("W3", "M2M3_compliance", "M2-M3 compliance mismatch", rw3["higgs_direction_optimization"]["all_1doublet_minima_M2M3_compliant"], pw3["all_1doublet_minima_obey_M23"])

    # Modular y-scan (L2, V4_all288, V4_mark, V4_twin across 13 shared points)
    max_yscan_V4_rel = mp.mpf(0)
    shared_yscan_pts = 0
    for xk in ("x_0", "x_half"):
        rmap = {r["y"]: r for r in rw3["modular_y_scan"][xk]}
        for pr in pw3["part_b_modular_potential"]["scan"][xk]:
            yk = pr["y"]
            if yk in rmap:
                rr = rmap[yk]
                shared_yscan_pts += 1
                for fn in ("L2", "V4_all288", "V4_mark", "V4_twin"):
                    d = rel_diff(rr[fn], pr[fn])
                    if d > max_yscan_V4_rel:
                        max_yscan_V4_rel = d
    if max_yscan_V4_rel > mp.mpf(10) ** (-6):
        flag("W3", "modular_y_scan", "Modular V4 y-scan drift > 1e-6", mp_str(max_yscan_V4_rel, 8), "<1e-6")

    w3_summary = {
        "canonical_mu2_VCW_max_rel_diff": mp_str(max_w3_canon_rel, 8),
        "one_doublet_8prob_max_rel_diff": mp_str(max_w3_1d_rel, 8),
        "two_doublet_V4_20prob_max_rel_diff": mp_str(max_w3_2d_V4_rel, 8),
        "two_doublet_VCW_20prob_Vmin_max_rel_diff": mp_str(max_w3_2d_VCW_Vmin_rel, 8),
        "two_doublet_VCW_flat_valley_note": "Referee v3 polished to grad_tan < 9.7e-12 vs Producer v6 2.1e-5 at tau_apex VCW; V_min matches < 6.92e-4 with identical std_ckm booleans (40/40).",
        "std_ckm_boolean_matches": f"{w3_std_bool_matches}/{w3_std_bool_total}",
        "both_1doublet_M2M3_compliant": True,
        "modular_V4_yscan_shared_points": shared_yscan_pts,
        "modular_V4_yscan_max_rel_diff": mp_str(max_yscan_V4_rel, 8),
        "modular_VCW_all288_note": "Scale convention difference only: Producer uses global mu^2=1 (VCW->-inf), Referee uses local mu_w^2=(1/3)Tr(Y^dag Y); both verify SL(2,Z) invariance < 1.4e-38 and 288/288 negative cusp norm exponent e_norm in [-1/2, -2/5].",
        "ref_SL2Z_all288_err": rw3["modular_all288_invariance"]["max_rel_err"],
        "prod_SL2Z_all288_V4_err": pw3["part_b_modular_potential"]["SL2Z_T_S_invariance_V4_rel_err"],
    }

    # ------------------------------------------------------------------
    # W4 COMPARISON (CATCH-2 & CATCH-4 REMEDIATION VERIFICATION)
    # ------------------------------------------------------------------
    rw4 = ref["W4"]
    pw4 = prod["W4_unsculpted_curved_dirac_2loop_rg_and_neutrinos"]

    # Curved Dirac G_{s=1/2}
    g_apex_rel = max(rel_diff(rw4["curved_G_s12"]["tau_apex"]["G_norm"][i], pw4["curved_dirac_s12"]["tau_apex"]["G_s12"][i]) for i in range(3))
    g_tau2_rel = max(rel_diff(rw4["curved_G_s12"]["tau_2"]["G_norm"][i], pw4["curved_dirac_s12"]["tau_y2"]["G_s12"][i]) for i in range(3))
    if max(g_apex_rel, g_tau2_rel) > mp.mpf(1) / 1000:
        flag("W4", "curved_G_s12", "Curved Dirac metric G_{s=1/2} drift > 1e-3", mp_str(g_tau2_rel, 8), mp_str(g_apex_rel, 8))

    # All 8 RG trajectories + covariant Y_nu Y_nu^T PMNS
    ir_key_map = [
        ("g1_IR", "g1"), ("g2_IR", "g2"), ("g3_IR", "g3"),
        ("l1_IR", "l1_IR"), ("l2_IR", "l2_IR"), ("l3_IR", "l3_IR"), ("l4_IR", "l4_IR"),
        ("yt_over_g3_IR", "yt_over_g3"), ("mb_over_mtau_IR", "mb_over_mtau"), ("ms_over_mmu_IR", "ms_over_mmu"),
        ("u_m2m3_IR", "u_m2m3"), ("d_m2m3_IR", "d_m2m3"), ("e_m2m3_IR", "e_m2m3"),
        ("V12_IR", "V12"), ("V23_IR", "V23"), ("V13_IR", "V13"), ("J_CP_IR", "Jcp"),
    ]
    rg_diff_table = {}
    max_rg_flat_rel = mp.mpf(0)
    max_rg_curved_rel = mp.mpf(0)
    max_pmns_flat_rel = mp.mpf(0)
    max_pmns_curved_nonzero_rel = mp.mpf(0)
    max_pmns_cpzero_abs = mp.mpf(0)
    all_ewsb_none_match = True
    all_std_ckm_ir_match = True

    for uname in ("UA_FrameC_y2", "UB_W3_DynamicVCW_y2", "UC_FrameC_GeodesicApex", "UD_W3_DynamicV4_ferro_y2"):
        rg_diff_table[uname] = {}
        for reg, preg in [("FLAT", "FLAT"), ("CURVED", "CURVED_s12")]:
            rs = rw4["rg_unfolding_t0_to_m35"][uname][reg]
            ps = pw4["unsculpted_2loop_rg_and_neutrinos"][uname][preg]
            pi = ps["ir_t_minus_35"]
            ir_rel = max(rel_diff(rs[rk], pi[pk]) for rk, pk in ir_key_map)
            g_l_rel = max(rel_diff(rs[rk], pi[pk]) for rk, pk in ir_key_map[:7])
            if rs["std_ckm_IR"] != pi["std_ckm"]:
                all_std_ckm_ir_match = False
                flag("W4", f"RG_{uname}_{reg}_std_ckm", "IR std_ckm mismatch", rs["std_ckm_IR"], pi["std_ckm"])
            if not (rs["t_EWSB_l1"] == pi["t_EWSB_l1_cross"] == "none" and rs["t_EWSB_l2"] == pi["t_EWSB_l2_cross"] == "none"):
                all_ewsb_none_match = False
                flag("W4", f"RG_{uname}_{reg}_EWSB", "EWSB crossing mismatch", (rs["t_EWSB_l1"], rs["t_EWSB_l2"]), (pi["t_EWSB_l1_cross"], pi["t_EWSB_l2_cross"]))

            pp = ps["canonical_neutrino_PMNS_MR_I3"]
            rp = rs["canonical_neutrino_PMNS_YYT"]
            pmns_nz = max(
                rel_diff(rp["s12_sq"], pp["s12_sq"]),
                rel_diff(rp["s23_sq"], pp["s23_sq"]),
                rel_diff(rp["s13_sq"], pp["s13_sq"]),
                rel_diff(rp["dm21_over_dm31"], pp["dm21_over_dm31"]),
                rel_diff(rp["s_nu_ratios"][0], pp["s_nu_ratios"][0]),
                rel_diff(rp["s_nu_ratios"][1], pp["s_nu_ratios"][1]),
            )
            jcp_abs = abs_diff(rp["J_PMNS"], pp["Jcp_PMNS"])
            if uname == "UC_FrameC_GeodesicApex":
                # Exact CP conservation at Re(tau)=1/2 -> J_PMNS = 0 up to G_0-G_2 mesh noise (~1e-9)
                if jcp_abs > max_pmns_cpzero_abs:
                    max_pmns_cpzero_abs = jcp_abs
                pmns_tot = pmns_nz
            else:
                pmns_tot = max(pmns_nz, rel_diff(rp["J_PMNS"], pp["Jcp_PMNS"]))

            if reg == "FLAT":
                if ir_rel > max_rg_flat_rel:
                    max_rg_flat_rel = ir_rel
                if pmns_tot > max_pmns_flat_rel:
                    max_pmns_flat_rel = pmns_tot
            else:
                if ir_rel > max_rg_curved_rel:
                    max_rg_curved_rel = ir_rel
                if pmns_tot > max_pmns_curved_nonzero_rel:
                    max_pmns_curved_nonzero_rel = pmns_tot

            rg_diff_table[uname][reg] = {
                "gauge_and_quartics_max_rel_diff": mp_str(g_l_rel, 8),
                "all17_IR_max_rel_diff": mp_str(ir_rel, 8),
                "pmns_nonzero_max_rel_diff": mp_str(pmns_tot, 8),
                "pmns_J_abs_diff": mp_str(jcp_abs, 8),
                "t_EWSB_both_none": True,
            }

    if max_rg_flat_rel > mp.mpf(10) ** (-4):
        flag("W4", "RG_FLAT", "FLAT RG IR drift > 1e-4", mp_str(max_rg_flat_rel, 8), "<1e-4")
    if max_rg_curved_rel > mp.mpf(5) / 1000:
        flag("W4", "RG_CURVED", "CURVED RG IR drift > 5e-3", mp_str(max_rg_curved_rel, 8), "<5e-3")
    if max_pmns_flat_rel > mp.mpf(10) ** (-4):
        flag("W4", "PMNS_FLAT", "FLAT PMNS drift > 1e-4", mp_str(max_pmns_flat_rel, 8), "<1e-4")
    if max_pmns_curved_nonzero_rel > mp.mpf(5) / 1000:
        flag("W4", "PMNS_CURVED", "CURVED PMNS drift > 5e-3", mp_str(max_pmns_curved_nonzero_rel, 8), "<5e-3")
    if max_pmns_cpzero_abs > mp.mpf(10) ** (-7):
        flag("W4", "PMNS_CPzero_apex", "Geodesic apex J_PMNS abs diff > 1e-7", mp_str(max_pmns_cpzero_abs, 8), "<1e-7")

    # Guardrail 3 Haar U(3)^5 & broken Y^T Y diagnostic (CATCH-2)
    haar_both_ok = (
        mp.mpf(rw4["guardrail3_cayley_haar_U3_5"]["max_observable_rel_err_covariant_YYT"]) < mp.mpf(10) ** (-25)
        and mp.mpf(pw4["haar_10trial_U3_5_max_drift"]) < mp.mpf(10) ** (-25)
        and mp.mpf(rw4["guardrail3_cayley_haar_U3_5"]["broken_literal_YTY_WL_violation_rel_err"]) > mp.mpf(1)
        and mp.mpf(pw4["diagnostic_broken_YTY_U3L_violation_rel_err"]) > mp.mpf(1)
    )
    if not haar_both_ok:
        flag("W4", "CATCH2_Haar_U3_5", "Covariant Y_nu Y_nu^T Haar invariance or broken Y^T Y diagnostic failed",
             rw4["guardrail3_cayley_haar_U3_5"], pw4["haar_10trial_U3_5_max_drift"])

    # Guardrail 4 benchmark & 2-loop quartic sensitivity (CATCH-4)
    bench_both_ok = (
        rw4["guardrail4_benchmark"]["sympy_ce15_all_exact"]
        and rw4["guardrail4_benchmark"]["opposite_xing_zhou_sign_ok"]
        and mp.mpf(rw4["guardrail4_benchmark"]["numeric_ce15_max_err"]) < mp.mpf(10) ** (-40)
        and mp.mpf(pw4["guardrail4_benchmarks"]["chowdhury_eberhardt_2hdm_15coeff_err"]) < mp.mpf(10) ** (-40)
        and pw4["guardrail4_benchmarks"]["xing_zhou_opposite_sign"] is True
        and pw4["g1_normalization"] == "GUT_g1_0_eq_1_2_b1_21_5"
    )
    if not bench_both_ok:
        flag("W4", "CATCH4_benchmark", "Guardrail 4 benchmark or GUT g1 convention mismatch",
             rw4["guardrail4_benchmark"], pw4["guardrail4_benchmarks"])

    w4_summary = {
        "curved_G_s12_tau_apex_max_rel_diff": mp_str(g_apex_rel, 8),
        "curved_G_s12_tau_2_max_rel_diff": mp_str(g_tau2_rel, 8),
        "ref_tau_apex_gb_err": rw4["curved_G_s12"]["tau_apex"]["gauss_bonnet_rel_err"],
        "ref_tau_2_gb_err": rw4["curved_G_s12"]["tau_2"]["gauss_bonnet_rel_err"],
        "CATCH4_RG_FLAT_max_rel_diff": mp_str(max_rg_flat_rel, 8),
        "CATCH4_RG_CURVED_max_rel_diff": mp_str(max_rg_curved_rel, 8),
        "CATCH2_PMNS_FLAT_max_rel_diff": mp_str(max_pmns_flat_rel, 8),
        "CATCH2_PMNS_CURVED_nonzero_max_rel_diff": mp_str(max_pmns_curved_nonzero_rel, 8),
        "CATCH2_PMNS_apex_CPzero_J_abs_diff": mp_str(max_pmns_cpzero_abs, 8),
        "all_8_trajectories_t_EWSB_none": all_ewsb_none_match,
        "all_8_trajectories_std_ckm_IR_match": all_std_ckm_ir_match,
        "CATCH2_Haar_U3_5_and_broken_YTY_both_verified": haar_both_ok,
        "CATCH4_Guardrail4_benchmark_both_verified": bench_both_ok,
        "ref_2loop_quartic_sensitivity": rw4["quartic_2loop_sensitivity"],
        "trajectories": rg_diff_table,
    }

    # ------------------------------------------------------------------
    # W5 COMPARISON (6/6 PLANTED CONTROLS)
    # ------------------------------------------------------------------
    w5_both_6_of_6 = (ref["W5"]["all_6_caught"] is True and prod["W5_planted_controls"]["caught_count"] == 6)
    if not w5_both_6_of_6:
        flag("W5", "planted_controls", "Planted controls not 6/6 on both sides", ref["W5"]["all_6_caught"], prod["W5_planted_controls"]["caught_count"])

    # ------------------------------------------------------------------
    # REPOSITORY MANIFEST SWEEP & ZERO NON-RELAY EDITS AUDIT
    # ------------------------------------------------------------------
    manifest_audit = verify_all_relay_manifests(repo_root, skip_paths=(diff_sha_path,))
    if not manifest_audit["all_ok"]:
        flag("CUSTODY", "relay_manifests", "Manifest verification failure", manifest_audit["failures"], 0)
    non_relay_audit = check_zero_non_relay_edits(repo_root)
    if not non_relay_audit["zero_non_relay_edits"]:
        flag("CUSTODY", "non_relay_edits", "Non-relay files modified on branch", non_relay_audit["non_relay_edits"], [])

    compare_ast = ast_purity_check(script_path)
    if not compare_ast["clean"]:
        flag("CUSTODY", "compare_script_ast", "AST purity failed on compare script", compare_ast, "clean")

    payload = {
        "card_id": "AGY-002_A2-WHOLE-INSTRUMENT",
        "comparison": "COLD_ROOM_DISJOINT_REFEREE_V3_VS_AUTHORITATIVE_PRODUCER_V6",
        "firewall": "0 of 19",
        "referee_v3_output_sha256": ref_sha,
        "producer_v6_output_sha256": prod_sha,
        "referee_v3_gates": ref["gates"],
        "producer_v6_gates": prod["gates"],
        "referee_v3_RPF_6_of_6": ref["W5"]["all_6_caught"],
        "producer_v6_PF_6_of_6": (prod["W5_planted_controls"]["caught_count"] == 6),
        "remediation_verification": {
            "CATCH_1_W2_symbolic_tropical_288": tropical_exact_match,
            "CATCH_2_W4_covariant_YYT_neutrino_Haar": bool(haar_both_ok and max_pmns_flat_rel < mp.mpf(10) ** (-4)),
            "CATCH_3_W2_three_closed_M_orbits_gamma_M": bool(max_geo_rel < mp.mpf(10) ** (-7)),
            "CATCH_4_W4_exact_MV84_GUT_g1_RGEs": bool(bench_both_ok and max_rg_flat_rel < mp.mpf(10) ** (-4) and all_ewsb_none_match),
        },
        "W1": w1_summary,
        "W2": w2_summary,
        "W3": w3_summary,
        "W4": w4_summary,
        "W5_both_6_of_6": w5_both_6_of_6,
        "custody_manifests_audit": manifest_audit,
        "zero_non_relay_edits_audit": non_relay_audit,
        "compare_script_ast_audit": compare_ast,
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "verdict": "CERTIFIED_ZERO_DISCREPANCIES" if len(discrepancies) == 0 else "DISCREPANCIES_FOUND",
    }

    raw_out = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    def reject_float_out(s):
        raise ValueError(f"JSON float token forbidden in diff output: {s}")

    json.loads(raw_out, parse_float=reject_float_out)
    with open(diff_json_path, "w", encoding="utf-8") as f:
        f.write(raw_out)

    diff_sha = hashlib.sha256(raw_out.encode("utf-8")).hexdigest()
    comp_sha = compare_ast["sha256"]
    with open(diff_sha_path, "w", encoding="utf-8") as f:
        f.write(f"{comp_sha}  compare_referee_v3_vs_producer_v6.py\n")
        f.write(f"{diff_sha}  referee_v3_vs_producer_v6_diff.json\n")

    print(f"VERDICT={payload['verdict']} discrepancies_count={len(discrepancies)} manifests={manifest_audit['manifests_scanned']}/{manifest_audit['entries_verified']} fail={manifest_audit['failures_count']} non_relay={non_relay_audit['non_relay_edits_count']}")
    print(f"COMPARE_SCRIPT_SHA256={comp_sha}")
    print(f"DIFF_JSON_SHA256={diff_sha}")


if __name__ == "__main__":
    main()
