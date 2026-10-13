"""Live exact map checks. They do not assert a physical end or generation count."""
import importlib.util
from pathlib import Path
import pytest

HERE = Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/weave_registered_embedding_2026_10_13'


@pytest.fixture(scope='module')
def modules():
    result=[]
    for name in ('probe','reference'):
        spec=importlib.util.spec_from_file_location('retained_embedding_'+name,HERE/(name+'.py'))
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);result.append(module)
    return result


@pytest.fixture(scope='module')
def outputs(modules):
    return [m.run() for m in modules]


def test_complete_two_methods(outputs):
    assert all(o['checks'] and all(o['checks'].values()) for o in outputs)
    assert outputs[0]['records']==outputs[1]['records']


def test_actual_lift_and_not_identity(modules):
    p=modules[0];s=p.s;a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]])
    transform=s.diag(b,a,a*b);actual=s.diag(-a,a,-a)
    assert p.zero(transform*s.kronecker_product(s.eye(3),a)*transform.H-actual)
    assert not p.zero(s.kronecker_product(s.eye(3),a)-actual)


def test_central_intertwiner_is_zero(modules):
    p=modules[0];s=p.s;x=s.Matrix(6,5,s.symbols('x0:30'))
    equations=-s.eye(6)*x-x*s.eye(5)
    coefficient=s.Matrix([equations[j] for j in range(30)]).jacobian(list(x))
    assert coefficient.rank()==30
    # Adding an odd tensor factor changes the centre and removes THIS test.
    assert (-s.eye(6))*x-x*(-s.eye(5))==s.zeros(6,5)


def test_whole_roster_and_nonconjugate_indices(outputs):
    record=outputs[0]['records']
    assert record['trace_indices']==[180,1200]
    assert record['new_sl2_irreps']==[[1,55],[2,52],[3,27],[4,2]]
    assert sum(d*n for d,n in record['old_sl2_irreps'])==248
    assert record['new_full_weights']!=record['old_full_weights']


def test_literal_moves_not_parity_only(outputs):
    checks=outputs[0]['checks']
    for label in ('L','R'):
        assert checks[label+' full factorization']
        assert checks[label+' unitary whole lift']
        assert checks[label+' arbitrary lift sign retained']


def test_pairing_and_cubic_not_dimension(outputs):
    checks=outputs[0]['checks']
    assert checks['full quadratic Cartan identity'] and checks['nonzero cubic control']
    assert all(v for k,v in checks.items() if k.startswith('full alternating cubic '))
    assert checks['omitted Cartans control'] and checks['group exterior is not Lie exterior']


def test_registered_boundary_not_shared_physical_action(outputs):
    checks=outputs[0]['checks']
    assert outputs[0]['records']['boundary_primitive_scale']==720
    assert checks['registered relation retained'] and checks['unflipped sheet rejected']


def test_singular_point_not_regular_transport(outputs):
    assert outputs[0]['checks']['singular common point not regular chart']
    assert outputs[0]['checks']['regular leaf positive control']
