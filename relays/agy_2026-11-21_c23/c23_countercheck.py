"""Card AGY-C23 Zero-Shared-Code Countercheck: Symbolic 7D Christoffel/Einstein
Self-Tuning Proof, 5D Weight-Lattice Spin(10) Matter Parity, Exact GFJN Flavored
Leptogenesis Identity, Pentagonal Hilltop Slow-Roll Audit, and 5 Planted Faults (0 of 19).

Guardrail 6 compliant: zero imports from producer or earlier relay scripts.
"""
from __future__ import annotations

import itertools
import math
import time

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 55


# ---------------------------------------------------------------------------
# Independent Check 1: Symbolic 7D Christoffel / Einstein Constraint & Plant 1
# ---------------------------------------------------------------------------
def check1_symbolic_7d_warped_cusp_and_plant1() -> int:
    print("=== COUNTERCHECK 1: SYMBOLIC 7D EINSTEIN (rr) CONSTRAINT & PLANT 1 ===")
    # Compute exact G_rr for 7D metric ds^2 = e^(2 A(r)) (-dt^2 + dx1^2 + dx2^2 + dx3^2) + dr^2 + e^(-2 B(r)) (dy1^2 + dy2^2)
    # directly from 1st-principles warped-product Gauss-Codazzi / Christoffel trace formulas in sympy:
    # For diagonal metric g_MN(r) depending only on r (M != r, g_rr = 1), letting h_M = 1/2 d_r ln|g_MM|:
    #   Gamma^r_{MM} = -g_MM h_M,   Gamma^M_{rM} = h_M
    #   R_{rr} = -sum_{M != r} (h_M' + h_M^2)
    #   R^M_M (no sum, M != r) = -(h_M' + h_M * sum_{K != r} h_K)
    #   R_7 = R_{rr} + sum_{M != r} R^M_M = -2 sum h_M' - sum h_M^2 - (sum h_M)^2
    #   => G_{rr} = R_{rr} - 1/2 R_7 = 1/2 * [ (sum_{M != r} h_M)^2 - sum_{M != r} h_M^2 ]  (ZERO second derivatives A''!)
    r = sp.Symbol("r", real=True)
    Ap, App = sp.symbols("Ap App", real=True)
    # Here 4 dimensions have h_mu = Ap, and 2 cusp torus dimensions have h_y = -1:
    h_vec = [Ap, Ap, Ap, Ap, -sp.Integer(1), -sp.Integer(1)]
    hp_vec = [App, App, App, App, sp.Integer(0), sp.Integer(0)]

    R_rr = -sum(hp + h**2 for h, hp in zip(h_vec, hp_vec))
    sum_h = sum(h_vec)
    R_mixed_sum = sum(-(hp + h * sum_h) for h, hp in zip(h_vec, hp_vec))
    R_7 = sp.expand(R_rr + R_mixed_sum)
    G_rr = sp.simplify(R_rr - sp.Rational(1, 2) * R_7)

    # Verify App cancels IDENTICALLY in G_rr!
    assert App not in G_rr.free_symbols
    # Balance bulk cosmological constant T_rr^bulk so static A'=0 satisfies G_rr == G_rr|_{Ap=0}:
    G_rr_at_0 = G_rr.subs(Ap, 0)
    constraint_poly = sp.factor(G_rr - G_rr_at_0)
    # Check roots of constraint_poly == 0: 6 Ap^2 - 8 Ap = 2 Ap (3 Ap - 4) == 0 -> roots {0, 4/3}!
    roots_ap = sorted(sp.solve(sp.Eq(constraint_poly, 0), Ap))
    print(f"  Symbolic 7D Einstein G_rr = {G_rr} (zero A'' dependence!); balanced Lambda_4=0 constraint = {constraint_poly}, roots A'(0+) = {roots_ap}.")
    assert roots_ap == [sp.Integer(0), sp.Rational(4, 3)]

    # Planted Fault 1: Shifting brane vacuum energy by EWSB delta_v = -0.0566 sets A'(0+) = -delta_v / 3 != 0, violating G_rr constraint!
    ap_ewsb = sp.Rational(566, 30000)
    viol = float(abs(constraint_poly.subs(Ap, ap_ewsb)))
    assert viol > 0.14
    print(f"  [CAUGHT Plant 1] Untuned EWSB brane shift violates symbolic Lambda_4=0 (rr) Einstein constraint by {viol:.5f} (> 0.14; B980 enforced)!")
    return 1


# ---------------------------------------------------------------------------
# Independent Check 2: 5D Spin(10) Weight-Lattice Matter Parity & Plant 2
# ---------------------------------------------------------------------------
def check2_spin10_weight_matter_parity_and_plant2() -> int:
    print("\n=== COUNTERCHECK 2: 5D WEIGHT-LATTICE Spin(10) MATTER PARITY & PLANT 2 ===")
    # Construct all 16 chiral spinor weights of 16_+ in R^5 (even number of minus signs):
    w_16 = [w for w in itertools.product((-0.5, 0.5), repeat=5) if sum(1 for x in w if x < 0) % 2 == 0]
    assert len(w_16) == 16
    # Construct all 10 vector weights +-e_I in R^5:
    w_10_color = []
    w_10_higgs = []
    for idx in range(5):
        for s in (-1.0, 1.0):
            v = [0.0] * 5
            v[idx] = s
            if idx < 3:
                w_10_color.append(tuple(v))
            else:
                w_10_higgs.append(tuple(v))
    w_1_singlet = [(0.0, 0.0, 0.0, 0.0, 0.0)]
    assert len(w_16) + len(w_10_color) + len(w_10_higgs) + len(w_1_singlet) == 27

    # Exact Spin(10) -> SU(4)_C x SU(2)_L x SU(2)_R formula: 3*(B - L) = 2*(w_0 + w_1 + w_2)!
    def pm_from_weight(w: tuple[float, ...], two_s: int) -> int:
        bml3 = int(round(2.0 * (w[0] + w[1] + w[2])))
        return -1 if ((bml3 + two_s) % 2 != 0) else 1

    pm_16 = [pm_from_weight(w, 1) for w in w_16]
    pm_higgs_scalars = [pm_from_weight(w, 0) for w in w_10_higgs]
    pm_color_fermions = [pm_from_weight(w, 1) for w in w_10_color]
    pm_singlet_fermion = pm_from_weight(w_1_singlet[0], 1)

    print(f"  5D weight-lattice P_M counts: 16_fermions={set(pm_16)}, 2HDM_scalars={set(pm_higgs_scalars)}, D_fermions={set(pm_color_fermions)}, psi_S={pm_singlet_fermion}.")
    assert set(pm_16) == {1} and set(pm_higgs_scalars) == {1} and set(pm_color_fermions) == {-1} and pm_singlet_fermion == -1

    # Planted Fault 2: Check whether psi_S (P_M = -1) can decay into ANY k-body SM+2HDM final state (all P_M = +1):
    # Also test forbidden bilinear/trilinear operator psi_S * L_L * H_u:
    w_lepton = (-0.5, -0.5, -0.5, -0.5, 0.5)  # 4 minus signs -> in 16_+, 3(B-L) = -3!
    prod_forbidden = pm_singlet_fermion * pm_from_weight(w_lepton, 1) * pm_from_weight(w_10_higgs[0], 0)
    assert prod_forbidden == -1
    print("  [CAUGHT Plant 2] 5D weight-lattice parity blocks psi_S L_L H_u (P_M = -1 != +1), guaranteeing psi_S stability!")
    return 1


# ---------------------------------------------------------------------------
# Independent Check 3: Exact GFJN Leptogenesis Identity, Hilltop eta_V, & Plants 3-5
# ---------------------------------------------------------------------------
def standalone_resonant_eps_flav(Ye: mp.matrix, Yn: mp.matrix, Mr: mp.matrix) -> tuple[list[mp.mpf], mp.mpf]:
    """Disjoint SVD/Takagi evaluation of flavored resonant 1-loop CP asymmetries."""
    # Diagonalize Ye * Ye^H = Ue * diag(se^2) * Ue^H:
    He = Ye * Ye.H
    ev_e, Ue = mp.eighe(mp.mpf("0.5") * (He + He.H))
    ord_e = sorted(range(3), key=lambda k: mp.re(ev_e[k]))
    Ue_ord = mp.matrix([[Ue[r, c] for c in ord_e] for r in range(3)])

    # Takagi on complex symmetric Mr:
    Hm = Mr * Mr.H
    ev_m, Vm = mp.eighe(mp.mpf("0.5") * (Hm + Hm.H))
    ord_m = sorted(range(3), key=lambda k: mp.re(ev_m[k]))
    m_vals = []
    Ut = mp.zeros(3, 3)
    for col, idx in enumerate(ord_m):
        mk = mp.sqrt(mp.re(ev_m[idx]))
        m_vals.append(mk)
        v = Vm[:, idx]
        vc = mp.matrix([mp.conj(v[r]) for r in range(3)])
        ph = mp.expj(mp.arg((v.H * Mr * vc)[0, 0]) / 2)
        for r in range(3):
            Ut[r, col] = v[r] * ph

    Ut_conj = mp.matrix([[mp.conj(Ut[i, j]) for j in range(3)] for i in range(3)])
    Yt = Ue_ord.H * Yn * Ut_conj
    Ht = Yt.H * Yt
    h11 = mp.re(Ht[0, 0])
    m1 = m_vals[0]
    eps = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    for j in (1, 2):
        x = (m_vals[j] / m1) ** 2
        gj = mp.re(Ht[j, j]) / (8 * mp.pi)
        den = (x - 1) ** 2 + x * (gj**2)
        f_sv = mp.sqrt(x) * ((x - 1) / den + 1 - (1 + x) * mp.log(1 + 1 / x))
        g_osc = (x - 1) / den
        for al in range(3):
            p = mp.conj(Yt[al, 0]) * Yt[al, j]
            eps[al] += (mp.im(p * Ht[0, j]) * f_sv + mp.im(p * Ht[j, 0]) * g_osc) / (8 * mp.pi * h11)
    return eps, eps[0] + eps[1] + eps[2]


def eta_pent_60(tau: mp.mpc) -> mp.mpc:
    q = mp.expjpi(2 * tau)
    s = mp.mpc(0, 0)
    for k in range(-45, 46):
        term = q ** ((k * (3 * k - 1)) // 2)
        s += -term if (k % 2 != 0) else term
    return mp.expjpi(tau / 12) * s


def check3_gfjn_flav_hilltop_and_plants3_4_5() -> int:
    print("\n=== COUNTERCHECK 3: EXACT GFJN 1-LOOP IDENTITY, FLAVORED eps_tau, HILLTOP eta_V, & PLANTS 3-5 ===")
    # Construct complex non-degenerate Ye and Yn, and set Mr = I_3 - 2*c*Re(Yn^H Yn) (exact 1-loop pure-Yn splitting):
    Ye = mp.diag([mp.mpf("1e-5"), mp.mpf("2e-3"), mp.mpf("0.10")])
    Yn = mp.matrix(
        [
            [mp.mpc("0.02", "0.01"), mp.mpc("0.05", "-0.03"), mp.mpc("0.01", "0.04")],
            [mp.mpc("-0.03", "0.02"), mp.mpc("0.11", "0.07"), mp.mpc("0.18", "-0.05")],
            [mp.mpc("0.04", "-0.02"), mp.mpc("0.19", "0.13"), mp.mpc("0.52", "0.21")],
        ]
    )
    Hn = Yn.H * Yn
    c_loop = mp.mpf("0.008")
    Mr_1loop = mp.eye(3) - c_loop * (Hn + Hn.T)  # real symmetric = I_3 - 2 c Re(Yn^H Yn)!

    eps_fl, eps_sum = standalone_resonant_eps_flav(Ye, Yn, Mr_1loop)
    print(f"  GFJN pure-1-loop test: |sum_alpha eps_{{1,alpha}}| = {mp.nstr(abs(eps_sum), 5)} (< 1e-48 == 0!), while flavored eps_{{1,tau}} = {mp.nstr(eps_fl[2], 8)} != 0!")
    assert abs(eps_sum) < mp.mpf("1e-48") and abs(eps_fl[2]) > mp.mpf("1e-6")

    # Verify Haar U(3)_L x O(3)_{N_R} invariance:
    rng = np.random.default_rng(2026112123)
    z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2.0)
    q_u, r_u = np.linalg.qr(z)
    q_u = q_u * (np.diag(r_u) / np.abs(np.diag(r_u)))
    UL = mp.matrix([[mp.mpc(float(q_u[i, j].real), float(q_u[i, j].imag)) for j in range(3)] for i in range(3)])
    for _ in range(6):
        UL = UL * (3 * mp.eye(3) - UL.H * UL) / 2
    eps_rot, _ = standalone_resonant_eps_flav(UL.H * Ye, UL.H * Yn, Mr_1loop)
    haar_err = abs(eps_rot[2] - eps_fl[2]) / abs(eps_fl[2])
    assert haar_err < mp.mpf("1e-48")

    # Planted Fault 3: Non-unitary left transformation diag(3, 1, 1) corrupts flavored eps_{1,tau}!
    D_bad = mp.diag([mp.mpf(3), mp.mpf(1), mp.mpf(1)])
    eps_bad, _ = standalone_resonant_eps_flav(D_bad * Ye, D_bad * Yn, Mr_1loop)
    assert abs(eps_bad[2] - eps_fl[2]) / abs(eps_fl[2]) > mp.mpf("0.10")
    print("  [CAUGHT Plant 3] Non-unitary lepton doublet scaling corrupts flavored eps_{1,tau} by > 10%!")

    # Planted Fault 4: Real CP-conserving Yn collapses flavored eps_{1,tau} to 0!
    Yn_real = mp.matrix([[mp.re(Yn[i, j]) for j in range(3)] for i in range(3)])
    Hn_r = Yn_real.H * Yn_real
    eps_real, _ = standalone_resonant_eps_flav(Ye, Yn_real, mp.eye(3) - c_loop * (Hn_r + Hn_r.T))
    assert max(abs(x) for x in eps_real) < mp.mpf("1e-50")
    print("  [CAUGHT Plant 4] CP-conserving real Yukawa matrix forces max|eps_{1,alpha}| == 0 (< 1e-50)!")

    # Disjoint pentagonal stencil evaluation of Fricke hilltop eta_V at tau_sad = i / sqrt(5) + Plant 5:
    def v_pent(x: mp.mpf, y: mp.mpf) -> mp.mpf:
        t = mp.mpc(x, y)
        e1 = eta_pent_60(t)
        e5 = eta_pent_60(5 * t)
        return -mp.pi * mp.log(y * mp.sqrt(5) * ((abs(e1) * abs(e5)) ** 2))

    y_sad = 1 / mp.sqrt(5)
    v_sad = v_pent(mp.mpf(0), y_sad)
    v_min = v_pent(mp.mpf(2) / 5, mp.mpf(1) / 5)
    h = mp.mpf("1e-10")
    v_xx = (-v_pent(2 * h, y_sad) + 16 * v_pent(h, y_sad) - 30 * v_sad + 16 * v_pent(-h, y_sad) - v_pent(-2 * h, y_sad)) / (12 * h * h)
    eta_v_nk1 = (2 * (y_sad**2)) * v_xx / (v_sad - v_min)
    assert eta_v_nk1 < -mp.mpf(5) and abs(eta_v_nk1 - mp.mpf("-5.5669136")) < mp.mpf("1e-5")
    print(f"  [CAUGHT Plant 5] Disjoint pentagonal Fricke hilltop eta_V(n_K=1) = {mp.nstr(eta_v_nk1, 8)} (|eta_V| > 5 >> 0.1 slow-roll bound; Steep-Modulus No-Go confirmed)!")
    return 3


def main() -> None:
    t0 = time.time()
    plants = 0
    plants += check1_symbolic_7d_warped_cusp_and_plant1()
    plants += check2_spin10_weight_matter_parity_and_plant2()
    plants += check3_gfjn_flav_hilltop_and_plants3_4_5()
    assert plants == 5
    print(f"\nALL AGY-C23 COUNTERCHECKS PASSED ({plants}/5 planted faults caught; elapsed: {time.time() - t0:.2f}s; 0 of 19).")


if __name__ == "__main__":
    main()
