import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/cone_exact.py'
spec=importlib.util.spec_from_file_location('r72_cone_exact',p)
C=importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)

def test_actual_changing_operator_has_conserved_Green_current():
    out=C.actual_controls()
    assert out['form_dimension']==72 and all(out['checks'].values())

def test_contraction_constants_inject_both_exact_solution_spaces():
    out=C.contraction_controls()
    assert out['slow_space_dimension']==54 and out['fast_space_dimension']==18
    assert out['contraction']==C.s.Rational(1,7) and all(out['checks'].values())

def test_actual_tail_bound_has_positive_and_unsafe_controls():
    out=C.tail_controls()
    assert out['exact_comparator_tail']==2**20
    assert all(out['checks'].values())

def test_witnessed_quotient_rank_is_not_particle_count():
    out=C.geometry_controls()
    assert out['witnessed_quotient_dimension']==36 and out['radical_dimension']==18
    assert out['witnessed_signature']==[18,18] and all(out['checks'].values())

def test_fast_graph_cutoff_and_slow_L2_are_different():
    assert all(C.norm_controls()['checks'].values())

def test_exact_rotated_fixture_preserves_current_not_frozen_slots():
    assert all(C.rotated_controls()['checks'].values())

def test_Q_cancellation_does_not_admit_separate_d_and_delta():
    assert all(C.split_controls()['checks'].values())

def test_all_frozen_exact_controls():
    out=C.run()
    assert set(out['groups'])=={'actual','contraction','tail','geometry','norm','rotated','split'}
    assert out['all_checks_pass']
