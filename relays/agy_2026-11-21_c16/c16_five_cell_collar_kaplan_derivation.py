"""AGY-C16 Producer: Five-Cell Collar Kaplan-Dirac Derivation of Y_f(Y_f^H Y_f)^2 / (tr(Y_f^H Y_f))^2
and Gauge-Forced Neutrino Untwisting on X_{4_1}^{(40)} -> X_{4_1}^{(8)} (strictly 0 of 19).

Tests Pre-Registered Expectations E1, E2, E3 of Card AGY-C16:
  - Section 1 (E1): Exhaustive 125-assignment pure-Higgs Z_5 no-go vs exact 15x15 five-cell
    alternating-parity collar Dirac operator D_5 with Frobenius bulk mass M_{KK,f}^2 ~ tr(Y_f^H Y_f),
    symbolic sympy Schur/determinant identities, finite-epsilon CKM stability, and Planted Control 1a.
  - Section 2 (E2): Symbolic 10x10 and 45-digit 30x30 symmetric Weyl Dirac-Majorana unification
    with uniform M_0 on all G_SM-neutral (1,1)_0 states (both N^c_{1,3,5} and N_{1,3,L}), proving
    m_eff(nu_L) = (M_0/(M^2 - M_0^2)) v_u^2 Y_nu(8) Y_nu(8)^T + O(v_u^6) vs Planted Control 1b.
  - Section 3 (E3): Exact degree-1 scale homogeneity, removal of synthetic svd[2] / 0.80 literals,
    2-loop QCD lift of IR y_{d3}/y_{e3} > 1.5 (vs Planted Control 2), and 45-digit Haar U(3)^5 x O(3)_{nuR}.
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

RELAYS_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RELAYS_ROOT / "agy_2026-11-20_c7"))
sys.path.insert(0, str(RELAYS_ROOT / "agy_2026-11-21_c12"))
sys.path.insert(0, str(RELAYS_ROOT / "agy_2026-11-21_c14"))

import c7_selberg_lefschetz_weave as C7  # noqa: E402
import c12_weave_crossover_and_radial_profile as C12  # noqa: E402
import c14_2loop_2hdm_rge_and_tan_beta as C14  # noqa: E402


def build_m8_weave_yukawas(dps: int = 50) -> tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
    mp.mp.dps = dps
    canon_l2 = C7.build_l2_interpolator()
    cls12 = C7.enum_primitive_lyndon(12)
    w3 = sum(C12.selberg_class_weight(tr, mp.mpf(2)) for tr, _, _ in cls12 if tr == 3)
    w4 = sum(C12.selberg_class_weight(tr, mp.mpf(2)) for tr, _, _ in cls12 if tr == 4)
    om3, om4 = w3 / (w3 + w4), w4 / (w3 + w4)

    tx, ty = Fr(16, 5), Fr(8, 5)
    ev8 = C7.TorusWeaveEvaluator(tx, ty, canon_l2(float(tx), float(ty)))
    p3, p4 = (Fr(1, 5), Fr(2, 5)), (Fr(1, 6), Fr(1, 6))

    mats = []
    for ql, qr in ((1, -4), (1, 2), (-3, 6)):
        _, y3 = ev8.mw_and_yukawa(*p3, ql, qr)
        _, y4 = ev8.mw_and_yukawa(*p4, ql, qr)
        gj = C12.herm_exp_mp(om3 * C12.herm_log_mp(y3 * y3.H) + om4 * C12.herm_log_mp(y4 * y4.H))
        evs, u = mp.eighe(mp.mpf("0.5") * (gj + gj.H))
        mats.append(u * mp.diag([mp.sqrt(max(mp.mpf(0), x)) for x in evs]) * u.H)
    _, yn_raw = ev8.mw_and_yukawa(*p3, -3, 0)
    return mats[0], mats[1], mats[2], yn_raw


def trace_norm_d5_analytic(ym: mp.matrix, eps: mp.mpf = mp.mpf(1)) -> mp.matrix:
    gram = ym.H * ym
    tr_g = mp.re(gram[0, 0] + gram[1, 1] + gram[2, 2])
    return (eps**4) * (ym * (gram**2)) / (tr_g**2)


def build_15x15_charged_collar(ym: mp.matrix, eps: mp.mpf, wrap_eps: mp.mpf = mp.mpf(0)) -> tuple[mp.matrix, mp.mpf]:
    """Constructs the explicit 15x15 (5x3 block) Kaplan-Dirac operator D_5 on Walls 0..5."""
    gram = ym.H * ym
    tr_g = mp.re(gram[0, 0] + gram[1, 1] + gram[2, 2])
    m_kk = mp.sqrt(tr_g) / eps
    d15 = mp.zeros(15, 15)

    def put_blk(bi: int, bj: int, blk: mp.matrix) -> None:
        r0, c0 = 3 * bi, 3 * bj
        for r in range(3):
            for c in range(3):
                d15[r0 + r, c0 + c] += blk[r, c]

    for b in range(5):
        put_blk(b, b, ym if b % 2 == 0 else ym.H)
    i3 = mp.eye(3)
    for b in range(4):
        put_blk(b + 1, b, -m_kk * i3)
    if wrap_eps != 0:
        put_blk(0, 4, wrap_eps * ym)
    return d15, m_kk


def mp_solve_cols(mat_a: mp.matrix, mat_b: mp.matrix) -> mp.matrix:
    n_r, n_c = mat_b.rows, mat_b.cols
    out = mp.zeros(n_r, n_c)
    for c in range(n_c):
        col = mp.lu_solve(mat_a, mat_b[:, c])
        for r in range(n_r):
            out[r, c] = col[r]
    return out


def schur_15x15_light(d15: mp.matrix) -> mp.matrix:
    """Exact Schur complement of the 12x12 heavy interior collar block (rows 3..14, cols 0..11)."""
    d00 = d15[:3, 12:15]
    u_top = d15[:3, :12]
    m_h = d15[3:15, :12]
    v_rt = d15[3:15, 12:15]
    return d00 - u_top * mp_solve_cols(m_h, v_rt)


def build_30x30_neutral_weyl(
    yn: mp.matrix, vu: mp.mpf, m_kk: mp.mpf, m0_r: mp.mpf, m0_l: mp.mpf
) -> mp.matrix:
    """Explicit 30x30 symmetric Weyl mass matrix on Walls 0..5 for neutral leptons."""
    w30 = mp.zeros(30, 30)
    i3 = mp.eye(3)

    def put_sym(bi: int, bj: int, blk: mp.matrix) -> None:
        r0, c0 = 3 * bi, 3 * bj
        for r in range(3):
            for c in range(3):
                w30[r0 + r, c0 + c] += blk[r, c]
                if bi != bj:
                    w30[c0 + c, r0 + r] += blk[r, c]

    put_sym(0, 1, vu * yn)
    put_sym(2, 3, vu * yn.H)
    put_sym(4, 5, vu * yn)
    put_sym(6, 7, vu * yn.H)
    put_sym(8, 9, vu * yn)
    for b_odd, b_ev in ((1, 2), (3, 4), (5, 6), (7, 8)):
        put_sym(b_odd, b_ev, -m_kk * i3)
    for b_r in (1, 5, 9):
        put_sym(b_r, b_r, m0_r * i3)
    for b_l in (2, 6):
        put_sym(b_l, b_l, m0_l * i3)
    return w30


def schur_30x30_nu(w30: mp.matrix) -> mp.matrix:
    w00 = w30[:3, :3]
    v_col = w30[3:30, :3]
    w_h = w30[3:30, 3:30]
    return w00 - v_col.T * mp_solve_cols(w_h, v_col)


def svd_left_asc_mp(ym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    u_m, sv_m, _ = mp.svd_c(ym)
    ord_i = sorted(range(3), key=lambda k: sv_m[k])
    return mp.matrix([[u_m[r, ord_i[c]] for c in range(3)] for r in range(3)]), [sv_m[ord_i[c]] for c in range(3)]


# ---------------------------------------------------------------------------
# Section 1: Pure-Higgs Z_5 No-Go vs 15x15 Five-Cell Collar Operator D_5 (E1)
# ---------------------------------------------------------------------------
def run_section1_z5_nogo_and_d5_schur(yu8: mp.matrix, yd8: mp.matrix, ye8: mp.matrix) -> None:
    print("=== SECTION 1: PURE-HIGGS Z_5 NO-GO VS 15x15 FIVE-CELL COLLAR KAPLAN-DIRAC OPERATOR (E1, 0 of 19) ===")
    mp.mp.dps = 50
    separating = 0
    for ql in range(5):
        for qr in range(5):
            for qh in range(5):
                # Y_f has +qh, Y_f^H has -qh => Y_f (Y_f^H Y_f)^k has charge qh + k*(-qh + qh) == qh mod 5!
                c_k0 = (-ql + qh + qr) % 5
                c_k2 = (-ql + 3 * qh - 2 * qh + qr) % 5
                if c_k0 != 0 and c_k2 == 0:
                    separating += 1
    print(f"  Pure-Higgs Z_5 scan across 5^3 = 125 charge triples: {separating}/125 separate k=2 from k=0 (exact 0: pure-Higgs Z_5 no-go proved).")
    assert separating == 0

    # Symbolic sympy check of 5x5 Kaplan bidiagonal block:
    x, m1, m2, m3, m4, m_sym = sp.symbols("x M1 M2 M3 M4 M", positive=True)
    b5 = sp.Matrix([[x, 0, 0, 0, 0], [-m1, x, 0, 0, 0], [0, -m2, x, 0, 0], [0, 0, -m3, x, 0], [0, 0, 0, -m4, x]])
    sch_sym = sp.simplify(0 - (b5[0, :4] * b5[1:, :4].inv() * b5[1:, 4])[0, 0])
    assert sp.simplify(sch_sym - (x**5) / (m1 * m2 * m3 * m4)) == 0
    assert sp.simplify(b5.det() - x**5) == 0
    b5_eq = b5.subs({m1: m_sym, m2: m_sym, m3: m_sym, m4: m_sym})
    tr_inv_sq = sp.simplify(sp.trace(b5_eq.inv().T * b5_eq.inv()) - (m_sym**8 + 2 * m_sym**6 * x**2 + 3 * m_sym**4 * x**4 + 4 * m_sym**2 * x**6 + 5 * x**8) / x**10)
    assert tr_inv_sq == 0
    print("  Symbolic sympy check: Schur(B_5) == x^5/(M1 M2 M3 M4), det(B_5) == x^5, tr((B_5^T B_5)^(-1)) exact.")

    # 50-digit explicit 15x15 Schur complement & finite-epsilon CKM eigenvector alignment:
    max_schur_err = mp.mpf(0)
    for ym in (yu8, yd8, ye8):
        d15, _ = build_15x15_charged_collar(ym, mp.mpf("0.1"))
        m_sch = schur_15x15_light(d15)
        m_ana = trace_norm_d5_analytic(ym, mp.mpf("0.1"))
        max_schur_err = max(max_schur_err, mp.norm(m_sch - m_ana) / mp.norm(m_ana))
    print(f"  50-digit 15x15 Schur complement vs analytic Y_f(Y_f^H Y_f)^2/(tr(Y_f^H Y_f))^2: max rel err = {mp.nstr(max_schur_err, 4)} (< 1e-45).")
    assert max_schur_err < mp.mpf("1e-45")

    # Finite-epsilon exact 15x15 SVD light zero modes (Wall-0 chiral projection + full 15-component overlap):
    uu_ref, _ = svd_left_asc_mp(trace_norm_d5_analytic(yu8))
    ud_ref, _ = svd_left_asc_mp(trace_norm_d5_analytic(yd8))
    v_ref = uu_ref.H * ud_ref

    kk_shifts = {}
    for eps_str in ("0.05", "0.15"):
        eps_v = mp.mpf(eps_str)
        du15, _ = build_15x15_charged_collar(yu8, eps_v)
        dd15, _ = build_15x15_charged_collar(yd8, eps_v)
        uu15, svu15, _ = mp.svd_c(du15)
        ud15, svd15, _ = mp.svd_c(dd15)
        iu = sorted(range(15), key=lambda k: svu15[k])[:3]
        id_ = sorted(range(15), key=lambda k: svd15[k])[:3]
        # Normalized Wall-0 boundary chiral projections:
        uw_u = mp.matrix([[uu15[r, iu[c]] for c in range(3)] for r in range(3)])
        uw_d = mp.matrix([[ud15[r, id_[c]] for c in range(3)] for r in range(3)])
        for c in range(3):
            nu_c = mp.sqrt(sum(abs(uw_u[r, c]) ** 2 for r in range(3)))
            nd_c = mp.sqrt(sum(abs(uw_d[r, c]) ** 2 for r in range(3)))
            for r in range(3):
                uw_u[r, c] /= nu_c
                uw_d[r, c] /= nd_c
        vw = uw_u.H * uw_d
        wall0_drift = max(abs(abs(vw[r, c]) - abs(v_ref[r, c])) for r in range(3) for c in range(3))
        # Full 15-component overlap (scales as O(eps^2) = 9x between 0.05 and 0.15):
        uf_u = mp.matrix([[uu15[r, iu[c]] for c in range(3)] for r in range(15)])
        uf_d = mp.matrix([[ud15[r, id_[c]] for c in range(3)] for r in range(15)])
        vf = uf_u.H * uf_d
        full15_shift = max(abs(abs(vf[r, c]) - abs(v_ref[r, c])) for r in range(3) for c in range(3))
        kk_shifts[eps_str] = full15_shift
        print(f"  Finite eps={eps_str}: exact Wall-0 CKM drift = {mp.nstr(wall0_drift, 4)} (< 1e-40), full 15-state KK shift = {mp.nstr(full15_shift, 4)} (O(eps^2)).")
        assert wall0_drift < mp.mpf("1e-40") and full15_shift < mp.mpf("3e-3")
    assert mp.mpf("8.8") < (kk_shifts["0.15"] / kk_shifts["0.05"]) < mp.mpf("9.3")

    # Planted Control 1a: Periodic 0 ~ 5 wrap shortcut!
    d15_wrap, _ = build_15x15_charged_collar(yd8, mp.mpf("0.2"), wrap_eps=mp.mpf("0.2"))
    _, sv_wrap = svd_left_asc_mp(schur_15x15_light(d15_wrap))
    _, sv_open = svd_left_asc_mp(trace_norm_d5_analytic(yd8, mp.mpf("0.2")))
    r23_open = sv_open[1] / sv_open[2]
    r23_wrap = sv_wrap[1] / sv_wrap[2]
    print(f"  [CAUGHT Plant 1a] Periodic 0~5 wrap spoils 5-cell hierarchy: d-sector m2/m3 jumps from {mp.nstr(r23_open, 4)} to {mp.nstr(r23_wrap, 4)} (> 50x)!")
    assert r23_wrap > 50 * r23_open
    print("  [PASS] Section 1 five-cell collar Kaplan-Dirac theorem verified.")


# ---------------------------------------------------------------------------
# Section 2: Uniform 30x30 Neutral Weyl Unification (E2)
# ---------------------------------------------------------------------------
def run_section2_uniform_30x30_neutral_seesaw(
    yu8: mp.matrix, yd8: mp.matrix, ye8: mp.matrix, yn8: mp.matrix
) -> None:
    print("\n=== SECTION 2: UNIFORM 30x30 WEYL UNIFICATION OF CHARGED 5-STEP & NEUTRAL 1-STEP SEESAW (E2) ===")
    mp.mp.dps = 45
    y_s, m_s, m0_s = sp.symbols("y M M0", nonzero=True)

    def sym_10x10_meff(m_left):
        w = sp.zeros(10, 10)
        for i, j, val in ((0, 1, y_s), (2, 3, y_s), (4, 5, y_s), (6, 7, y_s), (8, 9, y_s), (1, 2, -m_s), (3, 4, -m_s), (5, 6, -m_s), (7, 8, -m_s)):
            w[i, j] = val
            w[j, i] = val
        for ir in (1, 5, 9):
            w[ir, ir] = m0_s
        for il in (2, 6):
            w[il, il] = m_left
        return sp.simplify(-(w[1:, 0].T * w[1:, 1:].inv() * w[1:, 0])[0, 0])

    meff_unif = sym_10x10_meff(m0_s)
    meff_no_ml = sym_10x10_meff(0)
    lead_coeff = sp.simplify(sp.diff(meff_unif, y_s, 2).subs(y_s, 0) / 2 - m0_s / (m_s**2 - m0_s**2))
    no_ml_deg2 = sp.simplify(sp.diff(meff_no_ml, y_s, 2).subs(y_s, 0))
    assert lead_coeff == 0 and no_ml_deg2 == 0
    print("  Symbolic 10x10 neutral check: uniform M_0 on (N^c_{1,3,5}, N_{1,3,L}) gives (M_0/(M^2-M_0^2)) y^2 + O(y^6); M_0=0 on N_L cancels to O(y^10)!")

    # 45-digit 30x30 explicit matrix evaluation:
    vu_v = mp.mpf("0.01")
    mkk_v = mp.mpf("1.0")
    m0_v = mp.mpf("2.5")
    w30_unif = build_30x30_neutral_weyl(yn8, vu_v, mkk_v, m0_v, m0_v)
    assert mp.norm(w30_unif - w30_unif.T) < mp.mpf("1e-42")
    mnu_30 = schur_30x30_nu(w30_unif)
    mnu_lead = (m0_v / (mkk_v**2 - m0_v**2)) * (vu_v**2) * (yn8 * yn8.T)
    rel_diff = mp.norm(mnu_30 - mnu_lead) / mp.norm(mnu_lead)

    # Planted Control 1b: Omitting M_0 on N_{1,3,L}:
    w30_bad = build_30x30_neutral_weyl(yn8, vu_v, mkk_v, m0_v, mp.mpf(0))
    mnu_bad = schur_30x30_nu(w30_bad)
    sup_ratio = mp.norm(mnu_bad) / mp.norm(mnu_30)
    print(f"  45-digit 30x30 Weinberg match at v_u/M_KK=0.01: rel_diff = {mp.nstr(rel_diff, 4)} (O(eps^4) < 1e-7).")
    print(f"  [CAUGHT Plant 1b] Omitting M_0 on N_{{1,3,L}} triggers inverse-seesaw suppression ||m_bad||/||m_unif|| = {mp.nstr(sup_ratio, 4)} (< 1e-14)!")
    assert rel_diff < mp.mpf("1e-7") and sup_ratio < mp.mpf("1e-14")

    # Verify simultaneous PMNS + CKM from uniform 30x30 collar architecture:
    ye_eff = trace_norm_d5_analytic(ye8)
    ue, _ = svd_left_asc_mp(ye_eff)
    un, _ = svd_left_asc_mp(mnu_30)
    upmns = ue.H * un
    print(f"  30x30 Collar PMNS moduli: (|U_e2|, |U_mu3|, |U_e3|) = ({mp.nstr(abs(upmns[0,1]),4)}, {mp.nstr(abs(upmns[1,2]),4)}, {mp.nstr(abs(upmns[0,2]),4)}).")
    assert abs(upmns[0, 1]) > mp.mpf("0.5") and abs(upmns[1, 2]) > mp.mpf("0.5") and mp.mpf("0.05") < abs(upmns[0, 2]) < mp.mpf("0.30")
    print("  [PASS] Section 2 uniform 30x30 charged/neutral collar unification verified.")


# ---------------------------------------------------------------------------
# Section 3: Degree-1 Homogeneity, 2-Loop IR y_d/y_e > 1.5, & 45-Digit Haar Audit (E3)
# ---------------------------------------------------------------------------
def run_section3_homogeneity_rge_and_haar(
    yu8: mp.matrix, yd8: mp.matrix, ye8: mp.matrix, yn8: mp.matrix
) -> None:
    print("\n=== SECTION 3: DEGREE-1 HOMOGENEITY, SVD-FREE 2-LOOP y_d/y_e LIFT, & 45-DIGIT HAAR AUDIT (E3) ===")
    mp.mp.dps = 45
    lam = mp.mpf("3.7")
    hom_err = mp.norm(trace_norm_d5_analytic(lam * yd8) - lam * trace_norm_d5_analytic(yd8)) / mp.norm(yd8)
    assert hom_err < mp.mpf("1e-42")

    yu_uv = trace_norm_d5_analytic(yu8)
    yd_uv = trace_norm_d5_analytic(yd8)
    ye_uv = trace_norm_d5_analytic(ye8)
    _, su_uv = svd_left_asc_mp(yu_uv)
    _, sd_uv = svd_left_asc_mp(yd_uv)
    _, se_uv = svd_left_asc_mp(ye_uv)
    r_de_uv = sd_uv[2] / se_uv[2]

    # Planted Control 2: Un-normalized M_KK = 1 (omitting Frobenius trace kinetic mass):
    _, sd_un = svd_left_asc_mp(yd8 * ((yd8.H * yd8) ** 2))
    _, se_un = svd_left_asc_mp(ye8 * ((ye8.H * ye8) ** 2))
    r_de_un = sd_un[2] / se_un[2]
    print(f"  Degree-1 homogeneity err = {mp.nstr(hom_err,4)}; trace-normalized UV y_d3/y_e3 = {mp.nstr(r_de_uv,5)} (in (0.5, 0.8)).")
    print(f"  [CAUGHT Plant 2] Omitting Frobenius trace mass collapses UV y_d3/y_e3 to {mp.nstr(r_de_un,5)} (< 0.20)!")
    assert mp.mpf("0.50") < r_de_uv < mp.mpf("0.80") and r_de_un < mp.mpf("0.20")

    # Verify 2-loop QCD lift of trace-normalized (zero-0.80, zero-svd[2]) Yukawas over 30 e-folds from alpha_GUT = 1/40:
    def to_np(m: mp.matrix) -> np.ndarray:
        return np.array([[complex(float(mp.re(m[r, c])), float(mp.im(m[r, c]))) for c in range(3)] for r in range(3)], dtype=np.complex128)

    g0 = np.array([math.sqrt(math.pi / 10.0)] * 3)
    st0 = (g0, to_np(yu_uv), to_np(yd_uv), to_np(ye_uv), to_np(yn8), np.array([1.0, 1.0]))
    _, yu_ir, yd_ir, ye_ir, _, _ = C14.rk4_integrate(st0, t_end=-30.0, n_steps=1000)
    _, sd_ir, se_ir, v12_ir, v23_ir, v13_ir = C14.ckm_and_svs(yu_ir, yd_ir, ye_ir)
    r_de_ir = float(sd_ir[2] / se_ir[2])
    print(f"  SVD-free 2-loop IR flow (alpha_GUT=1/40, N=30): IR y_d3/y_e3 = {r_de_ir:.4f} (> 1.50!), normal CKM ({v12_ir:.4f}>{v23_ir:.4f}>{v13_ir:.4f}).")
    assert r_de_ir > 1.50 and v12_ir > v23_ir > v13_ir

    # 45-digit simultaneous Haar U(3)^5 x O(3)_{nuR} scrambling directly on the 15x15 and 30x30 collar operators:
    def extract_16_collar_obs(yu_in: mp.matrix, yd_in: mp.matrix, ye_in: mp.matrix, yn_in: mp.matrix) -> list[mp.mpf]:
        du15, _ = build_15x15_charged_collar(yu_in, mp.mpf("0.1"))
        dd15, _ = build_15x15_charged_collar(yd_in, mp.mpf("0.1"))
        de15, _ = build_15x15_charged_collar(ye_in, mp.mpf("0.1"))
        w30 = build_30x30_neutral_weyl(yn_in, mp.mpf("0.01"), mp.mpf("1.0"), mp.mpf("2.5"), mp.mpf("2.5"))
        uu, su = svd_left_asc_mp(schur_15x15_light(du15))
        ud, sd = svd_left_asc_mp(schur_15x15_light(dd15))
        ue, se = svd_left_asc_mp(schur_15x15_light(de15))
        un, sn = svd_left_asc_mp(schur_30x30_nu(w30))
        vc, up = uu.H * ud, ue.H * un
        return [
            su[0] / su[2], su[1] / su[2], sd[0] / sd[2], sd[1] / sd[2], se[0] / se[2], se[1] / se[2],
            sd[2] / se[2], su[2] / sd[2],
            abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]),
            abs(up[0, 1]), abs(up[1, 2]), abs(up[0, 2]),
            sn[0] / sn[2], sn[1] / sn[2],
        ]

    obs_ref = extract_16_collar_obs(yu8, yd8, ye8, yn8)
    rng = random.Random(2026112117)
    max_haar_drift = mp.mpf(0)
    for _ in range(6):
        uq = C7.cayley_random_unitary_mp(rng)
        uru = C7.cayley_random_unitary_mp(rng)
        urd = C7.cayley_random_unitary_mp(rng)
        ul = C7.cayley_random_unitary_mp(rng)
        ure = C7.cayley_random_unitary_mp(rng)
        onr = C12.cayley_orthogonal_mp(rng)
        obs_rot = extract_16_collar_obs(uq * yu8 * uru.H, uq * yd8 * urd.H, ul * ye8 * ure.H, ul * yn8 * onr.T)
        max_haar_drift = max(max_haar_drift, max(abs(obs_rot[k] - obs_ref[k]) for k in range(16)))

    print(f"  Guardrail 3 (6 simultaneous 45-digit Haar U(3)^5 x O(3)_{{nuR}} scramblings on 15x15 & 30x30 operators): max drift = {mp.nstr(max_haar_drift, 4)} (< 1e-35).")
    assert max_haar_drift < mp.mpf("1e-35")
    print("  [PASS] Section 3 degree-1 homogeneity, SVD-free 2-loop lift, and 45-digit Haar invariance verified.")


def main() -> None:
    t0 = time.time()
    yu8, yd8, ye8, yn8 = build_m8_weave_yukawas(50)
    run_section1_z5_nogo_and_d5_schur(yu8, yd8, ye8)
    run_section2_uniform_30x30_neutral_seesaw(yu8, yd8, ye8, yn8)
    run_section3_homogeneity_rge_and_haar(yu8, yd8, ye8, yn8)
    print(f"\nALL AGY-C16 PRODUCER CHECKS PASSED (elapsed: {time.time() - t0:.2f}s; 0 of 19).")


if __name__ == "__main__":
    main()
