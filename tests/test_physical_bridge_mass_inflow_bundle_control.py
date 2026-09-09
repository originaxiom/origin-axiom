"""R23 separate global characteristic-class controls; original source unchanged."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

SPEC = importlib.util.spec_from_file_location('r23_bundle_test', Path(__file__).resolve().parents[1]/
        'reports/physical_bridge_2026_09_05/mass_inflow_bundle_control.py')
b = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(b)


def test_reference_subtraction_is_the_negative_eigenbundle_not_half():
    r = b.eigenbundle_response(1, -1)
    assert sp.expand(r['response']+r['minus']) == 0
    assert sp.expand(r['response']+r['minus']/2) != 0
    assert b.eigenbundle_response(1, 1)['response'] == 0
    both = b.eigenbundle_response(-1, -1)
    assert sp.expand(both['response']+both['plus']+both['minus']) == 0


def test_full_degree_eight_expression_matches_independent_actual_weights():
    r = b.characteristic_forms()
    assert r['polynomial_identity']
    assert r['B8'] == r['independent_weight_expression']
    assert r['forms'][6] == b.m.ac.anomaly(b.m.ac.data()['spinor'])
    assert r['CPT_pair_invariant']


def test_flat_sphere_reduction_does_not_license_dropping_curved_bundle_terms():
    r = b.characteristic_forms()
    expected = -r['forms'][8]+b.K*r['forms'][6]
    assert sp.expand(r['flat_sphere_reduction']-expected) == 0
    assert r['omitted_terms'] != 0
    assert sp.Poly(r['omitted_terms'], b.K).nth(0) == 0
    assert sp.Poly(r['omitted_terms'], b.K).nth(1) == 0
    assert sp.Poly(r['omitted_terms'], b.K).nth(2) == -r['forms'][4]/2


def test_mass_reversal_changes_eigenline_but_not_the_reference_offset():
    r = b.characteristic_forms()
    assert r['inverse_line'] != -r['B8']
    assert sp.Poly(r['inverse_line'], b.K).nth(1) == -r['forms'][6]
    assert sp.Poly(r['inverse_line'], b.K).nth(0) == -r['forms'][8]


def test_compact_spin_product_integral_needs_the_full_expression():
    r = b.four_spheres()
    assert all(q == 1 for q in r['actual_charges'])
    assert r['integral'] == r['product_formula'] == -384
    assert r['truncated_integral'] == 544
    assert r['integral_class']
    other = b.four_spheres(gauge_flux=(1, -2, 3, -4), eigenline_flux=(-1, 1, 2, 0))
    assert other['integral'] == other['product_formula'] and other['integral_class']


def test_square_zero_eigenline_and_zero_flux_controls_recover_the_truncation():
    for k in ((1, 0, 0, 0), (0, 0, 0, 0)):
        r = b.four_spheres(eigenline_flux=k)
        assert r['integral'] == r['truncated_integral'] == r['product_formula']
    with pytest.raises(ValueError):
        b.four_spheres(gauge_flux=(1, 2, 3, sp.Rational(1, 2)))
