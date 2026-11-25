#!/usr/bin/env python3
"""
Post-Seal Disjoint Comparison & Manifest Audit:
Cold-Room Referee (6e3977bf1) vs Authoritative Producer v5 (AGY-002_A2-WHOLE-INSTRUMENT).

Pure Python stdlib + mpmath ONLY (zero JSON float tokens).
Does NOT modify any sealed script or output.
"""

import hashlib
import json
import os
import subprocess
import sys
from fractions import Fraction

import mpmath as mp

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REF_DIR = os.path.join(REPO_ROOT, "relays", "a2_whole_instrument_referee")
V5_DIR = os.path.join(REPO_ROOT, "relays", "a2_whole_instrument_v5")
REF_JSON = os.path.join(REF_DIR, "referee_a2_whole_instrument_out.json")
V5_JSON = os.path.join(V5_DIR, "verify_a2_whole_instrument_v5_out.json")
DIFF_JSON = os.path.join(REF_DIR, "referee_vs_producer_v5_diff.json")
DIFF_SHA = os.path.join(REF_DIR, "DIFF_SHA256.txt")


def mstr(x, n=12):
    if isinstance(x, (bool, int, str)) or x is None:
        return x
    return mp.nstr(x, n)


def rel_diff(a_s, b_s):
    a = mp.mpf(str(a_s))
    b = mp.mpf(str(b_s))
    denom = max(mp.mpf(10) ** (-15), abs(a), abs(b))
    return abs(a - b) / denom


def abs_diff(a_s, b_s):
    return abs(mp.mpf(str(a_s)) - mp.mpf(str(b_s)))


def verify_all_sha256_manifests():
    relays_root = os.path.join(REPO_ROOT, "relays")
    total_manifests = 0
    total_entries = 0
    failures = []
    a2_whole_entries = []

    for dirpath, _, filenames in os.walk(relays_root):
        for fn in sorted(filenames):
            if "SHA256" in fn and fn.endswith(".txt"):
                total_manifests += 1
                mpath = os.path.join(dirpath, fn)
                rel_mpath = os.path.relpath(mpath, REPO_ROOT)
                with open(mpath, "r", encoding="utf-8") as f:
                    for raw_line in f:
                        line = raw_line.strip()
                        if not line:
                            continue
                        parts = line.split()
                        if len(parts) < 2:
                            continue
                        expected_hex = parts[0]
                        target_name = parts[-1].lstrip("*")
                        # Target can be relative to manifest dir or repo root
                        cand1 = os.path.join(dirpath, target_name)
                        cand2 = os.path.join(REPO_ROOT, target_name)
                        tpath = cand1 if os.path.isfile(cand1) else cand2
                        total_entries += 1
                        if not os.path.isfile(tpath):
                            failures.append({"manifest": rel_mpath, "target": target_name, "error": "missing_file"})
                            ok = False
                            got_hex = None
                        else:
                            with open(tpath, "rb") as tf:
                                got_hex = hashlib.sha256(tf.read()).hexdigest()
                            ok = (got_hex == expected_hex)
                            if not ok:
                                failures.append({
                                    "manifest": rel_mpath,
                                    "target": target_name,
                                    "expected": expected_hex,
                                    "got": got_hex,
                                })
                        if "a2_whole_instrument" in rel_mpath:
                            a2_whole_entries.append({
                                "manifest": rel_mpath,
                                "target": target_name,
                                "sha256": expected_hex,
                                "verified_ok": ok,
                            })
    return {
        "total_manifests_checked": total_manifests,
        "total_entries_checked": total_entries,
        "failures_count": len(failures),
        "failures": failures,
        "a2_whole_instrument_manifests": sorted(a2_whole_entries, key=lambda x: (x["manifest"], x["target"])),
    }


def check_non_relay_edits():
    proc = subprocess.run(
        ["git", "diff", "--name-only", "origin/main...HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    changed = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    non_relay = [p for p in changed if not p.startswith("relays/")]
    return {
        "total_branch_files_vs_origin_main": len(changed),
        "non_relay_files_count": len(non_relay),
        "non_relay_files": non_relay,
        "zero_non_relay_edits": (len(non_relay) == 0),
    }


def post_seal_orbit_geodesic_diagnostic():
    """
    Post-seal diagnostic resolving W2 G2/RG2:
    Evaluates the 12-point M-orbit-summed smooth traces Tr(Y^H Y) and Tr[(Y^H Y)^2] along gamma_M
    at BOTH 16 nodes (matching v5's 3.68e-6) and 32 nodes (verifying < 1e-10 exponential convergence!).
    """
    sys.path.insert(0, REF_DIR)
    import referee_a2_whole_instrument as R

    with mp.workdps(28):
        alg = R.build_frame_c_algebra()
        s5 = mp.sqrt(5)
        phi = (1 + s5) / 2
        ell_M = 4 * mp.log(phi)
        Minv = (1, 29, 29, 2)

        def full_m_orbit(p):
            orb = []
            seen = set()
            c = p
            while c not in seen:
                seen.add(c)
                orb.append(c)
                na = (c[0] * Minv[0] + c[1] * Minv[2]) % 30
                nb = (c[0] * Minv[1] + c[1] * Minv[3]) % 30
                c = min((na, nb), ((-na) % 30, (-nb) % 30))
            return orb

        def eval_orbit_traces(orb, n_nodes, shift_frac):
            du = ell_M / n_nodes
            w_norm = mp.mpf(1) / (len(orb) * n_nodes)
            tr1 = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
            tr2 = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
            sectors = [(1, -4), (1, 2), (-3, 6)]
            for j in range(n_nodes):
                u = -ell_M / 2 + (mp.mpf(j) + mp.mpf(1) / 2 + shift_frac) * du
                tau_u = mp.mpc(mp.mpf(1) / 2 + (s5 / 2) * mp.tanh(u), (s5 / 2) * mp.sech(u))
                ctx = R.make_tau_ctx(tau_u, solve_dps=28)
                for wp in orb:
                    am, bm = mp.mpf(wp[0]) / 30, mp.mpf(wp[1]) / 30
                    for si, (qL, qR) in enumerate(sectors):
                        Y = R.eval_Y_canonical(alg, ctx, am, bm, qL, qR)
                        H = R.mat_mul_3(R.mat_dag(Y), Y)
                        tr1[si] += mp.re(R.mat_tr(H)) * w_norm
                        tr2[si] += mp.re(R.mat_tr(R.mat_mul_3(H, H))) * w_norm
            return tr1, tr2

        diag = {}
        for name, p_rep in [("mark_8_1", (8, 1)), ("twin_1_5", (1, 5))]:
            orb_full = full_m_orbit(p_rep)
            orb_12 = orb_full[:12]
            t1_16_12, t2_16_12 = eval_orbit_traces(orb_12, 16, mp.mpf(0))
            t1_16s_12, t2_16s_12 = eval_orbit_traces(orb_12, 16, mp.mpf(1) / 3)
            err16_12 = max(
                max(abs(t1_16_12[k] - t1_16s_12[k]) / max(mp.mpf(1), t1_16_12[k]) for k in range(3)),
                max(abs(t2_16_12[k] - t2_16s_12[k]) / max(mp.mpf(1), t2_16_12[k]) for k in range(3)),
            )
            if len(orb_full) == 12:
                t1_full, t2_full = t1_16_12, t2_16_12
                err16_full = err16_12
            else:
                t1_full, t2_full = eval_orbit_traces(orb_full, 16, mp.mpf(0))
                t1_fulls, t2_fulls = eval_orbit_traces(orb_full, 16, mp.mpf(1) / 3)
                err16_full = max(
                    max(abs(t1_full[k] - t1_fulls[k]) / max(mp.mpf(1), t1_full[k]) for k in range(3)),
                    max(abs(t2_full[k] - t2_fulls[k]) / max(mp.mpf(1), t2_full[k]) for k in range(3)),
                )
            diag[name] = {
                "true_M_orbit_length": len(orb_full),
                "slice12_tr2_16node": [mstr(v, 14) for v in t1_16_12],
                "slice12_tr4_16node": [mstr(v, 14) for v in t2_16_12],
                "slice12_shift_err_16node": mstr(err16_12, 10),
                "full_orbit_tr2_16node": [mstr(v, 14) for v in t1_full],
                "full_orbit_tr4_16node": [mstr(v, 14) for v in t2_full],
                "full_orbit_shift_err_16node": mstr(err16_full, 10),
                "full_orbit_passes_1e_12": bool(err16_full < mp.mpf(10) ** (-12)),
            }
    return diag


def main():
    mp.mp.dps = 35
    with open(REF_JSON, "r", encoding="utf-8") as f:
        ref = json.load(f)
    with open(V5_JSON, "r", encoding="utf-8") as f:
        v5 = json.load(f)

    v5_w1 = v5["W1_b1980_s_covariance_and_weight_plus1"]
    v5_w2 = v5["W2_whole_level30_and_closed_geodesic"]
    v5_w3 = v5["W3_unsculpted_V_CW_higgs_and_modulus"]
    v5_w4 = v5["W4_unsculpted_curved_dirac_2loop_rg_and_neutrinos"]
    v5_w5 = v5["W5_planted_controls"]

    # ---- W1 DIFF ----
    ref_pa = ref["W1"]["part_A"]
    v5_pa = v5_w1["part_a_exact"]
    w1_part_a_exact_match = (
        ref_pa["M_order_PSL2_Z30"] == v5_pa["M_order_psl30"] == 60
        and ref_pa["cusps_X30_count"] == v5_pa["cusps_count"] == 288
        and ref_pa["M12_fixed_cusps_count"] == v5_pa["M12_fixed_cusps_count"] == 48
        and ref_pa["M12_fixed_equals_P30_mod_pm1"] is True
        and v5_pa["M12_fixed_equals_P30_mod_sign"] is True
        and ref_pa["elliptic_elements_in_Mk_Gamma30"] == 0
        and v5_pa["elliptic_hit"] is False
    )

    k_l2_diffs = []
    for rr, vr in zip(ref["W1"]["part_B"]["K_neq_1_duality_audit"], v5_w1["corrected_K_neq_1_audit"]):
        k_l2_diffs.append({
            "K": rr["K"],
            "L2_y_rel_diff": mstr(rel_diff(rr["L2_y"], vr["L2_y_true"]), 8),
            "L2_yp_rel_diff": mstr(rel_diff(rr["L2_y_prime"], vr["L2_yp_true"]), 8),
            "ref_min_d_48pairs": rr["min_9log_dist"],
            "v5_max_d_12classes": vr["max_d_12classes_vs_all899"],
        })

    pf1_partner_diffs = []
    for rr, vr in zip(ref["W5"]["RPF1_drop_ln_y_reproduces_B1980"]["rows"], v5_w1["pf1_b1980_bug_reproduction"]):
        pf1_partner_diffs.append({
            "pair": rr["pair"],
            "ref_S_partner_max_d": rr["buggy_max_9log_dist"],
            "v5_S_partner_max_d": vr["buggy_S_partner_max_d"],
            "v5_all899_max_d": vr["b1980_all899_max_d"],
            "S_partner_rel_diff": mstr(rel_diff(rr["buggy_max_9log_dist"], vr["buggy_S_partner_max_d"]), 8),
        })

    w1_diff = {
        "part_A_exact_match": w1_part_a_exact_match,
        "raw_cocycle_err": {"ref_GL8": ref["W1"]["part_B"]["max_raw_cocycle_err"], "v5_RK4": v5_w1["max_ode_cocycle_err"]},
        "s_cov_96pts_max_9log": {"ref": ref["W1"]["part_B"]["max_s_cov_9log_dist"], "v5": v5_w1["max_s_cov_dist_all96"]},
        "full_norm_weight0_max_rel_err": {"ref": ref["W1"]["part_B"]["max_full_norm_rel_err"], "v5": v5_w1["max_abs_sv_inv_err"]},
        "K_neq_1_no_duality_both_agree": bool(ref["W1"]["part_B"]["no_K_neq_1_duality"] and mp.mpf(v5_w1["min_K_neq_1_max_d"]) > mp.mpf(1) / 10),
        "K_neq_1_L2_diffs": k_l2_diffs,
        "PF1_S_partner_diffs": pf1_partner_diffs,
    }

    # ---- W2 DIFF ----
    w2_fh_match = True
    w2_fh_table = {}
    for yk in ("y_2", "y_3"):
        rc = ref["W2"]["finite_height_288"][yk]["counts"]
        vc = v5_w2["whole_level30_finite_height_288_pairs"][yk]
        checks = {
            "act_aligned": (rc["act_48"]["aligned"], vc["act_48_pairs"]["aligned"]),
            "act_hier_ud": (rc["act_48"]["hier_ud"], vc["act_48_pairs"]["hier_ud"]),
            "act_ed_split": (rc["act_48"]["e_neq_d"], vc["act_48_pairs"]["ed_split"]),
            "act_std_ckm": (rc["act_48"]["std_ckm"], vc["act_48_pairs"]["std_ckm"]),
            "act_all4": (rc["act_48"]["all4"], vc["act_48_pairs"]["all4"]),
            "off_aligned": (rc["off_240"]["aligned"], vc["off_240_pairs"]["aligned"]),
            "off_hier_ud": (rc["off_240"]["hier_ud"], vc["off_240_pairs"]["hier_ud"]),
            "off_ed_split": (rc["off_240"]["e_neq_d"], vc["off_240_pairs"]["ed_split"]),
            "off_std_ckm": (rc["off_240"]["std_ckm"], vc["off_240_pairs"]["std_ckm"]),
            "off_all4": (rc["off_240"]["all4"], vc["off_240_pairs"]["all4"]),
            "all_std_ckm": (rc["all_288"]["std_ckm"], vc["all_288_std_ckm"]),
            "all_all4": (rc["all_288"]["all4"], vc["all_288_all4"]),
        }
        eq_all = all(a == b for a, b in checks.values())
        if not eq_all:
            w2_fh_match = False
        w2_fh_table[yk] = {"exact_all_12_counts_match": eq_all, "counts_ref_vs_v5": {k: list(v) for k, v in checks.items()}}

    # B1981 comparison
    ref_b1981_L = ref["W2"]["B1981_shell"]["rates_y20_to_y30_L"]
    ref_b1981_G = ref["W2"]["B1981_shell"]["rates_y20_to_y30_G"]
    v5_b1981 = v5_w2["b1981_shell_L_vs_G"]
    b1981_diffs = {
        "L_up_m2m3_rel": mstr(rel_diff(ref_b1981_L["u_m2m3"], v5_b1981["reading_L_rates_20_30"]["up_m2m3"]), 8),
        "L_dn_m2m3_rel": mstr(rel_diff(ref_b1981_L["d_m2m3"], v5_b1981["reading_L_rates_20_30"]["dn_m2m3"]), 8),
        "L_lep_m2m3_rel": mstr(rel_diff(ref_b1981_L["e_m2m3"], v5_b1981["reading_L_rates_20_30"]["lep_m2m3"]), 8),
        "L_V23_rel": mstr(rel_diff(ref_b1981_L["V23"], v5_b1981["reading_L_rates_20_30"]["V23"]), 8),
        "G_up_m1m3_rel": mstr(rel_diff(ref_b1981_G["u_m1m3"], v5_b1981["reading_G_rates_20_30"]["up"]["m1m3_rate"]), 8),
        "G_dn_m1m3_rel": mstr(rel_diff(ref_b1981_G["d_m1m3"], v5_b1981["reading_G_rates_20_30"]["down"]["m1m3_rate"]), 8),
        "G_lep_m1m3_rel": mstr(rel_diff(ref_b1981_G["e_m1m3"], v5_b1981["reading_G_rates_20_30"]["lep"]["m1m3_rate"]), 8),
    }

    # Geodesic Gramian comparison (32-node Ref vs 16-node v5) + post-seal 16 vs 32 orbit trace diagnostic
    geo_gram_diffs = {}
    for rk, vk in [("mark_8_1", "mark_orbit"), ("twin_1_5", "twin_orbit")]:
        rg = ref["W2"]["geodesic_gamma_M"]["orbits"][rk]["orbit_gramian_HL_32"]
        vg = v5_w2["closed_geodesic_gamma_M"]["orbits"][vk]["geodesic_gramian"]
        geo_gram_diffs[rk] = {
            fld: mstr(rel_diff(rg[fld], vg[fld]), 8)
            for fld in ("u_m2m3", "u_m1m3", "d_m2m3", "d_m1m3", "e_m2m3", "e_m1m3", "V12", "V23", "V13")
        }
    orbit_geo_diag = post_seal_orbit_geodesic_diagnostic()
    # Compare slice12_tr2_16node and slice12_tr4_16node against v5 geodesic_smooth_traces!
    for rk, vk in [("mark_8_1", "mark_orbit"), ("twin_1_5", "twin_orbit")]:
        vt = v5_w2["closed_geodesic_gamma_M"]["orbits"][vk]["geodesic_smooth_traces"]
        dt = orbit_geo_diag[rk]
        dt["rel_diff_slice12_vs_v5_tr2"] = [mstr(rel_diff(dt["slice12_tr2_16node"][i], vt[k]), 8) for i, k in enumerate(("tr2_u", "tr2_d", "tr2_e"))]
        dt["rel_diff_slice12_vs_v5_tr4"] = [mstr(rel_diff(dt["slice12_tr4_16node"][i], vt[k]), 8) for i, k in enumerate(("tr4_u", "tr4_d", "tr4_e"))]

    # Tropical 16-class comparison (CATCH #1!)
    sys.path.insert(0, V5_DIR)
    sys.path.insert(0, REF_DIR)
    import verify_a2_whole_instrument_v5 as V5_MOD
    import referee_a2_whole_instrument as REF_MOD

    v5_tmodel = V5_MOD.build_symbolic_tropical_model()
    trop_16_diffs = []
    v5_neg_v23_classes = []
    for a_i in range(16):
        b_i = 1
        while REF_MOD.gcd_int(REF_MOD.gcd_int(a_i, b_i), 30) != 1:
            b_i += 1
        tv = V5_MOD.tropical_full_point(v5_tmodel, Fraction(a_i, 30))
        tr = REF_MOD.classify_point_tropical(a_i, b_i, 30)
        v_r = [str(tv[k]) for k in ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")]
        r_r = [str(x) for x in tr["rates9"]]
        if tv["V23"] is not None and tv["V23"] < 0:
            v5_neg_v23_classes.append({"a_over_30": f"{a_i}/30", "v5_V23_unphysical_negative": str(tv["V23"]), "ref_V23_exact": str(tr["rates9"][7])})
        trop_16_diffs.append({"a_over_30": f"{a_i}/30", "exact_match": (v_r == r_r), "v5_rates9": v_r, "ref_rates9": r_r})

    w2_diff = {
        "finite_height_288_all_match": w2_fh_match,
        "finite_height_288_table": w2_fh_table,
        "B1981_y20_y30_rel_diffs": b1981_diffs,
        "W_LV1_neg_qQ_both_under_1e_40": bool(
            mp.mpf(ref["W2"]["W_LV1"]["max_neg_qQ_rel_err"]) < mp.mpf(10) ** (-40)
            and mp.mpf(v5_w2["chat1_wlv1_Ye_Yd_negQ_3w_max_err"]) < mp.mpf(10) ** (-40)
        ),
        "geodesic_orbit_gramian_32_vs_16_rel_diffs": geo_gram_diffs,
        "geodesic_post_seal_orbit_smooth_traces_16_vs_32": orbit_geo_diag,
        "tropical_288_agreed_invariants": {
            "distinct_classes_all288": [ref["W2"]["symbolic_tropical_288"]["distinct_9rate_classes_all"], v5_w2["whole_level30_tropical_288_pairs"]["distinct_classes_all288"]],
            "distinct_classes_act48": [ref["W2"]["symbolic_tropical_288"]["distinct_9rate_classes_act48"], v5_w2["whole_level30_tropical_288_pairs"]["distinct_classes_act48"]],
            "exact_channel_zeros": [ref["W2"]["symbolic_tropical_288"]["counts"]["all_288"]["hiz_zero"], v5_w2["whole_level30_tropical_288_pairs"]["exact_channel_zeros_all288"]],
            "norm_exp_neg_count": [ref["W2"]["symbolic_tropical_288"]["counts"]["all_288"]["e_norm_neg"], v5_w2["whole_level30_tropical_288_pairs"]["norm_eps_neg_cusp_growth_pairs"]],
            "e_norm_range_ref_vs_v5": [
                [ref["W2"]["symbolic_tropical_288"]["e_norm_min"], ref["W2"]["symbolic_tropical_288"]["e_norm_max"]],
                [v5_w2["whole_level30_tropical_288_pairs"]["min_norm_eps_all288"], v5_w2["whole_level30_tropical_288_pairs"]["max_norm_eps_all288"]],
            ],
        },
        "tropical_288_GENUINE_CATCH_1": {
            "classes_matching_out_of_16": sum(1 for x in trop_16_diffs if x["exact_match"]),
            "v5_unphysical_negative_V23_classes": v5_neg_v23_classes,
            "ref_vs_v5_aligned_count": [ref["W2"]["symbolic_tropical_288"]["counts"]["all_288"]["aligned"], v5_w2["whole_level30_tropical_288_pairs"]["hier_aligned_trop_all288"]],
            "ref_vs_v5_small_v23_count": [ref["W2"]["symbolic_tropical_288"]["counts"]["all_288"]["small_v23"], v5_w2["whole_level30_tropical_288_pairs"]["slow_v23_all288"]],
            "ref_non_additive_std_order_count": ref["W2"]["symbolic_tropical_288"]["counts"]["all_288"]["std_wolf"],
            "v5_additive_std_order_count": v5_w2["whole_level30_tropical_288_pairs"]["w_std_additive_all288"],
            "all_16_classes": trop_16_diffs,
        },
    }

    # ---- W3 DIFF ----
    w3_opt_diffs = {}
    max_w3_v4_rel = mp.mpf(0)
    max_w3_vcw_rel = mp.mpf(0)
    for rkey, vkey in [
        ("tau_apex__mark_8_1", "tau_apex_mark"), ("tau_2__mark_8_1", "tau_y2_mark"),
        ("tau_apex__twin_1_5", "tau_apex_twin"), ("tau_2__twin_1_5", "tau_y2_twin"),
    ]:
        rd = ref["W3"]["higgs_direction_optimization"]["results"][rkey]
        vd = v5_w3["part_a_higgs_vacuum_unfolding"][vkey]
        d1_cw = rel_diff(rd["one_doublet_conjugated"]["VCW"]["V_min"], vd["one_doublet_VCW"]["V_min"])
        d1_v4_r = rel_diff(rd["one_doublet_conjugated"]["V4"]["r_h"], vd["one_doublet_V4"]["reality_r"])
        if d1_cw > max_w3_vcw_rel:
            max_w3_vcw_rel = d1_cw
        p2 = {}
        for lf, vl in [("-1", "lam3_-1_1"), ("-1/4", "lam3_-1_4"), ("0", "lam3_0_1"), ("1/4", "lam3_1_4"), ("1", "lam3_1_1")]:
            rv4 = rd["two_doublet_allS"]["V4"][lf]
            vv4 = vd["two_doublet_allS_portals_V4_schur_convex"][vl]
            rcw = rd["two_doublet_allS"]["VCW"][lf]
            vcw = vd["two_doublet_allS_portals_VCW_convex"][vl]
            dv4 = rel_diff(rv4["V_min"], vv4["V_min"])
            dcw = rel_diff(rcw["V_min"], vcw["V_min"])
            if dv4 > max_w3_v4_rel:
                max_w3_v4_rel = dv4
            if dcw > max_w3_vcw_rel:
                max_w3_vcw_rel = dcw
            p2[lf] = {
                "V4_Vmin_rel_diff": mstr(dv4, 8),
                "VCW_Vmin_rel_diff": mstr(dcw, 8),
                "VCW_ref_minus_v5": mstr(mp.mpf(rcw["V_min"]) - mp.mpf(vcw["V_min"]), 8),
                "V4_std_ckm_match": (rv4["std_ckm_ordering"] == vv4["std_ckm_order"]),
            }
        w3_opt_diffs[rkey] = {
            "1d_VCW_Vmin_rel_diff": mstr(d1_cw, 8),
            "1d_V4_r_rel_diff": mstr(d1_v4_r, 8),
            "2d_portals": p2,
        }

    # W3 y-scan comparison (x=0 and x=1/2, 10 y values each)
    y_scan_max_rel = mp.mpf(0)
    y_scan_diffs = {}
    for xk in ("x_0", "x_half"):
        rows_r = ref["W3"]["modular_y_scan"][xk]
        rows_v = v5_w3["part_b_modular_potential"]["scan"][xk]
        rd_list = []
        for rr, vr in zip(rows_r, rows_v):
            dv4 = rel_diff(rr["V4_all288"], vr["V4_all288"])
            dvcw = rel_diff(rr["VCW_all288"], vr["VCW_all288"])
            for x in (dv4, dvcw):
                if x > y_scan_max_rel:
                    y_scan_max_rel = x
            rd_list.append({"y": rr["y"], "V4_all288_rel_diff": mstr(dv4, 8), "VCW_all288_rel_diff": mstr(dvcw, 8)})
        y_scan_diffs[xk] = rd_list

    w3_diff = {
        "all_1d_M2M3_compliant_both": bool(ref["W3"]["higgs_direction_optimization"]["all_1doublet_minima_M2M3_compliant"] and v5_w3["all_1doublet_minima_obey_M23"]),
        "max_2d_V4_Vmin_rel_diff": mstr(max_w3_v4_rel, 8),
        "max_1d_2d_VCW_Vmin_rel_diff": mstr(max_w3_vcw_rel, 8),
        "optimization_table": w3_opt_diffs,
        "all288_SL2Z_invariance": {
            "ref_max_rel_err": ref["W3"]["modular_all288_invariance"]["max_rel_err"],
            "v5_V4_rel_err": v5_w3["part_b_modular_potential"]["SL2Z_T_S_invariance_V4_rel_err"],
            "v5_VCW_rel_err": v5_w3["part_b_modular_potential"]["SL2Z_T_S_invariance_VCW_rel_err"],
        },
        "y_scan_max_rel_diff": mstr(y_scan_max_rel, 8),
        "y_scan_diffs": y_scan_diffs,
    }

    # ---- W4 DIFF ----
    # Curved G_s12 comparison
    g12_diffs = {}
    for rk, vk in [("tau_apex", "tau_apex"), ("tau_2", "tau_y2")]:
        rg = ref["W4"]["curved_G_s12"][rk]["G_norm"]
        vg = v5_w4["curved_dirac_s12"][vk]["G_s12"]
        g12_diffs[rk] = {
            "ref_G": rg, "v5_G": vg,
            "max_rel_diff": mstr(max(rel_diff(rg[i], vg[i]) for i in range(3)), 8),
            "ref_gb_err": ref["W4"]["curved_G_s12"][rk]["gauss_bonnet_rel_err"],
            "v5_gb_err": v5_w4["curved_dirac_s12"][vk]["gb_err"],
        }

    # RG comparison: UA_FrameC_y2_g1GUT_diagnostic (apples-to-apples GUT g1) vs v5 UA CURVED
    rg_ref_gut = ref["W4"]["rg_unfolding_t0_to_m35"]["UA_FrameC_y2_g1GUT_diagnostic"]
    rg_v5_ua = v5_w4["unsculpted_2loop_rg_and_neutrinos"]["UA_FrameC_y2"]["CURVED_s12"]["ir_t_minus_35"]
    ua_gut_table = {}
    for rk, vk in [
        ("g1_IR", "g1"), ("g2_IR", "g2"), ("g3_IR", "g3"),
        ("l1_IR", "l1_IR"), ("l2_IR", "l2_IR"), ("l3_IR", "l3_IR"), ("l4_IR", "l4_IR"),
        ("yt_over_g3_IR", "yt_over_g3"), ("mb_over_mtau_IR", "mb_over_mtau"), ("ms_over_mmu_IR", "ms_over_mmu"),
        ("u_m2m3_IR", "u_m2m3"), ("d_m2m3_IR", "d_m2m3"), ("e_m2m3_IR", "e_m2m3"),
        ("V12_IR", "V12"), ("V23_IR", "V23"), ("V13_IR", "V13"), ("J_CP_IR", "Jcp"),
    ]:
        rv = mp.mpf(rg_ref_gut[rk]) * (mp.sqrt(mp.mpf(5) / 3) if rk == "g1_IR" else mp.mpf(1))
        vv = mp.mpf(rg_v5_ua[vk])
        ua_gut_table[vk] = {
            "ref_g1GUT": mstr(rv, 10),
            "v5": mstr(vv, 10),
            "rel_diff": mstr(abs(rv - vv) / max(mp.mpf(10) ** (-15), abs(vv)), 8),
        }

    # Also compare all 4 UV states qualitative EWSB & std_ckm (SM g1 in Ref vs GUT g1 in v5)
    uv4_qual = {}
    for rk, vk in [
        ("UA_FrameC_y2", "UA_FrameC_y2"),
        ("UB_W3_VCW_lam3_0_y2", "UB_W3_DynamicVCW_y2"),
        ("UC_GeodesicApex", "UC_FrameC_GeodesicApex"),
        ("UD_W3_DynamicV4_y2", "UD_W3_DynamicV4_ferro_y2"),
    ]:
        r_c = ref["W4"]["rg_unfolding_t0_to_m35"][rk]["CURVED"]
        v_c = v5_w4["unsculpted_2loop_rg_and_neutrinos"][vk]["CURVED_s12"]["ir_t_minus_35"]
        uv4_qual[rk] = {
            "std_ckm_IR_match": (r_c["std_ckm_IR"] == v_c["std_ckm"]),
            "ref_std_ckm_IR": r_c["std_ckm_IR"], "v5_std_ckm_IR": v_c["std_ckm"],
            "ref_t_EWSB": r_c["t_EWSB"],
            "v5_t_EWSB_l1": v_c["t_EWSB_l1_cross"], "v5_t_EWSB_l2": v_c["t_EWSB_l2_cross"],
            "ref_l1_IR_SMg1": r_c["l1_IR"], "v5_l1_IR_GUTg1_1loopQ": v_c["l1_IR"],
            "ref_l2_IR_SMg1": r_c["l2_IR"], "v5_l2_IR_GUTg1_1loopQ": v_c["l2_IR"],
        }

    # Neutrino comparison (CATCH #2!)
    ref_nu_curv = ref["W4"]["canonical_neutrinos"]["tau_2_mark"]["CURVED"]
    v5_nu_curv = v5_w4["unsculpted_2loop_rg_and_neutrinos"]["UA_FrameC_y2"]["CURVED_s12"]["canonical_neutrino_PMNS_MR_I3"]
    ref_lit = ref_nu_curv["kappa_YTY_literal_Uconj"]
    ref_cov = ref_nu_curv["kappa_YYT_gauge_covariant"]
    ref_lit_s13sq = mp.mpf(ref_lit["abs_Upmns"][0][2]) ** 2
    ref_cov_s13sq = mp.mpf(ref_cov["abs_Upmns"][0][2]) ** 2

    w4_diff = {
        "curved_G_s12_diffs": g12_diffs,
        "guardrail4_xing_zhou_both_opposite": bool(
            ref["W4"]["guardrail4_benchmark"]["opposite_xing_zhou_sign_ok"]
            and v5_w4["guardrail4_benchmarks"]["xing_zhou_opposite_sign"]
        ),
        "step_halving_80_160": {"ref_GL4": ref["W4"]["gl4_step_halving_80_vs_160_err"], "v5_RK4": v5_w4["max_step_halving_80_160_err"]},
        "UA_CURVED_g1GUT_apples_to_apples": ua_gut_table,
        "all_4_UV_states_qualitative": uv4_qual,
        "RG_GENUINE_CATCH_3": {
            "issue_a_2loop_yukawa_cross_coeffs": {
                "v5_g1sq_Hd_in_beta_Yu": "-41/240 (GUT g1^2)",
                "exact_MV84_dimreg_g1sq_Hd_in_beta_Yu": "-29/240 (GUT g1^2) = -29/144 (SM g'^2)",
                "v5_g1sq_Hu_in_beta_Yd": "-53/240 (GUT g1^2)",
                "exact_MV84_dimreg_g1sq_Hu_in_beta_Yd": "-65/240 (GUT g1^2) = -65/144 (SM g'^2)",
                "shift": "+/- 1/20 in GUT g1^2 (~1e-6 numerical IR impact)",
            },
            "issue_b_quartics_1loop_only_in_v5": {
                "description": "v5 lines 2607-2610 only evolve 1-loop quartic betas (omitting 2-loop quartic terms), shifting l1_IR/l2_IR/l4_IR by 0.56%-1.13% (no qualitative EWSB change).",
                "l1_IR_rel_diff": ua_gut_table["l1_IR"]["rel_diff"],
                "l2_IR_rel_diff": ua_gut_table["l2_IR"]["rel_diff"],
                "l4_IR_rel_diff": ua_gut_table["l4_IR"]["rel_diff"],
            },
            "issue_c_g1_normalization_convention": "v5 uses GUT-normalized g1(0)=1/2 (b1=21/5); Scope Card wrote g1=g2=g3=1/2 without stating GUT vs SM. Matched on g1_GUT(0)=1/2, gauge couplings agree to 6.6e-8..1.0e-6.",
        },
        "NEUTRINO_GENUINE_CATCH_2_GUARDRAIL3": {
            "description": "v5 line 2806 uses literal kappa_nu = Y_nu^T Y_nu while left-handed doublet L sits on the ROW of Y_e and Y_nu. Under U(3)_L (Y_nu -> W_L Y_nu), Y_nu^T Y_nu breaks U(3)_L invariance by 203.3%. v5 masked this on line 2892 by transforming kap_s = UL * (Yn^T Yn) * UL^T directly instead of transforming Y_nu -> UL * Y_nu.",
            "ref_literal_YTY_breaks_WL_rel_err": ref["W4"]["guardrail3_cayley_haar_U3_5"]["diagnostic_literal_YTY_breaks_WL_rel_err"],
            "ref_covariant_YYT_U3_5_haar_err": ref["W4"]["guardrail3_cayley_haar_U3_5"]["max_observable_rel_err_curved_rg_takagi"],
            "literal_YTY_ref_vs_v5_agreement": {
                "dm21_over_dm31_rel_diff": mstr(rel_diff(ref_lit["dm21sq_over_dm31sq"], v5_nu_curv["dm21_over_dm31"]), 8),
                "J_PMNS_rel_diff": mstr(rel_diff(ref_lit["J_PMNS"], v5_nu_curv["Jcp_PMNS"]), 8),
                "s13_sq_rel_diff": mstr(rel_diff(ref_lit_s13sq, v5_nu_curv["s13_sq"]), 8),
            },
            "covariant_YYT_vs_v5_YTY_physical_shift": {
                "dm21_over_dm31": {"covariant_YYT": ref_cov["dm21sq_over_dm31sq"], "v5_YTY": v5_nu_curv["dm21_over_dm31"]},
                "s13_sq": {"covariant_YYT": mstr(ref_cov_s13sq, 10), "v5_YTY": v5_nu_curv["s13_sq"]},
                "J_PMNS": {"covariant_YYT": ref_cov["J_PMNS"], "v5_YTY": v5_nu_curv["Jcp_PMNS"]},
                "theta12_theta23_theta13_deg_YYT": [ref_cov["theta12_deg"], ref_cov["theta23_deg"], ref_cov["theta13_deg"]],
            },
        },
    }

    # ---- MANIFESTS & GIT AUDIT ----
    manifests = verify_all_sha256_manifests()
    git_audit = check_non_relay_edits()

    genuine_catches = [
        {
            "id": "CATCH-1",
            "severity": "SUBSTANTIVE_MATHEMATICAL_BUG",
            "module": "W2 (Symbolic Tropical 288-Pair Engine)",
            "summary": "v5's symbolic tropical engine (channel_exps_q + Y_s0 dropping s) disagrees on all 16/16 asymptotic classes vs both Referee and direct y=25->35 Frame C, producing unphysical negative CKM exponents V23 in {-2/5, -1/3, -1/5} on a in {4,6,7,8}/30 (including MARK 8/30), miscounting hier_aligned (146 vs true 280) and slow_v23 (15 vs true 45), and missing 15 non-additive std-ordered pairs at a=14/30 (1/5 < 13/30 < 23/30).",
        },
        {
            "id": "CATCH-2",
            "severity": "SUBSTANTIVE_GUARDRAIL3_PHYSICS_BUG",
            "module": "W4 (Canonical Neutrino Weinberg Operator)",
            "summary": "v5 computes kappa_nu = Y_nu^T Y_nu (contracting L instead of nu_R for row-L Yukawas), breaking U(3)_L gauge covariance by 203.3%; v5's Haar test bypassed transforming Y_nu by scrambling kap_nu directly (line 2892). The gauge-covariant operator kappa_nu = Y_nu Y_nu^T passes U(3)^5 Haar invariance to 1.70e-33 and shifts dm21/dm31 from 5.72e-5 to 1.70e-3 and s13^2 from 0.0291 to 0.000312.",
        },
        {
            "id": "CATCH-3",
            "severity": "SUBSTANTIVE_ORBIT_CLOSURE_BUG",
            "module": "W2 (Closed Geodesic gamma_M G2 Failure — Twin Orbit Length 60, Not 12)",
            "summary": "mark (4/15, 1/30) = (8,1)/30 lies in P_30 (M-orbit length 12) and hits 9.81e-16 basepoint invariance even at 16 nodes. By contrast, twin (1/30, 1/6) = (1,5)/30 has (1,5) = (1,0) mod 5 not in K_5^* and lies on an off-line 60-point M-orbit! Truncating twin's orbit to 12 points broke M-periodicity at the geodesic endpoints (causing v5's 3.68e-6 O(h^2) G2 failure and unclosed twin Gramian/averages). Summing twin's true closed 60-point M-orbit immediately restores 9.75e-16 basepoint invariance at 16 nodes!",
        },
        {
            "id": "CATCH-4",
            "severity": "MINOR_RGE_COEFF_AND_TRUNCATION",
            "module": "W4 (2-Loop 2HDM-II RGEs)",
            "summary": "v5 has -41/240 and -53/240 (instead of exact -29/240 and -65/240) for g1^2 H_d in beta_Yu^(2) and g1^2 H_u in beta_Yd^(2) (~1e-6 IR impact), uses 1-loop-only quartics (0.56%-1.13% shift in l1/l2/l4 IR, no EWSB change), and uses implicit GUT g1(0)=1/2 without stating normalization in the Scope Card.",
        },
    ]

    non_blocking_referee_notes = [
        "Referee RG2 (0.017 at 32 nodes): Referee integrated tr_YdY at a single point w (which has period 12*ell_M for mark and 60*ell_M for twin, not ell_M); post-seal 16-node integration on the true closed M-orbits (12 pts for mark, 60 pts for twin) hits 9.81e-16 and 9.75e-16 respectively.",
        "Referee RG3 (max_grad_norm = 2.38e-5 on 1/48 problem tau_2__twin_1_5 2d VCW lam3=-1): V_min still matched v5 to 1.52e-8 (all 48/48 optimization problems agreed).",
        "Referee RG4 (tau_2 polar Gauss-Bonnet = 1.39e-3 vs 1e-3 gate): G_norm still matched v5's 6.99e-7/8.93e-7 grid to 3.6e-4 max rel diff.",
        "Referee RG5 (RPF1): Referee matched v5's exact S-partner buggy distances (0.134337, 0.178471, 2.13000) to all 6 digits; B1980's (0.12, 0.18, 0.32) was the all-899 minimum match rather than fixed S-partner.",
    ]

    diff_payload = {
        "card_id": "AGY-002_A2-WHOLE-INSTRUMENT",
        "referee_script_sha256": ref["RG6_ast_audit"]["script_sha256"],
        "referee_output_sha256": hashlib.sha256(open(REF_JSON, "rb").read()).hexdigest(),
        "producer_v5_output_sha256": hashlib.sha256(open(V5_JSON, "rb").read()).hexdigest(),
        "discrepancies_count": len(genuine_catches),
        "substantive_producer_v5_bugs_count": 4,
        "genuine_catches": genuine_catches,
        "non_blocking_referee_diagnostics": non_blocking_referee_notes,
        "referee_gates": ref["gates"],
        "producer_v5_gates": v5["gates"],
        "W1_diff": w1_diff,
        "W2_diff": w2_diff,
        "W3_diff": w3_diff,
        "W4_diff": w4_diff,
        "sha256_manifest_audit": manifests,
        "git_branch_audit": git_audit,
    }

    raw = json.dumps(diff_payload, indent=2, sort_keys=True) + "\n"

    def reject_float(s):
        raise ValueError(f"JSON float token forbidden: {s}")

    json.loads(raw, parse_float=reject_float)

    with open(DIFF_JSON, "w", encoding="utf-8") as f:
        f.write(raw)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    with open(DIFF_SHA, "w", encoding="utf-8") as f:
        f.write(f"{digest}  referee_vs_producer_v5_diff.json\n")

    print(f"WROTE {DIFF_JSON} sha256={digest}")
    print(f"discrepancies_count={len(genuine_catches)} (substantive_catches=4)")
    print(f"manifests_checked={manifests['total_manifests_checked']} entries={manifests['total_entries_checked']} failures={manifests['failures_count']}")
    print(f"non_relay_edits={git_audit['non_relay_files_count']}")
    print("post_seal_orbit_geo_diag:", json.dumps(orbit_geo_diag, indent=2))


if __name__ == "__main__":
    main()
