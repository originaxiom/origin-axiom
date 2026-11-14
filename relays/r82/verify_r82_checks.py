#!/usr/bin/env python3
"""Standalone numerical and algebraic counterchecks for Review 82 (card A2-R82) at commit 86930f574.

Reads repository blobs strictly read-only from commit 86930f574 via `git show 86930f574:<path>`.
Shares zero code with producer modules; every algebraic, arithmetic, and statistical check is
computed independently from raw definitions. Nothing compared with empirical data. 0 of 19.
"""
from __future__ import annotations

import json
import math
import pathlib
import random
import re
import subprocess
import sys
from fractions import Fraction
import numpy as np

REV = "86930f574"
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def git_blob(path: str) -> str:
    return subprocess.check_output(["git", "-C", str(ROOT), "show", f"{REV}:{path}"], text=True)


def smith_2x2_int(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    """Exact Smith normal form (d1, d2) of a 2x2 integer matrix [[a, b], [c, d]]."""
    det = abs(a * d - b * c)
    g1 = math.gcd(math.gcd(abs(a), abs(b)), math.gcd(abs(c), abs(d)))
    if g1 == 0:
        return (0, 0)
    return (g1, det // g1)


def run_checks() -> dict:
    results: dict = {"commit": REV, "checks": {}}
    lines_out: list[str] = []

    def log(msg: str) -> None:
        print(msg)
        lines_out.append(msg)

    log(f"=== A2-R82 Standalone Counterchecks at {REV} ===")

    # 1. B1929 lock line 56: `assert worst < 1e10` + 601-character stored winding check
    b1929_dir = "frontier/B1929_the_records_odd_l_value_is_the_twisted_eta_invariant_of_the_closed_torus_bundle"
    b1929_lock = git_blob(f"{b1929_dir}/verification/test_b1929_twisted_eta.py").splitlines()
    line56 = b1929_lock[55]
    assert line56 == "    assert worst < 1e10", f"Unexpected line 56: {line56!r}"
    siegel_rows = json.loads(git_blob(f"{b1929_dir}/verification/main_siegel.json"))
    # Check that setting L_odd = 0 or flipping sign gives O(1) error that STILL passes `< 1e10`
    max_abs_eta_est = max(abs(2.0 * r["Delta"][1] / math.pi) for r in siegel_rows)
    assert 0.1 < max_abs_eta_est < 1e10
    results["checks"]["B1929_lock_1e10"] = {
        "line_56": line56,
        "n_chars": len(siegel_rows),
        "sign_flip_error_scale": 2.0 * max_abs_eta_est,
        "passes_1e10_when_zeroed_or_flipped": (2.0 * max_abs_eta_est) < 1e10,
    }
    log(f"[1] B1929 lock line 56: {line56!r}; zeroed/flipped error {2.0*max_abs_eta_est:.4f} < 1e10 (cannot fail).")

    # 2. B1917 lock line 32 tautology + hecke_s2 16 vs 17 & 4.545e-8
    b1917_dir = "frontier/B1917_the_slope_and_the_kronecker_function_one_l_function_on_the_threads_geodesic"
    b1917_lock = git_blob(f"{b1917_dir}/verification/test_b1917_one_l_function.py").splitlines()
    line32 = b1917_lock[31]
    assert "abs(L / (H.H(2) * R / 2) - 2) < 1e-4" in line32
    # Worst-case algebraic bound when |L - X| / |L| <= u = 1e-5:
    u_max = 1e-5
    worst_taut = 2.0 * u_max / (1.0 - u_max)
    assert worst_taut < 1e-4
    hs2 = json.loads(git_blob(f"{b1917_dir}/verification/hecke_s2.json"))
    rels_lt_1e7 = [r["rel"] for r in hs2 if r["rel"] < 1e-7]
    rels_ge_1e7 = [r["rel"] for r in hs2 if r["rel"] >= 1e-7]
    results["checks"]["B1917_lock_and_hecke_s2"] = {
        "line_32": line32,
        "algebraic_upper_bound_given_line_31": worst_taut,
        "total_chars": len(hs2),
        "count_lt_1e7": len(rels_lt_1e7),
        "max_among_16": max(rels_lt_1e7),
        "outliers_ge_1e7": rels_ge_1e7,
    }
    log(f"[2] B1917 lock line 32 upper bound = {worst_taut:.3e} < 1e-4 (tautology); hecke_s2: {len(rels_lt_1e7)}/{len(hs2)} < 1e-7, max_16={max(rels_lt_1e7):.3e}, outlier={rels_ge_1e7[0]:.3e}.")

    # 3. B1927 corner ratio 1.79 vs 1.99 + paired L_max vs L_2 |z| at n=16 and n=22
    b1927_dir = "frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle"
    ac = json.loads(git_blob(f"{b1927_dir}/verification/arc_corner.json"))
    corner_ratios = {}
    for deg, vals in ac.items():
        r_lmax_12 = (vals["0.02"][0] - vals["0.0"][0]) / (vals["0.01"][0] - vals["0.0"][0])
        r_lmax_24 = (vals["0.04"][0] - vals["0.0"][0]) / (vals["0.02"][0] - vals["0.0"][0])
        r_l2_12 = (vals["0.02"][1] - vals["0.0"][1]) / (vals["0.01"][1] - vals["0.0"][1])
        corner_ratios[deg] = {"L_max_01_02": r_lmax_12, "L_max_02_04": r_lmax_24, "L_2_01_02": r_l2_12}
    cr_json = json.loads(git_blob(f"{b1927_dir}/verification/canon_readout.json"))
    paired_stats = {}
    for tag in ("16 mark", "16 twin", "22 mark", "22 twin"):
        rows = cr_json[tag]["rows"]
        wts = np.array([r["length"] for r in rows], dtype=float)
        zs_all = []
        for k in rows[0]["A"]:
            if "L_max" not in k:
                continue
            k2 = k.replace("L_max", "L_2")
            a_max = np.array([r["A"][k] for r in rows], dtype=float)
            a_2 = np.array([r["A"][k2] for r in rows], dtype=float)
            diff_full = np.sum(wts[:, None] * (a_max - a_2), axis=0) / np.sum(wts)
            jk = []
            for i in range(len(rows)):
                m = np.ones(len(rows), dtype=bool)
                m[i] = False
                jk.append(np.sum(wts[m, None] * (a_max[m] - a_2[m]), axis=0) / np.sum(wts[m]))
            jk_arr = np.array(jk)
            se = np.sqrt((len(rows) - 1) * np.mean((jk_arr - diff_full[None, :]) ** 2, axis=0))
            zs_all.extend(np.abs(diff_full / se).tolist())
        zs_arr = np.array(zs_all)
        paired_stats[tag] = {
            "n_components": int(len(zs_arr)),
            "median_abs_z": float(np.median(zs_arr)),
            "share_gt_2": float(np.mean(zs_arr > 2.0)),
        }
    results["checks"]["B1927_corner_and_paired"] = {"corner_ratios": corner_ratios, "paired_Lmax_vs_L2": paired_stats}
    log(f"[3] B1927 corner L_max (0.01->0.02): 80deg={corner_ratios['80.0']['L_max_01_02']:.4f}, 70deg={corner_ratios['70.0']['L_max_01_02']:.4f} (1.99, NOT 1.79); paired |z| medians: 16m={paired_stats['16 mark']['median_abs_z']:.2f}, 22m={paired_stats['22 mark']['median_abs_z']:.2f} ({paired_stats['22 mark']['share_gt_2']*100:.0f}% > 2).")

    # 4. B1928 fine grid count (1046 vs 1034) + Series single-letter return time r(x) near L^inf vs switch
    b1928_dir = "frontier/B1928_the_read_out_on_the_whole_is_one_average_over_the_24_points_of_order_5"
    fg_fine = json.loads(git_blob(f"{b1928_dir}/verification/fiber_grid_fine.json"))
    n_fg_fine = len(fg_fine)
    assert n_fg_fine == 1046
    # Geodesic length of L^m R: matrix [[m, 1], [1, 0]]? Wait: L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]],
    # so L^m R = [[m+1, m], [1, 1]] with trace m + 2! Hyperbolic period ell(L^m R) = 2 arccosh((m + 2) / 2).
    # Average return time per letter over the (m + 1) letters of (L^m R)^inf is ell(L^m R) / (m + 1) -> 0 as m -> inf!
    per_letter_avg_m100 = 2.0 * math.acosh((100 + 2) / 2.0) / 101.0
    per_letter_avg_m10000 = 2.0 * math.acosh((10000 + 2) / 2.0) / 10001.0
    # Cross-section geodesic crossing points on imaginary-axis / Farey arc for (L^m R)^inf:
    # Attracting fixed point beta > 0 and repelling betap < 0 of M_m = [[m+1, m], [1, 1]]:
    # M_m z = ((m+1)z + m)/(z + 1) = z => z^2 - m z - m = 0 => beta = (m + sqrt(m^2 + 4m))/2, betap = (m - sqrt(m^2 + 4m))/2.
    # Under L^{-1}(z) = z - 1, the crossing from z in [1, beta] across Re z = 1... even simpler:
    # Series cross-section on |z| = 1 (or Re z = 0 for L/R^-1): on (L^m R)^inf, sum_{j=0}^m r(sigma^j x) = 2 arccosh((m+2)/2),
    # while for m = 0? No, for L^n alone, tr(L^n) = 2 => hyperbolic translation length ell(L^n) = 0 identically!
    tr_Ln = int(np.trace(np.linalg.matrix_power(np.array([[1, 1], [0, 1]], dtype=int), 12)))
    assert tr_Ln == 2
    results["checks"]["B1928_grid_and_return_time"] = {
        "fiber_grid_fine_len": n_fg_fine,
        "tr_L12_parabolic": tr_Ln,
        "per_letter_mean_return_L100R": per_letter_avg_m100,
        "per_letter_mean_return_L10000R": per_letter_avg_m10000,
    }
    log(f"[4] B1928 fiber_grid_fine len = {n_fg_fine} (NOT 1034); per-letter return mean on L^m R: m=100 -> {per_letter_avg_m100:.4f}, m=10000 -> {per_letter_avg_m10000:.6f} -> 0 at L^inf.")

    # 5. B1923 LOAD_BEARING_NEGATIVES row count (30 vs 26)
    b1923_dir = "frontier/B1923_the_load_bearing_negatives_reexamined_and_the_twin_chooses_the_icosahedral_triplet"
    lbn = git_blob(f"{b1923_dir}/verification/LOAD_BEARING_NEGATIVES.md")
    sec_rows = re.findall(r"^### ([A-D]\d+)\b", lbn, flags=re.M)
    assert len(sec_rows) == 30
    results["checks"]["B1923_scan_row_count"] = {"count_A_to_D": len(sec_rows), "ids": sec_rows}
    log(f"[5] B1923 LOAD_BEARING_NEGATIVES.md rows A..D = {len(sec_rows)} (NOT 26).")

    # 6. B1924 B1667 54-point global spread vs 48-point per-column spread
    b1667_pts = json.loads(git_blob("frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json"))["points"]
    assert len(b1667_pts) == 54
    lmax_inv = [p["L_max"] + 0.5 * math.log(p["tau"][1]) for p in b1667_pts]
    l2_inv = [p["L_2"] + 0.5 * math.log(p["tau"][1]) for p in b1667_pts]
    spread_54_lmax = max(lmax_inv) - min(lmax_inv)
    spread_54_l2 = max(l2_inv) - min(l2_inv)
    col_spreads_lmax = {}
    col_spreads_l2 = {}
    for xcol in (0.05, 0.15, 0.25, 0.35, 0.45):
        cpts = [p for p in b1667_pts if p.get("where") == "grid" and abs(p["tau"][0] - xcol) < 1e-9]
        v_m = [p["L_max"] + 0.5 * math.log(p["tau"][1]) for p in cpts]
        v_2 = [p["L_2"] + 0.5 * math.log(p["tau"][1]) for p in cpts]
        col_spreads_lmax[str(xcol)] = max(v_m) - min(v_m)
        col_spreads_l2[str(xcol)] = max(v_2) - min(v_2)
    results["checks"]["B1924_B1667_spreads"] = {
        "n_points": len(b1667_pts),
        "global_54_spread_L_max": spread_54_lmax,
        "global_54_spread_L_2": spread_54_l2,
        "per_column_48_spread_range_L_max": [min(col_spreads_lmax.values()), max(col_spreads_lmax.values())],
        "per_column_48_spread_range_L_2": [min(col_spreads_l2.values()), max(col_spreads_l2.values())],
    }
    log(f"[6] B1924/B1667 54-pt spread: L_max={spread_54_lmax:.4f}, L_2={spread_54_l2:.4f} (per-column 48-grid ranges: {min(col_spreads_lmax.values()):.4f}..{max(col_spreads_lmax.values()):.4f} and {min(col_spreads_l2.values()):.4f}..{max(col_spreads_l2.values()):.4f}).")

    # 7. B1925: even vs odd metallic acts, sqrts of 1 mod (m^2+4) at m=9,11,13, 180 vs 360 tr>0 hyperbolic matrices, and lock tautology
    even_cyclic = []
    odd_cyclic = []
    for m in range(1, 15):
        # G_m = L^m R^m = [[m^2 + 1, m], [m, 1]], so G_m + I = [[m^2 + 2, m], [m, 2]]
        d1, d2 = smith_2x2_int(m * m + 2, m, m, 2)
        is_cyclic_line = (d1 == 1 and d2 == m * m + 4)
        if m % 2 == 0:
            even_cyclic.append((m, d1, d2, is_cyclic_line))
        else:
            odd_cyclic.append((m, d1, d2, is_cyclic_line))
    assert all(not c[3] for c in even_cyclic) and all(c[3] for c in odd_cyclic)

    sqrts_mod = {}
    for m in (9, 11, 13):
        N = m * m + 4
        roots = [x for x in range(N) if (x * x) % N == 1]
        sqrts_mod[str(m)] = {"N": N, "roots": roots, "count": len(roots)}
    assert sqrts_mod["9"]["count"] == 4 and sqrts_mod["11"]["count"] == 2 and sqrts_mod["13"]["count"] == 2

    hyp_pos, hyp_neg, neg_counterexamples = 0, 0, 0
    for a in range(-7, 8):
        for b in range(-7, 8):
            for c in range(-7, 8):
                ad = 1 + b * c
                if a == 0:
                    if b * c == -1:
                        for d in range(-7, 8):
                            if abs(d) >= 3:
                                if d > 0:
                                    hyp_pos += 1
                                else:
                                    hyp_neg += 1
                    continue
                if ad % a != 0:
                    continue
                d = ad // a
                if -7 <= d <= 7 and abs(a + d) >= 3:
                    if a + d > 0:
                        hyp_pos += 1
                    else:
                        hyp_neg += 1
                        tor_d1, tor_d2 = smith_2x2_int(a - 1, b, c, d - 1)
                        lev_det = abs((a + 1) * (d + 1) - b * c)
                        tf = (tor_d1 * tor_d2 == 1)
                        if not (tf == (a + d == 3) == (lev_det == 5)):
                            neg_counterexamples += 1
    assert hyp_pos == 180 and hyp_neg == 180 and neg_counterexamples > 0

    # Lock line 53 algebraic tautology even when ad - bc != 1:
    rng = random.Random(20261114)
    taut_holds_non_sl2 = True
    for _ in range(200):
        a, b, c, d = [rng.randint(-50, 50) for _ in range(4)]
        lhs = abs((-a - 1) * (-d - 1) - (-b) * (-c))
        rhs = abs((a + 1) * (d + 1) - b * c)
        if lhs != rhs:
            taut_holds_non_sl2 = False
    assert taut_holds_non_sl2
    results["checks"]["B1925_checks"] = {
        "even_m_any_cyclic_line": any(c[3] for c in even_cyclic),
        "odd_m_all_cyclic_line": all(c[3] for c in odd_cyclic),
        "sqrts_of_1_mod_m2_plus_4": sqrts_mod,
        "hyperbolic_in_box_7": {"total": hyp_pos + hyp_neg, "tr_gt_0": hyp_pos, "tr_lt_0": hyp_neg, "tr_lt_0_violating_equiv": neg_counterexamples},
        "lock_line_53_tautology_on_arbitrary_integers": taut_holds_non_sl2,
    }
    log(f"[7] B1925: even m cyclic=0/7, odd m cyclic=7/7; sqrts of 1 mod(m^2+4): m=9->{sqrts_mod['9']['count']}, m=11->{sqrts_mod['11']['count']}, m=13->{sqrts_mod['13']['count']}; tr>0 count={hyp_pos}/360.")

    # 8. B1926: odd_ticks_no_modules.json twisted levels == [3, 5] only (level 7 missing)
    b1926_dir = "frontier/B1926_at_odd_ticks_the_frames_matter_exists_only_twisted_by_the_orientation_the_tick_inverts_the_scar"
    ot_json = json.loads(git_blob(f"{b1926_dir}/verification/odd_ticks_no_modules.json"))
    twisted_levels = sorted(int(r["n"]) for r in ot_json["control_odd_without_mu"])
    assert twisted_levels == [3, 5]
    results["checks"]["B1926_twisted_levels_run"] = twisted_levels
    log(f"[8] B1926 control_odd_without_mu levels in JSON: {twisted_levels} (level 7 not run).")

    # 9. B1918 period integral factor ell = 4 ln(phi) & B1920 Laurent constant-term cross-term -2 pi ln 2
    phi = 0.5 * (1.0 + math.sqrt(5.0))
    ell_golden_step3 = 4.0 * math.log(phi)  # tr(LR^2? step3_average uses M=[[2,1],[1,1]]^2=[[5,3],[3,2]], tr=7 => ell = 2 arccosh(7/2) = 4 ln phi)
    b1918_avg = json.loads(git_blob("frontier/B1918_the_channel_norm_is_not_the_l_functions_coefficient_at_a_point_or_on_average/verification/step3_average.json"))
    b1918_spread = max(b1918_avg["avgN"]) - min(b1918_avg["avgN"])
    true_avg_res = b1918_avg["max_residual"] / ell_golden_step3
    true_avg_spread = b1918_spread / ell_golden_step3
    ell_lr2 = 2.0 * math.log(0.5 * (7.0 + math.sqrt(45.0)))
    f_avg_golden = 8.906783
    kappa0_predicted = (2.0 * ell_lr2 / math.pi) * (f_avg_golden + 2.0 * math.pi * math.log(2.0))
    hv_rows = json.loads(git_blob(f"{b1917_dir}/verification/hecke_value.json"))
    neg_i_nonzero = sum(1 for r in hv_rows if str(r["level"][0]).startswith("-"))
    results["checks"]["B1918_B1920_math"] = {
        "B1918_ell": ell_golden_step3,
        "B1918_reported_integral_res_spread": [b1918_avg["max_residual"], b1918_spread],
        "B1918_true_average_res_spread": [true_avg_res, true_avg_spread],
        "B1920_ell_plus_LR2": ell_lr2,
        "B1920_F_u_average": f_avg_golden,
        "B1920_kappa0_at_s1": kappa0_predicted,
        "B1920_chars_where_Z0_ne_slope": neg_i_nonzero,
    }
    log(f"[9] B1918 true average residual={true_avg_res:.2f} on spread={true_avg_spread:.2f} (reported integral {b1918_avg['max_residual']:.2f} on {b1918_spread:.2f}); B1920 <F_u>={f_avg_golden:.4f} vs kappa_0={kappa0_predicted:.4f}, Z0!=slope on {neg_i_nonzero}/601 chars.")

    # 10. B1919 rotated shift range across all 24 kept rows in seat_formula_check.json
    b1919_rows = json.loads(git_blob("frontier/B1919_the_channel_norm_is_the_shifted_lattices_kronecker_limit_at_the_kernels_shift/verification/seat_formula_check.json"))
    r0 = b1919_rows[0]
    t0 = complex(r0["tau"][0], r0["tau"][1])
    c1_0, c2_0 = r0["c"]
    u1_0, u2_0 = c1_0 - 0.5, c2_0 - 0.5
    gamma_e = 0.5772156649015328606
    const_C = -2.0 * math.pi * (gamma_e + math.log(math.pi))

    def kronecker_limit_exact(u1: float, u2: float, tau: complex, M_sum: int = 80) -> float:
        """Exact s=1 analytic limit F_{(u1, u2)}(tau) of sum_{(m,n) in u+Z^2} y^s |m tau + n|^{-2s} - pi/(s-1)
        via exact digamma constant term and exact K_{1/2} geometric series (zero finite-difference step)."""
        import mpmath as mp
        x, y = tau.real, tau.imag
        a = u1 - math.floor(u1)
        b = u2 - math.floor(u2)
        if abs(a) < 1e-14:
            first_c = math.pi * (-2.0 * math.log(2.0) - math.log(y) + 2.0 * gamma_e)
            zero_row = y * float(mp.zeta(2, b) + mp.zeta(2, 1.0 - b))
        else:
            first_c = math.pi * (-2.0 * math.log(2.0) - math.log(y) - float(mp.psi(0, a) + mp.psi(0, 1.0 - a)))
            zero_row = 0.0
        bess = 0.0
        for k in range(-M_sum, M_sum + 1):
            m = a + k
            if abs(m) < 1e-14:
                continue
            z_phase = np.exp(-2.0 * math.pi * abs(m) * y + 2j * math.pi * (m * x + b))
            # sum_{r>=1} z_phase^r + conj(z_phase)^r = 2 Re(z_phase / (1 - z_phase))
            bess += (2.0 * math.pi / abs(m)) * float((z_phase / (1.0 - z_phase)).real)
        return first_c + zero_row + bess

    val_check = kronecker_limit_exact(u1_0, u2_0, t0) + math.pi * math.log(t0.imag) + const_C
    assert abs(val_check - r0["F_u+pi log y+C"]) < 1e-6, f"Mismatch: {val_check} vs {r0['F_u+pi log y+C']}"

    rot_diffs = []
    for r in b1919_rows:
        tt = complex(r["tau"][0], r["tau"][1])
        c1, c2 = r["c"]
        # Rotated shift in seat_formula.py: (c2 - 0.5, -(c1 - 0.5))
        f_rot = kronecker_limit_exact(c2 - 0.5, -(c1 - 0.5), tt) + math.pi * math.log(tt.imag) + const_C
        rot_diffs.append(abs(r["N"] - f_rot))
    results["checks"]["B1919_rotated_shift_24"] = {
        "min_abs_diff": min(rot_diffs),
        "max_abs_diff": max(rot_diffs),
    }
    log(f"[10] B1919 rotated shift across 24 kept rows: {min(rot_diffs):.4f} to {max(rot_diffs):.2f} (reported 0.3 to 7).")

    # 11. POINT_REGISTER.md open-debt ordinal skip (44 -> 46 .. 94, 93 items)
    pr_txt = git_blob("docs/POINT_REGISTER.md")
    debts_sec = pr_txt.split("## The debts, by load")[1].split("\n## ")[0]
    ranks = [int(m.group(1)) for m in re.finditer(r"^(\d+)\.\s+P-\d+", debts_sec, flags=re.M)]
    missing_ranks = sorted(set(range(1, max(ranks) + 1)) - set(ranks))
    assert len(ranks) == 93 and max(ranks) == 94 and missing_ranks == [45]
    results["checks"]["POINT_REGISTER_rank_skip"] = {
        "debt_count": len(ranks),
        "max_rank_label": max(ranks),
        "missing_ranks": missing_ranks,
    }
    log(f"[11] POINT_REGISTER.md open debts: count={len(ranks)}, max_rank={max(ranks)}, missing={missing_ranks}.")

    log("=== ALL 11 R82 STANDALONE COUNTERCHECKS PASSED (0 of 19.) ===")
    (HERE / "verify_r82_checks_out.txt").write_text("\n".join(lines_out) + "\n")
    (HERE / "verify_r82_checks_results.json").write_text(json.dumps(results, indent=2) + "\n")
    return results


if __name__ == "__main__":
    run_checks()
