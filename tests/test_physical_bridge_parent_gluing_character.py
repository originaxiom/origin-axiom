import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05'
def load(name):
    spec=importlib.util.spec_from_file_location(name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
N=load('parent_gluing_character'); R=load('parent_gluing_character_reference')


def test_complete_parent_weights_and_faithful_factor_not_only_dimension():
    out=N.parent_roots()
    assert out['root_count']==240 and out['total_weights']==248
    assert all(out['checks'].values())


def test_parent_invariant_controls_accept_conjugation_and_reject_false_shortcut():
    assert all(N.fixtures()['checks'].values())
    assert all(R.controls()['checks'].values())


def test_actual_parent_loop_character_is_nonconstant_for_each_join():
    for ab in N.N.CHARS:
        out=N.case(ab)
        assert out['parent_degree'] in (1,2)
        assert out['checks']['parent_separates_one_two']
        assert all(out['checks'].values())


def test_inverse_and_exterior_polynomials_are_derived_not_sample_fitted():
    for ab in N.N.CHARS:
        out=N.case(ab)
        assert out['checks']['both_inverse_quadratic']
        assert out['checks']['exterior_quadratic_coefficients_zero']
        assert [r['t'] for r in out['samples']]==['1','2','3','1/2']
        assert all(v for r in out['samples'] for v in r['checks'].values())


def test_same_author_separate_reference_rederives_all_actual_parent_characters():
    for p,r in R.PRIME_ROOTS:
        assert all(R.root_controls(p)['checks'].values())
        for ab in N.N.CHARS:
            out=R.verify(N.case(ab),p,r)
            assert all(out['checks'].values())
            assert all(v for row in out['samples'] for v in row['checks'].values())


def test_equal_adjoint_characters_are_not_used_as_equivalence_certificate():
    assert N.fixtures()['checks']['inverse_character_not_complete_classifier']
    assert R.controls()['checks']['inverse_parent_same']
    for ab in N.N.CHARS:
        # Derivative outcome is recorded, not used to accept nonconstancy.
        out=N.case(ab)
        assert isinstance(out['derivative_zero'],bool)
        assert out['checks']['parent_character_nonconstant']
