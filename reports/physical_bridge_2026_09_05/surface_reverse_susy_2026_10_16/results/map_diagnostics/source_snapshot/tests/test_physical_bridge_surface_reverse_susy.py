"""LIVE source supersymmetry and the amplitude phase boundary pair."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_reverse_susy_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    data=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout;data.append(json.loads(p.stdout))
    return data
def test_live_actual_source_and_Noether_map(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
    for k in ('single earned Noether parameter map all ten actual bosons','actual Noether factor and full real parameter subspace',
              'actual positive time and all spatial source action signs','all actual boson maps have graded rather than commuting reality'):
        assert cert[0]['checks'][k]
def test_complete_parameter_frame_and_Ward_coefficients(cert):
    for k in ('named scalar supercharge is actual source lambda by its full map','complete normalized real four parameter source frame',
              'every independent curvature coefficient in local Euler Ward identity','real parameter complex structure not species count'):
        assert cert[0]['checks'][k]
def test_actual_E8_background_and_complete_field_images(cert):
    for k in ('actual normalized E8 root map all generators metric parity reality','same exact full noncommuting BPS background',
              'complete actual amplitude fermion solves Dirac equation','every reverse image equals amplitude plus phase not rank matching'):
        assert cert[0]['checks'][k]
    for label in ('amplitude','phase'):
        assert cert[0]['checks']['complete BPS and covariant gauge tangent '+label]
        assert cert[0]['checks']['actual full linearized boson Euler '+label]
def test_gauge_partner_and_its_both_end_data(cert):
    for k in ('entire phase partner equals actual covariant gauge variation','phase gauge parameter covariantly harmonic including scalar terms',
              'gauge parameter nonzero at both ends not proper redundancy','actual covariant Green flux equals full gauge direction norm',
              'both oriented endpoints and no discarded outer norm'):
        assert cert[0]['checks'][k]
    r=cert[0]['records']['meaning'];assert not r['phase_is_proper_gauge'] and r['larger_quotient_is_a_different_ensemble']
def test_discriminating_controls_and_norm_scope(cert):
    for k in ('wrong Noether factor and missing odd reversal rejected','wrong normal BPS curvature sign fails annihilation',
              'omitting tangent connection fails true linearized equations','dropping scalar gauge Laplace terms rejected',
              'normalizable near inner end not a claim across outer pole','positive finite local coefficient norm and orthogonal equal partner'):
        assert cert[0]['checks'][k]
def test_not_complete_physics_or_a_particle_count(cert):
    r=cert[0]['records']['meaning'];assert r['real_bosonic_profile_span']==2 and r['all_real_supercharge_parameters']==4
    assert r['not_physical_generations'] and not r['complete_physical_boundary_law'] and not r['full_physical_SM_three_gravity']
