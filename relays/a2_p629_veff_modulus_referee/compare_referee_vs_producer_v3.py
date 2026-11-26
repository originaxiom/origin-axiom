#!/usr/bin/env python3
"""
Post-seal automated cross-diff audit comparing sealed Cold-Room Referee output
(referee_a2_p629_veff_modulus_out.json) against Producer v3 output
(verify_a2_p629_veff_modulus_v3_out.json).

Strictly 0 of 19; pure Python stdlib + mpmath; 0 JSON floats in diff output.
"""

import json
from pathlib import Path
import mpmath as mp


def fmt_r(val, digits=12):
    return mp.nstr(mp.mpf(val), digits)


def assert_zero_json_floats(obj, path="$"):
    if isinstance(obj, (bool, type(None), int, str)):
        return
    if isinstance(obj, list):
        for i, v in enumerate(obj):
            assert_zero_json_floats(v, f"{path}[{i}]")
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_zero_json_floats(v, f"{path}.{k}")
        return
    raise AssertionError(f"Forbidden JSON type at {path}: {type(obj).__name__}")


def main():
    mp.mp.dps = 30
    here = Path(__file__).resolve().parent
    repo = here.parent.parent
    ref = json.loads((here / "referee_a2_p629_veff_modulus_out.json").read_text(encoding="utf-8"))
    v3 = json.loads(
        (repo / "relays/a2_p629_veff_modulus_v3/verify_a2_p629_veff_modulus_v3_out.json").read_text(
            encoding="utf-8"
        )
    )

    items = []

    def cmp(category, name, r_val, p_val, tol_str, root_cause="none"):
        if r_val is None and p_val is None:
            items.append({
                "category": category, "name": name, "ref": "None", "v3": "None",
                "rel_diff": "0", "tol": tol_str, "match": True, "root_cause": "none",
            })
            return
        if isinstance(r_val, bool) or isinstance(p_val, bool):
            ok = bool(r_val) == bool(p_val)
            items.append({
                "category": category, "name": name, "ref": str(r_val), "v3": str(p_val),
                "rel_diff": "0" if ok else "BOOL_MISMATCH", "tol": "exact",
                "match": ok, "root_cause": "none" if ok else root_cause,
            })
            return
        rv = mp.mpf(str(r_val))
        pv = mp.mpf(str(p_val))
        tol = mp.mpf(tol_str)
        if abs(pv) > mp.mpf("1e-10"):
            rel = abs(rv - pv) / abs(pv)
        else:
            rel = abs(rv - pv)
        ok = bool(rel <= tol)
        items.append({
            "category": category, "name": name, "ref": fmt_r(rv, 14), "v3": fmt_r(pv, 14),
            "rel_diff": fmt_r(rel, 5), "tol": tol_str, "match": ok,
            "root_cause": "none" if ok else root_cause,
        })

    # P1 — Bosonic & FILQ(1990)
    p1r = ref["RP1"]
    p1v = v3["P1_bosonic_and_FILQ_benchmarks"]
    for n in (1, 2, 3):
        rn = p1r["FILQ_1990"][f"n={n}"]
        vn = p1v["FILQ_SUGRA_potentials"][f"n_{n}"]
        for k in ("y_star", "V_star", "V_i", "V_omega", "V_2i", "V_4i"):
            cmp("P1", f"FILQ_n{n}.{k}", rn[k], vn[k], "1e-7")
    cmp("P1", "half_period_exact", p1r["half_period_spin_sum_s3"]["exact_fraction"] == "-15/16", p1v["half_period_exact_ratio"] == "-15/16", "0")
    cmp("P1", "PF3_dV", ref["RP4"]["planted_controls"]["RPF3_off_minimum_shift"]["dV"], p1v["pf3_shift_off_FILQ1_dV"], "1e-6")
    cmp("P1", "PF3_grad", ref["RP4"]["planted_controls"]["RPF3_off_minimum_shift"]["grad_norm"], p1v["pf3_shift_off_FILQ1_grad"], "1e-6")

    # P2 — All-288 Boson + Fermion Phase Diagram
    p2r = ref["RP2"]
    p2v = v3["P2_boson_fermion_SL2Z_phase_diagram"]
    for r_orb, v_orb in [("omega", "omega_plus"), ("arc_5pi12", "arc_exp_i_5pi_12"), ("i", "i")]:
        for rk, vk in [("Tr2", "Tr2"), ("V4", "V4"), ("VCW1", "VCW_1"), ("VCW_tr", "VCW_tr")]:
            cmp("P2", f"{r_orb}.{rk}", p2r["orbifolds_and_cusp"][r_orb][rk], p2v["orbifolds_and_arc"][v_orb][vk], "1e-7")
    cmp("P2", "P2B.cB_crit", p2r["P2_B_casimir_nogo"]["cB_crit"], p2v["theorem_P2B_polynomial_casimir_nogo_and_transition"]["cB_crit_E3"], "1e-7")
    cmp("P2", "P2B.VCW1_plus_100E3_at_4i", p2r["P2_B_casimir_nogo"]["VCW1_plus_100E3_at_4i"], p2v["theorem_P2B_polynomial_casimir_nogo_and_transition"]["VCW1_plus_100E3_at_4i"], "1e-7")

    p2cr = p2r["P2_C_coupled_vacuum"]
    p2cv = p2v["theorem_P2C_globally_bounded_coupled_vacuum"]
    cmp("P2C", "y_star", p2cr["y_star"], p2cv["cF_70_y_star"], "1e-7")
    cmp("P2C", "V_star", p2cr["V_star"], p2cv["cF_70_V_star"], "1e-7")
    cmp("P2C", "V_at_0_ystar", p2cr["V_at_0_ystar"], p2cv["cF_70_V_at_zero_same_y"], "1e-7")
    cmp("P2C", "V_xx_half", p2cr["V_xx_half"], p2cv["cF_70_Vxx_at_half"], "2e-3")
    cmp("P2C", "V_xx_zero", p2cr["V_xx_zero"], p2cv["cF_70_Vxx_at_zero_saddle"], "2e-3")
    cmp("P2C", "V_yy_half", p2cr["V_yy_half"], p2cv["cF_70_Vyy_at_half"], "1e-6")
    cmp("P2C", "V_tot_FILQ3_star_70", p2cr["V_tot_at_FILQ3_star_70"], p2cv["cF_70_small_y_FILQ3_well_V"], "1e-7")
    cmp("P2C", "V_tot_half_4i_70", p2cr["V_tot_half_4i_70"], p2cv["cF_70_cusp_wall_at_half_plus_4i"], "1e-7")
    cmp("P2C", "V_tot_half_4i_100", p2cr["V_tot_half_4i_100"], p2cv["cF_100_V_at_half_plus_4i"], "1e-7")
    cmp("P2C", "V_tot_half_5i_100", p2cr["V_tot_half_5i_100"], p2cv["cF_100_V_at_half_plus_5i"], "1e-7")

    # P3 — Curved Dirac G_{s=1/2}, UV/IR Piece 2, Piece 3 PMNS across all 3 vacua & 3 branches
    vmap = [("omega", "V1_omega_plus"), ("FILQ1_star", "V2_FILQ1_star"), ("tot_star_70", "V3_coupled_cF70_star")]
    p3r = ref["RP3"]
    p3v = v3["P3_unsculpted_forward_unfolding_pieces2_and_3"]

    for rvk, vvk in vmap:
        Gr = p3r["curved_dirac_G_s12"][rvk]["G_am_423"]
        Gv = p3v["vacua_unfolding"][vvk]["curved_dirac_s12"]["G_s12"]
        for j in range(3):
            cmp("P3_G", f"{rvk}.G_s12[{j}]", Gr[j], Gv[j], "1e-4")

        for bname in ("Static_FLAT", "Static_CURVED_s12", "DynamicV4_ferro_CURVED_s12"):
            br = p3r["vacua_unfolding"][rvk][bname]
            bv = p3v["vacua_unfolding"][vvk]["branches"][bname]
            rc_dyn = "DynamicV4_flat_vs_curved_V4_order" if bname == "DynamicV4_ferro_CURVED_s12" else "unexpected"
            for rk, vk in [("u23", "u_m2m3"), ("d23", "d_m2m3"), ("e23", "e_m2m3"), ("V12", "V12"), ("V23", "V23"), ("V13", "V13"), ("std_ckm", "std_ckm")]:
                cmp("P3_UV", f"{rvk}.{bname}.{rk}", br["UV"][rk], bv["uv"][vk], "5e-3", root_cause=rc_dyn)

            ir = br["IR_n160"]
            iv = bv["piece2_ir_t_minus_35"]
            for rk, vk in [
                ("g1", "g1"), ("g2", "g2"), ("g3", "g3"), ("yt_over_g3", "yt_over_g3"), ("mb_over_mtau", "mb_over_mtau"),
                ("u23", "u_m2m3"), ("d23", "d_m2m3"), ("e23", "e_m2m3"),
                ("V12", "V12"), ("V23", "V23"), ("V13", "V13"),
                ("l1", "l1_IR"), ("l2", "l2_IR"), ("l3", "l3_IR"), ("l4", "l4_IR"),
                ("mHu2_IR", "mHu2_IR"), ("mHd2_IR", "mHd2_IR"), ("min_sf", "min_sfermion_m2_IR"),
                ("t_EWSB_u", "t_EWSB_u"), ("t_EWSB_d", "t_EWSB_d"),
                ("std_ckm", "std_ckm"), ("stab_all", "D_term_vacuum_stable"), ("ewsb_u_first", "Hu_crosses_first"),
            ]:
                rc = "Bug1_v3_Dterm_l1_l2_factor2" if rk in ("l1", "l2") else rc_dyn
                cmp("P3_IR", f"{rvk}.{bname}.{rk}", ir[rk], iv[vk], "5e-3", root_cause=rc)

            rc_pmns = "DynamicV4_static_vs_hu_Ynu" if bname == "DynamicV4_ferro_CURVED_s12" else "unexpected"
            for mrk, mvk in [("I3", "MR_I3"), ("sym_1w", "MR_sym_Ynu_1w"), ("sym_2w", "MR_sym_Ynu_2w")]:
                pr = br["Piece3_PMNS_IR"][mrk]
                pv = bv["piece3_majorana_PMNS"][mvk]
                for pk in ("s12_sq", "s23_sq", "s13_sq", "dm21_over_dm31"):
                    cmp("P3_PMNS", f"{rvk}.{bname}.{mrk}.{pk}", pr[pk], pv[pk], "5e-3", root_cause=rc_pmns)

    # P4 — Planted Negative Controls
    cmp("P4", "PF2_subcrit_4i", ref["RP4"]["planted_controls"]["RPF2_subcritical_FILQ1_cusp"]["V_at_half_4i"], p2v["pf2_subcritical_n1_plus_70VCW1_at_4i"], "1e-7")
    p4_map = [
        ("RPF1_drop_nonholo_E2", "PF1_drop_nonhol_E2_breaks_S_inv"),
        ("RPF2_subcritical_FILQ1_cusp", "PF2_subcritical_n1_restores_cusp_runaway"),
        ("RPF3_off_minimum_shift", "PF3_shift_off_FILQ1_raises_V_and_grad"),
        ("RPF4_degenerate_MR_YnuTYnu", "PF4_degenerate_MR_collapses_splitting"),
        ("RPF5_broken_contraction_Haar", "PF5_broken_YTM_fails_Haar_U3L"),
        ("RPF6_zero_yukawas_no_ewsb", "PF6_zero_yukawas_kill_radiative_EWSB"),
    ]
    for rk, vk in p4_map:
        cmp("P4", rk, ref["RP4"]["planted_controls"][rk]["triggered"], v3["P4_planted_controls"][vk], "0")

    # Code-level / Guardrail 4 checks recorded explicitly
    code_audit_findings = [
        {
            "id": "BUG-1",
            "severity": "CRITICAL",
            "location": "verify_a2_p629_veff_modulus_v3.py lines 1306-1309, 1851-1854, 1941-1942",
            "summary": "Quartic convention mismatch: Branco/CE beta functions and stability check (l3+l4+sqrt(l1*l2)>0) initialized with no-1/2 D-term values l1=l2=(g2^2+(3/5)g1^2)/8=0.05 instead of /4=0.10, violating UV stability at t=0 (-0.05 < 0) and shifting all reported l1_IR, l2_IR by ~2x vs no-1/2 convention.",
        },
        {
            "id": "BUG-2",
            "severity": "CRITICAL",
            "location": "verify_a2_p629_veff_modulus_v3.py lines 1269, 1284, 1790",
            "summary": "Guardrail 4 literature transcription error in 2-loop Type-II 2HDM beta functions: uses -29/240*g1^2*Hd in beta_Yu^(2) and -65/240*g1^2*Hu in beta_Yd^(2) instead of exact Chowdhury-Eberhardt (arXiv:1503.08216) & Luo-Wang-Xiao (hep-ph/0211440) -41/240 and -53/240, and copied -29/240 into its own benchmark formula at line 1790.",
        },
        {
            "id": "CONV-3",
            "severity": "MODERATE",
            "location": "verify_a2_p629_veff_modulus_v3.py lines 1884-1905",
            "summary": "DynamicV4_ferro_CURVED_s12 ordering & Y_nu assignment: v3 minimizes flat V_4(h_u,h_d) before applying curved G_{s=1/2} and keeps static S(tau) for Y_nu in Piece 3, whereas Referee minimizes V_4 in the canonical curved basis G^{-1/2} Y G^{-1/2} and couples Y_nu to h_u*.",
        },
    ]

    discrepancies = [x for x in items if not x["match"]]
    by_cause = {}
    for x in discrepancies:
        by_cause[x["root_cause"]] = by_cause.get(x["root_cause"], 0) + 1
    by_cat_fail = {}
    for x in discrepancies:
        by_cat_fail[x["category"]] = by_cat_fail.get(x["category"], 0) + 1
    by_cat_total = {}
    for x in items:
        by_cat_total[x["category"]] = by_cat_total.get(x["category"], 0) + 1

    out = {
        "total_compared": len(items),
        "matched_count": len(items) - len(discrepancies),
        "discrepancies_count": len(discrepancies),
        "by_category_total": by_cat_total,
        "by_category_discrepancies": by_cat_fail,
        "by_root_cause": by_cause,
        "code_audit_findings": code_audit_findings,
        "discrepancies": discrepancies,
        "all_comparisons": items,
    }
    assert_zero_json_floats(out)
    out_path = here / "referee_vs_producer_v3_diff.json"
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"TOTAL_COMPARED={out['total_compared']} MATCHED={out['matched_count']} DISCREPANCIES={out['discrepancies_count']}")
    print("BY_CATEGORY_TOTAL:", by_cat_total)
    print("BY_CATEGORY_DISCREPANCIES:", by_cat_fail)
    print("BY_ROOT_CAUSE:", by_cause)


if __name__ == "__main__":
    main()
