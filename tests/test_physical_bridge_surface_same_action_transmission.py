"""LIVE same-action interface checks; true end selection remains unearned."""
# BANKED IDENTITY: both full producers fresh. PRIOR ART: packet DESIGN.
import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'reports/physical_bridge_2026_09_05/surface_same_action_transmission_2026_10_16'

@pytest.fixture(scope='module')
def cert():
    data = []
    for name in ('probe', 'reference'):
        run = subprocess.run([sys.executable, '-B', str(HERE / (name+'.py'))], cwd=ROOT,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'), capture_output=True, text=True, timeout=1800)
        assert run.returncode == 0, run.stderr + run.stdout
        data.append(json.loads(run.stdout))
    assert data[0] == data[1] and data[0]['all_passed']
    return data[0]

def test_actual_source_and_every_normal_momentum(cert):
    assert cert['checks']['fresh complete80 root and actual source controls']
    assert all(cert['records']['fresh_source_action_checks'].values())
    for n in range(4):
        assert cert['checks']['actual source normal momenta all fields direction '+str(n)]

def test_raw_primitives_are_retained_and_oriented(cert):
    rows = cert['records']['source_interface']['retained_primitives']
    assert rows and {'auxiliary', 'calibration', 'fermion'} <= {r['name'].split('_')[0] for r in rows}
    for row in rows:
        assert row['words'] > 0
        assert cert['checks']['retained primitive cancels only under oriented matching '+row['name']]
    assert not cert['records']['source_interface']['canonical_momentum_substitution_used']

def test_full_real_graph_retains_gauge_multiplet(cert):
    for n in range(4):
        assert cert['checks']['full source Hermitian and Majorana matched graph '+str(n)]
        assert cert['checks']['same normal sign fails full source graph '+str(n)]
    assert cert['checks']['matched graph retains lambda and conjugates without one sided selection']
    assert cert['checks']['actual coefficient pairing is nontrivial positive and real']
    assert cert['checks']['nonunitary matching and deletion of conjugates fail distinct controls']

def test_every_joint_principal_direction_and_zero_sector(cert):
    for name in ('all joint covectors actual principal Clifford identity',
        'complementary two sided Cauchy projectors for every nonzero covector',
        'uniform normalized matching isometry on joint decaying space',
        'same decaying sign gives a nonzero false interface kernel',
        'zero principal covector matched not inverted or deleted',
        'gauge fixed boson and ghost principal transmission determinant'):
        assert cert['checks'][name]

def test_every_charged_block_and_transfer_derivative(cert):
    rows = cert['records']['charged_transfer']['jets']
    assert len(rows) == 28 and {r['highest_weight'] for r in rows} == {0, 1, 2}
    assert {r['computational_sign'] for r in rows} == {-1, 1}
    for row in rows:
        for prefix in ('full charged kernel current identity block ',
            'finite transfer ODE and full current coefficients block ',
            'wrong transfer derivative fails actual ODE block '):
            assert cert['checks'][prefix+str(row['block'])]
    assert not cert['records']['charged_transfer']['charged_global_Cauchy_or_spectrum_computed']

def test_current_parameter_and_frame_compensation(cert):
    for name in ('canonical_charge', 'parameter_correction'):
        assert cert['checks']['opposite source charges cancel only after full matching '+name]
    for name in ('independent gauge parameters retain possible surface charge',
        'existing interacting gauge sector has nonzero bracket and admits constants',
        'tilted normal spin frame and full reality covariant',
        'actual puncture transition preserves metric reality and both side graph',
        'inhomogeneous frame connection necessary for covariant transmission',
        'retained primitive descent and its variation telescope not vanish separately'):
        assert cert['checks'][name]

def test_interface_is_not_an_earned_physical_end_or_SM(cert):
    meaning = cert['records']['meaning']
    for name in ('same_source_two_sided_transmission', 'uniform_joint_principal_interface_transversality',
                 'retains_existing_local_interacting_gauge_sector', 'all_charged_and_kernel_blocks_retained'):
        assert meaning[name]
    for name in ('artificial_cut_changes_kernel_or_index', 'true_boundary_or_exterior_state_selected',
                 'global_stationary_Higgs_derived', 'full_curved_nonlinear_SUSY_boundary_action_verified',
                 'SM_three_parameters_gravity_derived'):
        assert not meaning[name]
