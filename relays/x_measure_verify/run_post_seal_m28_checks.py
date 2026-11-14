#!/usr/bin/env python3
"""
Post-seal M28 verification checks for agy-exp (X-MEASURE / area options).
Runs AFTER the raw X-MEASURE output (verify_x_measure_out.json) was sealed at 04293e826.

Performs the two checks requested in M27 and M28:
1. Comparison of agy-exp's sealed area readout (04293e826) against B1940's
   BIG_RUN_VALUES_v2.json (sha256 9ece85e1...) using B1937's / B1940's exact
   tolerance rule: |d ln| <= 3 * sqrt(e_main^2 + e_seat^2 + delta^2), delta = 5.4e-3.
2. Verification of the T-invariance identity F_bar(tau + 1) = F_bar(tau) (unreduced
   tau -> tau + 1 on entries and SVD) across every height regime used by our code
   (bulk float64 on y <= 5, and full dynamic-precision mpmath on y > 5: y = 5, 6, 12,
   20, 35, 45, 60, 120), plus a planted 15-digit control at y = 20 verifying that
   insufficient entry precision is caught by the T-check.

Strict mask hygiene: zero floating-point literals or scientific notation printed to stdout;
all numerical diagnostics written exclusively to post_seal_m28_checks.json.
Empirical firewall: 0 of 19 measured values touched.
"""

import hashlib
import json
import math
import pathlib
import subprocess
import time
from typing import Any, Dict, List

import mpmath as mp
import numpy as np

import verify_x_measure as vxm


ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent

POSITIONS = [
    "up__2_over_3",
    "up__1_over_3",
    "down__2_over_3",
    "down__1_over_3",
    "mixing__1_2",
    "mixing__2_3",
    "mixing__1_3",
]

DELTA_SYS = 5.4e-3


def eval_p5_avg_t90_mp_fixed_dps(x_val: float, y_val: float, l2_raw_val: float, fixed_dps: int) -> List[mp.mpf]:
    """
    Exact mirror of verify_x_measure.eval_p5_avg_four_modes_mp (W_minus_T90, 12 outputs)
    returning pure mp.mpf values and allowing fixed_dps override for planted low-dps V3 check
    and ultra-high-y relative error checks beyond IEEE-754 float64 exponent range.
    """
    with mp.workdps(fixed_dps):
        tau = mp.mpc(mp.mpf(repr(x_val)), mp.mpf(repr(y_val)))
        yv = mp.im(tau)
        l2 = mp.mpf(repr(l2_raw_val))
        tl2 = l2 + mp.mpf("0.5") * mp.log(yv) - (mp.euler + mp.log(mp.pi))
        exp_m2l2 = mp.exp(-2 * l2)

        xq = mp.exp(mp.j * mp.pi * tau / 4)
        c3_s = [mp.mpc(0), mp.mpc(0), mp.mpc(0)]
        cutoff_serre = mp.mpf(10) ** (-(fixed_dps + 10))
        for k_int, cols_frac in vxm.SERRE_EXACT_ROWS:
            pw = xq ** k_int
            if abs(pw) < cutoff_serre and k_int > 8:
                break
            for col_j in range(3):
                fr, fi = cols_frac[col_j]
                if fr or fi:
                    c_mp = mp.mpc(mp.mpf(fr.numerator) / fr.denominator, mp.mpf(fi.numerator) / fi.denominator)
                    c3_s[col_j] += pw * c_mp
        c3_st = [mp.conj(z) for z in c3_s]

        def th_char(al: mp.mpf, be: mp.mpf) -> mp.mpc:
            at = al - mp.nint(al)
            s = mp.mpc(0)
            for k in range(-9, 10):
                m = mp.mpf(k) + at
                s += mp.exp(mp.j * mp.pi * tau * m * m + 2 * mp.j * mp.pi * m * be)
            return s

        def a0_char(al: mp.mpf, be: mp.mpf) -> mp.mpc:
            at = al - mp.nint(al)
            num = mp.mpc(0)
            den = mp.mpc(0)
            for k in range(-9, 10):
                m = mp.mpf(k) + at
                t = mp.exp(mp.j * mp.pi * tau * m * m + 2 * mp.j * mp.pi * m * be)
                den += t
                num += 2 * mp.j * mp.pi * m * t
            return num / den

        th1p0 = mp.mpc(0)
        for k in range(10):
            h = mp.mpf(k) + mp.mpf("0.5")
            th1p0 += ((-1) ** k) * (2 * k + 1) * mp.exp(mp.j * mp.pi * tau * h * h)
        th1p0 *= 2 * mp.pi

        z_thr = mp.mpf(10) ** (-(fixed_dps - 5))

        def f_kron(u1: mp.mpf, u2: mp.mpf) -> mp.mpf:
            a = u1 - mp.floor(u1)
            b = u2 - mp.floor(u2)
            az = (abs(a) < mp.mpf("1e-35")) or (abs(a - 1) < mp.mpf("1e-35"))
            bz = (abs(b) < mp.mpf("1e-35")) or (abs(b - 1) < mp.mpf("1e-35"))
            if az:
                base = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yv))
                if not bz:
                    base += yv * (mp.pi ** 2) / (mp.sin(mp.pi * b) ** 2)
                a_eff = mp.mpf(0)
            else:
                base = -mp.pi * (2 * mp.log(2) + mp.log(yv) + mp.digamma(a) + mp.digamma(1 - a))
                a_eff = a
            tot = base
            for k in range(-14, 15):
                m = mp.mpf(k) + a_eff
                if abs(m) > mp.mpf("1e-35"):
                    w = mp.exp(-2 * mp.pi * abs(m) * yv + 2 * mp.j * mp.pi * (m * mp.re(tau) + u2))
                    if abs(w) > cutoff_serre:
                        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
            return tot

        half = mp.mpf("0.5")
        acc = [mp.mpf(0) for _ in range(12)]
        for ja, jb in vxm.P5_HALF_12_INT:
            a_p = mp.mpf(ja) / 5
            b_p = mp.mpf(jb) / 5
            u_t90_sec: Dict[str, List[mp.mpc]] = {}
            for sec, (q_l, q_r) in vxm.SIX_CHARGES.items():
                ap = (q_l + q_r) * a_p
                bp = (q_l + q_r) * b_p
                am = (q_l - q_r) * a_p
                bm = (q_l - q_r) * b_p
                ph1 = mp.exp(-mp.j * mp.pi * (ap + am))
                r_1 = (-mp.j) * ph1 * th_char(ap + half, bp + half) * th_char(am + half, bm + half) / th1p0
                r_i = (-1) * th_char(ap + half, bp) * th_char(am + half, bm) / th1p0
                r_j = (-1) * ph1 * th_char(ap, bp + half) * th_char(am, bm + half) / th1p0
                r_k = (+mp.j) * th_char(ap, bp) * th_char(am, bm) / th1p0
                rs = [r_1, r_i, r_j, r_k]
                sh = [
                    ((ap, bp), (ap + half, bp + half)),
                    ((ap, bp - half), (ap + half, bp)),
                    ((ap - half, bp), (ap, bp + half)),
                    ((ap - half, bp - half), (ap, bp)),
                ]
                vt90 = [mp.mpc(0)] * 4
                for s_i in range(4):
                    if abs(rs[s_i]) > z_thr:
                        fu = f_kron(sh[s_i][0][0], sh[s_i][0][1])
                        a0v = a0_char(sh[s_i][1][0], sh[s_i][1][1])
                        n_old = 2 * mp.pi * tl2 + fu
                        corr = mp.pi * (abs(a0v) ** 2) * exp_m2l2
                        vt90[s_i] = mp.sqrt(n_old - corr) * rs[s_i]
                u_t90_sec[sec] = vt90

            def make_y(c_vec: List[mp.mpc], u_v: List[mp.mpc]) -> mp.matrix:
                ym = mp.zeros(3, 3)
                for al_i, s_i, ra, cb, tr2, ti2 in vxm.T_COUP_NZ:
                    ym[ra, cb] += c_vec[al_i] * u_v[s_i] * mp.mpc(tr2, ti2) * half
                return ym

            yu = make_y(c3_st, u_t90_sec["up"])
            yd = make_y(c3_s, u_t90_sec["down"])
            yl = make_y(c3_s, u_t90_sec["lepton"])
            uu, sv_u, _ = mp.svd_c(yu)
            ud, sv_d, _ = mp.svd_c(yd)
            _, sv_l, _ = mp.svd_c(yl)
            vals = [
                sv_u[1] / sv_u[0],
                sv_u[2] / sv_u[0],
                sv_u[2] / sv_u[1],
                sv_d[1] / sv_d[0],
                sv_d[2] / sv_d[0],
                sv_d[2] / sv_d[1],
                sv_l[1] / sv_l[0],
                sv_l[2] / sv_l[0],
                sv_l[2] / sv_l[1],
            ]
            for i_asc, j_asc in ((0, 1), (1, 2), (0, 2)):
                ii = 2 - i_asc
                jj = 2 - j_asc
                s_ov = mp.mpc(0)
                for k_r in range(3):
                    s_ov += mp.conj(uu[k_r, ii]) * ud[k_r, jj]
                vals.append(abs(s_ov))
            for idx in range(12):
                acc[idx] += vals[idx] / 12
        return acc


def compare_option(main_vals: List[float], main_errs: List[float], seat_vals: List[float], seat_errs: List[float]) -> Dict[str, Any]:
    rows = []
    zs = []
    for pos, m_v, e_m, s_v, e_s in zip(POSITIONS, main_vals, main_errs, seat_vals, seat_errs):
        rm = e_m / m_v
        rs = e_s / s_v
        dl = math.log(s_v) - math.log(m_v)
        tol = 3.0 * math.sqrt(rm * rm + rs * rs + DELTA_SYS * DELTA_SYS)
        z_quad = dl / math.sqrt(rm * rm + rs * rs) if (rm or rs) else float("inf")
        rows.append({
            "position": pos,
            "delta_ln": dl,
            "dln_over_tol": dl / tol,
            "abs_dln_over_tol": abs(dl / tol),
            "z_quadrature_only": z_quad,
            "rel_diff_pct": 100.0 * (s_v / m_v - 1.0),
        })
        zs.append(z_quad)
    worst = max(r["abs_dln_over_tol"] for r in rows)
    max_abs_dln = max(abs(r["delta_ln"]) for r in rows)
    rms_z = math.sqrt(sum(z * z for z in zs) / len(zs))
    return {
        "agrees": bool(all(r["abs_dln_over_tol"] <= 1.0 for r in rows)),
        "worst_abs_dln_over_tol": worst,
        "max_abs_delta_ln": max_abs_dln,
        "rms_z_quadrature_only": rms_z,
        "rows": rows,
    }


def main() -> None:
    t_start = time.time()
    print("POST-SEAL M28 CHECKS: starting")

    # 1. Load sealed seat output (04293e826) and B1940's BIG_RUN_VALUES_v2.json from origin/main
    seat_raw = subprocess.check_output(
        ["git", "-C", str(ROOT), "show", "04293e826:relays/x_measure_verify/verify_x_measure_out.json"]
    )
    seat_sha = hashlib.sha256(seat_raw).hexdigest()
    seat_json = json.loads(seat_raw.decode("utf-8"))

    b1940_path = "origin/main:frontier/B1940_the_area_options_corrected_in_extended_precision/verification/BIG_RUN_VALUES_v2.json"
    b1940_raw = subprocess.check_output(["git", "-C", str(ROOT), "show", b1940_path])
    b1940_sha = hashlib.sha256(b1940_raw).hexdigest()
    assert b1940_sha.startswith("9ece85e1"), "Unexpected BIG_RUN_VALUES_v2.json SHA-256"
    b1940_json = json.loads(b1940_raw.decode("utf-8"))

    combs = seat_json["area_measure_readout"]["four_primary_combinations"]

    comparisons: Dict[str, Any] = {}
    for opt_name, world_prefix in (("W-|b (area)", "W_minus"), ("W+|b (area)", "W_plus")):
        m_entry = b1940_json["options"][opt_name]
        m_vals = m_entry["values"]
        m_errs = m_entry["error"]
        for tag in ("exact_T90", "old_small_cut"):
            comb_key = f"{world_prefix}__{tag}"
            s_dict = combs[comb_key]["claimed_7_frame_code"]
            se_dict = combs[comb_key]["claimed_7_frame_code_quad_err"]
            s_vals = [s_dict[k] for k in POSITIONS]
            s_errs = [se_dict[k] for k in POSITIONS]
            comparisons[f"{opt_name}__vs__{comb_key}"] = compare_option(m_vals, m_errs, s_vals, s_errs)

    assert comparisons["W-|b (area)__vs__W_minus__exact_T90"]["agrees"]
    assert comparisons["W+|b (area)__vs__W_plus__exact_T90"]["agrees"]
    print("CHECK 1 (B1940 BIG_RUN_VALUES_v2 comparison): BOTH EXACT-WEIGHT WORLDS AGREE")

    # Check B1934 lepton == down identity in our sealed area readout
    b1934_area_rel_diffs: Dict[str, float] = {}
    for comb_key in ("W_minus__exact_T90", "W_plus__exact_T90"):
        a12 = combs[comb_key]["all_12_outputs"]
        b1934_area_rel_diffs[comb_key] = max(
            abs(a12[f"lepton__{r}"] / a12[f"down__{r}"] - 1.0)
            for r in ("2_over_3", "1_over_3", "1_over_2")
        )

    # 2. Verify F_bar(tau + 1) = F_bar(tau) across all heights used by verify_x_measure.py
    spine_ys = [18.0, 26.0, 36.0]
    spine_l2 = [vxm.uniformize_L2_raw_fast(complex(0.0, yv)) for yv in spine_ys]
    a_sp = np.array([[1.0, 1.0 / (yv * yv), 1.0 / (yv ** 4)] for yv in spine_ys], dtype=np.float64)
    cusp_poly = np.linalg.solve(a_sp, np.array(spine_l2, dtype=np.float64))

    def fast_l2_raw(xv: float, yv: float) -> float:
        xr = ((xv + 0.5) % 1.0) - 0.5
        if yv <= 36.0:
            return float(vxm.uniformize_L2_raw_fast(complex(abs(xr), yv)))
        inv2 = 1.0 / (yv * yv)
        return float(cusp_poly[0] + cusp_poly[1] * inv2 + cusp_poly[2] * inv2 * inv2)

    # 2a. Bulk float64 heights (y <= 5: the ONLY heights where verify_x_measure uses float64)
    bulk_heights = [0.95, 1.5, 3.0, 5.0]
    bulk_t_check: Dict[str, Any] = {}
    for y_h in bulk_heights:
        x_base = -0.31 if y_h > 1.0 else 0.13
        l2_0 = fast_l2_raw(x_base, y_h)
        tl2_0 = l2_0 + 0.5 * math.log(y_h) - vxm.NORM_CONST_SHIFT
        l2_u0 = vxm.uniformize_L2_raw_fast(complex(x_base, y_h))
        l2_u1 = vxm.uniformize_L2_raw_fast(complex(x_base + 1.0, y_h))
        l2_t_rel = abs(l2_u0 - l2_u1) / abs(l2_u0)

        p5_a = np.array([p[0] for p in vxm.P5_HALF_12], dtype=np.float64)
        p5_b = np.array([p[1] for p in vxm.P5_HALF_12], dtype=np.float64)
        tau_rep_0 = np.full(12, complex(x_base, y_h), dtype=np.complex128)
        tau_rep_1 = np.full(12, complex(x_base + 1.0, y_h), dtype=np.complex128)
        tl_rep = np.full(12, tl2_0, dtype=np.float64)
        out_0 = vxm.evaluate_four_modes_f64_batch(tau_rep_0, p5_a, p5_b, tl_rep)
        out_1 = vxm.evaluate_four_modes_f64_batch(tau_rep_1, p5_a, p5_b, tl_rep)
        max_rel = 0.0
        max_abs = 0.0
        for m_k in out_0:
            v0 = np.mean(out_0[m_k], axis=0)
            v1 = np.mean(out_1[m_k], axis=0)
            max_abs = max(max_abs, float(np.max(np.abs(v0 - v1))))
            max_rel = max(max_rel, float(np.max(np.abs(v0 - v1) / np.abs(v0))))
        assert max_abs < 1e-11
        assert max_rel < 1e-7
        bulk_t_check[str(y_h)] = {
            "x_tested": x_base,
            "max_abs_diff_across_48_outputs": max_abs,
            "max_rel_diff_across_48_outputs": max_rel,
            "unreduced_lame_L2_rel_diff": l2_t_rel,
        }
    print("CHECK 2A (bulk float64 T-invariance on y <= 5): PASSED")

    # 2b. Extended-precision mpmath heights (y > 5: y = 5, 6, 12, 20, 35, 45, 60, 80, 120)
    mp_heights = [5.0, 6.0, 12.0, 20.0, 35.0, 45.0, 60.0, 80.0, 120.0]
    mp_t_check: Dict[str, Any] = {}
    for y_h in mp_heights:
        x_base = 0.13 if int(y_h) % 2 == 0 else -0.27
        l2_val = fast_l2_raw(x_base, y_h)
        res_0 = vxm.eval_p5_avg_four_modes_mp(x_base, y_h, l2_val, dps=165)
        res_1 = vxm.eval_p5_avg_four_modes_mp(x_base + 1.0, y_h, l2_val, dps=165)
        max_rel_f64 = 0.0
        for m_k in res_0:
            v0 = res_0[m_k]
            v1 = res_1[m_k]
            nz = v0 > 0.0
            rel = float(np.max(np.abs(v0[nz] - v1[nz]) / np.abs(v0[nz])))
            assert np.array_equal(v0 == 0.0, v1 == 0.0)
            max_rel_f64 = max(max_rel_f64, rel)
        assert max_rel_f64 < 1e-14

        # Pure mpf relative difference at dynamic dps_eff (no IEEE-754 float64 rounding)
        dps_eff = max(165, int(math.ceil(2.15 * y_h)) + 55)
        with mp.workdps(dps_eff):
            mp_0 = eval_p5_avg_t90_mp_fixed_dps(x_base, y_h, l2_val, dps_eff)
            mp_1 = eval_p5_avg_t90_mp_fixed_dps(x_base + 1.0, y_h, l2_val, dps_eff)
            max_rel_mp = float(max(abs(p - q) / abs(p) for p, q in zip(mp_0, mp_1)))
            up13_log10 = float(mp.log10(mp_0[1]))
        assert max_rel_mp < 1e-35
        mp_t_check[str(int(y_h))] = {
            "x_tested": x_base,
            "dps_eff": dps_eff,
            "up_1_over_3_log10_magnitude": up13_log10,
            "max_rel_diff_float64_cast_48_outputs": max_rel_f64,
            "max_rel_diff_pure_mpmath_12_outputs": max_rel_mp,
        }
    print("CHECK 2B (mpmath dynamic-dps T-invariance on y in [5..120]): PASSED")

    # 2c. Deep-cusp y = 240 (highest Zone-4 node u = 1/240, dps=200 in verify_x_measure -> dps_eff=571)
    y_deep = 240.0
    x_deep = 0.17
    l2_deep = fast_l2_raw(x_deep, y_deep)
    res_d0 = vxm.eval_p5_avg_four_modes_mp(x_deep, y_deep, l2_deep, dps=200)
    res_d1 = vxm.eval_p5_avg_four_modes_mp(x_deep + 1.0, y_deep, l2_deep, dps=200)
    max_rel_deep_f64_active = 0.0
    for m_k in res_d0:
        v0 = res_d0[m_k]
        v1 = res_d1[m_k]
        assert np.array_equal(v0 == 0.0, v1 == 0.0)
        nz = v0 > 0.0
        max_rel_deep_f64_active = max(max_rel_deep_f64_active, float(np.max(np.abs(v0[nz] - v1[nz]) / np.abs(v0[nz]))))
    assert max_rel_deep_f64_active < 1e-14

    dps_deep = max(200, int(math.ceil(2.15 * y_deep)) + 55)
    with mp.workdps(dps_deep):
        mp_d0 = eval_p5_avg_t90_mp_fixed_dps(x_deep, y_deep, l2_deep, dps_deep)
        mp_d1 = eval_p5_avg_t90_mp_fixed_dps(x_deep + 1.0, y_deep, l2_deep, dps_deep)
        max_rel_deep_all12 = float(max(abs(p - q) / abs(p) for p, q in zip(mp_d0, mp_d1)))
        max_rel_deep_mixing_and_up12 = float(max(abs(mp_d0[i] - mp_d1[i]) / abs(mp_d0[i]) for i in (2, 9, 10, 11)))
        up13_deep_log10 = float(mp.log10(mp_d0[1]))
    assert max_rel_deep_all12 < 1e-15
    assert max_rel_deep_mixing_and_up12 < 1e-50
    mp_t_check["240"] = {
        "x_tested": x_deep,
        "dps_eff": dps_deep,
        "up_1_over_3_log10_magnitude": up13_deep_log10,
        "max_rel_diff_float64_active_outputs": max_rel_deep_f64_active,
        "max_rel_diff_pure_mpmath_all_12_outputs": max_rel_deep_all12,
        "max_rel_diff_pure_mpmath_mixing_and_up12": max_rel_deep_mixing_and_up12,
    }
    print("CHECK 2C (deep-cusp y=240 pure-mpmath T-invariance): PASSED")

    # 2d. Planted 15-digit control at y = 20 (must fail T-check, proving entry-level sensitivity)
    y_plant = 20.0
    x_plant = 0.13
    l2_plant = fast_l2_raw(x_plant, y_plant)
    with mp.workdps(15):
        pl_0 = eval_p5_avg_t90_mp_fixed_dps(x_plant, y_plant, l2_plant, 15)
        pl_1 = eval_p5_avg_t90_mp_fixed_dps(x_plant + 1.0, y_plant, l2_plant, 15)
        planted_15dps_y20_rel_err = float(max(abs(p - q) / abs(p) for p, q in zip(pl_0, pl_1)))
    assert planted_15dps_y20_rel_err > 1e-3
    print("CHECK 2D (planted 15-dps entry precision loss at y=20 caught by T-check): PASSED")

    out_payload = {
        "purpose": "Post-seal M28 checks on sealed 04293e826 verify_x_measure_out.json",
        "empirical_firewall": "0 of 19",
        "sealed_x_measure_commit": "04293e826",
        "sealed_x_measure_json_sha256": seat_sha,
        "b1940_big_run_values_v2_sha256": b1940_sha,
        "tolerance_rule": "B1937 / B1940 compare_area_second.py: |d ln| <= 3 * sqrt(e_main^2 + e_seat^2 + delta^2), delta = 5.4e-3",
        "b1940_area_comparisons": comparisons,
        "b1934_lepton_equals_down_area_max_rel_diff": b1934_area_rel_diffs,
        "t_invariance_checks": {
            "bulk_float64_y_le_5": bulk_t_check,
            "mpmath_dynamic_dps_y_ge_5": mp_t_check,
            "planted_15dps_at_y20_t_check_max_rel_err": planted_15dps_y20_rel_err,
            "planted_15dps_caught": bool(planted_15dps_y20_rel_err > 1e-3),
        },
        "elapsed_seconds": round(time.time() - t_start, 3),
    }

    out_path = HERE / "post_seal_m28_checks.json"
    out_path.write_text(json.dumps(out_payload, indent=2) + "\n", encoding="utf-8")
    out_sha = hashlib.sha256(out_path.read_bytes()).hexdigest()
    (HERE / "POST_SEAL_M28_SHA256.txt").write_text(
        f"{out_sha}  post_seal_m28_checks.json\n", encoding="utf-8"
    )
    print("POST-SEAL M28 CHECKS: ALL PASSED, JSON WRITTEN")


if __name__ == "__main__":
    main()
