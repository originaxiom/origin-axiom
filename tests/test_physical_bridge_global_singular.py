"""R15 mathematical locks; finite controls do not certify a physical singular limit."""
import importlib.util
from pathlib import Path

import pytest


_SOURCE = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/global_singular.py'
_SPEC = importlib.util.spec_from_file_location('physical_bridge_global_singular', _SOURCE)
gs = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(gs)


def test_cutoff_flux_is_nonzero_and_constant_cutoff_is_zero():
    r = gs.parametrix_identities()
    assert r['metric_cutoff_identity'] == '0'
    assert [row['integral'] for row in r['transitions']] == ['2*A', '2*A']
    assert all(row['endpoint_values'] == ['0', '1'] for row in r['transitions'])
    assert all(row['endpoint_derivatives'] == ['0', '0'] for row in r['transitions'])
    assert r['cutoff_constant_integral'] == '0'


def test_scalar_gap_and_geodesic_source_normalization_identities():
    r = gs.parametrix_identities()
    assert r['hardy_identity'] == '0'
    assert r['line_ode'] == '0'
    assert r['line_flux_divided_by_2pi'] == '1'


def test_mean_repair_uses_actual_area_and_leaves_flow_freedom():
    r = gs.parametrix_identities()
    assert r['repaired_mean'] == '0'
    assert r['omitted_repair_mean'] == 'mu'
    assert r['unequal_area_control'] == '-7'
    assert all('flow' in c for c in r['matching_coefficients'])


@pytest.mark.parametrize('k', [1, 2, 3])
def test_cellular_groups_not_just_euler(k):
    r = gs.cellular_pair(k)
    assert r['Q']['betti'] == [1, 2, 1, 0]
    assert r['C']['betti'] == [1, k+1, 0, 0]
    assert r['T']['betti'] == [k, k, 0, 0]
    assert r['E']['betti'] == [2, 2*(k+1), 0, 0]
    assert r['relative_T']['betti'] == [0, k+1, 1, 0]
    assert r['relative_E']['betti'] == [0, 1, k+1, 0]
    assert r['relative_T']['betti'] == r['relative_E']['betti'][::-1]
    assert r['relative_T']['chi'] == -k
    assert r['relative_E']['chi'] == k


def test_three_arcs_resolution_and_height_control():
    small, large = gs.cellular_pair(3), gs.cellular_pair(3, 8, 2)
    for key in ('Q', 'C', 'T', 'E', 'relative_T', 'relative_E', 'boundary_C'):
        assert small[key]['betti'] == large[key]['betti']
        assert small[key]['chi'] == large[key]['chi']
    assert small['C']['cells'] != large['C']['cells']


def test_zero_arc_and_missing_tubes_are_not_the_same_domain():
    r = gs.cellular_pair(0)
    assert r['relative_T']['betti'] == [1, 2, 1, 0]
    assert r['relative_E']['betti'] == [0, 1, 2, 1]
    s = gs.cellular_pair(3)
    assert s['C']['chi'] == s['relative_T']['chi']
    assert s['C']['betti'] != s['relative_T']['betti']
    assert s['C']['betti'][0] == 1
    assert s['relative_T']['betti'][0] == 0
    assert s['relative_T']['betti'][2] == 1


def test_exact_sequence_is_independent_of_endpoint_pairing_but_needs_crossing():
    for v in ((1, 1, 1), (1, 0, 0), (-1, 1, -1)):
        assert gs.excision_prediction(2, v)['tubes'] == [0, 4, 1, 0]
    for invalid in ((), (0, 0, 0), (2, 2, 2)):
        with pytest.raises(ValueError, match='primitive'):
            gs.excision_prediction(2, invalid)


def test_actual_m202_self_cusp_order_three_not_a_swapped_torus():
    r = gs.m202_witness()['manifolds']
    assert r['m202']['b1'] == 2
    assert r['m202']['cusps'] == 2
    assert r['m202']['abelianized_relators'] == [[0, 0]]
    assert len(r['m202']['order_three_self_cusp']) == 2
    assert all(x['fixed_points_per_cusp'] == [3, 3] and x['preserving']
               for x in r['m202']['order_three_self_cusp'])
    assert not r['m004']['order_three_self_cusp']


def test_actual_parent_adjoint_has_two_spinor_orbits_not_a_27():
    r = gs.e6_parent()
    assert r['roots'] == 72 and r['root_lengths'] == ['2']
    assert r['adjoint_charge_dimensions'] == {'-1': 16, '0': 46, '1': 16}
    assert r['zero_roots'] == 40 and r['zero_root_rank'] == 5
    assert r['u_norm'] == '4/3'
    for orbit in r['charged_d5_orbits'].values():
        assert orbit['size'] == 16 and orbit['projected_norms'] == ['5/4']
        assert len(orbit['d5_dominant']) == 1
    assert r['charged_d5_orbits']['1']['d5_dominant'] != r['charged_d5_orbits']['-1']['d5_dominant']
    assert r['zero_u_neutral_dimension'] == 78
    assert sum(r['adjoint_charge_dimensions'].values()) != 27
