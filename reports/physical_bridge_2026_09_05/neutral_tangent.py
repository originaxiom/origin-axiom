"""R47 finite neutral-tangent controls; no global harmonic profile solver."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as s

spec = importlib.util.spec_from_file_location(
    'r47_parent_cusp',Path(__file__).with_name('parent_cusp.py'))
pc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pc)
cc = pc.cc
q,R = cc.Q,cc.R
RELATOR = 'mnMNmNMnmN'
LONGITUDE = 'nMNmmNMn'
BETA = 6/(q-1/q)
DOT_BETA = s.factor(q*s.diff(BETA,q))


def dot(a):
    return cc.clean(q*a.diff(q))


def tail_tangent():
    return cc.D+DOT_BETA*cc.P/R


def closure_residuals(omit_derivative=False):
    bx,bt,br,_ = cc.connection()
    ct = tail_tangent()
    radial = cc.comm(br,ct)
    if not omit_derivative:
        radial += ct.diff(R)
    return cc.clean(cc.comm(bx,ct)),cc.clean(radial)


def word_cocycle(word):
    """Adjoint cocycle composition, distinct from differentiating a word matrix."""
    m,n = cc.prior.generators(q)
    letters = {'m':m,'n':n}
    tangents = {g:cc.clean(dot(a)*a.inv()) for g,a in letters.items()}
    for g,a in tuple(letters.items()):
        ai = a.inv()
        letters[g.upper()] = ai
        tangents[g.upper()] = cc.clean(-ai*tangents[g]*a)
    hol = s.eye(4)
    tangent = s.zeros(4)
    for char in word:
        tangent = cc.clean(tangent+hol*tangents[char]*hol.inv())
        hol = cc.clean(hol*letters[char])
    return hol,tangent


@lru_cache(None)
def literal_longitude_detector():
    data = cc.peripheral(q)
    basis = data['basis']
    ell = cc.prior.word(LONGITUDE,cc.prior.generators(q))
    detector = cc.clean(basis*cc.D*basis.inv())
    tangent = cc.clean(dot(ell)*ell.inv())
    return {'detector':detector,'tangent':tangent,
            'parallel':cc.clean(cc.comm(detector,ell)),
            'pairing':cc.clean(s.trace(detector*tangent)),
            'trace_derivative':cc.clean(s.trace(dot(ell)))}


def compact_profile():
    # Extension by zero is C1. A smooth normalized bump is used in the proof.
    return 30*(R-1)**2*(2-R)**2


def reference_integrals():
    b,z = s.symbols('b z',real=True,positive=True)
    r0 = s.symbols('R0',positive=True)
    square = 12+b*b/R**2
    l2 = s.integrate(square*R**(-s.Rational(3,2)),(R,r0,s.oo))
    l4 = s.integrate(square**2*R**(-s.Rational(3,2)),(R,r0,s.oo))
    old = s.integrate(12/z,(z,1,s.oo))
    return b,r0,cc.clean(l2),cc.clean(l4),old


def pairing_witness():
    a,b,c = q/4,q/(2*(q+1)),(q*q+1)/(2*(q+1))
    return s.Matrix([[a,-a,b,c],[-a,a,-b,b],[b,-b,1,-1],[c,b,-1,1]])


def pairing_residuals(omit_compensator=False):
    witness = pairing_witness()
    answer = []
    for a in cc.prior.generators(q):
        residue = dot(a).T*witness-witness*dot(a)
        if not omit_compensator:
            residue += a.T*dot(witness)-dot(witness)*a
        answer.append(cc.clean(residue))
    return tuple(answer)


def run():
    hol,cocycle = word_cocycle(RELATOR)
    data = literal_longitude_detector()
    b,r0,l2,l4,old = reference_integrals()
    witness = pairing_witness()
    profile = compact_profile()
    checks = {
        'global_relation_tangent':hol==s.eye(4) and cocycle==s.zeros(4),
        'tail_covariant_closure':all(a==s.zeros(4) for a in closure_residuals()),
        'missing_radial_term_fails':closure_residuals(True)[1]!=s.zeros(4),
        'literal_longitude_detector':data['parallel']==s.zeros(4) and data['pairing']==12,
        'trace_class_nonconstant':cc.clean(data['trace_derivative']-3*(q**4-1)/q**3)==0,
        'compact_detector':s.integrate(profile,(R,1,2))==1
            and cc.clean(s.trace(tail_tangent()*cc.D))==12,
        'finite_canonical_L2':cc.clean(l2-24/s.sqrt(r0)-2*b*b/(5*r0**s.Rational(5,2)))==0,
        'finite_canonical_L4':cc.clean(l4-288/s.sqrt(r0)-48*b*b/(5*r0**s.Rational(5,2))
                                      -2*b**4/(9*r0**s.Rational(9,2)))==0,
        'old_metric_divergence_preserved':old==s.oo,
        'incoming_generic_pairing':all(cc.clean(a.T*witness-witness*a)==s.zeros(4)
                                       for a in cc.prior.generators(q)),
        'pairing_determinant':cc.clean(witness.det()+q*(q*q+q+1)**3/(16*(q+1)**4))==0,
        'differentiated_pairing':all(a==s.zeros(4) for a in pairing_residuals()),
        'wrong_compensator_detected':any(a!=s.zeros(4) for a in pairing_residuals(True))}
    return {'checks':checks,'all_checks_pass':all(checks.values()),
            'grade':'Finite controls; global Hilbert-space argument separately authored.',
            'full_neutral_dimension_computed':False,'nonlinear_modulus_derived':False,
            'canonical_geometric_pairing_derived':False,'physical_chirality_derived':False}


if __name__=='__main__':
    result = run()
    print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
