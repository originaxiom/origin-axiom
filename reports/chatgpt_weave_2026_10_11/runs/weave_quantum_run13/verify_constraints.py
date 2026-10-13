#!/usr/bin/env python3
"""Canonical constraint control for a real Fourier quadrature of one massive mode.
Independent of the finite internal complex and of the slab reference.
"""
from pathlib import Path
import json
import sympy as s
p=s.symbols('p',real=True); m=s.symbols('m',positive=True)
A,E,z,pi,h,ph=s.symbols('A E z pi h ph',real=True)
q=[A,z,h];mom=[E,pi,ph]
def PB(f,g):return s.expand(sum(s.diff(f,x)*s.diff(g,y)-s.diff(f,y)*s.diff(g,x) for x,y in zip(q,mom)))
facts={}
def check(name,cond):
    facts[name]=bool(cond)
    if not cond:raise AssertionError(name)
def zz(expr):return s.simplify(expr)==0
# A is a sine quadrature; z,lambda are cosine quadratures, so d_i lambda=-p lambda.
C=-p*E+m*pi
B=p*z+m*A
H=(E*E+pi*pi+B*B+ph*ph+(p*p+m*m)*h*h)/2
check('constraint_generates_vector_gauge_shift',zz(PB(A,C)+p))
check('constraint_generates_Goldstone_shift',zz(PB(z,C)-m))
check('constraint_leaves_scalar_h_unchanged',zz(PB(h,C)))
check('mass_term_is_gauge_invariant',zz(PB(B,C)))
check('Gauss_constraint_is_preserved_by_Hamiltonian',zz(PB(C,H)))
check('constraint_is_first_class',zz(PB(C,C)))
Cwrong=-p*E-m*pi
check('wrong_constraint_sign_breaks_preservation',not zz(PB(Cwrong,H)))
Hred=s.simplify(H.subs({z:0,pi:p*E/m}))
expected=((1+p*p/(m*m))*E*E+m*m*A*A+ph*ph+(p*p+m*m)*h*h)/2
check('unitary_gauge_reduced_Hamiltonian',zz(Hred-expected))
kin=s.diff(Hred,E,2);pot=s.diff(Hred,A,2)
check('longitudinal_frequency_squared',zz(kin*pot-p*p-m*m))
check('physical_scalar_frequency_squared',zz(s.diff(Hred,ph,2)*s.diff(Hred,h,2)-p*p-m*m))
omega=s.sqrt(p*p+m*m)
Q=m*A/omega; P=omega*E/m
check('longitudinal_rescaling_is_canonical',zz(PB(Q,P)-1))
check('longitudinal_Hamiltonian_is_positive_oscillator',zz((P*P+omega*omega*Q*Q)/2-Hred+(ph*ph+omega*omega*h*h)/2))
# Independent 4x4 Dirac dispersion for the two Weyl fields in a vector multiplet.
s1=s.Matrix([[0,1],[1,0]]);s2=s.Matrix([[0,-s.I],[s.I,0]]);s3=s.diag(1,-1)
pa=s.symbols('p1:4',real=True); P2=sum(t*t for t in pa)
alpha=[s.kronecker_product(s1,t) for t in [s1,s2,s3]]
beta=s.kronecker_product(s3,s.eye(2))
HD=m*beta
for t,a in zip(pa,alpha):HD+=t*a
check('Dirac_Hamiltonian_Hermitian',HD==HD.H)
check('fermion_dispersion_matches_all_bosonic_polarizations',all(zz(x) for x in HD*HD-(P2+m*m)*s.eye(4)))
# There is no unitary-gauge division by m at zero: keep the first-class constraint.
check('massless_constraint_does_not_delete_harmonic_gauge_field',zz(C.subs(m,0)+p*E))
result={'passed':sum(facts.values()),'total':len(facts),'facts':facts,
        'all_real_p_and_positive_m':True,'full_interacting_constraint_algebra':False,
        'actual_internal_eigenvalues_computed':False}
Path(__file__).with_name('CONSTRAINT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
