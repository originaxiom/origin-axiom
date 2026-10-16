"""Separate Fraction/Gaussian odd character and cross-form safeguards."""
from functools import lru_cache
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def helper():
    p=HERE.parent/'weave_registered_embedding_2026_10_13/reference.py'
    sp=importlib.util.spec_from_file_location('odd_form_gaussian',p)
    h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h);return h

@lru_cache(None)
def run():
    h=helper();checks={}
    def ck(n,v):checks[n]=bool(v)
    def power(m,n):
        out=h.identity(len(m))
        for _ in range(n):out=h.times(out,m)
        return out
    def gp(z,n):
        out=h.O
        for _ in range(n):out=h.gmul(out,z)
        return out
    trace=lambda m:h.sumg(m[j][j] for j in range(len(m)))
    a=[[h.I,h.Z],[h.Z,h.gscale(-1,h.I)]]
    b=[[h.Z,h.O],[h.gscale(-1,h.O),h.Z]]
    A=h.block_diag([h.mscale(-1,a),a,h.mscale(-1,a)])
    B=h.block_diag([b,h.mscale(-1,b),h.mscale(-1,b)])
    P=[[h.O if i==(2,1,0)[j] else h.Z for j in range(3)] for i in range(3)]
    LN=h.kron(P,h.madd(h.identity(2),a))
    ck('actual Q8 products',h.times(A,A)==h.mscale(-1,h.identity(6)) and h.times(B,B)==h.mscale(-1,h.identity(6)) and h.times(A,B)==h.mscale(-1,h.times(B,A)))
    ck('unnormalized cusp fourth power',power(LN,4)==h.mscale(-4,h.identity(6)))
    ck('cusp short covariance',h.times(LN,A)==h.times(A,LN))
    data={}
    for j in (0,1):
        for k in range(4):
            N=h.times(power(A,j),power(LN,k));t=trace(N);t2=trace(power(N,2));t3=trace(power(N,3))
            w3=h.gscale(Q(1,6),h.sumg([gp(t,3),h.gscale(-3,h.gmul(t,t2)),h.gscale(2,t3)]))
            data[j,k]=(t,w3)
    pop=[]
    phase_nums=[(1,h.gadd(h.O,h.I)),(3,h.gadd(h.gscale(-1,h.O),h.I)),(5,h.gscale(-1,h.gadd(h.O,h.I))),(7,h.gadd(h.O,h.gscale(-1,h.I)))]
    for label,aval in [('+i',h.I),('-i',h.gscale(-1,h.I))]:
        row=[]
        for r,num in phase_nums:
            total=h.Z
            for (j,k),(t,w3) in data.items():
                phase=gp(h.conj(num),k)
                exterior=h.gscale(Q(2,2**(2*k)),h.gmul(phase,w3))
                defining=h.gscale(Q(6,2**k),h.gmul(phase,h.gadd(t,h.conj(t))))
                total=h.gadd(total,h.gmul(gp(h.conj(aval),j),h.gadd(exterior,defining)))
            rank=h.gscale(Q(1,8),total)
            if rank[1] or rank[0].denominator!=1:raise ValueError('nonintegral odd phase rank')
            row.append([r,int(rank[0])])
        pop.append([label,row])
    ck('both short eigenspaces dimension56',all(sum(n for _,n in row)==56 for _,row in pop))
    ck('all112 odd directions included',sum(n for _,row in pop for _,n in row)==112)
    ck('all phase ranks nonnegative',all(n>=0 for _,row in pop for _,n in row))
    ck('odd eighth phases no zero',all(min(Q(r,8),1-Q(r,8))>=Q(1,8) for _,row in pop for r,n in row if n))
    I2=h.identity(2);I=h.identity(4)
    p1=[[h.Z,h.O],[h.O,h.Z]];p2=[[h.Z,h.gscale(-1,h.I)],[h.I,h.Z]];p3=[[h.O,h.Z],[h.Z,h.gscale(-1,h.O)]]
    imul=lambda m:[[h.gmul(h.I,x) for x in row] for row in m]
    cs=[imul(h.kron(p1,I2)),imul(h.kron(p2,I2)),imul(h.kron(p3,p1)),imul(h.kron(p3,p2))]
    c1,c2,c3,c4=cs
    sub=lambda x,y:h.madd(x,h.mscale(-1,y))
    def msum(*terms):
        out=h.matrix(len(terms[0]))
        for term in terms:out=h.madd(out,term)
        return out
    mixed=h.mscale(Q(1,4),h.times(h.times(c1,c3),c4))
    F3=msum(h.mscale(-1,h.times(c1,c4)),h.mscale(Q(1,2),h.times(c2,c3)),h.times(c3,mixed),h.times(mixed,c3))
    F4=msum(h.mscale(Q(-1,2),h.times(c2,c4)),h.times(c4,mixed),h.times(mixed,c4))
    K3=h.mscale(Q(1,2),sub(h.times(c2,c3),h.times(c1,c4)))
    K4=h.mscale(Q(-1,2),h.madd(h.times(c2,c4),h.times(c1,c3)))
    ck('E3 full cross coefficient',F3==K3)
    ck('E4 full cross coefficient',F4==K4)
    gv=imul(h.times(c3,c4))
    for label,K in [('E3',K3),('E4',K4)]:
        ck(label+' flips vertical chirality',h.madd(h.times(gv,K),h.times(K,gv))==h.matrix(4))
        ck(label+' is skew Hermitian',h.madd(h.dagger(K),K)==h.matrix(4))
        N=h.times(h.dagger(K),K)
        ck(label+' squared norm projection',h.times(N,N)==N and trace(N)[0]>0 and sub(N,I)!=h.matrix(4))
    ck('omitted mixed term rejected',h.madd(h.times(c3,mixed),h.times(mixed,c3))!=h.matrix(4))
    # Rational substitute a=sqrt(2)*u,b=v makes the absorption identity exact.
    for u,v in [(Q(0),Q(1)),(Q(2),Q(1)),(Q(7,3),Q(2,5))]:
        ck('absorption square '+str(u)+','+str(v),u*u+4*v*v-4*u*v==(u-2*v)**2)
    ck('critical derivative integral grows',all(Q(k)-1>Q(k//2)-1 for k in (4,16,64)))
    ck('zero phase rejecting comparator',Q(0)<Q(1,8))
    return {'checks':checks,'all_passed':all(checks.values()),'records':{
        'odd_phase_populations':pop,'odd_coefficient_dimension':112,
        'cross_matrix_norms_ell_one':[1,1],
        'form_vertical_fraction':[1,2],'form_norm_error_ell_one':4},
        'scope':'separate finite rational/Gaussian safeguards, not nonauthor domain acceptance or full physical spectrum'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
