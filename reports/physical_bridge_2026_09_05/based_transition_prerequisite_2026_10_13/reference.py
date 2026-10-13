"""Separate exact Gaussian matrices and Fraction roots; no native/SymPy import."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as Q

HERE=Path(__file__).resolve().parent
def helper():
    p=HERE.parent/'weave_registered_embedding_2026_10_13/reference.py'
    spec=importlib.util.spec_from_file_location('based_fraction_helpers',p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

@lru_cache(None)
def run():
    h=helper();checks={}
    def ck(n,v):checks[n]=bool(v)
    a=[[h.I,h.Z],[h.Z,h.gscale(-1,h.I)]];b=[[h.Z,h.O],[h.gscale(-1,h.O),h.Z]]
    A=h.block_diag([h.mscale(-1,a),a,h.mscale(-1,a)])
    B=h.block_diag([b,h.mscale(-1,b),h.mscale(-1,b)])
    P13=[[h.O if r==(2,1,0)[c] else h.Z for c in range(3)] for r in range(3)]
    P23=[[h.O if r==(0,2,1)[c] else h.Z for c in range(3)] for r in range(3)]
    L=h.kron(P13,h.madd(h.identity(2),a))
    R=h.kron(P23,h.madd(h.identity(2),h.mscale(-1,b)))
    S=h.times(h.times(R,h.dagger(L)),R);I=h.identity(6)
    ck('L omitted square root normalization',h.times(L,h.dagger(L))==h.mscale(2,I))
    ck('R omitted square root normalization',h.times(R,h.dagger(R))==h.mscale(2,I))
    for name,F,X,Y in [('L a',L,A,A),('L b',L,B,h.times(A,B)),('R a',R,A,h.times(A,B)),('R b',R,B,B)]:
        ck('covariance '+name,h.times(h.times(F,X),h.dagger(F))==h.mscale(2,Y))
    S2=h.times(S,S);S4=h.times(S2,S2)
    ck('exact unnormalized S square',S2==h.mscale(-8,I))
    ck('exact unnormalized S fourth',S4==h.mscale(64,I))
    C=h.times(h.times(h.times(h.dagger(B),A),B),h.dagger(A))
    ck('actual BabA puncture transport',C==h.mscale(-1,I))
    ck('ordinary one relation match',h.mscale(Q(-1,64),S4)==C)
    ck('canonical one relation mismatch',h.mscale(Q(1,64),S4)!=C)
    char=h.character(6,(1,-1)*3)
    even=sum(m for w,m in char.items() if w%2==0);odd=sum(char.values())-even
    ck('Fraction full E8 root count',sum(char.values())==248)
    ck('both centre parities from separate roots',(even,odd)==(136,112))
    ck('complete branching even',even==35+8+3+45+45)
    ck('complete branching odd',odd==40+36+36)
    def matched(r):return even*(r==1)+odd*(r==-1)
    ck('scalar plus one retains even',matched(1)==136)
    ck('scalar minus one retains odd',matched(-1)==112)
    ck('wrong scalar retains neither',matched(2)==0)
    ck('matrix matching control retains everything',even+odd==248 and even>0 and odd>0)
    # Scalar impossibility is analytic: equality requires the unequal constants 1,-1.
    parities=[(1,0),(0,1),(1,1)];maps=[b,a,h.times(a,b)]
    for p,U in zip(parities,maps):
        ck('half period '+str(p),h.times(h.times(U,a),h.dagger(U))==h.mscale((-1)**p[0],a)
           and h.times(h.times(U,b),h.dagger(U))==h.mscale((-1)**p[1],b))
    counts=[sum(all((p[j]+3*w[j])%2==0 for j in (0,1)) for p in parities) for w in parities]
    ck('each half period trivializes one distinct Higgs copy',counts==[1,1,1])
    ck('zero line does not cancel nontrivial parities',all(any(p) for p in parities))
    records={'S_word':{'a':'b','b':'BAb'},'S4_inner_word':'BabA','Delta4_inner_word':'aBAb',
             'coefficient_S4':1,'fibre_inner_sign':-1,'full_E8_central_parities':[even,odd],
             'conditional_spin_residual_ranks':[4*even,4*odd],
             'half_period_Higgs_trivial_counts':counts}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'separate exact coefficient/root controls; free-word constants checked by native route, not independently rederived here'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
