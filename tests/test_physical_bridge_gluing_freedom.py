import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05'
def load(name):
    spec=importlib.util.spec_from_file_location(name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m
N=load('gluing_freedom')
R=load('gluing_freedom_reference')


def test_relative_gluing_controls_distinguish_gauge_and_noncentral_seam():
    assert all(N.fixtures()['checks'].values())
    assert all(R.controls()['checks'].values())


def test_actual_piece_algebras_are_opposite_full_parabolics():
    for ab in N.N.CHARS:
        out=N.case(ab)
        assert out['left_algebra_dimension']==out['right_algebra_dimension']==21
        assert out['checks']['piece_scalar_commutants']
        assert out['checks']['matching_block_diagonal']


def test_actual_neutral_bends_are_not_global_coboundaries():
    for ab in N.N.CHARS:
        out=N.case(ab)
        assert out['peripheral_centralizer_dimension']==5
        assert out['neutral_h1_lower_bound']==4
        assert out['coboundary_rank']==24 and out['joined_rank']==28
        assert out['checks']['bend_tangent_relators']


def test_relative_bend_changes_an_actual_gauge_invariant_loop_trace():
    for ab in N.N.CHARS:
        out=N.case(ab); w=out['trace_witness']
        assert w and w['formula_pass'] and w['separates_one_two']
        assert out['checks']['changed_join_full_matrix25']
        assert all(out['checks'].values())


def test_actual_join_trivial_coefficient_has_one_degree_one_profile():
    out=N.trivial()
    assert out['counts']['h0']==out['counts']['h1']==1
    assert all(out['checks'].values())


def test_separate_modular_verifier_recomputes_bends_and_trace_at_two_primes():
    for p,r in R.PRIME_ROOTS:
        for ab in N.N.CHARS:
            out=R.verify(N.case(ab),p,r)
            assert all(out['checks'].values())
