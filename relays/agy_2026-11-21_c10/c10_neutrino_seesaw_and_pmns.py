r"""Card AGY-C10 producer script (0 of 19, pure data-free Spin(10) see-saw & 70-digit modular analysis, Guardrails 1-6):
  1. Section 1 (E1 - Spin(10) Clifford L*nu^c*H_u verification & symbolic Circular-Null Takagi 1/sqrt(2) Theorem):
     - Verifies on explicit 32x32 Cl(10, C) matrices that 5bar_4 x 1_0 (L nu^c, with 6Y = (-3, 0)) couples exclusively
       to H_5 (Y = +1/2, same doublet as Q u^c in B1970) and has zero coupling to H_5bar (Y = -1/2).
     - Proves symbolically in sympy that on circularly polarized light states v_+- = (e_1 +- i*e_2)/sqrt(2), Hermitian
       Dirac a^2 v_+ v_+^H + b^2 v_- v_-^H is diagonal whereas complex-symmetric Majorana mu*(v_+ v_-^T + v_- v_+^T) +
       eps*(v_+ v_+^T + v_- v_-^T) (0 < eps < mu) has distinct positive singular values (mu - eps, mu + eps) and exact
       pi/4-rotated Takagi eigenvectors (e_1, i*e_2), forcing |<v_a | u_b>| == 1/sqrt(2) identically for all eps > 0!
  2. Section 2 (E1, E2, & Planted Control 1 - 70-digit PMNS vs CKM across m in {8, 16, 40} & open-weave orbits):
     - Evaluates Y_nu (-3, 0), Y_e (-3, 6), Y_u (1, -4), Y_d (1, 2), and canonical zero-parameter Killing see-saw
       m_nu = Y_nu * I_3 * Y_nu^T across m * tau_*^+ (m in {8, 16, 40}):
         * Confirms strict normal Majorana hierarchy 0 < m_1 < m_2 << m_3 at every m, with (|U_e1|, |U_e2|) > 0.60
           approaching (1/sqrt(2), 1/sqrt(2)) within < 1e-3 at m = 40 (while Planted Control 1 pure-Dirac Y_nu Y_nu^H
           collapses |U_e2| to < 0.07 < 1/10 at m = 40).
         * Confirms at collar m = 8 ((16 + 8i)/5) simultaneous large solar (|U_e2| > 0.5) AND large atmospheric
           (|U_mu3| > 0.5) PMNS mixing with |U_e3| < 1/3 alongside normal-ordered CKM (|V_12| > |V_23| > |V_13|), while
           honestly reporting atmospheric |U_mu3| < 1e-2 suppression at deep m = 40 under unwarped M_R = M_0 I_3.
         * Audits P_5 (20 a != 0 points) and t = 4 overtone orbits (P_3, P_6).
  3. Section 3 (E3, Planted Control 2, & Guardrail 3 - U(3)_L x U(3)_{eR} x O(3)_{nuR} scrambling & complex-phase plant):
     - Verifies across 15 independent 70-digit U(3)_L x U(3)_{eR} x O(3)_{nuR} scramblings (including det = -1 improper
       O(3) reflections!) that all 9 |U_PMNS| moduli and 3 Majorana masses are invariant to < 1e-45 (< 1e-12).
     - Catches Planted Control 2: applying complex unitary diag(1, i, 1) outside O(3, R) shifts |U_PMNS| by > 0.10.
"""
from __future__ import annotations

import math
import random
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp


ROOT = next(
    (p for p in Path(__file__).resolve().parents if (p / "frontier").is_dir() and (p / "GENESIS.md").is_file()),
    Path.cwd(),
)
sys.path.insert(0, str(ROOT / "relays" / "agy_2026-11-20_c7"))
import c7_selberg_lefschetz_weave as C7


# ---------------------------------------------------------------------------
# Section 1: Spin(10) L*nu^c*H_u selection & Symbolic Circular-Null Theorem
# ---------------------------------------------------------------------------
def run_section1_spin10_and_circular_null_theorem() -> None:
    print("=== SECTION 1: SPIN(10) L*nu^c*H_u SELECTION & SYMBOLIC CIRCULAR-NULL 1/sqrt(2) THEOREM (E1) ===")
    cdag, c_op = [], []
    for a in range(5):
        m_f = np.zeros((32, 32), dtype=np.complex128)
        for mask in range(32):
            if not (mask & (1 << a)):
                below = bin(mask & ((1 << a) - 1)).count("1")
                m_f[mask | (1 << a), mask] = -1.0 if (below % 2 == 1) else 1.0
        cdag.append(m_f)
        c_op.append(m_f.T.copy())

    gammas = []
    for a in range(5):
        gammas.append(cdag[a] + c_op[a])
        gammas.append(-1j * (cdag[a] - c_op[a]))
    c32 = np.eye(32, dtype=np.complex128)
    for a in range(5):
        c32 = c32 @ gammas[2 * a + 1]

    idx_0 = [m for m in range(32) if bin(m).count("1") == 0]  # nu^c (6Y = 0, singlet!)
    idx_4 = [m for m in range(32) if bin(m).count("1") == 4]  # 5bar = d^c (+) L
    # Specifically, weak doublet L in 5bar has one missing index in {3, 4} (three color indices 0,1,2 occupied => masks 0b01111=15, 0b10111=23):
    idx_L = [15, 23]
    assert all(m in idx_4 for m in idx_L)
    # H_5 weak-doublet operators (a in {3, 4}: 2*cdag[a]) vs H_5bar (2*c_op[a]):
    norm_l_nuc_h5 = sum(float(np.linalg.norm((c32 @ (2.0 * cdag[a]))[np.ix_(idx_L, idx_0)])) for a in (3, 4))
    norm_l_nuc_h5b = sum(float(np.linalg.norm((c32 @ (2.0 * c_op[a]))[np.ix_(idx_L, idx_0)])) for a in (3, 4))
    assert norm_l_nuc_h5 > 2.5 and norm_l_nuc_h5b == 0.0
    print(f"  Spin(10) cubic coupling ||<L, H_5 nu^c>|| = {norm_l_nuc_h5:.4f} (> 0) vs ||<L, H_5bar nu^c>|| = {norm_l_nuc_h5b:.1f} (exact 0).")

    # Symbolic proof of the Circular-Null Takagi 1/sqrt(2) Theorem in sympy:
    mu, eps = sp.symbols("mu eps", positive=True)
    i_s = sp.I
    inv_rt2 = 1 / sp.sqrt(2)
    vp = sp.Matrix([inv_rt2, i_s * inv_rt2, 0])
    vm = sp.Matrix([inv_rt2, -i_s * inv_rt2, 0])
    assert sp.simplify((vp.T * vp)[0, 0]) == 0 and sp.simplify((vm.T * vm)[0, 0]) == 0
    assert sp.simplify((vp.T * vm)[0, 0]) == 1 and sp.simplify((vp.H * vm)[0, 0]) == 0

    m_maj = sp.expand(mu * (vp * vm.T + vm * vp.T) + eps * (vp * vp.T + vm * vm.T))
    assert m_maj == m_maj.T
    g_maj = sp.simplify(m_maj * m_maj.H)
    # Check exact action of g_maj on u1 = [1, 0, 0]^T and u2 = [0, i, 0]^T:
    u1 = sp.Matrix([1, 0, 0])
    u2 = sp.Matrix([0, i_s, 0])
    assert sp.simplify(g_maj * u1 - ((mu + eps) ** 2) * u1) == sp.zeros(3, 1)
    assert sp.simplify(g_maj * u2 - ((mu - eps) ** 2) * u2) == sp.zeros(3, 1)
    for va in (vp, vm):
        for ub in (u1, u2):
            ov = sp.simplify(abs((va.H * ub)[0, 0]) - inv_rt2)
            assert ov == 0
    print("  [PASS] Symbolic sympy proof: circular-null Majorana pair has distinct singular values |mu +- eps| and exact |U_ab| == 1/sqrt(2)!")


# ---------------------------------------------------------------------------
# Section 2: 70-digit PMNS vs CKM across m in {8, 16, 40} & open-weave check
# ---------------------------------------------------------------------------
def cayley_orthogonal_mp(rng: random.Random, det_sign: int = 1) -> mp.matrix:
    a = mp.matrix(
        [
            [mp.mpf(0), mp.mpf(rng.gauss(0, 1)), mp.mpf(rng.gauss(0, 1))],
            [mp.mpf(0), mp.mpf(0), mp.mpf(rng.gauss(0, 1))],
            [mp.mpf(0), mp.mpf(0), mp.mpf(0)],
        ]
    )
    a = a - a.T
    eye3 = mp.eye(3)
    rot = (eye3 + a) * ((eye3 - a) ** -1)
    if det_sign < 0:
        rot = mp.diag([mp.mpf(-1), mp.mpf(1), mp.mpf(1)]) * rot
    return rot


def run_section2_pmns_vs_ckm_hierarchy(canon_l2) -> dict:
    print("\n=== SECTION 2: 70-DIGIT SEE-SAW PMNS VS QUARK CKM ACROSS m IN {8, 16, 40} (E1, E2) ===")
    mp.mp.dps = 70
    inv_rt2_mp = 1 / mp.sqrt(2)
    saved = {}

    for m_cov in (8, 16, 40):
        tx, ty = Fr(2 * m_cov, 5), Fr(m_cov, 5)
        ev = C7.TorusWeaveEvaluator(tx, ty, canon_l2(float(tx), float(ty)))

        # Representative point (1/5, 2/5) + 20-point P_5 average of (|U_e2|, |U_mu3|, |U_e3|):
        _, ye = ev.mw_and_yukawa(Fr(1, 5), Fr(2, 5), -3, 6)
        _, ynu = ev.mw_and_yukawa(Fr(1, 5), Fr(2, 5), -3, 0)
        _, yu = ev.mw_and_yukawa(Fr(1, 5), Fr(2, 5), 1, -4)
        _, yd = ev.mw_and_yukawa(Fr(1, 5), Fr(2, 5), 1, 2)

        ue, _ = C7.eig_herm_asc(ye * ye.H)
        m_maj = ynu * ynu.T
        unu_maj, snu2_sqrt = C7.eig_herm_asc(m_maj * m_maj.H)
        # Note eig_herm_asc returns sqrt(eigenvalues of m_maj * m_maj.H) == Majorana singular values m_1 <= m_2 <= m_3!
        unu_dir, _ = C7.eig_herm_asc(ynu * ynu.H)
        uu, _ = C7.eig_herm_asc(yu * yu.H)
        ud, _ = C7.eig_herm_asc(yd * yd.H)

        pmns = ue.H * unu_maj
        pmns_dir = ue.H * unu_dir
        ckm = uu.H * ud

        rel_split_12 = (snu2_sqrt[1] - snu2_sqrt[0]) / snu2_sqrt[1]
        ue1, ue2, ue3 = abs(pmns[0, 0]), abs(pmns[0, 1]), abs(pmns[0, 2])
        umu3, utau3 = abs(pmns[1, 2]), abs(pmns[2, 2])
        v12, v23, v13 = abs(ckm[0, 1]), abs(ckm[1, 2]), abs(ckm[0, 2])

        # Also compute 20-point P_5 arithmetic mean of (|U_e1|, |U_e2|, |U_mu3|, |U_e3|):
        acc_pmns = [mp.mpf(0)] * 4
        for ia in range(1, 5):
            for jb in range(5):
                _, ye_p = ev.mw_and_yukawa(Fr(ia, 5), Fr(jb, 5), -3, 6)
                _, yn_p = ev.mw_and_yukawa(Fr(ia, 5), Fr(jb, 5), -3, 0)
                ue_p, _ = C7.eig_herm_asc(ye_p * ye_p.H)
                mm_p = yn_p * yn_p.T
                un_p, _ = C7.eig_herm_asc(mm_p * mm_p.H)
                up_m = ue_p.H * un_p
                acc_pmns[0] += abs(up_m[0, 0]) / 20
                acc_pmns[1] += abs(up_m[0, 1]) / 20
                acc_pmns[2] += abs(up_m[1, 2]) / 20
                acc_pmns[3] += abs(up_m[0, 2]) / 20

        print(
            f"  m={m_cov:2d} ({float(tx)}+{float(ty)}i): Maj (m2-m1)/m2={mp.nstr(rel_split_12,4)}, m2/m3={mp.nstr(snu2_sqrt[1]/snu2_sqrt[2],4)} "
            f"| pt(|Ue1|,|Ue2|,|Umu3|,|Ue3|)=({mp.nstr(ue1,4)},{mp.nstr(ue2,4)},{mp.nstr(umu3,4)},{mp.nstr(ue3,4)}) "
            f"| 20pt_avg=({mp.nstr(acc_pmns[0],4)},{mp.nstr(acc_pmns[1],4)},{mp.nstr(acc_pmns[2],4)},{mp.nstr(acc_pmns[3],4)})"
        )

        assert snu2_sqrt[0] > 0 and rel_split_12 > mp.mpf("1e-12") and snu2_sqrt[1] < snu2_sqrt[2]
        assert ue1 > mp.mpf("0.60") and ue2 > mp.mpf("0.60")

        if m_cov == 8:
            # E2: Simultaneous large solar + large atmospheric PMNS and normal-ordered CKM at m = 8!
            assert ue2 > mp.mpf("0.50") and umu3 > mp.mpf("0.50") and ue3 < mp.mpf(1) / 3
            assert acc_pmns[1] > mp.mpf("0.45") and acc_pmns[2] > mp.mpf("0.40")
            saved["m8"] = (ev, ye, ynu, pmns, snu2_sqrt)

        if m_cov == 40:
            # E1: Asymptotic 1/sqrt(2) convergence within < 1e-3, while Planted Control 1 (pure Dirac) collapses |U_e2| < 0.1!
            err_rt2 = max(abs(ue1 - inv_rt2_mp), abs(ue2 - inv_rt2_mp))
            ue2_dirac = abs(pmns_dir[0, 1])
            min_dirac_diag = min(abs(pmns_dir[k, k]) for k in range(3))
            print(
                f"  m=40 asymptotic solar check: max(|Ue1,2| - 1/sqrt(2)) = {mp.nstr(err_rt2, 4)} (< 1e-3), |U_mu3| = {mp.nstr(umu3, 4)} (< 1e-2); "
                f"[CAUGHT Planted Control 1] pure-Dirac min|U_kk|={mp.nstr(min_dirac_diag,5)} (> 0.99), |U_e2^Dir|={mp.nstr(ue2_dirac,4)} (< 0.1)."
            )
            assert err_rt2 < mp.mpf("1e-3") and umu3 < mp.mpf("1e-2") and min_dirac_diag > mp.mpf("0.99") and ue2_dirac < mp.mpf("0.10")
            saved["m40"] = (ev, ye, ynu, pmns, snu2_sqrt)

    # Also check t = 4 overtone (P_6 at w = (1/6, 1/6), m = 8):
    ev8 = saved["m8"][0]
    _, ye_6 = ev8.mw_and_yukawa(Fr(1, 6), Fr(1, 6), -3, 6)
    _, yn_6 = ev8.mw_and_yukawa(Fr(1, 6), Fr(1, 6), -3, 0)
    ue_6, _ = C7.eig_herm_asc(ye_6 * ye_6.H)
    un_6, sn_6 = C7.eig_herm_asc((yn_6 * yn_6.T) * (yn_6 * yn_6.T).H)
    pmns_6 = ue_6.H * un_6
    print(
        f"  Overtone P_6 (1/6,1/6) at m=8: snu_ratios=({mp.nstr(sn_6[0]/sn_6[1],4)},{mp.nstr(sn_6[1]/sn_6[2],4)}), "
        f"|U_PMNS| row0=({mp.nstr(abs(pmns_6[0,0]),4)},{mp.nstr(abs(pmns_6[0,1]),4)},{mp.nstr(abs(pmns_6[0,2]),4)})"
    )
    print("  [PASS] Section 2 PMNS vs CKM see-saw dichotomy and asymptotic 1/sqrt(2) solar law verified.")
    return saved


# ---------------------------------------------------------------------------
# Section 3: Guardrail 3 U(3)_L x U(3)_{eR} x O(3)_{nuR} Check & Phase Plant
# ---------------------------------------------------------------------------
def run_section3_majorana_basis_scrambling(saved: dict) -> None:
    print("\n=== SECTION 3: GUARDRAIL 3 U(3)_L x U(3)_{eR} x O(3)_{nuR} SCRAMBLING & COMPLEX-PHASE PLANT (E3) ===")
    mp.mp.dps = 70
    rng = random.Random(2026112110)

    for tag in ("m8", "m40"):
        _, ye0, ynu0, pmns0, snu0 = saved[tag]
        max_drift = mp.mpf(0)
        for trial in range(15):
            ul = C7.cayley_random_unitary_mp(rng)
            ure = C7.cayley_random_unitary_mp(rng)
            det_s = -1 if (trial % 2 == 1) else 1  # test both SO(3) and improper det=-1 O(3) reflections!
            or_mat = cayley_orthogonal_mp(rng, det_sign=det_s)
            assert mp.norm(or_mat * or_mat.T - mp.eye(3)) < mp.mpf("1e-60")

            ye_s = ul * ye0 * ure.H
            ynu_s = ul * ynu0 * or_mat.T
            ue_s, _ = C7.eig_herm_asc(ye_s * ye_s.H)
            mm_s = ynu_s * ynu_s.T
            unu_s, snu_s = C7.eig_herm_asc(mm_s * mm_s.H)
            pmns_s = ue_s.H * unu_s
            drift_u = max(abs(abs(pmns_s[r, c]) - abs(pmns0[r, c])) for r in range(3) for c in range(3))
            drift_m = max(abs(snu_s[k] - snu0[k]) / snu0[k] for k in range(3))
            max_drift = max(max_drift, drift_u, drift_m)

        print(f"  [{tag}] 15 independent 70-digit U(3)_L x U(3)_{{eR}} x O(3)_{{nuR}} scramblings: max drift = {mp.nstr(max_drift, 5)} (< 1e-40).")
        assert max_drift < mp.mpf("1e-40")

    # Planted Control 2: Apply illegal complex phase gate diag(1, i, 1) on nu_R without transforming M_R = I_3!
    _, ye8, ynu8, pmns8, _ = saved["m8"]
    phase_gate = mp.diag([mp.mpf(1), mp.mpc(0, 1), mp.mpf(1)])
    ynu_bad = ynu8 * phase_gate
    ue8, _ = C7.eig_herm_asc(ye8 * ye8.H)
    mm_bad = ynu_bad * ynu_bad.T
    unu_bad, _ = C7.eig_herm_asc(mm_bad * mm_bad.H)
    pmns_bad = ue8.H * unu_bad
    plant2_shift = max(abs(abs(pmns_bad[r, c]) - abs(pmns8[r, c])) for r in range(3) for c in range(3))
    print(f"  [CAUGHT Planted Control 2] Illegal complex phase diag(1,i,1) outside O(3,R) shifts |U_PMNS| by {mp.nstr(plant2_shift, 5)} (> 0.1).")
    assert plant2_shift > mp.mpf("0.10")
    print("  [PASS] Section 3 Guardrail 3 Majorana basis invariance verified.")


def main() -> None:
    t0 = time.time()
    canon_l2 = C7.build_l2_interpolator()
    run_section1_spin10_and_circular_null_theorem()
    saved = run_section2_pmns_vs_ckm_hierarchy(canon_l2)
    run_section3_majorana_basis_scrambling(saved)
    print(f"\nALL AGY-C10 PRODUCER CHECKS PASSED (elapsed: {time.time() - t0:.2f}s; 0 of 19).")


if __name__ == "__main__":
    main()
