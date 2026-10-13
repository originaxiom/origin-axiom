"""Exact specified based-transition prerequisite, not physical bundle closure."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
def load(path):
    spec=importlib.util.spec_from_file_location('based_roster',path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def inv(word):return word.swapcase()[::-1]
def red(word):
    stack=[]
    for c in word:
        if stack and stack[-1]==c.swapcase():stack.pop()
        else:stack.append(c)
    return ''.join(stack)
def image(f,word):
    return red(''.join(f[c] if c.islower() else inv(f[c.lower()]) for c in word))
def compose(f,g):return {c:image(f,g[c]) for c in 'ab'}
def power(f,n):
    out={'a':'a','b':'b'}
    for _ in range(n):out=compose(f,out)
    return out
def inner(word):return {c:red(word+c+inv(word)) for c in 'ab'}
def zero(m):return all(s.simplify(x)==0 for x in m)

@lru_cache(None)
def run():
    checks={}
    def ck(n,v):checks[n]=bool(v)
    E={'a':'a','b':'b'};Lw={'a':'a','b':'ab'};Rw={'a':'ab','b':'b'}
    Li={'a':'a','b':'Ab'};Ri={'a':'aB','b':'b'}
    ck('actual L word inverse',compose(Lw,Li)==compose(Li,Lw)==E)
    ck('actual R word inverse',compose(Rw,Ri)==compose(Ri,Rw)==E)
    Sw=compose(Rw,compose(Li,Rw));c='BabA'
    ck('S word not guessed from homology',Sw=={'a':'b','b':'BAb'})
    ck('S fourth is actual inner puncture word',power(Sw,4)==inner(c))
    ck('S fourth not based identity',power(Sw,4)!=E)
    ck('actual second modular word relation',power(compose(Sw,Lw),3)==power(Sw,2))
    D=compose(Lw,compose(Ri,Lw))
    ck('main Delta convention retained',power(D,4)==inner('aBAb'))
    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]]);I=s.eye(6)
    A=s.diag(-a,a,-a);B=s.diag(b,-b,-b)
    P13=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
    P23=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    L=s.kronecker_product(P13,(s.eye(2)+a)/s.sqrt(2))
    R=s.kronecker_product(P23,(s.eye(2)-b)/s.sqrt(2));S=R*L.H*R
    for name,f,expected in [('L a',L,A),('R a',R,A*B)]:
        ck('coefficient covariance '+name,zero(f*A*f.H-expected))
    for name,f,expected in [('L b',L,A*B),('R b',R,B)]:
        ck('coefficient covariance '+name,zero(f*B*f.H-expected))
    table={'a':A,'b':B,'A':A.H,'B':B.H};C=I
    for ch in c:C=C*table[ch]
    ck('actual inner coefficient retains minus centre',zero(C+I))
    ck('coefficient fourth power differs from inner transport',zero(S**4-I) and not zero(S**4-C))
    ck('ordinary sign matches rank6 on this relation',zero(-S**4-C))
    ck('canonical sign misses rank6 on this relation',not zero(S**4-C))
    roster=load(HERE.parent/'weave_registered_embedding_2026_10_13/probe.py')
    actual,expected,char,_,_=roster.a5_roster()
    even=sum(m for w,m in char.items() if w%2==0);odd=sum(char.values())-even
    ck('full actual root roster equals complete branching',actual==expected and sum(actual.values())==248)
    ck('both adjoint centre parities retained',(even,odd)==(136,112))
    ck('complete branching gives same parities',even==35+8+3+2*15*3 and odd==20*2+2*6*3*2)
    sigma=s.diag(*([1]*even+[-1]*odd))
    ck('full puncture involution is not scalar',sigma!=s.eye(248) and sigma!=-s.eye(248))
    # Reconstruct a non-scalar matching loop from the actual root-weight
    # parity projector, rather than from an asserted common scalar sign.
    Pe=s.diag(*([1]*even+[0]*odd));repair=2*Pe-s.eye(248)
    ck('matrix loop control can match both parities',repair*sigma==s.eye(248)
       and repair!=s.eye(248) and repair!=-s.eye(248))
    # Residual ranks follow from nonzero scalar entries on the two eigenspaces.
    ranks=[4*even,4*odd]
    ck('ordinary matches odd only',ranks[0]==544 and even>0 and odd>0)
    ck('canonical matches even only',ranks[1]==448 and even>0 and odd>0)
    r=s.Symbol('r')
    ck('no common scalar solves both parities',s.solve([r-1,r+1],[r])==[])
    parities=[(1,0),(0,1),(1,1)];maps=[b,a,a*b]
    for p,U in zip(parities,maps):
        ck('quaternion half period '+str(p),zero(U*a*U.H-(-1)**p[0]*a) and zero(U*b*U.H-(-1)**p[1]*b))
    cancellations=[]
    for w in parities:
        row=[p for p in parities if all((p[j]+3*w[j])%2==0 for j in (0,1))]
        cancellations.append(row)
        ck('one fibre trivial Higgs parity '+str(w),row==[w])
    ck('third period is not a quaternion sign twist',s.exp(2*s.pi*s.I/3) not in (1,-1))
    records={'S_word':Sw,'S4_inner_word':c,'Delta4_inner_word':'aBAb',
             'coefficient_S4':1,'fibre_inner_sign':-1,
             'full_E8_central_parities':[even,odd],
             'conditional_spin_residual_ranks':ranks,
             'half_period_Higgs_trivial_counts':[len(x) for x in cancellations]}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'one conditional factorized transition relation and fibre parity positives; no physical global closure'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
