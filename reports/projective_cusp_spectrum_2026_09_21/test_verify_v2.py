"""F11 post-failure expectation correction; preserve all unaffected checks."""
import importlib.util
from pathlib import Path
import sympy as s
import pytest

def load(name,filename):
    spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name(filename))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

original=load('f11_original_tests','test_verify.py')
e=load('f11_exception_checks','exception_verify.py')
v=original.v

# Re-export exact original functions WITH their pytest parameterization.
# Only the explicitly named failed expectation is replaced below.
REPLACED='test_every_positive_rank_exception_is_geometric'
for name,value in vars(original).items():
    if name.startswith('test_') and name!=REPLACED:
        globals()[name]=value


@pytest.mark.parametrize('phase',v.PHASES)
def test_corrected_full_parameter_rank_loci(phase):
    b,j=v.certificates(phase)
    expected=(v.q-1)**2 if phase==1 else e.modulus(phase)
    assert b['minors']==j['minors']==70
    assert b['q_only_denominators'] and j['q_only_denominators']
    assert b['gcd']==1 and b['positive_roots']==0
    assert s.expand(j['gcd']-expected)==0
    assert j['positive_roots']==(1 if phase==1 else 2)
    if phase==1:
        assert expected.subs(v.q,1)==0
    else:
        assert expected.subs(v.q,1)!=0
    old={name for name in vars(original) if name.startswith('test_')}
    exported={name for name in globals() if name in old}
    assert old-exported=={REPLACED}


@pytest.mark.parametrize('phase',[-s.Integer(1),s.I,-s.I])
@pytest.mark.parametrize('dual',[False,True])
def test_exceptional_class_is_exact_and_not_a_coboundary(phase,dual):
    cert=e.certificate(phase,dual)
    assert (cert['B_rank'],cert['J_rank'],cert['H1'])==(4,3,1)
    assert cert['cocycle_closed'] and cert['not_boundary']
    p=e.modulus(phase)
    assert e.reduce_scalar(cert['minor'],p)!=0
    b,j=e.v.complex_matrices(phase=phase,dual=dual)
    assert e.reduce_matrix(j*b,p)==s.zeros(4)


@pytest.mark.parametrize('phase',[-s.Integer(1),s.I,-s.I])
def test_symbolic_affine_pipeline_on_exceptional_families(phase):
    rho=v.representation(phase=phase)
    assert original.zero(v.affine_cocycle(v.RELATOR,rho)-v.fox(v.RELATOR,rho))


def test_quadratic_embeddings_and_positive_reciprocal_roots():
    for phase,roots in ((-1,(17-12*s.sqrt(2),17+12*s.sqrt(2))),
                        (s.I,(7-4*s.sqrt(3),7+4*s.sqrt(3)))):
        p=e.modulus(phase)
        assert s.Poly(p,e.q,extension=s.I).is_irreducible
        for root in roots:
            assert root.is_positive and root!=1
            assert s.simplify(p.subs(e.q,root))==0
        assert s.simplify(roots[0]*roots[1])==1
        assert s.expand(e.q**2*p.subs(e.q,1/e.q)-p)==0
