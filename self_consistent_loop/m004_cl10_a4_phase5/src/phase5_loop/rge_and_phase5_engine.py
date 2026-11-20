"""Gate P5-4 (Track A, 0 of 19) & Phase 5 Composite Engine:
Literature RGE Benchmark Gates (Pendleton-Ross, Machacek-Vaughn, ADKLR, Contino-Pilo),
Spin(11) Z_2 x Z_2' Orbifold Thresholds, Clause N6 QCD Confinement Pole, Clause N12 Amphicheiral CP Zero,
Phase 1-5 Seal Verifier, and Track-B Scorecard Runner."""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

from .clifford_hosotani_collar import run_gate_p5_2_clifford_hosotani_collar
from .geometry_and_selection import run_gate_p5_1_geometry
from .gravity_radion_and_warping import run_gate_p5_3_gravity_radion
from .track_b_unblinded_scorecard import run_track_b_v1_vs_v7_scorecard

mp.mp.dps = 50
PROJECT_ROOT = Path(__file__).resolve().parents[2]

PHASE_DIRS = (
    ("phase1", "self_consistent_loop_phi"),
    ("phase2", "cusped_3d_loop_phase2"),
    ("phase3", "relational_yukawa_phase3"),
    ("phase4", "unification_cap_lepton_phase4"),
    ("phase5", "m004_cl10_a4_phase5"),
)


def _verify_single_seal(phase_dir: Path) -> Dict[str, Any]:
    seal_path = phase_dir / "SEAL_SHA256.txt"
    if not seal_path.exists():
        return {"directory": phase_dir.name, "present": False, "seal_intact": False}
    parts = seal_path.read_text(encoding="utf-8").strip().splitlines()[0].split()
    expected_sha, target_name = parts[0].strip(), parts[1].strip()
    target_path = phase_dir / Path(target_name).name
    actual_sha = hashlib.sha256(target_path.read_bytes()).hexdigest()
    return {
        "directory": phase_dir.name,
        "preregistration_file": target_path.name,
        "present": True,
        "expected_sha256": expected_sha,
        "actual_sha256": actual_sha,
        "seal_intact": bool(actual_sha == expected_sha),
    }


def verify_all_phase5_seals(project_root: Path = PROJECT_ROOT) -> Dict[str, Any]:
    """Verify Phase 1-5 SEAL_SHA256.txt files plus Track-A v1 blind prediction SHA-256 lock."""
    parent = project_root.parent
    records: Dict[str, Any] = {}
    all_intact = True
    for key, dirname in PHASE_DIRS:
        pdir = project_root if dirname == project_root.name else (parent / dirname)
        if pdir.exists():
            rec = _verify_single_seal(pdir)
            records[key] = rec
            if not rec["seal_intact"]:
                all_intact = False
        elif key == "phase5":
            all_intact = False

    v1_json = project_root / "outputs" / "preregistered_blind_predictions_v1.json"
    v1_lock = project_root / "outputs" / "preregistered_blind_lock_sha256.json"
    v1_intact = False
    v1_actual = ""
    v1_expected = ""
    if v1_json.exists() and v1_lock.exists():
        v1_expected = json.loads(v1_lock.read_text(encoding="utf-8"))["preregistered_manifest_sha256"]
        v1_actual = hashlib.sha256(v1_json.read_bytes()).hexdigest()
        v1_intact = bool(v1_actual == v1_expected)
    all_intact = bool(all_intact and v1_intact)

    return {
        "phases": records,
        "track_a_v1_predictions_sha256": {
            "expected": v1_expected,
            "actual": v1_actual,
            "v1_lock_intact": v1_intact,
        },
        "all_seals_intact": all_intact,
    }


def pack76(g, Yu, Yd, Ye, lam, knu) -> np.ndarray:
    return np.concatenate([g.real, Yu.real.ravel(), Yu.imag.ravel(), Yd.real.ravel(), Yd.imag.ravel(), Ye.real.ravel(), Ye.imag.ravel(), [float(lam)], knu.real.ravel(), knu.imag.ravel()])


def unpack76(y):
    return (
        y[0:3],
        (y[3:12] + 1j * y[12:21]).reshape(3, 3),
        (y[21:30] + 1j * y[30:39]).reshape(3, 3),
        (y[39:48] + 1j * y[48:57]).reshape(3, 3),
        float(y[57]),
        (y[58:67] + 1j * y[67:76]).reshape(3, 3),
    )


def rhs76(t: float, y: np.ndarray) -> np.ndarray:
    g, Yu, Yd, Ye, lam, knu = unpack76(y)
    g1, g2, g3 = g
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3
    c1 = 1.0 / (16.0 * math.pi * math.pi)
    c2 = c1 * c1
    Hu, Hd, He = Yu @ Yu.conj().T, Yd @ Yd.conj().T, Ye @ Ye.conj().T
    tu, td, te = float(np.real(np.trace(Hu))), float(np.real(np.trace(Hd))), float(np.real(np.trace(He)))
    T = 3.0 * tu + 3.0 * td + te

    B2 = np.array([[3.98, 2.7, 8.8], [0.9, 35.0 / 6.0, 12.0], [1.1, 4.5, -26.0]])
    Cy = np.array([[1.7, 0.5, 1.5], [1.5, 1.5, 0.5], [2.0, 2.0, 0.0]])
    dg = c1 * np.array([4.1, -19.0 / 6.0, -7.0]) * (g**3) + c2 * (g**3) * (B2 @ np.array([g12, g22, g32]) - Cy @ np.array([tu, td, te]))

    tu2, td2, te2, tud = float(np.real(np.trace(Hu @ Hu))), float(np.real(np.trace(Hd @ Hd))), float(np.real(np.trace(He @ He))), float(np.real(np.trace(Hu @ Hd)))
    chi2 = -2.25 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.5 * tud
    y2g = ((85.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * tu + ((25.0 / 24.0) * g12 + (45.0 / 8.0) * g22 + 20.0 * g32) * td + ((75.0 / 8.0) * g12 + (15.0 / 8.0) * g22) * te

    dYu = c1 * ((1.5 * (Hu - Hd) + (T - 0.85 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ Yu) + c2 * (
        1.5 * (Hu @ Hu) - Hu @ Hd - 0.25 * (Hd @ Hu) + 2.75 * (Hd @ Hd) - 2.25 * T * Hu - 12.0 * lam * Hu
        + (chi2 + y2g + 6.0 * (lam**2) + (1187.0 / 600.0) * (g12**2) - 0.45 * g12 * g22 + (19.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (223.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * Hu - (43.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * Hd
    ) @ Yu
    dYd = c1 * ((1.5 * (Hd - Hu) + (T - 0.25 * g12 - 2.25 * g22 - 8.0 * g32) * np.eye(3)) @ Yd) + c2 * (
        1.5 * (Hd @ Hd) - Hd @ Hu - 0.25 * (Hu @ Hd) + 2.75 * (Hu @ Hu) - 2.25 * T * Hd - 12.0 * lam * Hd
        + (chi2 + y2g + 6.0 * (lam**2) - (127.0 / 600.0) * (g12**2) - 1.35 * g12 * g22 + (31.0 / 15.0) * g12 * g32 - 5.75 * (g22**2) + 9.0 * g22 * g32 - 108.0 * (g32**2)) * np.eye(3)
        + (187.0 / 80.0 * g12 + 135.0 / 16.0 * g22 + 16.0 * g32) * Hd - (79.0 / 80.0 * g12 - 9.0 / 16.0 * g22 + 16.0 * g32) * Hu
    ) @ Yd
    dYe = c1 * ((1.5 * He + (T - 2.25 * g12 - 2.25 * g22) * np.eye(3)) @ Ye) + c2 * (
        1.5 * (He @ He) - 2.25 * T * He - 12.0 * lam * He
        + (chi2 + y2g + 6.0 * (lam**2) + (1371.0 / 200.0) * (g12**2) + 1.35 * g12 * g22 - 5.75 * (g22**2)) * np.eye(3)
        + (387.0 / 80.0 * g12 + 135.0 / 16.0 * g22) * He
    ) @ Ye

    gp2 = 0.6 * g12
    dlam = c1 * (24.0 * (lam**2) + lam * (4.0 * T - 9.0 * g22 - 3.0 * gp2) - 2.0 * (3.0 * tu2 + 3.0 * td2 + te2) + 1.125 * (g22**2) + 0.75 * g22 * gp2 + 0.375 * (gp2**2)) + c2 * (
        -312.0 * (lam**3) - 144.0 * (lam**2) * tu + 36.0 * (lam**2) * (3.0 * g22 + gp2) - 3.0 * lam * (tu**2) + lam * tu * (80.0 * g32 + 22.5 * g22 + (85.0 / 6.0) * gp2) - 32.0 * g32 * (tu**2) - (8.0 / 3.0) * gp2 * (tu**2) + 30.0 * (tu**3)
    )
    dknu = c1 * (-1.5 * (He @ knu + knu @ He.T) + (-3.0 * g22 + 4.0 * lam + 2.0 * T) * knu)
    return pack76(dg, dYu, dYd, dYe, dlam, dknu)


def run_gate_p5_4_rge_benchmarks_and_clauses(eps1_val: float) -> Dict[str, Any]:
    """Run Guardrail 4 RGE benchmark gates, Spin(11) Z_2xZ_2' Dynkin indices, Clause N6, and Clause N12."""
    c1 = 1.0 / (16.0 * math.pi * math.pi)
    c2 = c1 * c1

    # 1. Pendleton-Ross (1981) 1-loop QCD + top analytical trajectory benchmark:
    g3_0, yt_0 = 0.6, 0.5
    sol_pr = solve_ivp(
        lambda t, u: np.array([-7.0 * c1 * (u[0] ** 3), c1 * (4.5 * (u[1] ** 3) - 8.0 * (u[0] ** 2) * u[1])]),
        (0.0, -25.0),
        np.array([g3_0, yt_0]),
        method="DOP853",
        rtol=1e-13,
        atol=1e-15,
    )
    g3_f, yt_f = float(sol_pr.y[0, -1]), float(sol_pr.y[1, -1])
    rho0 = (yt_0**2) / (g3_0**2)
    rx = (g3_f**2) / (g3_0**2)
    rho_exact = (2.0 / 9.0) / (1.0 + ((2.0 / (9.0 * rho0)) - 1.0) * (rx ** (-1.0 / 7.0)))
    pr_err = abs((yt_f**2) / (g3_f**2) - rho_exact)

    # 2. Machacek-Vaughn 2-loop pure SU(3) analytical integral benchmark (da/dt = -(7/(8*pi^2)) a^2 - (26/(128*pi^4)) a^3):
    sol_mv = solve_ivp(lambda t, u: np.array([-7.0 * c1 * (u[0] ** 3) - 26.0 * c2 * (u[0] ** 5)]), (0.0, -20.0), np.array([0.55]), method="DOP853", rtol=1e-13, atol=1e-15)
    a_uv, a_ir = mp.mpf("0.55") ** 2, mp.mpf(str(float(sol_mv.y[0, -1]))) ** 2
    r_b = mp.mpf(26) / (112 * (mp.pi**2))
    lhs_mv = (8 * (mp.pi**2) / 7) * ((1 / a_ir - 1 / a_uv) - r_b * mp.log(((1 / a_ir) + r_b) / ((1 / a_uv) + r_b)))
    mv_err = float(abs(lhs_mv - (-20))) / 20.0

    # 3. ADKLR (2001) Weinberg operator Ellis-Lola analytical integral benchmark:
    rng = np.random.default_rng(50505)
    z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2.0)
    U, _ = np.linalg.qr(z)
    Ye_b = U @ np.diag([0.05, 0.2, 0.8])
    knu_0 = U @ np.array([[1.0, 0.3, 0.1], [0.3, 0.5, 0.2], [0.1, 0.2, 0.2]], dtype=complex) @ U.T
    He_b = Ye_b @ Ye_b.conj().T
    def rhs_adklr(t, u):
        K = (u[:9] + 1j * u[9:]).reshape(3, 3)
        dK = c1 * (-1.5 * (He_b @ K + K @ He_b.T))
        return np.concatenate([dK.real.ravel(), dK.imag.ravel()])

    sol_w = solve_ivp(rhs_adklr, (0.0, -10.0), np.concatenate([knu_0.real.ravel(), knu_0.imag.ravel()]), method="DOP853", rtol=1e-13, atol=1e-15)
    knu_num = (sol_w.y[:9, -1] + 1j * sol_w.y[9:, -1]).reshape(3, 3)
    E_diag = U @ np.diag([math.exp(15.0 * c1 * (y**2)) for y in [0.05, 0.2, 0.8]]) @ U.conj().T
    knu_ex = E_diag @ knu_0 @ E_diag.T
    adklr_err = float(np.max(np.abs(knu_num - knu_ex)))

    # 4. Contino-Pilo orbifold Hurwitz-zeta 50-digit benchmark (-1/2 d/ds [2^{-2s} zeta(2s)]|_{s=0} == +1/2 ln(pi)):
    zeta_sum = -mp.diff(lambda s: (2 ** (-2 * s)) * mp.zeta(2 * s), mp.mpf(0))
    cp_err = float(abs(0.5 * zeta_sum - 0.5 * mp.log(mp.pi)))

    # 5. Spin(11) Z_2 x Z_2' Dynkin split from explicit 32x32 matrices:
    cd, ca = [], []
    for a in range(5):
        Md = np.zeros((32, 32), dtype=complex)
        for m in range(32):
            if ((m >> a) & 1) == 0:
                lower = bin(m & ((1 << a) - 1)).count("1")
                Md[m | (1 << a), m] = -1.0 if (lower % 2 == 1) else 1.0
        cd.append(Md)
        ca.append(Md.conj().T)
    gammas = []
    for a in range(5):
        gammas.append(ca[a] + cd[a])
        gammas.append(-1j * (ca[a] - cd[a]))

    def n4(M):
        return M / math.sqrt(float(np.real(np.trace(M @ M))) / 4.0)

    Yop = n4((-1.0 / 3.0) * sum(cd[i] @ ca[i] for i in range(3)) + 0.5 * sum(cd[j] @ ca[j] for j in [3, 4]))
    W3 = n4(cd[3] @ ca[3] - cd[4] @ ca[4])
    G3 = n4(cd[0] @ ca[0] - cd[1] @ ca[1])
    probes = [Yop, W3, G3]

    int_gens, half_gens = [], []
    for a in range(5):
        int_gens.append(n4(cd[a] @ ca[a] - 0.5 * np.eye(32)))
    for a in range(5):
        for b in range(a + 1, 5):
            same = (a < 3) == (b < 3)
            u_re, u_im = n4(cd[a] @ ca[b] + cd[b] @ ca[a]), n4(-1j * (cd[a] @ ca[b] - cd[b] @ ca[a]))
            p_re, p_im = n4(cd[a] @ cd[b] + ca[b] @ ca[a]), n4(-1j * (cd[a] @ cd[b] - ca[b] @ ca[a]))
            if same:
                int_gens += [u_re, u_im]
                half_gens += [p_re, p_im]
            else:
                half_gens += [u_re, u_im]
                int_gens += [p_re, p_im]
    for idx in range(10):
        g_m = n4(gammas[idx])
        # gamma_A has J_5 odd (-), P_5 = + on 0..5, - on 6..9 => J_5*P_5 = + on 6..9 (4 doublet modes!), - on 0..5 (6 triplet modes!)
        if idx >= 6:
            int_gens.append(g_m)
        else:
            half_gens.append(g_m)

    def dynkin_idx(gen_list, P):
        return sum(float(np.real(np.trace((P @ G - G @ P).conj().T @ (P @ G - G @ P)))) / 4.0 for G in gen_list)

    T_int = [round(dynkin_idx(int_gens, P), 10) for P in probes]
    T_half = [round(dynkin_idx(half_gens, P), 10) for P in probes]

    # 6. Clause N6: Selberg identification g_GUT^2 / (16*pi^2) == eps_1 (alpha_GUT^-1 = 24.0861) hits 2-loop QCD pole before 21 e-folds:
    g_sel = 4.0 * math.pi * math.sqrt(eps1_val)

    def pole_ev(t, y):
        return y[2] - 5.0

    pole_ev.terminal = True
    sol_pole = solve_ivp(
        rhs76,
        (0.0, -28.0),
        pack76(np.array([g_sel, g_sel, g_sel]), np.diag([0.0, 0.0, g_sel]).astype(complex), np.zeros((3, 3), dtype=complex), np.zeros((3, 3), dtype=complex), 0.001, np.zeros((3, 3), dtype=complex)),
        method="DOP853",
        events=pole_ev,
        rtol=1e-10,
        atol=1e-12,
    )
    pole_efolds = abs(float(sol_pole.t_events[0][0]))

    # 7. Clause N12: 50-digit amphicheiral m004 Shell-1 Weyl CP vanishing (det[Hu, Hd] == 0):
    omega = mp.exp(2j * mp.pi / 3)
    hl1 = mp.acosh((mp.mpf(2) + omega) / 2)
    l1, th1 = 2 * mp.re(hl1), 2 * mp.im(hl1)
    eps1_mp = mp.mpf(str(eps1_val))
    Lc = (4 * (mp.pi**2 / 15) / eps1_mp) ** mp.mpf("0.2")
    cp_m = mp.sqrt(2 * Lc / (1 - mp.exp(-2 * Lc)))
    cm_m = mp.sqrt(2 * Lc / (mp.exp(2 * Lc) - 1))
    bs_m = mp.sqrt(2 * mp.tanh(Lc / 2) / Lc)
    C3T_m = mp.matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    Xh_m = mp.diag([1, -1, -1])
    M_Ab_m = (C3T_m.T) * (Xh_m * C3T_m)
    M_ABab_m = (C3T_m.T) * ((C3T_m.T) * Xh_m) * C3T_m * (Xh_m * C3T_m)
    z5_m = mp.exp(2j * mp.pi / 5)
    v0_m = mp.matrix([1, 1, 1]) / mp.sqrt(3)
    Ws1_m = mp.exp(0.5j * th1) * z5_m * M_Ab_m + mp.exp(-0.5j * th1) * (z5_m**4) * M_ABab_m

    def outer_mp(a, b):
        R = mp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                R[i, j] = a[i] * mp.conj(b[j])
        return R

    def dag_mp(M):
        R = mp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                R[i, j] = mp.conj(M[j, i])
        return R

    def b_amp(cR, wR):
        w_lp = cR + bs_m
        TL, TR = Ws1_m, wR * Ws1_m
        return cR * outer_mp(v0_m, v0_m) + w_lp * eps1_mp * outer_mp(TL * v0_m, TR * v0_m) + (mp.mpf(1) / 3) * w_lp * eps1_mp * (outer_mp(TL * v0_m, v0_m) + outer_mp(v0_m, TR * v0_m))

    Yu_m, Yd_m = b_amp(cp_m, mp.mpf(8) / mp.mpf("10.5")), b_amp(cm_m, mp.mpf(7) / mp.mpf("10.5"))
    C_m = (Yu_m * dag_mp(Yu_m)) * (Yd_m * dag_mp(Yd_m)) - (Yd_m * dag_mp(Yd_m)) * (Yu_m * dag_mp(Yu_m))
    det_C_m = C_m[0, 0] * (C_m[1, 1] * C_m[2, 2] - C_m[1, 2] * C_m[2, 1]) - C_m[0, 1] * (C_m[1, 0] * C_m[2, 2] - C_m[1, 2] * C_m[2, 0]) + C_m[0, 2] * (C_m[1, 0] * C_m[2, 1] - C_m[1, 1] * C_m[2, 0])
    clause_n12_det_zero = float(abs(det_C_m))

    passed = bool(
        pr_err < 1e-13
        and mv_err < 1e-13
        and adklr_err < 1e-13
        and cp_err < 1e-45
        and T_int == [0.8, 6.0, 5.0]
        and T_half == [8.2, 3.0, 4.0]
        and 19.0 < pole_efolds < 22.0
        and clause_n12_det_zero < 1e-48
    )

    return {
        "gate_p5_4_passed": passed,
        "pendleton_ross_err": pr_err,
        "machacek_vaughn_2loop_err": mv_err,
        "adklr_weinberg_err": adklr_err,
        "contino_pilo_50d_err": cp_err,
        "spin11_dynkin_T_int": T_int,
        "spin11_dynkin_T_half": T_half,
        "clause_N6_selberg_qcd_pole_efolds": pole_efolds,
        "clause_N12_amphicheiral_det_commutator_50d": clause_n12_det_zero,
    }


def run_phase5_engine(write_output: bool = True) -> Dict[str, Any]:
    """Run all Phase 5 Track-A (0-of-19) gates and Track-B unblinded v1-vs-v7 scorecard."""
    seals = verify_all_phase5_seals(PROJECT_ROOT)
    if not seals["all_seals_intact"]:
        raise RuntimeError(f"Phase 5 SHA-256 seal check failed: {seals}")

    g1 = run_gate_p5_1_geometry()
    g2 = run_gate_p5_2_clifford_hosotani_collar(g1["eps_1"])
    g3 = run_gate_p5_3_gravity_radion(g1["vol_m5_cover"])
    g4 = run_gate_p5_4_rge_benchmarks_and_clauses(g1["eps_1"])
    g5 = run_track_b_v1_vs_v7_scorecard(PROJECT_ROOT, pack76, unpack76, rhs76)

    all_passed = bool(
        seals["all_seals_intact"]
        and g1["gate_p5_1_passed"]
        and g2["gate_p5_2_passed"]
        and g3["gate_p5_3_passed"]
        and g4["gate_p5_4_passed"]
        and g5["gate_p5_5_passed"]
    )

    payload = {
        "phase": "Phase 5: m004 x Cl(10) x A_4 Flavour, Spin(11) Hosotani/Collar, 7D Radion, & 2-Loop RGE Closure",
        "track_a_empirical_inputs_used": "0 of 19",
        "track_b_calibrated_macro_anchors": ["alpha_em_inv_MZ_MSbar", "alpha_3_MZ_MSbar"],
        "track_b_free_yukawa_mixing_higgs_seesaw_parameters": 0,
        "all_phase5_gates_passed": all_passed,
        "seal_verification": seals,
        "gate_p5_1_geometry": g1,
        "gate_p5_2_clifford_hosotani_collar": g2,
        "gate_p5_3_gravity_radion": g3,
        "gate_p5_4_rge_benchmarks_and_clauses": g4,
        "gate_p5_5_track_b_v1_vs_v7_scorecard": g5,
    }

    if write_output:
        out_path = PROJECT_ROOT / "outputs" / "phase5_results.json"
        out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    return payload


if __name__ == "__main__":
    res = run_phase5_engine(write_output=True)
    print("Phase 5 all_phase5_gates_passed:", res["all_phase5_gates_passed"])
    print("Track-B v1 Tier Summary:", res["gate_p5_5_track_b_v1_vs_v7_scorecard"]["v1_tier_summary"])
    print("Track-B v7 Tier Summary:", res["gate_p5_5_track_b_v1_vs_v7_scorecard"]["v7_tier_summary"])
    if not res["all_phase5_gates_passed"]:
        sys.exit(1)
