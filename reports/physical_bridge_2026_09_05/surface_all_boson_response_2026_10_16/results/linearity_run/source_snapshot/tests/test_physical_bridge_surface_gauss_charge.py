"""LIVE actual source Gauss current, nilpotent response and both endpoints."""
# BANKED IDENTITY: fixtures rerun both actual source/root replay methods.
# PRIOR ART: reverse_susy live tests; no other-parent mass/count import.
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_gauss_charge_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    data=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout;data.append(json.loads(p.stdout))
    return data
def test_actual_source_kinetic_Gauss_factor_and_retained_primitives(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
    for k in ('actual positive time and every source spatial action coefficient','actual temporal multiplier couples with positive Majorana half',
              'actual K time sector equals canonical kinetic plus explicit divergence','actual K Gauss Euler coefficient factor four',
              'actual external vector temporal sector and common internal weight','actual auxiliaries have no hidden temporal multiplier'):
        assert cert[0]['checks'][k]
def test_complete_real_source_E8_current_not_dimension_matching(cert):
    for k in ('complete248positive compact real frame not small substitute','all16source real derivative and velocity factors',
              'every compact E8 generator has nonzero real antisymmetric adjoint','faithful actual E8 triplet metric reality and all generators'):
        assert cert[0]['checks'][k]
    assert len(cert[0]['records']['full_real_current']['all248real_adjoint_matrices'])==248
def test_all_currents_and_genuine_odd_charge(cert):
    for k in ('complete actual amplitude fermion replay and zero Dirac residual','nonzero full Gauss current exact Cartan profile',
              'graded canonical fermion contraction gives minus charge variation','Majorana doubling and commuting trace detector rejected'):
        assert cert[0]['checks'][k]
    for n in range(10):assert cert[0]['checks']['complete Hermitian odd current '+str(n)]
    assert len(cert[0]['records']['family']['all_ten_currents'])==10
def test_actual_degree2_Gauss_response_and_homogeneous_freedom(cert):
    for k in ('actual scalar terms and source factor four in Gauss response','wrong response sign or Gauss normalization rejected',
              'unbackreacted zero temporal field fails full fermionic Gauss','homogeneous freedom and regular outer zero response retained',
              'particular response finite inner but not selected boundary data'):
        assert cert[0]['checks'][k]
def test_source_Noether_charge_and_Green_are_not_confused(cert):
    for k in ('full covariant Green reciprocity source not norm identification','canonical full fermion Gauss charge and local divergence',
              'field dependent gauge parameter subtraction nonzero','both endpoints not an unoriented or boundaryless charge',
              'actual full canonical presymplectic contraction matches corrected charge','omitting real fermion symplectic contribution fails',
              'electric charge is not Wronskian even up to sign'):
        assert cert[0]['checks'][k]
def test_partial_coupled_physics_scope_is_preserved(cert):
    r=cert[0]['records']['meaning'];assert r['fermion_Gauss_source_nonzero'] and r['Gauss_degree2_response']
    assert r['source_normalized_bosonic_momentum']==4 and r['charges_not_norms_or_particle_counts']
    assert not r['all_other_boson_equations_solved'] and not r['full_nonlinear_boundary_law_selected']
    assert not r['complete_physical_SM_three_gravity'] and not r['c_number_vacuum_charge_predicted']
