import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


v = load('cyclic_boundary_test', HERE/'verify.py')
r = load('cyclic_readout_test', HERE/'readout_probe.py')


def test_nonabelian_cyclic_closure_and_opposite_controls():
    out = v.controls()
    assert out['allowed_dimension']*2 == out['ambient_dimension']
    assert out['quadratic_bracket_rank'] == out['old_A2_zero_escape'] == 2
    assert out['enlarged_gauge_escape'] == 1


def test_all_eight_actual_neutral_spaces():
    rows = v.actual_members()
    assert len(rows) == 4
    for row in rows:
        for amp in row['amplitudes'].values():
            n = amp['neutral']
            assert n['isotropic'] and n['cup_rank'] == 2*n['restriction_dimension']
            assert n['H1_boundary'] == 2*n['H0_boundary']


def test_parent_dimension_and_endpoint_cost():
    for row in v.actual_members():
        for key,amp in row['amplitudes'].items():
            assert 2*sum(amp['allowed_A']) == sum(amp['parent_H'])
            assert amp['allowed_A'][0] == 24
            assert amp['charged_reversed_H1_difference'] == ([0,0] if key=='0' else [0,-1])


def test_repaired_readout_and_remaining_acceptance_boundaries():
    assert r.run()['all_expected_behaviors']
