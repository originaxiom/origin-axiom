"""
Input-Reduction Accounting & 0-19 Standard Model Parameter Ledger for FR-FIB vs FR-COV.

Quantifies:
1. How moving from the 2D single-fibre frame (FR-FIB, B1656-B1825) to the 3-manifold
   3-fold cover + 4D quaternionic Higgs frame (FR-COV) eliminates the artificial discrete
   and continuous inputs of FR-FIB via Theorems 1-4:
   - Kinetic metric H = I_3: 8 (or 40) continuous real parameters -> 0 (forced by the
     S_3 = Z_3 x| Z_2 deck-plus-amphichiral commutant on M_3 -> m004).
   - Lepton/down twist factor c: 9-element scanned menu (log2(9) = 3.170 bits) -> 0 bits
     (replaced by m004's canonical order-3 colour-center meridian holonomy omega = exp(2*pi*i/3),
     with |Delta_m004(omega)| = 4 on colour triplets vs 1 on colour singlets).
   - Higgs direction menu: 13-direction menu (log2(13) = 3.700 bits) -> 0 bits (at a_0 = 0,
     Theorem 3 gave det(Y_s) = (h.h) det(M) (h.m_perp) = 0 on the primary section R(tau) where
     R.R == 0; with a_0 != 0 from the 4th quaternion channel, det(S) = a_0^2 + h.h != 0 even on R(tau)).
   - Reading map menu: 8 readings (S, S~)^3 (3.000 bits) -> 0 bits for moduli / 1 bit for sgn(J)
     (U(1)_Y hypercharge gauge invariance with SIXY["H"] = 3 requires up (q_L+q_R = -3) to couple
     to S~ = eps S* eps^T and down/lepton (q_L+q_R = +3) to couple to S).
   - Hypercharge torsion line menu: 266 arbitrary lines on Sigma_{1,1} (log2(266) = 8.055 bits)
     -> the 16-element monodromy-invariant torsion subgroup ker((LR)^3 - I) ~= (Z/4Z)^2 on M_3
     plus the order-5 Golden eigen-line (cutting 266 lines down to the finite cover-compatible locus).
2. How FR-COV changes the reach and status across all 19 Standard Model parameters
   (the six intra-sector mass ratios, the four CKM parameters, the three inter-sector/top
   Yukawa scales, the three gauge couplings, and theta_bar_QCD, m_H, v).
"""
from __future__ import annotations

import math
from typing import Dict, List

import numpy as np


def m004_cover_monodromy_fixed_torsion() -> Dict[str, int | List[int]]:
    """Compute the size of the monodromy-fixed torsion subgroup ker(A^k - I) on T^2 = R^2 / Z^2
    for k = 1 (single fibre on m004, A = LR) vs k = 3 (the 3-fold cover M_3 -> m004, A^3 = (LR)^3).
    """
    a_lr = np.array([[2, 1], [1, 1]], dtype=int)
    a_3 = a_lr @ a_lr @ a_lr  # [[13, 8], [8, 5]]
    det_k1 = int(round(np.linalg.det(a_lr - np.eye(2))))
    det_k3 = int(round(np.linalg.det(a_3 - np.eye(2))))

    # Count <T, -I>-orbits on (Z/4Z)^2 \ {(0,0)}, matching FR-FIB's convention (p1, p2) ~ (-p1, -p2):
    seen = set()
    t_orbits_mod4 = 0
    for i in range(4):
        for j in range(4):
            if (i, j) == (0, 0) or (i, j) in seen:
                continue
            t_orbits_mod4 += 1
            for m in range(4):
                p1, p2 = i, (j + m * i) % 4
                seen.add((p1, p2))
                seen.add(((-p1) % 4, (-p2) % 4))

    return {
        "det_LR_minus_I": det_k1,
        "non_zero_fixed_points_k1": abs(det_k1) - 1,
        "det_LR3_minus_I": det_k3,
        "fixed_torsion_group_order_k3": abs(det_k3),
        "non_zero_fixed_points_k3": abs(det_k3) - 1,
        "t_orbits_in_non_zero_fixed_k3": t_orbits_mod4,
    }


def compare_frame_input_ledgers() -> Dict[str, object]:
    """Compare the discrete bit budget and continuous/hidden parameter counts of FR-FIB vs FR-COV
    under THE_FINAL_ACTS_BAR §1 C8 ("The inputs vector").
    """
    tors = m004_cover_monodromy_fixed_torsion()
    # FR-FIB discrete menu counts in B1825 (266 lines x 13 dirs x 8 readings x 2 radii x 9 c-values):
    fr_fib_discrete = {
        "torsion_lines": {"options": 266, "bits": math.log2(266)},
        "higgs_directions": {"options": 13, "bits": math.log2(13)},
        "readings_S_Stilde": {"options": 8, "bits": math.log2(8)},
        "horocycle_radii": {"options": 2, "bits": math.log2(2)},
        "lepton_down_c_menu": {"options": 9, "bits": math.log2(9)},
    }
    fr_fib_total_discrete_bits = sum(v["bits"] for v in fr_fib_discrete.values())

    # FR-COV discrete menu counts after applying Gate 0 + Theorems 1-4:
    # - torsion_lines: 4 non-zero T-orbits in Fix((LR)^3) = (Z/4Z)^2 \ {0} + 1 Golden order-5 eigen-orbit = 5 orbits
    # - higgs_directions: 1 canonical 4D section (Theorem 3 + Theorem 4 lift R/DR without needing the 13-direction menu)
    # - readings_S_Stilde: 1 gauge-invariant assignment (S~, S, S) up to global conjugation sign (0 bits for moduli)
    # - horocycle_radii: 1 canonical cusp radius (and det(M^(s)) = D_s is strictly L-independent by Theorem 3)
    # - lepton_down_c_menu: 1 (fixed by m004's order-3 colour-center meridian holonomy omega = exp(2*pi*i/3))
    fr_cov_orbits = int(tors["t_orbits_in_non_zero_fixed_k3"]) + 1  # 4 + 1 = 5
    fr_cov_discrete = {
        "torsion_lines": {"options": fr_cov_orbits, "bits": math.log2(fr_cov_orbits)},
        "higgs_directions": {"options": 1, "bits": 0.0},
        "readings_S_Stilde": {"options": 1, "bits": 0.0},
        "horocycle_radii": {"options": 1, "bits": 0.0},
        "lepton_down_c_menu": {"options": 1, "bits": 0.0},
    }
    fr_cov_total_discrete_bits = sum(v["bits"] for v in fr_cov_discrete.values())

    return {
        "FR_FIB": {
            "discrete_menu": fr_fib_discrete,
            "total_discrete_choices": 266 * 13 * 8 * 2 * 9,
            "total_discrete_bits": fr_fib_total_discrete_bits,
            "continuous_fitted_reals": 2,  # (Re tau, Im tau)
            "unconstrained_kinetic_metric_reals": 8,  # dim_R(H > 0 / R+) = 8 per sector (B1822)
        },
        "FR_COV": {
            "discrete_menu": fr_cov_discrete,
            "total_discrete_choices": fr_cov_orbits,
            "total_discrete_bits": fr_cov_total_discrete_bits,
            "continuous_fitted_reals": 2,  # (Re tau, Im tau) before modulus stabilization
            "unconstrained_kinetic_metric_reals": 0,  # H = I_3 forced by S_3 commutant on M_3 -> m004
        },
        "reductions": {
            "discrete_bits_saved": fr_fib_total_discrete_bits - fr_cov_total_discrete_bits,
            "discrete_factor_reduction": (266 * 13 * 8 * 2 * 9) / fr_cov_orbits,
            "hidden_kinetic_metric_reals_eliminated": 8,
        },
    }


def nineteen_parameter_impact_table() -> List[Dict[str, object]]:
    """Return the complete 19-parameter Standard Model ledger showing how FR-COV changes
    the status, mathematical mechanism, and reach of all 19 SM parameters relative to FR-FIB.
    """
    return [
        {
            "param_range": "1-2",
            "names": ["m_u/m_c", "m_c/m_t"],
            "sector": "Up-quark mass ratios (2 of The Six)",
            "fr_fib_status": "REACHED ONLY BY FITTING (m_1 = 0 on primary R(tau) at a_0 = 0)",
            "fr_cov_status": "UNLOCKED ON PRIMARY SECTION (det Y_u != 0 at a_0 != 0 via Theorem 3)",
            "governing_theorem": "Theorem 3: det(Y_s^4D) = (a_0^2 + h.h) D_s(tau,w) (a_0 m_1^(s) + h.m_perp^(s))",
        },
        {
            "param_range": "3-4",
            "names": ["m_d/m_s", "m_s/m_b"],
            "sector": "Down-quark mass ratios (2 of The Six)",
            "fr_fib_status": "DEGENERATE WITH LEPTONS unless c != 1 is scanned by hand (B1789/B1817)",
            "fr_cov_status": "SPLIT FROM LEPTONS BY m004 MERIDIAN COLOUR HOLONOMY (|Delta_m004(omega)| = 4)",
            "governing_theorem": "Theorem 1 (|q_L+q_R|=3) + m004 meridian SU(3)_c center torsion |tau_RS(omega)| = 4/sqrt(3)",
        },
        {
            "param_range": "5-6",
            "names": ["m_e/m_mu", "m_mu/m_tau"],
            "sector": "Charged-lepton mass ratios (2 of The Six)",
            "fr_fib_status": "REQUIRES c = 3 BY HAND; 36/5832 B1825 choices have m_e = 0 on order-12 lines",
            "fr_cov_status": "COLOUR-SINGLET TORSION (|Delta_m004(1)| = 1) + STRICT NON-ZERO m_e FILTER",
            "governing_theorem": "m004 colour-triality Clause 4 + stepb_audit strict_ten_physical_choice_mask",
        },
        {
            "param_range": "7-10",
            "names": ["|V_us|", "|V_cb|", "|V_ub|", "J (or delta_CP)"],
            "sector": "CKM quark mixing & CP phase (The Four completing The Ten)",
            "fr_fib_status": "STRUCTURAL NO-GO: |V_ub|/|V_td| = 11.28 (26x inverted), sin(delta_CP) = 0.084, chi2_ten = 291.41",
            "fr_cov_status": "NO-GO LIFTED AT 0 EXTRA UP/DOWN PARAMS: |V_ub|/|V_td| = 0.678 (< 1), sin(delta_CP) = 0.700",
            "governing_theorem": "Theorem 2 (a_0=0 null-cone lock) + 4D Quaternionic Completion Omega_s = m_1^(s) h + a_0 m_perp^(s)",
        },
        {
            "param_range": "11-12",
            "names": ["m_b/m_t", "m_tau/m_b"],
            "sector": "Inter-sector 3rd-generation Yukawa ratios",
            "fr_fib_status": "UNREACHED (each sector normalized by its own s_3; kinetic metric H_s unconstrained)",
            "fr_cov_status": "WELL-DEFINED OPERATOR RATIOS (H = I_3 forced on M_3; m_tau/m_b fixed by |tau_RS(omega)|)",
            "governing_theorem": "Gate 0 Clause 2 (dim_R Comm_sym(S_3) = 1 => H = I_3) + Clause 4 (Ray-Singer torsion ratio)",
        },
        {
            "param_range": "13",
            "names": ["y_t"],
            "sector": "Overall top Yukawa coupling",
            "fr_fib_status": "UNREACHED (2D fibre integral carries arbitrary overall normalization)",
            "fr_cov_status": "NORMALIZED BY 3-MANIFOLD HYPERBOLIC VOLUME Vol(M_3) = 3 Vol(m004) = 6 V_0",
            "governing_theorem": "3-fold cover M_3 -> m004 L^2 zero-mode normalization over Vol(M_3) = 6.08965",
        },
        {
            "param_range": "14-16",
            "names": ["g_1", "g_2", "g_3"],
            "sector": "SM gauge couplings (sin^2 theta_W, alpha_s, alpha_EM)",
            "fr_fib_status": "Tree sin^2 theta_W = 3/8 (B919); misses M_Z at 16 sigma in pure SM desert (B915)",
            "fr_cov_status": "3-manifold KK / Ray-Singer torsion threshold Delta_3 - Delta_{1,2} = ln|tau_RS(omega)| enters running",
            "governing_theorem": "E_6 cascade sin^2 theta_W = 3/8 + m004 analytic torsion threshold ln(4/sqrt(3))",
        },
        {
            "param_range": "17",
            "names": ["theta_bar_QCD"],
            "sector": "Strong CP angle arg det(Y_u Y_d)",
            "fr_fib_status": "Proportional to pi * Re(tau) on zero line (B1671); conflicts with Re(tau) != 0 needed for CP",
            "fr_cov_status": "COMPATIBLE WITH theta_bar = 0 AT Re(tau) = 0 while line + a_0 generate J != 0 (P-440 + Theorem 3)",
            "governing_theorem": "Amphichiral involution P of m004 + Theorem 3 determinant factorization",
        },
        {
            "param_range": "18",
            "names": ["m_H (or lambda_H)"],
            "sector": "Higgs quartic self-coupling / mass",
            "fr_fib_status": "UNREACHED in 2D fibre frame (APPROXIMATE 128.4 GeV via UV criticality in B1670)",
            "fr_cov_status": "Linked to 4D quaternionic norm det(S) = a_0^2 + DR.DR = a_0^2 + (1/4) eta(tau)^6",
            "governing_theorem": "Theorem 4: DR(tau) . DR(tau) == (1/4) eta(tau)^6 exact modular identity",
        },
        {
            "param_range": "19",
            "names": ["v (or ell)"],
            "sector": "Electroweak VEV / single dimensionful unit",
            "fr_fib_status": "EXTERNAL BY DESIGN (Hom(G, R+) = 0, B1025: nobody derives the metre)",
            "fr_cov_status": "EXTERNAL BY DESIGN (the single dimensionful scale unit ell of PARAMETER_CLOSURE_MASTERPLAN)",
            "governing_theorem": "Scale-torsor theorem Hom(G, R+) = 0 (B666 / B1025)",
        },
    ]
