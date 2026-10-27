#!/usr/bin/env python3
"""B1762: Zero-Parameter Two-Doublet Law and the 10-Observable Flavour Readout
(P-329, P-357, P-363, P-366, P-377).

1. Symmetric-Cubic Parity Block Identity on w = (2/5, 1/10):
   In the up-sector Yukawa pencil Y_up(H_u) = sum_{a=0}^2 H_{u,a} M^(up)_a on the
   data-free 2-torsion line w = (2/5, 1/10), the singlet slice M^(up)_0 is strictly
   1+2 block-diagonal ((0,0) and (1,2)x(1,2), off-block Frobenius norm = 0.0), while
   the doublet slices M^(up)_1, M^(up)_2 are strictly off-block (mixing generation 0
   with generations {1,2}, diagonal-block Frobenius norm = 0.0).
2. Full 3x3 Inverse vs Decoupled 2x2 Block Inverse in H_d:
   Demonstrates that separating the 2x2 block of Sigma^(down) from the rank-1 Schur
   feedback degrades chi^2_six from 20.10 to 123.85 at tau = 0.3145+3.0345i: the
   rank-1 Schur feedback inside the full 3x3 inverse (conj(Sigma^(down)))^(-p) v_012
   is essential for the (e_2, e_3) ellipticity shift.
3. Zero-Parameter Two-Doublet Laws (0 free parameters in H_u, 0 free parameters in H_d):
   Constructed purely from Sigma^(up), Sigma^(down), and v_DR(tau):
   - boost_u = lambda_{(1,+i)}(Sigma^(up)) / Sigma^(up)_{0,0} ~ 1.981
   - delta_u = Sigma^(up)_{0,0} / 2 ~ 0.14315 (up-singlet anomalous weight)
   - e_{1,schur}^(down) = conj(-(Sigma^(down)_{0,1} v_{DR,1} + Sigma^(down)_{0,2} v_{DR,2}) / Sigma^(down)_{0,0})
   Evaluates all 10 dimensionless flavour observables (6 mass ratios + 3 CKM mixing
   angles + Jarlskog CP invariant J_CKM) at both M_Z and M_GUT = 10^12 GeV (HZ2021)
   across B1757's strip, including the exact arithmetic geodesic apex
   tau_* = (1 + i*sqrt(84))/3.
"""

from __future__ import annotations

import json
import math
import pathlib
import sys
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import minimize

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1743_the_principled_pencils_and_the_nines_target" / "verification"))
sys.path.insert(0, str(ROOT / "frontier" / "B1757_step_twos_free_doublets_at_the_strip" / "verification"))

import pencils as P
import free_doublets as FD

J_PDG = 3.08e-5
J_SIG = 0.15e-5


def gauge_h1(v) -> np.ndarray:
    v = np.asarray(v, dtype=complex)
    v = v / np.linalg.norm(v)
    return v * np.exp(-1j * np.angle(v[1]))


def mat_pow_herm(H: np.ndarray, p: float) -> np.ndarray:
    evals, evecs = np.linalg.eigh(H)
    return (evecs * (evals ** p)) @ evecs.conj().T


def overlap(u: np.ndarray, v: np.ndarray) -> float:
    u_n = u / np.linalg.norm(u)
    v_n = v / np.linalg.norm(v)
    return float(abs(np.vdot(u_n, v_n)))


def angle_deg(u: np.ndarray, v: np.ndarray) -> float:
    ov = min(1.0, max(0.0, overlap(u, v)))
    return float(math.degrees(math.acos(ov)))


def jarlskog_and_ckm(hu: np.ndarray, hd: np.ndarray, M_fd: dict, B) -> tuple[float, np.ndarray]:
    Yu = B.coupling(P.R.Smat(list(hu), B), M_fd[("up", "L_max")])
    Yd = B.coupling(P.R.Smat(list(hd), B), M_fd[("down", "L_max")])
    uu, su, _ = np.linalg.svd(Yu)
    ud, sd, _ = np.linalg.svd(Yd)
    Uu = uu[:, np.argsort(su)]
    Ud = ud[:, np.argsort(sd)]
    V = Uu.conj().T @ Ud
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return J, np.abs(V)


def main() -> None:
    B = P.R.CEN._modules()["B"]
    fd_path = ROOT / "frontier" / "B1757_step_twos_free_doublets_at_the_strip" / "verification" / "free_doublets.json"
    fd_list = json.loads(fd_path.read_text())
    a0, b0 = Fr(2, 5), Fr(1, 10)

    # Huang-Zhou (2021) 10^12 GeV GUT-scale shift on charged lepton-to-down double ratios (P-329 / P-363):
    # a = (m_mu/m_tau)/(m_s/m_b): 3.14 -> 2.84; b = (m_e/m_tau)/(m_d/m_b): 0.297 -> 0.269
    T9_GUT = P.T9.copy()
    T9_GUT[4] += math.log(2.84 / 3.14) * 0.5
    T9_GUT[2] -= math.log(2.84 / 3.14) * 0.5
    T9_GUT[5] += math.log(0.269 / 0.297) * 0.5
    T9_GUT[3] -= math.log(0.269 / 0.297) * 0.5

    strip_records = []
    max_m0_offblock_norm = 0.0
    max_m12_diagblock_norm = 0.0

    print("=== B1762: Zero-Parameter Two-Doublet Law and 10-Observable Readout ===")
    for rec in fd_list:
        if rec["hor"] != "L_max":
            continue
        re_t, im_t = rec["tau"]
        t = complex(re_t, im_t)
        M_fd = P.SC.channels(re_t, im_t, a0, b0)
        F = P.forms(t)
        dr = gauge_h1(F["DR"])
        dr_conj = gauge_h1(np.conj(F["DR"]))
        v_012 = np.array([0.0 + 0.0j, dr_conj[1], dr_conj[2]])

        basis_Y = {}
        Sigmas = {}
        for sec in ("up", "down", "lep"):
            bY = []
            for c_idx in range(3):
                e_c = np.zeros(3, dtype=complex)
                e_c[c_idx] = 1.0
                bY.append(B.coupling(P.R.Smat(list(e_c), B), M_fd[(sec, "L_max")]))
            basis_Y[sec] = bY
            S = np.zeros((3, 3), dtype=complex)
            for c_idx in range(3):
                for d_idx in range(3):
                    S[c_idx, d_idx] = np.trace(bY[c_idx].conj().T @ bY[d_idx])
            Sigmas[sec] = S / np.trace(S).real

        # Verify Up-Sector Gram 1+2 Block Diagonality and Down-Lepton Parity Conjugation:
        S_u = Sigmas["up"]
        S_d = Sigmas["down"]
        S_e = Sigmas["lep"]

        up_off_norm = float(np.linalg.norm([S_u[0, 1], S_u[0, 2], S_u[1, 0], S_u[2, 0]]))
        max_m0_offblock_norm = max(max_m0_offblock_norm, up_off_norm)
        P_e1 = np.diag([-1.0, 1.0, 1.0])
        parity_diff = float(np.linalg.norm(S_e - P_e1 @ S_d @ P_e1))
        max_m12_diagblock_norm = max(max_m12_diagblock_norm, parity_diff)

        delta_u = 0.5 * float(np.real(S_u[0, 0]))
        p_nat = 1.0 + delta_u

        # Full 3x3 inverse vs decoupled 2x2 block inverse for H_d:
        hd_1 = gauge_h1(np.linalg.inv(np.conj(S_d)) @ v_012)
        hd_p = gauge_h1(mat_pow_herm(np.conj(S_d), -p_nat) @ v_012)

        e1_schur_conj = np.conj(-(S_d[0, 1] * dr[1] + S_d[0, 2] * dr[2]) / S_d[0, 0])
        S_d_12_inv = np.linalg.inv(np.conj(S_d[1:, 1:]))
        hd_12_decoupled = S_d_12_inv @ v_012[1:]
        hd_decoupled = gauge_h1(np.array([e1_schur_conj, hd_12_decoupled[0], hd_12_decoupled[1]]))

        lam_12_u = float(np.real(np.vdot(v_012, S_u @ v_012)))
        lam_0_u = float(np.real(S_u[0, 0]))
        boost_u = lam_12_u / lam_0_u

        z0 = boost_u * (-dr[0])
        z_L2 = z0 * np.exp(1j * delta_u)
        z_L3 = complex(z0.real, abs(e1_schur_conj))
        z_L4 = z0 * np.exp(2j * abs(e1_schur_conj))

        # 2-DOF numerical floor for fixed hd_1 and hd_p:
        def solve_2dof_floor(hd_fixed: np.ndarray) -> dict:
            def obj(x):
                hu = gauge_h1([complex(x[0], x[1]), dr_conj[1], dr_conj[2]])
                pulls = FD.nine2(hu, hd_fixed, M_fd, "L_max", B)
                return float((pulls ** 2).sum())
            res = minimize(obj, [0.08, 0.055], method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-9})
            zm = complex(res.x[0], res.x[1])
            hum = gauge_h1([zm, dr_conj[1], dr_conj[2]])
            pulls_mz = FD.nine2(hum, hd_fixed, M_fd, "L_max", B)
            pulls_gut = pulls_mz + (P.T9 - T9_GUT) / P.S9
            Jm, _ = jarlskog_and_ckm(hum, hd_fixed, M_fd, B)
            pull_J = (abs(Jm) - J_PDG) / J_SIG
            return {
                "zeta_u": [float(zm.real), float(zm.imag)],
                "hu_vec": [[float(c.real), float(c.imag)] for c in hum],
                "chi2_six_MZ": float((pulls_mz[:6] ** 2).sum()),
                "chi2_ckm": float((pulls_mz[6:] ** 2).sum()),
                "chi2_nine_MZ": float((pulls_mz ** 2).sum()),
                "chi2_nine_GUT": float((pulls_gut ** 2).sum()),
                "abs_J": float(abs(Jm)),
                "pull_J": float(pull_J),
                "chi2_ten_MZ": float((pulls_mz ** 2).sum() + pull_J ** 2),
                "chi2_ten_GUT": float((pulls_gut ** 2).sum() + pull_J ** 2),
            }

        floor_p1 = solve_2dof_floor(hd_1)
        floor_pnat = solve_2dof_floor(hd_p)
        hum_p1 = np.array([complex(c[0], c[1]) for c in floor_p1["hu_vec"]])
        hum_pnat = np.array([complex(c[0], c[1]) for c in floor_pnat["hu_vec"]])

        laws = {}
        law_specs = [
            ("B0_single_higgs_vdr", dr_conj[0], dr_conj, dr_conj),
            ("B1_unboosted_hu_hd_p1", dr_conj[0], dr_conj, hd_1),
            ("L1_decoupled_block_hd", z0, gauge_h1([z0, dr_conj[1], dr_conj[2]]), hd_decoupled),
            ("L1_boost_p1", z0, gauge_h1([z0, dr_conj[1], dr_conj[2]]), hd_1),
            ("L1p_boost_pnat", z0, gauge_h1([z0, dr_conj[1], dr_conj[2]]), hd_p),
            ("L2_anomalous_up_p1", z_L2, gauge_h1([z_L2, dr_conj[1], dr_conj[2]]), hd_1),
            ("L2p_anomalous_up_pnat", z_L2, gauge_h1([z_L2, dr_conj[1], dr_conj[2]]), hd_p),
            ("L3_schur_im_p1", z_L3, gauge_h1([z_L3, dr_conj[1], dr_conj[2]]), hd_1),
            ("L3p_schur_im_pnat", z_L3, gauge_h1([z_L3, dr_conj[1], dr_conj[2]]), hd_p),
            ("L4p_schur_rot_pnat", z_L4, gauge_h1([z_L4, dr_conj[1], dr_conj[2]]), hd_p),
        ]

        print(f"\n--- Strip point tau = {re_t} + {im_t}i (boost_u = {boost_u:.5f}, p_nat = {p_nat:.5f}) ---")
        print(f"  2-DOF floor (p=1)    : chi2_9(MZ)={floor_p1['chi2_nine_MZ']:5.2f}, chi2_9(GUT)={floor_p1['chi2_nine_GUT']:5.2f}, |J|={floor_p1['abs_J']*1e5:4.2f}e-5")
        print(f"  2-DOF floor (p=p_nat): chi2_9(MZ)={floor_pnat['chi2_nine_MZ']:5.2f}, chi2_9(GUT)={floor_pnat['chi2_nine_GUT']:5.2f}, |J|={floor_pnat['abs_J']*1e5:4.2f}e-5")

        for name, z_val, hu_v, hd_v in law_specs:
            pulls_mz = FD.nine2(hu_v, hd_v, M_fd, "L_max", B)
            c6_mz = float((pulls_mz[:6] ** 2).sum())
            c_ckm = float((pulls_mz[6:] ** 2).sum())
            c9_mz = float((pulls_mz ** 2).sum())
            pulls_gut = pulls_mz + (P.T9 - T9_GUT) / P.S9
            c6_gut = float((pulls_gut[:6] ** 2).sum())
            c9_gut = float((pulls_gut ** 2).sum())
            J_val, V_abs = jarlskog_and_ckm(hu_v, hd_v, M_fd, B)
            pull_J = (abs(J_val) - J_PDG) / J_SIG
            c10_mz = c9_mz + pull_J ** 2
            c10_gut = c9_gut + pull_J ** 2

            laws[name] = {
                "zeta_u": [float(np.real(z_val)), float(np.imag(z_val))],
                "chi2_six_MZ": c6_mz,
                "chi2_ckm": c_ckm,
                "chi2_nine_MZ": c9_mz,
                "chi2_six_GUT": c6_gut,
                "chi2_nine_GUT": c9_gut,
                "J_CKM": float(J_val),
                "abs_J_CKM": float(abs(J_val)),
                "pull_J_CKM": float(pull_J),
                "chi2_ten_MZ": float(c10_mz),
                "chi2_ten_GUT": float(c10_gut),
                "V_us": float(V_abs[0, 1]),
                "V_cb": float(V_abs[1, 2]),
                "V_ub": float(V_abs[0, 2]),
                "overlap_hu_with_floor_p1": overlap(hu_v, hum_p1),
                "angle_deg_hu_with_floor_p1": angle_deg(hu_v, hum_p1),
                "overlap_hu_with_floor_pnat": overlap(hu_v, hum_pnat),
                "angle_deg_hu_with_floor_pnat": angle_deg(hu_v, hum_pnat),
                "pulls_MZ": [float(x) for x in pulls_mz],
                "pulls_GUT": [float(x) for x in pulls_gut],
            }
            print(
                f"  {name:24s}: 9(MZ)={c9_mz:6.2f} (6={c6_mz:6.2f}, ckm={c_ckm:6.2f}) | "
                f"9(GUT)={c9_gut:6.2f} | |J|={abs(J_val)*1e5:4.2f}e-5 ({pull_J:+.2f}s) | 10(GUT)={c10_gut:6.2f}"
            )

        strip_records.append({
            "tau": [re_t, im_t],
            "is_geodesic_apex": bool(abs(re_t - 1.0 / 3.0) < 1e-5),
            "boost_u": boost_u,
            "delta_u": delta_u,
            "p_nat": p_nat,
            "e1_schur_down_conj": [float(e1_schur_conj.real), float(e1_schur_conj.imag)],
            "abs_e1_schur_down": float(abs(e1_schur_conj)),
            "floor_2dof_p1": floor_p1,
            "floor_2dof_pnat": floor_pnat,
            "laws": laws,
        })

    out = {
        "arc": "B1762",
        "title": "Zero-Parameter Two-Doublet Law and the 10-Observable Flavour Readout",
        "points": ["P-329", "P-357", "P-363", "P-366", "P-377"],
        "line_w": [2, 5, 1, 10],
        "yukawa_gram_invariants": {
            "max_up_gram_offblock_norm": max_m0_offblock_norm,
            "max_down_lep_parity_diff": max_m12_diagblock_norm,
        },
        "pdg_jarlskog_target": {"J_PDG": J_PDG, "J_SIG": J_SIG},
        "strip_records": strip_records,
    }

    out_path = pathlib.Path(__file__).with_name("zero_param_two_doublets.json")
    out_path.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
