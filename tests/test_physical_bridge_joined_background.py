import importlib.util
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05'
def load(name):
    spec=importlib.util.spec_from_file_location(name,BASE/(name+'.py'))
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m
N=load('joined_background')
R=load('joined_background_reference')


def test_simultaneous_transpose_has_whole_space_singular_opposite_control():
    out=N.fixtures()
    assert out['checks']['entire_counterpair_kernel_singular']
    assert out['checks']['diagonal_positive_match']
    assert all(out['checks'].values())


def test_commutant_one_is_not_an_irreducibility_certificate():
    out=N.fixtures()
    assert out['flag_commutant_dimension']==1
    assert out['checks']['flag_algebra_not_full']
    assert out['checks']['full_two_algebra'] and out['checks']['proper_two_algebra']


def test_all_three_actual_character_joins_are_full_matrix_representations():
    for ab in N.CHARS:
        out=N.case(ab)
        assert out['outcome']=='FULL_MATRIX_ADMISSION_PREMISE'
        assert out['algebra_dimension']==25 and all(out['checks'].values())


def test_same_closed_rank_five_count_has_its_invariant_terms_and_dual():
    out=N.spectrum()
    assert out['representative']==[0,1]
    assert out['rank_five']['h0']==out['dual_five']['h0']==0
    assert out['rank_five']['h1']==out['dual_five']['h1']


def test_actual_exterior_boundary_and_exact_piece_counts_transport_together():
    out=N.spectrum()
    assert out['checks']['exterior_torus_acyclic']
    assert out['exterior_join_h1']==sum(x['h1'] for x in out['exterior_piece_counts'][:2])
    assert out['dual_exterior_join_h1']==sum(x['h1'] for x in out['exterior_piece_counts'][2:])
    assert all(out['checks'].values())


def test_separate_modular_reference_detects_opposites_and_recomputes_double():
    assert all(R.controls()['checks'].values())
    p=next(p for p in R.PRIMES if R.roots(p))
    r=R.roots(p)[0]
    for ab in N.CHARS:
        out=R.verify_case(N.public(N.case(ab)),p,r,N.spectrum())
        assert all(out['checks'].values())
