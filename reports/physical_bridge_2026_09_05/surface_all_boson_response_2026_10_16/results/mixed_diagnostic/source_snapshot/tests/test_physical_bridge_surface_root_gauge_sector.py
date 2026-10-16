"""LIVE complete root reduction and retained local interacting gauge sector."""
import json,os,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'reports/physical_bridge_2026_09_05/surface_root_gauge_sector_2026_10_16'
@pytest.fixture(scope='module')
def cert():
    data=[]
    for name in ('probe','reference'):
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True,timeout=1800)
        assert p.returncode==0,p.stderr+p.stdout;data.append(json.loads(p.stdout))
    return data
def test_complete_live_methods_and_actual_parent(cert):
    assert cert[0]==cert[1] and cert[0]['all_passed'] and all(cert[0]['checks'].values())
    assert cert[0]['checks']['same complete actual source dictionary']
def test_full_E8_root_maps_not_dimension_matching(cert):
    for k in ('actual root compact metric and parity data','complete root Casimir polynomial not sampled character',
        'all root Casimir projectors complete and orthogonal','root branching dimensions are coefficient dimensions',
        'actual normalized triplet intertwines every root generator','all actual doublet maps and norms not only dimension match',
        'actual root maps and singlet kernel resolve all248','full coefficient decomposition retains eta and compact conjugation',
        'even and odd root kernels and doublets all retained'):assert cert[0]['checks'][k],k
def test_full_source_spin_and_Lorentz_reconstruction(cert):
    for k in ('computational spin label is Hermitian and complete','spin reduction holds on whole unit horizontal circle',
        'source reconstruction is full16 not one computational sign',
        'external Lorentz mixes computational signs and full radial law retains it',
        'actual root Cartan plus R conserved including both Higgs vertices'):assert cert[0]['checks'][k],k
def test_all_small_radial_matrices_and_current_retained(cert):
    r=cert[0]['records']['blocks'];assert r['directions']==3968 and r['largest_active_size']==4
    assert r['charged_finite_cauchy_response_computed'] is False
    assert {x['computational_sign'] for x in r['list']}=={-1,1}
    for x in r['list']:
        assert x['size'] in (2,4)
        for label in ('indicial','backreaction','yukawa','horizontal','normal_current'):
            assert len(x[label])==x['size'] and all(len(row)==x['size'] for row in x[label])
    assert cert[0]['checks']['all charged and root kernel blocks resolve full3968 coefficients']
def test_complete_compact_nonabelian_gauge_sector(cert):
    for k in ('complete even centralizer basis not a selected commuting subset','centralizer membership criteria act on every basis column',
        'all6241 retained gauge basis brackets close','actual compact nonabelian gauge interaction survives',
        'nonabelian retained pair is actually compact real','retained gauge algebra is real and orthogonal to root background'):assert cert[0]['checks'][k],k
    assert len(cert[0]['records']['root']['even_centralizer_basis'])==79
def test_actual_scalar_supercharge_no_omitted_source_and_boundary_recovery(cert):
    for k in ('actual scalar supercharge is named lambda not equal rank only',
        'all6 untraced internal gauge and Higgs gaugino currents vanish','external gauge and kinetic action preserves real lambda',
        'normal gaugino boundary current zero for every internal normal',
        'free normal response exact on nonzero background kernel',
        'all local nonlinear mixed gauge sources vanish without abelianizing',
        'retained regular gauge and lambda has zero normal response','reduced gauge kinetic volume factor positive not predicted'):assert cert[0]['checks'][k],k
    assert cert[0]['records']['gauge_sector']['gauge_group_selected_as_SM'] is False
