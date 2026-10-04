import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location('charged_boundary_test_source',Path(__file__).with_name('verify.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_two_sided_controls():
    r = v.controls()
    assert r['nonisotropic_input_detected'] and r['compact_su2_positive']
    assert r['abelian_ideal_adjoint_rank'] > 0 and r['abelian_ideal_adjoint_square_zero']
    assert r['complex_nilpotent_alone_is_not_obstruction']


def test_actual_population_and_no_deleted_degrees():
    rows = v.actual_members()
    assert len(rows) == 4
    for row in rows:
        assert set(row['amplitudes']) == {'0','1'}
        for a in row['amplitudes'].values():
            pair = a['fundamental_complex']
            assert len(pair['E']['H']) == len(pair['dual']['H']) == 4
            assert pair['E']['H'] == pair['dual']['H'][::-1]
            assert a['physical_fermion_domain'] == 'not derived'


def test_construction_success_means_every_inclusion():
    for row in v.actual_members():
        for key,a in row['amplitudes'].items():
            if a['status'] == 'PASS':
                assert not a['errors'] and a['forced_neutral_isotropic']
                assert a['new_neutral_escape']['rank'] == 0
                assert all(r['rank']==0 for r in a['charged_actions'].values())
                assert a['H1_differences'] == ([0,0] if key=='0' else [-1,-1])
                assert 2*sum(a['allowed_A']) == sum(a['parent_H'])
            else:
                assert a['status'] == 'CONSTRUCTION_FAIL'
                assert a['errors']
