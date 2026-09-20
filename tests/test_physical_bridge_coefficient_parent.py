"""R40 exact sealed producer controls; not a physical spectrum certificate."""
import json
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'reports/physical_bridge_2026_09_05/coefficient_parent.py'


@pytest.fixture(scope='module')
def data():
    sage = shutil.which('sage')
    if sage is None:
        pytest.skip('Sage exact number-field runtime required')
    completed = subprocess.run([sage, '-python', '-u', str(SOURCE)], cwd=ROOT,
                               text=True, capture_output=True, timeout=600, check=False)
    assert completed.returncode == 0, completed.stdout+'\n'+completed.stderr
    rows = [json.loads(line) for line in completed.stdout.splitlines() if line.startswith('{')]
    return {row['part']: row['result'] for row in rows}


def test_actual_coefficient_not_literal_SL4_but_preserved_in_SL5(data):
    d = data['coefficient_map']
    assert d['nontrivial_det'] and d['det_character'] and d['line_is_chi2']
    assert d['detW'] == {'a': 1, 'b': 1}
    assert d['exact_original_block'] and d['wrong_line_fails']
    assert d['relator'] and d['peripheral_blocks']
    assert d['retained_nonsplit'] and d['complement_ranks'][1] > d['complement_ranks'][0]


def test_all_scalar_repairs_are_checked_and_do_not_preserve_index(data):
    rows = data['scalar_repairs']
    assert len(rows) == 8
    assert len({(str(r['delta']['a']), str(r['delta']['b'])) for r in rows}) == 8
    assert all(r['determinants'] == [1, 1] and r['index'] == 0 for r in rows)
    assert sum(r['cusp_character'] == [1, 1] for r in rows) == 2
    assert all(r['V']['t1'] == 0 for r in rows if r['cusp_character'] != [1, 1])


def test_explicit_clebsch_gordan_intertwines_actual_generators(data):
    d = data['clebsch_gordan']
    assert d['determinant'] != 0 and d['singlet_dimension'] == 1
    assert d['actual_generator_equations'] == {'a': True, 'b': True}


def test_whole_parent_weights_not_dimension_coincidence(data):
    d = data['whole_parent']
    assert (d['root_count'], d['total'], d['wrong_bars_dimension']) == (240, 248, 248)
    assert d['correct_cartans'] and d['orthogonal'] and d['actual_simple_roots']
    assert d['all_joint_weights'] and d['wrong_bars_rejected']
    assert d['lattice_integral'] and d['lattice_index'] == d['euclidean_index'] == 5


def test_center_kernel_and_separate_factor_faithfulness(data):
    d = data['whole_parent']
    assert d['center_kernel'] == [[j, (-2*j) % 5] for j in range(5)]
    assert d['kernel_expected'] and d['separate_factor_injective']


@pytest.mark.parametrize('name', ['trivial', 'V', 'L', 'W', 'wedgeV', 'VL',
                                'wedgeW', 'VLinv', 'End0V', 'End0W', 'chi2Sym4'])
def test_every_parent_sector_keeps_full_cohomology_and_dual_checks(data, name):
    d = data['sector_'+name]
    assert all(d['identities'].values())
    assert d['index'] == d['V']['n']-d['dual']['n']
    for side in ('V', 'dual'):
        r = d[side]
        assert all(r['checks'].values())
        assert r['n'] == r['a1']-r['r1'] >= 0
        assert r['a0']-r['a1']+r['a2'] == 0


def test_original_positive_and_enlargement_do_not_semisimplify_it(data):
    assert data['sector_V']['index'] == data['sector_W']['index'] == 1
    assert (data['sector_V']['V']['n'], data['sector_V']['dual']['n']) == (1, 0)
    assert data['sector_L']['index'] == 0
    assert data['sector_VL']['index'] == 0
    assert data['sector_VLinv']['index'] == -1


def test_all_direct_sum_counts_not_only_indices_agree(data):
    assert data['direct_sum_checks'] == dict(W=True, wedgeW=True, wedgeV=True, End0W=True)


def test_anomaly_instrument_has_both_outcomes_without_fitting_roster(data):
    d = data['conditional_anomalies']
    assert d['quadratic_identity'] and d['cubic_identity'] and d['conjugate_cubic_sign']
    assert d['anomaly_free_control'] and d['anomalous_control']
    i = d['indices']
    assert d['SU5_cubic'] == i['W']-i['wedgeW']
    assert d['SU5_squared_U1'] == 3*(i['V']-4*i['L'])+2*i['wedgeV']-3*i['VL']
    assert d['gravity_squared_U1'] == 10*(i['V']-4*i['L'])+5*(2*i['wedgeV']-3*i['VL'])+5*i['VLinv']
    assert d['U1_cubic'] == 10*(i['V']-64*i['L'])+5*(8*i['wedgeV']-27*i['VL'])+125*i['VLinv']


def test_metric_and_current_map_is_positive_and_equivariant(data):
    d = data['metric_and_current']
    assert d['det_metric'] == 1 and all(v > 0 for v in d['positive_principal_minors'])
    assert d['metric_equivariance'] and d['group_homomorphism'] and d['bracket_map']
    assert d['dagger_map'] and d['current_trace_zero']
    assert d['identity_source_image'] == [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],
                                         [0,0,0,1,0],[0,0,0,0,-4]]
    assert data['whole_parent']['trace_factor_60']
