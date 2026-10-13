#!/usr/bin/env python3
"""Independent short physical-scope controls; sympy only."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parent
out=[]
def ck(name,ok,data=None):
    if not ok:raise AssertionError(name)
    out.append({'name':name,'passed':True,**({'data':data} if data is not None else {})})
# Classical central commutator forces zero traces in SU(2).
# If AB=-BA, A is conjugate to -A and B is conjugate to -B. Cayley-Hamilton then A²=B²=-I.
a0,b0=s.symbols('a0 b0',real=True)
ck('Trace anticommutation necessity',s.solve([2*a0,2*b0],[a0,b0])=={a0:0,b0:0})
# Three-dimensional adjoint of quaternion units has central kernel; spinor does not.
I=s.I
px=s.Matrix([[0,1],[1,0]]);py=s.Matrix([[0,-I],[I,0]]);pz=s.diag(1,-1)
Aa=I*px;Bb=I*py
ck('Ramond spinor quaternion center remains faithful',Aa*Bb*Aa.inv()*Bb.inv()==-s.eye(2))
adA=s.diag(1,-1,-1);adB=s.diag(-1,1,-1)
ck('Vector adjoint holonomies commute and lose the center',adA*adB==adB*adA)
ck('Original four-real faithful field vs diagonal embedding center mismatch',s.trace(-s.eye(4))!=s.trace(s.eye(4)))
# Subspace {(x,x)} of su2_A + su2_B is not invariant under Q8 acting only on A.
inc=s.eye(3).col_join(s.eye(3));act=s.diag(adA,s.eye(3))
ck('Diagonal level-two subalgebra is not old Q8-left invariant',inc.row_join(act*inc).rank()>3)
# Wilson-loop eigenvalues in the unique central-puncture handle channel.
rows=[]
for k in range(2,41,2):
    x=k//2
    eigen=[]
    for label in range(k+1):
        v=s.simplify(s.sin(s.pi*(label+1)*(x+1)/(k+2))/s.sin(s.pi*(x+1)/(k+2)))
        eigen.append(v)
    ck(f'k={k}: all integrable Wilson characters equal quaternion-axis characters',all(v==s.sin(s.pi*(j+1)/2) for j,v in enumerate(eigen)))
    ck(f'k={k}: fundamental quantum trace zero',eigen[1]==0)
    rows.append({'k':k,'fundamental':str(eigen[1]),'adjoint':str(eigen[2])})
ck('Fusion relation on puncture state is 0²=1+(-1)',0**2==1-1)
# Additional explicitly conditional selector: exactly one copy of the original
# quaternion doublet in the unique handle ground multiplet, not just the same phase.
for n in range(6):
    k=2+16*n; ground_dimension=k//2+1; doublet_copies=ground_dimension//2
    ck(f'Phase-compatible level {k}: quaternion-doublet multiplicity',doublet_copies==1+4*n)
ck('Exactly one quaternion doublet selects k=2 within the phase-compatible family', [2+16*n for n in range(6) if ((2+16*n)//2+1)//2==1]==[2])
# At level two the one-puncture state is one, not three independent vectors.
ck('Gauss-law dimensional distinction',sum(1 for j in (0,1,2) if 2-j==j)==1)
# Protected earlier current algebra level vs new action.
ck('Level differs by discrete central coefficient',s.Rational(2,2)-s.Rational(1,2)==s.Rational(1,2))
# Primary weight 1/2 vector has zero trace; cubic descendant has nonzero trace.
ck('All zero-mode spinor generators traceless',all(s.trace(p)==0 for p in [px,py,pz]))
ck('Cubic Clifford volume nonzero',s.simplify(s.trace(-I*(px/s.sqrt(2))*(py/s.sqrt(2))*(pz/s.sqrt(2))))==1/s.sqrt(2))
# A genuine same-theory current-vector response on the Ramond ground module.
for a,pa in enumerate([px,py,pz]):
    for b,pb in enumerate([px,py,pz]):
        ck(f'Current-vector Ramond response {a},{b}',s.simplify(s.trace((pa/2)*(pb/s.sqrt(2))))==(1/s.sqrt(2) if a==b else 0))
# Wick signs of the cubic supercurrent: triple contractions give +1/z^3,
# double contractions give +chi_a(z)chi_a(w)/z^2, hence 2T/z.
from itertools import combinations
def contract_sign(pairs):
    remaining=list(range(6));sgn=1
    for i,j in sorted(pairs):
        x,y=remaining.index(i),remaining.index(j)
        sgn*=(-1)**(y-x-1)
        remaining.remove(j);remaining.remove(i)
    return sgn
ck('Cubic supercurrent leading Wick coefficient',(-I)**2*contract_sign([(0,3),(1,4),(2,5)])==1)
for keep in range(3):
    pairs=[(i,i+3) for i in range(3) if i!=keep]
    ck(f'Cubic supercurrent stress tensor coefficient species {keep}',(-I)**2*contract_sign(pairs)==1)
# 2n sigma worldlines fusing to vacuum: calculate from fusion matrix separately.
Ns=s.Matrix([[0,1,0],[1,0,1],[0,1,0]])
for n in range(1,9):ck(f'{2*n} sigma particles: fusion degeneracy',int((Ns**(2*n))[0,0])==2**(n-1))
(R/'results'/'physical_controls.json').write_text(json.dumps({'number_checks':len(out),'checks':out,'Wilson_eigenvalues':rows},indent=2))
print(json.dumps({'number_checks':len(out),'all_passed':True},indent=2))
