"""LIVE R93 algebraic locks; analytic/physical completion is not inferred."""
import importlib.util
from pathlib import Path
import sympy as s

path=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/joined_wilson.py'
spec=importlib.util.spec_from_file_location('pb_r93',path)
M=importlib.util.module_from_spec(spec); spec.loader.exec_module(M)


def test_primitive_character_on_the_actual_join_not_a_seam_spurion():
    data=M.character()
    assert data['b1']==1 and all(data['checks'].values())
    assert M.exponent('zc')==0 and M.exponent('z')==1
    assert M.exponent('zc',dict(M.PERIOD,c=0))==1


def test_full_E8_root_roster_not_only_a_dimension():
    data=M.geometry()
    assert data['checks']['full_248_roster']
    assert data['checks']['equal_dimension_wrong_bars_rejected']
    assert data['checks']['omitted_Cartans_rejected']


def test_SM_centralizer_and_two_opposite_holonomy_controls():
    assert M.centralizer_dimension([v%7 for v in M.Y])==12
    assert M.centralizer_dimension([v%5 for v in M.Y])==24
    assert M.centralizer_dimension([-2,-1,0,1,2])==4
    assert M.centralizer_dimension([0]*5)!=12


def test_all_248_trace_includes_mixed_sectors():
    y=M.Y+(0,0,0)
    value=sum((M.dot(r,y)//2)**2 for r in M.roots())
    assert value==1800 and value!=sum(v*v for v in M.Y)


def test_connected_global_kernel_has_all_six_elements():
    data=M.global_kernel()
    assert data['kernel']==[(k,k%3,k%2) for k in range(6)]
    assert all(data['checks'].values())


def test_existing_commuting_field_residuals_and_wrong_field_opposites():
    data=M.action_controls()
    assert data['checks']['commuting_Wilson_curvature_additivity']
    assert data['checks']['commuting_Wilson_moment_additivity']
    assert data['checks']['noncommuting_opposite_has_moment']
    assert data['checks']['nonclosed_omega_opposite_has_curvature']


def test_odd_alternating_invariant_argument_keeps_its_rank_hypothesis():
    r=s.diag(2,3); t=s.Matrix([[0,1],[-1,0]]); chi=s.Rational(1,6)
    assert chi*r*t*r.T==t and (chi*r)*t==t*r.inv().T
    assert (r/chi)*t!=t*r.inv().T
    assert s.Matrix([[0,1],[-1,0]]).det()==1
    skew=s.zeros(5)
    for i in range(5):
        for j in range(i):
            skew[i,j]=i+j+1; skew[j,i]=-skew[i,j]
    assert skew.det()==0
    assert (s.eye(1)-s.eye(1)).nullspace()


def test_actual_three_join_coefficients_are_recomputed_full_algebra():
    for ab in M.N.CHARS:
        row=M.N.case(ab)
        assert row['algebra_dimension']==25
        assert all(row['checks'].values())


def test_charged_branching_and_extra_adjoint_profile_cost():
    data=M.geometry()
    assert data['checks']['ten_SM_weights'] and data['checks']['barfive_SM_weights']
    assert data['adjoint_one_form_complex_profiles']==12
    assert data['cartan_Wilson_coordinates_at_least']==4


def test_finite_premises_pass_without_claiming_generated_physics():
    data=M.evaluate()
    assert all(data['checks'].values())
    for name in ('physical_goal_achieved','generated_SM_selection','physical_chirality_derived',
                 'non_author_acceptance','quantum_moduli_lifting_computed'):
        assert data[name] is False
