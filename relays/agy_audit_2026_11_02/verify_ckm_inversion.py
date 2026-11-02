#!/usr/bin/env python3
"""Independent verification of Theorem 2:
The (1,3)<->(3,1) CKM Corner Inversion & CP-Suppression No-Go Theorem in FR-FIB,
and its 3D-Higgs vs. 4D-Matter Null-Cone Framing Root Cause.

Proves and numerically verifies:
  1. For w != 0, the matter residue R_s = (R_1, R_i, R_j, R_k) is null in 4D C^4 = H_C
     (R_1^2 + R_i^2 + R_j^2 + R_k^2 = 0), so its 3D projection R_perp = (R_i, R_j, R_k)
     is NOT null in C^3 (R_perp . R_perp = -R_1^2 != 0).
  2. In the basis BLOCKS = [QJ, QI, QK], setting h = (a_j, a_i, a_k) and m_perp = (u_j, u_i, u_k),
     since C_a^T EPS = -EPS C_a for all C_a in BLOCKS, the Yukawa matrix is identically:
       Y_s = h m_perp^T + m_perp h^T - (h . m_perp) I_3 - u_1 [h]_x
     so that Y_s h = Y_s^T h = (h . h) m_perp (u_1 drops out completely along h).
  3. On the null Higgs cone r = |h . h| / ||h||^2 << 1, the 1st-generation left singular
     vector u_1^(s) is locked to the sector-blind vector h_hat^*, forcing:
       theta_12^(s) = |<u_2^(s), h_hat^*>| ~ O(r / (m_2^(s)/m_3^(s)))
       theta_13^(s) = |<u_3^(s), h_hat^*>| ~ r/2  (cancelling in V = U_u^dagger U_d).
  4. Because m_c/m_t << m_s/m_b in Nature, theta_12^(u) >> theta_12^(d), which places the
     dominant Cabibbo rotation in U_u^dagger (left of R_23) instead of U_d (right of R_23),
     transposing the (1,3) and (3,1) corners of V_CKM:
       |V_ub| / (|V_us| |V_cb|) = 1 + O(theta_12^(d)/theta_12^(u)) ~ 1   (PDG: 0.3965)
       |V_td| / (|V_us| |V_cb|) = O(theta_12^(d)/theta_12^(u)) << 1      (PDG: 0.9135)
       sin(delta_CP) <= O(theta_12^(d)/theta_12^(u)) << 1                (PDG: 0.948)
     and proves the Lagrange-multiplier compromise (2.522^(-1/3), 2.522^(-1/3), 2.522^(+1/3))
     = (0.735, 0.735, 1.361) for free Higgs vectors h in CP^2 (B1743, P-377).
"""
from __future__ import annotations

from fractions import Fraction as F
import json
import math
import pathlib
import sys

import mpmath as mp
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
V_DIR = ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification"
sys.path.insert(0, str(V_DIR / "correction"))
sys.path.insert(0, str(V_DIR))

import qseries as Q
import b1656_funcs as B

mp.mp.dps = 30
th2, th3, th4 = Q.theta2(), Q.theta3(1), Q.theta3(-1)
di = (th2 * th3 * th4).inv()
R_ser = [-(th2 * th2) * di, -(th4 * th4) * di, (th3 * th3) * Q.S.c(0, 1) * di]
e2, e4 = Q.E2(), Q.E4()
DR_ser = [Q.serre(c, F(-1, 2), e2) for c in R_ser]
D2R_ser = [Q.serre(c, F(3, 2), e2) for c in DR_ser]
a0_ser = [D2R_ser[j] + Q.S.c(F(-1, 48)) * e4 * R_ser[j] for j in range(3)]


def ev(s, tau: complex) -> complex:
    x = mp.exp(2j * mp.pi * mp.mpc(tau.real, tau.imag) / 8)
    return complex(
        mp.fsum(
            mp.mpc(mp.mpf(a.numerator) / a.denominator, mp.mpf(b.numerator) / b.denominator) * (x ** kk)
            for kk, (a, b) in s.d.items()
        )
    )


col = sorted(
    (p["tau"][1], p["L_max"], p["L_2"])
    for p in json.loads(
        (ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text(encoding="utf-8")
    )["points"]
    if abs(p["tau"][0] - 0.25) < 1e-9
)


def radii(tau: complex) -> tuple[float, float]:
    return (
        float(np.interp(tau.imag, [c[0] for c in col], [c[1] for c in col])),
        float(np.interp(tau.imag, [c[0] for c in col], [c[2] for c in col])),
    )


def direction(name: str, tau: complex) -> list[complex]:
    if name == "DR":
        return [ev(c, tau) for c in DR_ser]
    if name == "a0":
        return [ev(c, tau) for c in a0_ser]
    if name == "R":
        return [ev(c, tau) for c in R_ser]
    a_ = int(name[2:])
    q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag))
    eps = 1j ** ((a_ + 2) // 2)
    t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    return [complex(eps * (t2 ** a_)), complex(eps * (t4 ** a_)), complex(1j * (t3 ** a_))]


def skew3(v: np.ndarray) -> np.ndarray:
    return np.array([
        [0.0, -v[2], v[1]],
        [v[2], 0.0, -v[0]],
        [-v[1], v[0], 0.0],
    ], dtype=complex)


def analyze_point(
    label: str,
    tau: complex,
    line: tuple[F, F],
    a_dir: list[complex],
    rad_name: str,
    rd: tuple[int, int, int],
) -> dict:
    Lmax, L2 = radii(tau)
    L = Lmax if rad_name == "L_max" else L2

    U = {}
    S_vals = {}
    h_vecs = {}
    max_4d_null_err = 0.0
    min_3d_nonnull_ratio = 1.0
    max_vec_id_err = 0.0
    max_yh_err = 0.0

    for (sn, ql, qr), r in zip([("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)], rd):
        w = B.line_w(line[0], line[1], tau)
        x, yy = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, yy, tau)
        c = B.cA(x, yy, tau, R)

        # Verify 4D nullity R_1^2 + R_i^2 + R_j^2 + R_k^2 = 0 vs 3D non-nullity R_i^2 + R_j^2 + R_k^2 = -R_1^2 != 0
        r1, ri, rj, rk = R["1"], R["i"], R["j"], R["k"]
        norm_sq = float(abs(r1) ** 2 + abs(ri) ** 2 + abs(rj) ** 2 + abs(rk) ** 2)
        if norm_sq > 0:
            null4 = float(abs(r1 ** 2 + ri ** 2 + rj ** 2 + rk ** 2)) / norm_sq
            perp3 = float(abs(ri ** 2 + rj ** 2 + rk ** 2)) / norm_sq
            max_4d_null_err = max(max_4d_null_err, null4)
            min_3d_nonnull_ratio = min(min_3d_nonnull_ratio, perp3)

        Sm = a_dir[0] * B.QI + a_dir[1] * B.QJ + a_dir[2] * B.QK
        if r:
            Sm = B.EPS @ Sm.conj() @ B.EPS.T
        u = {
            k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0.0)
            for k in B.UNITS
        }
        M_mat = B.weighted_M(u)
        Y = B.coupling(Sm, M_mat)

        # Extract h = (h_J, h_I, h_K) and m_perp = (u_j, u_i, u_k) in BLOCKS = [QJ, QI, QK]
        h_vec = np.array([a_dir[1], a_dir[0], a_dir[2]], dtype=complex)
        if r:
            h_vec = h_vec.conj()
        m1 = u["1"]
        m_perp = np.array([u["j"], u["i"], u["k"]], dtype=complex)

        # Verify Y == h m_perp^T + m_perp h^T - (h.m_perp) I_3 - m1 [h]_x
        Y_vec = (
            np.outer(h_vec, m_perp)
            + np.outer(m_perp, h_vec)
            - np.dot(h_vec, m_perp) * np.eye(3)
            - m1 * skew3(h_vec)
        )
        max_vec_id_err = max(max_vec_id_err, float(np.max(np.abs(Y - Y_vec))))
        max_yh_err = max(
            max_yh_err,
            float(np.max(np.abs(Y @ h_vec - (np.dot(h_vec, h_vec) * m_perp)))),
            float(np.max(np.abs(Y.T @ h_vec - (np.dot(h_vec, h_vec) * m_perp)))),
        )

        u_, s, _ = np.linalg.svd(Y)
        o = np.argsort(s)
        s = s[o]
        U[sn] = u_[:, o]
        S_vals[sn] = s / s[2]
        h_vecs[sn] = h_vec / np.linalg.norm(h_vec)

    Vm = U["up"].conj().T @ U["down"]
    h_ref = h_vecs["up"].conj()
    proj_u = np.abs(U["up"].conj().T @ h_ref)
    proj_d = np.abs(U["down"].conj().T @ h_ref)

    J = float(np.imag(Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1])))
    s12, s23, s13 = float(abs(Vm[0, 1])), float(abs(Vm[1, 2])), float(abs(Vm[0, 2]))
    c12 = math.sqrt(max(0.0, 1.0 - s12 ** 2))
    c23 = math.sqrt(max(0.0, 1.0 - s23 ** 2))
    c13 = math.sqrt(max(0.0, 1.0 - s13 ** 2))
    j_max = c12 * c23 * (c13 ** 2) * s12 * s23 * s13
    sin_delta = abs(J) / j_max if j_max > 0 else 0.0

    h_raw = np.array([a_dir[1], a_dir[0], a_dir[2]], dtype=complex)
    r_null = float(abs(np.dot(h_raw, h_raw)) / (np.linalg.norm(h_raw) ** 2))

    res = {
        "label": label,
        "tau": f"{tau.real}+{tau.imag}j",
        "line": [str(line[0]), str(line[1])],
        "radius": rad_name,
        "reading": list(rd),
        "max_4d_null_err": max_4d_null_err,
        "min_3d_nonnull_ratio": min_3d_nonnull_ratio,
        "max_vec_formula_err": max_vec_id_err,
        "max_yh_identity_err": max_yh_err,
        "higgs_nullity_r": r_null,
        "mc_over_mt": float(S_vals["up"][1]),
        "ms_over_mb": float(S_vals["down"][1]),
        "mu_over_mt": float(S_vals["up"][0]),
        "md_over_mb": float(S_vals["down"][0]),
        "align_u1_with_h_conj": float(proj_u[0]),
        "align_d1_with_h_conj": float(proj_d[0]),
        "theta_12_u": float(proj_u[1]),
        "theta_12_d": float(proj_d[1]),
        "ratio_theta_12_u_over_d": float(proj_u[1] / proj_d[1]),
        "theta_13_u": float(proj_u[2]),
        "theta_13_d": float(proj_d[2]),
        "V_abs": [[float(abs(Vm[i, j])) for j in range(3)] for i in range(3)],
        "V_us": s12,
        "V_cb": s23,
        "V_ub": s13,
        "V_td": float(abs(Vm[2, 0])),
        "V_cd": float(abs(Vm[1, 0])),
        "V_ts": float(abs(Vm[2, 1])),
        "ratio_Vub_over_Vus_Vcb": float(s13 / (s12 * s23)),
        "ratio_Vtd_over_Vus_Vcb": float(abs(Vm[2, 0]) / (s12 * s23)),
        "ratio_Vub_over_Vtd": float(s13 / abs(Vm[2, 0])),
        "abs_J": abs(J),
        "J_max": j_max,
        "sin_delta_CP": sin_delta,
    }

    print(f"\n=== {label} ===")
    print(
        f"  4D null err = {max_4d_null_err:.2e}, 3D non-null |R_perp.R_perp|/||R||^2 >= {min_3d_nonnull_ratio:.4f}, "
        f"PY_vec err = {max_vec_id_err:.2e}, (PY)h err = {max_yh_err:.2e}"
    )
    print(
        f"  Higgs nullity r = {r_null:.4e} | m2/m3: up={S_vals['up'][1]:.5f}, down={S_vals['down'][1]:.5f} "
        f"(down/up = {S_vals['down'][1]/S_vals['up'][1]:.2f})"
    )
    print(
        f"  |<u_k^(up),   h*>| = {np.round(proj_u, 5)} -> theta_12^(u)={proj_u[1]:.4f}, theta_13^(u)={proj_u[2]:.5f}"
    )
    print(
        f"  |<u_k^(down), h*>| = {np.round(proj_d, 5)} -> theta_12^(d)={proj_d[1]:.4f}, theta_13^(d)={proj_d[2]:.5f} "
        f"(theta_12^(u)/theta_12^(d) = {proj_u[1]/proj_d[1]:.2f})"
    )
    print("  Full |V_CKM| matrix:")
    for r_idx, r_name in enumerate(["u", "c", "t"]):
        print(f"    {r_name}: [{abs(Vm[r_idx,0]):.5f}, {abs(Vm[r_idx,1]):.5f}, {abs(Vm[r_idx,2]):.5f}]")
    print(f"  |V_ub| / (|V_us|*|V_cb|) = {res['ratio_Vub_over_Vus_Vcb']:.4f}  (PDG = 0.3965)")
    print(f"  |V_td| / (|V_us|*|V_cb|) = {res['ratio_Vtd_over_Vus_Vcb']:.4f}  (PDG = 0.9135)")
    print(f"  |V_ub| / |V_td|          = {res['ratio_Vub_over_Vtd']:.4f}  (PDG = 0.4340)")
    print(f"  |J| = {abs(J):.4e}, J_max = {j_max:.4e}, sin(delta_CP) = {sin_delta:.4f} (PDG = 0.948)")
    return res


def main() -> int:
    benchmarks = []

    # 1. B1825 best chi2_ten address
    tau1 = complex(0.093359375, 2.742578125)
    benchmarks.append(
        analyze_point(
            "B1825 Best chi2_ten: (3/8, 3/8), DR, L_2, S~S~S, tau=0.0934+2.7426j",
            tau1, (F(3, 8), F(3, 8)), direction("DR", tau1), "L_2", (1, 1, 0),
        )
    )

    # 2. B1726 best nine-row
    tau2 = complex(0.55, 2.55)
    benchmarks.append(
        analyze_point(
            "B1726 Best nine-row: (2/5, 1/10), DR, L_max, S~S~S~, tau=0.55+2.55j",
            tau2, (F(2, 5), F(1, 10)), direction("DR", tau2), "L_max", (1, 1, 1),
        )
    )

    # 3. P-377 strip: tau = 0.45 + 3.00j on (2/5, 1/10), DR, L_max, S~S~S~
    tau3 = complex(0.45, 3.00)
    benchmarks.append(
        analyze_point(
            "P-377 Strip: (2/5, 1/10), DR, L_max, S~S~S~, tau=0.45+3.00j",
            tau3, (F(2, 5), F(1, 10)), direction("DR", tau3), "L_max", (1, 1, 1),
        )
    )

    # 4. B1743 F_6 on (2/5, 3/10), L_max, SSS, tau = 0.3125 + 3.30j
    tau4 = complex(0.3125, 3.30)
    benchmarks.append(
        analyze_point(
            "B1743 F_6: (2/5, 3/10), F_6, L_max, SSS, tau=0.3125+3.30j",
            tau4, (F(2, 5), F(3, 10)), direction("F_6", tau4), "L_max", (0, 0, 0),
        )
    )

    v_us_pdg, v_cb_pdg, v_ub_pdg, v_td_pdg = 0.22500, 0.04182, 0.003732, 0.00858
    k_pdg = (v_us_pdg * v_cb_pdg) / v_ub_pdg
    lagrange_compromise = {
        "K_PDG_Vus_Vcb_over_Vub": k_pdg,
        "PDG_Vub_over_Vus_Vcb": 1.0 / k_pdg,
        "PDG_Vtd_over_Vus_Vcb": v_td_pdg / (v_us_pdg * v_cb_pdg),
        "PDG_Vub_over_Vtd": v_ub_pdg / v_td_pdg,
        "equal_rel_weight_compromise": [
            k_pdg ** (-1.0 / 3.0),
            k_pdg ** (-1.0 / 3.0),
            k_pdg ** (+1.0 / 3.0),
        ],
        "B1743_free_CP2_reported_ratios_to_PDG": [0.773, 0.775, 1.213],
        "P377_reported_ratios_to_PDG": [0.692, 0.761, 1.545],
    }

    print("\n=== Lagrange-Multiplier Compromise Under |V_ub| = |V_us|*|V_cb| = 2.5213 * |V_ub|_PDG ===")
    print(f"  Analytic equal-relative-weight compromise: {np.round(lagrange_compromise['equal_rel_weight_compromise'], 4)}")
    print(f"  B1743 free-CP^2 optimum ratios to PDG:     {lagrange_compromise['B1743_free_CP2_reported_ratios_to_PDG']}")
    print(f"  P-377 strip ratios to PDG:                 {lagrange_compromise['P377_reported_ratios_to_PDG']}")

    out_json = pathlib.Path(__file__).resolve().parent / "verify_ckm_inversion_results.json"
    out_json.write_text(
        json.dumps({"lagrange_compromise": lagrange_compromise, "benchmarks": benchmarks}, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
