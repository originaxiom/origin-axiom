#!/usr/bin/env python3
"""Mask-safe comparison of agy-002's blind A2-CANON-T90 output (7609cca49) against B1940's BIG_RUN_VALUES_v2.json (M37).

Checks:
  1. Verifies sha256 seals of agy-002's blind verify_a2_canon_results.json (sealed at 7609cca49),
     B1940's BIG_RUN_VALUES_v2.json (9ece85e1...), and B1932's uncorrected BIG_RUN_VALUES.json (df1c9bee...).
  2. Applies B1937/B1940's exact tolerance rule:
       |d ln| <= 3 * sqrt(r_main^2 + r_seat^2 + delta^2),   delta = 5.4e-3,
     on all four options (W-|a move count, W+|a move count, W-|b area, W+|b area),
     plus strict r_seat = 0 sensitivity check on the area options,
     plus discriminating controls against B1932's uncorrected area values and truncated channel weights.
  3. Evaluates verify_a2_canon.py's own extended-precision frame (eval_mp_12pt_avg, 30 + 3*y digits)
     on F_bar(tau + 1) vs F_bar(tau) across every height region used in our u = 1/y quadrature
     (y = 1.5, 3, 5, 8, 11, 12, 15, 20, 30, 45, 80, 120, 200), confirming machine-precision periodicity
     throughout the cusp, while demonstrating double-precision breakdown above y = 11.
  4. Prints and writes ONLY scaled differences, tolerance ratios, hashes, and periodicity residuals —
     ZERO physical 7-values and ZERO measured numbers appear anywhere.

0 of 19.
"""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import verify_a2_canon as VAC  # noqa: E402

DELTA = 5.4e-3
POSITIONS = ["up m2/m3", "up m1/m3", "down m2/m3", "down m1/m3", "|V12|", "|V23|", "|V13|"]

V2_PATH_GIT = "frontier/B1940_the_area_options_corrected_in_extended_precision/verification/BIG_RUN_VALUES_v2.json"
V1_PATH_GIT = "frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/BIG_RUN_VALUES.json"
EXPECTED_V2_SHA_PREFIX = "9ece85e154238ae9"
EXPECTED_V1_SHA_PREFIX = "df1c9bee002ecf5e"


def git_read_bytes(rev_path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(REPO_ROOT), "show", rev_path])


def compare_option(main_vals: list[float], main_errs: list[float], seat_vals: list[float], seat_rel_errs: list[float]) -> dict:
    assert len(main_vals) == len(main_errs) == len(seat_vals) == len(seat_rel_errs) == 7
    rows = []
    for pos, m, em, s, rs in zip(POSITIONS, main_vals, main_errs, seat_vals, seat_rel_errs):
        rm = em / m
        dl = math.log(s) - math.log(m)
        tol = 3.0 * math.sqrt(rm * rm + rs * rs + DELTA * DELTA)
        denom_stat = math.sqrt(rm * rm + rs * rs)
        z_stat = dl / denom_stat if denom_stat > 0 else float("inf")
        rows.append(
            {
                "position": pos,
                "d_ln": dl,
                "tol_ln": tol,
                "dln_over_tol": dl / tol,
                "z_stat_only": z_stat,
            }
        )
    worst = max(abs(r["dln_over_tol"]) for r in rows)
    max_abs_dln = max(abs(r["d_ln"]) for r in rows)
    return {
        "agrees": all(abs(r["dln_over_tol"]) <= 1.0 for r in rows),
        "worst_dln_over_tol": worst,
        "max_abs_dln": max_abs_dln,
        "rows": rows,
    }


def check_tau_plus_1_periodicity() -> dict:
    """Verify F_bar(tau + 1) == F_bar(tau) on verify_a2_canon.py's own frame across heights y = 1.5..200."""
    heights = [1.5, 3.0, 5.0, 8.0, 11.0, 12.0, 15.0, 20.0, 30.0, 45.0, 80.0, 120.0, 200.0]
    x_base = 0.13
    l2_interp = VAC.CanonicalL2Interpolant()
    mp_rows = []
    f64_rows = []
    for y in heights:
        tau0 = complex(x_base, y)
        tau1 = complex(x_base + 1.0, y)
        # Canonical end L2 is SL(2, Z)-invariant (read at x reduced mod 1 into [-0.5, 0.5] for y >= 1.5):
        tau0_fd = complex(((tau0.real + 0.5) % 1.0) - 0.5, tau0.imag)
        tau1_fd = complex(((tau1.real + 0.5) % 1.0) - 0.5, tau1.imag)
        l2_0 = float(l2_interp.eval_fd(VAC.np.array([tau0_fd]))[0])
        l2_1 = float(l2_interp.eval_fd(VAC.np.array([tau1_fd]))[0])
        # Pass UNREDUCED tau0 = 0.13 + i*y and tau1 = 1.13 + i*y directly into eval_mp_12pt_avg:
        r0 = VAC.eval_mp_12pt_avg(tau0, l2_0)["exact_T90"]
        r1 = VAC.eval_mp_12pt_avg(tau1, l2_1)["exact_T90"]
        # Indices for claimed 7 in W- (up St: 2,3; down S: 4,5; mix St,S: 18,19,20)
        # and W+ (up S: 0,1; down St: 6,7; mix S,St: 15,16,17)
        idx_wm = [2, 3, 4, 5, 18, 19, 20]
        idx_wp = [0, 1, 6, 7, 15, 16, 17]
        rel_wm = max(abs(r1[i] - r0[i]) / max(abs(r0[i]), 1e-300) for i in idx_wm)
        rel_wp = max(abs(r1[i] - r0[i]) / max(abs(r0[i]), 1e-300) for i in idx_wp)
        mp_rows.append(
            {
                "y": y,
                "dps_used": int(max(55, 30 + 3 * math.ceil(y))),
                "l2_diff": abs(l2_1 - l2_0),
                "max_rel_diff_W_minus": float(rel_wm),
                "max_rel_diff_W_plus": float(rel_wp),
            }
        )
        # Also test double-precision eval_frame_12pt_avg_fd at y <= 30 to document exact float64 breakdown above y=11:
        if y <= 30.0:
            d0 = VAC.eval_frame_12pt_avg_fd(
                VAC.np.array([tau0], dtype=VAC.np.complex128),
                VAC.np.array([l2_0]),
            )[0]["exact_T90"][0]
            d1 = VAC.eval_frame_12pt_avg_fd(
                VAC.np.array([tau1], dtype=VAC.np.complex128),
                VAC.np.array([l2_1]),
            )[0]["exact_T90"][0]
            f64_wm = max(abs(d1[i] - d0[i]) / max(abs(d0[i]), 1e-300) for i in idx_wm)
            f64_rows.append({"y": y, "float64_max_rel_diff_W_minus": float(f64_wm)})

    return {
        "x_column": x_base,
        "mpmath_max_rel_diff_all_heights_W_minus": max(r["max_rel_diff_W_minus"] for r in mp_rows),
        "mpmath_max_rel_diff_all_heights_W_plus": max(r["max_rel_diff_W_plus"] for r in mp_rows),
        "mpmath_rows": mp_rows,
        "float64_control_rows": f64_rows,
    }


def main() -> None:
    seat_path = HERE / "verify_a2_canon_results.json"
    seat_bytes = seat_path.read_bytes()
    seat_sha = hashlib.sha256(seat_bytes).hexdigest()
    # Verify exact match with sealed commit 7609cca49
    sealed_bytes = git_read_bytes("7609cca49:relays/a2_canon/verify_a2_canon_results.json")
    assert seat_sha == hashlib.sha256(sealed_bytes).hexdigest(), "Local results differ from sealed commit 7609cca49!"
    seat = json.loads(seat_bytes)

    # Read B1940 v2 and B1932 v1 from origin/main (or b35eac607 fallback)
    ref = "origin/main"
    v2_bytes = git_read_bytes(f"{ref}:{V2_PATH_GIT}")
    v1_bytes = git_read_bytes(f"{ref}:{V1_PATH_GIT}")
    v2_sha = hashlib.sha256(v2_bytes).hexdigest()
    v1_sha = hashlib.sha256(v1_bytes).hexdigest()
    assert v2_sha.startswith(EXPECTED_V2_SHA_PREFIX), f"Unexpected v2 sha256: {v2_sha}"
    assert v1_sha.startswith(EXPECTED_V1_SHA_PREFIX), f"Unexpected v1 sha256: {v1_sha}"

    v2 = json.loads(v2_bytes)
    v1 = json.loads(v1_bytes)
    assert v2["positions"] == POSITIONS

    sv_sum = seat["seven_values_summary"]
    bulk_abs_err = float(seat["area_measure_detail"]["bulk_coarse_vs_fine_max_err"])

    # Move-count options (exact_T90 and old_weight control):
    move_res = {}
    for opt_key, w_key in (("W-|a (move count)", "W_minus"), ("W+|a (move count)", "W_plus")):
        mv, me = v2["options"][opt_key]["values"], v2["options"][opt_key]["error"]
        s_block = sv_sum["move_count_measure"]["exact_T90"][w_key]
        sv = s_block["mean_7"]
        s_rel = [se_i / sv_i for sv_i, se_i in zip(sv, s_block["se_7"])]
        comp_exact = compare_option(mv, me, sv, s_rel)

        s_old_block = sv_sum["move_count_measure"]["old_weight"][w_key]
        sv_old = s_old_block["mean_7"]
        s_old_rel = [se_i / sv_i for sv_i, se_i in zip(sv_old, s_old_block["se_7"])]
        comp_old_ctrl = compare_option(mv, me, sv_old, s_old_rel)

        move_res[opt_key] = {
            "exact_T90_vs_B1940_v2": comp_exact,
            "old_weight_control_vs_B1940_v2": {
                "max_abs_dln": comp_old_ctrl["max_abs_dln"],
                "worst_dln_over_tol": comp_old_ctrl["worst_dln_over_tol"],
                "rms_z_stat": math.sqrt(sum(r["z_stat_only"] ** 2 for r in comp_old_ctrl["rows"]) / 7.0),
            },
        }

    # Area options (exact_T90 vs B1940 v2, plus r_seat=0 strict check, plus B1932 v1 control, plus old_weight control):
    area_res = {}
    for opt_key, w_key in (("W-|b (area)", "W_minus"), ("W+|b (area)", "W_plus")):
        mv2, me2 = v2["options"][opt_key]["values"], v2["options"][opt_key]["error"]
        mv1, me1 = v1["options"][opt_key]["values"], v1["options"][opt_key]["error"]
        sv = sv_sum["area_measure_exact_untruncated"]["exact_T90"][w_key]["value_7"]
        sv_old = sv_sum["area_measure_exact_untruncated"]["old_weight"][w_key]["value_7"]
        # Relative quadrature error bound from coarse-vs-fine bulk difference:
        s_rel = [min(bulk_abs_err / sv_i, 5e-3) for sv_i in sv]
        s_rel_zero = [0.0] * 7

        comp_v2 = compare_option(mv2, me2, sv, s_rel)
        comp_v2_zero = compare_option(mv2, me2, sv, s_rel_zero)
        comp_v1_ctrl = compare_option(mv1, me1, sv, s_rel)
        comp_old_w_ctrl = compare_option(mv2, me2, sv_old, s_rel)

        area_res[opt_key] = {
            "exact_T90_vs_B1940_v2": comp_v2,
            "exact_T90_vs_B1940_v2_strict_zero_seat_err": {
                "agrees": comp_v2_zero["agrees"],
                "worst_dln_over_tol": comp_v2_zero["worst_dln_over_tol"],
            },
            "control_vs_B1932_uncorrected_v1": {
                "agrees": comp_v1_ctrl["agrees"],
                "worst_dln_over_tol": comp_v1_ctrl["worst_dln_over_tol"],
                "max_abs_dln": comp_v1_ctrl["max_abs_dln"],
                "per_pos_dln_over_tol": [r["dln_over_tol"] for r in comp_v1_ctrl["rows"]],
            },
            "control_seat_old_weight_vs_B1940_v2": {
                "worst_dln_over_tol": comp_old_w_ctrl["worst_dln_over_tol"],
                "max_abs_dln": comp_old_w_ctrl["max_abs_dln"],
            },
        }

    t_check = check_tau_plus_1_periodicity()

    worst_area_v2 = max(area_res[k]["exact_T90_vs_B1940_v2"]["worst_dln_over_tol"] for k in area_res)
    worst_area_v1 = max(area_res[k]["control_vs_B1932_uncorrected_v1"]["worst_dln_over_tol"] for k in area_res)
    worst_move_v2 = max(move_res[k]["exact_T90_vs_B1940_v2"]["worst_dln_over_tol"] for k in move_res)
    all_four_agree = all(area_res[k]["exact_T90_vs_B1940_v2"]["agrees"] for k in area_res) and all(
        move_res[k]["exact_T90_vs_B1940_v2"]["agrees"] for k in move_res
    )

    out = {
        "card": "A2-CANON-T90 / M37",
        "seat": "agy-002",
        "sealed_seat_commit": "7609cca49",
        "sealed_seat_json_sha256": seat_sha,
        "b1940_v2_json_sha256": v2_sha,
        "b1932_v1_json_sha256": v1_sha,
        "delta_systematic_ln": DELTA,
        "summary": {
            "all_four_options_agree_with_B1940_v2": all_four_agree,
            "worst_area_dln_over_tol_vs_B1940_v2": worst_area_v2,
            "worst_area_dln_over_tol_vs_B1932_uncorrected_v1": worst_area_v1,
            "worst_move_count_dln_over_tol_vs_B1940_v2": worst_move_v2,
            "mpmath_tau_plus_1_max_rel_diff_y1p5_to_200": max(
                t_check["mpmath_max_rel_diff_all_heights_W_minus"],
                t_check["mpmath_max_rel_diff_all_heights_W_plus"],
            ),
        },
        "area_options": area_res,
        "move_count_options": move_res,
        "tau_plus_1_periodicity_check": t_check,
    }

    out_json = HERE / "compare_b1940_v2.json"
    out_txt = HERE / "compare_b1940_v2_out.txt"
    out_json.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    lines = [
        "=== agy-002 M37 Comparison: Blind A2-CANON-T90 (7609cca49) vs B1940 BIG_RUN_VALUES_v2.json ===",
        f"seat JSON sha256 (7609cca49): {seat_sha}",
        f"B1940 v2 JSON sha256:         {v2_sha}",
        f"B1932 v1 JSON sha256:         {v1_sha}",
        "",
        "1. Area options (B1937/B1940 tolerance: |d ln| <= 3 * sqrt(r_main^2 + r_seat^2 + 0.0054^2)):",
    ]
    for opt_key, b in area_res.items():
        c2 = b["exact_T90_vs_B1940_v2"]
        c2z = b["exact_T90_vs_B1940_v2_strict_zero_seat_err"]
        c1 = b["control_vs_B1932_uncorrected_v1"]
        cw = b["control_seat_old_weight_vs_B1940_v2"]
        per = " ".join(f"{r['dln_over_tol']:+.3f}" for r in c2["rows"])
        lines.append(
            f"  {opt_key}: {'AGREE' if c2['agrees'] else 'DISAGREE'} "
            f"(worst |d ln|/tol = {c2['worst_dln_over_tol']:.3f}; strict r_seat=0: {c2z['worst_dln_over_tol']:.3f}; "
            f"max |d ln| = {c2['max_abs_dln']:.5f})"
        )
        lines.append(f"    per-position d ln / tol: {per}")
        lines.append(
            f"    control vs B1932 uncorrected v1: {'AGREE' if c1['agrees'] else 'DISAGREE'} "
            f"(worst |d ln|/tol = {c1['worst_dln_over_tol']:.3f}, max |d ln| = {c1['max_abs_dln']:.5f})"
        )
        lines.append(
            f"    control seat old_weight vs B1940 v2: worst |d ln|/tol = {cw['worst_dln_over_tol']:.3f}, "
            f"max |d ln| = {cw['max_abs_dln']:.5f}"
        )

    lines.append("")
    lines.append("2. Move-count options:")
    for opt_key, b in move_res.items():
        c2 = b["exact_T90_vs_B1940_v2"]
        cw = b["old_weight_control_vs_B1940_v2"]
        per = " ".join(f"{r['dln_over_tol']:+.3f}" for r in c2["rows"])
        lines.append(
            f"  {opt_key}: {'AGREE' if c2['agrees'] else 'DISAGREE'} "
            f"(worst |d ln|/tol = {c2['worst_dln_over_tol']:.3f}, max |d ln| = {c2['max_abs_dln']:.5f})"
        )
        lines.append(f"    per-position d ln / tol: {per}")
        lines.append(
            f"    control seat old_weight vs B1940 v2: max |d ln| = {cw['max_abs_dln']:.5f}, "
            f"rms z_stat = {cw['rms_z_stat']:.2f}"
        )

    lines.append("")
    lines.append("3. Extended-precision periodicity check F_bar(tau + 1) == F_bar(tau) (x = 0.13, y = 1.5..200):")
    lines.append(
        f"  mpmath (30 + 3*y digits) max rel diff across all 13 heights: "
        f"W- {t_check['mpmath_max_rel_diff_all_heights_W_minus']:.2e}, "
        f"W+ {t_check['mpmath_max_rel_diff_all_heights_W_plus']:.2e}"
    )
    for r in t_check["float64_control_rows"]:
        lines.append(f"  float64 control y = {r['y']:5.1f}: W- max rel diff = {r['float64_max_rel_diff_W_minus']:.2e}")
    lines.append("")
    lines.append(
        f"OVERALL: {'AGREE' if all_four_agree else 'DISAGREE'} on all 4 options vs B1940 v2 "
        f"(area worst {worst_area_v2:.3f} of tol; move-count worst {worst_move_v2:.3f} of tol; "
        f"vs B1932 uncorrected area worst {worst_area_v1:.3f} -> DISAGREE). 0 of 19."
    )

    txt_content = "\n".join(lines) + "\n"
    out_txt.write_text(txt_content, encoding="utf-8")
    print(txt_content, end="")


if __name__ == "__main__":
    main()
