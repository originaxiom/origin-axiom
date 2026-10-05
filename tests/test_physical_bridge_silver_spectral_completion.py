"""LIVE exact cone, spectrum, symbol and nonlinear opposite controls."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_spectral_completion_2026_10_05'


@pytest.fixture(scope='module')
def native():
    spec=importlib.util.spec_from_file_location('spectral_completion_tests',BASE/'probe.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


def test_boundary_dimensions_recomputed(native):
    rows=native.charged()['charged']['1']
    assert [rows[k]['boundary_H0'] for k in ('W','F')]==[2,3]
    assert [rows[k]['boundary_H1'] for k in ('W','F')]==[4,6]


def test_received_full_cones_not_just_H1(native):
    rows=native.charged()['charged']['1']
    assert rows['W']['natural']['E']['H']==[0,2,2,0]
    assert rows['F']['natural']['E']['H']==[0,3,4,0]
    assert rows['F']['natural']['dual']['H']==[0,4,3,0]


def test_all_dimensions_and_full_dual_pairing(native):
    for amp in native.charged()['charged'].values():
        for row in amp.values():
            for ell,result in enumerate(row['spectra']):
                assert result['E']['H']==result['dual']['H'][::-1]
                assert result['E']['J']==ell-row['boundary_H0']
                assert result['E']['H'][0]==result['E']['H'][3]==0


def test_anomaly_census_not_target_fit(native):
    rows=native.charged()['census'];assert len(rows)==35
    good=[r for r in rows if r['conditional_SU5_cubic']==0]
    assert [(r['ellW'],r['ellF']) for r in good]==[(i,i+1) for i in range(5)]
    assert [r['JW'] for r in good]==[-2,-1,0,1,2]


def test_split_control_same_index_for_same_dimensions(native):
    rows=native.charged()['charged']
    for k in ('W','F'):
        assert rows['0'][k]['natural']['E']['J']==0
        assert [r['E']['J'] for r in rows['0'][k]['spectra']]==[r['E']['J'] for r in rows['1'][k]['spectra']]


def test_neutral_full_degrees_preserved(native):
    for row in native.charged()['neutral_native_only'].values():
        assert row['H']==row['H'][::-1] and row['J']==0
    assert native.analytic_controls()['gauge_endpoint_H_per_coefficient']==[1,0,0,1]


def test_universal_exact_block_and_wrong_preimage(native):
    out=native.analytic_controls()
    assert out['checks']['high_symbol_universal']
    assert out['checks']['primitive_omission_nonelliptic']
    assert out['checks']['high_maximal_green'] and out['checks']['high_reality']


def test_auxiliary_derivative_and_nonlinear_obstruction(native):
    out=native.analytic_controls()['checks']
    assert out['exact_auxiliary_derivative_admitted']
    assert out['nonlinear_gauge_control_detected']
    assert out['bulk_interaction_not_deleted']


def test_rref_field_not_rational_nullspace(native):
    m=s.Matrix([[1,s.sqrt(2),0]])
    k=native.kernel(m)
    assert k==s.Matrix([[-s.sqrt(2),0],[1,0],[0,1]])
    assert native.zero(native.mul(m,k)) and k.cols==2


def test_gauge_endpoints_from_actual_marked_cone(native):
    out=native.analytic_controls()['gauge_cone']
    assert out['H']==[1,0,0,1] and out['J']==0
    assert out['dimensions']==[2,5,4,1] and out['ranks']==[1,4,0]


def test_live_results_and_nonclaims(native):
    out=native.run();assert out['passed']==len(out['checks']) and out['failed']==[]
    for k in ('nonlinear_physical_domain_closed','genesis_polarization_selected',
              'numerical_PDE_kernel_solved','physical_goal_achieved','non_author_acceptance'):
        assert out[k] is False
