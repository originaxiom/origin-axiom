import pytest
import sympy as s
import verify as v


def test_all_exact_safeguards():
    result = v.checks()
    assert result and all(result.values())


def test_inverse_move_is_not_forward_move():
    a,b,t = v.coefficient()
    assert v.zero(t.H*b*t-a.H*b)
    assert not v.zero(t*b*t.H-a.H*b)
    assert v.zero(t.H*a*t-a)


def test_actual_cusp_spectra_and_both_spin_lifts():
    assert v.cusp_phases(1) == (s.Rational(1,8),s.Rational(5,8),s.Rational(7,8))
    assert v.cusp_phases(-1) == (s.Rational(1,8),s.Rational(3,8),s.Rational(7,8))
    for gamma in (-1,1):
        for sign in (-1,1):
            assert min(min(p,1-p) for p in v.cusp_phases(gamma,sign)) == s.Rational(1,8)
    with pytest.raises(ValueError):
        v.cusp_phases(0)


def test_profile_mixing_does_not_preserve_vertical_domain():
    result = v.checks()
    for gamma in (-1,1):
        assert result[f'{gamma}_off_diagonal_identity']
        assert result[f'{gamma}_vertical_derivative_not_cancelled']
        assert result[f'{gamma}_coupling_rank_one_not_zero']
    assert result['mixing_profile_L2_power']
    assert result['mixing_vertical_derivative_not_L2_power']


def test_quarter_coefficient_needs_mixed_term():
    result = v.checks()
    assert result['same_full_metric_Cliffords'] and result['mixed_spin_term_sign']
    for gamma in (-1,1):
        assert result[f'{gamma}_projected_quarter']
        assert result[f'{gamma}_dropped_mixed_term_detected']


def test_confinement_has_actual_frequency_and_derivative_controls():
    result = v.checks()
    assert result['radial_square_all_differential_terms']
    assert result['squared_potential_Hermitian_involution']
    assert result['shifted_mass_bound_SOS'] and result['linear_potential_bound_SOS']
    assert result['zero_phase_control_no_confinement']


def test_growing_gap_does_not_control_rotating_projection():
    result = v.checks()
    assert result['rotating_control_true_projection']
    assert result['rotating_control_exact_kernel']
    assert result['rotating_control_growing_complement_gap']
    assert result['rotating_control_unbounded_horizontal_derivative']
