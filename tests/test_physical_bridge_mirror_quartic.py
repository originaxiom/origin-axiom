"""R34 algebraic matching; no quantum-phase or geometric-overlap assertions."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/mirror_quartic.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_mirror_quartic', PATH)
mq = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mq)


def test_exterior_engine_known_positive_and_negative():
    e = [{(i,): sp.Integer(1)} for i in range(4)]
    wedge = mq.cd.wedge
    assert wedge(e[0], e[0]) == {}
    assert wedge(e[0], e[1]) == {(0, 1): 1}
    assert wedge(e[1], e[0]) == {(0, 1): -1}
    assert wedge(wedge(e[0], e[1]), e[2]) == wedge(e[0], wedge(e[1], e[2]))
    B = {(0, 1): 1, (2, 3): 1}
    assert wedge(B, B) == {(0, 1, 2, 3): 2}
    assert wedge({(0, 1): 1}, {(0, 1): 1}) == {}


@pytest.mark.parametrize('sign', (1, -1))
def test_full_epsilon_bilinear_normalization(sign):
    for Y, B in zip(mq.mi.clifford_data()['sectors'][sign]['yukawa'], mq.bilinears(sign)):
        full = {}
        A = sp.kronecker_product(sp.Matrix([[0, 1], [-1, 0]]), Y)
        for i in range(32):
            for j in range(32):
                if i != j and A[i, j] != 0:
                    key = tuple(sorted((i, j)))
                    full[key] = full.get(key, 0)+(1 if i < j else -1)*A[i, j]
        assert mq.clean(full) == B
        assert B


@pytest.mark.parametrize('sign', (1, -1))
def test_nonzero_Grassmann_quartic_all_coefficients_independent(sign):
    Q = mq.quartic(sign)
    assert Q and Q == mq.minor_quartic(sign)
    witness = min(Q)
    assert Q[witness] != 0
    assert Q[witness] == mq.permutation_coefficient(sign, witness)
    assert all(len(k) == 4 and sum(i < 16 for i in k) == 2 for k in Q)


@pytest.mark.parametrize('sign', (1, -1))
def test_commuting_Fierz_comparator_is_not_the_fermion(sign):
    assert mq.commuting_quartic(sign) == {}
    assert mq.quartic(sign) != {}


@pytest.mark.parametrize('sign', (1, -1))
def test_all_45_gauge_and_three_Lorentz_generators(sign):
    row = mq.exterior_controls(sign)
    assert row['ward_count'] == 45 and row['ward_all'] and row['lorentz_all']
    assert row['omitted_components_rejected']
    # The fermion-number generator acts nontrivially, unlike the Lorentz Cartan.
    assert mq.variation(mq.quartic(sign), sp.eye(32)) == {k: 4*v for k, v in mq.quartic(sign).items()}


def test_invalid_sector_and_generator_fail_closed():
    with pytest.raises(ValueError):
        mq.bilinears(0)
    with pytest.raises(ValueError):
        mq.variation({(0, 1): 1}, sp.eye(16))
    with pytest.raises(ValueError):
        mq.permutation_coefficient(1, (0, 0, 1, 2))


def test_Gaussian_stationary_equations_and_value():
    g = mq.gaussian_controls()
    assert g['stationary_residuals'] == [0, 0]
    assert g['stationary_value_matches'] and g['inverse_matches']
    assert g['wrong_Phi_conjugation_rejected']


def test_positive_singular_and_negative_scalar_controls():
    g = mq.gaussian_controls()
    assert g['stable_control_eigenvalues'] == [1, 5]
    assert g['unstable_control_eigenvalues'] == [-1, 3]
    assert g['singular_control'] == 0
    assert g['hessian_determinant_matches'] and g['gaussian_log_coefficient'] == 5


def test_all_ten_interaction_coefficients_not_just_channel_count():
    g = mq.gaussian_controls()
    s = g['symbols']
    r, k, P, Pb = (s[x] for x in ('r', 'kappa', 'Phi', 'Phi_bar'))
    ym, ymb, yp, ypb = (s[x] for x in ('y_m', 'y_m_bar', 'y_p', 'y_p_bar'))
    expected = {
        (1, 1, 0, 0): r*ym*ymb, (1, 0, 1, 0): r*ym*yp,
        (0, 1, 0, 1): r*ymb*ypb, (0, 0, 1, 1): r*yp*ypb,
        (2, 0, 0, 0): k*P*ym**2, (1, 0, 0, 1): 2*k*P*ym*ypb,
        (0, 0, 0, 2): k*P*ypb**2, (0, 2, 0, 0): k*Pb*ymb**2,
        (0, 1, 1, 0): 2*k*Pb*ymb*yp, (0, 0, 2, 0): k*Pb*yp**2}
    actual = {tuple(row['powers']): row['coefficient'] for row in g['monomials']}
    assert actual == expected
    assert g['full_H_charge_residual'] == 0


def test_mirror_only_limit_and_breaking_requires_locking():
    g = mq.gaussian_controls()
    s = g['symbols']
    a, b = s['B_m'], s['B_m_bar']
    r, k, P, Pb, ym, ymb = (s[x] for x in ('r', 'kappa', 'Phi', 'Phi_bar', 'y_m', 'y_m_bar'))
    only = sp.expand(g['numerator'].subs({s['y_p']: 0, s['y_p_bar']: 0}))
    assert only == sp.expand(r*ym*ymb*a*b+k*P*ym**2*a**2+k*Pb*ymb**2*b**2)
    assert sp.expand(only.subs(k, 0)-r*ym*ymb*a*b) == 0
    assert sp.expand(only.subs({P: 0, Pb: 0})-r*ym*ymb*a*b) == 0
    assert s['B_p'] not in only.free_symbols and s['B_p_bar'] not in only.free_symbols


def test_ordinary_terms_survive_when_allowed_coupling_is_nonzero():
    g = mq.gaussian_controls()
    s = g['symbols']
    only = sp.expand(g['numerator'].subs({s['y_m']: 0, s['y_m_bar']: 0}))
    assert only != 0 and s['B_p'] in only.free_symbols
    both = g['numerator']
    assert sp.diff(both, s['B_m'], s['B_p']) != 0


def test_continuous_phase_kernel_is_gauge_not_independent_mirror_number():
    p = mq.phase_controls()
    gauge = sp.Matrix([1, -1, 2, 4])
    assert p['rank'] == 3 and len(p['kernel']) == 1
    assert p['matrix']*gauge == sp.zeros(4, 1)
    assert p['kernel'][0]*4 == gauge
    assert p['without_ordinary_yukawa_rank'] == 3
    assert p['without_locking_rank'] == 2
    assert p['without_ordinary_and_mixing_rank'] == 2
    assert p['bare_mirror_quartic_charge'] == -4
    assert p['Phi_completed_quartic_charge'] == 0


def test_dimensions_and_breakdown_of_near_critical_matching():
    p, g = mq.phase_controls(), mq.gaussian_controls()
    assert p['quartic_dimension']+p['conserving_coefficient_dimension'] == 4
    assert p['Phi_quartic_dimension']+p['breaking_coefficient_dimension'] == 4
    s = g['symbols']
    r, k, f = s['r'], s['kappa'], s['f']
    D = g['determinant'].subs({s['Phi']: f, s['Phi_bar']: f})
    assert sp.factor(D) == (r-2*k*f)*(r+2*k*f)
    assert D.subs(r, 2*k*f) == 0
    assert sp.diff(D, r).subs({r: 2*k*f, k: 1, f: 1}) != 0
