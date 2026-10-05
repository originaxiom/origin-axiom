"""LIVE symbol, reality, compensation and opposite controls, not a particle census."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/silver_smooth_boundary_gate_2026_10_05'


@pytest.fixture(scope='module')
def native():
    spec=importlib.util.spec_from_file_location('smooth_silver_gate',BASE/'probe.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def test_all_eight_components_current_and_dimension(native):
    gamma=native.matrices()[2]
    for kind in ('gauge','complement'):
        for sign in (-1,1):
            full=native.domain(kind,sign)[2]
            assert full.shape==(8,4) and full.rank()==4
            assert full.H*gamma*full==s.zeros(4)
    assert gamma.det()!=0


def test_universal_symbol_polynomial_not_finite_sampling(native):
    x,y=s.symbols('x y',real=True)
    for kind in ('gauge','complement'):
        for sign in (-1,1):
            assert s.factor(native.restricted_symbol(kind,sign).det())==-(x*x+y*y)


def test_real_line_current_pass_does_not_imply_ellipticity(native):
    x,y=s.symbols('x y',real=True);gamma=native.matrices()[2]
    for kind,xi in (('gauge',{x:0,y:1}),('complement',{x:1,y:0})):
        full=native.domain(kind,real_line=True)[2]
        assert full.H*gamma*full==s.zeros(4)
        assert native.restricted_symbol(kind,real_line=True).subs(xi).rank()==0


def test_combined_reality_and_parity_are_preserved(native):
    *_,j,p=native.matrices()
    for kind in ('gauge','complement'):
        full=native.domain(kind)[2]
        assert full.row_join(j*full.conjugate()).rank()==4
        assert full.row_join(p*full).rank()==4
        assert full.row_join(full.conjugate()).rank()==6


def test_wrong_complement_leaks_current(native):
    full=native.domain('gauge',wrong_complement=True)[2]
    assert full.H*native.matrices()[2]*full!=s.zeros(4)
    with pytest.raises(ValueError,match='population'):native.domain('charged-only')


def test_gauge_endpoints_and_bulk_cubic_are_not_deleted(native):
    full=native.domain('gauge')[2]
    assert full.row_join(s.eye(8)[:,0]).row_join(s.eye(8)[:,7]).rank()==4
    assert native.bulk_cubic()==1


def test_affine_reference_term_and_common_line(native):
    w=[1,s.I];dw=[2,2*s.I];c0=[3,5]
    assert native.boundary_pair(w,dw)==0
    affine=native.boundary_pair(c0,w)
    assert affine==3*s.I-5 and affine!=0
    assert -affine+native.boundary_pair(c0,w)==0
    assert native.boundary_pair(w,[1,-s.I])!=0


def test_compensation_moves_data_to_vector_not_to_zero(native):
    x,y=s.symbols('x y',real=True);g=native.supergauge(x,y)
    assert g['f_after']==s.zeros(2,1) and g['v_after']!=0
    assert s.simplify(g['z_after']-g['z_before'])==s.zeros(2,1)
    assert -s.I*g['f_after']!=g['z_before']
    assert (g['reject']*g['z_after']).subs({x:1,y:0})!=s.zeros(2,1)


def test_nonzero_fourier_escape_and_constant_comparator(native):
    x,y=s.symbols('x y',real=True)
    for sign in (-1,1):
        g=native.supergauge(x,y,sign)
        assert s.simplify((g['residual'].H*g['residual'])[0])==(x*x+y*y)/2
        assert g['residual'].subs({x:0,y:0})==s.zeros(2,1)
        realgrad=g['reject']*s.Matrix([x,y])
        assert s.simplify((realgrad.H*realgrad)[0])==(x*x+y*y)/2


def test_live_population_and_nonclaims(native):
    result=native.run()
    assert result['checks'] and all(result['checks'].values()) and result['failed']==[]
    assert len(result['profiles'])==4
    assert result['parent']['allowed_dimension']==992
    assert not result['physical_kernel_computed']
    assert not result['full_superfield_domain_closed']
    assert not result['physical_goal_achieved'] and not result['non_author_acceptance']
