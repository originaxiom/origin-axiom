"""R84 finite facts, not transcript assertions or a global physical certificate."""
import importlib.util
from pathlib import Path
import sympy as s
import pytest

P = Path(__file__).resolve().parents[1]/'reports'/'physical_bridge_2026_09_05'


def load(name):
    spec = importlib.util.spec_from_file_location(name, P/(name+'.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_adjoint_is_derived_by_conjugation():
    m=load('rigidity_transport')
    z=s.symbols('z')
    assert m.adjoint(z)==s.Matrix([[1,-2*z,-z*z],[0,1,z],[0,0,1]])


def test_local_positive_is_not_deleted():
    m=load('rigidity_transport')
    x,y=m.adjoint(1)-s.eye(3),m.adjoint(s.I)-s.eye(3)
    c=s.zeros(6,1); c[3]=1
    assert (-y).row_join(x)*c==s.zeros(3,1)
    assert x.col_join(y).row_join(c).rank()==3


def test_nu_squared_case_keeps_cusp():
    m=load('rigidity_transport')
    a,b=m.adjoint(1),m.adjoint(s.I)
    assert m.cohom(a-s.eye(3),b-s.eye(3))==[1,2,1]
    assert m.cohom(-a-s.eye(3),b-s.eye(3))==[0,0,0]


def test_split_and_nonsplit_are_distinguished():
    m=load('rigidity_transport')
    assert m.cohom(*m.logs(0,0))==[2,4,2]
    assert m.cohom(*m.logs(1,0))==[1,3,2]
    with pytest.raises(ValueError):
        m.cohom(s.Matrix([[0,1],[0,0]]),s.Matrix([[0,0],[1,0]]))


def test_all_native_controls():
    assert all(load('rigidity_transport').checks().values())


def test_separate_rational_controls():
    assert all(load('rigidity_transport_control').run().values())
