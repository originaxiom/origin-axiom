"""Gate P5-2 (Track A, 0 of 19): Spin(11) Kawamura 0-Triplet Projection, Non-Abelian GHU Triangle,
Spin(10) 6.591x Cartan Interference, 50-Digit Hosotani EW Minimum, & UV-IR Collar Mirror Duality."""

from __future__ import annotations

import math
from typing import Any, Dict

import mpmath as mp
import numpy as np

mp.mp.dps = 50


def run_gate_p5_2_clifford_hosotani_collar(eps1_val: float) -> Dict[str, Any]:
    """Verify Spin(11) Kawamura projection, GHU triangle algebra, Hosotani root, and UV-IR collar duality."""
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

    # Spin(11) Lie closure:
    closure_err = 0.0
    for i in range(10):
        for j in range(i + 1, 10):
            TA, TB = 0.5 * gammas[i], 0.5 * gammas[j]
            Sig = -0.25j * (gammas[i] @ gammas[j] - gammas[j] @ gammas[i])
            closure_err = max(closure_err, float(np.max(np.abs((TA @ TB - TB @ TA) - 1j * Sig))))

    # Kawamura P_5-odd doublet-triplet projection:
    F_P5 = np.diag([-1.0 if (((m >> 3) & 1) + ((m >> 4) & 1)) % 2 == 1 else 1.0 for m in range(32)])
    triplet_norm = max(float(np.linalg.norm(0.5 * (gammas[idx] - F_P5 @ gammas[idx] @ F_P5))) for idx in range(6))
    doublet_err = max(float(np.linalg.norm(0.5 * (gammas[idx] + F_P5 @ gammas[idx] @ F_P5))) for idx in range(6, 10))

    # 12x12 SM gauge boson mass matrix at H_vev = (1/2) gamma_9:
    def norm4(M):
        return M / math.sqrt(float(np.real(np.trace(M @ M))) / 4.0)

    sm_gens = []
    gluons = []
    for i in range(3):
        for j in range(i + 1, 3):
            g_re = norm4(cd[i] @ ca[j] + cd[j] @ ca[i])
            g_im = norm4(-1j * (cd[i] @ ca[j] - cd[j] @ ca[i]))
            gluons += [g_re, g_im]
            sm_gens += [g_re, g_im]
    g3 = norm4(cd[0] @ ca[0] - cd[1] @ ca[1])
    g8 = norm4(cd[0] @ ca[0] + cd[1] @ ca[1] - 2.0 * cd[2] @ ca[2])
    gluons += [g3, g8]
    sm_gens += [g3, g8]

    su2L = [
        norm4(cd[3] @ ca[4] + cd[4] @ ca[3]),
        norm4(-1j * (cd[3] @ ca[4] - cd[4] @ ca[3])),
        norm4(cd[3] @ ca[3] - cd[4] @ ca[4]),
    ]
    Yop = (-1.0 / 3.0) * (cd[0] @ ca[0] + cd[1] @ ca[1] + cd[2] @ ca[2]) + 0.5 * (cd[3] @ ca[3] + cd[4] @ ca[4])
    sm_gens += su2L + [norm4(Yop)]

    H_vev = 0.5 * gammas[8]
    M2 = np.zeros((12, 12))
    for a_i, Ta in enumerate(sm_gens):
        ca_m = Ta @ H_vev - H_vev @ Ta
        for b_i, Tb in enumerate(sm_gens):
            cb_m = Tb @ H_vev - H_vev @ Tb
            M2[a_i, b_i] = float(np.real(np.trace(ca_m.conj().T @ cb_m))) / 4.0
    ev = np.sort(np.linalg.eigvalsh(M2))
    n_massless = int(np.sum(np.abs(ev) < 1e-13))
    sin2_tw_tree = 1.0 - float(ev[-3] / ev[-1])

    # Non-abelian GHU triangle commutator checks:
    T3L = 0.5 * (cd[3] @ ca[3] - cd[4] @ ca[4])
    Qem = T3L + Yop
    qem_comm_err = float(np.max(np.abs(Qem @ H_vev - H_vev @ Qem)))
    gluon_comm_norm = max(float(np.linalg.norm(G @ H_vev - H_vev @ G)) for G in gluons)
    tr_d = H_vev[1, 17]
    su2_fhL_down = float(np.real((sum((H_vev @ T - T @ H_vev) @ T for T in su2L)[1, 17]) / tr_d))
    su2_ff_down = float(np.real((sum(T @ H_vev @ T for T in su2L)[1, 17]) / tr_d))

    # Spin(10) Cartan dipole constructive/destructive interference ratio:
    N_tot = sum(cd[a] @ ca[a] for a in range(5))
    QX5 = (2.0 * N_tot - 5.0 * np.eye(32)) / 5.0
    gY = math.sqrt(0.6)
    qd_Q = float(np.real(QX5[17, 17])) - 0.2 + gY * (float(np.real(Yop[17, 17])) - 0.25)
    qd_dc = float(np.real(QX5[27, 27])) - 0.2 + gY * (float(np.real(Yop[27, 27])) - 0.25)
    qe_L = float(np.real(QX5[23, 23])) - 0.2 + gY * (float(np.real(Yop[23, 23])) - 0.25)
    qe_ec = float(np.real(QX5[24, 24])) - 0.2 + gY * (float(np.real(Yop[24, 24])) - 0.25)
    cartan_ratio = abs(qd_Q * qd_dc) / abs(qe_L * qe_ec)
    exact_cartan_ratio = ((24.0 + math.sqrt(15.0)) / (9.0 * math.sqrt(15.0) - 24.0)) ** 2

    # P-540 orbifold-oddness of T_{3R} = (3/5) Y + (1/10) Q_X:
    T_3R = 0.6 * Yop + 0.5 * QX5
    B_plus = gammas[1] @ gammas[3] @ gammas[5] @ gammas[7] @ gammas[9]
    t3r_orbifold_odd_err = float(np.max(np.abs(T_3R.T @ B_plus + B_plus @ T_3R)))

    # 50-digit 1-loop Hosotani effective potential minimum (Stage B2a):
    def cl_cos5(x):
        return mp.re(mp.polylog(5, mp.exp(1j * x)))

    def cl_sin4(x):
        return mp.im(mp.polylog(4, mp.exp(1j * x)))

    def dV_hosotani(th):
        # d/d(th) [-9 Li5(cos th) - 18 Li5(-cos th) + 16 Li5(cos(th/2))]:
        return 9 * cl_sin4(th) + 18 * cl_sin4(th + mp.pi) - 8 * cl_sin4(th / 2)

    theta_H_star = mp.findroot(dV_hosotani, mp.mpf("3.12"))
    h_step = mp.mpf("1e-20")
    d2V_hosotani = float((dV_hosotani(theta_H_star + h_step) - dV_hosotani(theta_H_star - h_step)) / (2 * h_step))

    # Flat-bundle 1-loop collar L_c* & 50-digit UV-IR mirror duality:
    eps1_mp = mp.mpf(str(eps1_val))
    Lc_star = (4 * (mp.pi**2 / 15) / eps1_mp) ** mp.mpf("0.2")
    psi_p_UV = mp.sqrt(2 * Lc_star / (mp.exp(2 * Lc_star) - 1)) * mp.exp(Lc_star)
    psi_p_IR = mp.sqrt(2 * Lc_star / (mp.exp(2 * Lc_star) - 1))
    psi_m_UV = mp.sqrt(2 * Lc_star / (1 - mp.exp(-2 * Lc_star))) * mp.exp(-Lc_star)
    psi_m_IR = mp.sqrt(2 * Lc_star / (1 - mp.exp(-2 * Lc_star)))
    uv_ir_duality_err = float(max(abs(psi_p_UV - psi_m_IR), abs(psi_p_IR - psi_m_UV)))

    passed = bool(
        closure_err < 1e-14
        and triplet_norm == 0.0
        and doublet_err == 0.0
        and n_massless == 9
        and abs(sin2_tw_tree - 0.375) < 1e-14
        and qem_comm_err == 0.0
        and gluon_comm_norm == 0.0
        and abs(su2_fhL_down - 0.75) < 1e-14
        and abs(su2_ff_down) < 1e-14
        and abs(cartan_ratio - exact_cartan_ratio) < 1e-13
        and t3r_orbifold_odd_err < 1e-14
        and d2V_hosotani > 0.0
        and uv_ir_duality_err < 1e-48
    )

    return {
        "gate_p5_2_passed": passed,
        "spin11_closure_err": closure_err,
        "kawamura_triplet_norm": triplet_norm,
        "n_massless_gauge_bosons": n_massless,
        "tree_sin2_thetaW": sin2_tw_tree,
        "gluon_H_vev_comm_norm": gluon_comm_norm,
        "su2_fhL_down": su2_fhL_down,
        "su2_ff_down": su2_ff_down,
        "spin10_cartan_down_over_elec_ratio": cartan_ratio,
        "t3r_orbifold_odd_err": t3r_orbifold_odd_err,
        "theta_H_star": float(theta_H_star),
        "d2V_hosotani_at_star": d2V_hosotani,
        "Lc_star_flat_1loop": float(Lc_star),
        "uv_ir_mirror_duality_50d_err": uv_ir_duality_err,
    }
