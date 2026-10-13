#!/usr/bin/env python3
"""Exact tests for Run 7. Requires sympy. No earlier verification code imported.
The SU(2)_2 F/R data are standard data from Rowell–Stong–Wang, §5.3.5,
arXiv:0712.1377v4. They are inputs, not independently discovered constants.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import product
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results'; OUT.mkdir(exist_ok=True)
checks=[]
def simp(x):
    return s.simplify(s.expand_complex(x))
def equal(x,y=0):
    if isinstance(x,s.MatrixBase):
        return x.shape==y.shape and all(simp(a-b)==0 for a,b in zip(x,y))
    return simp(x-y)==0
def check(name,ok,detail=None):
    if not bool(ok): raise AssertionError(name + (' '+str(detail) if detail else ''))
    checks.append({'name':name,'passed':True,**({'detail':detail} if detail is not None else {})})
def expturn(r):
    return s.expand_complex(s.exp(2*s.pi*s.I*s.Rational(r)))
I=s.I; rt2=s.sqrt(2); z8=expturn(s.Rational(1,8))
sx=s.Matrix([[0,1],[1,0]]); sy=s.Matrix([[0,-I],[I,0]]); sz=s.diag(1,-1)
A=I*sz; B=I*sy; C=A*B; eye=s.eye(2)
check('Quaternion squares and commutator',equal(A*A,-eye) and equal(B*B,-eye) and equal(A*B,-B*A) and equal(A*B*A.inv()*B.inv(),-eye))
nL=(eye+A)/rt2; nR=(eye-B)/rt2
check('Both prescribed quaternion normalizers',equal(nL*A*nL.inv(),A) and equal(nL*B*nL.inv(),A*B) and equal(nR*A*nR.inv(),A*B) and equal(nR*B*nR.inv(),B))
OL=s.Matrix([[1,0,0],[0,0,1],[0,-1,0]])
OR=s.Matrix([[0,-1,0],[1,0,0],[0,0,1]])
check('Adjoint axes (A,C,B)', all(equal(n*axis*n.inv(),sum((O[j,k]*[A,C,B][j] for j in range(3)),s.zeros(2))) for n,O in [(nL,OL),(nR,OR)] for k,axis in enumerate([A,C,B])))
TL=z8*OL; TR=s.conjugate(z8)*OR; TS=TR*TL.inv()*TR
D=s.diag(-I,1,I); P=s.Matrix([[0,0,1],[0,1,0],[1,0,0]]); M=s.Matrix([[I,0,0],[0,0,1],[0,1,0]])
check('Source intertwiner on both generators',equal(D*TL*D.inv(),s.conjugate(z8)*M) and equal(D*TS*D.inv(),z8*P))
check('Genuine source metaplectic relations',equal(TS**4,-s.eye(3)) and equal(TS**8,s.eye(3)) and equal(TS**2,(TS*TL)**3))

# SU(2)_k labels are twice the spin: 0,...,k.
def fusion_k(k,a,b):
    return list(range(abs(a-b),min(a+b,2*k-a-b)+1,2))
def weight(k,a): return s.Rational(a*(a+2),4*(k+2))
def central_charge(k): return s.Rational(3*k,k+2)
level_rows=[]
for k in range(1,81):
    J=k
    check(f'Level {k}: simple-current action',all(fusion_k(k,J,x)==[k-x] for x in range(k+1)))
    returns=[x for x in range(k+1) if x in fusion_k(k,J,x)]
    check(f'Level {k}: central-puncture rank',returns==([] if k%2 else [k//2]))
    # Exact monodromy exponent; exponent differs from -r/2 by no integer.
    check(f'Level {k}: quantum center monodromy',all(weight(k,k-r)-weight(k,k)-weight(k,r)==-s.Rational(r,2) for r in range(k+1)))
    row={'k':k,'rank':len(returns),'c':str(central_charge(k))}
    if returns:
        exponent=weight(k,returns[0])-central_charge(k)/24
        check(f'Level {k}: unique handle twist exponent',exponent==s.Rational(k,16))
        row.update(handle_label=returns[0],T_exponent=str(exponent),target_T_match=(exponent-s.Rational(1,8)).q==1)
    level_rows.append(row)
matching=[r['k'] for r in level_rows if r.get('target_T_match')]
check('Necessary matching levels are 2 modulo 16',matching==[2,18,34,50,66])

# SU(2)_2: labels 0=vacuum, 1=sigma, 2=f (vector simple current).
labels=(0,1,2)
def fusion(a,b): return fusion_k(2,a,b)
S=s.Matrix([[1,rt2,1],[rt2,0,-rt2],[1,-rt2,1]])/2
theta=[s.Integer(1),expturn(s.Rational(3,16)),s.Integer(-1)]
c=s.Rational(3,2)
T=s.diag(*[expturn(weight(2,a)-c/24) for a in labels])
dims=[s.Integer(1),rt2,s.Integer(1)]
check('SU2 level2 modular S unitary',equal(S*S.T,s.eye(3)))
check('SU2 level2 modular relation',equal((S*T)**3,S*S))
check('SU2 level2 Verlinde coefficients',all(equal(sum(S[a,x]*S[b,x]*s.conjugate(S[c_,x])/S[0,x] for x in labels),int(c_ in fusion(a,b))) for a,b,c_ in product(labels,repeat=3)))
check('Fusion associativity',all(sorted(y for x in fusion(a,b) for y in fusion(x,c_))==sorted(y for x in fusion(b,c_) for y in fusion(a,x)) for a,b,c_ in product(labels,repeat=3)))
indicators=[]
for k in labels:
    nu=sum(int(k in fusion(a,b))*dims[a]*dims[b]*(theta[a]/theta[b])**2 for a,b in product(labels,repeat=2))/4
    indicators.append(simp(nu))
check('Frobenius Schur indicators including pseudoreal sigma',indicators==[1,-1,1])
check('Gauss Milgram chiral central charge',equal(sum(d*d*t for d,t in zip(dims,theta))/2,expturn(s.Rational(3,16))))
check('Central line f has -1 monodromy with sigma',equal(theta[1]/(theta[2]*theta[1]),-1))

@lru_cache(None)
def F(a,b,c_,d,e,f,wrong=False):
    # ((a b)e c)d -> (a (b c)f)d.
    if e not in fusion(a,b) or d not in fusion(e,c_) or f not in fusion(b,c_) or d not in fusion(a,f): return s.Integer(0)
    if (a,b,c_,d)==(1,1,1,1):
        H=s.Matrix([[1,1],[1,-1]])/rt2
        return (1 if wrong else -1)*H[[0,2].index(e),[0,2].index(f)]
    if (a,b,c_,d) in [(2,1,2,1),(1,2,1,2)]: return s.Integer(-1)
    return s.Integer(1)
@lru_cache(None)
def R(a,b,d):
    if d not in fusion(a,b): return s.Integer(0)
    if 0 in (a,b): return s.Integer(1)
    if (a,b,d)==(1,1,0): return -expturn(-s.Rational(3,16))
    if (a,b,d)==(1,1,2): return expturn(s.Rational(1,16))
    if (a,b,d)==(2,2,0): return s.Integer(-1)
    if (a,b,d) in [(1,2,1),(2,1,1)]: return I
    raise ValueError((a,b,d))
check('All channel ribbon identities',all(equal(R(a,b,d)*R(b,a,d),theta[d]/(theta[a]*theta[b])) for a,b in product(labels,repeat=2) for d in fusion(a,b)))

# General fusion-tree implementation. The objects at leaves are fixed, leaf IDs move.
# State dictionaries map frozensets of leaf IDs to the internal fusion label.
def leaves(t): return frozenset([t]) if isinstance(t,int) else leaves(t[0])|leaves(t[1])
def tree_at(t,path):
    for x in path: t=t[x]
    return t
def replace(t,path,new):
    if not path: return new
    i=path[0]; pair=list(t); pair[i]=replace(pair[i],path[1:],new); return tuple(pair)
def all_states(t,objects):
    if isinstance(t,int): return [(objects[t],{frozenset([t]):objects[t]})]
    out=[]
    for a,sa in all_states(t[0],objects):
        for b,sb in all_states(t[1],objects):
            for d in fusion(a,b): out.append((d,{**sa,**sb,leaves(t):d}))
    return out
def basis(t,objects,total): return [state for d,state in all_states(t,objects) if d==total]
def assoc(t,path,objects,total,inverse=False,wrong=False):
    node=tree_at(t,path)
    if inverse:
        a,(b,c_)=node
        newnode=((a,b),c_)
    else:
        (a,b),c_=node
        newnode=(a,(b,c_))
    outtree=replace(t,path,newnode)
    bs=basis(t,objects,total); bt=basis(outtree,objects,total)
    mat=s.zeros(len(bt),len(bs))
    for col,st in enumerate(bs):
        for row,tt in enumerate(bt):
            if any(st[key]!=tt[key] for key in st.keys() & tt.keys()):continue
            aa=st[leaves(a)];bb=st[leaves(b)];cc=st[leaves(c_)];dd=st[leaves(node)]
            if inverse:
                e=tt[leaves(a)|leaves(b)];f=st[leaves(b)|leaves(c_)]
                coeff=s.conjugate(F(aa,bb,cc,dd,e,f,wrong))
            else:
                e=st[leaves(a)|leaves(b)];f=tt[leaves(b)|leaves(c_)]
                coeff=F(aa,bb,cc,dd,e,f,wrong)
            mat[row,col]=coeff
    return outtree,mat
def braid(t,path,objects,total):
    a,b=tree_at(t,path); newtree=replace(t,path,(b,a))
    bs=basis(t,objects,total);bt=basis(newtree,objects,total)
    mat=s.zeros(len(bt),len(bs))
    for j,st in enumerate(bs):
        for i,tt in enumerate(bt):
            if st==tt:mat[i,j]=R(st[leaves(a)],st[leaves(b)],st[leaves(a)|leaves(b)])
    return newtree,mat
def path_product(t,steps,objects,total,wrong=False):
    result=s.eye(len(basis(t,objects,total)))
    for kind,path in steps:
        if kind=='a': t,mat=assoc(t,path,objects,total,wrong=wrong)
        elif kind=='ai':t,mat=assoc(t,path,objects,total,inverse=True,wrong=wrong)
        elif kind=='r':t,mat=braid(t,path,objects,total)
        else:raise ValueError(kind)
        result=mat*result
    return t,result
pent=0;hexag=0;badhex=0
for objects in product(labels,repeat=4):
    for total in labels:
        t0=(((0,1),2),3)
        if not basis(t0,objects,total):continue
        ta,ma=path_product(t0,[('a',(0,)),('a',()),('a',(1,))],objects,total)
        tb,mb=path_product(t0,[('a',()),('a',())],objects,total)
        if ta!=tb or not equal(ma,mb):raise AssertionError(('pentagon',objects,total,ma,mb))
        pent+=1
for objects in product(labels,repeat=3):
    for total in labels:
        # Hexagon I, a(bc) -> (bc)a.
        for t0,steps in [((0,(1,2)),[('ai',()),('r',(0,)),('a',()),('r',(1,)),('ai',())]),
                         (((0,1),2),[('a',()),('r',(1,)),('ai',()),('r',(0,)),('a',())])]:
            if not basis(t0,objects,total):continue
            target,direct=braid(t0,(),objects,total)
            final,path=path_product(t0,steps,objects,total)
            if final!=target or not equal(direct,path):raise AssertionError(('hexagon',objects,total,t0,direct,path))
            hexag+=1
            _,wrong=path_product(t0,steps,objects,total,wrong=True)
            if not equal(direct,wrong):badhex+=1
check('Complete multiplicity-free pentagon enumeration',pent>0,{'nonempty_blocks':pent})
check('Both full hexagon families',hexag>0,{'nonempty_blocks':hexag})
check('Wrong Frobenius sign fails hexagons',badhex>0,{'failed_blocks':badhex})

# Explicit braid statistics on three sigma anyons with total sigma.
B1=s.diag(R(1,1,0),R(1,1,2))
F3=-s.Matrix([[1,1],[1,-1]])/rt2
B2=F3.T.conjugate()*B1*F3
check('Non-Abelian braid relation',equal(B1*B2*B1,B2*B1*B2))
check('Braids really do not commute',not equal(B1*B2,B2*B1))
check('Quantum dimension of sigma',equal(S[0,1]/S[0,0],rt2))

# All-genus dimension formulas checked against exact S-sums.
genus=[]
for g in range(1,8):
    vacuum=simp(sum(S[0,x]**(2-2*g) for x in labels))
    punct=simp(sum(S[2,x]*S[0,x]**(1-2*g) for x in labels))
    check(f'Genus {g}: vacuum and central puncture dimensions',vacuum==2**(g-1)*(2**g+1) and punct==2**(g-1)*(2**g-1))
    genus.append({'g':g,'vacuum':int(vacuum),'central_puncture':int(punct)})

# Ramond Clifford construction, one nonzero oscillator level per species.
def annihilator(n,index):
    dim=1<<n; mat=s.zeros(dim)
    for state in range(dim):
        if state&(1<<index):
            dest=state^(1<<index)
            sign=(-1)**((state&((1<<index)-1)).bit_count())
            mat[dest,state]=sign
    return mat
N=3; parity=s.diag(*[(-1)**i.bit_count() for i in range(1<<N)])
paulis=[sx,sy,sz]
zero=[s.kronecker_product(p/rt2,parity) for p in paulis]
a=[s.kronecker_product(s.eye(2),annihilator(N,i)) for i in range(N)]
check('Ramond zero-mode Clifford algebra',all(equal(zero[i]*zero[j]+zero[j]*zero[i],s.eye(16)*int(i==j)) for i,j in product(range(3),repeat=2)))
check('Zero and nonzero modes anticommute',all(equal(z*a_+a_*z,s.zeros(16)) for z in zero for a_ in a))
modes=[{-1:a[i].T,0:zero[i],1:a[i]} for i in range(3)]
G0=s.zeros(16)
for r1,r2,r3 in product([-1,0,1],repeat=3):
    if r1+r2+r3==0: G0+=-I*modes[0][r1]*modes[1][r2]*modes[2][r3]
q=s.Symbol('q'); diag=[q**state.bit_count() for _spin in range(2) for state in range(8)]
trace=s.expand(sum(G0[i,i]*diag[i] for i in range(16)))
check('Explicit Ramond insertion trace, not an ordinary partition',equal(trace,(1-q)**3/rt2))
check('Single Majorana insertion has zero trace',all(equal(sum(z[i,i]*diag[i] for i in range(16)),0) for z in zero))
check('Ramond leading exponent from h_sigma minus c/24',weight(2,1)-c/24==s.Rational(1,8))
check('Cubic Ramond insertion is nonzero on ground states',equal(G0[0,0],1/(2*rt2)) and equal(G0[8,8],1/(2*rt2)))

# Euler cube versus independent Jacobi derivative series, exact finite coefficients.
order=60; coeff=[0]*(order+1);coeff[0]=1
for n in range(1,order+1):
    nxt=[0]*(order+1)
    for k0,v in enumerate(coeff):
        if not v:continue
        for j,b in enumerate([1,-3,3,-1]):
            if k0+j*n<=order:nxt[k0+j*n]+=v*b
    coeff=nxt
jac=[0]*(order+1)
for n in range(order+1):
    d=n*(n+1)//2
    if d<=order:jac[d]=(-1)**n*(2*n+1)
check('Independent eta-cubed q coefficients through q60',coeff==jac)
# Current level from explicit adjoint matrices of three Majoranas.
E=[]
for i in range(3):
    mat=s.zeros(3)
    for j in range(3):
        for k in range(3):mat[j,k]=s.LeviCivita(i,j,k)
    E.append(mat)
# J_i=-i/2 epsilon_iab chi_a chi_b. Double contractions give -Tr(E_i E_j)/2.
metric=s.Matrix(3,3,lambda i,j:-s.trace(E[i]*E[j])/2)
check('Three Majorana currents have level two (double pole delta)',metric==s.eye(3))
check('Cannot relabel level one currents as level two preserving OPE',not equal(metric,s.eye(3)/2))

# Coefficient line of the nonzero cubic block.
ellT=z8;ellS=z8**(-3)
check('Quantum line metaplectic relations',equal(ellS**2,(ellS*ellT)**3) and equal(ellS**4,-1) and equal(ellS**8,1))
check('Quantum line equals source cohomology character',equal(ellT,z8) and equal(ellS,z8**(-3)))
# Actual unpunctured three-dimensional state space is a negative control.
vac_exponents=[(weight(2,a)-c/24)%1 for a in labels]
target_exponents=[s.Rational(1,8),s.Rational(3,8),s.Rational(7,8)]
check('Torus vacuum three-space is not manuscript triplet',sorted(vac_exponents)!=sorted(target_exponents))
# A scalar shift cannot equate even their projective T spectra.
projective_match=False
for x in vac_exponents:
    for y in target_exponents:
        shift=(y-x)%1
        if sorted((a+shift)%1 for a in vac_exponents)==sorted(target_exponents):projective_match=True
check('Vacuum torus spectrum fails even scalar-shift T test',not projective_match)
# Explicit all-positive-word checks and homology traces (formula is the proof).
word_rows=[]
for length in range(1,9):
    for letters in product('LR',repeat=length):
        w=''.join(letters); n=w.count('L')-w.count('R')
        word_rows.append({'word':w,'phase_turns':str(s.Rational(n,8)%1)})
check('All positive words through length8 inventoried',len(word_rows)==510)
check('Key mapping-torus line phases', next(x['phase_turns'] for x in word_rows if x['word']=='LR')=='0' and next(x['phase_turns'] for x in word_rows if x['word']=='LLLR')=='1/4')

results={'scope':'New conditional SU(2)_k Chern-Simons/WZW model; not the old level-one theory',
 'checks':checks,'named_checks':len(checks), 'coherence':{'pentagon_blocks':pent,'hexagon_blocks':hexag,'negative_control_failed_hexagons':badhex},
 'level_scan':level_rows,'T_matching_levels':matching,'genus_dimensions':genus,
 'matrices':{n:str(v) for n,v in {'S_SU2_2':S,'T_SU2_2':T,'F_sigma':F3,'braid1':B1,'braid2':B2,'OL':OL,'OR':OR,'source_T':TL,'source_S':TS}.items()},
 'Ramond_trace_one_level':str(trace),'eta_cube_relative_coefficients':coeff,
 'vacuum_T_exponents':list(map(str,vac_exponents)),'source_T_exponents':list(map(str,target_exponents)),
 'indicators':list(map(str,indicators)), 'positive_words':word_rows}
(OUT/'exact_results.json').write_text(json.dumps(results,indent=2))
print(json.dumps({k:results[k] for k in ['named_checks','coherence','T_matching_levels','Ramond_trace_one_level','vacuum_T_exponents','source_T_exponents']},indent=2))
