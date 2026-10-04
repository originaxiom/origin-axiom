"""Exact comparator controls; not a solver of the actual silver PDE."""
import hashlib
import json
from functools import lru_cache
from pathlib import Path

import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
for line in (HERE/'INPUT_HASHES.txt').read_text().splitlines():
    digest,path=line.split(maxsplit=1)
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path


def comm(A,B):
    return A*B-B*A


def clean(A):
    return A.applyfunc(lambda x:s.trigsimp(s.simplify(x)))


@lru_cache(None)
def jacobi():
    r=s.symbols('r',real=True)
    A=s.I*s.Matrix([[r,1],[1,-r]])
    P=s.Matrix([[1,r+s.I],[r-s.I,-1]])
    S=s.Matrix([[r*r+1,1+s.I*r],[1-s.I*r,-r*r-1]])
    assert A.conjugate().T==-A and P.conjugate().T==P and S.conjugate().T==S
    cov=lambda B:B.diff(r)+comm(A,B)
    dA=-comm(P,S)/2
    dP=-cov(S)/2
    dmu=-cov(dP)-comm(dA,P)
    L=-cov(cov(S))+comm(P,comm(P,S))
    assert clean(dmu+L/2)==s.zeros(2)
    omitted=-cov(dP)
    assert clean((omitted-dmu).subs(r,0))!=s.zeros(2)
    Q=comm(P,S)
    assert s.simplify(s.trace(S*comm(P,Q))-s.trace(Q.conjugate().T*Q))==0
    assert s.simplify(s.trace(Q.conjugate().T*Q).subs(r,0))>0
    # Infinitesimal orthonormal metric frame, including derivative term.
    C=A+P
    dC=comm(S,C)/2-S.diff(r)/2
    assert clean(dC-dA-dP)==s.zeros(2)
    return {'status':'PASS','full_connection_variation':True,
            'omitted_variation_detected':True,'positive_commutator_form':True}


@lru_cache(None)
def comparator():
    r,k=s.symbols('r k',real=True)
    L=s.symbols('L',positive=True)
    N=s.zeros(5); N[0,4]=1
    J=s.diag(1,0,0,0,-1)
    xi=s.diag(1,1,1,1,-4)
    t=k/s.cos(k*L)
    h=s.cos(k*L)/s.cos(k*r)
    H=s.diag(h,1,1,1,1/h)
    assert s.simplify(H.det()-1)==0
    assert clean(H.subs(r,L)-s.eye(5))==s.zeros(5)
    assert clean(H.subs(r,-L)-s.eye(5))==s.zeros(5)
    Cr=-k*s.tan(k*r)*J/2
    Cx=k/s.cos(k*r)*N
    assert clean(Cx-t*h*N)==s.zeros(5)
    assert clean(Cr+s.diff(h,r)/h*J/2)==s.zeros(5)
    curvature=clean(Cx.diff(r)+comm(Cr,Cx))
    moment=clean((Cr+Cr.T).diff(r)+comm(Cr,Cr.T)+comm(Cx,Cx.T))
    assert curvature==moment==s.zeros(5)
    density=s.simplify(s.trace(Cx.T*Cx))
    primitive=k*s.tan(k*r)
    assert s.trigsimp(s.diff(primitive,r)-density)==0
    integral=s.simplify(primitive.subs(r,L)-primitive.subs(r,-L))
    psi_r=(Cr+Cr.T)/2
    flux=s.simplify(s.trace(xi*psi_r.subs(r,L))-s.trace(xi*psi_r.subs(r,-L)))
    assert s.simplify(integral-2*k*s.tan(k*L))==0
    assert s.simplify(flux+5*k*s.tan(k*L))==0
    assert s.simplify(2*flux+5*integral)==0
    point={k:1,L:s.pi/3,r:s.pi/4}
    assert integral.subs(point)>0 and flux.subs(point)<0
    wrong_radial=clean(Cx.diff(r)+comm(-Cr,Cx))
    assert clean(wrong_radial.subs(point))!=s.zeros(5)
    assert s.simplify((-2*flux+5*integral).subs(point))!=0
    frozen=comm(t*N,t*N.T)
    assert clean(frozen.subs(point))!=s.zeros(5)
    assert clean(Cr.subs(k,0))==clean(Cx.subs(k,0))==s.zeros(5)
    assert clean(H.subs(k,0))==s.eye(5)
    hol=s.eye(5)-t*N
    assert clean((hol-s.eye(5))**2)==s.zeros(5)
    assert (hol-s.eye(5)).subs(point).rank()==1
    assert s.simplify(hol.det()-1)==0
    dual_r=-Cr.T; dual_x=-Cx.T; dual_xi=-xi.T
    dual_moment=clean((dual_r+dual_r.T).diff(r)+comm(dual_r,dual_r.T)+comm(dual_x,dual_x.T))
    assert dual_moment==s.zeros(5)
    dual_flux=s.simplify(s.trace(dual_xi*dual_r.subs(r,L))-s.trace(dual_xi*dual_r.subs(r,-L)))
    assert s.simplify(dual_flux-flux)==0
    assert clean(H.subs(k,-k)-H)==s.zeros(5)
    assert s.simplify(flux.subs(k,-k)-flux)==0
    assert s.limit(t/k,k,0)==1
    assert s.limit(flux/(t*t),k,0)==-5*L
    assert s.series(flux,k,0,4).removeO()==-5*L*k*k
    assert s.simplify(s.trace(curvature.T*curvature)+s.trace(moment.T*moment)/4)==0
    return {'status':'PASS','rank':5,'fixed_boundary_metric':True,
            'full_flatness_and_moment':True,'nonsplit_periodic_loop':True,
            'flux':str(flux),'extension_norm':str(integral),
            'small_amplitude_coefficient':'-5*L','split_smooth':True,
            'dual_same_scalar_flux':True,'radial_sign_failure_detected':True,
            'normal_sign_failure_detected':True,'frozen_metric_failure_detected':True,
            'bare_residual_potential':0,'silver_PDE_solved_numerically':False,
            'comparator_peripheral_matrices_constant':False}


def custody():
    records=[json.loads(line) for line in (ROOT/'reports/silver_global_boundary_2026_10_04/NATIVE_FIRST.jsonl').read_text().splitlines()]
    members=[r['member'] for r in records if 'member' in r]
    assert len(members)==4 and records[-1]['status']=='PASS'
    assert all(row['same_peripheral_matrices'] for row in members)
    return {'pinned_previous_members':4,'replay_here':False}


if __name__=='__main__':
    print(json.dumps({'jacobi':jacobi(),'comparator':comparator(),
                      'input_custody':custody()},sort_keys=True),flush=True)
