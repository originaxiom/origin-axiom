#!/usr/bin/env python3
"""
Independent Cold-Room Zero-Trust Referee for AGY-002 Card A2-OW9.

Pre-registration card:
  relays/cards/AGY-002_A2-OW9_kk-tower-cosmological-constant-and-dark-matter-stabilizer.md

Strictly disjoint numerical and algebraic methods:
  - OW9-A1: Explicit 8x8 6D Clifford algebra (Gamma^0..Gamma^6, Gamma_7, hat_iota)
            and explicit 2x2 KK Stueckelberg momentum projectors P_parallel, P_perp
            for M_4 x (T^2 / Z_2) parity and real d.o.f. counting.
  - OW9-A2: 55-dps Ewald / Terras incomplete-Gamma splitting for E_3(tau) (zero
            Chowla-Selberg / Bessel K), verified for splitting-parameter lambda
            invariance, unreduced SL_2(Z) modular invariance, R=25 direct lattice
            sum, proper-time Casimir quadrature, 4th-order Richardson gradient and
            Hessian, exact (3, 4, 5) Pythagorean interlocking, 6-coset compactified
            X_0(5) global scan, and 6-start 2D Nelder-Mead + damped Newton solver.
  - OW9-B1: Explicit PSL(2, F_5) = SL(2, F_5)/{+-I} (60 matrices over F_5) conjugacy
            classes, Lagrange subset-sum simplicity proof, and commutator subgroup;
            8-species P_M == (-1)^F check; bottom-up DP multiset G_SM x SL(2, C)
            dim <= 6 single-nu^c operator enumerator with SU(3) singlet verification.
  - OW9-B2: Exact Fraction Gaussian-norm Q(m, n) identity for |m|, |n| <= 6 and
            complete Q <= 10 shell census; direct trace-bounded {L, R, J} generator
            tree enumerating all 547 = 363 + 184 primitive hyperbolic GL(2, Z)
            classes (tr <= 50), independently cross-checked trace-by-trace against
            Gauss narrow class numbers h^+(D) of reduced indefinite binary quadratic
            forms; GL(2, F_2) action on all 547 classes, m004 3-cycle, and E[2]
            half-period democracy vs single-puncture (0, 0) breaking.
  - OW9-C:  All 4 planted faults (PF-OW9-1..4) evaluated directly via the referee
            operators (zero hardcoded flags).

Guardrails:
  - 0 float/complex AST literals.
  - 0 frontier/ imports (strict 0 of 19 empirical firewall).
  - 0 hardcoded boolean/zero proof flags.
"""

from collections import Counter
from fractions import Fraction
import json
import math
from pathlib import Path
import mpmath as mp
import sympy as sp


# ---------------------------------------------------------------------------
# Precision and exact tolerance helpers (zero float/complex AST literals)
# ---------------------------------------------------------------------------

WORK_DPS = 55
REPORT_DPS = 45
SCAN_DPS = 22
EWALD_CUT_HIGH = 140
EWALD_CUT_SCAN = 65


def inv_pow10(k):
    return mp.mpf(1) / (mp.mpf(10) ** k)


def mp_str(val, digits=REPORT_DPS):
    return mp.nstr(val, digits)


# ---------------------------------------------------------------------------
# OW9-A1: Exact T^2 / Z_2 KK-Tower Supertrace No-Go Theorem
# ---------------------------------------------------------------------------

def _kron(A, B):
    return sp.kronecker_product(A, B)


def verify_6d_weyl_orbifold_decomposition():
    """
    Construct explicit 8x8 6D Clifford matrices Gamma^0..Gamma^3, Gamma^5, Gamma^6
    with signature (+, -, -, -, -, -), chirality Gamma_7, 4D chirality Gamma_5_4D,
    and orbifold reflection hat_iota = -i Gamma^5 Gamma^6.
    Verify directly on the Gamma_7 = +1 eigenspace (dim 4) that hat_iota splits
    1 6D Weyl spinor into 1 even 4D Weyl (psi_L, 2 complex = 2 real on-shell dof)
    and 1 odd 4D Weyl (psi_R, 2 complex = 2 real on-shell dof).
    """
    I2 = sp.eye(2)
    I4 = sp.eye(4)
    I8 = sp.eye(8)
    Z8 = sp.zeros(8, 8)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])

    g0 = _kron(s1, I2)
    g1 = _kron(sp.I * s2, s1)
    g2 = _kron(sp.I * s2, s2)
    g3 = _kron(sp.I * s2, s3)
    g5_4d = sp.I * g0 * g1 * g2 * g3

    G = [
        _kron(g0, s1),
        _kron(g1, s1),
        _kron(g2, s1),
        _kron(g3, s1),
        _kron(I4, sp.I * s2),
        _kron(g5_4d, sp.I * s1),
    ]
    eta = [1, -1, -1, -1, -1, -1]

    clifford_ok = True
    for a in range(6):
        for b in range(6):
            anticomm = G[a] * G[b] + G[b] * G[a]
            target = 2 * eta[a] * I8 if a == b else Z8
            if anticomm != target:
                clifford_ok = False

    Gamma7 = G[0] * G[1] * G[2] * G[3] * G[4] * G[5]
    hat_iota = -sp.I * G[4] * G[5]
    G5_4d_lifted = _kron(g5_4d, I2)

    gamma7_sq_ok = (Gamma7 * Gamma7 == I8)
    iota_sq_ok = (hat_iota * hat_iota == I8)
    iota_comm_4d = all((hat_iota * G[mu] - G[mu] * hat_iota) == Z8 for mu in range(4))
    iota_anticomm_int = all((hat_iota * G[a] + G[a] * hat_iota) == Z8 for a in (4, 5))
    iota_comm_gamma7 = ((hat_iota * Gamma7 - Gamma7 * hat_iota) == Z8)

    # Basis of Gamma_7 = +1 eigenspace (6D positive-chirality Weyl spinor)
    plus_basis = (Gamma7 - I8).nullspace()
    dim_6d_weyl = len(plus_basis)
    B = sp.Matrix.hstack(*plus_basis)
    # Restricted operators on the 4-dim Gamma_7 = +1 subspace
    # Solve B * R = Op * B
    iota_restricted = B.pinv() * hat_iota * B
    g5_restricted = B.pinv() * G5_4d_lifted * B

    iota_eq_g5_on_weyl = (iota_restricted == g5_restricted)
    eigs_iota = iota_restricted.eigenvals()
    even_components = int(eigs_iota.get(sp.Integer(1), 0))
    odd_components = int(eigs_iota.get(sp.Integer(-1), 0))

    # Each 4D Weyl spinor has 2 complex components = 2 real on-shell helicity d.o.f.
    even_real_onshell_per_6d_weyl = even_components
    odd_real_onshell_per_6d_weyl = odd_components

    return {
        "clifford_algebra_6d_ok": bool(clifford_ok),
        "gamma7_sq_identity": bool(gamma7_sq_ok),
        "hat_iota_sq_identity": bool(iota_sq_ok),
        "hat_iota_commutes_4d_gammas": bool(iota_comm_4d),
        "hat_iota_anticommutes_56_gammas": bool(iota_anticomm_int),
        "hat_iota_commutes_gamma7": bool(iota_comm_gamma7),
        "dim_6d_weyl_subspace": dim_6d_weyl,
        "hat_iota_equals_4d_chirality_on_weyl": bool(iota_eq_g5_on_weyl),
        "even_4d_weyl_real_onshell_dof": even_real_onshell_per_6d_weyl,
        "odd_4d_weyl_real_onshell_dof": odd_real_onshell_per_6d_weyl,
    }


def verify_kk_stueckelberg_projectors():
    """
    For nonzero internal KK momentum k = (k5, k6) != (0, 0), construct explicit
    2x2 orthogonal projectors P_parallel = (k k^T)/|k|^2 (eaten Stueckelberg
    Goldstone from odd A_5, A_6) and P_perp = I - P_parallel (physical odd scalar).
    Verify over multiple sample nonzero KK modes using exact sympy rationals.
    """
    I2 = sp.eye(2)
    Z2 = sp.zeros(2, 2)
    sample_momenta = [(1, 0), (0, 1), (1, 1), (2, -1), (1, -2), (3, -4)]
    all_ok = True
    goldstone_rank_list = []
    physical_odd_rank_list = []

    for k5, k6 in sample_momenta:
        k = sp.Matrix([k5, k6])
        k2 = k5 * k5 + k6 * k6
        P_par = (k * k.T) / k2
        P_perp = I2 - P_par
        idemp = (P_par * P_par == P_par) and (P_perp * P_perp == P_perp)
        orth = (P_par * P_perp == Z2) and (P_perp * P_par == Z2)
        compl = (P_par + P_perp == I2)
        gauge_shift_par = (P_par * k == k)
        gauge_inv_perp = (P_perp * k == sp.Matrix([0, 0]))
        r_par = int(P_par.rank())
        r_perp = int(P_perp.rank())
        goldstone_rank_list.append(r_par)
        physical_odd_rank_list.append(r_perp)
        if not (idemp and orth and compl and gauge_shift_par and gauge_inv_perp and r_par == 1 and r_perp == 1):
            all_ok = False

    # Verify orbifold Fourier basis parity under y -> -y:
    # cos(k.(-y)) = +cos(k.y), sin(k.(-y)) = -sin(k.y), cos(0) = 1, sin(0) = 0.
    y_sym = sp.Symbol("y")
    k_sym = sp.Symbol("k")
    cos_even = (sp.cos(k_sym * (-y_sym)) == sp.cos(k_sym * y_sym))
    sin_odd = (sp.sin(k_sym * (-y_sym)) == -sp.sin(k_sym * y_sym))
    zero_mode_even = int(sp.cos(0))
    zero_mode_odd = int(sp.sin(0))

    return {
        "projectors_verified_all_samples": bool(all_ok),
        "eaten_goldstone_rank_per_generator": goldstone_rank_list[0],
        "physical_odd_scalar_rank_per_generator": physical_odd_rank_list[0],
        "cos_even_under_reflection": bool(cos_even),
        "sin_odd_under_reflection": bool(sin_odd),
        "zero_mode_cos_survival": zero_mode_even,
        "zero_mode_sin_survival": zero_mode_odd,
    }


def compute_kk_supertrace_spectrum(weyl_info, stueck_info, higgs_localization="bulk", gauge_internal_mode="full"):
    """
    Compute exact real bosonic and fermionic on-shell d.o.f. on M_4 x (T^2 / Z_2)
    at zero mode (0, 0) and at every nonzero unordered KK pair {(m, n), (-m, -n)}.
    """
    n_generations = 3
    spin10_chiral_dim = 16
    n_6d_weyl = n_generations * spin10_chiral_dim  # 48

    # G_SM = SU(3) x SU(2) x U(1): 8 + 3 + 1 = 12
    n_gauge = 8 + 3 + 1  # 12

    # 2H = 2 complex SU(2)_L doublets = 2 * 2 * 2 = 8 real scalars (even parity +1)
    n_higgs_real = 2 * 2 * 2  # 8

    # Zero-mode survival multipliers from explicit cos(0)=1, sin(0)=0
    surv_even_0 = stueck_info["zero_mode_cos_survival"]  # 1
    surv_odd_0 = stueck_info["zero_mode_sin_survival"]   # 0

    # 1. Fermions
    weyl_even_dof = weyl_info["even_4d_weyl_real_onshell_dof"]  # 2
    weyl_odd_dof = weyl_info["odd_4d_weyl_real_onshell_dof"]    # 2
    n_F_zero = n_6d_weyl * (weyl_even_dof * surv_even_0 + weyl_odd_dof * surv_odd_0)
    # Nonzero unordered pair: 1 cos mode (psi_L) + 1 sin mode (psi_R) -> 1 massive Dirac (4 real dof)
    n_F_pair = n_6d_weyl * (weyl_even_dof + weyl_odd_dof)
    n_F_lat = Fraction(n_F_pair, 2)

    # 2. Gauge bosons
    # A_mu (even): 2 massless transverse polarizations per generator
    n_gauge_transverse = 2
    n_B_gauge_zero_vec = n_gauge * n_gauge_transverse * surv_even_0
    n_B_gauge_zero_adj_scalar = n_gauge * (
        stueck_info["eaten_goldstone_rank_per_generator"]
        + stueck_info["physical_odd_scalar_rank_per_generator"]
    ) * surv_odd_0
    n_B_gauge_zero = n_B_gauge_zero_vec + n_B_gauge_zero_adj_scalar

    if gauge_internal_mode == "full":
        eaten_per_gen = stueck_info["eaten_goldstone_rank_per_generator"]      # 1
        phys_odd_per_gen = stueck_info["physical_odd_scalar_rank_per_generator"]  # 1
    elif gauge_internal_mode == "drop_A5_A6":
        eaten_per_gen = 0
        phys_odd_per_gen = 0
    else:
        raise ValueError("Unknown gauge_internal_mode")

    n_B_proca_pair = n_gauge * (n_gauge_transverse + eaten_per_gen)
    n_B_odd_scalar_pair = n_gauge * phys_odd_per_gen
    n_B_gauge_pair = n_B_proca_pair + n_B_odd_scalar_pair

    # 3. 2H Higgs scalars (even parity +1)
    n_B_higgs_zero = n_higgs_real * surv_even_0
    if higgs_localization == "bulk":
        n_B_higgs_pair = n_higgs_real
    elif higgs_localization == "brane":
        n_B_higgs_pair = 0
    else:
        raise ValueError("Unknown higgs_localization")

    n_B_zero = n_B_gauge_zero + n_B_higgs_zero
    n_B_pair = n_B_gauge_pair + n_B_higgs_pair
    n_B_lat = Fraction(n_B_pair, 2)

    str_zero = n_B_zero - n_F_zero
    str_pair = n_B_pair - n_F_pair
    str_lat = n_B_lat - n_F_lat

    return {
        "higgs_localization": higgs_localization,
        "gauge_internal_mode": gauge_internal_mode,
        "n_6d_weyl": n_6d_weyl,
        "n_gauge": n_gauge,
        "n_higgs_real": n_higgs_real,
        "zero_mode": {
            "n_B_gauge_vec": n_B_gauge_zero_vec,
            "n_B_gauge_adj_scalar": n_B_gauge_zero_adj_scalar,
            "n_B_higgs": n_B_higgs_zero,
            "n_B": n_B_zero,
            "n_F": n_F_zero,
            "n_B_minus_n_F": str_zero,
        },
        "kk_unordered_pair": {
            "n_B_proca": n_B_proca_pair,
            "n_B_odd_scalar": n_B_odd_scalar_pair,
            "n_B_gauge_total": n_B_gauge_pair,
            "n_B_higgs": n_B_higgs_pair,
            "n_B": n_B_pair,
            "n_F_massive_dirac_count": n_6d_weyl,
            "n_F": n_F_pair,
            "n_B_minus_n_F": str_pair,
        },
        "kk_per_T2_lattice_point": {
            "n_B": int(n_B_lat) if n_B_lat.denominator == 1 else str(n_B_lat),
            "n_F": int(n_F_lat) if n_F_lat.denominator == 1 else str(n_F_lat),
            "n_B_minus_n_F": int(str_lat) if str_lat.denominator == 1 else str(str_lat),
        },
    }


def run_ow9_a1():
    weyl_info = verify_6d_weyl_orbifold_decomposition()
    stueck_info = verify_kk_stueckelberg_projectors()
    bulk_2h = compute_kk_supertrace_spectrum(weyl_info, stueck_info, "bulk", "full")
    brane_2h = compute_kk_supertrace_spectrum(weyl_info, stueck_info, "brane", "full")

    passed = (
        weyl_info["clifford_algebra_6d_ok"]
        and weyl_info["hat_iota_equals_4d_chirality_on_weyl"]
        and stueck_info["projectors_verified_all_samples"]
        and bulk_2h["zero_mode"]["n_B"] == 32
        and bulk_2h["zero_mode"]["n_F"] == 96
        and bulk_2h["zero_mode"]["n_B_minus_n_F"] == -64
        and bulk_2h["zero_mode"]["n_B_gauge_adj_scalar"] == 0
        and bulk_2h["kk_unordered_pair"]["n_B_proca"] == 36
        and bulk_2h["kk_unordered_pair"]["n_B_odd_scalar"] == 12
        and bulk_2h["kk_unordered_pair"]["n_F"] == 192
        and bulk_2h["kk_unordered_pair"]["n_B_minus_n_F"] == -136
        and bulk_2h["kk_per_T2_lattice_point"]["n_B_minus_n_F"] == -68
        and brane_2h["kk_unordered_pair"]["n_B_minus_n_F"] == -144
        and brane_2h["kk_per_T2_lattice_point"]["n_B_minus_n_F"] == -72
        and bulk_2h["zero_mode"]["n_B_minus_n_F"] != 0
        and bulk_2h["kk_per_T2_lattice_point"]["n_B_minus_n_F"] != 0
        and brane_2h["kk_per_T2_lattice_point"]["n_B_minus_n_F"] != 0
    )

    return {
        "weyl_6d_clifford_check": weyl_info,
        "stueckelberg_projector_check": stueck_info,
        "bulk_2H": bulk_2h,
        "brane_2H": brane_2h,
        "pass": bool(passed),
    }


# ---------------------------------------------------------------------------
# OW9-A2: Ewald/Terras E_3(tau), Positive dS Casimir, & X_0(5) Stabilization
# ---------------------------------------------------------------------------

def sl2z_reduce(tau):
    """Map tau in H to the standard SL_2(Z) fundamental domain."""
    t = mp.mpc(tau)
    eps = inv_pow10(max(mp.mp.dps - 8, 10))
    for _ in range(200):
        k = int(mp.nint(mp.re(t)))
        t = t - k
        if abs(t) < mp.mpf(1) - eps:
            t = -mp.mpf(1) / t
        else:
            break
    return t


def E3_ewald_core(tau, lam, cut, reduce_first):
    """
    Exact Ewald / Terras incomplete-Gamma splitting for E_s(tau) at s = 3:
      pi^{-s} Gamma(s) E_s(tau)
        = lam^{s-1}/(s-1) - lam^s/s
          + sum'_{(m,n) != (0,0)} [ (pi Q)^{-s} Gamma(s, pi Q lam)
                                  + (pi Q)^{s-1} Gamma(1-s, pi Q / lam) ]
    where Q(m, n) = |m + n tau|^2 / Im(tau).
    Uses ZERO Chowla-Selberg / Bessel K functions.
    """
    t = sl2z_reduce(tau) if reduce_first else mp.mpc(tau)
    x = mp.re(t)
    y = mp.im(t)
    s = mp.mpf(3)
    pi = mp.pi
    lam_min = min(lam, mp.mpf(1) / lam)
    n_max = int(mp.ceil(mp.sqrt(cut / (pi * y * lam_min)))) + 1

    total = mp.mpf(0)
    for n in range(0, n_max + 1):
        rem = cut / (pi * lam_min) - (n * n) * y
        if rem < 0:
            rem = mp.mpf(0)
        m_rad = int(mp.ceil(mp.sqrt(rem * y))) + 2
        m_center = int(mp.nint(-n * x))
        m_lo = 1 if n == 0 else (m_center - m_rad)
        m_hi = m_center + m_rad
        for m in range(m_lo, m_hi + 1):
            Q = ((m + n * x) ** 2 + (n * y) ** 2) / y
            piQ = pi * Q
            term = (piQ ** (-s)) * mp.gammainc(s, piQ * lam) + (piQ ** (s - 1)) * mp.gammainc(1 - s, piQ / lam)
            total += 2 * term

    rhs = (lam ** (s - 1)) / (s - 1) - (lam ** s) / s + total
    return rhs * (pi ** s) / mp.gamma(s)


def E3_ewald(tau, lam=None, cut=EWALD_CUT_HIGH, reduce_first=True):
    if lam is None:
        lam = mp.mpf(1)
    return E3_ewald_core(tau, lam, mp.mpf(cut), reduce_first)


def F3_ewald(tau, cut=EWALD_CUT_HIGH):
    return E3_ewald(tau, cut=cut) + E3_ewald(5 * tau, cut=cut)


def E3_direct_sum(tau, R=25):
    x = mp.re(tau)
    y = mp.im(tau)
    y3 = y ** 3
    total = mp.mpf(0)
    for m in range(-R, R + 1):
        for n in range(-R, R + 1):
            if m == 0 and n == 0:
                continue
            d = (m + n * x) ** 2 + (n * y) ** 2
            total += y3 / (d ** 3)
    return total


def verify_casimir_proper_time_quadrature():
    """
    Independently verify by numerical quadrature (mp.quad) that the Poisson-resummed
    proper-time integral for 1 real bulk bosonic d.o.f. on unit-area T^2 yields
    exact prefactor -(1 / pi^3) * Q^{-3}:
      I(Q) = -(1/2) * (4 pi)^{-2} * (1/(4 pi)) * int_0^infty t^{-4} exp(-Q / (4 t)) dt
    Substitute u = 1/t (du = -dt/t^2, t^{-4} dt = u^2 du):
      I(Q) = -(1 / (128 pi^3)) * int_0^infty u^2 exp(-Q u / 4) du.
    """
    pref = -mp.mpf(1) / (128 * (mp.pi ** 3))
    max_err = mp.mpf(0)
    checked = {}
    for Q_int in (1, 2, 5):
        Q = mp.mpf(Q_int)
        quad_val = pref * mp.quad(lambda u: (u ** 2) * mp.exp(-Q * u / 4), [0, mp.inf])
        analytic_val = -(mp.mpf(1) / (mp.pi ** 3)) * (Q ** (-3))
        err = abs(quad_val - analytic_val)
        if err > max_err:
            max_err = err
        checked[f"Q={Q_int}"] = {
            "quad_val": mp_str(quad_val, 30),
            "analytic_val": mp_str(analytic_val, 30),
            "abs_err": mp_str(err, 10),
        }
    return {
        "samples": checked,
        "max_abs_err": mp_str(max_err, 10),
        "verified": bool(max_err < inv_pow10(25)),
    }


def richardson_grad_and_hessian(fn, x0, y0, h_grad, h_hess):
    """
    4th-order central finite-difference gradient and 4th-order Richardson Hessian
    evaluated at arbitrary precision.
    """
    def f(x, y):
        return fn(mp.mpc(x, y))

    # 4th-order gradient
    gx = (f(x0 - 2 * h_grad, y0) - 8 * f(x0 - h_grad, y0)
          + 8 * f(x0 + h_grad, y0) - f(x0 + 2 * h_grad, y0)) / (12 * h_grad)
    gy = (f(x0, y0 - 2 * h_grad) - 8 * f(x0, y0 - h_grad)
          + 8 * f(x0, y0 + h_grad) - f(x0, y0 + 2 * h_grad)) / (12 * h_grad)

    # 4th-order diagonal second derivatives
    f00 = f(x0, y0)
    hxx = (-f(x0 - 2 * h_hess, y0) + 16 * f(x0 - h_hess, y0) - 30 * f00
           + 16 * f(x0 + h_hess, y0) - f(x0 + 2 * h_hess, y0)) / (12 * (h_hess ** 2))
    hyy = (-f(x0, y0 - 2 * h_hess) + 16 * f(x0, y0 - h_hess) - 30 * f00
           + 16 * f(x0, y0 + h_hess) - f(x0, y0 + 2 * h_hess)) / (12 * (h_hess ** 2))

    # 4th-order Richardson extrapolation for mixed partial f_xy
    def D_xy(step):
        return (f(x0 + step, y0 + step) - f(x0 + step, y0 - step)
                - f(x0 - step, y0 + step) + f(x0 - step, y0 - step)) / (4 * (step ** 2))

    hxy = (4 * D_xy(h_hess) - D_xy(2 * h_hess)) / 3

    tr = hxx + hyy
    det = hxx * hyy - hxy * hxy
    disc = mp.sqrt(tr * tr - 4 * det)
    e1 = (tr - disc) / 2
    e2 = (tr + disc) / 2
    return {
        "gx": gx,
        "gy": gy,
        "grad_norm": mp.hypot(gx, gy),
        "hxx": hxx,
        "hyy": hyy,
        "hxy": hxy,
        "trace": tr,
        "det": det,
        "e1": e1,
        "e2": e2,
    }


def nelder_mead_2d(fn, x_start, y_start, step, max_iter, tol):
    """
    Disjoint 2D Nelder-Mead simplex minimizer strictly inside upper half-plane H (y > 0).
    Uses exact mpmath rational coefficients (zero float literals).
    """
    alpha = mp.mpf(1)
    gamma = mp.mpf(2)
    rho = mp.mpf(1) / 2
    sigma = mp.mpf(1) / 2
    big = mp.mpf("inf")

    def eval_safe(pt):
        if pt[1] <= inv_pow10(12):
            return big
        return fn(mp.mpc(pt[0], pt[1]))

    p0 = (x_start, y_start)
    p1 = (x_start + step, y_start)
    p2 = (x_start, y_start + step)
    simplex = [(eval_safe(p), p) for p in (p0, p1, p2)]

    for _ in range(max_iter):
        simplex.sort(key=lambda item: item[0])
        f_best, p_best = simplex[0]
        f_mid, p_mid = simplex[1]
        f_worst, p_worst = simplex[2]

        diam = max(
            mp.hypot(p_mid[0] - p_best[0], p_mid[1] - p_best[1]),
            mp.hypot(p_worst[0] - p_best[0], p_worst[1] - p_best[1]),
        )
        if diam < tol and abs(f_worst - f_best) < tol:
            break

        cx = (p_best[0] + p_mid[0]) / 2
        cy = (p_best[1] + p_mid[1]) / 2

        pr = (cx + alpha * (cx - p_worst[0]), cy + alpha * (cy - p_worst[1]))
        fr = eval_safe(pr)

        if f_best <= fr < f_mid:
            simplex[2] = (fr, pr)
            continue

        if fr < f_best:
            pe = (cx + gamma * (pr[0] - cx), cy + gamma * (pr[1] - cy))
            fe = eval_safe(pe)
            if fe < fr:
                simplex[2] = (fe, pe)
            else:
                simplex[2] = (fr, pr)
            continue

        # Contraction
        if fr < f_worst:
            pc = (cx + rho * (pr[0] - cx), cy + rho * (pr[1] - cy))
            fc = eval_safe(pc)
            if fc <= fr:
                simplex[2] = (fc, pc)
                continue
        else:
            pc = (cx + rho * (p_worst[0] - cx), cy + rho * (p_worst[1] - cy))
            fc = eval_safe(pc)
            if fc < f_worst:
                simplex[2] = (fc, pc)
                continue

        # Shrink
        new_p1 = (p_best[0] + sigma * (p_mid[0] - p_best[0]),
                  p_best[1] + sigma * (p_mid[1] - p_best[1]))
        new_p2 = (p_best[0] + sigma * (p_worst[0] - p_best[0]),
                  p_best[1] + sigma * (p_worst[1] - p_best[1]))
        simplex = [(f_best, p_best), (eval_safe(new_p1), new_p1), (eval_safe(new_p2), new_p2)]

    simplex.sort(key=lambda item: item[0])
    return simplex[0][1][0], simplex[0][1][1], simplex[0][0]


def damped_newton_2d(fn, x0, y0, max_iter=15):
    """
    2D damped Newton polish with Armijo backtracking and Levenberg shift
    when Hessian is not positive-definite.
    """
    x, y = mp.mpf(x0), mp.mpf(y0)
    h_g = inv_pow10(8)
    h_h = inv_pow10(6)
    f_cur = fn(mp.mpc(x, y))

    for _ in range(max_iter):
        gh = richardson_grad_and_hessian(fn, x, y, h_g, h_h)
        if gh["grad_norm"] < inv_pow10(22):
            break
        hxx, hyy, hxy = gh["hxx"], gh["hyy"], gh["hxy"]
        gx, gy = gh["gx"], gh["gy"]
        # Ensure positive-definite step matrix (H + mu I)
        mu = mp.mpf(0)
        if gh["e1"] <= 0:
            mu = -gh["e1"] + mp.mpf(1)
        a11 = hxx + mu
        a22 = hyy + mu
        det = a11 * a22 - hxy * hxy
        dx = -(a22 * gx - hxy * gy) / det
        dy = -(-hxy * gx + a11 * gy) / det

        step = mp.mpf(1)
        accepted = False
        for _bt in range(30):
            xn = x + step * dx
            yn = y + step * dy
            if yn > inv_pow10(10):
                fn_val = fn(mp.mpc(xn, yn))
                if fn_val <= f_cur:
                    x, y, f_cur = xn, yn, fn_val
                    accepted = True
                    break
            step = step / 2
        if not accepted:
            break

    return x, y, f_cur


def gamma0_5_right_cosets():
    r"""
    Return the 6 right coset representatives of Gamma_0(5) \ SL_2(Z):
      I = [[1, 0], [0, 1]] and S T^k = [[0, -1], [1, k]] for k = 0..4,
    together with verification that their projective bottom rows span all 6 points of P^1(F_5).
    """
    reps = [
        ("I", (1, 0, 0, 1)),
        ("S", (0, -1, 1, 0)),
        ("ST", (0, -1, 1, 1)),
        ("ST^2", (0, -1, 1, 2)),
        ("ST^3", (0, -1, 1, 3)),
        ("ST^4", (0, -1, 1, 4)),
    ]
    # Verify det == 1 and pairwise distinct right cosets Gamma_0(5) g_i
    det_ok = all((a * d - b * c) == 1 for _, (a, b, c, d) in reps)
    p1_pts = set()
    for _, (_a, _b, c, d) in reps:
        c5, d5 = c % 5, d % 5
        if c5 != 0:
            inv_c = pow(c5, -1, 5)
            p1_pts.add((1, (d5 * inv_c) % 5))
        else:
            p1_pts.add((0, 1))
    distinct_ok = (len(p1_pts) == 6)
    return reps, bool(det_ok and distinct_ok)


def mobius(M, tau):
    a, b, c, d = M
    return (a * tau + b) / (c * tau + d)


def run_ow9_a2(a1_res):
    mp.mp.dps = WORK_DPS

    quad_check = verify_casimir_proper_time_quadrature()

    i_pt = mp.mpc(0, 1)
    rho_pt = mp.mpc(-1, mp.sqrt(3)) / 2
    tau_plus = mp.mpc(2, 1) / 5
    tau_minus = mp.mpc(-2, 1) / 5
    two_plus_i = mp.mpc(2, 1)
    i_div_sqrt5 = mp.mpc(0, 1) / mp.sqrt(5)
    i_mul_sqrt5 = mp.mpc(0, mp.sqrt(5))

    # 1. Ewald splitting-parameter lambda invariance test (lam=1 vs lam=3/2)
    e3_i_lam1 = E3_ewald(i_pt, lam=mp.mpf(1))
    e3_i_lam32 = E3_ewald(i_pt, lam=mp.mpf(3) / 2)
    lam_invariance_err = abs(e3_i_lam1 - e3_i_lam32)

    # 2. Evaluate E_3 at all 6 benchmark points: reduced Ewald, unreduced Ewald, and direct sum R=25
    bench_pts = [
        ("i", i_pt),
        ("rho", rho_pt),
        ("(2+i)/5", tau_plus),
        ("2+i", two_plus_i),
        ("i/sqrt(5)", i_div_sqrt5),
        ("i*sqrt(5)", i_mul_sqrt5),
    ]
    bench_table = {}
    max_direct_diff = mp.mpf(0)
    max_unreduced_diff = mp.mpf(0)
    for name, pt in bench_pts:
        val_red = E3_ewald(pt, reduce_first=True)
        val_unred = E3_ewald(pt, reduce_first=False)
        val_dir = E3_direct_sum(pt, R=25)
        diff_dir = abs(val_red - val_dir)
        diff_unred = abs(val_red - val_unred)
        if diff_dir > max_direct_diff:
            max_direct_diff = diff_dir
        if diff_unred > max_unreduced_diff:
            max_unreduced_diff = diff_unred
        bench_table[name] = {
            "E3_ewald_45dps": mp_str(val_red, REPORT_DPS),
            "E3_ewald_unreduced_diff": mp_str(diff_unred, 10),
            "E3_direct_R25": mp_str(val_dir, 20),
            "abs_diff_ewald_vs_R25": mp_str(diff_dir, 10),
        }

    e3_i = E3_ewald(i_pt, reduce_first=False)
    e3_rho = E3_ewald(rho_pt, reduce_first=False)
    e3_tplus = E3_ewald(tau_plus, reduce_first=False)
    e3_2pi = E3_ewald(two_plus_i, reduce_first=False)

    # Non-trivial unreduced modular equality checks (no circular reduction!)
    diff_tplus_i = abs(e3_tplus - e3_i)
    diff_2pi_i = abs(e3_2pi - e3_i)
    ref_e3_i = mp.mpf(46589136156) / (mp.mpf(10) ** 10)
    ref_e3_rho = mp.mpf(41412565472) / (mp.mpf(10) ** 10)
    err_ref_i = abs(e3_i - ref_e3_i)
    err_ref_rho = abs(e3_rho - ref_e3_rho)

    # 3. Positive dS Casimir energy density from OW9-A1 lattice-point supertrace
    str_bulk = a1_res["bulk_2H"]["kk_per_T2_lattice_point"]["n_B_minus_n_F"]    # -68
    str_brane = a1_res["brane_2H"]["kk_per_T2_lattice_point"]["n_B_minus_n_F"]  # -72
    rho_1B_at_i = -(mp.mpf(1) / (mp.pi ** 3)) * e3_i
    rho_1F_at_i = +(mp.mpf(1) / (mp.pi ** 3)) * e3_i
    rho_casimir_bulk = mp.mpf(str_bulk) * rho_1B_at_i
    rho_casimir_brane = mp.mpf(str_brane) * rho_1B_at_i

    # 4. Saddle of E_3 at tau = i (4th-order Richardson + Maass Laplacian identity check)
    h_grad = inv_pow10(8)
    h_hess = inv_pow10(6)
    gh_i = richardson_grad_and_hessian(E3_ewald, mp.mpf(0), mp.mpf(1), h_grad, h_hess)
    a_saddle = gh_i["hxx"]
    b_saddle = gh_i["hyy"]
    laplacian_residual_i = abs((a_saddle + b_saddle) - 6 * e3_i)

    # 5. Gradient, Hessian, and exact (3, 4, 5) Pythagorean interlocking at tau_*^{+-}
    gh_plus = richardson_grad_and_hessian(F3_ewald, mp.mpf(2) / 5, mp.mpf(1) / 5, h_grad, h_hess)
    gh_minus = richardson_grad_and_hessian(F3_ewald, -mp.mpf(2) / 5, mp.mpf(1) / 5, h_grad, h_hess)

    # Conformal map gamma_+(tau) = 2 - 1/tau -> gamma_+'(tau_*^+) = 1 / (tau_*^+)^2 = 3 - 4i
    gamma_prime_plus = mp.mpf(1) / (tau_plus ** 2)
    gamma_prime_minus = mp.mpf(1) / (tau_minus ** 2)
    sin2_theta_plus = (mp.im(gamma_prime_plus) ** 2) / (abs(gamma_prime_plus) ** 2)
    sin2_theta_exact = mp.mpf(16) / 25
    sin2_theta_err = abs(sin2_theta_plus - sin2_theta_exact)

    tr_analytic = 50 * (a_saddle + b_saddle)
    det_analytic = 625 * (4 * a_saddle * b_saddle + sin2_theta_exact * ((b_saddle - a_saddle) ** 2))
    tr_rel_err_plus = abs(gh_plus["trace"] - tr_analytic) / abs(tr_analytic)
    det_rel_err_plus = abs(gh_plus["det"] - det_analytic) / abs(det_analytic)
    tr_rel_err_minus = abs(gh_minus["trace"] - tr_analytic) / abs(tr_analytic)
    det_rel_err_minus = abs(gh_minus["det"] - det_analytic) / abs(det_analytic)

    # 6. 6-coset Gamma_0(5) images of rho and W_5-fixed i / sqrt(5)
    f3_star = F3_ewald(tau_plus)
    f3_star_minus = F3_ewald(tau_minus)
    two_e3_i = 2 * e3_i
    f3_i_sqrt5 = F3_ewald(i_div_sqrt5)

    cosets, cosets_valid = gamma0_5_right_cosets()
    rho_coset_vals = []
    for label, M in cosets:
        z_img = mobius(M, rho_pt)
        val = F3_ewald(z_img)
        rho_coset_vals.append({
            "coset": label,
            "tau_re": mp_str(mp.re(z_img), 20),
            "tau_im": mp_str(mp.im(z_img), 20),
            "F3": mp_str(val, 25),
            "F3_mpf": val,
        })
    min_rho_coset = min(item["F3_mpf"] for item in rho_coset_vals)
    gap_rho = min_rho_coset - f3_star
    gap_i_sqrt5 = f3_i_sqrt5 - f3_star

    # 7. Analytic compactification bound for y >= 2 on SL_2(Z) fundamental domain D:
    #    F_3(g_j(tau)) > E_3(tau) > 2 * zeta(6) * y^3 >= 16 * zeta(6) > F_3(tau_*^{+-}).
    y_cut = mp.mpf(2)
    analytic_y_ge_2_lower_bound = 2 * mp.zeta(6) * (y_cut ** 3)
    compactification_bound_beats_star = (analytic_y_ge_2_lower_bound > f3_star)

    # 8. Unbiased global 6-coset grid scan over compact fundamental domain D_{y <= 2}
    mp.mp.dps = SCAN_DPS
    grid_nx = 16
    grid_ny = 14
    best_grid_val = mp.mpf("inf")
    best_grid_tau = None
    best_grid_coset = None
    n_grid_evals = 0
    for ix in range(grid_nx + 1):
        x = -mp.mpf(1) / 2 + mp.mpf(ix) / grid_nx
        y_lo = mp.sqrt(mp.mpf(1) - x * x)
        for iy in range(grid_ny + 1):
            y = y_lo + (mp.mpf(2) - y_lo) * mp.mpf(iy) / grid_ny
            base_tau = mp.mpc(x, y)
            for label, M in cosets:
                z = mobius(M, base_tau)
                val = F3_ewald(z, cut=EWALD_CUT_SCAN)
                n_grid_evals += 1
                if val < best_grid_val:
                    best_grid_val = val
                    best_grid_tau = z
                    best_grid_coset = label

    # 9. Disjoint multi-start 2D Nelder-Mead (scan dps) + damped Newton polish (55 dps)
    #    6 distinct unbiased starting points across X_0(5) (none equal to tau_*^{+-})
    starts = [
        ("start_1", mp.mpf(1) / 5, mp.mpf(2) / 5),
        ("start_2", -mp.mpf(1) / 5, mp.mpf(2) / 5),
        ("start_3", mp.mpf(1) / 10, mp.mpf(4) / 10),
        ("start_4", -mp.mpf(1) / 10, mp.mpf(4) / 10),
        ("start_5", mp.mpf(3) / 5, mp.mpf(1) / 4),
        ("start_6", -mp.mpf(3) / 5, mp.mpf(1) / 4),
    ]
    opt_runs = []
    max_opt_f3_err = mp.mpf(0)
    max_opt_grad = mp.mpf(0)
    for label, sx, sy in starts:
        mp.mp.dps = SCAN_DPS
        x_nm, y_nm, _f_nm = nelder_mead_2d(
            lambda z: F3_ewald(z, cut=EWALD_CUT_SCAN),
            sx,
            sy,
            step=mp.mpf(1) / 20,
            max_iter=200,
            tol=inv_pow10(8),
        )
        mp.mp.dps = WORK_DPS
        x_opt, y_opt, f_opt = damped_newton_2d(F3_ewald, x_nm, y_nm, max_iter=15)
        gh_opt = richardson_grad_and_hessian(F3_ewald, x_opt, y_opt, h_grad, h_hess)
        f_err = abs(f_opt - two_e3_i)
        if f_err > max_opt_f3_err:
            max_opt_f3_err = f_err
        if gh_opt["grad_norm"] > max_opt_grad:
            max_opt_grad = gh_opt["grad_norm"]
        # Verify E_3(tau_opt) == E_3(i) and E_3(5 tau_opt) == E_3(i)
        e_opt_1 = abs(E3_ewald(mp.mpc(x_opt, y_opt)) - e3_i)
        e_opt_5 = abs(E3_ewald(5 * mp.mpc(x_opt, y_opt)) - e3_i)
        opt_runs.append({
            "label": label,
            "start_re": mp_str(sx, 10),
            "start_im": mp_str(sy, 10),
            "opt_re": mp_str(x_opt, 25),
            "opt_im": mp_str(y_opt, 25),
            "F3_opt": mp_str(f_opt, 30),
            "abs_diff_from_2E3i": mp_str(f_err, 10),
            "grad_norm": mp_str(gh_opt["grad_norm"], 10),
            "e1": mp_str(gh_opt["e1"], 15),
            "e2": mp_str(gh_opt["e2"], 15),
            "E3_tau_minus_E3i": mp_str(e_opt_1, 10),
            "E3_5tau_minus_E3i": mp_str(e_opt_5, 10),
        })

    # Refine global grid best point at 55 dps as well
    mp.mp.dps = WORK_DPS
    gx_opt, gy_opt, gf_opt = damped_newton_2d(
        F3_ewald, mp.re(best_grid_tau), mp.im(best_grid_tau), max_iter=15
    )
    grid_best_diff = abs(gf_opt - two_e3_i)

    passed = (
        quad_check["verified"]
        and lam_invariance_err < inv_pow10(45)
        and max_unreduced_diff < inv_pow10(40)
        and max_direct_diff < inv_pow10(4)
        and diff_tplus_i < inv_pow10(35)
        and diff_2pi_i < inv_pow10(35)
        and err_ref_i < inv_pow10(9)
        and err_ref_rho < inv_pow10(9)
        and e3_rho < e3_i
        and rho_1B_at_i < 0
        and rho_1F_at_i > 0
        and rho_casimir_bulk > 0
        and rho_casimir_brane > 0
        and a_saddle < -7
        and b_saddle > 35
        and (a_saddle * b_saddle) < 0
        and laplacian_residual_i < inv_pow10(20)
        and gh_plus["grad_norm"] < inv_pow10(11)
        and gh_minus["grad_norm"] < inv_pow10(11)
        and sin2_theta_err < inv_pow10(45)
        and gh_plus["e1"] > 60
        and gh_plus["e2"] > 1300
        and gh_minus["e1"] > 60
        and gh_minus["e2"] > 1300
        and tr_rel_err_plus < inv_pow10(7)
        and det_rel_err_plus < inv_pow10(7)
        and tr_rel_err_minus < inv_pow10(7)
        and det_rel_err_minus < inv_pow10(7)
        and cosets_valid
        and min_rho_coset > mp.mpf(114) / 10
        and gap_rho > 2
        and f3_i_sqrt5 > mp.mpf(464) / 10
        and gap_i_sqrt5 > 37
        and compactification_bound_beats_star
        and best_grid_val >= f3_star - inv_pow10(12)
        and grid_best_diff < inv_pow10(10)
        and max_opt_f3_err < inv_pow10(10)
        and max_opt_grad < inv_pow10(11)
    )

    return {
        "method": "ewald_terras_incomplete_gamma_splitting_plus_nelder_mead_damped_newton",
        "proper_time_quadrature_check": quad_check,
        "ewald_lambda_invariance_err": mp_str(lam_invariance_err, 10),
        "max_unreduced_vs_reduced_err": mp_str(max_unreduced_diff, 10),
        "max_ewald_vs_direct_R25_err": mp_str(max_direct_diff, 10),
        "benchmarks": bench_table,
        "modular_equalities": {
            "E3_i": mp_str(e3_i, REPORT_DPS),
            "E3_rho": mp_str(e3_rho, REPORT_DPS),
            "abs_E3_tplus_minus_E3_i_unreduced": mp_str(diff_tplus_i, 10),
            "abs_E3_2plusi_minus_E3_i_unreduced": mp_str(diff_2pi_i, 10),
            "abs_E3_i_minus_ref": mp_str(err_ref_i, 10),
            "abs_E3_rho_minus_ref": mp_str(err_ref_rho, 10),
            "E3_rho_lt_E3_i": bool(e3_rho < e3_i),
        },
        "casimir_density_at_tau_star": {
            "rho_1B": mp_str(rho_1B_at_i, 25),
            "rho_1F": mp_str(rho_1F_at_i, 25),
            "rho_casimir_bulk_2H": mp_str(rho_casimir_bulk, 25),
            "rho_casimir_brane_2H": mp_str(rho_casimir_brane, 25),
            "is_dS_positive_bulk": bool(rho_casimir_bulk > 0),
            "is_dS_positive_brane": bool(rho_casimir_brane > 0),
        },
        "saddle_at_i": {
            "grad_norm": mp_str(gh_i["grad_norm"], 10),
            "a_Exx": mp_str(a_saddle, 25),
            "b_Eyy": mp_str(b_saddle, 25),
            "c_Exy": mp_str(gh_i["hxy"], 10),
            "a_times_b": mp_str(a_saddle * b_saddle, 20),
            "maass_laplacian_residual": mp_str(laplacian_residual_i, 10),
            "is_saddle": bool(a_saddle < -7 and b_saddle > 35 and a_saddle * b_saddle < 0),
        },
        "tau_star_plus": {
            "F3": mp_str(f3_star, REPORT_DPS),
            "grad_norm": mp_str(gh_plus["grad_norm"], 10),
            "gamma_prime_re": mp_str(mp.re(gamma_prime_plus), 20),
            "gamma_prime_im": mp_str(mp.im(gamma_prime_plus), 20),
            "sin2_theta": mp_str(sin2_theta_plus, 25),
            "e1": mp_str(gh_plus["e1"], 20),
            "e2": mp_str(gh_plus["e2"], 20),
            "trace_num": mp_str(gh_plus["trace"], 20),
            "trace_analytic": mp_str(tr_analytic, 20),
            "trace_rel_err": mp_str(tr_rel_err_plus, 10),
            "det_num": mp_str(gh_plus["det"], 20),
            "det_analytic": mp_str(det_analytic, 20),
            "det_rel_err": mp_str(det_rel_err_plus, 10),
        },
        "tau_star_minus": {
            "F3": mp_str(f3_star_minus, REPORT_DPS),
            "grad_norm": mp_str(gh_minus["grad_norm"], 10),
            "gamma_prime_re": mp_str(mp.re(gamma_prime_minus), 20),
            "gamma_prime_im": mp_str(mp.im(gamma_prime_minus), 20),
            "e1": mp_str(gh_minus["e1"], 20),
            "e2": mp_str(gh_minus["e2"], 20),
            "trace_rel_err": mp_str(tr_rel_err_minus, 10),
            "det_rel_err": mp_str(det_rel_err_minus, 10),
        },
        "x0_5_global_comparison": {
            "cosets_valid": bool(cosets_valid),
            "F3_tau_star": mp_str(f3_star, 30),
            "F3_i_over_sqrt5": mp_str(f3_i_sqrt5, 30),
            "gap_over_i_over_sqrt5": mp_str(gap_i_sqrt5, 25),
            "ratio_i_over_sqrt5_to_star": mp_str(f3_i_sqrt5 / f3_star, 15),
            "rho_coset_images": [
                {k: v for k, v in item.items() if k != "F3_mpf"}
                for item in rho_coset_vals
            ],
            "min_rho_coset_F3": mp_str(min_rho_coset, 25),
            "gap_over_min_rho_coset": mp_str(gap_rho, 25),
            "analytic_lower_bound_y_ge_2": mp_str(analytic_y_ge_2_lower_bound, 20),
            "compactification_bound_beats_star": bool(compactification_bound_beats_star),
            "grid_scan_evals": n_grid_evals,
            "grid_scan_min_F3": mp_str(best_grid_val, 20),
            "grid_scan_best_coset": best_grid_coset,
            "grid_refined_F3_diff_from_2E3i": mp_str(grid_best_diff, 10),
        },
        "multistart_nelder_mead_damped_newton": {
            "n_starts": len(opt_runs),
            "max_F3_diff_from_2E3i": mp_str(max_opt_f3_err, 10),
            "max_grad_norm": mp_str(max_opt_grad, 10),
            "runs": opt_runs,
        },
        "pass": bool(passed),
    }


# ---------------------------------------------------------------------------
# OW9-B1: PSL(2, F_5) Simplicity, Matter Parity, & DP Single-nu^c Operator Census
# ---------------------------------------------------------------------------

def psl2_f5_canon(M):
    a, b, c, d = (x % 5 for x in M)
    neg = ((-a) % 5, (-b) % 5, (-c) % 5, (-d) % 5)
    return min((a, b, c, d), neg)


def psl2_f5_mul(A, B):
    return psl2_f5_canon((
        A[0] * B[0] + A[1] * B[2],
        A[0] * B[1] + A[1] * B[3],
        A[2] * B[0] + A[3] * B[2],
        A[2] * B[1] + A[3] * B[3],
    ))


def psl2_f5_inv(A):
    # For det = 1, inverse of (a, b, c, d) is (d, -b, -c, a)
    return psl2_f5_canon((A[3], -A[1], -A[2], A[0]))


def verify_a5_simplicity_via_psl2_f5():
    """
    Construct PSL(2, F_5) = SL(2, F_5) / {+-I} directly from 2x2 matrices over F_5
    (100% disjoint from S_5 even permutations). Partition into conjugacy classes,
    exhaust all 2^4 class unions containing identity to prove simplicity, and
    compute the commutator subgroup [G, G] to prove perfectness (no abelian quotient).
    """
    sl2 = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    if (a * d - b * c) % 5 == 1:
                        sl2.append((a, b, c, d))

    elems = sorted({psl2_f5_canon(M) for M in sl2})
    elem_set = set(elems)
    e = psl2_f5_canon((1, 0, 0, 1))

    # Verify closure and inverses
    closure_ok = all(psl2_f5_mul(x, y) in elem_set for x in elems for y in elems)
    inv_ok = all(psl2_f5_mul(x, psl2_f5_inv(x)) == e for x in elems)

    # Element order distribution
    order_counts = Counter()
    for x in elems:
        cur = x
        k = 1
        while cur != e:
            cur = psl2_f5_mul(cur, x)
            k += 1
        order_counts[k] += 1

    # Conjugacy classes
    visited = set()
    classes = []
    for x in elems:
        if x in visited:
            continue
        cls = {psl2_f5_mul(psl2_f5_mul(g, x), psl2_f5_inv(g)) for g in elems}
        visited |= cls
        classes.append(cls)

    class_sizes = sorted(len(c) for c in classes)
    non_id_sizes = class_sizes[1:]  # [12, 12, 15, 20]

    # Exhaust all subsets of non-identity conjugacy classes containing identity (size 1)
    dividing_union_sizes = []
    n_non_id = len(non_id_sizes)
    for mask in range(1 << n_non_id):
        sz = 1 + sum(non_id_sizes[i] for i in range(n_non_id) if (mask >> i) & 1)
        if len(elems) % sz == 0:
            dividing_union_sizes.append(sz)
    dividing_union_sizes.sort()
    proper_nontrivial_normal_candidates = [s for s in dividing_union_sizes if 1 < s < len(elems)]

    # Compute commutator subgroup [G, G] via closure of all commutators
    comms = {
        psl2_f5_mul(psl2_f5_mul(x, y), psl2_f5_mul(psl2_f5_inv(x), psl2_f5_inv(y)))
        for x in elems
        for y in elems
    }
    derived = set(comms)
    changed = True
    while changed:
        changed = False
        new_items = {psl2_f5_mul(a, b) for a in derived for b in comms} - derived
        if new_items:
            derived |= new_items
            changed = True

    is_simple = (
        len(sl2) == 120
        and len(elems) == 60
        and closure_ok
        and inv_ok
        and class_sizes == [1, 12, 12, 15, 20]
        and len(proper_nontrivial_normal_candidates) == 0
        and len(derived) == 60
    )

    return {
        "sl2_f5_order": len(sl2),
        "psl2_f5_order": len(elems),
        "group_axioms_ok": bool(closure_ok and inv_ok),
        "element_order_distribution": {str(k): int(v) for k, v in sorted(order_counts.items())},
        "conjugacy_class_sizes": class_sizes,
        "lagrange_dividing_union_sizes": dividing_union_sizes,
        "proper_nontrivial_normal_candidates": proper_nontrivial_normal_candidates,
        "commutator_subgroup_order": len(derived),
        "abelianization_order": len(elems) // len(derived),
        "is_simple": bool(is_simple),
    }


def verify_matter_parity_on_8_species():
    """
    Verify P_M = (-1)^{3(B-L)} == (-1)^F = (-1)^{2s} across all 8 species
    (Q, u^c, d^c, L, e^c, nu^c, H_u, H_d) of non-SUSY Spin(10) 16 + 10 + 45.
    """
    # (name, 3B, L, twice_spin)
    species = [
        ("Q", 1, 0, 1),
        ("u^c", -1, 0, 1),
        ("d^c", -1, 0, 1),
        ("L", 0, 1, 1),
        ("e^c", 0, -1, 1),
        ("nu^c", 0, -1, 1),
        ("H_u", 0, 0, 0),
        ("H_d", 0, 0, 0),
    ]
    rows = []
    matches = 0
    for name, threeB, L, two_s in species:
        three_BmL = threeB - 3 * L
        P_M = -1 if (three_BmL % 2 != 0) else 1
        ferm_parity = -1 if (two_s % 2 != 0) else 1
        eq = (P_M == ferm_parity)
        if eq:
            matches += 1
        rows.append({
            "species": name,
            "3B": threeB,
            "L": L,
            "3(B-L)": three_BmL,
            "P_M": P_M,
            "minus1_to_F": ferm_parity,
            "P_M_equals_fermion_parity": bool(eq),
        })
    return {
        "n_species": len(species),
        "n_matching": matches,
        "all_match": bool(matches == len(species)),
        "species_table": rows,
    }


def su3_has_singlet(n_fund, n_antifund):
    """
    Explicit SU(3) tensor-product singlet check for (3)^{otimes n_fund} otimes (3bar)^{otimes n_antifund}.
    Uses exact Young-diagram / weight-space decomposition via stepwise multiplication
    by 3 = (1, 0) and 3bar = (0, 1) in Dynkin labels (p, q):
      (p, q) x (1, 0) = (p+1, q) + [if p>0: (p-1, q+1)] + [if q>0: (p, q-1)]
      (p, q) x (0, 1) = (p, q+1) + [if q>0: (p+1, q-1)] + [if p>0: (p-1, q)]
    """
    reps = Counter({(0, 0): 1})
    for _ in range(n_fund):
        nxt = Counter()
        for (p, q), mult in reps.items():
            nxt[(p + 1, q)] += mult
            if p > 0:
                nxt[(p - 1, q + 1)] += mult
            if q > 0:
                nxt[(p, q - 1)] += mult
        reps = nxt
    for _ in range(n_antifund):
        nxt = Counter()
        for (p, q), mult in reps.items():
            nxt[(p, q + 1)] += mult
            if q > 0:
                nxt[(p + 1, q - 1)] += mult
            if p > 0:
                nxt[(p - 1, q)] += mult
        reps = nxt
    return int(reps[(0, 0)])


def enumerate_single_nuc_operators_dp(n_deriv, sl2c_mode="chiral"):
    """
    Disjoint bottom-up dynamic programming (DP) multiset enumerator for all
    G_SM x SL(2, C) invariant single-nu^c decay operators up to mass dimension 6
    (1 nu^c, 0 nu^c_bar, n_deriv in {0, 1}).
    Also verifies explicit SU(3) singlet multiplicity >= 1 for every surviving operator.
    """
    # Field catalog (excluding nu^c and nu^c_bar):
    # (name, dim2, su3_rep, is_su2_doublet, sixY, threeB, L, dL, dR)
    # su3_rep: +1 for 3, -1 for 3bar, 0 for 1
    fields = [
        ("Q",       3,  1, 1,  1,  1,  0, 1, 0),
        ("u^c",     3, -1, 0, -4, -1,  0, 1, 0),
        ("d^c",     3, -1, 0,  2, -1,  0, 1, 0),
        ("L",       3,  0, 1, -3,  0,  1, 1, 0),
        ("e^c",     3,  0, 0,  6,  0, -1, 1, 0),
        ("Q_bar",   3, -1, 1, -1, -1,  0, 0, 1),
        ("u^c_bar", 3,  1, 0,  4,  1,  0, 0, 1),
        ("d^c_bar", 3,  1, 0, -2,  1,  0, 0, 1),
        ("L_bar",   3,  0, 1,  3,  0, -1, 0, 1),
        ("e^c_bar", 3,  0, 0, -6,  0,  1, 0, 1),
        ("H_u",     2,  0, 1,  3,  0,  0, 0, 0),
        ("H_d",     2,  0, 1, -3,  0,  0, 0, 0),
        ("H_u_bar", 2,  0, 1, -3,  0,  0, 0, 0),
        ("H_d_bar", 2,  0, 1,  3,  0,  0, 0, 0),
    ]

    max_dim2 = 12  # dim <= 6 -> 2*dim <= 12
    # Seed state with 1 nu^c (dim2=3, L=-1, nL=1, nR=0) and n_deriv derivatives (dim2 += 2*n_deriv)
    # DP state key: (dim2, tri_mod3, su2_mod2, sixY, nL_mod2, nR_mod2)
    # Value: list of (threeB, L, n3, n3bar, multiset_tuple)
    init_state = (3 + 2 * n_deriv, 0, 0, 0, 1, 0)
    dp = {init_state: [(0, -1, 0, 0, ("nu^c",))]}

    for name, d2, su3_r, dsu2, d6Y, d3B, dL_lep, dnL, dnR in fields:
        nxt_dp = {}
        for state, records in dp.items():
            cur_d2, tri, su2, sixY, nL_m2, nR_m2 = state
            max_k = (max_dim2 - cur_d2) // d2
            for k in range(max_k + 1):
                nd2 = cur_d2 + k * d2
                ntri = (tri + k * su3_r) % 3
                nsu2 = (su2 + k * dsu2) % 2
                n6Y = sixY + k * d6Y
                nnL = (nL_m2 + k * dnL) % 2
                nnR = (nR_m2 + k * dnR) % 2
                nkey = (nd2, ntri, nsu2, n6Y, nnL, nnR)
                bucket = nxt_dp.setdefault(nkey, [])
                add_names = (name,) * k
                add_3 = k if su3_r == 1 else 0
                add_3bar = k if su3_r == -1 else 0
                for threeB, L_val, n3, n3bar, mset in records:
                    bucket.append((
                        threeB + k * d3B,
                        L_val + k * dL_lep,
                        n3 + add_3,
                        n3bar + add_3bar,
                        mset + add_names,
                    ))
        dp = nxt_dp

    ops = []
    for (dim2, tri, su2, sixY, nL_m2, nR_m2), records in dp.items():
        if tri != 0 or su2 != 0 or sixY != 0:
            continue
        if sl2c_mode == "chiral":
            if (nL_m2 + n_deriv) % 2 != 0 or (nR_m2 + n_deriv) % 2 != 0:
                continue
        elif sl2c_mode == "ignore_chiral_parity":
            if (nL_m2 + nR_m2) % 2 != 0:
                continue
        else:
            raise ValueError("Unknown sl2c_mode")

        for threeB, L_val, n3, n3bar, mset in records:
            su3_mult = su3_has_singlet(n3, n3bar)
            if su3_mult >= 1:
                three_BmL = threeB - 3 * L_val
                ops.append({
                    "dim": str(Fraction(dim2, 2)),
                    "dim2": dim2,
                    "n_deriv": n_deriv,
                    "B_minus_L": str(Fraction(three_BmL, 3)),
                    "abs_3_BmL": abs(three_BmL),
                    "su3_singlet_mult": su3_mult,
                    "fields": list(mset),
                })

    ops.sort(key=lambda r: (r["dim2"], r["abs_3_BmL"], r["fields"]))
    return ops


def run_ow9_b1():
    psl2_res = verify_a5_simplicity_via_psl2_f5()
    pm_res = verify_matter_parity_on_8_species()

    ops_0 = enumerate_single_nuc_operators_dp(0, sl2c_mode="chiral")
    ops_1 = enumerate_single_nuc_operators_dp(1, sl2c_mode="chiral")

    ops_0_bml0 = [op for op in ops_0 if op["abs_3_BmL"] == 0]
    ops_0_bml2 = [op for op in ops_0 if op["abs_3_BmL"] == 6]
    ops_1_bml0 = [op for op in ops_1 if op["abs_3_BmL"] == 0]
    ops_1_bml2 = [op for op in ops_1 if op["abs_3_BmL"] == 6]

    dim4_fields = sorted(tuple(op["fields"]) for op in ops_0 if op["dim2"] == 8)
    has_nu_L_Hu = ("nu^c", "L", "H_u") in dim4_fields
    has_nu_L_Hdbar = ("nu^c", "L", "H_d_bar") in dim4_fields
    ops_0_bml2_all_dim5 = all(op["dim2"] == 10 for op in ops_0_bml2)
    ops_1_bml0_all_dim6 = all(op["dim2"] == 12 for op in ops_1_bml0)
    ops_1_bml2_all_dim5 = all(op["dim2"] == 10 for op in ops_1_bml2)

    passed = (
        psl2_res["is_simple"]
        and pm_res["all_match"]
        and len(ops_0) == 17
        and len(ops_0_bml0) == 14
        and len(ops_0_bml2) == 3
        and ops_0_bml2_all_dim5
        and has_nu_L_Hu
        and has_nu_L_Hdbar
        and len(ops_1) == 5
        and len(ops_1_bml0) == 3
        and len(ops_1_bml2) == 2
        and ops_1_bml0_all_dim6
        and ops_1_bml2_all_dim5
    )

    return {
        "a5_simplicity_via_psl2_f5": psl2_res,
        "matter_parity_8_species": pm_res,
        "single_nuc_operators": {
            "zero_deriv_total": len(ops_0),
            "zero_deriv_BmL_0": len(ops_0_bml0),
            "zero_deriv_abs_BmL_2": len(ops_0_bml2),
            "zero_deriv_abs_BmL_2_all_dim5": bool(ops_0_bml2_all_dim5),
            "dim4_leading_operators": [list(t) for t in dim4_fields],
            "one_deriv_total": len(ops_1),
            "one_deriv_BmL_0": len(ops_1_bml0),
            "one_deriv_BmL_0_all_dim6": bool(ops_1_bml0_all_dim6),
            "one_deriv_abs_BmL_2": len(ops_1_bml2),
            "one_deriv_abs_BmL_2_all_dim5": bool(ops_1_bml2_all_dim5),
            "zero_deriv_list": ops_0,
            "one_deriv_list": ops_1,
        },
        "pass": bool(passed),
    }


# ---------------------------------------------------------------------------
# OW9-B2: Gaussian-Norm KK Shells & 547 Primitive Hyperbolic GL(2, Z) Classes
# ---------------------------------------------------------------------------

def verify_gaussian_norm_shells():
    """
    Verify exact integer identity Q(m, n) = |m + n tau_*^+|^2 / Im(tau_*^+)
      = 5 m^2 + 4 m n + n^2 = (2 m + n)^2 + m^2
    for all |m|, |n| <= 6 using exact Fraction arithmetic (and tau_*^- mirror),
    and certify the lowest nonzero T^2 / Z_2 unordered KK shells Q = 1, 2, 4.
    """
    tau_re = Fraction(2, 5)
    tau_im = Fraction(1, 5)
    n_checked = 0
    identity_all_ok = True
    mirror_all_ok = True

    for m in range(-6, 7):
        for n in range(-6, 7):
            n_checked += 1
            re_part = Fraction(m) + Fraction(n) * tau_re
            im_part = Fraction(n) * tau_im
            q_frac = (re_part * re_part + im_part * im_part) / tau_im
            q_quad = 5 * m * m + 4 * m * n + n * n
            q_gauss = (2 * m + n) ** 2 + m * m
            if not (q_frac == q_quad == q_gauss):
                identity_all_ok = False
            # Mirror tau_*^- = (-2 + i)/5
            re_m = Fraction(m) - Fraction(n) * tau_re
            q_frac_m = (re_m * re_m + im_part * im_part) / tau_im
            q_gauss_m = (2 * m - n) ** 2 + m * m
            if not (q_frac_m == q_gauss_m):
                mirror_all_ok = False

    # Complete enumeration of all nonzero unordered pairs with Q(m, n) <= 10.
    # Since Q = (2m + n)^2 + m^2 <= 10, |m| <= 3 and |2m + n| <= 3 -> |n| <= 9.
    shells = {}
    for m in range(-3, 4):
        for u in range(-3, 4):
            n = u - 2 * m
            if m == 0 and n == 0:
                continue
            Q = u * u + m * m
            if Q > 10:
                continue
            # Canonical unordered pair representative: first nonzero entry positive
            pair = (m, n) if (m > 0 or (m == 0 and n > 0)) else (-m, -n)
            grade = (pair[0] % 2, pair[1] % 2)
            shells.setdefault(Q, set()).add((pair, grade))

    formatted_shells = {}
    for Q in sorted(shells):
        items = sorted(shells[Q])
        formatted_shells[str(Q)] = [
            {"pair": list(p), "grade": list(g)} for p, g in items
        ]

    q1_pairs = {p for p, _ in shells.get(1, set())}
    q1_grades = {g for _, g in shells.get(1, set())}
    q2_pairs = {p for p, _ in shells.get(2, set())}
    q2_grades = {g for _, g in shells.get(2, set())}
    q3_count = len(shells.get(3, set()))
    q4_grades = {g for _, g in shells.get(4, set())}

    first_trivial_Q = min(
        Q for Q in sorted(shells)
        if any(g == (0, 0) for _, g in shells[Q])
    )
    mass_ratio_sq = Fraction(first_trivial_Q, 1)
    mass_ratio = int(math.isqrt(first_trivial_Q))

    ok = (
        n_checked == 169
        and identity_all_ok
        and mirror_all_ok
        and q1_pairs == {(0, 1), (1, -2)}
        and q1_grades == {(0, 1), (1, 0)}
        and q2_pairs == {(1, -1), (1, -3)}
        and q2_grades == {(1, 1)}
        and q3_count == 0
        and first_trivial_Q == 4
        and q4_grades == {(0, 0)}
        and mass_ratio * mass_ratio == first_trivial_Q
        and mass_ratio == 2
    )

    return {
        "n_points_checked_abs_le_6": n_checked,
        "gaussian_norm_identity_exact": bool(identity_all_ok),
        "mirror_tau_minus_identity_exact": bool(mirror_all_ok),
        "shells_Q_le_10": formatted_shells,
        "Q1_grades": sorted(list(g) for g in q1_grades),
        "Q2_grades": sorted(list(g) for g in q2_grades),
        "Q3_pair_count": q3_count,
        "first_trivial_grade_Q": first_trivial_Q,
        "first_trivial_mass_ratio": mass_ratio,
        "mass_ratio_sq": str(mass_ratio_sq),
        "verified": bool(ok),
    }


def _mat2_mul(A, B):
    return (
        A[0] * B[0] + A[1] * B[2],
        A[0] * B[1] + A[1] * B[3],
        A[2] * B[0] + A[3] * B[2],
        A[2] * B[1] + A[3] * B[3],
    )


def enumerate_primitive_hyperbolic_lrj_tree(trace_max=50):
    r"""
    Disjoint direct trace-bounded matrix generator tree in {L, R, J}:
      L = [[1, 0], [1, 1]], R = [[1, 1], [0, 1]], J = [[0, 1], [1, 0]].
    - det = +1 (PSL_2(Z)): primitive cyclic words in {L, R} with >=1 L and >=1 R,
      trace(M) <= trace_max.
    - det = -1 (PGL_2(Z) \ PSL_2(Z)): primitive twisted-cyclic words W*J in {L, R}*J,
      trace(W*J) <= trace_max, where L^{-1}(L W' J)L = W' R J flips first letter.
    Zero continued fractions!
    """
    L = (1, 0, 1, 1)
    R = (1, 1, 0, 1)
    J = (0, 1, 1, 0)
    I = (1, 0, 0, 1)
    swap_tbl = str.maketrans("LR", "RL")

    # 1. det = +1 classes
    pos_classes = {}

    def is_prim_cyclic(w):
        n = len(w)
        for d in range(1, n):
            if n % d == 0 and w == w[:d] * (n // d):
                return False
        return True

    def dfs_pos(w, M):
        tr = M[0] + M[3]
        if tr > trace_max:
            return
        if is_prim_cyclic(w):
            canon = min(w[i:] + w[:i] for i in range(len(w)))
            if canon not in pos_classes:
                pos_classes[canon] = (tr, 1, M)
        dfs_pos(w + "L", _mat2_mul(M, L))
        dfs_pos(w + "R", _mat2_mul(M, R))

    for k in range(1, trace_max - 1):
        # L^k R = [[1, 1], [k, k+1]], tr = k + 2
        dfs_pos("L" * k + "R", (1, 1, k, k + 1))

    # 2. det = -1 classes: W * J with W in {L, R}^+ and tr(W J) = M[1] + M[2] <= trace_max
    neg_classes = {}

    def twisted_rots(w):
        res = set()
        cur = w
        for _ in range(2 * len(w)):
            res.add(cur)
            cur = cur[1:] + ("R" if cur[0] == "L" else "L")
        return res

    def is_prim_twisted(w):
        n = len(w)
        for k in range(3, n + 1, 2):
            if n % k == 0:
                d = n // k
                u = w[:d]
                us = u.translate(swap_tbl)
                if "".join(u if i % 2 == 0 else us for i in range(k)) == w:
                    return False
        return True

    def dfs_neg(w, M):
        tr_mj = M[1] + M[2]
        if tr_mj > trace_max:
            return
        if tr_mj >= 1 and is_prim_twisted(w):
            canon = min(twisted_rots(w))
            if canon not in neg_classes:
                neg_classes[canon] = (tr_mj, -1, _mat2_mul(M, J))
        dfs_neg(w + "L", _mat2_mul(M, L))
        dfs_neg(w + "R", _mat2_mul(M, R))

    dfs_neg("", I)
    return pos_classes, neg_classes


def gauss_narrow_class_counts(trace_max=50):
    """
    Independent mathematical completeness check: compute exact trace-by-trace
    counts of primitive hyperbolic classes using Gauss narrow class numbers h^+(D)
    of reduced indefinite binary quadratic forms (b^2 - 4ac = D).
    """
    def h_plus(D):
        sD = math.isqrt(D)
        if sD * sD == D:
            return 0
        forms = set()
        for b in range(1, sD + 1):
            if (D - b * b) % 4 != 0:
                continue
            m = (D - b * b) // 4
            lo = (sD - b) // 2 + 1
            hi = (sD + b) // 2
            for abs_a in range(lo, hi + 1):
                if m % abs_a == 0:
                    abs_c = m // abs_a
                    if math.gcd(abs_a, math.gcd(b, abs_c)) == 1:
                        forms.add((abs_a, b, -abs_c))
                        forms.add((-abs_a, b, abs_c))
        vis = set()
        cnt = 0
        for f in sorted(forms):
            if f in vis:
                continue
            cnt += 1
            cur = f
            while cur not in vis:
                vis.add(cur)
                a, b, c = cur
                k = (sD + b) // (2 * abs(c))
                bn = 2 * abs(c) * k - b
                cur = (c, bn, (bn * bn - D) // (4 * c))
        return cnt

    pos_by_tr = Counter()
    seen_D_pos = set()
    for T in range(3, trace_max + 1):
        val = T * T - 4
        for u in range(1, T + 1):
            if val % (u * u) == 0:
                D = val // (u * u)
                if D % 4 in (0, 1) and math.isqrt(D) ** 2 != D and D not in seen_D_pos:
                    seen_D_pos.add(D)
                    pos_by_tr[T] += h_plus(D)

    neg_by_tr = Counter()
    seen_D_neg = set()
    for T in range(1, trace_max + 1):
        val = T * T + 4
        for u in range(1, T + 3):
            if val % (u * u) == 0:
                D = val // (u * u)
                if D % 4 in (0, 1) and math.isqrt(D) ** 2 != D and D not in seen_D_neg:
                    seen_D_neg.add(D)
                    neg_by_tr[T] += h_plus(D)

    return pos_by_tr, neg_by_tr


def evaluate_brane_coupling(mode_mn, weights_e2):
    """
    Evaluate brane coupling sum_{p in E[2]} w(p) * (-1)^{m p_1 + n p_2}
    for KK mode (m, n) across the 4 orbifold fixed points E[2] = {(0,0),(1,0),(0,1),(1,1)}.
    """
    m, n = mode_mn
    total = 0
    for (p1, p2), w in weights_e2.items():
        sign = -1 if ((m * p1 + n * p2) % 2 != 0) else 1
        total += w * sign
    return total


def run_ow9_b2():
    shell_res = verify_gaussian_norm_shells()

    pos_classes, neg_classes = enumerate_primitive_hyperbolic_lrj_tree(trace_max=50)
    gauss_pos_tr, gauss_neg_tr = gauss_narrow_class_counts(trace_max=50)

    tree_pos_tr = Counter(tr for tr, _d, _M in pos_classes.values())
    tree_neg_tr = Counter(tr for tr, _d, _M in neg_classes.values())
    trace_by_trace_pos_match = (tree_pos_tr == gauss_pos_tr)
    trace_by_trace_neg_match = (tree_neg_tr == gauss_neg_tr)

    all_classes = list(pos_classes.values()) + list(neg_classes.values())
    nontrivial_grades = [(1, 0), (0, 1), (1, 1)]
    nontrivial_set = set(nontrivial_grades)

    failures = 0
    order_mod2_counts = Counter()
    for tr, expected_det, M in all_classes:
        a, b, c, d = M
        det_M = a * d - b * c
        tr_M = a + d
        disc_M = tr_M * tr_M - 4 * det_M
        is_hyp = (disc_M > 0 and math.isqrt(disc_M) ** 2 != disc_M)
        det_mod2 = det_M % 2

        # Direct action on Z_2 x Z_2 and dual action (M^T) on Z_2 characters
        zero_img = ((a * 0 + b * 0) % 2, (c * 0 + d * 0) % 2)
        nt_imgs = {((a * u + b * v) % 2, (c * u + d * v) % 2) for (u, v) in nontrivial_grades}
        dual_imgs = {((a * u + c * v) % 2, (b * u + d * v) % 2) for (u, v) in nontrivial_grades}

        # Order of M mod 2 in GL(2, F_2) = S_3
        M2 = (a % 2, b % 2, c % 2, d % 2)
        cur = M2
        ord_m2 = 1
        while cur != (1, 0, 0, 1):
            cur = (
                (cur[0] * M2[0] + cur[1] * M2[2]) % 2,
                (cur[0] * M2[1] + cur[1] * M2[3]) % 2,
                (cur[2] * M2[0] + cur[3] * M2[2]) % 2,
                (cur[2] * M2[1] + cur[3] * M2[3]) % 2,
            )
            ord_m2 += 1
        order_mod2_counts[ord_m2] += 1

        ok_cls = (
            det_M == expected_det
            and tr_M == tr
            and 1 <= tr_M <= 50
            and is_hyp
            and det_mod2 == 1
            and zero_img == (0, 0)
            and nt_imgs == nontrivial_set
            and dual_imgs == nontrivial_set
        )
        if not ok_cls:
            failures += 1

    # Explicit m004 = [[2, 1], [1, 1]] check
    m004 = (2, 1, 1, 1)
    m004_det = m004[0] * m004[3] - m004[1] * m004[2]
    m004_tr = m004[0] + m004[3]
    # Orbit of (1, 0) under m004 mod 2
    orbit = []
    v = (1, 0)
    for _ in range(3):
        orbit.append(v)
        v = ((m004[0] * v[0] + m004[1] * v[1]) % 2, (m004[2] * v[0] + m004[3] * v[1]) % 2)
    m004_returns = (v == (1, 0))
    m004_is_3_cycle = (len(set(orbit)) == 3 and set(orbit) == nontrivial_set and m004_returns)
    m004_fixed_characters = [
        chi for chi in nontrivial_grades
        if ((m004[0] * chi[0] + m004[2] * chi[1]) % 2, (m004[1] * chi[0] + m004[3] * chi[1]) % 2) == chi
    ]
    # Verify m004's conjugacy class 'LR' is present in our 363 det=+1 list
    m004_in_tree = ("LR" in pos_classes and pos_classes["LR"][0] == 3)

    # E[2] half-period democracy vs single-puncture (0, 0) breaking
    w_democracy = {(0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 1}
    w_single_00 = {(0, 0): 1, (1, 0): 0, (0, 1): 0, (1, 1): 0}
    grades_all = [(0, 0), (1, 0), (0, 1), (1, 1)]
    democracy_evals = {f"{g[0]},{g[1]}": evaluate_brane_coupling(g, w_democracy) for g in grades_all}
    single_00_evals = {f"{g[0]},{g[1]}": evaluate_brane_coupling(g, w_single_00) for g in grades_all}

    democracy_forbids_all_nontrivial = all(
        evaluate_brane_coupling(g, w_democracy) == 0 for g in nontrivial_grades
    ) and evaluate_brane_coupling((0, 0), w_democracy) == 4
    single_00_couples_all_grades = all(
        evaluate_brane_coupling(g, w_single_00) == 1 for g in grades_all
    )

    passed = (
        shell_res["verified"]
        and len(pos_classes) == 363
        and len(neg_classes) == 184
        and len(all_classes) == 547
        and trace_by_trace_pos_match
        and trace_by_trace_neg_match
        and failures == 0
        and m004_det == 1
        and m004_tr == 3
        and m004_in_tree
        and m004_is_3_cycle
        and len(m004_fixed_characters) == 0
        and democracy_forbids_all_nontrivial
        and single_00_couples_all_grades
    )

    return {
        "gaussian_norm_shells": shell_res,
        "hyperbolic_gl2z_census": {
            "method": "direct_LRJ_trace_bounded_generator_tree_plus_gauss_h_plus_cross_check",
            "trace_max": 50,
            "det_plus_1_count": len(pos_classes),
            "det_minus_1_count": len(neg_classes),
            "total_classes": len(all_classes),
            "trace_by_trace_matches_gauss_h_plus_det_pos": bool(trace_by_trace_pos_match),
            "trace_by_trace_matches_gauss_h_plus_det_neg": bool(trace_by_trace_neg_match),
            "gl2_f2_action_failures": failures,
            "gl2_f2_order_distribution": {str(k): int(v) for k, v in sorted(order_mod2_counts.items())},
        },
        "m004_check": {
            "matrix": [2, 1, 1, 1],
            "det": m004_det,
            "trace": m004_tr,
            "present_in_363_tree": bool(m004_in_tree),
            "mod2_orbit_from_1_0": [list(p) for p in orbit],
            "is_3_cycle": bool(m004_is_3_cycle),
            "fixed_nontrivial_Z2_characters_count": len(m004_fixed_characters),
        },
        "e2_fixed_point_democracy": {
            "democracy_weights_couplings": democracy_evals,
            "single_puncture_00_couplings": single_00_evals,
            "democracy_forbids_all_nontrivial_grades": bool(democracy_forbids_all_nontrivial),
            "single_00_breaks_stabilizer": bool(single_00_couples_all_grades),
        },
        "pass": bool(passed),
    }


# ---------------------------------------------------------------------------
# OW9-C: Planted-Fault Self-Checks (4 / 4)
# ---------------------------------------------------------------------------

def run_ow9_c(a1_res, a2_res, b1_res):
    mp.mp.dps = WORK_DPS

    # PF-OW9-1: Dropping internal A_5, A_6 odd gauge polarizations
    weyl_info = a1_res["weyl_6d_clifford_check"]
    stueck_info = a1_res["stueckelberg_projector_check"]
    fault_a1 = compute_kk_supertrace_spectrum(
        weyl_info, stueck_info, higgs_localization="bulk", gauge_internal_mode="drop_A5_A6"
    )
    nominal_bulk_lat = a1_res["bulk_2H"]["kk_per_T2_lattice_point"]["n_B_minus_n_F"]
    fault_bulk_lat = fault_a1["kk_per_T2_lattice_point"]["n_B_minus_n_F"]
    pf1_caught = (nominal_bulk_lat == -68 and fault_bulk_lat == -80 and fault_bulk_lat != nominal_bulk_lat)

    # PF-OW9-2: Flipping the Berezin fermion Casimir sign makes rho_Casimir < 0 (AdS)
    e3_star = E3_ewald(mp.mpc(2, 1) / 5)
    rho_1B = -(mp.mpf(1) / (mp.pi ** 3)) * e3_star
    n_B_lat_bulk = a1_res["bulk_2H"]["kk_per_T2_lattice_point"]["n_B"]
    n_F_lat_bulk = a1_res["bulk_2H"]["kk_per_T2_lattice_point"]["n_F"]
    n_B_lat_brane = a1_res["brane_2H"]["kk_per_T2_lattice_point"]["n_B"]
    n_F_lat_brane = a1_res["brane_2H"]["kk_per_T2_lattice_point"]["n_F"]

    # Correct Berezin sign: rho_1F = -rho_1B; Flipped Berezin sign: rho_1F_fault = +rho_1B
    rho_nom_bulk = n_B_lat_bulk * rho_1B + n_F_lat_bulk * (-rho_1B)
    rho_fault_bulk = n_B_lat_bulk * rho_1B + n_F_lat_bulk * (+rho_1B)
    rho_fault_brane = n_B_lat_brane * rho_1B + n_F_lat_brane * (+rho_1B)
    pf2_caught = (rho_nom_bulk > 0 and rho_fault_bulk < 0 and rho_fault_brane < 0)

    # PF-OW9-3: Ignoring chiral (n_L, n_R) SL(2, C) parity inflates 0-deriv operators 17 -> 34
    ops_0_nochiral = enumerate_single_nuc_operators_dp(0, sl2c_mode="ignore_chiral_parity")
    nom_ops_0 = b1_res["single_nuc_operators"]["zero_deriv_total"]
    fault_ops_0 = len(ops_0_nochiral)
    pf3_caught = (nom_ops_0 == 17 and fault_ops_0 == 34 and fault_ops_0 != nom_ops_0)

    # PF-OW9-4: Single-puncture (0, 0) brane operator gives +1 on Q=1 LKP modes (0, 1) and (1, -2)
    w_single_00 = {(0, 0): 1, (1, 0): 0, (0, 1): 0, (1, 1): 0}
    w_democracy = {(0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 1}
    c_dem_01 = evaluate_brane_coupling((0, 1), w_democracy)
    c_dem_1m2 = evaluate_brane_coupling((1, -2), w_democracy)
    c_flt_01 = evaluate_brane_coupling((0, 1), w_single_00)
    c_flt_1m2 = evaluate_brane_coupling((1, -2), w_single_00)
    pf4_caught = (c_dem_01 == 0 and c_dem_1m2 == 0 and c_flt_01 == 1 and c_flt_1m2 == 1)

    caught_count = sum(1 for flag in (pf1_caught, pf2_caught, pf3_caught, pf4_caught) if flag)

    return {
        "PF-OW9-1": {
            "description": "Drop internal A_5, A_6 odd gauge polarizations",
            "nominal_bulk_2H_per_lattice_pt": nominal_bulk_lat,
            "fault_bulk_2H_per_lattice_pt": fault_bulk_lat,
            "shift": fault_bulk_lat - nominal_bulk_lat,
            "caught": bool(pf1_caught),
        },
        "PF-OW9-2": {
            "description": "Flip Berezin fermion Casimir sign",
            "nominal_rho_casimir_bulk": mp_str(rho_nom_bulk, 20),
            "fault_rho_casimir_bulk": mp_str(rho_fault_bulk, 20),
            "fault_rho_casimir_brane": mp_str(rho_fault_brane, 20),
            "caught": bool(pf2_caught),
        },
        "PF-OW9-3": {
            "description": "Ignore chiral (n_L, n_R) SL(2, C) parity",
            "nominal_zero_deriv_count": nom_ops_0,
            "fault_zero_deriv_count": fault_ops_0,
            "spurious_inflation": fault_ops_0 - nom_ops_0,
            "caught": bool(pf3_caught),
        },
        "PF-OW9-4": {
            "description": "Break E[2] half-period democracy with single-puncture (0, 0) operator",
            "democracy_coupling_0_1": c_dem_01,
            "democracy_coupling_1_m2": c_dem_1m2,
            "single_00_coupling_0_1": c_flt_01,
            "single_00_coupling_1_m2": c_flt_1m2,
            "caught": bool(pf4_caught),
        },
        "caught_count": caught_count,
        "total_faults": 4,
        "pass": bool(caught_count == 4),
    }


def main():
    a1_res = run_ow9_a1()
    a2_res = run_ow9_a2(a1_res)
    b1_res = run_ow9_b1()
    b2_res = run_ow9_b2()
    c_res = run_ow9_c(a1_res, a2_res, b1_res)

    all_pass = bool(
        a1_res["pass"]
        and a2_res["pass"]
        and b1_res["pass"]
        and b2_res["pass"]
        and c_res["pass"]
    )

    report = {
        "card_id": "AGY-002_A2-OW9",
        "role": "independent_cold_room_zero_trust_referee",
        "empirical_firewall": "0_of_19",
        "OW9_A1": a1_res,
        "OW9_A2": a2_res,
        "OW9_B1": b1_res,
        "OW9_B2": b2_res,
        "OW9_C": c_res,
        "overall_pass": all_pass,
    }

    out_path = Path(__file__).resolve().parent / "referee_a2_ow9_out.json"
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, sort_keys=False)
        fh.write("\n")


if __name__ == "__main__":
    main()
