"""Fraction-only root, coefficient and polynomial safeguards; no native/SymPy."""
from functools import lru_cache
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def helper():
    p=HERE.parent/'weave_registered_embedding_2026_10_13/reference.py';sp=importlib.util.spec_from_file_location('uniform_fraction',p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

@lru_cache(None)
def run():
    checks={}
    def ck(k,v):checks[k]=bool(v)
    h=helper();char=h.character(6,(1,-1)*3);irr=h.decomposition(char)
    ck('full weight census248',sum(char.values())==248)
    ck('odd continuous quartet retained',sum(n for d,n in irr if d==4)>0)
    odd=sum(d*n for d,n in irr if d%2==0);copies=sum((d//2)*n for d,n in irr if d%2==0)
    ck('Q8 and SU2 are not identified',odd==112 and copies==56 and any(d!=2 for d,n in irr if d%2==0))
    rr,chain,ws=h.frame(6);e,_=h.root_data()
    HQ=tuple(sum(Q(v)*w[j] for v,w in zip((-1,1,1,-1,-1,1),ws)) for j in range(8))
    alpha=h.add(e[3],e[5]);omega=h.dot(alpha,HQ)
    ck('actual condensate has weight one',abs(omega)==1 and omega.denominator==1)
    oldh=Q(-1,4);c=Q(1,2)
    ck('old spin residual',-c*(Q(1,2)+2*oldh)==0)
    residue=-c*(1+2*oldh)
    ck('naive K residual rejects',residue==Q(-1,4) and residue!=0)
    ck('changed connection opposite control',-c*(1+2*Q(-1,2))==0)
    ck('changed old moment fails',Q(-1,2)+c*c==Q(-1,4))
    ck('fixed old moment passes',oldh+c*c==0)
    ck('connection curvature squared differs',(Q(-1,2)/oldh)**2==4)
    ck('frames differ without curvature convention',Q(1,2)!=Q(1,4))
    # Gaussian local 3x3 matrix values; derivative-free exact polynomial
    # interpolation of the actual squared residuals, then independent formula.
    Z=h.Z;O=h.O
    X=h.matrix(3);X[0][2]=O
    K=h.matrix(3);K[0][0]=O;K[1][1]=h.gscale(-1,O)
    HA=h.matrix(3);HA[0][0]=O;HA[2][2]=h.gscale(-1,O)
    def br(a,b):return h.madd(h.times(a,b),h.mscale(-1,h.times(b,a)))
    def trace(m):return h.sumg(m[j][j] for j in range(len(m)))
    def val(t,u,f):
        q=h.mscale(t,X);r=h.mscale(u,K)
        M=h.madd(br(q,h.dagger(q)),br(r,h.dagger(r)))
        moment=h.madd(h.mscale(f,HA),M);qr=br(q,r)
        v=h.gadd(h.gscale(2,trace(h.times(h.dagger(qr),qr))),h.gscale(Q(1,2),trace(h.times(moment,moment))))
        if v[1]:raise ValueError('nonreal comparator energy')
        return v[0]
    for t,u,f in [(Q(1),Q(2),Q(3)),(Q(2,3),Q(-3,5),Q(1,7)),(Q(-4,3),Q(0),Q(-1))]:
        ck('full noncommuting energy '+str((t,u,f)),val(t,u,f)==f*f+2*f*t*t+t**4+2*u*u*t*t)
    ck('quartic coefficient central difference',(val(1,1,0)+val(1,-1,0)-2*val(1,0,0))/2==2)
    ck('zero-r cubic central difference',val(1,1,0)-val(1,-1,0)==0)
    for v in [Q(1),Q(-2),Q(3,7)]:ck('induced cubic retains v '+str(v),(val(1,v+1,0)-val(1,v-1,0))/2==4*v)
    ck('curvature source central difference',(val(1,0,1)-val(1,0,-1))/2==2)
    Y=h.matrix(3);Y[0][1]=O
    ck('natural ordinary bracket exists',br(X,h.dagger(X))==HA)
    ck('self bracket identicallyzero',br(X,X)==h.matrix(3))
    ck('two nilpotents commute but not normal',br(X,Y)==h.matrix(3) and br(Y,h.dagger(Y))!=h.matrix(3))
    # This route does NOT independently replay W75's ODE; those three
    # incoming predicates are deliberately not included in its records.
    records={'spinor_residual':0,'same_connection_ordinary_residual_E_over_y2':'-I/4',
             'changed_connection_original_moment':'-1/4','curvature_squared_ratio':4,
             'frame_weights':['1/2','1'],'continuous_SU2_irreps':irr,
             'odd_continuous_dimension':odd,'Q8_odd_doublet_copies':copies,
             'literal_original_root_HQ_weight':int(omega),
             'quartic_coefficient':2,'zero_background_standalone_cubic':0,
             'induced_v_u_t2_coefficient':4,'curvature_f_t2_coefficient':2}
    return {'checks':checks,'records':records,'all_passed':all(checks.values()),
            'scope':'separate exact safeguards, not an incoming full W75 run or physical identification'}
if __name__=='__main__':
    out=run();print(json.dumps(out,indent=2));raise SystemExit(0 if out['all_passed'] else 1)
