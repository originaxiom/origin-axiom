#!/usr/bin/env python3
"""Standalone Review 83 algebraic and numerical counterchecks (seat agy-002, card A2-R83 / M38).

Independently recomputes on standalone agy-002 code (zero main code imported, zero measured data):
  1. B1940 & M36/M37: F_bar(tau + 1) = F_bar(tau) across heights y in [1.5, 200] in extended-precision
     mpmath (both pure-mpmath and verify_a2_canon.eval_mp_12pt_avg), vs double-precision float64 breakdown
     above height 11, plus a planted 15-digit mpmath control at y = 20. Also verifies max |Delta ln|
     between B1940 BIG_RUN_VALUES_v2.json and B1932 BIG_RUN_VALUES.json (0.068 vs FINDINGS.md's 0.086).
  2. B1942 & M33 (SM-C13): Exact combinatorics of (Z/15Z)^2 (192 exact-order-15 points -> 24 order-5
     points with multiplicity 8, NOT 6!), order-5 lepton-down copy (< 1e-15), and order-15 lepton vs
     quark shifts at tau in {0.13+1.5i, -0.31+2.4i, 0.27+3.6i} plus planted lepton-charge control (-2, 6).
  3. B1943: Exact integer Smith normal forms of A - I and A + I for LR, RL, (LR)^T, (LR)^{-1}, ((LR)^T)^{-1}
     (Smith(LR + I) = (1, 5), NOT (1, 3)!), exhaustive enumeration of fixed-up-to-sign torsion points
     for exact orders N = 2..60, and trace-4 LRR control.
  4. B1934, B1935, B1936: Level-5 Weil representation in SO(3) x SU(2), Legendre quadratic character hand
     on all 32 elements +-J^n K^e, S_3 channel permutations under T and S, weave triplet T-eigenphases,
     exact sector coincidences for N = 2..60, and Lambda*(C^5) exterior-degree parity selection of W_-.
  5. B1938: Kronecker Szego residue R_s = kappa_s Z(c_s) Z(d_s)/(2*pi*eta), sum_s R_s^2 = 0, up's R_1 = 0
     at order 5, and Kronecker second limit formula |theta[c](0)/eta|^2 = exp(-zeta'_chi(0)) via independent
     incomplete-gamma lattice theta Mellin sum.
  6. B1941: Pointwise fermion determinant ln det H_hat vs one-loop trace -Tr H_hat^2 across 28 points on X(1).

0 of 19.
"""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Tuple

import mpmath as mp
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "relays" / "a2_canon"))
import verify_a2_canon as a2c  # our own standalone blind module


# =============================================================================
# ARBITRARY-DENOMINATOR MPMATH SINGLE-POINT & AVERAGED FRAME EVALUATOR
# =============================================================================

def eval_mp_arbitrary_points(
    tau: complex,
    l2_val: float,
    pts: List[Tuple[Fraction, Fraction]],
    dps_override: int | None = None,
    sect_override: List[Tuple[str, int, int]] | None = None,
) -> Dict[str, List[mp.mpf]]:
    """Evaluate averaged 24-component frame observables over an arbitrary rational torsion point list
    pts = [(a, b), ...] in (Q/Z)^2 in pure arbitrary-precision mpmath (no float64 rounding)."""
    y_f = tau.imag
    dps = dps_override if dps_override is not None else max(55, int(3.2 * y_f) + 45)
    sects = sect_override if sect_override is not None else list(a2c.SECT)
    with mp.workdps(dps):
        t = mp.mpc(mp.mpf(repr(tau.real)), mp.mpf(repr(tau.imag)))
        x_r, y_r = mp.re(t), mp.im(t)
        l2 = mp.mpf(repr(l2_val))
        pi = mp.pi
        eg = mp.euler
        q = mp.exp(2j * pi * t)
        m_max = max(8, int(math.ceil(dps * math.log(10) / (2.0 * math.pi * max(y_f, 0.8)) + 4)))
        eta_prod = mp.mpf(1)
        e2 = mp.mpf(1)
        qp = mp.mpc(1)
        for m in range(1, m_max + 3):
            qp *= q
            eta_prod *= 1 - qp
            e2 -= 24 * m * qp / (1 - qp)
        denom_hat = 2 * pi * ((mp.exp(1j * pi * x_r / 12) * eta_prod) ** 3)
        n_th = max(7, int(math.ceil(math.sqrt(dps * math.log(10) / (math.pi * max(y_f, 0.8))) + 4)))

        def th0_dt_mp(ca: Fraction, cb: Fraction):
            ca_m = mp.mpf(ca.numerator) / mp.mpf(ca.denominator)
            cb_m = mp.mpf(cb.numerator) / mp.mpf(cb.denominator)
            s0 = mp.mpc(0)
            s1 = mp.mpc(0)
            for k in range(-n_th, n_th + 1):
                na = mp.mpf(k) + ca_m
                tm = mp.exp(1j * pi * na * na * t + 2j * pi * na * cb_m)
                s0 += tm
                s1 += mp.mpf("0.5") * na * na * tm
            return s0, s1

        t2, dt2 = th0_dt_mp(Fraction(1, 2), Fraction(0, 1))
        t4, dt4 = th0_dt_mp(Fraction(0, 1), Fraction(1, 2))
        t3, dt3 = th0_dt_mp(Fraction(0, 1), Fraction(0, 1))
        R_h = [-(t2 * t2) / denom_hat, -(t4 * t4) / denom_hat, 1j * (t3 * t3) / denom_hat]
        dN_h = [-2 * t2 * dt2 / denom_hat, -2 * t4 * dt4 / denom_hat, 2j * t3 * dt3 / denom_hat]
        c3_S = [dN_h[q_i] - (e2 / 12) * R_h[q_i] for q_i in range(3)]
        c3_St = [mp.conj(v) for v in c3_S]

        th_cache = {}
        fa_cache = {}

        def thc01_frac(af: Fraction, bf: Fraction):
            key = (af, bf)
            if key in th_cache:
                return th_cache[key]
            aa = mp.mpf(af.numerator) / mp.mpf(af.denominator)
            bb = mp.mpf(bf.numerator) / mp.mpf(bf.denominator)
            k0 = round(-float(aa))
            k1 = round(-float(aa) - 0.5)
            X0 = mp.mpc(0)
            X1 = mp.mpc(0)
            for k in range(-n_th, n_th + 1):
                n0 = mp.mpf(k + k0) + aa
                X0 += mp.exp(2j * pi * t * n0 * n0 + 2j * pi * n0 * bb)
                n1 = mp.mpf(k + k1) + aa
                X1 += mp.exp(2j * pi * t * ((n1 + mp.mpf("0.5")) ** 2) + 2j * pi * n1 * bb)
            th_cache[key] = (X0, X1)
            return X0, X1

        def Fu_a0sq_frac(u1: Fraction, u2: Fraction):
            u1_r = u1 - Fraction(math.floor(u1))
            u2_r = u2 - Fraction(math.floor(u2))
            key = (u1_r, u2_r)
            if key in fa_cache:
                return fa_cache[key]
            if u1_r == 0 and u2_r == 0:
                fa_cache[key] = (None, mp.mpf(0))
                return fa_cache[key]
            a_m = mp.mpf(u1_r.numerator) / mp.mpf(u1_r.denominator)
            b_m = mp.mpf(u2_r.numerator) / mp.mpf(u2_r.denominator)
            if u1_r == 0:
                fu = pi * (2 * eg - 2 * mp.log(2) - mp.log(y_r)) + (pi ** 2) * y_r / (mp.sin(pi * b_m) ** 2)
                for m in range(1, m_max + 2):
                    for ms in (mp.mpf(m), mp.mpf(-m)):
                        wm = mp.exp(2j * pi * (ms * x_r + b_m) - 2 * pi * abs(ms) * y_r)
                        fu += (2 * pi / abs(ms)) * mp.re(wm / (1 - wm))
            else:
                fu = -pi * (mp.digamma(a_m) + mp.digamma(1 - a_m) + 2 * mp.log(2) + mp.log(y_r))
                for k in range(-m_max - 1, m_max + 2):
                    ms = mp.mpf(k) + a_m
                    wm = mp.exp(2j * pi * (ms * x_r + b_m) - 2 * pi * abs(ms) * y_r)
                    fu += (2 * pi / abs(ms)) * mp.re(wm / (1 - wm))
            nu_r = (u1_r + Fraction(1, 2)) - Fraction(math.floor(u1_r + Fraction(1, 2))) - Fraction(1, 2)
            if nu_r == Fraction(-1, 2):
                nu_r = Fraction(1, 2)
            nu = mp.mpf(nu_r.numerator) / mp.mpf(nu_r.denominator)
            bm_r = (-u2_r) - Fraction(math.floor(-u2_r))
            Bm = mp.mpf(bm_r.numerator) / mp.mpf(bm_r.denominator)
            w_z = nu * t - Bm
            ser = mp.mpc(0)
            for m in range(1, m_max + 2):
                qm = q ** m
                ser += (mp.exp(2j * pi * m * (t + w_z)) - mp.exp(2j * pi * m * (t - w_z))) / (2j * (1 - qm))
            a0 = pi * mp.cot(pi * w_z) + 4 * pi * ser + 2j * pi * nu
            fa_cache[key] = (fu, abs(a0) ** 2)
            return fa_cache[key]

        shift_old = 2 * pi * (l2 + mp.mpf("0.5") * mp.log(y_r) - eg - mp.log(pi))
        em2l2 = mp.exp(-2 * l2)
        char_shifts_frac = [
            (Fraction(0, 1), Fraction(0, 1)),
            (Fraction(0, 1), Fraction(1, 2)),
            (Fraction(1, 2), Fraction(0, 1)),
            (Fraction(1, 2), Fraction(1, 2)),
        ]
        acc = {"exact_T90": [mp.mpf(0) for _ in range(24)], "old_weight": [mp.mpf(0) for _ in range(24)]}
        n_pts = mp.mpf(len(pts))

        for la, lb in pts:
            sec_R = {}
            for sname, ql, qr in sects:
                ax, bx = ql * la, 2 * ql * lb
                ay, by = qr * la, 2 * qr * lb
                X0, X1 = thc01_frac(ax, bx)
                Y0, Y1 = thc01_frac(ay, by)
                bx_m = mp.mpf((bx - 2 * Fraction(math.floor(bx / 2))).numerator) / mp.mpf(bx.denominator)
                by_m = mp.mpf((by - 2 * Fraction(math.floor(by / 2))).numerator) / mp.mpf(by.denominator)
                eb_x = mp.exp(1j * pi * bx_m)
                eb_y = mp.exp(1j * pi * by_m)
                Mm = [
                    [X0 * Y0 / denom_hat, eb_y * X0 * Y1 / (1j * denom_hat)],
                    [eb_x * X1 * Y0 / (1j * denom_hat), -(eb_x * eb_y) * X1 * Y1 / denom_hat],
                ]
                R_ch = [
                    sum(mp.mpc(a2c.EC_LIST[si][r, c].real, a2c.EC_LIST[si][r, c].imag) * Mm[r][c] for r in range(2) for c in range(2))
                    for si in range(4)
                ]
                sec_R[sname] = (R_ch, ax + ay, Fraction(1, 2) * (bx + by))

            for mname in ("exact_T90", "old_weight"):
                obs = [mp.mpf(0) for _ in range(24)]
                U_st = {}
                col = 0
                for sname, _, _ in sects:
                    R_ch, ap, bp = sec_R[sname]
                    u_ch = []
                    for si, (ds1, ds2) in enumerate(char_shifts_frac):
                        fu, a0sq = Fu_a0sq_frac(ap + ds1, bp + ds2)
                        if fu is None:
                            u_ch.append(mp.mpc(0))
                        else:
                            nv = shift_old + fu - (pi * a0sq * em2l2 if mname == "exact_T90" else mp.mpf(0))
                            u_ch.append(mp.sqrt(nv) * R_ch[si] if nv > 0 else mp.mpc(0))
                    for rn, c3v, Cmat in [("S", c3_S, a2c.COUP_S), ("St", c3_St, a2c.COUP_ST)]:
                        Ym = mp.matrix(3, 3)
                        for a_i in range(3):
                            for b_i in range(3):
                                s_val = mp.mpc(0)
                                for qi in range(3):
                                    for si in range(4):
                                        cc = Cmat[qi, si, a_i, b_i]
                                        if cc != 0:
                                            s_val += c3v[qi] * u_ch[si] * mp.mpc(cc.real, cc.imag)
                                Ym[a_i, b_i] = s_val
                        if sname in ("up", "down"):
                            U_m, S_v, _ = mp.svd_c(Ym)
                            sv0, sv1, sv2 = S_v[0], S_v[1], S_v[2]
                            U_asc = mp.matrix(3, 3)
                            for r in range(3):
                                U_asc[r, 0] = U_m[r, 2]
                                U_asc[r, 1] = U_m[r, 1]
                                U_asc[r, 2] = U_m[r, 0]
                            U_st[(sname, rn)] = U_asc
                        else:
                            S_v = mp.svd_c(Ym, compute_uv=False)
                            sv0, sv1, sv2 = S_v[0], S_v[1], S_v[2]
                        obs[col] = (sv1 / sv0) if sv0 > 0 else mp.mpf(0)
                        obs[col + 1] = (sv2 / sv0) if sv0 > 0 else mp.mpf(0)
                        col += 2
                for ru in ("S", "St"):
                    for rd in ("S", "St"):
                        Uu = U_st[("up", ru)]
                        Ud = U_st[("down", rd)]
                        V = Uu.H * Ud
                        obs[col] = abs(V[0, 1])
                        obs[col + 1] = abs(V[1, 2])
                        obs[col + 2] = abs(V[0, 2])
                        col += 3
                for idx in range(24):
                    acc[mname][idx] += obs[idx] / n_pts
        return acc


# =============================================================================
# CHECK 1: B1940 & M36/M37 — F_bar(tau + 1) = F_bar(tau) ACROSS HEIGHTS
# =============================================================================

def reduce_to_fd_point(tau: complex) -> complex:
    z = complex(tau)
    for _ in range(200):
        n = round(z.real)
        if n != 0:
            z = z - n
        if (z.real * z.real + z.imag * z.imag) < 1.0 - 1e-13:
            z = -1.0 / z
        else:
            break
    return z


def run_check1_b1940(l2_interp: a2c.CanonicalL2Interpolant) -> Dict:
    pts_5_12 = [(Fraction(round(a * 5), 5), Fraction(round(b * 5), 5)) for a, b in a2c.ORDER5_12_REPS]
    x0 = 0.13729184
    heights_mp = [1.5, 3.0, 5.0, 6.0, 9.0, 11.0, 12.0, 15.0, 20.0, 30.0, 45.0, 100.0, 200.0]
    mp_shift_errs = {}
    a2c_mp_shift_errs = {}
    for y in heights_mp:
        tau0 = complex(x0, y)
        tau1 = complex(x0 + 1.0, y)
        l2_v = float(l2_interp.eval_fd(np.array([reduce_to_fd_point(tau0)]))[0])
        # Pure mpmath check:
        f0 = eval_mp_arbitrary_points(tau0, l2_v, pts_5_12)["exact_T90"]
        f1 = eval_mp_arbitrary_points(tau1, l2_v, pts_5_12)["exact_T90"]
        with mp.workdps(60):
            err_pure = float(max(abs(f1[i] - f0[i]) for i in range(24)))
        mp_shift_errs[str(y)] = err_pure
        # verify_a2_canon.eval_mp_12pt_avg check:
        g0 = a2c.eval_mp_12pt_avg(tau0, l2_v)["exact_T90"]
        g1 = a2c.eval_mp_12pt_avg(tau1, l2_v)["exact_T90"]
        a2c_mp_shift_errs[str(y)] = float(np.max(np.abs(g1 - g0)))

    # Planted 15-digit mpmath run at y = 20 (B1940 V3):
    l2_20 = float(l2_interp.eval_fd(np.array([reduce_to_fd_point(complex(x0, 20.0))]))[0])
    p0 = eval_mp_arbitrary_points(complex(x0, 20.0), l2_20, pts_5_12, dps_override=15)["exact_T90"]
    p1 = eval_mp_arbitrary_points(complex(x0 + 1.0, 20.0), l2_20, pts_5_12, dps_override=15)["exact_T90"]
    plant_15dps_y20_err = float(max(abs(p1[i] - p0[i]) for i in range(24)))

    # Double-precision float64 shift failure across heights:
    heights_f64 = [1.5, 3.0, 6.0, 9.0, 11.0, 12.0, 15.0, 20.0, 30.0]
    f64_shift_errs = {}
    for y in heights_f64:
        t_arr = np.array([complex(x0, y), complex(x0 + 1.0, y)], dtype=np.complex128)
        l2_v = float(l2_interp.eval_fd(np.array([reduce_to_fd_point(complex(x0, y))]))[0])
        l2_arr = np.array([l2_v, l2_v], dtype=np.float64)
        f64_out, _ = a2c.eval_frame_12pt_avg_fd(t_arr, l2_arr, mode_list=("exact_T90",))
        v = f64_out["exact_T90"]
        f64_shift_errs[str(y)] = float(np.max(np.abs(v[1] - v[0])))

    # Check B1940 BIG_RUN_VALUES_v2.json vs B1932 BIG_RUN_VALUES.json at b35eac607 (diffs only, zero raw values):
    raw_v2 = subprocess.check_output([
        "git", "-C", str(REPO_ROOT), "show",
        "b35eac607:frontier/B1940_the_area_options_corrected_in_extended_precision/verification/BIG_RUN_VALUES_v2.json",
    ])
    raw_v1 = subprocess.check_output([
        "git", "-C", str(REPO_ROOT), "show",
        "b35eac607:frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/BIG_RUN_VALUES.json",
    ])
    v2 = json.loads(raw_v2)
    v1 = json.loads(raw_v1)
    dln_v2_vs_v1 = {}
    max_abs_dln = 0.0
    for opt in v2["options"]:
        diffs = [math.log(v2["options"][opt]["values"][i]) - math.log(v1["options"][opt]["values"][i]) for i in range(7)]
        dln_v2_vs_v1[opt] = [round(d, 6) for d in diffs]
        max_abs_dln = max(max_abs_dln, max(abs(d) for d in diffs))

    return {
        "pure_mpmath_tau_plus_1_max_err": mp_shift_errs,
        "a2c_eval_mp_tau_plus_1_max_err": a2c_mp_shift_errs,
        "plant_15dps_y20_tau_plus_1_err": plant_15dps_y20_err,
        "float64_tau_plus_1_max_err": f64_shift_errs,
        "b1940_v2_sha256": hashlib.sha256(raw_v2).hexdigest(),
        "b1940_v2_minus_b1932_v1_dln": dln_v2_vs_v1,
        "b1940_max_abs_dln_actual": round(max_abs_dln, 6),
    }


# =============================================================================
# CHECK 2: B1942 & M33 (SM-C13) — ORDER-5 COPY AND ORDER-15 FORK + MULTIPLICITY
# =============================================================================

def exact_order_points(N: int) -> List[Tuple[Fraction, Fraction]]:
    pts = []
    for i in range(N):
        for j in range(N):
            if math.gcd(math.gcd(i, j), N) == 1:
                pts.append((Fraction(i, N), Fraction(j, N)))
    return pts


def run_check2_b1942_and_smc13(l2_interp: a2c.CanonicalL2Interpolant) -> Dict:
    pts5 = exact_order_points(5)
    pts15 = exact_order_points(15)
    assert len(pts5) == 24
    assert len(pts15) == 192

    # Check multiplicity of w -> 6*w mod 1 from exact order 15 onto exact order 5:
    hit_counts: Dict[Tuple[Fraction, Fraction], int] = {p: 0 for p in pts5}
    for a, b in pts15:
        img = ((6 * a) - math.floor(6 * a), (6 * b) - math.floor(6 * b))
        hit_counts[img] += 1
    mult_min = min(hit_counts.values())
    mult_max = max(hit_counts.values())

    # Use projective halves (c and -c give identical outputs):
    seen5 = set()
    pts5_half = []
    for a, b in pts5:
        neg = ((-a) - math.floor(-a), (-b) - math.floor(-b))
        if (a, b) not in seen5 and neg not in seen5:
            seen5.add((a, b))
            seen5.add(neg)
            pts5_half.append((a, b))
    assert len(pts5_half) == 12
    # Build 96 projective reps of pts15:
    seen15 = set()
    pts15_half = []
    for a, b in pts15:
        neg = ((-a) - math.floor(-a), (-b) - math.floor(-b))
        if (a, b) not in seen15 and neg not in seen15:
            seen15.add((a, b))
            seen15.add(neg)
            pts15_half.append((a, b))
    assert len(pts15_half) == 96

    moduli = [complex(0.13, 1.5), complex(-0.31, 2.4), complex(0.27, 3.6)]
    table_rows = {}
    for tau in moduli:
        l2_v = float(l2_interp.eval_fd(np.array([reduce_to_fd_point(tau)]))[0])
        o5 = [float(x) for x in eval_mp_arbitrary_points(tau, l2_v, pts5_half, dps_override=45)["exact_T90"]]
        o15 = [float(x) for x in eval_mp_arbitrary_points(tau, l2_v, pts15_half, dps_override=45)["exact_T90"]]

        # Indices in OBS24:
        # up S: 0,1; up St: 2,3; down S: 4,5; down St: 6,7; lep S: 8,9; lep St: 10,11
        def rel_diff(v_a, v_b):
            return max(abs(a - b) / abs(b) for a, b in zip(v_a, v_b))

        # Also add r12 = r13 / r23 as B1942 may include all 3 ratios (m2/m3, m1/m3, m1/m2):
        def three_ratios(vec, idx0):
            r23, r13 = vec[idx0], vec[idx0 + 1]
            return [r23, r13, r13 / r23]

        lep5_vs_down5_S = rel_diff(three_ratios(o5, 8), three_ratios(o5, 4))
        lep5_vs_down5_St = rel_diff(three_ratios(o5, 10), three_ratios(o5, 6))
        lep15_vs_down5_S = rel_diff(three_ratios(o15, 8), three_ratios(o5, 4))
        lep15_vs_down5_St = rel_diff(three_ratios(o15, 10), three_ratios(o5, 6))
        down15_vs_down5_S = rel_diff(three_ratios(o15, 4), three_ratios(o5, 4))
        down15_vs_down5_St = rel_diff(three_ratios(o15, 6), three_ratios(o5, 6))
        up15_vs_up5_S = rel_diff(three_ratios(o15, 0), three_ratios(o5, 0))
        up15_vs_up5_St = rel_diff(three_ratios(o15, 2), three_ratios(o5, 2))
        lep15_vs_down15_S = rel_diff(three_ratios(o15, 8), three_ratios(o15, 4))
        lep15_vs_down15_St = rel_diff(three_ratios(o15, 10), three_ratios(o15, 6))

        table_rows[f"{tau.real:+.2f}+{tau.imag:.1f}i"] = {
            "lep5_vs_down5_S_St": [lep5_vs_down5_S, lep5_vs_down5_St],
            "lep15_vs_down5_S_St": [lep15_vs_down5_S, lep15_vs_down5_St],
            "down15_vs_down5_S_St": [down15_vs_down5_S, down15_vs_down5_St],
            "up15_vs_up5_S_St": [up15_vs_up5_S, up15_vs_up5_St],
            "lep15_vs_down15_S_St": [lep15_vs_down15_S, lep15_vs_down15_St],
        }

    # Planted control at tau = 0.13 + 1.5i: lepton charges (-2, 6) instead of (-3, 6)
    tau_ctl = complex(0.13, 1.5)
    l2_ctl = float(l2_interp.eval_fd(np.array([reduce_to_fd_point(tau_ctl)]))[0])
    sect_bad = [("up", 1, -4), ("down", 2, 1), ("lep", -2, 6)]
    o5_ref = [float(x) for x in eval_mp_arbitrary_points(tau_ctl, l2_ctl, pts5_half, dps_override=40)["exact_T90"]]
    o15_bad = [float(x) for x in eval_mp_arbitrary_points(tau_ctl, l2_ctl, pts15_half, dps_override=40, sect_override=sect_bad)["exact_T90"]]
    ctl_break_S = max(abs(o15_bad[8 + k] - o5_ref[4 + k]) / abs(o5_ref[4 + k]) for k in range(2))

    return {
        "n_exact_order_5": len(pts5),
        "n_exact_order_15": len(pts15),
        "map_6w_hit_multiplicity_min_max": [mult_min, mult_max],
        "b1942_findings_claimed_multiplicity": 6,
        "multiplicity_discrepancy_confirmed": (mult_min == 8 and mult_max == 8),
        "moduli_table": table_rows,
        "planted_lepton_charge_m2_6_break": ctl_break_S,
    }


# =============================================================================
# CHECK 3: B1943 — SMITH NORMAL FORMS AND FIXED TORSION LINES UP TO N = 60
# =============================================================================

def smith_2x2_int(M: np.ndarray) -> Tuple[int, int]:
    a, b, c, d = int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1])
    det = abs(a * d - b * c)
    g = math.gcd(math.gcd(abs(a), abs(b)), math.gcd(abs(c), abs(d)))
    if g == 0:
        return (0, 0)
    return (g, det // g)


def fixed_up_to_sign_orders(A: np.ndarray, max_N: int = 60) -> Dict[int, List[Tuple[int, int, str]]]:
    found: Dict[int, List[Tuple[int, int, str]]] = {}
    for N in range(2, max_N + 1):
        hits = []
        for i in range(N):
            for j in range(N):
                if math.gcd(math.gcd(i, j), N) != 1:
                    continue
                vi = (int(A[0, 0]) * i + int(A[0, 1]) * j) % N
                vj = (int(A[1, 0]) * i + int(A[1, 1]) * j) % N
                if (vi, vj) == (i, j):
                    hits.append((i, j, "+"))
                elif (vi, vj) == ((-i) % N, (-j) % N):
                    hits.append((i, j, "-"))
        if hits:
            found[N] = hits
    return found


def run_check3_b1943() -> Dict:
    # Check both conventions of L, R (record's L=[[1,1],[0,1]], R=[[1,0],[1,1]] and J*L*R / L*R):
    # Wait: in B1943, LR fixes {(1/5, 2/5), ...} up to sign sending each to its negative!
    # Check [[1,1],[0,1]] @ [[1,0],[1,1]] = [[2,1],[1,1]] (det +1, trace +3 -> det(A-I)=1, det(A+I)=5? Wait:
    # det([[3,1],[1,2]]) = 6 - 1 = 5! Let us check [[2,1],[1,1]] on (1, 2) mod 5:
    # [[2,1],[1,1]] @ [1,2] = [4, 3] == [-1, -2] mod 5! BINGO!)
    L = np.array([[1, 1], [0, 1]], dtype=int)
    R = np.array([[1, 0], [1, 1]], dtype=int)
    LR = L @ R
    RL = R @ L
    LRT = LR.T
    LR_inv = np.array([[1, -1], [-1, 2]], dtype=int)
    LRT_inv = LR_inv.T
    I2 = np.eye(2, dtype=int)

    acts = {
        "LR": LR,
        "RL": RL,
        "LR_T": LRT,
        "LR_inv": LR_inv,
        "LR_T_inv": LRT_inv,
    }
    smith_res = {}
    enum_res = {}
    for name, A in acts.items():
        smith_res[name] = {
            "Smith_A_minus_I": list(smith_2x2_int(A - I2)),
            "Smith_A_plus_I": list(smith_2x2_int(A + I2)),
        }
        fnd = fixed_up_to_sign_orders(A, 60)
        enum_res[name] = {str(k): len(v) for k, v in fnd.items()}

    LRR = L @ R @ R
    lrr_fnd = fixed_up_to_sign_orders(LRR, 60)
    return {
        "LR_matrix": LR.tolist(),
        "LR_fixed_points_N5": fixed_up_to_sign_orders(LR, 60).get(5, []),
        "smith_forms": smith_res,
        "b1943_findings_claimed_Smith_LR_plus_I": [1, 3],
        "actual_Smith_LR_plus_I": list(smith_2x2_int(LR + I2)),
        "fixed_orders_up_to_60_counts": enum_res,
        "control_LRR": {
            "Smith_LRR_minus_I": list(smith_2x2_int(LRR - I2)),
            "Smith_LRR_plus_I": list(smith_2x2_int(LRR + I2)),
            "fixed_orders": sorted(lrr_fnd.keys()),
        },
    }


# =============================================================================
# CHECK 4: B1934, B1935, B1936 — WEIL REP, LEGENDRE HAND, S3, DEGREES
# =============================================================================

def run_check4_b1934_b1935_b1936() -> Dict:
    # 1. Level-5 Weil representation for k = 1, 2:
    weil_res = {}
    for k in (1, 2):
        T = np.diag([np.exp(2j * math.pi * (k * x * x % 5) / 5.0) for x in range(5)])
        F = np.array([[np.exp(-2j * math.pi * (k * x * y % 5) / 5.0) / math.sqrt(5.0) for y in range(5)] for x in range(5)])
        # Find phase alpha in 8th/12th roots so <S, T> has order 120 and det = 1 on blocks:
        # Gauss sum for sum_{x=0}^4 e(k x^2 / 5) = +sqrt(5) for k=1, -sqrt(5) for k=2:
        gs = sum(np.exp(2j * math.pi * (k * x * x % 5) / 5.0) for x in range(5))
        # Standard Weil phase: S = (gs / abs(gs))^{-1} * F^* or check phases e^{i*pi*m/12}:
        best_order = None
        S_mat = None
        for m in range(24):
            ph = np.exp(1j * math.pi * m / 12.0)
            Sc = ph * F
            # Generate group <Sc, T> by BFS up to 200:
            grp = [np.eye(5, dtype=np.complex128)]
            for _ in range(12):
                new_els = []
                for g in grp:
                    for gen in (Sc, T):
                        cand = g @ gen
                        if not any(np.max(np.abs(cand - h)) < 1e-9 for h in grp + new_els):
                            new_els.append(cand)
                            if len(grp) + len(new_els) > 250:
                                break
                    if len(grp) + len(new_els) > 250:
                        break
                if not new_els or len(grp) + len(new_els) > 250:
                    grp.extend(new_els)
                    break
                grp.extend(new_els)
            if len(grp) == 120:
                best_order = 120
                S_mat = Sc
                break
        assert best_order == 120
        # Even / odd basis on C^5 (x in {0, 1, 2, 3, 4}, -x mod 5):
        # Even: e0, (e1+e4)/sqrt2, (e2+e3)/sqrt2; Odd: (e1-e4)/sqrt2, (e2-e3)/sqrt2
        B = np.zeros((5, 5), dtype=np.complex128)
        B[0, 0] = 1.0
        B[1, 1] = B[4, 1] = 1.0 / math.sqrt(2.0)
        B[2, 2] = B[3, 2] = 1.0 / math.sqrt(2.0)
        B[1, 3] = 1.0 / math.sqrt(2.0); B[4, 3] = -1.0 / math.sqrt(2.0)
        B[2, 4] = 1.0 / math.sqrt(2.0); B[3, 4] = -1.0 / math.sqrt(2.0)
        Sb = B.conj().T @ S_mat @ B
        Tb = B.conj().T @ T @ B
        cross_err = float(max(np.max(np.abs(Sb[:3, 3:])), np.max(np.abs(Sb[3:, :3])),
                              np.max(np.abs(Tb[:3, 3:])), np.max(np.abs(Tb[3:, :3]))))
        det_even_S = complex(np.linalg.det(Sb[:3, :3]))
        det_even_T = complex(np.linalg.det(Tb[:3, :3]))
        det_odd_S = complex(np.linalg.det(Sb[3:, 3:]))
        det_odd_T = complex(np.linalg.det(Tb[3:, 3:]))
        minus_I_odd = B[3:, :].conj() @ (S_mat @ S_mat) @ B[:, 3:]
        weil_res[f"k={k}"] = {
            "group_order": best_order,
            "block_cross_err": cross_err,
            "det_even_S_T": [round(det_even_S.real, 12), round(det_even_T.real, 12)],
            "det_odd_S_T": [round(det_odd_S.real, 12), round(det_odd_T.real, 12)],
            "tr_T_even": round(float(np.trace(Tb[:3, :3]).real), 10),
            "minus_I_on_odd_trace": round(float(np.trace(minus_I_odd).real), 10),
        }

    # 2. Legendre symbol hand on +-J^n K^e at mark (1, 2) vs planted wrong mark (1, 1):
    J_act = np.array([[1, 1], [1, 0]], dtype=int)
    K_act = np.array([[0, 1], [-1, 0]], dtype=int)
    leg5 = {1: 1, 2: -1, 3: -1, 4: 1}

    def check_hand_mark(mv: Tuple[int, int]) -> int:
        v = np.array(mv, dtype=int)
        matches = 0
        for sgn in (1, -1):
            for n in range(8):
                Jn = np.linalg.matrix_power(J_act, n)
                for e in (0, 1):
                    Ke = np.eye(2, dtype=int) if e == 0 else K_act
                    M = (sgn * (Jn @ Ke)) % 5
                    img = (M @ v) % 5
                    lam = next((l for l in range(1, 5) if np.array_equal(img, (l * v) % 5)), None)
                    if lam is not None and leg5[lam] == ((-1) ** (n + e)):
                        matches += 1
        return matches

    hand_matches_1_2 = check_hand_mark((1, 2))
    hand_matches_plant_1_1 = check_hand_mark((1, 1))

    # 3. B1935: Direct numerical check of Higgs triplet T-eigenphases (1/8, 3/8, 7/8) from c3(tau + 1) vs c3(tau):
    t_h = np.array([0.21 + 1.37j, 1.21 + 1.37j], dtype=np.complex128)
    _, c3_S_pair, _ = a2c._eval_base_c3(t_h, wide_cut=True)
    # Build 3x3 diagonal/swap operator M_T such that c3_S(tau + 1) = M_T @ c3_S(tau):
    # Check at a 3-point basis of taus so M_T is uniquely determined without assuming B1724!
    taus0 = np.array([0.13 + 1.21j, -0.27 + 1.54j, 0.39 + 1.83j], dtype=np.complex128)
    _, c3_0, _ = a2c._eval_base_c3(taus0, wide_cut=True)
    _, c3_1, _ = a2c._eval_base_c3(taus0 + 1.0, wide_cut=True)
    # c3_0 and c3_1 have shape (3_taus, 3_components); solve c3_1.T = M_T @ c3_0.T:
    M_T = c3_1.T @ np.linalg.inv(c3_0.T)
    M_T_unitarity_err = float(np.max(np.abs(M_T.conj().T @ M_T - np.eye(3))))
    eig_T = np.linalg.eigvals(M_T)
    eig_phases_over_2pi = sorted([(math.atan2(z.imag, z.real) / (2.0 * math.pi)) % 1.0 for z in eig_T])

    # 4. Sector coincidences for N = 2..60 (B1935 sec 4):
    # Charges 6Y: Q=1, u=-4, d=2, L=-3, e=6 -> pairs: up=(1,-4), down=(1,2), lep=(-3,6)
    pairs = {"up": (1, -4), "down": (1, 2), "lep": (-3, 6)}
    coinc = {}
    for p1, p2 in [("up", "down"), ("up", "lep"), ("down", "lep")]:
        a1, b1 = pairs[p1]
        a2, b2 = pairs[p2]
        eq_N, neg_N, tr_N, neg_tr_N = [], [], [], []
        for N in range(2, 61):
            if (a1 - a2) % N == 0 and (b1 - b2) % N == 0:
                eq_N.append(N)
            if (a1 + a2) % N == 0 and (b1 + b2) % N == 0:
                neg_N.append(N)
            if (a1 - b2) % N == 0 and (b1 - a2) % N == 0:
                tr_N.append(N)
            if (a1 + b2) % N == 0 and (b1 + a2) % N == 0:
                neg_tr_N.append(N)
        coinc[f"{p1}_vs_{p2}"] = {
            "equal": eq_N,
            "negated": neg_N,
            "transposed": tr_N,
            "negated_transposed": neg_tr_N,
        }

    # 5. B1936 exterior degrees k = 2 * (6Y) mod 5:
    charges_6Y = {"Q": 1, "u_c": -4, "e_c": 6, "d_c": 2, "L": -3, "nu_c": 0, "H": 3}
    degrees = {k: (2 * v) % 5 for k, v in charges_6Y.items()}

    return {
        "weil_level_5": weil_res,
        "legendre_hand_32_cases_mark_1_2": hand_matches_1_2,
        "legendre_hand_plant_mark_1_1": hand_matches_plant_1_1,
        "higgs_triplet_T_unitarity_err": M_T_unitarity_err,
        "higgs_triplet_T_eigenphases_over_2pi": [round(x, 12) for x in eig_phases_over_2pi],
        "sector_coincidences_N_2_to_60": coinc,
        "b1936_exterior_degrees": degrees,
    }


# =============================================================================
# CHECK 5: B1938 — KRONECKER SZEGO RESIDUE & MELLIN DETERMINANT
# =============================================================================

def run_check5_b1938() -> Dict:
    # Check |theta[c](0)/eta|^2 = det Delta_chi via incomplete-gamma Riemann/Epstein Mellin formula
    # for flat line bundle holonomy chi = c - (1/2, 1/2) reduced to [0, 1)^2:
    # For lattice L = Z + Z*tau (area y = Im tau), shifted lattice v = (m + u1)*tau + (n + u2) (Wait:
    # theta[c](0|tau) = sum_n exp(i*pi*(n + c1)^2*tau + 2*pi*i*(n + c1)*c2).
    # Its zeros are at c = (1/2, 1/2); Kronecker's second limit formula says:
    # -zeta'_{chi}(0) = ln |theta[c](0|tau) / eta(tau)|^2 where chi = (u1, u2) = (c1 - 1/2, c2 - 1/2) mod 1,
    # and lambda_{m,n} = |m + u1 + (n + u2)*tau|^2 / y (Wait: check convention of (u1, u2) -> (c1, c2)!).
    with mp.workdps(45):
        pi = mp.pi
        max_err = mp.mpf(0)
        test_cases = [
            (mp.mpc("0.17", "1.35"), Fraction(1, 5), Fraction(2, 5)),
            (mp.mpc("-0.29", "1.82"), Fraction(2, 5), Fraction(3, 5)),
            (mp.mpc("0.41", "1.12"), Fraction(1, 7), Fraction(4, 7)),
            (mp.mpc("-0.11", "2.15"), Fraction(3, 10), Fraction(7, 10)),
        ]
        for t, c1f, c2f in test_cases:
            y = mp.im(t)
            c1 = mp.mpf(c1f.numerator) / c1f.denominator
            c2 = mp.mpf(c2f.numerator) / c2f.denominator
            # theta[c1, c2](0|tau):
            th = mp.mpc(0)
            for n in range(-22, 23):
                nc = mp.mpf(n) + c1
                th += mp.exp(1j * pi * nc * nc * t + 2j * pi * nc * c2)
            q = mp.exp(2j * pi * t)
            eta_p = mp.exp(1j * pi * t / 12)
            qp = mp.mpc(1)
            for m in range(1, 35):
                qp *= q
                eta_p *= (1 - qp)
            lhs = abs(th / eta_p) ** 2

            # Exact Poisson-resummed Mellin formula for Z(s) = sum_{m,n} (pi |(m+al)tau - (n-be)|^2 / y)^{-s}
            # where al = (c1 - 1/2) mod 1, be = (c2 - 1/2) mod 1:
            # Z'(0) = -1 + sum_{m,n} E_1(pi |(m+al)tau - (n-be)|^2 / y)
            #            + sum_{(m,n)!=(0,0)} cos(2*pi*(m*be + n*al)) * exp(-pi |m*tau - n|^2 / y) / (pi |m*tau - n|^2 / y)
            # and det Delta_chi = exp(-Z'(0)) = |theta[c1, c2](0|tau) / eta(tau)|^2.
            al = (c1 - mp.mpf("0.5")) % 1
            be = (c2 - mp.mpf("0.5")) % 1
            s_shift = mp.mpf(0)
            s_dual = mp.mpf(0)
            R_box = 16
            for m in range(-R_box, R_box + 1):
                for n in range(-R_box, R_box + 1):
                    A1 = pi * (abs((mp.mpf(m) + al) * t - (mp.mpf(n) - be)) ** 2) / y
                    s_shift += mp.e1(A1)
                    if m != 0 or n != 0:
                        A2 = pi * (abs(mp.mpf(m) * t - mp.mpf(n)) ** 2) / y
                        ph = mp.cos(2 * pi * (mp.mpf(m) * be + mp.mpf(n) * al))
                        s_dual += ph * mp.exp(-A2) / A2
            det_mellin = mp.exp(-(-mp.mpf(1) + s_shift + s_dual))
            max_err = max(max_err, abs(lhs - det_mellin))

        # Planted control: chi = c instead of c - (1/2, 1/2) at tau = 0.13 + 1.07i, c = (0.7, 0.1):
        t_pl = mp.mpc("0.13", "1.07")
        y_pl = mp.im(t_pl)
        c1_pl, c2_pl = mp.mpf("0.7"), mp.mpf("0.1")
        th_pl = sum(mp.exp(1j * pi * ((mp.mpf(n) + c1_pl) ** 2) * t_pl + 2j * pi * (mp.mpf(n) + c1_pl) * c2_pl) for n in range(-22, 23))
        q_pl = mp.exp(2j * pi * t_pl)
        eta_pl = mp.exp(1j * pi * t_pl / 12)
        qp_pl = mp.mpc(1)
        for m in range(1, 35):
            qp_pl *= q_pl
            eta_pl *= (1 - qp_pl)
        lhs_pl = mp.log(abs(th_pl / eta_pl) ** 2)
        s_sh_pl = mp.mpf(0)
        s_du_pl = mp.mpf(0)
        for m in range(-16, 17):
            for n in range(-16, 17):
                A1 = pi * (abs((mp.mpf(m) + c1_pl) * t_pl - (mp.mpf(n) - c2_pl)) ** 2) / y_pl
                s_sh_pl += mp.e1(A1)
                if m != 0 or n != 0:
                    A2 = pi * (abs(mp.mpf(m) * t_pl - mp.mpf(n)) ** 2) / y_pl
                    s_du_pl += mp.cos(2 * pi * (mp.mpf(m) * c2_pl + mp.mpf(n) * c1_pl)) * mp.exp(-A2) / A2
        plant_chi_eq_c_log_err = float(abs(lhs_pl - (-(-mp.mpf(1) + s_sh_pl + s_du_pl))))

    # Also check sum_s R_s^2 = 0 and up's R_1 == 0 on all 12 order-5 reps:
    taus_test = np.array([0.17 + 1.35j, -0.29 + 1.82j, 0.41 + 2.45j], dtype=np.complex128)
    max_sum_R2_rel = 0.0
    max_up_R1 = 0.0
    denom_hat, _, _ = a2c._eval_base_c3(taus_test, wide_cut=True)
    ks = np.arange(-12.0, 13.0)[None, :]
    t_col = taus_test[:, None]
    for la, lb in a2c.ORDER5_12_REPS:
        for sname, ql, qr in a2c.SECT:
            ax, bx = ql * la, 2.0 * ql * lb
            ay, by = qr * la, 2.0 * qr * lb
            def th01(af, bf):
                k0 = round(-af); n0 = ks + (k0 + af)
                X0 = np.sum(np.exp(2j * math.pi * t_col * (n0 ** 2) + 2j * math.pi * n0 * bf), axis=1)
                k1 = round(-af - 0.5); n1 = ks + (k1 + af)
                X1 = np.sum(np.exp(2j * math.pi * t_col * ((n1 + 0.5) ** 2) + 2j * math.pi * n1 * bf), axis=1)
                return X0, X1
            X0, X1 = th01(ax, bx)
            Y0, Y1 = th01(ay, by)
            eb_x = a2c.cmath_exp_pi(bx)
            eb_y = a2c.cmath_exp_pi(by)
            M_mat = np.zeros((3, 2, 2), dtype=np.complex128)
            M_mat[:, 0, 0] = X0 * Y0 / denom_hat
            M_mat[:, 0, 1] = eb_y * X0 * Y1 / (1j * denom_hat)
            M_mat[:, 1, 0] = eb_x * X1 * Y0 / (1j * denom_hat)
            M_mat[:, 1, 1] = -(eb_x * eb_y) * X1 * Y1 / denom_hat
            R_arr = np.column_stack([np.sum(a2c.EC_LIST[si][None, :, :] * M_mat, axis=(1, 2)) for si in range(4)])
            sum_r2 = np.abs(np.sum(R_arr ** 2, axis=1)) / np.sum(np.abs(R_arr) ** 2, axis=1)
            max_sum_R2_rel = max(max_sum_R2_rel, float(np.max(sum_r2)))
            if sname == "up":
                max_up_R1 = max(max_up_R1, float(np.max(np.abs(R_arr[:, 0]))))

    return {
        "mellin_det_vs_theta_eta_max_err": float(max_err),
        "plant_chi_eq_c_log_err": plant_chi_eq_c_log_err,
        "sum_R_s_sq_rel_max_err": max_sum_R2_rel,
        "up_R1_order5_max_abs": max_up_R1,
    }


# =============================================================================
# CHECK 6: B1941 — POINTWISE DETERMINANT VS ONE-LOOP TRACE IN MPMATH
# =============================================================================

def eval_mp_det_and_tr2_12pt(tau: complex, l2_val: float, exact_weight: bool = True) -> Dict[Tuple[str, str], Tuple[float, float]]:
    """Arbitrary-precision mpmath evaluation of <ln det H_hat> and <Tr H_hat^2> across the 12 projective order-5 reps."""
    y_f = tau.imag
    dps = max(45, int(3.0 * y_f) + 35)
    pts_5_12 = [(Fraction(round(a * 5), 5), Fraction(round(b * 5), 5)) for a, b in a2c.ORDER5_12_REPS]
    with mp.workdps(dps):
        t = mp.mpc(mp.mpf(repr(tau.real)), mp.mpf(repr(tau.imag)))
        x_r, y_r = mp.re(t), mp.im(t)
        l2 = mp.mpf(repr(l2_val))
        pi = mp.pi
        eg = mp.euler
        q = mp.exp(2j * pi * t)
        m_max = max(8, int(math.ceil(dps * math.log(10) / (2.0 * math.pi * max(y_f, 0.8)) + 4)))
        eta_prod = mp.mpf(1)
        e2 = mp.mpf(1)
        qp = mp.mpc(1)
        for m in range(1, m_max + 3):
            qp *= q
            eta_prod *= 1 - qp
            e2 -= 24 * m * qp / (1 - qp)
        denom_full = 2 * pi * ((mp.exp(1j * pi * t / 12) * eta_prod) ** 3)
        n_th = max(7, int(math.ceil(math.sqrt(dps * math.log(10) / (math.pi * max(y_f, 0.8))) + 4)))

        def th0_dt_mp(ca: Fraction, cb: Fraction):
            ca_m = mp.mpf(ca.numerator) / mp.mpf(ca.denominator)
            cb_m = mp.mpf(cb.numerator) / mp.mpf(cb.denominator)
            s0 = mp.mpc(0)
            s1 = mp.mpc(0)
            for k in range(-n_th, n_th + 1):
                na = mp.mpf(k) + ca_m
                tm = mp.exp(1j * pi * na * na * t + 2j * pi * na * cb_m)
                s0 += tm
                s1 += mp.mpf("0.5") * na * na * tm
            return s0, s1

        t2, dt2 = th0_dt_mp(Fraction(1, 2), Fraction(0, 1))
        t4, dt4 = th0_dt_mp(Fraction(0, 1), Fraction(1, 2))
        t3, dt3 = th0_dt_mp(Fraction(0, 1), Fraction(0, 1))
        R_h = [-(t2 * t2) / denom_full, -(t4 * t4) / denom_full, 1j * (t3 * t3) / denom_full]
        dN_h = [-2 * t2 * dt2 / denom_full, -2 * t4 * dt4 / denom_full, 2j * t3 * dt3 / denom_full]
        c3_S = [dN_h[q_i] - (e2 / 12) * R_h[q_i] for q_i in range(3)]
        c3_St = [mp.conj(v) for v in c3_S]

        th_cache = {}
        fa_cache = {}

        def thc01_frac(af: Fraction, bf: Fraction):
            key = (af, bf)
            if key in th_cache:
                return th_cache[key]
            aa = mp.mpf(af.numerator) / mp.mpf(af.denominator)
            bb = mp.mpf(bf.numerator) / mp.mpf(bf.denominator)
            k0 = round(-float(aa))
            k1 = round(-float(aa) - 0.5)
            X0 = mp.mpc(0)
            X1 = mp.mpc(0)
            for k in range(-n_th, n_th + 1):
                n0 = mp.mpf(k + k0) + aa
                X0 += mp.exp(2j * pi * t * n0 * n0 + 2j * pi * n0 * bb)
                n1 = mp.mpf(k + k1) + aa
                X1 += mp.exp(2j * pi * t * ((n1 + mp.mpf("0.5")) ** 2) + 2j * pi * n1 * bb)
            th_cache[key] = (X0, X1)
            return X0, X1

        def Fu_a0sq_frac(u1: Fraction, u2: Fraction):
            u1_r = u1 - Fraction(math.floor(u1))
            u2_r = u2 - Fraction(math.floor(u2))
            key = (u1_r, u2_r)
            if key in fa_cache:
                return fa_cache[key]
            if u1_r == 0 and u2_r == 0:
                fa_cache[key] = (None, mp.mpf(0))
                return fa_cache[key]
            a_m = mp.mpf(u1_r.numerator) / mp.mpf(u1_r.denominator)
            b_m = mp.mpf(u2_r.numerator) / mp.mpf(u2_r.denominator)
            if u1_r == 0:
                fu = pi * (2 * eg - 2 * mp.log(2) - mp.log(y_r)) + (pi ** 2) * y_r / (mp.sin(pi * b_m) ** 2)
                for m in range(1, m_max + 2):
                    for ms in (mp.mpf(m), mp.mpf(-m)):
                        wm = mp.exp(2j * pi * (ms * x_r + b_m) - 2 * pi * abs(ms) * y_r)
                        fu += (2 * pi / abs(ms)) * mp.re(wm / (1 - wm))
            else:
                fu = -pi * (mp.digamma(a_m) + mp.digamma(1 - a_m) + 2 * mp.log(2) + mp.log(y_r))
                for k in range(-m_max - 1, m_max + 2):
                    ms = mp.mpf(k) + a_m
                    wm = mp.exp(2j * pi * (ms * x_r + b_m) - 2 * pi * abs(ms) * y_r)
                    fu += (2 * pi / abs(ms)) * mp.re(wm / (1 - wm))
            nu_r = (u1_r + Fraction(1, 2)) - Fraction(math.floor(u1_r + Fraction(1, 2))) - Fraction(1, 2)
            if nu_r == Fraction(-1, 2):
                nu_r = Fraction(1, 2)
            nu = mp.mpf(nu_r.numerator) / mp.mpf(nu_r.denominator)
            bm_r = (-u2_r) - Fraction(math.floor(-u2_r))
            Bm = mp.mpf(bm_r.numerator) / mp.mpf(bm_r.denominator)
            w_z = nu * t - Bm
            ser = mp.mpc(0)
            for m in range(1, m_max + 2):
                qm = q ** m
                ser += (mp.exp(2j * pi * m * (t + w_z)) - mp.exp(2j * pi * m * (t - w_z))) / (2j * (1 - qm))
            a0 = pi * mp.cot(pi * w_z) + 4 * pi * ser + 2j * pi * nu
            fa_cache[key] = (fu, abs(a0) ** 2)
            return fa_cache[key]

        shift_old = 2 * pi * (l2 + mp.mpf("0.5") * mp.log(y_r) - eg - mp.log(pi))
        em2l2 = mp.exp(-2 * l2)
        char_shifts_frac = [
            (Fraction(0, 1), Fraction(0, 1)),
            (Fraction(0, 1), Fraction(1, 2)),
            (Fraction(1, 2), Fraction(0, 1)),
            (Fraction(1, 2), Fraction(1, 2)),
        ]
        acc = {(s, r): [mp.mpf(0), mp.mpf(0)] for s in ("up", "down", "lep") for r in ("S", "St")}
        for la, lb in pts_5_12:
            for sname, ql, qr in a2c.SECT:
                ax, bx = ql * la, 2 * ql * lb
                ay, by = qr * la, 2 * qr * lb
                X0, X1 = thc01_frac(ax, bx)
                Y0, Y1 = thc01_frac(ay, by)
                bx_m = mp.mpf((bx - 2 * Fraction(math.floor(bx / 2))).numerator) / mp.mpf(bx.denominator)
                by_m = mp.mpf((by - 2 * Fraction(math.floor(by / 2))).numerator) / mp.mpf(by.denominator)
                eb_x = mp.exp(1j * pi * bx_m)
                eb_y = mp.exp(1j * pi * by_m)
                Mm = [
                    [X0 * Y0 / denom_full, eb_y * X0 * Y1 / (1j * denom_full)],
                    [eb_x * X1 * Y0 / (1j * denom_full), -(eb_x * eb_y) * X1 * Y1 / denom_full],
                ]
                R_ch = [
                    sum(mp.mpc(a2c.EC_LIST[si][r, c].real, a2c.EC_LIST[si][r, c].imag) * Mm[r][c] for r in range(2) for c in range(2))
                    for si in range(4)
                ]
                ap, bp = ax + ay, Fraction(1, 2) * (bx + by)
                u_ch = []
                for si, (ds1, ds2) in enumerate(char_shifts_frac):
                    fu, a0sq = Fu_a0sq_frac(ap + ds1, bp + ds2)
                    if fu is None:
                        u_ch.append(mp.mpc(0))
                    else:
                        nv = shift_old + fu - (pi * a0sq * em2l2 if exact_weight else mp.mpf(0))
                        u_ch.append(mp.sqrt(nv) * R_ch[si] if nv > 0 else mp.mpc(0))
                for rn, c3v, Cmat in [("S", c3_S, a2c.COUP_S), ("St", c3_St, a2c.COUP_ST)]:
                    Ym = mp.matrix(3, 3)
                    for a_i in range(3):
                        for b_i in range(3):
                            s_val = mp.mpc(0)
                            for qi in range(3):
                                for si in range(4):
                                    cc = Cmat[qi, si, a_i, b_i]
                                    if cc != 0:
                                        s_val += c3v[qi] * u_ch[si] * mp.mpc(cc.real, cc.imag)
                            Ym[a_i, b_i] = s_val
                    ld = 2 * mp.log(abs(mp.det(Ym))) + 3 * mp.log(y_r)
                    Hm = y_r * (Ym.H * Ym)
                    tr2 = mp.re(sum(Hm[i, j] * Hm[j, i] for i in range(3) for j in range(3)))
                    acc[(sname, rn)][0] += ld / 12
                    acc[(sname, rn)][1] += tr2 / 12
        return {k: (float(v[0]), float(v[1])) for k, v in acc.items()}


def summarize_point_sample(taus: List[complex], l2_interp: a2c.CanonicalL2Interpolant) -> Dict:
    taus_arr = np.array(taus, dtype=np.complex128)
    l2_arr = l2_interp.eval_fd(taus_arr)
    det_331_pos, det_111_pos = 0, 0
    tr2_331_pos, tr2_111_pos = 0, 0
    det_331_vals, det_111_vals, tr2_331_vals = [], [], []
    for tau, l2_v in zip(taus, l2_arr):
        st = eval_mp_det_and_tr2_12pt(tau, float(l2_v), exact_weight=True)
        d_det_331 = (3 * st[("up", "St")][0] + 3 * st[("down", "S")][0] + st[("lep", "S")][0]) - (
            3 * st[("up", "S")][0] + 3 * st[("down", "St")][0] + st[("lep", "St")][0]
        )
        d_det_111 = (st[("up", "St")][0] + st[("down", "S")][0] + st[("lep", "S")][0]) - (
            st[("up", "S")][0] + st[("down", "St")][0] + st[("lep", "St")][0]
        )
        d_mtr2_331 = -(3 * st[("up", "St")][1] + 3 * st[("down", "S")][1] + st[("lep", "S")][1]) + (
            3 * st[("up", "S")][1] + 3 * st[("down", "St")][1] + st[("lep", "St")][1]
        )
        d_mtr2_111 = -(st[("up", "St")][1] + st[("down", "S")][1] + st[("lep", "S")][1]) + (
            st[("up", "S")][1] + st[("down", "St")][1] + st[("lep", "St")][1]
        )
        if d_det_331 > 0:
            det_331_pos += 1
        if d_det_111 > 0:
            det_111_pos += 1
        if d_mtr2_331 > 0:
            tr2_331_pos += 1
        if d_mtr2_111 > 0:
            tr2_111_pos += 1
        det_331_vals.append(d_det_331)
        det_111_vals.append(d_det_111)
        tr2_331_vals.append(d_mtr2_331)
    return {
        "n_points": len(taus),
        "ln_det_331_pos_count": det_331_pos,
        "ln_det_111_pos_count": det_111_pos,
        "minus_tr_H2_331_pos_count": tr2_331_pos,
        "minus_tr_H2_111_pos_count": tr2_111_pos,
        "ln_det_331_range": [round(min(det_331_vals), 4), round(max(det_331_vals), 4)],
        "ln_det_111_range": [round(min(det_111_vals), 4), round(max(det_111_vals), 4)],
        "minus_tr_H2_331_range": [min(tr2_331_vals), max(tr2_331_vals)],
    }


def run_check6_b1941(l2_interp: a2c.CanonicalL2Interpolant) -> Dict:
    import random
    # 1. B1941's exact 28-point sample (random.Random(1939)):
    rng_b1941 = random.Random(1939)
    taus_b1941 = []
    for yv in (0.9, 1.2, 1.6, 2.2, 3.0, 4.5, 6.0, 9.0):
        for _ in range(4):
            x = rng_b1941.uniform(-0.5, 0.5)
            if x * x + yv * yv >= 1.0:
                taus_b1941.append(complex(x, yv))

    # 2. Independent agy-002 28-point sample (np.random.default_rng(20261115)):
    rng_ind = np.random.default_rng(20261115)
    taus_ind = []
    while len(taus_ind) < 28:
        x = float(rng_ind.uniform(-0.49, 0.49))
        y = float(np.exp(rng_ind.uniform(math.log(0.9), math.log(8.5))))
        if x * x + y * y >= 1.001:
            taus_ind.append(complex(x, y))

    res_b1941 = summarize_point_sample(taus_b1941, l2_interp)
    res_ind = summarize_point_sample(taus_ind, l2_interp)
    return {
        "b1941_seed_1939_mpmath": res_b1941,
        "independent_seed_20261115_mpmath": res_ind,
    }


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    print("Building standalone CanonicalL2Interpolant...", flush=True)
    l2_interp = a2c.CanonicalL2Interpolant()

    print("Running Check 1 (B1940 tau -> tau + 1 & v2 vs v1)...", flush=True)
    c1 = run_check1_b1940(l2_interp)
    print("  pure mpmath max err across y=1.5..200:", max(c1["pure_mpmath_tau_plus_1_max_err"].values()), flush=True)
    print("  a2c eval_mp max err across y=1.5..200:", max(c1["a2c_eval_mp_tau_plus_1_max_err"].values()), flush=True)
    print("  planted 15-dps y=20 err:", c1["plant_15dps_y20_tau_plus_1_err"], flush=True)
    print("  B1940 actual max |dln| vs B1932:", c1["b1940_max_abs_dln_actual"], flush=True)

    print("Running Check 2 (B1942 order 15 & SM-C13 order 5)...", flush=True)
    c2 = run_check2_b1942_and_smc13(l2_interp)
    print("  exact order-15 -> order-5 multiplicity:", c2["map_6w_hit_multiplicity_min_max"], flush=True)
    print("  planted (-2, 6) break:", c2["planted_lepton_charge_m2_6_break"], flush=True)

    print("Running Check 3 (B1943 Smith normal forms & fixed lines)...", flush=True)
    c3 = run_check3_b1943()
    print("  Smith(LR - I), Smith(LR + I):", c3["smith_forms"]["LR"], flush=True)

    print("Running Check 4 (B1934, B1935, B1936 algebra)...", flush=True)
    c4 = run_check4_b1934_b1935_b1936()
    print("  Weil group orders & block cross errs:",
          {k: (v["group_order"], v["block_cross_err"]) for k, v in c4["weil_level_5"].items()}, flush=True)

    print("Running Check 5 (B1938 Kronecker & Mellin det)...", flush=True)
    c5 = run_check5_b1938()
    print("  Mellin det vs |theta/eta|^2 max err:", c5["mellin_det_vs_theta_eta_max_err"], flush=True)
    print("  sum R_s^2 rel err:", c5["sum_R_s_sq_rel_max_err"], "up R1 max:", c5["up_R1_order5_max_abs"], flush=True)

    print("Running Check 6 (B1941 pointwise ln det vs -Tr H^2)...", flush=True)
    c6 = run_check6_b1941(l2_interp)
    print("  seed 1939 ln det pos:", c6["b1941_seed_1939_mpmath"]["ln_det_331_pos_count"], "/ 28; range:", c6["b1941_seed_1939_mpmath"]["ln_det_331_range"], flush=True)
    print("  seed 20261115 ln det pos:", c6["independent_seed_20261115_mpmath"]["ln_det_331_pos_count"], "/ 28; range:", c6["independent_seed_20261115_mpmath"]["ln_det_331_range"], flush=True)

    res = {
        "check1_b1940_and_m37": c1,
        "check2_b1942_and_smc13": c2,
        "check3_b1943_smith": c3,
        "check4_b1934_b1935_b1936": c4,
        "check5_b1938_kronecker_mellin": c5,
        "check6_b1941_pointwise": c6,
    }
    out_json = out_dir / "verify_r83_counterchecks.json"
    out_json.write_text(json.dumps(res, indent=2, allow_nan=False) + "\n")
    print("Saved", out_json.name, "successfully.", flush=True)


if __name__ == "__main__":
    main()
