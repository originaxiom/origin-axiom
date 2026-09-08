"""R21 action tests assert derived derivatives, phases and descent."""
import importlib.util
from pathlib import Path

import sympy as sp

PATH = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/anomaly_action_control.py'
SPEC = importlib.util.spec_from_file_location('physical_bridge_anomaly_action_control', PATH)
aa = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(aa)


def test_covariant_kinetic_derived_in_cartesian_and_polar_fields():
    r = aa.kinetic()
    assert r['polar_identity'] and r['finite_gauge_covariance']
    assert r['missing_connection_fails'] and r['gauge_mass_check']
    assert r['gauge_mass_squared'] != 0


def test_radial_mass_from_potential_and_ungauged_phase_zero():
    r = aa.kinetic()
    f, lam = sp.symbols('f lambda', real=True)
    assert r['potential_radial_first'] == r['potential_phase_second'] == 0
    assert r['potential_radial_second'] == 2*lam*f*f
    assert r['potential_radial_second'].subs({lam: -1, f: 1}) < 0


def test_mass_monomials_and_spinor_mass_exclusion():
    r = aa.masses()
    f, M, yv, yn = sp.symbols('f M yV yN', positive=True)
    assert r['vector_mass_at_zero_phase'] == yv*f/sp.sqrt(2)
    assert r['singlet_mass_at_zero_phase'] == yn*f*f/(2*M)
    assert r['vector_phase_cancellation'] and r['singlet_phase_cancellation']
    assert r['wrong_singlet_conjugation_fails']
    assert r['spinor_opposite_weight_pairs'] == []


def test_full_polynomial_descent_cancellation_and_wrong_charge_control():
    r = aa.descent()
    assert sp.expand(r['light_variation']+r['counterterm_variation']) == 0
    assert r['light_variation'] != 0 and r['missing_counterterm_fails']
    assert r['wrong_charge_fails'] and r['cancellation']


def test_residual_gauge_subgroup_acts_on_actual_spinor_weights():
    r = aa.residual()
    assert r['spinor_phase_exponents'] == [sp.Rational(1, 3)]*16
    assert r['quotient_phase'] == sp.Rational(1, 3)
    assert r['gauge_element_order'] == 3
    assert r['cube_in_kernel'] and r['generator_outside_spin10']
