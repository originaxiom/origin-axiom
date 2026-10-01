import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/cross_branch_positives.py'
SPEC=importlib.util.spec_from_file_location('r75_cross',P)
C=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(C)


def test_literal_word_cocycles_recover_all_three_quotient_polynomials():
    out=C.algebra_controls()
    assert len(out['quotients'])==3 and all(out['checks'].values())


def test_double_root_is_jordan_not_merely_a_repeated_characteristic_root():
    out=C.root_controls()
    assert out['nullities']==[[1,2,2,2]]*3
    assert all(out['checks'].values())


def test_nonsplit_index_and_split_control_use_actual_peripheral_restriction():
    out=C.index_controls()
    assert out['index']==-1 and out['split_index']==0
    assert all(out['checks'].values())


def test_hopping_square_has_the_received_mixed_coefficient_and_controls():
    assert all(C.hopping_controls()['checks'].values())


def test_same_nonsplit_coefficient_has_an_explicit_source_balance_duty():
    assert all(C.balance_controls()['checks'].values())


def test_complete_bounded_control_population():
    out=C.run()
    assert out['all_checks_pass'] and out['passed']==out['total']
