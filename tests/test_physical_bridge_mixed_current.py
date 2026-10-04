"""R91 live mathematical checks, not physical generation or receipt-string locks."""
from pathlib import Path
import importlib.util
import sympy as s

PATH=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/mixed_current.py'
spec=importlib.util.spec_from_file_location('pb_r91',PATH)
M=importlib.util.module_from_spec(spec); spec.loader.exec_module(M)


def test_actual_E8_embedding_and_complete_weight_roster():
    data=M.geometry()
    assert data['checks']['whole_248_branching']
    assert data['checks']['wrong_bars_rejected_at_equal_dimension']
    assert data['checks']['omitted_Cartans_rejected']
    assert data['color_weak_commutant_dimension']==35


def test_frame_map_is_full_Weyl_transport_not_partial_relabel():
    checks=M.geometry()['checks']
    for name in ('reflection_bijects_E8','reflection_fixes_color_weak','actual_Y_transport',
                 'matrix_root_transport','every_root_charge_transports','partial_relabel_rejected'):
        assert checks[name],name


def test_full_mixed_current_and_all_three_projectors():
    cs=M.fixture(); current=sum((M.bracket(c,c.T) for c in cs),s.zeros(6))
    assert current==s.diag(3,-1,-1,-1,0,0)
    for k,expected in ((1,12),(2,8),(3,4)):
        xi=s.diag(*([4-k]*k+[-k]*(4-k)+[0,0]))
        assert s.trace(xi*current)==expected


def test_zero_gauge_moment_does_not_imply_unbroken_gauge():
    cs=M.fixture(); y=s.diag(1,1,1,1,1,-5); yp=s.diag(1,1,1,1,-5,1)
    current=sum((M.bracket(c,c.T) for c in cs),s.zeros(6))
    assert s.trace(y*current)==0
    assert sum(M.norm(M.bracket(y,c)) for c in cs)==216
    assert all(M.bracket(yp,c)==s.zeros(6) for c in cs)


def test_curvature_and_real_residual_not_dropped():
    data=M.current()
    assert data['checks']['all_curvatures_retained']
    assert data['checks']['real_residual_retained']
    assert data['checks']['same_action_potential']


def test_entire_unbroken_algebra_not_only_SM_subset():
    cs=M.fixture(); closure=M.lie_closure(cs+[c.T for c in cs])
    assert len(closure)==24
    assert M.geometry()['fixture_unbroken_algebra_dimension']==24
    assert M.geometry()['full_A5_unbroken_dimension']==11


def test_complex_off_diagonal_current_retained():
    c=M.unit(0,1)+s.I*M.unit(5,0)+2*M.unit(0,5)+M.unit(1,5)
    assert M.block_current(c)==M.bracket(c,c.conjugate().T)
    assert M.block_current(c)[:5,5:]!=s.zeros(5,1)


def test_nonzero_scaling_variation_and_opposite_zero_residual_control():
    a=s.symbols('a',real=True); cs=[a*c for c in M.fixture()]
    j=sum((M.bracket(c,c.T) for c in cs),s.zeros(6))
    fs=[M.bracket(cs[i],cs[k]) for i,k in ((0,1),(0,2),(1,2))]
    v=2*(sum(M.norm(f) for f in fs)+M.norm(j/2))
    assert s.expand(v)==18*a**4 and s.diff(v,a)==72*a**3
    diagonal=s.diag(1,1,1,1,1,-5)
    assert M.bracket(diagonal,diagonal.conjugate().T)==s.zeros(6)
