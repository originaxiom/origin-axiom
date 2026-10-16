"""LIVE full boson source and deliberately separated boundary criteria."""
# BANKED IDENTITY: fixture replays actual source twice. PRIOR ART: Gauss tests.
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_all_boson_response_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    data=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout;data.append(json.loads(p.stdout))
    assert data[0]==data[1] and data[0]['all_passed'];return data[0]
def test_actual_source_auxiliaries_and_full_curvature(cert):
    for k in ('fresh all39 actual Gauss source antecedents','actual untraced D and all six G source equations','all static raw auxiliary surface terms retained exactly','all seven curvature components derived from source auxiliaries','actual auxiliary elimination equals seven component potential','full curvature calibration is explicit divergence not omission'):assert cert['checks'][k]
def test_full_generic_Hessian_and_external_action(cert):
    for n in range(6):assert cert['checks']['generic source boson Euler '+str(n)]
    for k in ('all six generic Hessians retain actual curvature term','all four actual vector kinetic sectors and boundary primitives','actual external Lorentzian source factor four all directions','actual external quartic retained beyond quadratic response'):assert cert['checks'][k]
def test_all_ten_actual_response_equations(cert):
    for k in ('all freshly computed current coefficients faithfully projected','all ten actual boson Euler equations at fermion degree two','independent polar and Cartesian scalar full operators on response','time and all five spatial source signs independently retained','wrong source signs and normalization fail','all degree two responses have correct odd compact reality','all responses retain actual half winding gauge transition','actual linear Lorenz condition all coefficients'):assert cert['checks'][k]
    assert len(cert['records']['degree2']['all_ten_Euler_residuals'])==10
def test_outer_homogeneous_freedom_and_actual_auxiliary_conditions(cert):
    for k in ('actual Cartan and both dual root harmonic freedoms','outer zero benchmark retains every actual boson equation','outer correction preserves odd compact reality and transition','outer corrected coefficient norm and derivative energy integrable at inner end'):assert cert['checks'][k]
    for st in cert['records']['degree2']['auxiliary_responses']:
        assert cert['checks']['all six auxiliary and D responses '+st]
        assert cert['checks']['actual free normal boson momenta zero at outer '+st]
def test_actual_variational_boundary_tests_are_not_spectrum_claim(cert):
    for k in ('raw auxiliary normal primitives in undifferentiated boundary ideal','raw fermion normal primitives in undifferentiated boundary ideal','actual fermion lies in benchmark isotropic normal trace space'):assert cert['checks'][k]
    assert cert['records']['meaning']['benchmark_variational_tests_passed']
def test_principal_counterexample_and_positive_control_both_retained(cert):
    for sign in ('1','-1'):
        r=cert['records']['boundary']['principal_tests'][sign]
        assert r['rank']==4 and not r['ordinary_angular_transverse'] and r['complement_control_rank']==0
        assert cert['checks']['computed nontransverse angular benchmark sign '+sign]
        assert cert['checks']['transverse complement control sign '+sign]
    m=cert['records']['meaning'];assert m['all_ten_boson_equations_solved_at_degree2']
    assert not m['ordinary_angular_principal_transverse'] and not m['global_kernel_or_Fredholm_verdict']
    assert not m['complete_nonlinear_boundary_law_selected'] and not m['derived_SM_three_chiral_gravity']
