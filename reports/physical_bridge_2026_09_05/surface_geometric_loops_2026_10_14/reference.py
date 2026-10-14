"""Separate free-word/Gaussian frame test and Fraction phase transport."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
def load(folder):
    p=HERE.parent/folder/'reference.py';sp=importlib.util.spec_from_file_location('geom_ref_'+folder,p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
@lru_cache(None)
def run():
    w=load('surface_based_gauge_2026_10_14');h=load('weave_registered_embedding_2026_10_13')
    checks={}
    def ck(n,v):checks[n]=bool(v)
    X={'a':'a','b':'ab'};Y={'a':'aB','b':'b'};Z={'a':'a','b':'ba'}
    Yi={'a':'ab','b':'b'};Zi={'a':'a','b':'bA'};E={'a':'a','b':'b'};c='abAB'
    frame=w.mpow(w.compose(Z,Y),6);positive_frame=w.mpow(w.compose(Yi,Zi),6)
    ck('separate negative frame word',frame==w.inner(w.inverse(c)))
    ck('separate positive frame word',positive_frame==w.inner(c))
    ck('separate wrong frame orientation rejected',frame!=w.inner(c))
    ck('separate frame not trivial',w.inner(c)!=E)
    q=w.compose(w.inner('A'),w.mpow(w.compose(Yi,Zi),2))
    ck('separate order3 exact',q=={'a':'b','b':'AB'} and w.mpow(q,3)==E)
    ck('separate order4 exact',w.mpow(w.compose(X,w.compose(Y,Z)),4)==E)
    ck('separate based lift distinction',w.compose(w.inner('A'),X)==Z and X!=Z)
    def power(g,n):
        out=h.identity(len(g))
        for _ in range(n):out=h.times(out,g)
        return out
    a=[[h.I,h.Z],[h.Z,h.gscale(-1,h.I)]];b=[[h.Z,h.O],[h.gscale(-1,h.O),h.Z]]
    A=h.block_diag([h.mscale(-1,a),a,h.mscale(-1,a)])
    B=h.block_diag([b,h.mscale(-1,b),h.mscale(-1,b)])
    PX=[[h.O if i==(2,1,0)[j] else h.Z for j in range(3)] for i in range(3)]
    PY=[[h.O if i==(0,2,1)[j] else h.Z for j in range(3)] for i in range(3)]
    NX=h.kron(PX,h.madd(h.identity(2),a));NY=h.kron(PY,h.madd(h.identity(2),b));NZ=h.times(h.dagger(A),NX)
    ck('Gaussian normalized frame plus',power(h.times(NZ,NY),6)==h.mscale(64,h.identity(6)))
    C=h.times(h.times(h.times(A,B),h.dagger(A)),h.dagger(B))
    ck('Gaussian actual puncture minus',C==h.mscale(-1,h.identity(6)))
    NQ=h.times(h.dagger(A),power(h.times(h.dagger(NY),h.dagger(NZ)),2))
    ck('Gaussian order3 retained centre',power(NQ,3)==h.mscale(-64,h.identity(6)))
    ck('Gaussian order4 retained centre',power(h.times(h.times(NX,NY),NZ),4)==h.mscale(-64,h.identity(6)))
    for m in (1,3,5,7,9,11):
        ck('Fraction frame weak sign '+str(m),12*Q(-m,24)%1==Q(1,2))
        ck('Fraction order3 weak sign '+str(m),-12*Q(-m,24)%1==Q(1,2))
    base=load('surface_weak_completions_2026_10_14').run();ck('prior whole family exact transport',base['all_passed'])
    rows=[]
    for old in base['records']['classes']:
        census=[]
        for kind in ('even','odd'):
            out=[]
            for label,rr in old[kind]:
                shift={'+1':0,'-1':6,'+i':-3,'-i':3}[label]
                counts=Counter()
                for r,n in rr:counts[(r+shift)%12]+=n
                out.append([label,[[r,counts[r]] for r in range(12)]])
            census.append(out)
        even,odd=census;m=old['m']
        ck('Fraction keeps all248 '+str(m),sum(n for _,rr in even for _,n in rr)==136 and sum(n for _,rr in odd for _,n in rr)==112)
        rows.append({'m':m,'Z_even':even,'Z_odd':odd,'Z_odd_zero_phase_ranks':[rr[0][1] for _,rr in odd],
            'inverse_Z_odd':[[label,[[r,dict(rr)[(-r)%12]] for r in range(12)]] for label,rr in odd]})
    # Distinct exact normal-frame test; not a density/closed-domain certificate.
    z=(Q(3,5),Q(4,5));zinv=h.conj(z)
    weights=[h.O,h.gmul(zinv,zinv),zinv,h.gmul(h.gmul(zinv,zinv),zinv)]
    ck('Gaussian canonical frame unitary',all(h.gmul(v,h.conj(v))==h.O for v in weights))
    flip=(2,3,0,1);plus=(1,1,0,0)
    ck('Gaussian normal reversal exchanges extremes',tuple(plus[j] for j in flip)==tuple(1-j for j in plus))
    return {'checks':checks,'records':{'frame_inner_word':w.inverse(c),'positive_frame_inner_word':c,
        'negative_frame_action':frame,'positive_frame_action':positive_frame,'frame_SU6_sign':1,'puncture_SU6_sign':-1,
        'frame_weak_sign':-1,'paired_E8_frame_matches_puncture':True,'order3_word':q,
        'positive_coordinate_T_homology':[[1,-1],[0,1]],'classes':rows},'all_passed':all(checks.values()),
        'scope':'independent finite exact geometric controls; not physical mode transport or nonauthor analytic acceptance'}
if __name__=='__main__':
    o=run();print(json.dumps(o,indent=2));raise SystemExit(0 if o['all_passed'] else 1)
