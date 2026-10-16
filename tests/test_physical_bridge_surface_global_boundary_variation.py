"""LIVE actual global-tube source boundary variation and destructive controls."""
# BANKED IDENTITY: both producers execute. PRIOR ART: packet DESIGN.
import json
import os
from pathlib import Path
import subprocess
import sys
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_global_boundary_variation_2026_10_16'

@pytest.fixture(scope='module')
def cert():
    values=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout
        values.append(json.loads(p.stdout))
    assert values[0]==values[1] and values[0]['all_passed']
    return values[0]

def check(cert,*names):
    for name in names:
        assert cert['checks'][name]

def test_fresh_actual_source_geometry_and_interface_records(cert):
    for folder,count in [('surface_arena_boundary_2026_10_16',44),('surface_curved_boson_2026_10_16',53),('surface_same_action_transmission_2026_10_16',144)]:
        check(cert,'fresh complete antecedent '+folder)
        assert len(cert['records'][folder]['checks'])==count
        assert cert['records'][folder]['all_passed']

def test_actual_variable_normal_density_and_current(cert):
    check(cert,'actual coframe inverse in both orders and oriented volume',
        'full variable normal retains horizontal geometry and radius gradient',
        'normal norm has nonzero positive vertical contribution',
        'vertical normal approximation rejected even at fixed radius',
        'actual CR form pulled back with the full normal',
        'induced density agrees with actual graph metric determinant',
        'coarea and oriented flux retain every horizontal term',
        'wrong vertical scalar current and same-normal joining are detected')

def test_nonlinear_source_momenta_not_rough_energy(cert):
    check(cert,'normal symbol derived from all actual seven residuals',
        'all-normal rank-five symbol and only normal-gauge kernel',
        'actual nonlinear residual momenta from full first variation',
        'wrong source factor and discarded derivative term are detected',
        'source momentum is tangential in gauge slots',
        'commutator retained rather than dropped from actual source momentum',
        'rough Yang Mills momentum is not the source momentum')

def test_end_functional_variation_retains_corners_and_nonflat_data(cert):
    check(cert,'actual CS first variation retains the corner derivative',
        'deleting the CS corner term is detected',
        'flat pure gauge CS cubic is nonzero and has the correct coefficient',
        'full nonlinear scalar end flux and derivative variations retained',
        'both endpoint primitive signs are required')
    assert cert['records']['end_primitive']['caps_corners_and_patch_descent_required']
    assert not cert['records']['end_primitive']['quantum_level_derived']

def test_gauge_covariance_and_natural_boson_scope(cert):
    check(cert,'zero residual gives natural momenta without Dirichlet values',
        'full nonlinear boundary pairing gauge covariance before interpretation')
    assert not cert['records']['meaning']['global_stationary_SM_phase_derived']

def test_actual_real_fermion_pairing_requires_a_domain(cert):
    check(cert,'actual full source Clifford and symmetric Majorana normal pairing',
        'full source real normal map retains both conjugate blocks',
        'both intrinsic half planes are real Green null but unselected',
        'unrestricted fermion pairing nondegenerate not a half-rank condition')
    assert not cert['records']['fermion_trace']['old_pointwise_principal_failure_repaired']
    assert not cert['records']['meaning']['true_end_state_selected']
    assert not cert['records']['meaning']['full_raw_curved_superfield_completion_derived']
