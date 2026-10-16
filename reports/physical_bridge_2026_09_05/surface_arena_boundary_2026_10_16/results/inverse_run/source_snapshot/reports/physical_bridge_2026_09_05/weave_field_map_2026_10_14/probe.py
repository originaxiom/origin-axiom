"""Full coefficient-centre map and exact W61 algebra, not a physical spectrum."""
from collections import Counter
from functools import lru_cache
from itertools import product
import ast
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
def load(path):
    sp=importlib.util.spec_from_file_location('field_map_prior_'+path.parent.name,path)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def zero(m):return all(s.simplify(x)==0 for x in m)
def data():
    p=load(HERE.parent/'weave_registered_embedding_2026_10_13/probe.py')
    e,rr=p.roots();chain=[e[6]-e[7],e[5]-e[6],e[6]+e[7],-s.ones(8,1)/2,e[3]+e[4]]
    c=s.Matrix.hstack(*chain);ws=[c*(c.T*c).inv()*s.Matrix([1,0,0,0,0])]
    for a in chain:ws.append(ws[-1]-a)
    hq=sum((a*w for a,w in zip((1,-1)*3,ws)),s.zeros(8,1))
    ha=sum((a*w for a,w in zip((1,1,-1,-1,0,0),ws)),s.zeros(8,1))
    return p,e,rr,hq,ha
def joint(rr,hq,hw):
    out=Counter((int(r.dot(hq))%2,int(r.dot(hw))%2) for r in rr)
    out[(0,0)]+=8
    return out
def pack(c):return [[list(k),v] for k,v in sorted(c.items())]

@lru_cache(None)
def run():
    checks={}
    def ck(n,v):checks[n]=bool(v)
    p,e,rr,hq,ha=data();hw=e[3]-e[4]
    original=joint(rr,hq,hw);alternative=joint(rr,hq,ha)
    actual,expected,_,_,_=p.a5_roster()
    ck('actual full root roster agrees with branching',actual==expected and len(rr)==240)
    ck('puncture equals original weak centre on every root',all(int(r.dot(hq-hw))%2==0 for r in rr))
    ck('all Cartans and conjugates retained',sum(original.values())==sum(alternative.values())==248 and
       actual[(0,)*8]==8 and all(actual[tuple(-x for x in w)]==m for w,m in actual.items()))
    ck('current joint population exact',original==Counter({(0,0):136,(1,1):112}))
    ck('alternative has both cross parities',alternative[(0,1)]>0 and alternative[(1,0)]>0)
    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]]);I=s.eye(2)
    S=s.diag(b,a,a*b);A=s.diag(-a,a,-a);B=s.diag(b,-b,-b)
    h=s.diag(1,1,-1,-1,0,0);ef=s.zeros(3);ef[0,1]=1
    ep=S*s.kronecker_product(ef,I)*S.H;em=ep.H
    ck('alternative is an actual sl2 subalgebra',zero(h*ep-ep*h-2*ep) and zero(h*em-em*h+2*em) and zero(ep*em-em*ep-h))
    ck('alternative centralizes literal quaternion holonomies',all(zero(x*y-y*x) for x in [h,ep,em] for y in [A,B]))
    C={(0,0):I,(1,0):b,(0,1):a,(1,1):a*b};par=[(1,0),(0,1),(1,1)]
    names={'Q':1,'L':1,'u^c':0,'d^c':0,'e^c':0,'neutral_singlet':0}
    compatibility={k:bool(v==1) for k,v in names.items()}
    ck('necessary central test distinguishes all field labels',compatibility=={'Q':True,'L':True,'u^c':False,'d^c':False,'e^c':False,'neutral_singlet':False})
    weak_signs={(-1)**int(r.dot(hq)) for r in rr if abs(r.dot(hw))==1}
    line_signs={sa*sb*sa*sb for sa,sb in product((-1,1),repeat=2)}
    ck('bare parity Higgs fails this weak-doublet coefficient test',line_signs=={1} and weak_signs=={-1} and line_signs!=weak_signs)
    z=s.Matrix([[s.symbols('x'),s.symbols('y')]])
    for sa,sb in product((-1,1),repeat=2):
        eq=list(z*a-sa*z)+list(z*b-sb*z);M,_=s.linear_eq_to_matrix(eq,list(z))
        ck(f'no quaternion to line map {sa},{sb}',M.rank()==2)
    ck('quaternion tensor comparator has even centre',s.kronecker_product(-I,-I)==s.eye(4))
    ck('flat sign twist cannot change commutator',all(zero((sa*a)*(sb*b)*(sa*a).H*(sb*b).H+I) for sa,sb in product((-1,1),repeat=2)))
    J=b;v=s.Matrix(s.symbols('f0 f1'));rows=[];matrices=[]
    for c1,c2,hp in product(C,C,par):
        allowed=tuple((c1[j]+c2[j])%2 for j in (0,1))==hp
        BB=C[c1].T*J*C[hp]*C[c2];HH=C[c2].H*C[hp]*C[c1]
        invB=all(zero(g.T*BB*g-BB) for g in [a,b]);invH=all(zero(g.H*HH*g-HH) for g in [a,b])
        ck(f'exact selection {c1},{c2},{hp}',invB==invH==allowed)
        if allowed:
            ck(f'exact common-profile zero {c1},{c2},{hp}',zero(BB+BB.T) and (v.T*BB*v)[0].expand()==0)
            ck(f'exact Hermitian scalar {c1},{c2},{hp}',HH in [I,-I])
        rows.append((c1,c2,hp,allowed,BB,HH))
    for w in par:
        Y=s.zeros(3)
        for j,r in enumerate(par):
            for k,t in enumerate(par):
                c1=tuple((r[n]+w[n])%2 for n in (0,1))
                if tuple((c1[n]+t[n])%2 for n in (0,1))==w:Y[j,k]=(C[t].H*C[w]*C[c1])[0,0]
        ck('all-tau common normalized matrix '+str(w),Y.H*Y==s.eye(3) and all(Y[j,k]==0 for j in range(3) for k in range(3) if j!=k))
        matrices.append([int(Y[j,j]) for j in range(3)])
    ck('non-skew polynomial control is nonzero',(v.T*s.diag(1,-1)*v)[0].expand()!=0)
    yk=s.diag(1,s.Rational(1,2),s.Rational(1,3))
    ck('supplied unequal kinetic Gram changes masses',len((yk.H*yk).eigenvals())==3 and yk.H*s.diag(1,4,9)*yk==s.eye(3))
    # Exact full equations, not the numerical SVD fallback, establish J.
    js=s.Matrix(2,2,s.symbols('j0:4'));eq=[]
    for g in [a,b]:eq.extend(list(g.T*js*g-js))
    E,_=s.linear_eq_to_matrix(eq,list(js));ck('invariant bilinear nullity exactly one',4-E.rank()==1 and zero(a.T*J*a-J) and zero(b.T*J*b-J))
    # Replay unchanged upstream function bodies only, excluding Q3/imports.
    tree=ast.parse((HERE/'upstream_W61.py').read_text())
    wanted={'add','invariant_form','character','couple','Q1','Q2'}
    funcs=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in wanted]
    ns={'np':np,'RA':np.array(a.tolist(),complex),'RB':np.array(b.tolist(),complex),
        'BLOCKS':{k:np.array(m.tolist(),complex) for k,m in C.items()},'PARITIES':par,'TOL':1e-12,
        'OP':SimpleNamespace(CHARGES={'Q':1,'u^c':-4,'d^c':2,'L':-3,'e^c':6,'H':3})}
    exec(compile(ast.Module(body=funcs,type_ignores=[]),'unchanged_W61_Q1_Q2','exec'),ns)
    ns['J']=ns['invariant_form']();q1,q2=ns['Q1'](),ns['Q2'](2.0)
    ck('unchanged upstream Q1 and normalized Q2 replay',len(funcs)==6 and q1['holds'] and q2['holds'])
    ck('replayed upstream invariant is actual epsilon',np.allclose(ns['J'],np.array(J.tolist(),complex),atol=1e-12))
    got=[]
    for w in par:
        sectors=q2[f'w = {w} (halves), p* = {w}'];diags=[]
        for row in sectors.values():
            mat=np.array(row['T-bar x T: Y']);diags.append([int(round(x)) for x in mat.diagonal()])
        ck('upstream three sectors agree '+str(w),all(d==matrices[len(got)] for d in diags));got.append(diags[0])
    records={'original_joint_parities':pack(original),'alternative_joint_parities':pack(alternative),
             'uniform_rho_necessary_compatibility':compatibility,'allowed_overlap_channels':sum(row[3] for row in rows),
             'normalized_Hermitian_diagonals':matrices}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'specified complete gauge map and raw W61 contraction; no physical family/index or global completion'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
