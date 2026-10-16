"""LIVE actual interacting source identities; no uncomputed physical index."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_interacting_transport_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    data=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout;data.append(json.loads(p.stdout))
    return data
def test_complete_actual_source_and_both_computations(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
    for k in ('actual source all nine Clifford coefficients and Hermiticity','actual complementary MW isometry and Majorana map',
        'all actual source velocities intertwine complementary MW','critical sign map is explicit not old label matching',
        'full graph to source coefficients retain scalar coordinates'):assert cert[0]['checks'][k],k
def test_actual_dressed_singular_source_not_undressed_free_domain(cert):
    c=cert[0]['checks']
    for r in (1,-1):
        for g in (1,-1):
            for name in ('P','Q'):assert c['actual MW generic dressed cancellation '+str((r,g,name))]
    for r in (1,-1):
        for b in (1,-1):
            assert c['critical coupled indicial sector '+str((r,b))]
            assert c['actual bounded or log dressed first jet '+str((r,b))]
def test_actual_E8_nonnormal_background_and_scalar_normalization(cert):
    for k in ('actual E8 charges integral before parity','actual full coefficient metric positive and parity complete',
        'actual E8 adjoint root is faithful noncommuting SL2','compact adjoint metric not naive identity',
        'actual root Yukawa flips gauge parity and keeps compact reality',
        'canonical root background balances full moment not commuting mass','same background holomorphic equation and scalar normalization',
        'halving real scalar but not backreaction fails'):assert cert[0]['checks'][k],k
def test_complete_angular_connection_monodromy_and_coupled_current(cert):
    for k in ('scalar rotating frame keeps both physical Higgs vertices','rotating frame angular connection is retained',
        'rotating frame monodromy is not deleted','all quarter shifted angular lattices match transition',
        'coupled root sectors close without angular truncation','radial interacting current conserved in actual metric',
        'full radial change keeps Higgs gauge and horizontal terms'):assert cert[0]['checks'][k],k
    assert cert[0]['records']['radial']['finite_radius_full_response_computed'] is False
    assert cert[0]['records']['radial']['global_boundary_domain_proved'] is False
def test_same_source_local_supersymmetric_interacting_tangent(cert):
    for k in ('actual scalar supercharge real and nonzero','all16 ordered BPS tangent coefficients in actual MW',
        'source BPS tangent preserves full reality and positive norm','actual scalar tangent enters plus critical source plane',
        'full nonlinear parameter tangent residual vanishes','actual connection tangent is gauge fixed and retained'):assert cert[0]['checks'][k],k
def test_interacting_horizontal_domain_symmetry_not_free_gap_transfer(cert):
    for k in ('horizontal symbol anticommutes full interacting coefficients',
        'horizontal symbol preserves both dressed leading trace planes','horizontal symmetry respects polar and rotating frames',
        'wrong horizontal scalar shortcut fails trace preservation'):assert cert[0]['checks'][k],k
