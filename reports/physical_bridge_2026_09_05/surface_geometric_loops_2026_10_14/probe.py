"""Actual geometric-loop controls; no physical projected transport inferred."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
def load(folder,name='probe'):
    p=HERE.parent/folder/(name+'.py');sp=importlib.util.spec_from_file_location('geometric_'+folder+'_'+name,p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
@lru_cache(None)
def run():
    w=load('based_transition_prerequisite_2026_10_13');h=load('surface_based_gauge_2026_10_14')
    checks={}
    def ck(n,v):checks[n]=bool(v)
    X={'a':'a','b':'ab'};Y={'a':'aB','b':'b'};Z={'a':'a','b':'ba'}
    Yi={'a':'ab','b':'b'};Zi={'a':'a','b':'bA'};E={'a':'a','b':'b'};c='abAB'
    ck('tangential twists fix actual puncture',w.image(Z,c)==c and w.image(Y,c)==c)
    ck('tangential braid',w.compose(Z,w.compose(Y,Z))==w.compose(Y,w.compose(Z,Y)))
    frame=w.power(w.compose(Z,Y),6)
    ck('negative frame inner inverse puncture',frame==w.inner(w.inv(c)))
    ck('wrong original frame orientation rejected',frame!=w.inner(c))
    positive_frame=w.power(w.compose(Yi,Zi),6)
    ck('positive frame inner puncture',positive_frame==w.inner(c))
    ck('homology-only identity is rejected',frame!=E)
    q=w.compose(w.inner('A'),w.power(w.compose(Yi,Zi),2))
    ck('actual order3 word and order',q=={'a':'b','b':'AB'} and w.power(q,3)==E and q!=E)
    delta=w.compose(X,w.compose(Y,Z))
    ck('actual order4 word',w.power(delta,4)==E and w.power(delta,2)!=E)
    ck('same homology different based lift',w.compose(w.inner('A'),X)==Z and X!=Z)
    a=s.diag(s.I,-s.I);b=s.Matrix([[0,1],[-1,0]]);I6=s.eye(6)
    A=s.diag(-a,a,-a);B=s.diag(b,-b,-b)
    PX=s.Matrix([[0,0,1],[0,1,0],[1,0,0]]);PY=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    L=s.kronecker_product(PX,(s.eye(2)+a)/s.sqrt(2))
    Y6=s.kronecker_product(PY,(s.eye(2)+b)/s.sqrt(2));Z6=A.H*L
    ck('actual SU6 frame power plus identity',h.zero((Z6*Y6)**6-I6))
    ck('actual fibre puncture minus identity',h.zero(A*B*A.H*B.H+I6))
    ck('SU6 alone does not match geometric frame',not h.zero((Z6*Y6)**6-A*B*A.H*B.H))
    Q6=A.H*(Y6.H*Z6.H)**2
    ck('order3 SU6 centre retained',h.zero(Q6**3+I6))
    ck('order4 SU6 centre retained',h.zero((L*Y6*Z6)**4+I6))
    f=load('weave_field_map_2026_10_14');_,ee,roots,hq,_=f.data();hw=ee[3]-ee[4]
    ck('paired centre vanishes on all240 roots',len(roots)==240 and all(int(r.dot(hq-hw))%2==0 for r in roots))
    ck('unpaired coefficient centre rejected',any(int(r.dot(hq))%2 for r in roots))
    for m in (1,3,5,7,9,11):
        ck('weak frame centre '+str(m),h.clean(s.exp(-s.I*s.pi*m))==-1)
        ck('weak order3 inverse centre '+str(m),h.clean(s.exp(s.I*s.pi*m))==-1)
    J=s.diag(1,-1);T=s.Matrix([[1,1],[0,1]])
    C=J*T*J
    ck('positive coordinate cusp inverse shear',C==s.Matrix([[1,-1],[0,1]]))
    for n,G in enumerate([T,s.Matrix([[0,-1],[1,0]]),s.Matrix([[2,1],[1,1]])]):
        ck('coordinate homology automorphism '+str(n),J*G*J*J*T*J==J*(G*T)*J and (J*G*J).det()==1)
    qrot=s.Rational(3,5)+s.I*s.Rational(4,5)
    U=s.diag(1,qrot**-2,qrot**-1,qrot**-3);Pv=s.diag(1,1,0,0);Nv=s.eye(4)-Pv
    flip=s.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
    ck('canonical leading trace unitary',h.zero(U.H*U-s.eye(4)))
    ck('both extreme complex planes preserved',h.zero(U*Pv-Pv*U) and h.zero(U*Nv-Nv*U))
    ck('normal reversal exchanges extremes',flip*Pv*flip.T==Nv and flip*Pv!=Pv*flip)
    rows=[]
    for m in (1,3,5,7,9,11):
        census=[]
        for odd,phases in [(False,[('+1',s.Integer(1)),('-1',s.Integer(-1))]),(True,[('+i',s.I),('-i',-s.I)])]:
            chars={}
            for j in (0,1):
                for k in range(12):
                    g=A**j*Z6**k;t=h.clean(s.trace(g));t2=h.clean(s.trace(g*g));t3=h.clean(s.trace(g*g*g))
                    w2=h.clean((t*t-t2)/2);w3=h.clean((t**3-3*t*t2+2*t3)/6)
                    chars[j,k]=h.clean((w3+3*(t+s.conjugate(t)))*2*s.cos(s.pi*m*k/12) if odd else
                        t*s.conjugate(t)+8+2*s.cos(s.pi*m*k/6)+3*(w2+s.conjugate(w2)))
            out=[]
            for label,av in phases:
                row=[]
                for r in range(12):
                    val=h.clean(sum(v*av**(-j)*s.exp(-s.I*s.pi*r*k/6) for (j,k),v in chars.items())/24)
                    ck('integral actual Z phase '+str((m,odd,label,r)),val.is_Integer and val>=0)
                    row.append([r,int(val)])
                out.append([label,row])
            census.append(out)
        even,odd=census
        ck('whole coefficient kept '+str(m),sum(n for _,rr in even for _,n in rr)==136 and sum(n for _,rr in odd for _,n in rr)==112)
        rows.append({'m':m,'Z_even':even,'Z_odd':odd,'Z_odd_zero_phase_ranks':[rr[0][1] for _,rr in odd],
            'inverse_Z_odd':[[label,[[r,dict(rr)[(-r)%12]] for r in range(12)]] for label,rr in odd]})
    return {'checks':checks,'records':{'frame_inner_word':w.inv(c),'positive_frame_inner_word':c,
        'negative_frame_action':frame,'positive_frame_action':positive_frame,'frame_SU6_sign':1,'puncture_SU6_sign':-1,
        'frame_weak_sign':-1,'paired_E8_frame_matches_puncture':True,'order3_word':q,
        'positive_coordinate_T_homology':[[1,-1],[0,1]],'classes':rows},'all_passed':all(checks.values()),
        'scope':'supplied orbifold flat bundle and leading complex trace gluing; physical projected transport/reality not earned'}
if __name__=='__main__':
    o=run();print(json.dumps(o,indent=2));raise SystemExit(0 if o['all_passed'] else 1)
