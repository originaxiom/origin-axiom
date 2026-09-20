"""Post-failure F06 expectation repair; unchanged producer and explicit old-test coverage."""
import importlib.util
from itertools import combinations
from pathlib import Path
import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('f06_original_tests', Path(__file__).with_name('test_verify.py'))
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)
m = original.m

UNCHANGED = (
    'test_parent_charge_and_full_isotropic_current',
    'test_flatness_is_full_matrix_and_holds_before_the_PDE',
    'test_entire_moment_equation_not_just_its_central_projection',
    'test_rank_two_central_retuning_keeps_a_nonzero_su3_residual',
    'test_dual_solution_reverses_source_sign_without_changing_metric',
    'test_constant_v_requires_zero_amplitude_and_is_not_a_false_positive',
    'test_christoffel_ricci_tensor_and_scalar_are_derived',
    'test_hyperbolic_metric_control_has_negative_curvature_but_fails_moment',
    'test_higgs_tensor_norm_and_curvature_sign_with_correct_trace',
    'test_full_einstein_comparison_has_a_hessian_obligation_not_just_trace',
    'test_harmonic_quadratic_change_keeps_BPS_but_fails_einstein_tensor',
    'test_einstein_action_trace_really_implies_the_tensor_equation_in_3d',
    'test_explicit_ball_PDE_and_finite_boundary_distance',
    'test_maximal_ball_Higgs_norm_diverges_logarithmically_not_finitely',
    'test_boundary_flux_is_retained_and_balances_volume_source',
    'test_nonparallel_higgs_blocks_the_homogeneous_gap_inference',
)


@pytest.mark.parametrize('name', UNCHANGED)
def test_unchanged_original_assertions(name):
    getattr(original, name)()


def test_corrected_polynomial_and_all_originally_unreached_kernel_assertions():
    h = m.center_h(1)
    lam = s.symbols('lam')
    assert h == h.H
    actual = h.charpoly(lam).as_expr()
    corrected = lam**5*(lam-s.Rational(1, 2))**3*(lam-s.Rational(3, 4))**4
    old = lam**5*(lam-s.Rational(1, 2))**6*(lam-s.Rational(3, 4))
    assert s.factor(actual-corrected) == 0
    assert s.factor(actual-old) != 0
    assert len(h.nullspace()) == 5
    b11, b22, b12, b13, b23 = s.symbols('b11 b22 b12 b13 b23')
    b = s.Matrix([[b11, b12, b13], [b12, b22, b23], [b13, b23, -b11-b22]])
    u = s.Matrix([value for i in range(3) for value in [0, *list(b.row(i))]])
    assert h*u == s.zeros(12, 1)
    assert m.center_h(0) == s.diag(s.Rational(3, 4), *([s.Rational(1, 4)]*3))
    names = {name for name in vars(original) if name.startswith('test_')}
    assert names == set(UNCHANGED) | {'test_center_algebraic_operator_has_exact_kernel_but_is_not_the_full_Laplacian'}


def test_independent_component_formula_includes_the_whole_positive_adjoint_norm():
    rr = s.symbols('r0:12', real=True)
    ii = s.symbols('i0:12', real=True)
    values = [r+s.I*i for r, i in zip(rr, ii)]
    t = values[:3]
    b = s.Matrix(3, 3, values[3:])
    u = s.Matrix([entry for j in range(3) for entry in [t[j], *list(b.row(j))]])
    contraction = s.Matrix([s.trace(b), *t])/2
    wedge_components = []
    for i, j in combinations(range(3), 2):
        block = s.Matrix([b[j, i]-b[i, j], 0, 0, 0])/2
        block[i+1] = t[j]/2
        block[j+1] = -t[i]/2
        wedge_components.extend(block)
    wedge_vector = s.Matrix(wedge_components)
    assert s.expand(m.center_t(0).H*u-contraction) == s.zeros(4, 1)
    assert s.expand(m.center_t(1)*u-wedge_vector) == s.zeros(12, 1)
    norm = (contraction.H*contraction)[0]+(wedge_vector.H*wedge_vector)[0]
    expected = (s.conjugate(s.trace(b))*s.trace(b)+3*sum(s.conjugate(x)*x for x in t)
                +sum(s.conjugate(b[i, j]-b[j, i])*(b[i, j]-b[j, i]) for i, j in combinations(range(3), 2)))/4
    assert s.expand(norm-expected) == 0
    assert s.expand((u.H*m.center_h(1)*u)[0]-expected) == 0


def test_single_component_witness_falsifies_the_old_omitted_term():
    u = s.zeros(12, 1)
    u[0] = 1
    adjoint_norm = (u.H*m.center_t(0)*m.center_t(0).H*u)[0]
    wedge_norm = (u.H*m.center_t(1).H*m.center_t(1)*u)[0]
    assert adjoint_norm == s.Rational(1, 4)
    assert wedge_norm == s.Rational(1, 2)
    assert adjoint_norm+wedge_norm == s.Rational(3, 4)
    assert adjoint_norm+wedge_norm != s.Rational(1, 2)
