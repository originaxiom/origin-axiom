import sympy as s
import verify as v


def test_all_safeguards():
    rows = v.checks()
    assert rows and all(rows.values())


def test_actual_noncommuting_transport_and_end_gluing():
    a, b = v.literal_coefficient()
    assert v.zero(a*b+b*a)
    assert not v.zero(a*b-b*a)
    assert len((a-s.I*s.eye(6)).nullspace()) == 3
    assert v.checks()['same_actual_coefficient_as_nodal_packet']


def test_integer_interval_is_strict_and_not_a_frequency_window():
    assert v.laurent_interval(s.Rational(1,4)) == (0,)
    assert v.laurent_interval(s.Rational(3,4)) == ()
    assert v.laurent_interval(s.Integer(0)) == ()
    assert v.laurent_interval(s.Rational(1,2)) == ()
    assert v.laurent_interval(s.Rational(401,4)) == (-100,)


def test_profile_requires_the_critical_trace_and_central_sign():
    rows = v.checks()
    assert rows['profile_fourth_power_derivative']
    assert rows['wrong_puncture_sign_rejected']
    assert rows['regular_trace_rejects_only_scalar_mode']
    assert rows['near_puncture_nonzero_critical_coefficient_squared']
    assert rows['upper_end_norm_integrable'] and rows['lower_end_norm_integrable']


def test_metric_scale_and_nonvacuous_no_escape_control():
    rows = v.checks()
    assert rows['actual_sheared_fibre_scale'] and rows['inverse_complement_scale']
    assert rows['cutoff_commutator_exact_norm']
    assert rows['periodic_control_actual_eigenfunction']
    assert rows['periodic_control_orthogonal_to_constants']
    assert rows['periodic_control_closing_gap']
