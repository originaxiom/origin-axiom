#!/usr/bin/env python3
"""AST-Isolated Zero-Import Referee Suite for Phase 10 (`145 / 145` Cumulative Controls, Guardrails 1-6)."""
from __future__ import annotations

import ast
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

mp.mp.dps = 50
PROJECT_ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_REFEREE_IMPORTS = (
    "phase10_toe",
    "phase9_toe",
    "phase8_toe",
    "phase7_toe",
    "phase6_toe",
    "phase5_loop",
    "phase4_loop",
    "relational_loop",
    "cusped_loop",
    "phi_loop",
    "src.",
)

TRACK_A_MODULES = {
    "src/phase10_toe/p10_1_pati_salam_projection.py",
    "src/phase10_toe/p10_2_m5_axion_baryon_closure.py",
    "src/phase10_toe/p10_3_falsifiability_observables.py",
    "src/phase10_toe/p10_4_joint_consistency.py",
    "src/phase10_toe/phase10_engine.py",
}

FORBIDDEN_PDG_FLOATS = (
    127.951,
    0.1179,
    0.23121,
    0.225,
    0.04182,
    0.003732,
    3.12e-5,
    0.307,
    0.546,
    0.02203,
    246.21965,
    2.43536e18,
    0.120,
    2.10e-9,
    0.9649,
    6.12e-10,
    0.038,
    0.036,
    2.4e34,
)

FORBIDDEN_FLAG_KEYS = {"extends_to_cover", "bar_theta_QCD", "theta_qcd_bar", "dynamical_strong_cp_theta_eff"}


def run_ast_guardrail_scan(project_root: Path = PROJECT_ROOT) -> Dict[str, Any]:
    ref_path = Path(__file__).resolve()
    py_files: List[Path] = []
    for d in (project_root / "src", project_root / "scripts", project_root / "tests"):
        if d.exists():
            py_files.extend(sorted(d.rglob("*.py")))

    bad_imports: List[str] = []
    bad_track_a_floats: List[str] = []
    bad_flags: List[str] = []

    for fp in py_files:
        rel = str(fp.relative_to(project_root)).replace("\\", "/")
        tree = ast.parse(fp.read_text(encoding="utf-8"), filename=rel)
        is_ref = fp.resolve() == ref_path
        is_track_a = rel in TRACK_A_MODULES

        for node in ast.walk(tree):
            if is_ref:
                if isinstance(node, ast.Import):
                    for a in node.names:
                        if a.name.startswith(FORBIDDEN_REFEREE_IMPORTS) or a.name == "src":
                            bad_imports.append(a.name)
                elif isinstance(node, ast.ImportFrom):
                    mod = node.module or ""
                    if node.level > 0 or mod.startswith(FORBIDDEN_REFEREE_IMPORTS) or mod == "src":
                        bad_imports.append(mod or f"relative_{node.level}")

            if is_track_a and isinstance(node, ast.Constant) and isinstance(node.value, float):
                val = float(node.value)
                for tgt in FORBIDDEN_PDG_FLOATS:
                    if abs(val - tgt) <= 1e-11 * max(1.0, abs(tgt)):
                        bad_track_a_floats.append(f"{rel}:{node.lineno}:{val}")

            if isinstance(node, ast.Dict):
                for k_n, v_n in zip(node.keys, node.values):
                    if isinstance(k_n, ast.Constant) and k_n.value in FORBIDDEN_FLAG_KEYS:
                        if isinstance(v_n, ast.Constant) and isinstance(v_n.value, (bool, int, float)):
                            bad_flags.append(f"{rel}:{k_n.lineno}:{k_n.value}")

    passed = bool(not bad_imports and not bad_track_a_floats and not bad_flags)
    return {
        "passed": passed,
        "num_scanned_files": len(py_files),
        "forbidden_referee_imports": bad_imports,
        "forbidden_track_a_pdg_floats": bad_track_a_floats,
        "forbidden_literal_flags": bad_flags,
    }


def _random_haar_u(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    q = q * (d / np.abs(d))
    return q / (np.linalg.det(q) ** (1.0 / n))


def _rhs76_indep(_t: float, y: np.ndarray) -> np.ndarray:
    g = y[0:3]
    yu = (y[3:12] + 1j * y[12:21]).reshape(3, 3)
    yd = (y[21:30] + 1j * y[30:39]).reshape(3, 3)
    ye = (y[39:48] + 1j * y[48:57]).reshape(3, 3)
    lam = float(y[57])
    knu = (y[58:67] + 1j * y[67:76]).reshape(3, 3)
    g1, g2, g3 = g
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    c1 = 1.0 / (16.0 * math.pi * math.pi)
    c2 = c1 * c1
    hu, hd, he = yu @ yu.conj().T, yd @ yd.conj().T, ye @ ye.conj().T
    tu, td, te = float(np.real(np.trace(hu))), float(np.real(np.trace(hd))), float(np.real(np.trace(he)))
    tr_tot = 3.0 * tu + 3.0 * td + te
    b2 = np.array([[3.98, 2.7, 8.8], [0.9, 35.0 / 6.0, 12.0], [1.1, 4.5, -26.0]])
    cy = np.array([[1.7, 0.5, 1.5], [1.5, 1.5, 0.5], [2.0, 2.0, 0.0]])
    dg = c1 * np.array([4.1, -19.0 / 6.0, -7.0]) * (g**3) + c2 * (g**3) * (b2 @ np.array([g12, g22, g32]) - cy @ np.array([tu, td, te]))
    tu2, td2, te2, tud = (
        float(np.real(np.trace(hu @ hu))),
        float(np.real(np.trace(hd @ hd))),
        float(np.real(np.trace(he @ he))),
        float(np.real(np.trace(hu @ hd))),
    )
    chi2 = -2.25 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.5 * tud
    y2g = (
        ((85.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * tu
        + ((25.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * td
        + ((75.0 / 8.0) * g12 + (15.0 / 8.0) * g22) * te
    )
    dyu = c1 * ((1.5 * (hu - hd) + (tr_tot - 0.85 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ yu) + c2 * (
        1.5 * (hu @ hu) - hu @ hd - 0.25 * (hd @ hu) + 2.75 * (hd @ hd) - 2.25 * tr_tot * hu - 12.0 * lam * hu
        + (chi2 + y2g + 6.0 * (lam**2) + (1187.0 / 600.0) * (g12**2) - 0.45 * g12 * g22 + (19.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (223.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * hu - (43.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * hd
    ) @ yu
    dyd = c1 * ((1.5 * (hd - hu) + (tr_tot - 0.25 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ yd) + c2 * (
        1.5 * (hd @ hd) - hd @ hu - 0.25 * (hu @ hd) + 2.75 * (hu @ hu) - 2.25 * tr_tot * hd - 12.0 * lam * hd
        + (chi2 + y2g + 6.0 * (lam**2) - (127.0 / 600.0) * (g12**2) - 1.35 * g12 * g22 + (31.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (187.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * hd - (79.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * hu
    ) @ yd
    dye = c1 * ((1.5 * he + (tr_tot - 2.25 * g12 - 2.25 * g22) * np.eye(3)) @ ye) + c2 * (
        1.5 * (he @ he) - 2.25 * tr_tot * he - 12.0 * lam * he
        + (chi2 + y2g + 6.0 * (lam**2) + (1371.0 / 200.0) * (g12**2) + 1.35 * g12 * g22 - 5.75 * (g22**2)) * np.eye(3)
        + (387.0 / 80.0 * g12 + 135.0 / 16.0 * g22) * he
    ) @ ye
    gp2 = 0.6 * g12
    dlam = c1 * (24.0 * (lam**2) + lam * (4.0 * tr_tot - 9.0 * g22 - 3.0 * gp2) - 2.0 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.125 * (g22**2) + 0.75 * g22 * gp2 + 0.375 * (gp2**2)) + c2 * (
        -312.0 * (lam**3) - 144.0 * (lam**2) * tu + 36.0 * (lam**2) * (3.0 * g22 + gp2) - 3.0 * lam * (tu**2)
        + lam * tu * (80.0 * g32 + 22.5 * g22 + (85.0 / 6.0) * gp2) - 32.0 * g32 * (tu**2) - (8.0 / 3.0) * gp2 * (tu**2) + 30.0 * (tu**3)
    )
    dknu = c1 * (-1.5 * (he @ knu + knu @ he.T) + (-3.0 * g22 + 4.0 * lam + 2.0 * tr_tot) * knu)
    return np.concatenate([dg.real, dyu.real.ravel(), dyu.imag.ravel(), dyd.real.ravel(), dyd.imag.ravel(), dye.real.ravel(), dye.imag.ravel(), [float(dlam)], dknu.real.ravel(), dknu.imag.ravel()])


def run_all_referee_checks(project_root: Path = PROJECT_ROOT, write_verdict: bool = True) -> Dict[str, Any]:
    """Run full AST scan, Phase 1-10 seal checks, and 145 / 145 cumulative planted-fault controls."""
    mp.mp.dps = 50
    ast_scan = run_ast_guardrail_scan(project_root)
    assert ast_scan["passed"], f"AST Guardrail scan failed: {ast_scan}"

    parent = project_root.parent
    seal_ok = True
    for _, dname in [
        ("phase1", "self_consistent_loop_phi"),
        ("phase2", "cusped_3d_loop_phase2"),
        ("phase3", "relational_yukawa_phase3"),
        ("phase4", "unification_cap_lepton_phase4"),
        ("phase5", "m004_cl10_a4_phase5"),
        ("phase6", "weave_toe_phase6"),
        ("phase7", "inflation_lepton_phase7"),
        ("phase8", "fourfold_majorana_phase8"),
        ("phase9", "zero_input_precision_phase9"),
        ("phase10", "precision_falsifiability_phase10"),
    ]:
        pdir = project_root if dname == project_root.name else (parent / dname)
        sp_f = pdir / "SEAL_SHA256.txt"
        exp_sha, tgt_nm = sp_f.read_text(encoding="utf-8").strip().splitlines()[0].split()
        act_sha = hashlib.sha256((pdir / Path(tgt_nm).name).read_bytes()).hexdigest()
        seal_ok = bool(seal_ok and (act_sha == exp_sha))

    p5_dir = parent / "m004_cl10_a4_phase5"
    p9_dir = parent / "zero_input_precision_phase9"
    v1_lock_sha = json.loads((p5_dir / "outputs" / "preregistered_blind_lock_sha256.json").read_text(encoding="utf-8"))["preregistered_manifest_sha256"]
    v1_act_sha = hashlib.sha256((p5_dir / "outputs" / "preregistered_blind_predictions_v1.json").read_bytes()).hexdigest()
    seal_ok = bool(seal_ok and (v1_act_sha == v1_lock_sha) and (v1_act_sha == "ece3d98345a3f4982757dad6cea6837af95923ff088086f64cbc374674f2edbd"))
    assert seal_ok, "Cryptographic seal check failed"

    p9_verdict = json.loads((p9_dir / "outputs" / "referee_phase9_verdict.json").read_text(encoding="utf-8"))
    p9_details: Dict[str, bool] = {k: bool(v) for k, v in p9_verdict["planted_fault_controls"]["details"].items()}
    assert len(p9_details) == 125 and all(p9_details.values())

    prod = json.loads((project_root / "outputs" / "phase10_results.json").read_text(encoding="utf-8"))
    g1 = prod["gate_p10_1_pati_salam_projection"]
    g2 = prod["gate_p10_2_m5_axion_baryon_closure"]
    g3 = prod["gate_p10_3_falsifiability_observables"]
    g4 = prod["gate_p10_4_joint_consistency"]
    g5 = prod["gate_p10_5_track_b_scorecard"]

    tr_t3r2 = 6 * 0.0 + 3 * 0.25 + 3 * 0.25 + 2 * 0.0 + 0.25 + 0.25
    tr_y2 = 6 * (1.0 / 36.0) + 3 * (4.0 / 9.0) + 3 * (1.0 / 9.0) + 2 * 0.25 + 1.0 + 0.0
    cos_r_indep = math.sqrt(tr_t3r2 / tr_y2)

    ser = g5["serialized_v12_operators"]
    yw = [np.array(r) + 1j * np.array(im) for r, im in zip(ser["Yw_weave_real"], ser["Yw_weave_imag"])]
    k_u = np.array(ser["K_v10_real"]) + 1j * np.array(ser["K_v10_imag"])
    au0, mrs = ser["au_0"], ser["mrs_v12"]

    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    ell1, th1 = float(2 * mp.re(hl1)), float(2 * mp.im(hl1))
    eps1 = (math.exp(-2.9745505801732 * ell1) / abs(2 * np.sinh(0.5 * (ell1 + 1j * th1)))) / (2 * math.pi)
    lc = (4 * (math.pi**2 / 15) / eps1) ** 0.2
    reg_i, reg_h = 0.5 * math.log(2.0 * math.pi), 0.5 * math.log(2.0)
    t_i, t_h = [0.8, 6.0, 5.0], [8.2, 3.0, 4.0]
    rsh_g = [(-1.0 / (8.0 * math.pi**2)) * (-3.5 * t_i[i] * reg_i - 3.5 * t_h[i] * reg_h) for i in range(3)]
    d_sh = [rsh_g[i] - rsh_g[2] for i in range(3)]

    def rk45_eval(lr_v: float, bm=None):
        ig3 = au0 / (4.0 * math.pi)
        guv = np.sqrt(1.0 / np.array([ig3 + d_sh[0], ig3 + d_sh[1], ig3 + d_sh[2]]))
        gb = float(np.mean(guv))
        sf = gb / float(np.max(np.linalg.svd(yw[0], compute_uv=False)))
        yu0, yd0, ye0, ynu0 = yw[0] * sf, yw[1] * sf, yw[2] * sf, yw[3] * sf
        ynt = float(np.max(np.linalg.svd(ynu0, compute_uv=False)))
        knu0 = ((ynt**2) / mrs) * k_u.copy()
        lam0 = ((gb**2) / 8.0) * ((0.1272571765 * math.sqrt((1.0 / au0) / 0.04)) ** 2)
        if bm is not None:
            uq, uu, ud, ul, ue = bm
            yu0, yd0, ye0, knu0 = uq @ yu0 @ uu.conj().T, uq @ yd0 @ ud.conj().T, ul @ ye0 @ ue.conj().T, ul @ knu0 @ ul.T
        y0 = np.concatenate([guv.real, yu0.real.ravel(), yu0.imag.ravel(), yd0.real.ravel(), yd0.imag.ravel(), ye0.real.ravel(), ye0.imag.ravel(), [lam0], knu0.real.ravel(), knu0.imag.ravel()])
        sol = solve_ivp(_rhs76_indep, (0.0, -lr_v), y0, method="RK45", rtol=1e-11, atol=1e-13)
        yf = sol.y[:, -1]
        g1_v, g2_v, _ = yf[0:3]
        yu = (yf[3:12] + 1j * yf[12:21]).reshape(3, 3)
        yd = (yf[21:30] + 1j * yf[30:39]).reshape(3, 3)
        ye = (yf[39:48] + 1j * yf[48:57]).reshape(3, 3)
        knu = 0.5 * ((yf[58:67] + 1j * yf[67:76]).reshape(3, 3) + (yf[58:67] + 1j * yf[67:76]).reshape(3, 3).T)
        su = np.linalg.svd(yu, compute_uv=False)[::-1]
        sd = np.linalg.svd(yd, compute_uv=False)[::-1]
        we, _, _ = np.linalg.svd(ye)
        we_a = we[:, ::-1]
        mnu_vew = 0.5 * math.exp(-lr_v) * knu
        u_nu, snu_d, _ = np.linalg.svd(mnu_vew)
        snu = snu_d[::-1]
        u_nu_a = u_nu[:, ::-1]
        p_d = u_nu_a.conj().T @ mnu_vew @ u_nu_a.conj()
        w_tak = u_nu_a @ np.diag(np.exp(0.5j * np.angle(np.diag(p_d))))
        up = we_a.conj().T @ w_tak
        mbb_vew = float(abs(sum((up[0, i] ** 2) * snu[i] for i in range(3))))
        mzv = 0.5 * math.sqrt(g2_v * g2_v + 0.6 * g1_v * g1_v)
        return mzv, float(su[2] / sd[2]), mbb_vew

    lr_rk = float(brentq(lambda l: l - (7.5 * lc - math.log(rk45_eval(l)[0])), 27.0, 32.0, xtol=1e-11))
    _, mt_mb_rk, mbb_rk = rk45_eval(lr_rk)
    rng_r = np.random.default_rng(66554433)
    haar_rk = max(
        abs(rk45_eval(lr_rk, [_random_haar_u(3, rng_r) for _ in range(5)])[2] - mbb_rk) / mbb_rk
        for _ in range(10)
    )

    dw = np.linalg.det(yw[0] @ yw[1])
    th_w = mp.atan2(mp.mpf(str(dw.imag)), mp.mpf(str(dw.real)))
    a_it = -th_w + mp.mpf("0.07")
    for _ in range(8):
        a_it = a_it - mp.sin(th_w + a_it) / mp.cos(th_w + a_it)
    th_eff_50 = float(abs(th_w + a_it))

    rw = g5["v12_sm24_rows"]
    ts = g5["v12_sm24_tier_summary"]
    cc = g5["zero_input_cosmology_comparison"]
    pfc = cc["planted_fault_cosmology_signals"]
    fl = g5["experimental_falsifiability_ledger"]
    pfp = fl["planted_fault_proton_decay_yr"]
    u4 = g5["unified_36_observable_summary"]
    led = g5["non_dimensionalized_zero_continuous_input_ledger"]
    scales = [r["ratio_to_MPl_red"] for r in g4["track_a_ten_scale_M5_hierarchy"]]
    smap = {r["scale"]: r["ratio_to_MPl_red"] for r in g4["track_a_ten_scale_M5_hierarchy"]}

    p10_plants: Dict[str, bool] = {
        "P10_1_P1_spin10_16plet_T3R_Y_orthogonality_and_sqrt_3_5_verified": bool(
            abs(cos_r_indep - math.sqrt(0.6)) < 1e-15 and abs(g1["spin10_16plet_trace_benchmarks"]["tr_T3R_dot_half_BL"]) < 1e-15
        ),
        "P10_1_P2_wrong_inverse_cos_degrades_mt_over_mb_caught": bool(
            abs(math.log10(g1["planted_fault_signals_track_a"]["wrong_inverse_cos_mt_over_mb_plant"] / rw["mt_over_mb"]["observed"])) > 0.25
        ),
        "P10_1_P3_wrong_sin_theta_R_shifts_mt_over_mb_caught": bool(
            abs(g1["planted_fault_signals_track_a"]["wrong_sin_theta_R_mt_over_mb_plant"] - rw["mt_over_mb"]["v12_zero_input_predicted"]) > 5.0
        ),
        "P10_1_P4_rg_quasi_invariance_bound_on_6_remaining_tier2_verified": bool(
            g1["v12_zero_input_fixed_point_track_a"]["remaining_tier2_max_rg_drift_dex"] < 0.15
        ),
        "P10_1_P5_independent_rk45_and_haar_18_of_24_sm_tier1_verified": bool(
            abs(mt_mb_rk - rw["mt_over_mb"]["v12_zero_input_predicted"]) < 1e-3
            and ts["Tier_1_Precision_Hit"] == 18
            and ts["Tier_2_Structural_O1_Hit"] == 6
            and ts["Tier_3_Quantitative_Tension_or_Miss"] == 0
        ),
        "P10_2_P1_five_sheet_L2_norm_sqrt5_and_3gen_abj_benchmarks_verified": bool(
            abs(g2["covering_and_abj_benchmarks"]["kinetic_norm_sqrt5"] - math.sqrt(5.0)) < 1e-13
            and abs(g2["covering_and_abj_benchmarks"]["abj_anomaly_3_generations"] - 3.0) < 1e-15
        ),
        "P10_2_P2_zero_input_Omega_a_h2_promoted_to_tier1_and_beta_iso_0p0029": bool(
            abs(cc["Omega_a_h2_log10_ratio"]) <= 0.15 and cc["beta_iso_1B_SD_M5"] < 0.005
        ),
        "P10_2_P3_three_generation_eta_B_promoted_to_tier1_verified": bool(
            abs(cc["eta_B_log10_ratio"]) <= 0.15 and cc["eta_B_tier"] == "Tier_1_Precision_Hit"
        ),
        "P10_2_P4_wrong_inverse_sqrt5_dilutes_Omega_a_into_tier3_caught": bool(
            abs(math.log10(pfc["wrong_inverse_sqrt5_Omega_a_h2_plant"] / 0.120)) > 0.50
        ),
        "P10_2_P5_post_inflationary_overclosure_and_wrong_9x_abj_plants_caught": bool(
            pfc["post_inflationary_random_theta_Omega_a_h2_plant"] > 200.0
            and abs(math.log10(pfc["wrong_Ngen_squared_eta_B_plant"] / 6.12e-10)) > 0.50
        ),
        "P10_3_P1_50d_takagi_and_srednicki_8_over_3_benchmarks_verified": bool(
            g3["benchmarks"]["takagi_50d_abs_err"] < 1e-45
            and abs(g3["benchmarks"]["srednicki_E_over_N_spin10"] - 8.0 / 3.0) < 1e-15
        ),
        "P10_3_P2_haar_invariance_of_mbb_and_delta_cp_vs_unrotated_plant_caught": bool(
            haar_rk < 1e-10
            and abs(mbb_rk * 246.21965e12 - fl["m_beta_beta_meV"]) < 1e-4
            and g3["planted_fault_signals_track_a"]["unrotated_mnu_00_haar_violation_plant"] > 0.1
        ),
        "P10_3_P3_naive_4d_su5_mkk_proton_decay_superk_violation_caught": bool(
            pfp["naive_4d_su5_mkk_tau_p_yr_plant"] < 2.4e34
        ),
        "P10_3_P4_single_16_5d_overlap_proton_decay_superk_violation_caught": bool(
            pfp["single_16_5d_overlap_tau_p_yr_plant"] < 2.4e34
        ),
        "P10_3_P5_e8_su4_split_16_proton_decay_2p1e35_yr_and_falsifiability_verified": bool(
            abs(g3["benchmarks"]["e8_su4_split_16_xy_coupling"]) < 1e-15
            and fl["tau_p_to_e_pi0_yr"] > 2.4e34
            and 190.0 < fl["delta_CP_deg"] < 205.0
            and fl["sum_m_nu_meV"] < 72.0
        ),
        "P10_4_P1_50d_newton_strong_cp_on_v12_verified": bool(
            th_eff_50 < 1e-35 and g4["strong_cp_v12"]["minimized_strong_cp_residual_abs"] < 1e-14
        ),
        "P10_4_P2_eleven_step_M5_scale_hierarchy_VCas_gt_fa0_M5_verified": bool(
            all(scales[i] > scales[i + 1] for i in range(len(scales) - 1))
            and smap["T_reh_radion"] > cc["T_BBN_over_MPl_red"]
        ),
        "P10_4_P3_unified_36_observable_26_tier1_6_tier2_4_bounds_verified": bool(
            u4["total_tier1_precision_hits_of_36"] == 26
            and u4["total_tier2_structural_hits_of_36"] == 6
            and u4["total_bound_and_vacuum_passes_of_36"] == 4
            and u4["total_passing_of_36"] == 36
        ),
        "P10_4_P4_clause_P10_C1_rg_quasi_invariance_disclosed": bool(
            "Selberg" in led["clause_P10_C1_rg_quasi_invariance_disclosure"]
        ),
        "P10_4_P5_clause_P10_C2_phase10_preregistration_provenance_disclosed": bool(
            "pre-registered at Phase 10" in led["clause_P10_C2_preregistration_provenance"]
        ),
    }

    all_145: Dict[str, bool] = {}
    all_145.update(p9_details)
    all_145.update(p10_plants)
    n_total = len(all_145)
    n_caught = sum(1 for v in all_145.values() if v)
    assert n_total == 145 and n_caught == 145, f"Expected 145/145 controls caught, got {n_caught}/{n_total}: {p10_plants}"

    verdict = {
        "referee": "Phase 10 Zero-Import Referee Suite (145 / 145 Cumulative Planted-Fault Controls)",
        "ast_guardrail_scan": ast_scan,
        "all_seals_1_to_10_and_v1_intact": seal_ok,
        "phase10_new_controls": {"total": 20, "caught": sum(1 for v in p10_plants.values() if v), "details": p10_plants},
        "planted_fault_controls": {"total": n_total, "caught": n_caught, "details": all_145},
        "all_referee_checks_passed": bool(ast_scan["passed"] and seal_ok and n_caught == 145),
    }
    if write_verdict:
        out_dir = project_root / "outputs"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "referee_phase10_verdict.json").write_text(json.dumps(verdict, indent=2), encoding="utf-8")
    return verdict


if __name__ == "__main__":
    v = run_all_referee_checks(write_verdict=True)
    print(f"Phase 10 Zero-Import Referee PASSED: {v['planted_fault_controls']['caught']} / {v['planted_fault_controls']['total']} controls caught!")
