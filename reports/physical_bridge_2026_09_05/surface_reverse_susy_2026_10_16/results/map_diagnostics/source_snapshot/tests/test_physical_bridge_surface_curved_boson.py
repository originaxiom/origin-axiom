"""Live curved residual/field-space boundary audit, no physical count assertion."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_curved_boson_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    out=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1200)
        assert p.returncode==0,p.stderr+p.stdout
        out.append(json.loads(p.stdout))
    return out
def test_both_complete_curved_bosonic_calculations(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
def test_actual_metric_gaussian_and_normalization(cert):
    c=cert[0]['checks']
    for k in ('actual Chern curvature and scalar relation','actual Kahler form closed in full frame',
        'actual chiral metric gives field space symplectic coefficient','unit anti hol volume wedge hol volume is real volume',
        'actual transformed auxiliary metrics and inverse factors','positive Gaussian elimination not a chosen potential',
        'D Gaussian gives necessary whole vector boundary moment',
        'actual Gaussian potential equals complete squares','wrong superpotential normalization changes actual potential'):assert c[k],k
def test_full_curved_energy_and_required_variational_terms(cert):
    c=cert[0]['checks']
    for k in ('universal full curved current including frame gauge and line','complete curved bosonic identity all ordered words',
        'omitted frame divergence detected','omitted line curvature detected','omitted gauge curvature detected',
        'omitted gauge Pontryagin term detected','omitted end current detected','omitted scalar quartic detected',
        'curvature coefficient is scalar R times P norm quarter',
        'first variation retains curvature topology and both end primitive',
        'independent noncommuting coordinate energy identity','coordinate detector sees curvature topology and end',
        'positive full potential despite negative isolated curvature'):assert c[k],k
    for i in range(4):
        for j in range(i+1,4):assert c['actual matrix gauge line second jet '+str((i,j))]
def test_standard_transgression_and_superpotential_boundary(cert):
    c=cert[0]['checks']
    for k in ('graded form differential squared zero','standard gauge Chern Weil transgression retained',
        'standard gauge Pontryagin first variation has boundary',
        'global superpotential variation keeps full normal primitive','dropping superpotential boundary primitive detected'):assert c[k],k
def test_field_space_moment_not_physical_time_charge(cert):
    c=cert[0]['checks']
    for k in ('field space affine moment with retained boundary','bulk moment alone fails for boundary valued parameters',
        'field space Higgs moment coefficient from same metric','wrong metric changes Hamiltonian moment',
        'moment matches actual Hermitian D source pairing','field space boundary cocycle sign and coefficient',
        'bulk gauge moment bracket cancels','boundary cocycle skew is exact derivative',
        'boundary cocycle Jacobi is exact derivative','local commuting circle cocycle nonzero',
        'both annulus ends cancel common traces','one end cutoff witness keeps opposite orientation'):assert c[k],k
def test_matrix_auxiliary_boundary_jets_keep_nonlinearity(cert):
    c=cert[0]['checks']
    for k in ('matrix normal auxiliary linearization derived before trace',
        'linearized normal compatibility keeps connection Higgs term','matrix source is not replaced by its zero trace',
        'whole auxiliary zero needs moment beyond tangent value','whole tangent auxiliary zero needs normal Higgs derivative',
        'coupled normal BPS boundary jets pass','dropping nonabelian moment prevents coupled normal boundary'):assert c[k],k
