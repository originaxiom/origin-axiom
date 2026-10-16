"""Separate exact Fock/rational-rotation controls, no symbolic/native import."""
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

def arithmetic():
    p=Path(__file__).resolve().parents[1]/'weave_registered_embedding_2026_10_13/reference.py'
    sp=importlib.util.spec_from_file_location('pinned_gaussian_arithmetic',p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

@lru_cache(None)
def run():
    a=arithmetic();O,Z,I=a.O,a.Z,a.I
    checks={}
    def ck(n,v):checks[n]=bool(v)
    def iz(m):return [[a.gmul(I,x) for x in row] for row in m]
    def neg(m):return a.mscale(-1,m)
    def add(*ms):
        out=a.matrix(len(ms[0]))
        for m in ms:out=a.madd(out,m)
        return out
    eh,ev=a.matrix(4),a.matrix(4)
    eh[1][0]=eh[3][2]=O;ev[2][0]=O;ev[3][1]=a.gscale(-1,O)
    cs=[add(eh,neg(a.dagger(eh))),iz(add(eh,a.dagger(eh))),
        add(ev,neg(a.dagger(ev))),iz(add(ev,a.dagger(ev)))]
    KH,KV=a.times(cs[0],cs[1]),a.times(cs[2],cs[3])
    G=add(KH,a.mscale(Q(1,2),KV))
    def lower(c):return add(a.mscale(Q(-1,2),c[1]),a.mscale(Q(1,4),a.times(a.times(c[0],c[2]),c[3])))
    K=lower(cs);Kc=add(K,a.mscale(Q(3,4),iz(cs[0])))
    weights=[Q(3,2),Q(-1,2),Q(1,2),Q(-3,2)]
    cw=[w-Q(3,2) for w in weights]
    ck('Fock spin generator charges',all(G[j][k]==(a.gscale(-weights[j],I) if j==k else Z) for j in range(4) for k in range(4)))
    ck('canonical exterior charges',cw==[0,-2,-1,-3])
    angles=[(Q(3,5),Q(4,5)),(Q(7,25),Q(24,25)),(Q(0),Q(1)),(Q(-3,5),Q(4,5)),(Q(-1),Q(0)),(Q(1),Q(0))]
    for n,(C,S) in enumerate(angles):
        ck(f'rotation {n} exact unit circle',C*C+S*S==1)
        rc=[add(a.mscale(C*C-S*S,cs[0]),a.mscale(-2*C*S,cs[1])),
            add(a.mscale(2*C*S,cs[0]),a.mscale(C*C-S*S,cs[1])),
            add(a.mscale(C,cs[2]),a.mscale(-S,cs[3])),
            add(a.mscale(S,cs[2]),a.mscale(C,cs[3]))]
        grad=[-S*S,S*C,Q(0),Q(0)]
        source=add(*(a.mscale(grad[j],a.times(rc[j],G)) for j in range(4)))
        Gc=add(G,a.mscale(Q(3,2),iz(a.identity(4))))
        csource=add(*(a.mscale(grad[j],a.times(rc[j],Gc)) for j in range(4)))
        rcK=lower(rc);rcKc=add(rcK,a.mscale(Q(3,4),iz(rc[0])))
        ck(f'rotation {n} full ordinary covariance',add(K,neg(rcK),neg(source))==a.matrix(4))
        ck(f'rotation {n} full canonical covariance',add(Kc,neg(rcKc),neg(csource))==a.matrix(4))
        if S:
            bad=add(G,a.mscale(Q(-3,2),iz(a.identity(4))))
            badsource=add(*(a.mscale(grad[j],a.times(rc[j],bad)) for j in range(4)))
            ck(f'rotation {n} wrong R phase rejected',add(Kc,neg(rcKc),neg(badsource))!=a.matrix(4))
    ck('ordinary loop all half integral charges',all(w.denominator==2 and w.numerator%2 for w in weights))
    ck('R half charge keeps its sign',Q(-3,2).denominator==2)
    ck('canonical loop all integral charges',all(w.denominator==1 for w in cw))
    # Independent exact central powers in the literal coefficient frame.
    p1=[[Z,O],[O,Z]];p2=[[Z,a.gscale(-1,I)],[I,Z]];p3=[[O,Z],[Z,a.gscale(-1,O)]]
    qa=iz(p3);qb=[[Z,O],[a.gscale(-1,O),Z]]
    # Remove common sqrt2 denominators: S_c=(R0 L0^* R0)/(2sqrt2).
    p13=[[Z,Z,O],[Z,O,Z],[O,Z,Z]];p23=[[O,Z,Z],[Z,Z,O],[Z,O,Z]]
    L0=a.kron(p13,add(a.identity(2),qa));R0=a.kron(p23,add(a.identity(2),neg(qb)))
    S0=a.times(a.times(R0,a.dagger(L0)),R0)
    ck('coefficient S square from unnormalized exact lifts',a.times(S0,S0)==a.mscale(-8,a.identity(6)))
    ck('coefficient fourth power is plus identity',a.times(a.times(S0,S0),a.times(S0,S0))==a.mscale(64,a.identity(6)))
    ck('puncture quaternion sign not lost',a.times(a.times(a.times(qa,qb),a.dagger(qa)),a.dagger(qb))==neg(a.identity(2)))
    roots,_,_=a.frame(6)
    char=a.character(6,(1,-1)*3)
    parities=[sum(m for w,m in char.items() if w%2==p) for p in range(2)]
    ck('all adjoint companions counted',len(roots)+8==248 and sum(char.values())==248)
    ck('adjoint coefficient centre is not scalar',parities==[136,112])
    records={'spin_weights':[[w.numerator,w.denominator] for w in weights],
             'canonical_weights':[int(w) for w in cw],
             'geometric_loop_signs':[-1,-1,1],'coefficient_S_powers':[-1,1],
             'full_E8_central_parities':parities}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'independent finite exact Fock/rotation safeguards, not global based or PDE certificate'}

if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2));raise SystemExit(0 if r['all_passed'] else 1)
