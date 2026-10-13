#!/usr/bin/env python3
"""Exact parity-twist conjugacy, in a complex representation independent of verify.py."""
import json
from pathlib import Path
import sympy as s
I=s.I
A=s.diag(I,-I)
B=s.Matrix([[0,1],[-1,0]])
checks=[]
def check(name,yes):
    assert bool(yes),name
    checks.append(name)
check('quaternion defining relations in complex dimension two',A*A==B*B==-s.eye(2) and A*B==-B*A)
check('peripheral commutator equals -I2',A*B*A.inv()*B.inv()==-s.eye(2))
intertwiners=[]
for name,signs,U in [('chi_(+,-)',(1,-1),A),('chi_(-,+)',(-1,1),B),('chi_(-,-)',(-1,-1),A*B)]:
    check(name+' unitary intertwiner',U.H*U==s.eye(2))
    check(name+' conjugates both holonomies exactly',U*A*U.inv()==signs[0]*A and U*B*U.inv()==signs[1]*B)
    intertwiners.append({'character_values_on_A_B':signs,'U':[[str(v) for v in U.row(i)] for i in range(2)]})
r={'checks':checks,'intertwiners':intertwiners,'grade':'COMPUTED EXACTLY; operator conclusion conditional on covariant domains and identical insertion-free prescription',
   'operator_consequence':'D_(chi*rho)=U D_rho U^-1; spectra of D^dagger D and determinant magnitudes coincide',
   'theta_control':'|theta_2(i)^2/theta_3(i)^2|=1/sqrt(2), whereas limit_(Im tau -> infinity) |theta_2^2/theta_3^2|=0',
   'excluded_interpretation':'three parity-labelled free-fermion vacuum determinants, up to fixed monomial basis rescaling, equal the theta triplet',
   'not_excluded':['cohomology representation','puncture-state amplitudes','correlators with nontrivial insertions','noncovariant or parity-specific extra boundary data','larger quantum theories']}
Path(__file__).with_name('parity_conjugacy_results.json').write_text(json.dumps(r,indent=2)+'\n')
print(f'{len(checks)} exact checks passed: all three nontrivial parity twists are unitarily conjugate.')
print('Equal vacuum determinant magnitudes follow only for identical, gauge-covariant domains/prescriptions.')
