"""R94 live mathematics; the complete physical goal is not a test fixture."""
import importlib.util
from pathlib import Path
import sympy as sp

PATH=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/register_action.py'
spec=importlib.util.spec_from_file_location('r94_register_action',PATH)
native=importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)


def test_every_primitive_move_preserves_leaf_and_transports_all_poisson_components():
    values=native.checks()
    for name in ('L','R','P','Li','Ri','T','Ti'):
        assert values[name+'_preserves_K']
        for suffix in ('01','12','20'):assert values[name+'_poisson_'+suffix]


def test_contravariant_word_order_and_literal_inverse_maps():
    values=native.checks()
    for name in ('L','R','T','P'):assert values[name+'_inverse']
    assert values['contravariant_LP_halfstep']
    assert values['contravariant_LR_square']
    assert values['swap_conjugates_shears']


def test_orientation_register_transport_and_unsafe_scalar_form_quotient():
    values=native.checks()
    assert values['nonzero_sheet_coefficient_is_odd']
    assert values['constant_nonzero_coefficient_rejected']
    assert values['unflipped_halfstep_rejected']
    for name in ('L','R','P','Li','Ri','T','Ti'):assert values[name+'_tracked_form']


def test_actual_parabolic_darboux_chart_not_abelian_linearization():
    r,b,coordinates,K,area=native.chart()
    assert K==0
    assert sp.cancel(area-1/(r*b))==0
    assert native.checks()['wrong_abelian_leaf_rejected']


def test_regular_generating_form_derivatives_and_reject_wrong_sign():
    g=native.generating();normal=g['normal']
    assert normal(g['pQ']-g['cross'])==0
    assert normal(g['Pq']-g['cross'])==0
    assert normal(g['pQ']+g['Pq'])!=0
    assert normal(g['cross'])!=0


def test_all_three_nonlinear_coordinates_and_branch_custody():
    g=native.generating()
    for i in range(3):assert g['normal'](g['new'][i]-g['target'][i])==0
    assert native.checks()['old_y_matched_branch']
    assert native.checks()['opposite_sqrt_changes_old_point']


def test_signed_first_variation_matches_momenta_not_their_sum():
    values=native.checks()
    assert values['signed_DEL_matches_momenta']
    assert values['untracked_DEL_rejected']
    assert values['wrong_generating_sign_rejected']


def test_nonreal_monodromy_orbit_regular_chart_and_floquet_not_singular_origin():
    values=native.checks()
    for j in range(2):
        for suffix in ('leaf','half_exchange','square_fixed','regular','chart_discriminant','Floquet'):
            assert values['geometric_'+str(j)+'_'+suffix]
    assert values['singular_origin_rejected']
