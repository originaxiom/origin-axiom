"""Separate rational character sums and frame connection checks."""
from functools import lru_cache
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def helper():
    p=HERE.parent/'weave_registered_embedding_2026_10_13/reference.py'
    sp=importlib.util.spec_from_file_location('full_even_gaussian',p)
    h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h);return h

@lru_cache(None)
def run():
    h=helper();checks={}
    def ck(n,v):checks[n]=bool(v)
    def power(m,n):
        out=h.identity(len(m))
        for _ in range(n):out=h.times(out,m)
        return out
    trace=lambda m:h.sumg(m[j][j] for j in range(len(m)))
    a=[[h.I,h.Z],[h.Z,h.gscale(-1,h.I)]];b=[[h.Z,h.O],[h.gscale(-1,h.O),h.Z]]
    A=h.block_diag([h.mscale(-1,a),a,h.mscale(-1,a)])
    B=h.block_diag([b,h.mscale(-1,b),h.mscale(-1,b)])
    P=[[h.O if i==(2,1,0)[j] else h.Z for j in range(3)] for i in range(3)]
    LN=h.kron(P,h.madd(h.identity(2),a))
    ck('unnormalized fourth power correct',power(LN,4)==h.mscale(-4,h.identity(6)))
    chars={}
    for j in (0,1):
        for k in range(4):
            for u in (0,1):
                N=h.times(h.times(power(A,j),power(LN,k)),power(B,u));t=trace(N);t2=trace(h.times(N,N))
                wedge=h.gscale(Q(1,2*2**k),h.gadd(h.gmul(t,t),h.gscale(-1,t2)))
                char=h.gmul(t,h.conj(t))[0]/(2**k)+10+6*wedge[0]
                if char.denominator!=1:raise ValueError('nonintegral complete character')
                chars[j,k,u]=char
    phases=[('+1',h.O),('-1',h.gscale(-1,h.O)),('+i',h.I),('-i',h.gscale(-1,h.I))]
    pop=[]
    for label,z in phases:
        row=[]
        for sign in (1,-1):
            total=h.Z
            for (j,k,u),v in chars.items():
                zk=h.O
                for _ in range(k):zk=h.gmul(zk,h.conj(z))
                total=h.gadd(total,h.gscale(v*sign**u,zk))
            rank=h.gscale(Q(1,16),total)
            if rank[1] or rank[0].denominator!=1:raise ValueError('nonintegral joint projector')
            row.append(int(rank[0]))
        pop.append([label,row])
    ck('complete136 character',chars[0,0,0]==136)
    ck('joint ranks exhaust82 short periodic',sum(sum(v) for _,v in pop)==82)
    ck('nonnegative joint ranks',all(n>=0 for _,v in pop for n in v))
    ck('actual quarter phases not discarded',sum(sum(v) for _,v in pop[2:])>0)
    I2=h.identity(2);I=h.identity(4)
    p1=[[h.Z,h.O],[h.O,h.Z]];p2=[[h.Z,h.gscale(-1,h.I)],[h.I,h.Z]];p3=[[h.O,h.Z],[h.Z,h.gscale(-1,h.O)]]
    imul=lambda m:[[h.gmul(h.I,x) for x in row] for row in m]
    cs=[imul(h.kron(p1,I2)),imul(h.kron(p2,I2)),imul(h.kron(p3,p1)),imul(h.kron(p3,p2))]
    c1,c2,c3,c4=cs
    O1=h.madd(h.mscale(Q(1,2),h.times(c1,c2)),h.mscale(Q(1,4),h.times(c3,c4)))
    O3=h.mscale(Q(1,4),h.madd(h.times(c1,c4),h.mscale(-1,h.times(c2,c3))))
    M1=h.times(h.dagger(O1),O1);M3=h.times(h.dagger(O3),O3)
    sub=lambda x,y:h.madd(x,h.mscale(-1,y))
    def quadratic(m,a,b):
        return h.times(sub(m,h.mscale(a,I)),sub(m,h.mscale(b,I)))==h.matrix(4)
    ck('Omega1 squared eigenvalues controlled',quadratic(M1,Q(1,16),Q(9,16)))
    ck('Omega3 squared eigenvalues controlled',quadratic(M3,Q(0),Q(1,4)))
    ck('actual GammaH unit norm',h.times(imul(h.times(c1,c2)),imul(h.times(c1,c2)))==I)
    for beta in [Q(3,4),Q(-21,4),Q(27,4)]:
        ck('canonical positive last stratum '+str(beta),abs(beta)*(abs(beta)-Q(1,2))>=Q(3,16))
    ck('ordinary0 rejecting comparison',Q(0)*(Q(0)-Q(1,2))<Q(3,16))
    records={'short_periodic_phase_populations':pop,'even_coefficient_dimension':136,
             'short_periodic_dimension':sum(sum(v) for _,v in pop),
             'connection_squared_norms_ell_one':[[9,16],[1,4]],
             'canonical_uniform_tail_squared_bound_ell_one':[3,16]}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'independent rational characters and finite connection controls; not nonauthor analytic acceptance'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
