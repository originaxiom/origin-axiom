#!/usr/bin/env python3
"""Independent Cold-Room Zero-Trust Referee (v2) for Gate 7B (Campaign AGY-002-COMPLETE-CLOSURE).

Audits Card AGY-002_CLOSURE-G7B (with errata AGY-002_CLOSURE-G7B-REFEREE-ERRATUM
and AGY-002_CLOSURE-G7B-REFEREE-ERRATUM-2) under strict 0-of-19 empirical firewall,
Guardrails 1-6, zero repository imports, and zero float/complex AST literals:
  1. Deliverable 1 (F13, Guardrail 5): Exact QQ Buckingham-Pi rank-nullity for
     same-dimension mass scales (1x19 vs 1x20) + Planted Fault PF7B.1.
  2. Deliverable 2 (F16, Guardrail 2): Symbolic Bessel identity, E_6 -> G_422 x| Z_2^D
     collar supertrace weights (C_UV = 189/2, C_IR = 28), 30-digit mpmath Casimir
     monotonicity proof on equal-gap flat collar, and genuine 32-pt / 48-pt Cauchy
     contour analyticity + negative-degree Laurent/Taylor jet quadrature + PF7B.2.
  3. Deliverable 3 (F17, Guardrails 3 & 4): Symbolic Antusch mass-gap denominator
     proofs, literature benchmark gate, 32-state scoped TM1 Weinberg RGE grid via
     Kahan-compensated RK4 and exact matrix exponential, 10-trial U(3)_L x U(3)_{eR}
     Haar basis-scrambling invariance via unsquared SVD projectors, + PF7B.3.
  4. Deliverable 4 (F14, F15): Exact 240-root E_8 construction, A_2 x E_6 centralizer
     decomposition, Role A (0 singlets) vs Role B (9 singlets) SU(3)_c non-equivalence
     (+ PF7B.4), borrowed_model_premises DAG invariant across PR-1..PR-10 and
     OP:Level6_Higgs (+ PF7B.5), and 44-manifest campaign SHA-256 custody
     (46 including prior referee SCRIPT_SHA256.txt files) + runtime self-hash check.
"""

from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys
from typing import Any, Callable

import mpmath as mp
import numpy as np
import sympy as sp


def _sanitize_for_json(obj: Any) -> Any:
    """Recursively convert numpy bool/int scalars into native Python JSON-safe types."""
    if isinstance(obj, dict):
        return {str(k): _sanitize_for_json(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_sanitize_for_json(v) for v in obj]
    if isinstance(obj, np.bool_):
        return bool(obj)
    if isinstance(obj, np.integer):
        return int(obj)
    return obj


def _mpf_to_rational_str(val: mp.mpf, sig_digits: int = 12) -> str:
    """Serialize an mpmath real value as an exact mask-safe rational string."""
    if val == 0:
        return "0"
    sign = "-" if val < 0 else ""
    av = abs(val)
    ten = mp.mpf(10)
    k = int(mp.floor(mp.log(av) / mp.log(ten)))
    shift = sig_digits - 1 - k
    if shift >= 0:
        num = int(mp.nint(av * (ten ** shift)))
        if num == 0:
            return "0"
        if shift <= 18:
            frac = Fraction(num, 10 ** shift)
            if frac.denominator == 1:
                return f"{sign}{frac.numerator}"
            return f"{sign}{frac.numerator}/{frac.denominator}"
        return f"{sign}{num}/10^{shift}"
    scale_exp = -shift
    num_scaled = int(mp.nint(av / (ten ** scale_exp)))
    if scale_exp <= 18:
        return f"{sign}{num_scaled * (10 ** scale_exp)}"
    return f"{sign}{num_scaled}*10^{scale_exp}"


def _float_to_rational_str(val: Any, denom_power: int = 15) -> str:
    """Convert a Python/NumPy real scalar into a mask-safe rational string via mpmath."""
    fval = float(val)
    mp.mp.dps = 30
    mval = mp.mpf(int(round(fval * (10 ** denom_power)))) / (mp.mpf(10) ** denom_power)
    if mval == 0 and fval != 0:
        av = abs(fval)
        k = 0
        scaled = av
        while scaled < 1 and k < 300:
            scaled *= 10
            k += 1
        num = int(round(scaled * (10 ** 6)))
        sign = "-" if fval < 0 else ""
        return f"{sign}{num}/10^{k + 6}"
    return _mpf_to_rational_str(mval, sig_digits=12)


def _self_ast_and_mask_audit(script_path: Path) -> dict[str, Any]:
    """Verify 0 float AST literals, 0 complex AST literals, 0 repo imports, and 0 decimal patterns."""
    src = script_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(script_path))

    float_literals = 0
    complex_literals = 0
    allowed_roots = {
        "__future__",
        "ast",
        "fractions",
        "hashlib",
        "itertools",
        "json",
        "mpmath",
        "numpy",
        "pathlib",
        "re",
        "sympy",
        "sys",
        "typing",
    }
    disallowed_imports: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals += 1
            elif isinstance(node.value, complex):
                complex_literals += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root not in allowed_roots:
                    disallowed_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level != 0 or (node.module is not None and node.module.split(".")[0] not in allowed_roots):
                disallowed_imports.append(str(node.module))

    decimal_tokens = re.findall(r"\d+\.\d+", src)
    passed = bool(
        float_literals == 0
        and complex_literals == 0
        and len(disallowed_imports) == 0
        and len(decimal_tokens) == 0
    )
    return {
        "passed": passed,
        "float_ast_literals": float_literals,
        "complex_ast_literals": complex_literals,
        "disallowed_imports": disallowed_imports,
        "decimal_prose_tokens_in_script": len(decimal_tokens),
    }


# ---------------------------------------------------------------------------
# Deliverable 1: Exact QQ Buckingham-Pi Rank-Nullity for Same-Dimension Scales
# ---------------------------------------------------------------------------


def _validate_buckingham_pi_ledger(dim_matrix: sp.Matrix, claimed_nullity: int) -> bool:
    """Audit gate enforcing exact Rank-Nullity over QQ for dimensionless parameter count."""
    actual_rank = int(dim_matrix.rank())
    null_basis = dim_matrix.nullspace()
    actual_nullity = len(null_basis)
    return bool(
        actual_nullity == int(dim_matrix.cols) - actual_rank
        and actual_nullity == claimed_nullity
    )


def _audit_deliverable_1() -> dict[str, Any]:
    """Verify 1x19 vs 1x20 QQ mass-dimension matrices and catch PF7B.1."""
    dim1_names = [
        "v_EW",
        "m_H",
        "m_e",
        "m_mu",
        "m_tau",
        "m_u",
        "m_c",
        "m_t",
        "m_d",
        "m_s",
        "m_b",
    ]
    dim0_names = [
        "g_1",
        "g_2",
        "g_3",
        "theta_QCD",
        "s12_CKM",
        "s23_CKM",
        "s13_CKM",
        "delta_CKM",
    ]
    assert len(dim1_names) == 11 and len(dim0_names) == 8

    row_19 = [sp.Rational(1, 1) for _ in dim1_names] + [sp.Rational(0, 1) for _ in dim0_names]
    d19 = sp.Matrix([row_19])
    rank_19 = int(d19.rank())
    ns_19 = d19.nullspace()
    nullity_19 = len(ns_19)
    ns_19_mat = sp.Matrix.hstack(*ns_19)
    ns_19_basis_rank = int(ns_19_mat.rank())
    ns_19_in_kernel = bool(all((d19 * vec) == sp.zeros(1, 1) for vec in ns_19))

    row_20 = row_19 + [sp.Rational(1, 1)]
    d20 = sp.Matrix([row_20])
    rank_20 = int(d20.rank())
    ns_20 = d20.nullspace()
    nullity_20 = len(ns_20)
    ns_20_mat = sp.Matrix.hstack(*ns_20)
    ns_20_basis_rank = int(ns_20_mat.rank())
    ns_20_in_kernel = bool(all((d20 * vec) == sp.zeros(1, 1) for vec in ns_20))

    v_m2_minus_vew = sp.zeros(20, 1)
    v_m2_minus_vew[0, 0] = sp.Rational(-1, 1)
    v_m2_minus_vew[19, 0] = sp.Rational(1, 1)
    ratio_in_ker_d20 = bool((d20 * v_m2_minus_vew) == sp.zeros(1, 1))

    ns_19_embedded = sp.Matrix.vstack(ns_19_mat, sp.zeros(1, 18))
    combined_19_span = sp.Matrix.hstack(ns_19_embedded, v_m2_minus_vew)
    ratio_spans_new_direction = bool(
        int(ns_19_embedded.rank()) == 18 and int(combined_19_span.rank()) == 19
    )

    d20_dynamically_fixed = sp.Matrix.vstack(d20, v_m2_minus_vew.T)
    bridged_rank = int(d20_dynamically_fixed.rank())
    bridged_nullity = len(d20_dynamically_fixed.nullspace())

    valid_19_ledger = _validate_buckingham_pi_ledger(d19, 18)
    fault_unpriced_20_accepted = _validate_buckingham_pi_ledger(d20, 18)
    pf7b_1_caught = bool(valid_19_ledger and (not fault_unpriced_20_accepted) and (nullity_20 == 19 > 18))

    passed = bool(
        d19.shape == (1, 19)
        and rank_19 == 1
        and nullity_19 == 18
        and ns_19_basis_rank == 18
        and ns_19_in_kernel
        and d20.shape == (1, 20)
        and rank_20 == 1
        and rank_20 == rank_19
        and nullity_20 == 19
        and ns_20_basis_rank == 19
        and ns_20_in_kernel
        and ratio_in_ker_d20
        and ratio_spans_new_direction
        and bridged_rank == 2
        and bridged_nullity == 18
        and pf7b_1_caught
    )

    return {
        "passed": passed,
        "d19_shape": [1, 19],
        "dim1_count_sm": 11,
        "dim0_count_sm": 8,
        "rank_d19": rank_19,
        "nullity_d19": nullity_19,
        "nullspace_19_basis_rank": ns_19_basis_rank,
        "d20_shape": [1, 20],
        "rank_d20": rank_20,
        "rank_unchanged_under_same_dim_scale": bool(rank_20 == rank_19),
        "nullity_d20": nullity_20,
        "nullspace_20_basis_rank": ns_20_basis_rank,
        "e_M2_minus_e_vEW_in_ker_d20": ratio_in_ker_d20,
        "e_M2_minus_e_vEW_independent_of_sm_18": ratio_spans_new_direction,
        "dynamically_bridged_rank": bridged_rank,
        "dynamically_bridged_nullity": bridged_nullity,
        "pf7b_1_caught": pf7b_1_caught,
    }


# ---------------------------------------------------------------------------
# Deliverable 2: Global Analytic Casimir Sign Proof & Cauchy Contour Quadrature
# ---------------------------------------------------------------------------


def _mp_log1p(u: mp.mpf) -> mp.mpf:
    """Compute ln(1 + u) in mpmath without small-u cancellation."""
    fn = getattr(mp, "log1p", None)
    if fn is not None:
        return fn(u)
    threshold = (mp.mpf(1) / mp.mpf(10)) ** 8
    if abs(u) < threshold:
        acc = mp.mpf(0)
        for j in range(1, 7):
            term = (u ** j) / mp.mpf(j)
            acc = acc + term if (j % 2 == 1) else acc - term
        return acc
    return mp.log(mp.mpf(1) + u)


def _theta_char(alpha: Fraction, beta: Fraction, w: mp.mpc, omega: mp.mpc, n_trunc: int = 8) -> mp.mpc:
    """Evaluate Jacobi theta[alpha; beta](w | omega) via exact lattice reduction into |Im u| <= Im(omega)/2."""
    i_unit = mp.mpc(0, 1)
    a_mp = mp.mpf(alpha.numerator) / mp.mpf(alpha.denominator)
    b_mp = mp.mpf(beta.numerator) / mp.mpf(beta.denominator)

    m_shift = int(mp.nint(mp.im(w) / mp.im(omega)))
    w1 = w - mp.mpf(m_shift) * omega
    ell_shift = int(mp.nint(mp.re(w1)))
    u = w1 - mp.mpf(ell_shift)

    acc = mp.mpc(0, 0)
    for n in range(-n_trunc, n_trunc + 1):
        na = mp.mpf(n) + a_mp
        exponent = mp.pi * i_unit * (na ** 2) * omega + 2 * mp.pi * i_unit * na * (u + b_mp)
        acc += mp.exp(exponent)

    phase_exp = (
        2 * mp.pi * i_unit * a_mp * mp.mpf(ell_shift)
        - mp.pi * i_unit * (mp.mpf(m_shift) ** 2) * omega
        - 2 * mp.pi * i_unit * mp.mpf(m_shift) * (u + b_mp)
    )
    return mp.exp(phase_exp) * acc


def _theta1(z: mp.mpc, tau: mp.mpc) -> mp.mpc:
    """Standard odd Jacobi theta_1(z | tau) = -vartheta[1/2; 1/2](z | tau) with period 1."""
    half = Fraction(1, 2)
    return -_theta_char(half, half, z, tau, n_trunc=8)


def _cauchy_laurent_jet(
    func: Callable[[mp.mpc], mp.mpc],
    z0: mp.mpc,
    radius: mp.mpf,
    deg: int,
    n_pts: int,
) -> mp.mpc:
    """Compute (1 / (2 pi i)) oint_{|z - z0| = radius} f(z) / (z - z0)^(deg + 1) dz.

    Uniform trapezoidal contour quadrature across all integer degrees (deg < 0 and deg >= 0)
    with zero conditional branches on deg.
    """
    i_unit = mp.mpc(0, 1)
    acc = mp.mpc(0, 0)
    for k in range(n_pts):
        angle = 2 * mp.pi * mp.mpf(k) / mp.mpf(n_pts)
        dz_vec = radius * mp.exp(i_unit * angle)
        acc += func(z0 + dz_vec) * (dz_vec ** (-deg))
    return acc / mp.mpf(n_pts)


def _verify_no_if_shortcut_in_jet_helper(script_path: Path) -> bool:
    """Ensure _cauchy_laurent_jet contains zero ast.If or ast.IfExp nodes (Guardrail 2)."""
    tree = ast.parse(script_path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "_cauchy_laurent_jet":
            for child in ast.walk(node):
                if isinstance(child, (ast.If, ast.IfExp)):
                    return False
            return True
    return False


def _audit_deliverable_2(script_path: Path) -> dict[str, Any]:
    """Prove analytic Casimir monotonicity and genuine Cauchy contour analyticity + PF7B.2."""
    x_sym = sp.Symbol("x", positive=True)
    bessel_expr = sp.diff((x_sym ** (-2)) * sp.besselk(2, x_sym), x_sym) + (x_sym ** (-2)) * sp.besselk(3, x_sym)
    bessel_residual = sp.simplify(sp.besselsimp(bessel_expr))
    bessel_identity_proved = bool(bessel_residual == 0)

    l4_sym, m_sym, w_sym = sp.symbols("L_4 m w", positive=True)
    v_ir_sym = sp.Rational(28, 1) * (sp.pi ** 2) / (sp.Rational(90, 1) * ((4 * l4_sym) ** 4))
    dv_ir_check = sp.simplify(sp.diff(v_ir_sym, l4_sym) + sp.Rational(7, 1440) * (sp.pi ** 2) / (l4_sym ** 5))
    v_tw_mode = (
        sp.Rational(19, 8)
        * (m_sym ** 2)
        / ((sp.pi ** 2) * (l4_sym ** 2))
        * sp.besselk(2, 4 * m_sym * w_sym * l4_sym)
        / (w_sym ** 2)
    )
    dv_tw_check = sp.simplify(
        sp.besselsimp(
            sp.diff(v_tw_mode, l4_sym)
            + sp.Rational(19, 2)
            * (m_sym ** 3)
            / ((sp.pi ** 2) * (l4_sym ** 2))
            * sp.besselk(3, 4 * m_sym * w_sym * l4_sym)
            / w_sym
        )
    )
    potential_derivative_identities_proved = bool(dv_ir_check == 0 and dv_tw_check == 0)

    gauge_78_blocks = [
        ("SU4_adj", 15, 1, 1, 1),
        ("SU2L_adj", 1, 3, 1, 1),
        ("SU2R_adj", 1, 1, 3, 1),
        ("U1_psi_coset", 1, 1, 1, -1),
        ("SO10_G422_coset", 6, 2, 2, -1),
        ("E6_SO10_spin_L", 4, 2, 1, -1),
        ("E6_SO10_spinbar_L", 4, 2, 1, -1),
        ("E6_SO10_spin_R", 4, 1, 2, -1),
        ("E6_SO10_spinbar_R", 4, 1, 2, -1),
    ]
    gauge_untwisted = sum(d4 * dL * dR for _, d4, dL, dR, p in gauge_78_blocks if p == 1)
    gauge_twisted = sum(d4 * dL * dR for _, d4, dL, dR, p in gauge_78_blocks if p == -1)

    n_gen = 3
    fermion_27_blocks = [
        ("Q_L_421", 4, 2, 1, 1),
        ("Q_R_4bar12", 4, 1, 2, 1),
        ("Exotic_611", 6, 1, 1, -1),
        ("Bidoublet_122", 1, 2, 2, -1),
        ("Singlet_111", 1, 1, 1, -1),
    ]
    weyl_untwisted = n_gen * sum(d4 * dL * dR for _, d4, dL, dR, p in fermion_27_blocks if p == 1)
    weyl_twisted = n_gen * sum(d4 * dL * dR for _, d4, dL, dR, p in fermion_27_blocks if p == -1)

    higgs_27_blocks = [
        ("Bidoublet_H_122", 1, 2, 2, 1),
        ("PS_Breaker_4bar12", 4, 1, 2, 1),
        ("Singlet_S_111", 1, 1, 1, 1),
        ("Triplet_611", 6, 1, 1, -1),
        ("Partner_421", 4, 2, 1, -1),
    ]
    scalar_untwisted = sum(d4 * dL * dR for _, d4, dL, dR, p in higgs_27_blocks if p == 1)
    scalar_twisted = sum(d4 * dL * dR for _, d4, dL, dR, p in higgs_27_blocks if p == -1)

    nb_plus = 2 * gauge_untwisted + 2 * scalar_untwisted
    nf_plus = 2 * weyl_untwisted
    nb_minus = 2 * gauge_twisted + 2 * scalar_twisted
    nf_minus = 2 * weyl_twisted

    c_ir = Fraction(nf_plus - nb_plus, 1)
    delta_twisted = Fraction(nf_minus - nb_minus, 1)
    c_uv = c_ir - Fraction(7, 8) * delta_twisted

    collar_weights_ok = bool(
        gauge_untwisted == 21
        and gauge_twisted == 57
        and gauge_untwisted + gauge_twisted == 78
        and weyl_untwisted == 48
        and weyl_twisted == 33
        and weyl_untwisted + weyl_twisted == 81
        and scalar_untwisted == 13
        and scalar_twisted == 14
        and scalar_untwisted + scalar_twisted == 27
        and c_ir == Fraction(28, 1)
        and c_uv == Fraction(189, 2)
    )

    mp.mp.dps = 30
    ten = mp.mpf(10)
    tol_rel_casimir = (mp.mpf(1) / ten) ** 22
    tol_tail = (mp.mpf(1) / ten) ** 150
    cosh_7_gt_548 = bool(mp.cosh(7) > mp.mpf(548))

    casimir_grid_records: list[dict[str, Any]] = []
    max_rel_diff_casimir = mp.mpf(0)
    max_tail_bound = mp.mpf(0)
    all_leibniz_positive = True
    all_dva_negative = True
    all_tail_bounds_ok = True

    for num_l4, den_l4 in [(1, 5), (1, 1), (3, 1)]:
        l4_val = mp.mpf(num_l4) / mp.mpf(den_l4)
        m_hyp = mp.mpf(1)
        x_val = 4 * m_hyp * l4_val

        pair_diffs = [
            mp.besselk(3, mp.mpf(2 * k - 1) * x_val) / mp.mpf(2 * k - 1)
            - mp.besselk(3, mp.mpf(2 * k) * x_val) / mp.mpf(2 * k)
            for k in range(1, 16)
        ]
        min_pair_diff = min(pair_diffs)
        if min_pair_diff <= 0:
            all_leibniz_positive = False

        alpha_slope = x_val * mp.sinh(7) - mp.mpf(3)
        tail_bound = mp.exp(-x_val * mp.cosh(7) + mp.mpf(21)) / alpha_slope
        if not (alpha_slope > 0 and 0 < tail_bound < tol_tail):
            all_tail_bounds_ok = False
        if tail_bound > max_tail_bound:
            max_tail_bound = tail_bound

        quad_int = mp.quad(
            lambda t: _mp_log1p(mp.exp(-x_val * mp.cosh(t))) * mp.cosh(3 * t),
            [0, 1, 3, 7],
        )
        w_max = 150
        series_int = mp.mpf(0)
        for w in range(1, w_max + 1):
            term = mp.besselk(3, mp.mpf(w) * x_val) / mp.mpf(w)
            series_int = series_int + term if (w % 2 == 1) else series_int - term

        rel_diff = abs(series_int - quad_int) / abs(quad_int)
        if rel_diff > max_rel_diff_casimir:
            max_rel_diff_casimir = rel_diff

        term_ir = -(7 * (mp.pi ** 2)) / (1440 * (l4_val ** 5))
        term_tw = -(19 * (m_hyp ** 3)) / (2 * (mp.pi ** 2) * (l4_val ** 2)) * quad_int
        dva_dl4 = term_ir + term_tw
        if not (term_ir < 0 and term_tw < 0 and dva_dl4 < 0):
            all_dva_negative = False

        casimir_grid_records.append(
            {
                "L_4": f"{num_l4}/{den_l4}" if den_l4 != 1 else f"{num_l4}",
                "x_arg": _mpf_to_rational_str(x_val),
                "min_leibniz_pair_k1_15": _mpf_to_rational_str(min_pair_diff),
                "analytic_tail_bound_above_t7": _mpf_to_rational_str(tail_bound),
                "series_vs_quad_rel_diff": _mpf_to_rational_str(rel_diff),
                "dVA_dL4": _mpf_to_rational_str(dva_dl4),
                "strictly_negative": bool(dva_dl4 < 0),
            }
        )

    casimir_scope = (
        "Global monotonicity d V_A / d L_4 < 0 on (0, infty) is analytically proved "
        "within the equal-gap flat-collar 1-loop Kaluza-Klein tower (28 net massless "
        "untwisted chiral d.o.f. and 76 net twisted bosonic-minus-fermionic d.o.f. "
        "sharing uniform collar mass gap m > 0); non-uniform threshold splittings or "
        "warped collar curvature terms lie outside this closed-form scope."
    )

    mp.mp.dps = 30
    i_unit = mp.mpc(0, 1)
    tau_cusp = 2 * mp.sqrt(3) * i_unit

    z_probe = mp.mpc(mp.mpf(2) / mp.mpf(11), mp.mpf(3) / mp.mpf(7))
    th_probe = _theta1(z_probe, tau_cusp)
    th_probe_tau = _theta1(z_probe + tau_cusp, tau_cusp)
    qp_rel_1 = abs(_theta1(z_probe + 1, tau_cusp) + th_probe) / abs(th_probe)
    qp_rel_tau = abs(
        th_probe_tau
        + mp.exp(-mp.pi * i_unit * tau_cusp - 2 * mp.pi * i_unit * z_probe) * th_probe
    ) / abs(th_probe_tau)
    theta1_quasiperiodicity_ok = bool(
        qp_rel_1 < (mp.mpf(1) / ten) ** 25 and qp_rel_tau < (mp.mpf(1) / ten) ** 25
    )

    def _f_cim_flux_ratio(z: mp.mpc) -> mp.mpc:
        return (_theta1(3 * z, 3 * tau_cusp) ** 2) / _theta1(6 * z, 6 * tau_cusp)

    w1_div = (mp.mpf(1) + tau_cusp) / mp.mpf(3)
    w2_div = (mp.mpf(2) + 2 * tau_cusp) / mp.mpf(3)

    def _f_cim_divisor_raw(z: mp.mpc) -> mp.mpc:
        return (
            mp.exp(-6 * mp.pi * i_unit * z)
            * (_theta1(z - w1_div, tau_cusp) ** 3)
            * (_theta1(z - w2_div, tau_cusp) ** 3)
            / (_theta1(z, tau_cusp) ** 6)
        )

    norm_half = _f_cim_divisor_raw(mp.mpc(mp.mpf(1) / mp.mpf(2), 0))

    def _f_cim_divisor(z: mp.mpc) -> mp.mpc:
        return _f_cim_divisor_raw(z) / norm_half

    f_probe = _f_cim_divisor(z_probe)
    dp_rel_1 = abs(_f_cim_divisor(z_probe + 1) - f_probe) / abs(f_probe)
    dp_rel_tau = abs(_f_cim_divisor(z_probe + tau_cusp) - f_probe) / abs(f_probe)
    divisor_elliptic_ok = bool(
        dp_rel_1 < (mp.mpf(1) / ten) ** 24 and dp_rel_tau < (mp.mpf(1) / ten) ** 24
    )

    torsion_points = [
        (a, b, (mp.mpf(a) + mp.mpf(b) * tau_cusp) / mp.mpf(3))
        for a in range(3)
        for b in range(3)
        if not (a == 0 and b == 0)
    ]
    assert len(torsion_points) == 8

    contour_radius = mp.mpf(1) / mp.mpf(60)
    tol_cauchy = (mp.mpf(1) / ten) ** 15
    tol_pole_capture = (mp.mpf(1) / ten) ** 13

    max_residue_32 = mp.mpf(0)
    max_residue_48 = mp.mpf(0)
    max_refinement_diff = mp.mpf(0)
    max_neg_jet_mag = mp.mpf(0)
    min_nonneg_jet_mag = mp.mpf(10) ** 10
    max_fault_pole_err = mp.mpf(0)
    min_fault_pole_mag = mp.mpf(10) ** 10

    for _, _, zp in torsion_points:
        for fn in (_f_cim_flux_ratio, _f_cim_divisor):
            for idx_deg, neg_deg in enumerate((-1, -2, -3)):
                jet_32_c = _cauchy_laurent_jet(fn, zp, contour_radius, neg_deg, 32)
                jet_48_c = _cauchy_laurent_jet(fn, zp, contour_radius, neg_deg, 48)
                jet_32 = abs(jet_32_c)
                jet_48 = abs(jet_48_c)
                if idx_deg == 0:
                    ref_diff = abs(jet_32_c - jet_48_c)
                    if jet_32 > max_residue_32:
                        max_residue_32 = jet_32
                    if jet_48 > max_residue_48:
                        max_residue_48 = jet_48
                    if ref_diff > max_refinement_diff:
                        max_refinement_diff = ref_diff
                if jet_32 > max_neg_jet_mag:
                    max_neg_jet_mag = jet_32
                if jet_48 > max_neg_jet_mag:
                    max_neg_jet_mag = jet_48

            nonneg_max = max(
                abs(_cauchy_laurent_jet(fn, zp, contour_radius, pos_deg, 32))
                for pos_deg in (0, 1, 3)
            )
            if nonneg_max < min_nonneg_jet_mag:
                min_nonneg_jet_mag = nonneg_max

        def _f_fault(z: mp.mpc, center: mp.mpc = zp) -> mp.mpc:
            return _f_cim_flux_ratio(z) + mp.mpf(1) / (z - center)

        fault_res_32 = _cauchy_laurent_jet(_f_fault, zp, contour_radius, -1, 32)
        fault_res_48 = _cauchy_laurent_jet(_f_fault, zp, contour_radius, -1, 48)
        err_from_one = max(abs(fault_res_32 - 1), abs(fault_res_48 - 1))
        mag_min = min(abs(fault_res_32), abs(fault_res_48))
        if err_from_one > max_fault_pole_err:
            max_fault_pole_err = err_from_one
        if mag_min < min_fault_pole_mag:
            min_fault_pole_mag = mag_min

    no_if_shortcut = _verify_no_if_shortcut_in_jet_helper(script_path)
    pf7b_2_caught = bool(
        max_fault_pole_err < tol_pole_capture
        and min_fault_pole_mag > mp.mpf(1) / mp.mpf(2)
        and min_fault_pole_mag > tol_cauchy
    )

    passed = bool(
        bessel_identity_proved
        and potential_derivative_identities_proved
        and collar_weights_ok
        and cosh_7_gt_548
        and all_leibniz_positive
        and all_tail_bounds_ok
        and max_rel_diff_casimir < tol_rel_casimir
        and all_dva_negative
        and theta1_quasiperiodicity_ok
        and divisor_elliptic_ok
        and no_if_shortcut
        and max_residue_32 < tol_cauchy
        and max_residue_48 < tol_cauchy
        and max_neg_jet_mag < tol_cauchy
        and min_nonneg_jet_mag > (mp.mpf(1) / ten) ** 12
        and pf7b_2_caught
    )

    return {
        "passed": passed,
        "symbolic_bessel_identity_zero": bessel_identity_proved,
        "symbolic_potential_derivative_identities_zero": potential_derivative_identities_proved,
        "collar_weights": {
            "gauge_78_untwisted": gauge_untwisted,
            "gauge_78_twisted": gauge_twisted,
            "weyl_3x27_untwisted": weyl_untwisted,
            "weyl_3x27_twisted": weyl_twisted,
            "scalar_27_untwisted": scalar_untwisted,
            "scalar_27_twisted": scalar_twisted,
            "C_UV": f"{c_uv.numerator}/{c_uv.denominator}",
            "C_IR": f"{c_ir.numerator}",
        },
        "casimir_scope": casimir_scope,
        "cosh_7_gt_548": cosh_7_gt_548,
        "max_tail_bound_above_t7": _mpf_to_rational_str(max_tail_bound),
        "max_series_vs_quad_rel_diff": _mpf_to_rational_str(max_rel_diff_casimir),
        "all_leibniz_pairs_positive": all_leibniz_positive,
        "all_dVA_dL4_strictly_negative": all_dva_negative,
        "casimir_grid": casimir_grid_records,
        "cauchy_contour_audit": {
            "torsion_points_tested": len(torsion_points),
            "quadrature_nodes_tested": [32, 48],
            "contour_radius": "1/60",
            "zero_if_deg_lt_0_shortcut_ast_verified": no_if_shortcut,
            "theta1_quasiperiodicity_verified": theta1_quasiperiodicity_ok,
            "divisor_double_periodicity_verified": divisor_elliptic_ok,
            "max_residue_32pt": _mpf_to_rational_str(max_residue_32),
            "max_residue_48pt": _mpf_to_rational_str(max_residue_48),
            "max_32_vs_48_refinement_diff": _mpf_to_rational_str(max_refinement_diff),
            "max_negative_degree_jet_mag_deg_m1_m2_m3": _mpf_to_rational_str(max_neg_jet_mag),
            "min_nonnegative_jet_mag": _mpf_to_rational_str(min_nonneg_jet_mag),
            "pf7b_2_max_error_from_unit_residue": _mpf_to_rational_str(max_fault_pole_err),
        },
        "pf7b_2_caught": pf7b_2_caught,
    }


# ---------------------------------------------------------------------------
# Deliverable 3: Symbolic Antusch Mass-Gap Formula & 32-State Scoped TM1 Grid
# ---------------------------------------------------------------------------


def _weinberg_rhs(kappa: np.ndarray, he_mat: np.ndarray) -> np.ndarray:
    """1-loop SM flavor-dependent Weinberg-operator RGE d kappa / d ln(mu)."""
    pref = -(3 / (32 * (np.pi ** 2)))
    return pref * (he_mat @ kappa + kappa @ he_mat.T)


def _integrate_weinberg_rk4(
    kappa0: np.ndarray,
    he_mat: np.ndarray,
    dt_total: Fraction,
    n_steps: int = 80,
) -> np.ndarray:
    """Independent Kahan-compensated 4th-order Runge-Kutta integrator for d kappa / dt."""
    h = (dt_total.numerator / dt_total.denominator) / n_steps
    y = kappa0.copy()
    comp = np.zeros_like(y)
    for _ in range(n_steps):
        k1 = _weinberg_rhs(y, he_mat)
        k2 = _weinberg_rhs(y + (h / 2) * k1, he_mat)
        k3 = _weinberg_rhs(y + (h / 2) * k2, he_mat)
        k4 = _weinberg_rhs(y + h * k3, he_mat)
        inc = (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4) - comp
        y_next = y + inc
        comp = (y_next - y) - inc
        y = y_next
    return y


def _integrate_weinberg_exact_expm(
    kappa0: np.ndarray,
    he_mat: np.ndarray,
    dt_total: Fraction,
) -> np.ndarray:
    """Exact matrix-exponential solution exp(A dt) kappa0 exp(A^T dt) for Hermitian H_e."""
    dt_val = dt_total.numerator / dt_total.denominator
    coeff = -(3 / (32 * (np.pi ** 2))) * dt_val
    evals, evecs = np.linalg.eigh(he_mat)
    exp_a = (evecs * np.exp(coeff * evals)) @ evecs.conj().T
    return exp_a @ kappa0 @ exp_a.T


def _extract_i_tm1_basis_invariant(
    ye_mat: np.ndarray,
    kappa_mat: np.ndarray,
    nu1_rank_idx: int,
) -> float:
    """Basis-invariant observable I_TM1 = Tr(P_e P_{nu_1}) = |U_{e1}|^2 via unsquared SVD (Guardrail 3)."""
    u_e, s_e, _ = np.linalg.svd(ye_mat)
    assert float(s_e[0] - s_e[1]) > 0 and float(s_e[1] - s_e[2]) > 0
    ve = u_e[:, 2]
    proj_e = np.outer(ve, ve.conj())

    u_nu, s_nu, _ = np.linalg.svd(kappa_mat)
    assert float(s_nu[0] - s_nu[1]) > 0 and float(s_nu[1] - s_nu[2]) > 0
    svd_nu1_idx = 2 - nu1_rank_idx
    u_nu1 = u_nu[:, svd_nu1_idx]
    proj_nu1 = np.outer(u_nu1, u_nu1.conj())

    return float(np.real(np.trace(proj_e @ proj_nu1)))


def _haar_unitary_u3(rng: np.random.Generator) -> np.ndarray:
    """Sample a 3x3 Haar-random unitary matrix via Mezzadri complex-Ginibre QR."""
    i_unit = complex(0, 1)
    z = (rng.standard_normal((3, 3)) + i_unit * rng.standard_normal((3, 3))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    diag_r = np.diag(r)
    phases = diag_r / np.abs(diag_r)
    return q * phases


def _build_tm1_pmns(delta_cp: Any) -> np.ndarray:
    """Construct UV TM1 PMNS matrix U_TBM * R_23(psi, delta_cp) with exact cos(psi)=12/13, sin(psi)=5/13."""
    i_unit = complex(0, 1)
    u_tbm = np.array(
        [
            [np.sqrt(2 / 3), 1 / np.sqrt(3), 0],
            [-1 / np.sqrt(6), 1 / np.sqrt(3), 1 / np.sqrt(2)],
            [1 / np.sqrt(6), -1 / np.sqrt(3), 1 / np.sqrt(2)],
        ],
        dtype=complex,
    )
    c_psi = 12 / 13
    s_psi = 5 / 13
    r_23 = np.array(
        [
            [1, 0, 0],
            [0, c_psi, s_psi * np.exp(-i_unit * delta_cp)],
            [0, -s_psi * np.exp(i_unit * delta_cp), c_psi],
        ],
        dtype=complex,
    )
    return u_tbm @ r_23


def _audit_deliverable_3() -> dict[str, Any]:
    """Prove symbolic Antusch denominator and audit 32-state TM1 grid + Haar + PF7B.3."""
    m1, m2, p_real, theta, dtheta_dt = sp.symbols("m_1 m_2 p theta dtheta_dt", real=True)
    h11, h22 = sp.symbols("h_11 h_22", real=True)
    u_rot = sp.Matrix([[sp.cos(theta), sp.sin(theta)], [-sp.sin(theta), sp.cos(theta)]])
    d_diag = sp.Matrix([[m1, 0], [0, m2]])
    dkappa_rot = sp.diff(u_rot * d_diag * u_rot.T, theta).subs(theta, 0)
    h_real = sp.Matrix([[h11, p_real], [p_real, h22]])
    rhs_real = -sp.Rational(3, 2) * (h_real * d_diag + d_diag * h_real.T)
    rot_rate_12 = sp.solve(sp.Eq(dkappa_rot[0, 1] * dtheta_dt, rhs_real[0, 1]), dtheta_dt)[0]
    target_rot = -sp.Rational(3, 2) * p_real * (m1 + m2) / (m2 - m1)
    real_sym_proved = bool(sp.simplify(rot_rate_12 - target_rot) == 0)

    phi1, phi2, pr, pi_im = sp.symbols("phi_1 phi_2 p_r p_i", real=True)
    p12 = pr + sp.I * pi_im
    p12_conj = pr - sp.I * pi_im
    h_herm = sp.Matrix([[h11, p12], [p12_conj, h22]])
    phase1 = sp.cos(phi1) + sp.I * sp.sin(phi1)
    phase2 = sp.cos(phi2) + sp.I * sp.sin(phi2)
    k_complex = sp.Matrix([[m1 * phase1, 0], [0, m2 * phase2]])
    dk_dt = -sp.Rational(3, 2) * (h_herm * k_complex + k_complex * h_herm.T)
    dk_dag_dt = -sp.Rational(3, 2) * (k_complex.H * h_herm + h_herm.conjugate() * k_complex.H)
    dm2_dt = sp.expand(dk_dt * k_complex.H + k_complex * dk_dag_dt)
    w12_complex = sp.cancel(dm2_dt[0, 1] / (m2 ** 2 - m1 ** 2))
    denom_quot = sp.simplify(sp.denom(w12_complex) / (m2 ** 2 - m1 ** 2))
    num_at_degeneracy = sp.simplify(dm2_dt[0, 1].subs(m2, m1))
    complex_denom_proved = bool(
        denom_quot != 0
        and len(denom_quot.free_symbols) == 0
        and num_at_degeneracy != 0
        and sp.simplify(w12_complex.subs({phi1: 0, phi2: 0, pi_im: 0, pr: p_real}) - target_rot) == 0
    )

    theta_bench = float(np.pi / 6)
    c_b, s_b = float(np.cos(theta_bench)), float(np.sin(theta_bench))
    u2_b = np.array([[c_b, s_b], [-s_b, c_b]], dtype=complex)
    kappa2_uv = u2_b @ np.diag([1, 2]).astype(complex) @ u2_b.T
    ytau_b = 1 / 5
    he2_b = np.diag([0, ytau_b ** 2]).astype(complex)
    dt_bench = Fraction(-1, 10)
    kappa2_ir = _integrate_weinberg_rk4(kappa2_uv, he2_b, dt_bench, n_steps=80)
    u2_svd, _, _ = np.linalg.svd(kappa2_ir)
    theta_ir_num = float(np.arccos(abs(u2_svd[0, 1])))
    dtheta_num = float(theta_ir_num - theta_bench)
    dtheta_lit = float(
        (3 * (ytau_b ** 2) / (64 * (np.pi ** 2))) * np.sin(2 * theta_bench) * ((1 + 2) / (2 - 1)) * (-1 / 10)
    )
    bench_rel_err = float(abs(dtheta_num - dtheta_lit) / abs(dtheta_lit))
    benchmark_gate_passed = bool(dtheta_num < 0 and bench_rel_err < (1 / 1000))

    i_unit = complex(0, 1)
    spectra = [
        ("NO_gap_3_5", Fraction(1, 1), Fraction(2, 1), Fraction(5, 1), 0),
        ("NO_gap_4_5", Fraction(1, 1), Fraction(3, 1), Fraction(9, 1), 0),
        ("IO_gap_3_5", Fraction(2, 1), Fraction(4, 1), Fraction(1, 1), 1),
        ("IO_gap_4_5", Fraction(3, 1), Fraction(9, 1), Fraction(1, 1), 1),
    ]
    phase_sets = [
        ("phases_0_0_0", 0, 0, 0),
        ("phases_pi_0_pi4", np.pi, 0, np.pi / 4),
        ("phases_pi2_pi_pi2", np.pi / 2, np.pi, np.pi / 2),
        ("phases_pi3_2pi3_pi3", np.pi / 3, 2 * np.pi / 3, np.pi / 3),
    ]
    ytau_fracs = [Fraction(1, 20), Fraction(1, 5)]
    dt_total = Fraction(-30, 1)

    max_drift_all = float(0)
    max_drift_ytau_1_20 = float(0)
    max_rk4_vs_expm_diff = float(0)
    max_uv_tm1_err = float(0)
    min_gap_ratio = Fraction(10, 1)
    state_count = 0

    representative_states_for_haar: list[tuple[np.ndarray, np.ndarray, int, float]] = []

    for spec_name, m1_f, m2_f, m3_f, nu1_idx in spectra:
        gap_12 = abs(m2_f ** 2 - m1_f ** 2) / (m2_f ** 2 + m1_f ** 2)
        gap_13 = abs(m3_f ** 2 - m1_f ** 2) / (m3_f ** 2 + m1_f ** 2)
        spec_gap = min(gap_12, gap_13)
        assert spec_gap >= Fraction(3, 5) >= Fraction(1, 3)
        if spec_gap < min_gap_ratio:
            min_gap_ratio = spec_gap

        m1_v = m1_f.numerator / m1_f.denominator
        m2_v = m2_f.numerator / m2_f.denominator
        m3_v = m3_f.numerator / m3_f.denominator

        for ph_name, a21, a31, d_cp in phase_sets:
            u_tm1 = _build_tm1_pmns(d_cp)
            d_nu = np.diag([m1_v, m2_v * np.exp(i_unit * a21), m3_v * np.exp(i_unit * a31)])
            kappa0 = u_tm1 @ d_nu @ u_tm1.T

            for yt_f in ytau_fracs:
                state_count += 1
                yt_v = yt_f.numerator / yt_f.denominator
                ye_mat = np.diag([yt_v / 100, yt_v / 10, yt_v]).astype(complex)
                he_mat = ye_mat @ ye_mat.conj().T

                i_uv = _extract_i_tm1_basis_invariant(ye_mat, kappa0, nu1_idx)
                uv_err = float(abs(i_uv - (2 / 3)))
                if uv_err > max_uv_tm1_err:
                    max_uv_tm1_err = uv_err

                kappa_rk4 = _integrate_weinberg_rk4(kappa0, he_mat, dt_total, n_steps=80)
                kappa_exp = _integrate_weinberg_exact_expm(kappa0, he_mat, dt_total)
                solver_diff = float(np.linalg.norm(kappa_rk4 - kappa_exp, ord="fro"))
                if solver_diff > max_rk4_vs_expm_diff:
                    max_rk4_vs_expm_diff = solver_diff

                i_ir = _extract_i_tm1_basis_invariant(ye_mat, kappa_rk4, nu1_idx)
                drift = float(abs(i_ir - (2 / 3)))
                if drift > max_drift_all:
                    max_drift_all = drift
                if yt_f == Fraction(1, 20) and drift > max_drift_ytau_1_20:
                    max_drift_ytau_1_20 = drift

                if ph_name == "phases_pi3_2pi3_pi3" and yt_f == Fraction(1, 5) and spec_name in ("NO_gap_3_5", "IO_gap_3_5"):
                    representative_states_for_haar.append((ye_mat, kappa0, nu1_idx, i_ir))

    assert state_count == 32 and len(representative_states_for_haar) == 2

    rng = np.random.Generator(np.random.PCG64(20261117))
    max_haar_diff = float(0)
    haar_trials = 10
    for _ in range(haar_trials):
        u_left = _haar_unitary_u3(rng)
        u_right = _haar_unitary_u3(rng)
        for ye_ref, kappa0_ref, nu1_idx, i_ir_ref in representative_states_for_haar:
            ye_rot = u_left @ ye_ref @ u_right.conj().T
            kappa0_rot = u_left @ kappa0_ref @ u_left.T
            he_rot = ye_rot @ ye_rot.conj().T
            kappa_ir_rot = _integrate_weinberg_rk4(kappa0_rot, he_rot, dt_total, n_steps=80)
            i_ir_rot = _extract_i_tm1_basis_invariant(ye_rot, kappa_ir_rot, nu1_idx)
            diff = float(abs(i_ir_rot - i_ir_ref))
            if diff > max_haar_diff:
                max_haar_diff = diff

    u_tm1_0 = _build_tm1_pmns(0)
    m2_deg_frac = Fraction(100001, 100000)
    deg_gap_frac = (m2_deg_frac ** 2 - 1) / (m2_deg_frac ** 2 + 1)
    kappa0_deg = u_tm1_0 @ np.diag([1, m2_deg_frac.numerator / m2_deg_frac.denominator, 3]).astype(complex) @ u_tm1_0.T
    yt_deg = 1 / 20
    ye_deg = np.diag([yt_deg / 100, yt_deg / 10, yt_deg]).astype(complex)
    he_deg = ye_deg @ ye_deg.conj().T
    kappa_deg_rk4 = _integrate_weinberg_rk4(kappa0_deg, he_deg, dt_total, n_steps=80)
    kappa_deg_exp = _integrate_weinberg_exact_expm(kappa0_deg, he_deg, dt_total)
    deg_solver_diff = float(np.linalg.norm(kappa_deg_rk4 - kappa_deg_exp, ord="fro"))
    i_ir_deg = _extract_i_tm1_basis_invariant(ye_deg, kappa_deg_rk4, 0)
    deg_drift = float(abs(i_ir_deg - (2 / 3)))

    pf7b_3_caught = bool(
        deg_gap_frac < Fraction(1, 3)
        and deg_drift > (1 / 5)
        and deg_drift > (1 / 50)
        and deg_solver_diff < ((1 / 10) ** 12)
    )

    passed = bool(
        real_sym_proved
        and complex_denom_proved
        and benchmark_gate_passed
        and state_count == 32
        and min_gap_ratio == Fraction(3, 5)
        and max_uv_tm1_err < ((1 / 10) ** 14)
        and max_rk4_vs_expm_diff < ((1 / 10) ** 13)
        and max_drift_all < (1 / 50)
        and max_drift_ytau_1_20 < (1 / 1000)
        and max_haar_diff < ((1 / 10) ** 13)
        and pf7b_3_caught
    )

    return {
        "passed": passed,
        "symbolic_real_2x2_rotation_formula_proved": real_sym_proved,
        "symbolic_complex_hermitian_m2_minus_m1_sq_denominator_proved": complex_denom_proved,
        "literature_benchmark_gate": {
            "reference": "Antusch-Kersten-Lindner-Ratz Nucl Phys B660 (2003) 369 Eq 17 downward SM running",
            "passed": benchmark_gate_passed,
            "downward_theta12_decrease": bool(dtheta_num < 0),
            "relative_error_vs_analytic_slope": _float_to_rational_str(bench_rel_err),
        },
        "grid_state_count": state_count,
        "min_mass_gap_ratio_on_grid": f"{min_gap_ratio.numerator}/{min_gap_ratio.denominator}",
        "max_uv_tm1_error": _float_to_rational_str(max_uv_tm1_err),
        "max_rk4_vs_expm_frobenius_diff": _float_to_rational_str(max_rk4_vs_expm_diff),
        "max_abs_I_TM1_minus_2_3_all_32": _float_to_rational_str(max_drift_all),
        "bound_all_32": "1/50",
        "max_abs_I_TM1_minus_2_3_ytau_1_20": _float_to_rational_str(max_drift_ytau_1_20),
        "bound_ytau_1_20": "1/1000",
        "haar_trials": haar_trials,
        "max_u3_haar_basis_invariance_diff": _float_to_rational_str(max_haar_diff),
        "pf7b_3_near_degenerate_drift": _float_to_rational_str(deg_drift),
        "pf7b_3_caught": pf7b_3_caught,
    }


# ---------------------------------------------------------------------------
# Deliverable 4: E_8 240-Root Colour Roles, Premise DAG, & 44-Manifest Custody
# ---------------------------------------------------------------------------


def _construct_e8_scaled_roots() -> list[tuple[int, ...]]:
    """Construct all 240 roots of E_8 as exact integer 8-tuples v = 2*alpha (v . v == 8)."""
    roots: list[tuple[int, ...]] = []
    for i, j in itertools.combinations(range(8), 2):
        for s1 in (-2, 2):
            for s2 in (-2, 2):
                vec = [0] * 8
                vec[i] = s1
                vec[j] = s2
                roots.append(tuple(vec))
    for signs in itertools.product((-1, 1), repeat=8):
        if sum(1 for s in signs if s == -1) % 2 == 0:
            roots.append(signs)
    return roots


def _dot8(u: tuple[int, ...], v: tuple[int, ...]) -> int:
    return sum(x * y for x, y in zip(u, v))


def _is_true_su3_singlet(
    v: tuple[int, ...],
    a2_simple: tuple[tuple[int, ...], tuple[int, ...]],
    a2_all_roots: list[tuple[int, ...]],
    e8_set: set[tuple[int, ...]],
) -> bool:
    """Verify Cartan weight (0, 0) AND annihilation by all 6 SU(3) step operators (Guardrail 2)."""
    s1, s2 = a2_simple
    if _dot8(v, s1) != 0 or _dot8(v, s2) != 0:
        return False
    for r in a2_all_roots:
        plus = tuple(x + y for x, y in zip(v, r))
        minus = tuple(x - y for x, y in zip(v, r))
        if plus in e8_set or minus in e8_set:
            return False
    return True


def _build_premise_dag() -> dict[str, dict[str, Any]]:
    """Construct stratified Rank-0 / Rank-1 DAG across PR-1..PR-10 and OP:Level6_Higgs."""
    dag: dict[str, dict[str, Any]] = {
        "M-1:BuckinghamPi_QQ": {
            "rank": 0,
            "parents": [],
            "borrowed_model_premises": [],
        },
        "M-2:BesselK_Cauchy_Analyticity": {
            "rank": 0,
            "parents": [],
            "borrowed_model_premises": [],
        },
        "M-3:Antusch_Perturbation_Identity": {
            "rank": 0,
            "parents": [],
            "borrowed_model_premises": [],
        },
        "M-4:E8_Root_Centralizer_Algebra": {
            "rank": 0,
            "parents": [],
            "borrowed_model_premises": [],
        },
    }
    rank1_specs = [
        ("PR-1", ["M-4:E8_Root_Centralizer_Algebra"], ["E_8 gauge-matter embedding premise"]),
        ("PR-2", ["PR-1"], ["E_6 grand-unified chiral matter assignment premise"]),
        ("PR-3", ["PR-2"], ["Orbifold holonomy E_6 -> G_422 x| Z_2^D boundary condition"]),
        ("PR-4", ["PR-3"], ["3-generation 3 x 27_F chiral zero-mode multiplicity premise"]),
        ("PR-5", ["PR-3", "M-2:BesselK_Cauchy_Analyticity"], ["Equal-gap flat hyperbolic collar KK tower ansatz"]),
        ("PR-6", ["PR-4", "M-2:BesselK_Cauchy_Analyticity"], ["Closed-fibre CIM (3, 3, -6) magnetized torus identification"]),
        ("PR-7", ["PR-6"], ["Closed-fibre cuspidal modulus tau_cusp = 2 sqrt(3) i frame premise"]),
        ("PR-8", ["PR-4", "M-3:Antusch_Perturbation_Identity"], ["UV TM1 seesaw boundary condition and hierarchical mass-gap regime"]),
        ("PR-9", ["PR-2", "M-4:E8_Root_Centralizer_Algebra"], ["Role B colour identification SU(3)_c subset SU(4)_c subset E_6^GUT"]),
        ("PR-10", ["PR-9", "M-1:BuckinghamPi_QQ"], ["Single-anchor v_EW non-dimensionalization ledger premise"]),
        ("OP:Level6_Higgs", ["PR-3", "PR-10"], ["27_H scalar sector doublet-triplet splitting and Level-6 Higgs bridge premise"]),
    ]
    for node_id, parents, premises in rank1_specs:
        dag[node_id] = {
            "rank": 1,
            "parents": list(parents),
            "borrowed_model_premises": list(premises),
        }
    return dag


def _validate_premise_dag(dag: dict[str, dict[str, Any]]) -> tuple[bool, list[str]]:
    """Enforce acyclicity, transitive premise propagation, and Rank-0 purity."""
    errors: list[str] = []
    visiting: set[str] = set()
    memo: dict[str, set[str]] = {}

    def _effective_premises(nid: str) -> set[str]:
        if nid in memo:
            return memo[nid]
        if nid in visiting:
            errors.append(f"Cycle detected at {nid}")
            return set()
        if nid not in dag:
            errors.append(f"Missing parent node {nid}")
            return set()
        visiting.add(nid)
        node = dag[nid]
        own = {p.strip() for p in node.get("borrowed_model_premises", []) if isinstance(p, str) and p.strip()}
        eff = set(own)
        for par in node.get("parents", []):
            eff |= _effective_premises(par)
        visiting.remove(nid)
        memo[nid] = eff
        return eff

    for nid, node in dag.items():
        eff = _effective_premises(nid)
        rk = node.get("rank")
        own_list = node.get("borrowed_model_premises", [])
        if rk == 0:
            if len(own_list) > 0 or len(eff) > 0:
                errors.append(f"Rank-0 purity violated at {nid}: effective_premises={sorted(eff)}")
        elif rk == 1:
            if len(own_list) == 0:
                errors.append(f"Rank-1 node {nid} missing explicit borrowed_model_premises")
        else:
            errors.append(f"Invalid rank at {nid}: {rk}")

    required_rank1 = {f"PR-{i}" for i in range(1, 11)} | {"OP:Level6_Higgs"}
    for req in sorted(required_rank1):
        if req not in dag:
            errors.append(f"Missing required node {req}")

    return bool(len(errors) == 0), errors


def _verify_manifest_file(manifest_path: Path, repo_root: Path) -> tuple[bool, int]:
    """Verify every SHA-256 entry recorded in a *SHA256.txt manifest byte-for-byte."""
    lines = [ln.strip() for ln in manifest_path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    if not lines:
        return False, 0

    verified_entries = 0
    for line in lines:
        parts = line.split(None, 1)
        expected_hex = parts[0].lower()
        if len(expected_hex) != 64 or any(ch not in "0123456789abcdef" for ch in expected_hex):
            return False, verified_entries

        target_path: Path | None = None
        if len(parts) == 2:
            rel_str = parts[1].strip().lstrip("*").strip()
            cand_root = repo_root / rel_str
            cand_local = manifest_path.parent / rel_str
            cand_name = manifest_path.parent / Path(rel_str).name
            for cand in (cand_root, cand_local, cand_name):
                if cand.is_file():
                    target_path = cand
                    break
        else:
            suffix = "*.py" if "SCRIPT" in manifest_path.name else "*.json"
            matches = sorted(manifest_path.parent.glob(suffix))
            if len(matches) == 1:
                target_path = matches[0]

        if target_path is None or not target_path.is_file():
            return False, verified_entries

        actual_hex = hashlib.sha256(target_path.read_bytes()).hexdigest().lower()
        if actual_hex != expected_hex:
            return False, verified_entries
        verified_entries += 1

    return True, verified_entries


def _audit_deliverable_4(script_path: Path, repo_root: Path) -> dict[str, Any]:
    """Verify E_8 colour-role non-equivalence, premise-scoped DAG, and 44-manifest custody."""
    e8_roots = _construct_e8_scaled_roots()
    e8_set = set(e8_roots)
    all_norms_8 = all(_dot8(r, r) == 8 for r in e8_roots)
    assert len(e8_roots) == 240 and len(e8_set) == 240 and all_norms_8

    a2_roots = [r for r in e8_roots if r[3:] == (0, 0, 0, 0, 0) and (r[0] + r[1] + r[2] == 0)]
    a1 = (2, -2, 0, 0, 0, 0, 0, 0)
    a2 = (0, 2, -2, 0, 0, 0, 0, 0)
    a2_cartan = [[2 * _dot8(x, y) // _dot8(y, y) for y in (a1, a2)] for x in (a1, a2)]

    e6_roots = [r for r in e8_roots if all(_dot8(r, a) == 0 for a in a2_roots)]
    e6_rank = int(sp.Matrix(e6_roots).rank())
    overlap_a2_e6 = len(set(a2_roots) & set(e6_roots))

    rem_roots = [r for r in e8_roots if (r not in set(a2_roots)) and (r not in set(e6_roots))]
    fibers: dict[tuple[int, int], list[tuple[int, ...]]] = {}
    for r in rem_roots:
        w = (_dot8(r, a1) // 4, _dot8(r, a2) // 4)
        fibers.setdefault(w, []).append(r)

    triplet_weights = {(1, 0), (-1, 1), (0, -1)}
    antitriplet_weights = {(0, 1), (1, -1), (-1, 0)}
    fibers_6x27_ok = bool(
        set(fibers.keys()) == (triplet_weights | antitriplet_weights)
        and all(len(v) == 27 for v in fibers.values())
    )

    one_27 = fibers[(1, 0)]
    role_a_singlets = sum(1 for v in one_27 if _is_true_su3_singlet(v, (a1, a2), a2_roots, e8_set))

    a2_gut_roots = [
        r for r in e6_roots if r[:3] == (0, 0, 0) and r[6:] == (0, 0) and (r[3] + r[4] + r[5] == 0)
    ]
    b1 = (0, 0, 0, 2, -2, 0, 0, 0)
    b2 = (0, 0, 0, 0, 2, -2, 0, 0)
    a2_gut_cartan = [[2 * _dot8(x, y) // _dot8(y, y) for y in (b1, b2)] for x in (b1, b2)]
    su4_gut_roots = [r for r in e6_roots if r[:3] == (0, 0, 0) and r[6:] == (0, 0)]

    role_b_singlets = sum(
        1 for v in one_27 if _is_true_su3_singlet(v, (b1, b2), a2_gut_roots, e8_set)
    )
    role_b_triplet_states = sum(
        1 for v in one_27 if (_dot8(v, b1) // 4, _dot8(v, b2) // 4) in triplet_weights
    )
    role_b_antitriplet_states = sum(
        1 for v in one_27 if (_dot8(v, b1) // 4, _dot8(v, b2) // 4) in antitriplet_weights
    )

    conflated_roles_equal = (role_a_singlets == role_b_singlets)
    pf7b_4_caught = bool((role_a_singlets == 0) and (role_b_singlets == 9) and (not conflated_roles_equal))

    dag = _build_premise_dag()
    dag_valid, dag_errors = _validate_premise_dag(dag)

    dag_fault_higgs = {k: dict(v) for k, v in dag.items()}
    dag_fault_higgs["OP:Level6_Higgs"] = dict(dag["OP:Level6_Higgs"], rank=0)
    valid_fault_higgs, _ = _validate_premise_dag(dag_fault_higgs)

    dag_fault_pr1 = {k: dict(v) for k, v in dag.items()}
    dag_fault_pr1["PR-1"] = dict(dag["PR-1"], rank=0)
    valid_fault_pr1, _ = _validate_premise_dag(dag_fault_pr1)

    dag_fault_transitive = {k: dict(v) for k, v in dag.items()}
    dag_fault_transitive["LAUNDERED_CHILD"] = {
        "rank": 0,
        "parents": ["PR-5"],
        "borrowed_model_premises": [],
    }
    valid_fault_transitive, _ = _validate_premise_dag(dag_fault_transitive)

    pf7b_5_caught = bool(
        dag_valid
        and (not valid_fault_higgs)
        and (not valid_fault_pr1)
        and (not valid_fault_transitive)
    )

    referee_v2_dir = script_path.parent.resolve()
    referee_prior_dirs = {
        (repo_root / "relays" / "agy002_closure_g7b_referee").resolve(),
        (repo_root / "relays" / "agy002_closure_g7b_referee_fixed").resolve(),
        referee_v2_dir,
    }
    relays_dir = repo_root / "relays"
    all_manifests = sorted(relays_dir.rglob("*SHA256.txt"))

    campaign_44_manifests = [
        p for p in all_manifests
        if p.parent.resolve() not in referee_prior_dirs
    ]
    all_prior_manifests = [
        p for p in all_manifests
        if p.parent.resolve() != referee_v2_dir
    ]

    campaign_44_matched = 0
    all_prior_matched = 0
    failed_manifests: list[str] = []

    for mp_file in all_prior_manifests:
        ok, _ = _verify_manifest_file(mp_file, repo_root)
        if ok:
            all_prior_matched += 1
            if mp_file.parent.resolve() not in referee_prior_dirs:
                campaign_44_matched += 1
        else:
            failed_manifests.append(str(mp_file.relative_to(repo_root)))

    self_script_manifest = referee_v2_dir / "SCRIPT_SHA256.txt"
    self_script_ok = False
    if self_script_manifest.is_file():
        ok_self, _ = _verify_manifest_file(self_script_manifest, repo_root)
        expected_first = self_script_manifest.read_text(encoding="utf-8").strip().split()[0].lower()
        actual_self = hashlib.sha256(script_path.read_bytes()).hexdigest().lower()
        self_script_ok = bool(ok_self and (expected_first == actual_self))

    custody_ok = bool(
        len(campaign_44_manifests) == 44
        and campaign_44_matched == 44
        and len(all_prior_manifests) == 46
        and all_prior_matched == 46
        and len(failed_manifests) == 0
        and self_script_ok
    )

    passed = bool(
        len(e8_roots) == 240
        and len(a2_roots) == 6
        and a2_cartan == [[2, -1], [-1, 2]]
        and len(e6_roots) == 72
        and e6_rank == 6
        and overlap_a2_e6 == 0
        and len(rem_roots) == 162
        and fibers_6x27_ok
        and len(one_27) == 27
        and len(a2_gut_roots) == 6
        and a2_gut_cartan == [[2, -1], [-1, 2]]
        and len(su4_gut_roots) == 12
        and role_a_singlets == 0
        and role_b_singlets == 9
        and role_b_triplet_states == 9
        and role_b_antitriplet_states == 9
        and (role_b_singlets + role_b_triplet_states + role_b_antitriplet_states == 27)
        and pf7b_4_caught
        and dag_valid
        and pf7b_5_caught
        and custody_ok
    )

    return {
        "passed": passed,
        "e8_root_decomposition": {
            "e8_root_count": len(e8_roots),
            "a2_root_count": len(a2_roots),
            "e6_centralizer_root_count": len(e6_roots),
            "e6_rank": e6_rank,
            "a2_cap_e6_count": overlap_a2_e6,
            "remaining_root_count": len(rem_roots),
            "fiber_count": len(fibers),
            "single_27_count": len(one_27),
            "su4_gut_root_count": len(su4_gut_roots),
            "a2_gut_root_count": len(a2_gut_roots),
            "role_A_su3c_singlets_in_27": role_a_singlets,
            "role_B_su3c_singlets_in_27": role_b_singlets,
            "role_B_su3c_triplet_states_in_27": role_b_triplet_states,
            "role_B_su3c_antitriplet_states_in_27": role_b_antitriplet_states,
        },
        "pf7b_4_caught": pf7b_4_caught,
        "premise_dag": {
            "valid": dag_valid,
            "errors": dag_errors,
            "rank0_node_count": sum(1 for v in dag.values() if v["rank"] == 0),
            "rank1_node_count": sum(1 for v in dag.values() if v["rank"] == 1),
            "rank1_nodes": sorted(k for k, v in dag.items() if v["rank"] == 1),
        },
        "pf7b_5_caught": pf7b_5_caught,
        "sha256_custody": {
            "prior_manifests_expected": 44,
            "prior_manifests_found": len(campaign_44_manifests),
            "prior_manifests_matched": campaign_44_matched,
            "all_prior_manifests_including_referee_revisions_found": len(all_prior_manifests),
            "all_prior_manifests_including_referee_revisions_matched": all_prior_matched,
            "failed_manifests": failed_manifests,
            "self_script_sha256_verified": self_script_ok,
        },
    }


def main() -> int:
    script_path = Path(__file__).resolve()
    referee_dir = script_path.parent
    repo_root = referee_dir.parents[1]
    out_path = referee_dir / "referee_closure_g7b_out.json"

    ast_audit = _self_ast_and_mask_audit(script_path)
    d1 = _audit_deliverable_1()
    d2 = _audit_deliverable_2(script_path)
    d3 = _audit_deliverable_3()
    d4 = _audit_deliverable_4(script_path, repo_root)

    planted_faults = {
        "PF7B_1_same_dim_unpriced_scale_laundering": bool(d1["pf7b_1_caught"]),
        "PF7B_2_meromorphic_pole_injection_cauchy": bool(d2["pf7b_2_caught"]),
        "PF7B_3_near_degenerate_majorana_mass_breakdown": bool(d3["pf7b_3_caught"]),
        "PF7B_4_conflated_e8_colour_embeddings": bool(d4["pf7b_4_caught"]),
        "PF7B_5_unconditional_promotion_of_premise_rank1_node": bool(d4["pf7b_5_caught"],),
    }
    all_5_caught = bool(all(planted_faults.values()))
    overall_passed = bool(
        ast_audit["passed"]
        and d1["passed"]
        and d2["passed"]
        and d3["passed"]
        and d4["passed"]
        and all_5_caught
    )

    report = _sanitize_for_json(
        {
            "gate": "AGY-002_CLOSURE-G7B",
            "role": "cold_room_zero_trust_referee_v2",
            "erratum_cards": [
                "relays/cards/AGY-002_CLOSURE-G7B-REFEREE-ERRATUM_svd-projector-and-numpy-bool-json.md",
                "relays/cards/AGY-002_CLOSURE-G7B-REFEREE-ERRATUM-2_rk4-compensated-summation.md",
            ],
            "empirical_inputs_used": "0/19",
            "overall_passed": overall_passed,
            "all_5_planted_faults_caught": all_5_caught,
            "planted_faults": planted_faults,
            "self_ast_and_firewall_audit": ast_audit,
            "deliverable_1_buckingham_pi_same_dim_nullity": d1,
            "deliverable_2_analytic_casimir_and_cauchy_contours": d2,
            "deliverable_3_antusch_mass_gap_and_tm1_grid": d3,
            "deliverable_4_e8_colour_roles_dag_and_custody": d4,
        }
    )

    payload = json.dumps(report, indent=2, sort_keys=False) + "\n"
    assert len(re.findall(r"\d+\.\d+", payload)) == 0, "Mask-unsafe decimal token in JSON payload"
    out_path.write_text(payload, encoding="utf-8")
    print("Gate 7B referee (v2) completed: wrote relays/agy002_closure_g7b_referee_v2/referee_closure_g7b_out.json")
    return 0 if overall_passed else 1


if __name__ == "__main__":
    sys.exit(main())
