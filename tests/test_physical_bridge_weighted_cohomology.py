"""R18: weighted homotopy controls; see the separate maximal-domain proof."""
import importlib.util
from pathlib import Path

import pytest

_SOURCE = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/weighted_cohomology.py'
_SPEC = importlib.util.spec_from_file_location('physical_bridge_weighted_cohomology', _SOURCE)
wc = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(wc)


def test_changed_hilbert_space_conjugacy_and_all_metric_weights():
    r = wc.norm_and_conjugacy()
    assert r['unitary_error'] == '0'
    assert len(r['conjugacy']) == 8 and all(r['conjugacy'])
    assert sum(r['wrong_sign_nonzero']) == 7  # top-degree differential is zero for either sign
    for row in r['rows']:
        assert row['ratio_error'] == row['cusp_error'] == '0'
        assert row['ratio_limits'] == ['1']*4


def test_hardy_kernel_integrals_and_complex_profiles():
    exact = wc.hardy_bounds()
    assert exact['forward'] == exact['backward'] == '0'
    rows = wc.hardy_profiles()
    assert len(rows) == 24 and any(row['log_primitive'] for row in rows)
    assert all(0 < row['normalized_ratio'] < 1+1e-10 for row in rows)
    assert {row['radius'] for row in rows} == {1., .3}


def test_strong_traces_and_weak_nonzero_projection_control():
    rows = wc.constant_trace_rows()
    positive = [row for row in rows if row['a'] in ('1', '2')]
    negative = [row for row in rows if row['a'] in ('-1', '-2')]
    assert all(not row['constant_L2'] and row['forward_bounded'] for row in positive)
    assert all(row['constant_L2'] and row['backward_bounded'] for row in negative)
    weak = next(row for row in rows if row['a'] == '1/2' and row['angular'] == 0)
    assert weak['constant_L2'] and weak['forward_bounded']
    assert weak['p'] == '0'


def test_actual_cusp_radial_margin_in_every_tangential_degree():
    rows = wc.cusp_slope_controls()
    assert len(rows) == 216
    assert {row['j'] for row in rows} == {0, 1, 2}
    assert all(row['alpha'] >= 7-1e-12 and row['margin'] >= -1e-10 for row in rows)
    assert max(row['derivative_error'] for row in rows) < 2e-12


def test_conjugated_volterra_and_wrong_unweighted_control():
    rows = wc.volterra_controls()
    assert len(rows) == 18
    for row in rows:
        for n, value in zip((64, 128), row['scaled_norms']):
            assert value <= 1+3/n
        assert row['refinement_change'] < .05
        assert all(value > 2 for value in row['unweighted_scaled_norms'])


def test_averaged_domain_homotopy_cutoff_and_corner_maps():
    r = wc.homotopy_controls()
    assert r['averaged_identity'] and r['relative_identity'] and r['cutoff_commutes']
    assert r['projection_nonzero'] and r['omitted_projection_fails']
    assert r['omitted_cutoff_term_fails'] and r['cap_preserved']


def test_point_trace_is_not_a_bounded_L2_projection():
    r = wc.homotopy_controls()
    assert r['bump_norm'] == '2/3'
    assert r['bump_point_limit'] == 'oo'
    assert r['bump_integral'] == 'sqrt(epsilon)'


def test_global_chain_parametrix_algebra_not_finite_betti_inference():
    r = wc.parametrix_algebra()
    assert r['chain_nilpotent'] and r['chain_i'] and r['chain_p']
    assert r['original_homotopy'] and r['composed_parametrix']
    assert r['projection_kills_exact'] and r['projection_closed']
    assert r['projection_rank'] == 2
    assert r['omitted_core_homotopy_fails'] and r['projection_is_not_orthogonal']


def test_full_pairs_and_zero_arc_controls_recomputed():
    rows = wc.topology_controls()
    for row in rows[1:]:
        k = row['k']
        assert row['relative_T']['betti'] == [0, k+1, 1, 0]
        assert row['relative_E']['betti'] == [0, 1, k+1, 0]
        assert row['relative_T']['betti'] != row['C']['betti']
    assert rows[0]['relative_T']['betti'] == [1, 2, 1, 0]
    assert rows[0]['relative_E']['betti'] == [0, 1, 2, 1]
    assert rows[3]['C']['cells'] != rows[4]['C']['cells']


def test_amplitude_and_cusp_hypotheses_cannot_be_silently_dropped():
    assert wc.strong_class(1, (1, 1, 1), (3, 3)) == 'relative_T'
    assert wc.strong_class(-2, (.5, 1, 2), (1.5, 3.5)) == 'relative_E'
    for q, beta, totals in ((0, (1,), (1,)), (1, (.5,), (.5,)), (1, (1, -1), (1,)),
                            (1, (1,), (0,)), (1, (), (1,)), (float('inf'), (1,), (1,))):
        with pytest.raises(ValueError):
            wc.strong_class(q, beta, totals)
