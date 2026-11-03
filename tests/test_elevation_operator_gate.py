"""
Tests locking the three core elevation modules in src/origin_axiom/:
1. src/origin_axiom/twisted_norms.py (Theorem 1: exact closed-form c_s(tau, w), resolution of B1788 (a)-(b)).
2. src/origin_axiom/operator_gate.py (Gate 0: The Algebraic Operator Gate, Theorem 2: CKM corner inversion,
   and the 4D Quaternionic + 3-Fold Cover Frame FR-COV).
3. src/origin_axiom/stepb_audit.py (Step B choice 30900 decoding, 7,680 order-12 massless-electron choices,
   and strict 10-column physical-choice mask).
"""
from __future__ import annotations

from fractions import Fraction
import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from origin_axiom.twisted_norms import (
    channel_pair_decay_exponents,
    closed_form_cA,
    cusp_combination_D_inf,
    sector_higgs_twist_multiple,
)
from origin_axiom.operator_gate import (
    ckm_full_diagnostics,
    direct_quaternion_coupling,
    evaluate_operator_gate,
    lagrange_ckm_compromise,
    m004_three_fold_cover_invariants,
    quaternionic_4d_yukawa,
    serre_dr_dot_dr_eta6_identity,
    yukawa_4d_determinant_factorization,
)
from origin_axiom.parameter_ledger import (
    compare_frame_input_ledgers,
    m004_cover_monodromy_fixed_torsion,
    nineteen_parameter_impact_table,
)
from origin_axiom.stepb_audit import (
    count_order12_massless_electron_choices,
    decode_stepb_choice_index,
    strict_ten_physical_choice_mask,
)


def test_theorem1_sector_independence_and_closed_form_c():
    # 1. All three fermion sectors have |q_L + q_R| == 3:
    assert abs(sector_higgs_twist_multiple("up")) == 3
    assert abs(sector_higgs_twist_multiple("down")) == 3
    assert abs(sector_higgs_twist_multiple("lepton")) == 3

    # 2. Cusp combination D^inf(alpha) = c_j^inf + c_k^inf - c_1^inf - c_i^inf
    # vanishes on (0, 1/2) iff alpha in {1/12, 1/4, 5/12} (resolving B1788 Hypothesis (b)):
    for alpha_zero in (Fraction(1, 12), Fraction(1, 4), Fraction(5, 12)):
        d_val = cusp_combination_D_inf(alpha_zero)
        assert d_val is not None and abs(d_val) < 1e-14

    for alpha_nonzero in (Fraction(1, 5), Fraction(2, 5), Fraction(1, 7), Fraction(3, 8), Fraction(4, 9)):
        d_val = cusp_combination_D_inf(alpha_nonzero)
        assert d_val is not None and abs(d_val) > 0.5

    # 3. Exact fermion-independent decay exponents E(c_1 - c_i) and E(c_j - c_k)
    # satisfy E(c_1 - c_i) + E(c_j - c_k) = 1/4 and resolve B1788's anomalies:
    exp_2_5 = channel_pair_decay_exponents(Fraction(2, 5))
    assert exp_2_5["E_c1_minus_ci"] == Fraction(1, 10)
    assert exp_2_5["E_cj_minus_ck"] == Fraction(3, 20)
    assert exp_2_5["sum"] == Fraction(1, 4)

    exp_1_7 = channel_pair_decay_exponents(Fraction(1, 7))
    assert exp_1_7["E_c1_minus_ci"] == Fraction(3, 14)
    assert exp_1_7["E_cj_minus_ck"] == Fraction(1, 28)
    assert exp_1_7["sum"] == Fraction(1, 4)

    exp_4_9 = channel_pair_decay_exponents(Fraction(4, 9))
    assert exp_4_9["E_c1_minus_ci"] == Fraction(1, 6)
    assert exp_4_9["E_cj_minus_ck"] == Fraction(1, 12)
    assert exp_4_9["sum"] == Fraction(1, 4)

    # 4. Compare closed_form_cA against B1691's 2D Gauss-Legendre quadrature cA:
    v_dir = ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/correction"
    sys.path.insert(0, str(v_dir))
    import b1656_funcs as B

    tau = complex(0.17, 1.85)
    for a_line, b_line in ((Fraction(2, 5), Fraction(1, 10)), (Fraction(1, 3), Fraction(1, 9))):
        w = B.line_w(a_line, b_line, tau)
        x, y = B.sector_twists(w, tau, 1, -4)
        r_res = B.residues(x, y, tau)
        c_quad = B.cA(x, y, tau, r_res)
        c_exact = closed_form_cA(tau, a_line, b_line)
        for s in ("1", "i", "j", "k"):
            assert c_exact[s] is not None
            if c_quad[s] is not None:
                assert abs(c_quad[s] - c_exact[s]) < 5e-12


def test_theorem2_4d_quaternionic_yukawa_and_operator_gate():
    # 1. Verify exact 4D quaternionic Yukawa formula against direct 2x2 quaternion trace bilinear:
    rng = np.random.default_rng(42)
    for a0 in (0.0 + 0.0j, 0.35 - 0.21j):
        h_vec = rng.normal(size=3) + 1j * rng.normal(size=3)
        m1 = complex(rng.normal() + 1j * rng.normal())
        m_perp = rng.normal(size=3) + 1j * rng.normal(size=3)

        y_formula = quaternionic_4d_yukawa(a0, h_vec, m1, m_perp)
        y_direct = direct_quaternion_coupling(a0, h_vec, m1, m_perp)
        assert np.allclose(y_formula, y_direct, atol=1e-14)

        # At a0 == 0, Y h = Y^T h = (h . h) m_perp; at a0 != 0, Y h picks up a0*(m1*h - m_perp x h):
        expected_yh = (
            np.dot(h_vec, h_vec) * m_perp
            + a0 * (m1 * h_vec - np.cross(m_perp, h_vec))
        )
        assert np.allclose(y_formula @ h_vec, expected_yh, atol=1e-14)

    # 2. Verify Lagrange-multiplier CKM compromise (0.7347, 0.7347, 1.3611):
    r12, r23, r13 = lagrange_ckm_compromise()
    assert abs(r12 - 0.7347) < 5e-4
    assert abs(r23 - 0.7347) < 5e-4
    assert abs(r13 - 1.3611) < 5e-4
    assert abs((r13 / (r12 * r23)) - (0.22500 * 0.04182 / 0.003732)) < 1e-12

    # 3. Verify m004 3-fold cover and colour-center Wilson line torsion invariants:
    inv = m004_three_fold_cover_invariants()
    assert inv["det_LR_minus_i" if "det_LR_minus_i" in inv else "det_LR_minus_I"] == -1
    assert inv["deck_only_S3_commutant_dim_R"] == 2
    assert inv["deck_commutant_dim_R"] == 1
    assert inv["forces_H_proportional_to_I"] is True
    assert abs(float(inv["alexander_at_omega_abs"]) - 4.0) < 1e-12
    assert abs(float(inv["reidemeister_torsion_at_omega_abs"]) - 4.0 / math.sqrt(3.0)) < 1e-12

    # 4. Evaluate Gate 0 (The Algebraic Operator Gate) on FR-FIB vs FR-COV:
    rep_fib = evaluate_operator_gate("FR-FIB")
    assert rep_fib.passed is False
    assert rep_fib.clauses_passed == 0
    assert rep_fib.sample_Vub_over_Vtd > 10.0
    assert rep_fib.sample_sin_delta_CP < 0.10

    rep_cov = evaluate_operator_gate("FR-COV")
    assert rep_cov.passed is True
    assert rep_cov.clauses_passed == 4
    assert rep_cov.sample_Vub_over_Vtd < 1.0
    assert rep_cov.sample_sin_delta_CP > 0.50


def test_stepb_structural_audit_defects():
    manifest = json.loads(
        (ROOT / "scripts/census/REFINED_CENSUS_MANIFEST.json").read_text(encoding="utf-8")
    )["per_file"]

    # 1. Decode choice 30900 selected by six_mixture in B1825:
    c30900 = decode_stepb_choice_index(30900, manifest)
    assert c30900["line"] == (Fraction(2, 5), Fraction(0, 1))
    assert c30900["direction"] == "F_26"
    assert c30900["radius"] == "L_max"
    assert c30900["reading"] == ("S~", "S", "S")
    assert c30900["has_complex_ckm"] is True

    # And verify the two null-quaternion directions R (d_idx=2) and t=-5/288 (d_idx=3) have has_complex_ckm=False:
    c_r = decode_stepb_choice_index(2 * 16, manifest)
    c_t = decode_stepb_choice_index(3 * 16, manifest)
    assert c_r["direction"] == "R" and c_r["has_complex_ckm"] is False
    assert c_t["direction"] == "t=-5/288" and c_t["has_complex_ckm"] is False

    # 2. Count order-12 massless-electron choices included in physical_choice:
    o12 = count_order12_massless_electron_choices(manifest)
    assert o12["order_12_lines"] == 48
    assert o12["order_12_total_choices"] == 9216
    assert o12["order_12_choices_in_physical_choice"] == 7680
    assert abs(float(o12["fraction_of_40000_physical_choices"]) - 0.192) < 1e-12

    # 3. Verify strict_ten_physical_choice_mask rejects massless-electron choices (col 5 = -inf)
    # even when CKM columns 6..9 are finite:
    f_mat = np.full((4, 10), -2.0, dtype=float)
    f_mat[2:, 5] = -np.inf  # choice 1 has massless electron (e/tau = 0)
    r_tab = np.array([[0, 1], [2, 3]], dtype=np.int64)
    phys_ten, zero10 = strict_ten_physical_choice_mask(f_mat, r_tab)
    assert phys_ten.tolist() == [True, False]
    assert zero10[1, 5] == True and not zero10[1, 6:10].any()


def test_theorem3_theorem4_and_19_parameter_ledger():
    # 1. Theorem 3: Exact quaternionic determinant factorization
    # det(Y_s^4D) == (a_0^2 + h.h) * (m_1^2 + m_perp.m_perp) * (a_0*m_1 + h.m_perp)
    rng = np.random.default_rng(20261103)
    for _ in range(25):
        a0 = complex(rng.normal() + 1j * rng.normal())
        h_vec = rng.normal(size=3) + 1j * rng.normal(size=3)
        m1 = complex(rng.normal() + 1j * rng.normal())
        m_perp = rng.normal(size=3) + 1j * rng.normal(size=3)
        res = yukawa_4d_determinant_factorization(a0, h_vec, m1, m_perp)
        assert float(res["rel_error"]) < 1e-13

        # On the 3D null cone h.h = 0 (like primary R(tau)), det(Y) == 0 at a0 = 0
        # but det(Y) != 0 as soon as a0 != 0:
        h_null = np.array([1.0 + 0.0j, 0.0 + 0.0j, 1j], dtype=complex)  # h_null . h_null == 0
        res_zero = yukawa_4d_determinant_factorization(0.0, h_null, m1, m_perp)
        res_lifted = yukawa_4d_determinant_factorization(a0, h_null, m1, m_perp)
        assert abs(complex(res_zero["det_Y"])) < 1e-14
        assert abs(complex(res_lifted["det_Y"])) > 1e-3

    # 2. Theorem 4: DR(tau) . DR(tau) == (1/4) eta(tau)^6 modular identity:
    id4 = serre_dr_dot_dr_eta6_identity(0.093359375 + 2.742578125j)
    assert float(id4["rel_error"]) < 1e-13

    # 3. Input-reduction ledger & 0-19 parameter table:
    tors = m004_cover_monodromy_fixed_torsion()
    assert tors["det_LR_minus_I"] == -1
    assert tors["non_zero_fixed_points_k1"] == 0
    assert tors["det_LR3_minus_I"] == -16
    assert tors["non_zero_fixed_points_k3"] == 15
    assert tors["t_orbits_in_non_zero_fixed_k3"] == 5

    led = compare_frame_input_ledgers()
    assert led["FR_FIB"]["total_discrete_choices"] == 497952
    assert abs(float(led["FR_FIB"]["total_discrete_bits"]) - math.log2(497952)) < 1e-12
    assert led["FR_COV"]["total_discrete_choices"] == 6
    assert float(led["reductions"]["discrete_bits_saved"]) > 16.3
    assert led["reductions"]["hidden_kinetic_metric_reals_eliminated"] == 8

    table19 = nineteen_parameter_impact_table()
    assert len(table19) == 10
    all_names = [n for row in table19 for n in row["names"]]
    assert len(all_names) == 19

