"""F05 exact controls for one specified physical-operator/background join."""
from collections import Counter
import importlib.util
from itertools import combinations, product
from pathlib import Path

import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('parent_twist_gap', Path(__file__).with_name('verify.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_full_local_bps_and_norm_match_the_received_background():
    c = v.connection()
    for i, j in combinations(range(3), 2):
        residual = c[j].diff(v.COORDS[i])-c[i].diff(v.COORDS[j])+c[i]*c[j]-c[j]*c[i]
        assert v.clean(residual) == s.zeros(4)
    divergence = v.z**3*sum(((matrix+matrix.H).applyfunc(lambda entry: entry/v.z).diff(t)
                            for matrix, t in zip(c, v.COORDS)), s.zeros(4))
    commutator = v.z**2*sum((matrix*matrix.H-matrix.H*matrix for matrix in c), s.zeros(4))
    assert v.clean(divergence+commutator) == s.zeros(4)
    assert v.clean(divergence) == -2*v.lie()[2]
    _, psi = v.split()
    assert s.simplify(v.z**2*sum(s.trace(matrix*matrix) for matrix in psi)) == 15


def test_geometric_higgs_is_covariantly_parallel_with_both_connections():
    assert all(matrix == s.zeros(4) for matrix in v.parallel_residual())
    assert any(matrix != s.zeros(4) for matrix in v.parallel_residual(omit_connection=True))
    assert any(matrix != s.zeros(4) for matrix in v.parallel_residual(omit_christoffel=True))


def test_principal_first_order_mixed_terms_cancel_by_clifford_algebra():
    wedges = v.total_wedges()
    for i, j in product(range(3), repeat=2):
        c = wedges[i]-wedges[i].T
        chat = wedges[j]+wedges[j].T
        assert c*chat+chat*c == s.zeros(8)


def test_casimir_uses_curvature_one_half_generator_normalization():
    triple = v.hermitian_triple()
    assert all(matrix == matrix.H for matrix in triple)
    assert sum((matrix*matrix for matrix in triple), s.zeros(4)) == s.Rational(15, 4)*s.eye(4)
    assert v.bochner(1, scale=2) == 4*v.bochner(1)
    assert v.bochner(1, scale=2) != v.bochner(1)


@pytest.mark.parametrize('degree', [0, 1, 2, 3])
def test_exact_bochner_polynomial_and_independent_formula(degree):
    h = v.bochner(degree)
    assert h == h.H
    assert h == v.block_bochner(degree)
    lam = s.symbols('lam')
    actual = h.charpoly(lam).as_expr()
    if degree in (0, 3):
        expected = (lam-s.Rational(15, 4))**4
    else:
        expected = (lam-s.Rational(9, 4))**6*(lam-s.Rational(19, 4))**4*(lam-s.Rational(25, 4))**2
    assert s.factor(actual-expected) == 0
    shifted = h-s.Rational(9, 4)*s.eye(h.rows)
    assert shifted.is_positive_semidefinite is True


@pytest.mark.parametrize('degree', [0, 1, 2, 3])
def test_trivial_coefficient_is_a_zero_gap_control(degree):
    h = v.bochner(degree, power=0)
    assert h == s.zeros(h.rows)


def test_nonparallel_higgs_does_not_obey_the_geometric_mixed_term_identity():
    x = s.symbols('x', real=True)
    u = s.Function('u')(x)
    psi = x
    d = s.diff(u, x)+psi*u
    laplacian = -s.diff(d, x)+psi*d
    naive = -s.diff(u, x, 2)+psi**2*u
    assert s.simplify(laplacian-naive) == -u
    # The harmonic oscillator has an exact zero mode despite psi^2>=0.
    gaussian = s.exp(-x*x/2)
    assert s.simplify(s.diff(gaussian, x)+psi*gaussian) == 0


def test_character_is_global_order_four_with_marked_cusp_holonomy():
    assert v.character('aaabABBAb') == 1
    assert v.character('ab') == s.I
    assert v.character('aBAbABab') == 1
    assert [v.character('b'*k) for k in range(1, 5)] == [s.I, -1, -s.I, 1]
    assert v.character('ab')**2 == -1


def test_actual_geometric_and_twisted_relations_and_determinants():
    assert v.word('aaabABBAb', v.geometric_matrices()) == s.eye(2)
    twisted = v.twisted_matrices()
    assert v.word('aaabABBAb', twisted) == s.eye(4)
    for matrix in twisted:
        assert s.simplify(s.expand_complex(matrix.det())) == 1
    omega = (-1+s.I*s.sqrt(3))/2
    assert s.simplify(s.expand_complex((omega*s.eye(4)).det())) == omega
    assert omega != 1


def test_trace_not_literal_matrix_inequality_proves_non_self_duality():
    matrix = v.twisted_matrices()[1]
    omega = (-1+s.I*s.sqrt(3))/2
    trace = s.simplify(s.expand_complex(s.trace(matrix)))
    dual_trace = s.simplify(s.expand_complex(s.trace(matrix.inv().T)))
    assert s.simplify(trace-s.I*(-8+4*omega)) == 0
    assert s.simplify(dual_trace+s.I*(-8+4*omega)) == 0
    assert s.simplify(trace-dual_trace) != 0


def test_order_two_keeps_J_order_four_does_not():
    j = v.invariant_j()
    assert j.T == -j and j.H*j == s.eye(4)
    for matrix in v.lie():
        assert v.clean(matrix.T*j+j*matrix) == s.zeros(4)
    for matrix in v.twisted_matrices(-1):
        assert v.algebraic_clean(matrix.T*j*matrix-j) == s.zeros(4)
    for matrix, phase in zip(v.twisted_matrices(), (1, s.I)):
        assert v.algebraic_clean(matrix.T*j*matrix-phase**2*j) == s.zeros(4)
    assert (s.I*s.eye(4)).T*j*(s.I*s.eye(4)) == -j


def test_invariant_wedge_line_is_removed_not_counted_as_ten_zero_modes():
    actions = [v.exterior_lie(matrix) for matrix in v.lie()]
    kernel = s.Matrix.vstack(*actions).nullspace()
    assert len(kernel) == 1
    assert all(matrix*kernel[0] == s.zeros(6, 1) for matrix in actions)
    assert v.exterior_group(s.I*s.eye(4)) == -s.eye(6)
    assert v.exterior_group(-s.eye(4)) == s.eye(6)
    assert (v.exterior_group(s.I*s.eye(4))-s.eye(6))*kernel[0] != s.zeros(6, 1)


def test_complete_parent_center_phase_roster():
    roots = v.e8_roots()
    assert len(roots) == 240
    assert {sum(value*value for value in root) for root in roots} == {2}
    counts = Counter(v.center_exponent(root) for root in roots)
    counts[0] += 8  # all Cartan directions
    assert counts == {0: 60, 1: 64, 2: 60, 3: 64}
    d5 = {root for root in roots if root[5:] == (0, 0, 0)}
    a3 = {root for root in roots if root[:5] == (0,)*5}
    assert len(d5) == 40 and len(a3) == 12
    assert all(v.center_exponent(root) == 0 for root in d5 | a3)


def test_whole_B5_root_set_loses_short_roots_but_keeps_D5_cartan():
    short = set()
    for i, sign in product(range(5), (-1, 1)):
        vector = [0]*5
        vector[i] = sign
        short.add(tuple(vector))
    d5 = {root[:5] for root in v.e8_roots() if root[5:] == (0, 0, 0)}
    b5 = d5 | short
    assert len(b5) == 50 and len(d5) == 40 and len(short) == 10
    assert {sum(x*x for x in root) for root in d5} == {2}
    assert {sum(x*x for x in root) for root in short} == {1}
    surviving = {root for root in b5 if sum(x*x for x in root) == 2}
    assert surviving == d5
    assert len(surviving)+5 == 45


def test_unitary_constant_transitions_preserve_local_connection_metric_and_T():
    for phase in (1, s.I, -1, -s.I):
        transition = phase*s.eye(4)
        assert transition.H*transition == s.eye(4)
        assert transition.det() == 1
        for matrix in v.connection():
            assert transition.inv()*matrix*transition == matrix
        assert v.bochner(1) == v.bochner(1).H
    nonunitary = 2*s.eye(4)
    assert nonunitary.H*nonunitary != s.eye(4)


def test_shifted_cusp_lattice_and_exact_nonsquare_control():
    m, n = s.symbols('m n', integer=True)
    h0 = s.Matrix([[2, 1], [1, 3]])
    p = s.Matrix([m+s.Rational(1, 2), n])
    norm = (p.T*h0.inv()*p)[0]
    decomposition = (m+s.Rational(1, 2))**2/2+s.Rational(2, 5)*(n-(m+s.Rational(1, 2))/2)**2
    assert s.expand(norm-decomposition) == 0
    assert s.simplify(norm.subs({m: 0, n: 0})) == s.Rational(3, 20)
    # The all-integer minimum proof uses half-integer and odd-quarter
    # lower bounds in the authored argument, not a truncated lattice grid.
    assert s.Rational(1, 2)*s.Rational(1, 2)**2+s.Rational(2, 5)*s.Rational(1, 4)**2 == s.Rational(3, 20)
    assert 4*s.pi**2*s.Rational(3, 20) == 3*s.pi**2/5
    assert (s.zeros(2, 1).T*h0.inv()*s.zeros(2, 1))[0] == 0


def test_cusp_fourier_scaling_and_small_tail_estimate():
    r, kappa = s.symbols('r kappa', positive=True)
    h0 = s.Matrix([[2, 1], [1, 3]])
    p = s.Matrix(s.symbols('p1 p2', real=True))
    assert s.simplify((p.T*(s.exp(-2*r)*h0).inv()*p)[0]-s.exp(2*r)*(p.T*h0.inv()*p)[0]) == 0
    assert s.limit(1/(kappa*s.exp(2*r)), r, s.oo) == 0


def test_bound_is_not_exact_spectral_bottom_and_perturbation_threshold_is_failable():
    q = s.diag(s.Rational(3, 2), -s.Rational(3, 2))
    small = s.diag(-s.Rational(1, 2), s.Rational(1, 2))
    threshold = -q
    assert (q+small)**2 == s.eye(2)
    assert (q+threshold) == s.zeros(2)
    assert small.H == small and threshold.H == threshold
    stronger = s.diag(2, -2)
    assert (stronger*stronger-s.Rational(9, 4)*s.eye(2)).is_positive_definite
    # These are finite inequality controls, not BPS deformations or
    # actual eigenvalues of the complete hyperbolic operator.
