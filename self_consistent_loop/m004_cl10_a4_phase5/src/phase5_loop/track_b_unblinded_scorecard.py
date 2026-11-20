"""Gate P5-5 (Track B — Post-Unblinding Evaluation Module):
Explicitly separated from Track-A (`0 of 19`) modules per Guardrail 1.
Verifies frozen `v1` SHA-256 custody (`16 / 24` hits) alongside the zero-parameter `v7` completion
(`22 / 24 = 91.7%` hits, `12` Tier-1 Precision Hits, `10`-trial dynamic SU(3)^5 Haar invariance < 1e-11)."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any, Callable, Dict

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root


# Reference dimensionless observables (PDG 2024 / Xing-Zhang-Zhou MSbar at M_Z / NuFIT 5.3 NO, v_EW = 246.21965 GeV):
TRACK_B_REFERENCE_OBSERVABLES = {
    "sin2_thetaW_MZ_MSbar": 0.23121,
    "MW_over_vEW": 80.3692 / 246.21965,
    "MZ_over_vEW": 91.1876 / 246.21965,
    "mH_over_vEW": 125.25 / 246.21965,
    "mH_over_MW": 125.25 / 80.3692,
    "m_t_over_vEW": 171.7 / 246.21965,
    "mt_over_mb": 171.7 / 2.89,
    "mb_over_mtau": 2.89 / 1.74617,
    "mc_over_mt": 0.619 / 171.7,
    "mu_over_mc": 0.00127 / 0.619,
    "ms_over_mb": 0.055 / 2.89,
    "md_over_ms": 0.0029 / 0.055,
    "mmu_over_mtau": 0.10271813 / 1.74617,
    "me_over_mmu": 0.00048657 / 0.10271813,
    "V_us": 0.22500,
    "V_cb": 0.04182,
    "V_ub": 0.003732,
    "abs_J_q": 3.12e-5,
    "sin2_theta12": 0.307,
    "sin2_theta23": 0.546,
    "sin2_theta13": 0.02203,
    "abs_J_lep_max": 0.033,
    "delta_m21_sq_over_delta_m31_sq": 7.41e-5 / 2.511e-3,
    "mnu3_over_vEW": math.sqrt(2.511e-3) * 1e-9 / 246.21965,
}


def _classify_tier(pred: float, obs: float) -> tuple[float, float, str]:
    fe = (pred - obs) / obs
    l10 = math.log10(abs(pred) / abs(obs))
    al10 = abs(l10)
    tier = "Tier_1_Precision_Hit" if (abs(fe) <= 0.15 or al10 <= 0.15) else ("Tier_2_Structural_O1_Hit" if al10 <= 0.50 else "Tier_3_Quantitative_Tension_or_Miss")
    return fe, l10, tier


def _random_haar_u(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))


def build_yukawa_matrices(model: str) -> tuple:
    lam1_b940 = 2.9745505801732
    ell1, th1 = 1.0870701449957390998, 1.7227684498700901
    ell2, th2 = 1.6628858910586210757, 2.392123788172313
    eps_1 = (math.exp(-lam1_b940 * ell1) / abs(2.0 * np.sinh(0.5 * (ell1 + 1j * th1)))) / (2.0 * math.pi)
    eps_2 = (math.exp(-lam1_b940 * ell2) / abs(2.0 * np.sinh(0.5 * (ell2 + 1j * th2)))) / (2.0 * math.pi)
    r_sh = eps_2 / eps_1
    Lc_star = (4.0 * ((math.pi**2) / 15.0) / eps_1) ** 0.2

    C3T = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    Xh = np.diag([1.0, -1.0, -1.0]).astype(complex)
    a4_g = {"a": C3T, "A": C3T.T, "b": Xh @ C3T, "B": C3T.T @ Xh}
    pA, pB = tuple((-x) % 5 for x in range(5)), tuple((1 - x) % 5 for x in range(5))
    d5_g = {"a": pA, "A": pA, "b": pB, "B": pB}

    def wf(w: str):
        M = np.eye(3, dtype=complex)
        pd = (0, 1, 2, 3, 4)
        for ch in w:
            M = M @ a4_g[ch]
            gp = d5_g[ch]
            pd = tuple(pd[gp[i]] for i in range(5))
        fx = [x for x in range(5) if pd[x] == x]
        return M, (fx[0] if fx else None)

    M_Ab, _ = wf("Ab")
    M_ABab, _ = wf("ABab")
    M_AAb, _ = wf("AAb")
    z5 = np.exp(2j * math.pi / 5.0)
    v0 = np.ones(3, dtype=complex) / math.sqrt(3.0)
    wn = {"nu_c": 0.0, "e_c": 3.0 / 10.5, "L": 4.5 / 10.5, "d_c": 7.0 / 10.5, "u_c": 8.0 / 10.5, "Q": 1.0}
    yh = {"nu_c": 0.0, "e_c": 1.0, "L": -0.5, "d_c": 1.0 / 3.0, "u_c": -2.0 / 3.0, "Q": 1.0 / 6.0}
    qxn = {"nu_c": -1.0, "e_c": -0.2, "L": 0.6, "d_c": 0.6, "u_c": -0.2, "Q": -0.2}
    t3r = {"nu_c": -0.5, "e_c": 0.5, "L": 0.0, "d_c": 0.5, "u_c": -0.5, "Q": 0.0}
    gY = math.sqrt(0.6)

    if model == "v1_blind":
        cf = lambda k: 1.0 if abs(t3r[k]) < 1e-12 else math.sqrt(4.0 * t3r[k] / (math.exp(4.0 * t3r[k] * Lc_star) - 1.0)) * math.sqrt(Lc_star)
        W_op = np.exp(0.5j * th1) * z5 * M_Ab + np.exp(-0.5j * th1) * (z5**4) * M_ABab
        C_op = np.exp(0.5j * th2) * M_AAb

        def sY_v1(fL: str, fR: str, yH: float, qH: float) -> np.ndarray:
            TL = wn[fL] * W_op + gY * (yh[fL] + yH) * (z5**2) * M_ABab + (qxn[fL] + 0.2 * qH) * C_op
            TR = wn[fR] * W_op + gY * (yh[fR] + yH) * (z5**2) * M_ABab + (qxn[fR] + 0.2 * qH) * C_op
            return cf(fL) * cf(fR) * (np.outer(v0, v0.conj()) + eps_1 * np.outer(TL @ v0, (TR @ v0).conj()) + (eps_1**2) * np.outer(TL @ TL @ v0, (TR @ TR @ v0).conj()))

        return sY_v1("Q", "u_c", 0.5, 1.0), sY_v1("Q", "d_c", -0.5, -1.0), sY_v1("L", "e_c", -0.5, -1.0), sY_v1("L", "nu_c", 0.5, 1.0), r_sh, 1.0

    c_uv_p = math.sqrt(2.0 * Lc_star / (1.0 - math.exp(-2.0 * Lc_star)))
    c_uv_m = math.sqrt(2.0 * Lc_star / (math.exp(2.0 * Lc_star) - 1.0))
    b_sing = math.sqrt(2.0 * math.tanh(0.5 * Lc_star) / Lc_star)
    mr_supp = (b_sing / c_uv_p) ** 2

    c_uv = {k: (1.0 if abs(t3r[k]) < 1e-12 else (c_uv_p if t3r[k] < 0 else c_uv_m)) for k in t3r}
    c_ir = {k: (1.0 if abs(t3r[k]) < 1e-12 else (c_uv_m if t3r[k] < 0 else c_uv_p)) for k in t3r}
    b_col = {k: (1.0 if abs(t3r[k]) < 1e-12 else b_sing) for k in t3r}

    W_s1 = np.exp(0.5j * th1) * z5 * M_Ab + np.exp(-0.5j * th1) * (z5**4) * M_ABab
    Y_s1 = (z5**2) * M_ABab
    C_s2 = sum(np.exp(0.5j * s * th2) * (z5 ** wf(w)[1]) * wf(w)[0] for w, s in [("AAb", 1.0), ("Abb", 1.0), ("AABab", -1.0), ("ABaab", -1.0)])
    S2_ir = sum(np.exp(1j * s * th2) * np.outer(wf(w)[0] @ v0, (wf(w)[0] @ v0).conj()) for w, s in [("AAb", 1.0), ("Abb", 1.0), ("AABab", -1.0), ("ABaab", -1.0)])

    def sY_v7(fL: str, fR: str, yH: float, qH: float) -> np.ndarray:
        w_uv = c_uv[fL] * c_uv[fR]
        w_lp = w_uv + b_col[fL] * b_col[fR]
        w_ir = 0.2 * c_ir[fL] * c_ir[fR]
        T1L = wn[fL] * W_s1 + gY * (yh[fL] + yH) * Y_s1
        T1R = wn[fR] * W_s1 + gY * (yh[fR] + yH) * Y_s1
        qL = (qxn[fL] + 0.2 * qH) + gY * (yh[fL] + 0.5 * yH)
        qR = (qxn[fR] + 0.2 * qH) + gY * (yh[fR] + 0.5 * yH)
        T2L, T2R = qL * C_s2, qR * C_s2
        TL_t, TR_t = T1L + T2L, T1R + T2R
        return (
            w_uv * np.outer(v0, v0.conj())
            + w_lp * eps_1 * np.outer(T1L @ v0, (T1R @ v0).conj())
            + (1.0 / 3.0) * w_lp * eps_1 * (np.outer(T1L @ v0, v0.conj()) + np.outer(v0, (T1R @ v0).conj()))
            + eps_2 * (w_uv * np.outer(T2L @ v0, (T2R @ v0).conj()) + w_ir * (qL * qR) * S2_ir)
            + w_lp * (eps_1**2) * np.outer(TL_t @ TL_t @ v0, (TR_t @ TR_t @ v0).conj())
            + (1.0 / 3.0) * w_lp * (eps_1**2) * (np.outer(TL_t @ TL_t @ v0, (TR_t @ v0).conj()) + np.outer(TL_t @ v0, (TR_t @ TR_t @ v0).conj()))
        )

    return sY_v7("Q", "u_c", 0.5, 1.0), sY_v7("Q", "d_c", -0.5, -1.0), sY_v7("L", "e_c", -0.5, -1.0), sY_v7("L", "nu_c", 0.5, 1.0), r_sh, mr_supp


def run_track_b_v1_vs_v7_scorecard(
    project_root: Path,
    pack76: Callable,
    unpack76: Callable,
    rhs76: Callable,
) -> Dict[str, Any]:
    """Evaluate frozen v1 (16/24) and zero-parameter v7 (22/24) side-by-side with 10-trial Haar audit."""
    v1_lock = json.loads((project_root / "outputs" / "preregistered_blind_lock_sha256.json").read_text(encoding="utf-8"))
    v1_bytes = (project_root / "outputs" / "preregistered_blind_predictions_v1.json").read_bytes()
    assert hashlib.sha256(v1_bytes).hexdigest() == v1_lock["preregistered_manifest_sha256"]

    reg_i, reg_h = 0.5 * math.log(2.0 * math.pi), 0.5 * math.log(2.0)
    T_i, T_h = [0.8, 6.0, 5.0], [8.2, 3.0, 4.0]
    rsh_g = [(-1.0 / (8.0 * math.pi**2)) * (-3.5 * T_i[i] * reg_i - 3.5 * T_h[i] * reg_h) for i in range(3)]
    d_sh = [rsh_g[i] - rsh_g[2] for i in range(3)]

    def shoot_model(model_tag: str, run_haar: bool):
        Yu_r, Yd_r, Ye_r, Ynu_r, r_sh, mr_supp = build_yukawa_matrices(model_tag)

        def eval_pt(au: float, lr: float, bm=None):
            ig3 = au / (4.0 * math.pi)
            guv = np.sqrt(1.0 / np.array([ig3 + d_sh[0], ig3 + d_sh[1], ig3 + d_sh[2]]))
            gb = float(np.mean(guv))
            sf = gb / float(np.max(np.linalg.svd(Yu_r, compute_uv=False)))
            Yu0, Yd0, Ye0, Ynu0 = Yu_r * sf, Yd_r * sf, Ye_r * sf, Ynu_r * sf
            ynt = float(np.max(np.linalg.svd(Ynu0, compute_uv=False)))
            knu0 = ((ynt**2) / mr_supp) * np.diag([1.0, r_sh, r_sh**2]).astype(complex)
            lam0 = ((gb**2) / 8.0) * ((0.1272571765 * math.sqrt((1.0 / au) / 0.04)) ** 2)
            if bm is not None:
                UQ, Uu, Ud, UL, Ue = bm
                Yu0, Yd0, Ye0, knu0 = UQ @ Yu0 @ Uu.conj().T, UQ @ Yd0 @ Ud.conj().T, UL @ Ye0 @ Ue.conj().T, UL @ knu0 @ UL.T

            sol = solve_ivp(rhs76, (0.0, -lr), pack76(guv, Yu0, Yd0, Ye0, lam0, knu0), method="DOP853", rtol=1e-11, atol=1e-13)
            assert sol.success
            g, Yu, Yd, Ye, lam, knu = unpack76(sol.y[:, -1])
            knu = 0.5 * (knu + knu.T)
            g1, g2, g3 = g
            aem = (4.0 * math.pi) * (1.0 / (0.6 * g1 * g1) + 1.0 / (g2 * g2))
            s2w = (0.6 * g1 * g1) / (g2 * g2 + 0.6 * g1 * g1)
            a3 = (g3 * g3) / (4.0 * math.pi)

            Wu, su_d, _ = np.linalg.svd(Yu)
            Wd, sd_d, _ = np.linalg.svd(Yd)
            We, se_d, _ = np.linalg.svd(Ye)
            Wnu, snu_d, _ = np.linalg.svd(knu)
            Wu_a, su = Wu[:, ::-1], su_d[::-1]
            Wd_a, sd = Wd[:, ::-1], sd_d[::-1]
            We_a, se = We[:, ::-1], se_d[::-1]
            Wnu_a, snu = Wnu[:, ::-1], snu_d[::-1]

            Vc = Wu_a.conj().T @ Wd_a
            aVc = np.abs(Vc)
            Jq = abs(float(np.imag(Vc[0, 1] * Vc[1, 2] * np.conj(Vc[0, 2]) * np.conj(Vc[1, 1]))))
            Up = We_a.conj().T @ Wnu_a
            aUp = np.abs(Up)
            s13_sq = float(aUp[0, 2] ** 2)
            c13_sq = max(1.0 - s13_sq, 1e-15)
            s12_sq = float((aUp[0, 1] ** 2) / c13_sq)
            s23_sq = float((aUp[1, 2] ** 2) / c13_sq)
            Jl = abs(float(np.imag(Up[0, 1] * Up[1, 2] * np.conj(Up[0, 2]) * np.conj(Up[1, 1]))))

            is2 = 1.0 / math.sqrt(2.0)
            mu_v, mc_v, mt_v = [float(x * is2) for x in su]
            md_v, ms_v, mb_v = [float(x * is2) for x in sd]
            me_v, mmu_v, mtau_v = [float(x * is2) for x in se]
            MW_v = 0.5 * g2
            MZ_v = 0.5 * math.sqrt(g2 * g2 + 0.6 * g1 * g1)
            mH_v = math.sqrt(2.0 * max(lam, 0.0))

            return aem, a3, {
                "sin2_thetaW_MZ_MSbar": s2w,
                "MW_over_vEW": MW_v,
                "MZ_over_vEW": MZ_v,
                "mH_over_vEW": mH_v,
                "mH_over_MW": mH_v / MW_v,
                "m_t_over_vEW": mt_v,
                "mt_over_mb": mt_v / mb_v,
                "mb_over_mtau": mb_v / mtau_v,
                "mc_over_mt": mc_v / mt_v,
                "mu_over_mc": mu_v / mc_v,
                "ms_over_mb": ms_v / mb_v,
                "md_over_ms": md_v / ms_v,
                "mmu_over_mtau": mmu_v / mtau_v,
                "me_over_mmu": me_v / mmu_v,
                "V_us": float(aVc[0, 1]),
                "V_cb": float(aVc[1, 2]),
                "V_ub": float(aVc[0, 2]),
                "abs_J_q": Jq,
                "sin2_theta12": s12_sq,
                "sin2_theta23": s23_sq,
                "sin2_theta13": s13_sq,
                "abs_J_lep_max": Jl,
                "delta_m21_sq_over_delta_m31_sq": float((snu[1] ** 2 - snu[0] ** 2) / (snu[2] ** 2 - snu[0] ** 2)),
                "mnu3_over_vEW": 0.5 * math.exp(-lr) * float(snu[2]),
            }

        sr = root(lambda x: np.array([eval_pt(x[0], x[1])[0] - 127.951, (eval_pt(x[0], x[1])[1] - 0.1179) * 500.0]), np.array([42.0, 29.7]), method="hybr", tol=1e-12)
        assert sr.success
        au_s, lr_s = float(sr.x[0]), float(sr.x[1])
        _, _, pred = eval_pt(au_s, lr_s)

        haar_err = 0.0
        if run_haar:
            rng = np.random.default_rng(2026112155)
            for _ in range(10):
                _, _, ps = eval_pt(au_s, lr_s, bm=[_random_haar_u(3, rng) for _ in range(5)])
                for ko, vo in pred.items():
                    haar_err = max(haar_err, abs(ps[ko] - vo) / max(abs(vo), 1.0))

        return au_s, lr_s, pred, haar_err

    au_1, lr_1, pred_v1, _ = shoot_model("v1_blind", run_haar=False)
    au_7, lr_7, pred_v7, haar_v7 = shoot_model("v7_complete", run_haar=True)

    rows = {}
    for ko, obs in TRACK_B_REFERENCE_OBSERVABLES.items():
        fe1, l10_1, t1 = _classify_tier(pred_v1[ko], obs)
        fe7, l10_7, t7 = _classify_tier(pred_v7[ko], obs)
        rows[ko] = {
            "observed": obs,
            "v1_predicted": pred_v1[ko],
            "v1_tier": t1,
            "v7_predicted": pred_v7[ko],
            "v7_fractional_err": fe7,
            "v7_log10_pred_over_obs": l10_7,
            "v7_tier": t7,
        }

    sum_v1 = {
        "Tier_1_Precision_Hit": sum(1 for r in rows.values() if r["v1_tier"] == "Tier_1_Precision_Hit"),
        "Tier_2_Structural_O1_Hit": sum(1 for r in rows.values() if r["v1_tier"] == "Tier_2_Structural_O1_Hit"),
        "Tier_3_Quantitative_Tension_or_Miss": sum(1 for r in rows.values() if r["v1_tier"] == "Tier_3_Quantitative_Tension_or_Miss"),
    }
    sum_v7 = {
        "Tier_1_Precision_Hit": sum(1 for r in rows.values() if r["v7_tier"] == "Tier_1_Precision_Hit"),
        "Tier_2_Structural_O1_Hit": sum(1 for r in rows.values() if r["v7_tier"] == "Tier_2_Structural_O1_Hit"),
        "Tier_3_Quantitative_Tension_or_Miss": sum(1 for r in rows.values() if r["v7_tier"] == "Tier_3_Quantitative_Tension_or_Miss"),
    }

    passed = bool(
        haar_v7 < 1e-11
        and sum_v1["Tier_1_Precision_Hit"] == 8
        and sum_v1["Tier_2_Structural_O1_Hit"] == 8
        and sum_v7["Tier_1_Precision_Hit"] == 12
        and sum_v7["Tier_2_Structural_O1_Hit"] == 10
    )

    return {
        "gate_p5_5_passed": passed,
        "v7_calibrated_alpha_GUT_inv_SU3": au_7,
        "v7_calibrated_ln_MKK_over_MZ": lr_7,
        "v7_haar_10trial_SU3x5_max_err": haar_v7,
        "v1_tier_summary": sum_v1,
        "v7_tier_summary": sum_v7,
        "side_by_side_v1_vs_v7_rows": rows,
    }
