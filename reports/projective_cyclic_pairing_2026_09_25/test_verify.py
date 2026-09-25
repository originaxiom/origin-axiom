"""F18 marked algebra, finite witnesses and actual bundle controls."""
from pathlib import Path
from itertools import product
import importlib.util
import pytest
import sympy as s

spec=importlib.util.spec_from_file_location('f18_test_producer',Path(__file__).with_name('verify.py'))
q=importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
p,v=q.p,q.v


def test_tietze_marking_free_automorphism_and_relator():
    assert q.substitute(p.REL,{'m':'t','n':'xt'})=='txTXXTxtX'
    for w in ('x','y','xyXY','xxYxy'):
        assert q.beta(q.beta(w,1),-1)==p.reduce_word(w)
        assert q.beta(q.beta(w,-1),1)==p.reduce_word(w)
    assert q.free_normal(p.REL)==('',0)
    assert [q.free_normal(w) for w in q.FIBER]==[('x',0),('y',0)]
    for length in range(5):
        for letters in product('mnMN',repeat=length):
            w=''.join(letters); fw,k=q.free_normal(w); aw,ak=q.abelian_normal(w)
            assert k==ak and q.fiber_exponents(fw)==aw


def test_marked_monodromy_reflections_and_existing_basis():
    assert q.A==s.Matrix([[0,1],[-1,3]])
    assert q.C==s.Matrix([[-3,1],[-8,3]])
    assert q.fiber_action('T')==-s.eye(2)
    assert q.fiber_action('thetaT')==-q.C
    assert q.C*q.C==s.eye(2) and q.C*q.A*q.C==q.A.inv()
    change=s.Matrix([[1,2],[0,1]]); old=s.Matrix([[2,1],[1,1]])
    assert change.det()==1 and old*change==change*q.B
    for name,sign in (('theta',1),('thetaT',-1)):
        for j in range(3): assert q.fiber_action(name,j)==sign*q.C*q.A**j


def test_mod_four_all_degree_hypotheses_not_simple_module():
    assert q.mod(q.A**3)==s.eye(2)
    assert q.mod(s.eye(2)+q.A+q.A**2)==s.zeros(2)
    assert [(q.A**j-s.eye(2)).det() for j in (1,2)]==[-1,-5]
    assert all(s.gcd(int((q.A**j-s.eye(2)).det()),4)==1 for j in (1,2))
    sub={(0,0),(2,0),(0,2),(2,2)}
    assert {tuple(q.mod(q.A*s.Matrix(a))) for a in sub}==sub
    assert 1<len(sub)<16  # Proper nonzero invariant submodule, not irreducible.
    for d in range(1,13): assert len(q.fiber_characters(d))==(16 if d%3==0 else 1)


def test_all_sixteen_torsion_witnesses_join_exact_f17_marking():
    for a in product(range(4),repeat=2):
        tau=(0,a[0],a[1],(-a[0]+3*a[1])%4)
        assert tau in p.characters()
        assert q.witnesses(a)
        expected={(name,j) for name,j,kind in p.geometric_linear(p.pairing_labels(tau))}
        assert set(q.witnesses(a))==expected
        for c in range(4):
            oldmark=(c,a[0],a[1],(-a[0]+3*a[1]+c)%4)
            assert oldmark in p.characters()
            for name,j in q.witnesses(a):
                assert (name,j,'linear') in p.pairing_labels(oldmark)
    assert len(p.characters())==64


def test_all_degree_controls_and_nonextendable_free_phase():
    for degree in range(1,13):
        for a in q.fiber_characters(degree):
            name,j=q.choose(degree,a)
            assert j<degree
            for c in range(4):
                for w in q.cover_generators(degree):
                    image='m'*j+p.subst(w,name)+'M'*j
                    assert (q.evaluate_character(degree,c,a,image)+q.evaluate_character(degree,c,a,w))%4==0
    assert not any(4*t%4==1 for t in range(4))
    assert q.evaluate_character(4,1,(0,0),'mmmm')==1
    assert q.evaluate_character(4,1,(0,0),'MMMM')==3
    with pytest.raises(ValueError): q.evaluate_character(4,1,(0,0),'m')
    with pytest.raises(ValueError): q.evaluate_character(1,0,(1,0),'m')
    with pytest.raises(ValueError): q.fiber_characters(0)


@pytest.mark.parametrize('middle',[14,34])
def test_actual_bundles_all_characters_at_two_control_degrees(middle):
    for degree in (4,6):
        for a in q.fiber_characters(degree):
            for c in range(4):
                assert all(r.is_zero_matrix for r in q.actual_residuals(middle,degree,c,a))
    # Explicit lower-root controls; complete all-degree implication is algebraic.
    for degree,c,a in ((4,1,(0,0)),(6,1,(0,1)),(6,3,(2,3))):
        assert all(r.is_zero_matrix for r in q.actual_residuals(middle,degree,c,a,embedding=-1))


def test_universal_unipotent_power_recovery_and_mutants():
    d,x,power,recovery,res=q.universal_unipotent_polynomial()
    assert res.is_zero
    wrong=recovery-(1-d)*(power-1)**2/(2*d*d)
    assert s.rem(s.expand(wrong-1-x),x**4,x)!=0
    # The general polynomial is not a root formula for nonunipotent matrices.
    z=s.Rational(2)**3-1
    candidate=1+z/3-s.Rational(1,9)*z*z+s.Rational(5,81)*z**3
    assert candidate!=2
    for middle in (14,34):
        for embedding in (-1,1):
            k,_,_,_=v.context(middle,embedding)
            assert p.matrix_algebra_determinant(middle,embedding)!=k.zero


def test_prime19_countercontrol_does_not_become_a_physical_sl4_twist():
    a=s.Matrix([1,6])
    assert q.mod(q.A*a,19)==q.mod(6*a,19)
    assert q.mod((q.A**9-s.eye(2))*a,19)==s.zeros(2,1)
    assert q.witnesses((1,6),19,9)==()
    t=s.symbols('t')
    assert s.rem(t**4-1,s.cyclotomic_poly(19,t),t)!=0
