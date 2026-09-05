"""Post-result regression locks for the pre-sealed upstream action instrument."""
import pytest

from reports.physical_bridge_2026_09_05 import upstream_check as u


@pytest.fixture(scope="module")
def result():
    return u.exact_checks()


def test_actual_descent_action_and_nonvacuous_anomalies(result):
    assert result["metric_equals_prior_Cartan_inverse"]
    assert result["weak_doublets"] == 4
    assert all(value == 0 for value in result["trace_anomalies"].values())
    assert any(result["nonvacuous_color_cubic_block_traces"])
    assert len(result["derived_multiplets"]) == 6


def test_preserved_witness_nonunique_full_centralizer_and_explicit_transport(result):
    assert result["distinct_normalized_histogram_hits"] == 2
    assert result["Weyl_transports_R4_grading_to_D2_and_preserves_cubic"]
