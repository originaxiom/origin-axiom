"""Post-result numerical regression locks: known positives, not blind predictions.

R5's pre-run tests intentionally did not assert its hoped-for sign. The first
result and independent derivative check now exist. These additional locks
keep their positive content from disappearing behind generic consistency tests.
Changing the action or conventions requires a deliberate new scoped result.
"""
import numpy as np

from reports.physical_bridge_2026_09_05 import quantum_derivative as d
from reports.physical_bridge_2026_09_05 import quantum_vacuum as q


def test_positive_octet_and_triplet_coefficients_are_retained():
    result = d.analytic_curvatures()
    expected = {"color_octet": [0.002521562402497298, 0.1187021837494442],
                "weak_triplet": [0.011521110594170905, 0.11047574321489007]}
    for name, values in expected.items():
        actual = result[name]["scalar_vector_curvature_by_mu"]["1.0"]
        np.testing.assert_allclose(actual, values, rtol=1e-9, atol=1e-11)
        assert min(actual) > 0
        assert result[name]["lambda_point2_g_point5_leading_m2"] > 0


def test_preselected_SM_energy_advantage_over_named_competitors_is_retained():
    points = q.named_backgrounds()
    reference = q.potential_parts(*q.spectra(points["SM_Y"]), .2, .5)
    for name, expected in [("SU4_U1", 0.0006567328101432235),
                           ("old_generic_competitor", 0.0028009237201501933)]:
        actual = float(np.sum(q.potential_parts(*q.spectra(points[name]), .2, .5)-reference))
        assert actual > 0
        np.testing.assert_allclose(actual, expected, rtol=1e-9, atol=1e-11)
