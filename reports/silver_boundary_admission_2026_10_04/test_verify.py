import json
import importlib.util
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('silver_boundary_verify', HERE/'verify.py')
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)
DATA = json.loads((HERE/'members.json').read_text())


def test_field_and_dual_controls():
    v.scalar_controls()


@pytest.mark.parametrize('label', list(DATA['states']))
def test_topology_and_trivial_pair(label):
    state = DATA['states'][label]
    v.check_marking(label,state)
    p = v.Complex({g:v.s.eye(2) for g in v.GEN},state).profile()
    assert p == {'h0_absolute':1,'h0_boundary':1,'h1_absolute':1,
                 'h1_relative':1,'restriction_rank':1,'h1_interior':0}


@pytest.mark.parametrize('label,number', [(label,n) for label in DATA['states'] for n in range(2)])
def test_exact_candidate_and_domain_comparison(label,number):
    state = DATA['states'][label]
    result = v.member(label,state,state['members'][number],v.four(state))
    assert result['controls'] == 'PASS'
    # B1530's previously known value: this is an informed reproduction target.
    assert [result[k]['difference']['h1_interior'] for k in ('W','wedge2W')] == [-1,-1]
    # Other domains are not assumed to match that target; their values are reported.
    for k in ('W','wedge2W'):
        p = result[k]
        assert p['E']['h1_relative'] == p['dual']['h1_absolute']-p['dual']['h0_absolute']
