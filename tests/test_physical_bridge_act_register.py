"""Mathematical assertions, not consciousness or physical-observer claims."""
import importlib.util
from itertools import product
from pathlib import Path

import pytest

BASE=Path(__file__).resolve().parents[1]/"reports/physical_bridge_2026_09_05"


def load(name):
    spec=importlib.util.spec_from_file_location(name,BASE/(name+".py"))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


N=load("act_register_control")
E=load("act_register_exhaustive")


def test_safe_and_unsafe_record_controls():
    checks=N.record_controls()["checks"]
    assert all(checks.values())
    assert N.descended_update((0,0),(0,1))==(0,)
    assert N.descended_update((0,0,1),(0,2,2)) is None


def test_all_declared_finite_quotients_match_independent_existence():
    counts=[0,0]
    for n in range(1,5):
        for q in E.partitions(n):
            for t in product(range(n),repeat=n):
                assert N.descended_update(q,t)==E.possible_descents(q,t,True)
                counts[0]+=1
            for out in product((0,1),repeat=n):
                assert N.descended_output(q,out)==E.possible_descents(q,out,False)
                counts[1]+=1
    assert counts==[3984,290]


def test_coarsest_future_records_against_pair_reachability():
    count=0
    for n in range(1,4):
        for a,b in product(list(product(range(n),repeat=n)),repeat=2):
            for out in product((0,1),repeat=n):
                actual=N.sufficient_record((a,b),out)
                assert actual==E.pair_record((a,b),out)
                assert N.descended_update(actual,a) is not None
                assert N.descended_update(actual,b) is not None
                assert N.descended_output(actual,out) is not None
                count+=1
    assert count==5898


def test_symbol_insertion_is_identical_not_new_mechanism():
    c=N.source_controls()["checks"]
    assert c["original_literal_record_absent"]
    assert c["rewritten_literal_record_present"]
    assert c["rewritten_same_on_record_graph"]
    assert c["original_trace_invariant"]


def test_empty_elimination_does_not_exclude_isolated_component():
    c=N.source_controls()["checks"]
    assert c["global_elimination_empty_with_isolated_point"]
    assert c["isolated_point_full_jacobian_rank"]
    assert c["point_only_opposite_elimination"]
    assert c["actual_old_m2_empty_elimination_retained"]


def test_field_label_correction_retains_nonconjugacy():
    c=N.source_controls()["checks"]
    assert c["perron_fields_one_and_four_equal"]
    assert c["one_and_four_matrix_traces_distinct"]


def test_galois_membership_control_and_separate_integer_controls():
    assert N.source_controls()["checks"]["complex_conjugation_does_not_fix_K"]
    assert all(E.independent_algebra().values())


@pytest.mark.parametrize("q,t",[((),()),((True,),(0,)),((0,2),(0,1)),((0,0),(0,)),((0,),(1,))])
def test_invalid_or_vacuous_state_data_rejected(q,t):
    with pytest.raises(ValueError):
        N.descended_update(q,t)
