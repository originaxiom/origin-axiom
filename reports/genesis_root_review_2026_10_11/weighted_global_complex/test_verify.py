"""Two-sided detector checks; all science imports occur only after the seal."""
import importlib.util
from pathlib import Path
import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('weighted_flag_native',Path(__file__).with_name('verify.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_unmatched_boundary_endpoint_and_cancellation():
    z = s.zeros(0)
    C = (z,z)
    T = (s.zeros(0,1),z)
    f = (s.zeros(1,0),z,z)
    assert v.census(v.cone(C,T,f))['H'] == [0,1,0,0]
    attached = v.full_fiber(C,T,f,T,(s.eye(1),z,z))
    assert v.census(attached)['H'] == [0,0,0,0]


def test_empty_boundary_recovers_source():
    z = s.zeros(0)
    C = (s.Matrix([[1,0]]),s.zeros(0,1))
    model = v.cone(C,(z,z),(s.zeros(0,2),s.zeros(0,1),z))
    assert v.census(model)['H'] == [1,0,0,0]


def test_broken_chain_map_is_rejected():
    C = (s.eye(1),s.zeros(0,1))
    with pytest.raises(AssertionError,match='not a chain map'):
        v.cone(C,C,(s.eye(1),2*s.eye(1),s.zeros(0)))


def test_attached_differential_must_not_be_erased():
    z = s.zeros(0)
    C = (z,z)
    T = (s.eye(1),s.zeros(0,1))
    f = (s.zeros(1,0),s.zeros(1,0),z)
    inc = (s.eye(1),s.eye(1),z)
    assert v.census(v.full_fiber(C,T,f,T,inc))['H'] == [0,0,0,0]
    with pytest.raises(AssertionError,match='not a chain map'):
        v.full_fiber(C,T,f,(s.zeros(1),s.zeros(0,1)),inc)


def test_rank_and_field_encoding():
    M = s.Matrix([[1,s.sqrt(2)],[s.sqrt(2),2]])
    assert v.rank(M) == 1
    assert v.rank(M+s.eye(2)) == 2
    assert v.pack(M)['Qsqrt2_pairs'] == [['1','0'],['0','1'],['0','1'],['2','0']]
    with pytest.raises(AssertionError,match='outside Qsqrt2'):
        v.pack(s.Matrix([[s.sqrt(3)]]))


def test_weight_derivative_and_zero_amplitude_control():
    r,ell,b,a,q,j = s.symbols('r ell b a q j',real=True)
    phi = ((j-1)/ell-a)*r+ell*b*(s.exp(2*r/ell)-1)*q/2
    assert s.simplify(s.diff(phi,r)-((j-1)/ell-a+b*q*s.exp(2*r/ell))) == 0
    # ell=b=1, exp(2R)=4, |a|<=2, |q|>=1 covers all charged sectors.
    for degree in range(3):
        for aval in range(-2,3):
            for qval in (-4,-3,-2,-1,1,2,3,4):
                tail = degree-1-aval+4*qval
                assert tail >= 1 if qval>0 else tail <= -1
    assert not (0-1-1 >= 1)  # b=0 in a growing W direction fails the bound.


def test_full_fiber_and_quotient_with_nonzero_end_differential():
    z = s.zeros(0)
    C = (z,z)
    T = (s.diag(1,0),s.zeros(0,2))
    f = (s.zeros(2,0),s.zeros(2,0),z)
    A = (s.eye(1),s.zeros(0,1))
    i0 = s.Matrix([[1],[0]])
    full = v.full_fiber(C,T,f,A,(i0,i0,s.zeros(0)))
    quotient = v.cone(C,(s.zeros(1),s.zeros(0,1)),(s.zeros(1,0),s.zeros(1,0),z))
    assert v.census(full)['H'] == v.census(quotient)['H'] == [0,1,1,0]


def test_explicit_quadratic_normalization_and_field_guard():
    u = s.sqrt(2)
    assert v.clean(s.Matrix([[1/(3+2*u)]])) == s.Matrix([[3-2*u]])
    assert v.clean(s.Matrix([[(123+87*u)*(123-87*u)]])) == s.Matrix([[-9]])
    assert v.clean(s.Matrix([[(1+u)**8]])) == s.Matrix([[577+408*u]])
    with pytest.raises(AssertionError,match='outside Qsqrt2'):
        v.clean(s.Matrix([[s.sqrt(3)]]))
