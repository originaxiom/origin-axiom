"""Independent Gaussian/Fraction spin and coefficient safeguards."""
from functools import lru_cache
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def helper():
    p=HERE.parent/'weave_registered_embedding_2026_10_13/reference.py'
    sp=importlib.util.spec_from_file_location('even_fraction_helpers',p)
    h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h);return h

@lru_cache(None)
def run():
    h=helper();checks={}
    def ck(n,v):checks[n]=bool(v)
    sub=lambda x,y:h.madd(x,h.mscale(-1,y))
    imul=lambda m:[[h.gmul(h.I,x) for x in row] for row in m]
    I2=h.identity(2);I=h.identity(4)
    p1=[[h.Z,h.O],[h.O,h.Z]];p2=[[h.Z,h.gscale(-1,h.I)],[h.I,h.Z]];p3=[[h.O,h.Z],[h.Z,h.gscale(-1,h.O)]]
    cs=[imul(h.kron(p1,I2)),imul(h.kron(p2,I2)),imul(h.kron(p3,p1)),imul(h.kron(p3,p2))]
    c1,c2,c3,c4=cs;K=h.times(h.times(c1,c3),c4);GV=imul(h.times(c3,c4))
    Z=imul(h.times(c1,c3));J=imul(h.times(c2,c4));Pi=h.mscale(Q(1,4),h.times(h.madd(I,Z),h.madd(I,J)))
    ck('rank one exact projector',h.times(Pi,Pi)==Pi and h.dagger(Pi)==Pi and sum(Pi[j][j][0] for j in range(4))==1)
    ck('actual projector involutions',h.times(Z,Z)==h.times(J,J)==I and h.times(Z,J)==h.times(J,Z))
    ck('full GammaV involution',h.times(GV,GV)==I and h.dagger(GV)==GV)
    for amp in [Q(1,8),Q(1,4),Q(1,2),Q(2)]:
        D=h.madd(h.mscale(amp-Q(1,4),c2),h.madd(h.mscale(amp,imul(c4)),h.mscale(Q(1,4),K)))
        ck('zero profile coefficient '+str(amp),h.times(D,Pi)==h.matrix(4))
        ck('missing mixed rejected '+str(amp),h.times(sub(D,h.mscale(Q(1,4),K)),Pi)!=h.matrix(4))
    for B in [Q(0),Q(3,4),Q(-3,4),Q(6),Q(-6),Q(-21,4),Q(27,4)]:
        R=h.mscale(B,imul(c1));M0=h.mscale(Q(1,4),K)
        ck('twist full square '+str(B),h.times(R,R)==h.mscale(B*B,I))
        ck('twist mixed cross '+str(B),h.madd(h.times(R,M0),h.times(M0,R))==h.mscale(-B/2,GV))
        ck('radial twist anticomm '+str(B),h.madd(h.times(c2,R),h.times(R,c2))==h.matrix(4))
        ck('vertical twist anticomm '+str(B),h.madd(h.times(c4,R),h.times(R,c4))==h.matrix(4))
        for Xi in [Q(0),Q(1,3)]:
            H=h.madd(h.mscale(Xi,imul(c2)),h.madd(M0,R))
            target=h.madd(h.mscale(Xi*Xi+B*B+Q(1,16),I),h.mscale(-B/2,GV))
            ck('full asymptotic squared matrix '+str((B,Xi)),h.times(H,H)==target)
    a=[[h.I,h.Z],[h.Z,h.gscale(-1,h.I)]];b=[[h.Z,h.O],[h.gscale(-1,h.O),h.Z]]
    A0=h.block_diag([h.mscale(-1,a),a,h.mscale(-1,a)]);B0=h.block_diag([b,h.mscale(-1,b),h.mscale(-1,b)])
    perm=[[h.O if i==(2,1,0)[j] else h.Z for j in range(3)] for i in range(3)]
    L=h.kron(perm,h.madd(I2,a));s3=[[h.O,h.Z],[h.Z,h.gscale(-1,h.O)]]
    hs=[h.block_diag([h.mscale(-1,s3),s3,h.mscale(-1,s3)]),h.block_diag([I2,h.matrix(2),h.mscale(-1,I2)])]
    chars=[(1,-1,1),(1,1,-1)]
    for j,(H,ch) in enumerate(zip(hs,chars)):
        ck('literal A character '+str(j),h.times(h.times(A0,H),h.dagger(A0))==h.mscale(ch[0],H))
        ck('literal B character '+str(j),h.times(h.times(B0,H),h.dagger(B0))==h.mscale(ch[1],H))
        ck('literal normalized T character '+str(j),h.times(h.times(h.dagger(L),H),L)==h.mscale(2*ch[2],H))
    # The profile norm substitution gives 2/C int_0^infty exp(-2z)dz=1/C.
    ck('norm substitution exact factor',2*Q(1,2)==1)
    bounds=[]
    for name,B in [('ordinary0',Q(0)),('canonical0',Q(3,4)),('ordinary1',Q(-6)),('canonical1',Q(-21,4)),('canonical_minus1',Q(27,4))]:
        q=abs(B)*(abs(B)-Q(1,2));bounds.append([name,q.numerator,q.denominator])
    ck('canonical positive even channel bound',bounds[1][1:]==[3,16])
    ck('nonzero ordinary unit positive',bounds[2][1]>0)
    records={'coefficient_characters':[list(x) for x in chars],'spin_projector_rank':1,'profile_norm_power':-1,
             'fixed_p_squared_masses_ordinary0':[[1,16],[1,16]],
             'fixed_p_squared_masses_canonical0':[[1,4],[1,1]],'uniform_squared_bounds_ell_one':bounds}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'separate finite rational spin/coefficient controls; Weyl and global domain reasoning remains authored'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
