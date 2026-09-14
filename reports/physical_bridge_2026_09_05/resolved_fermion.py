"""R30 controls: declared resolved fermions, actual Fox gluing, local well norms.

No full m202 PDE, uniform global Poisson estimate, complete cusp limit,
empirical mass or full-parent quantum completion is certified by this file.
"""
from __future__ import annotations

from functools import lru_cache
import importlib.util
import json
import math
from pathlib import Path
import time

import numpy as np
from scipy.integrate import quad
from scipy.linalg import block_diag, eigvalsh
import sympy as sp


def local(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


hs = local('r30_frozen_holonomy', 'holonomy_spectrum.py')
mi = local('r30_frozen_clifford', 'mass_inflow.py')
dg = local('r30_frozen_source', 'defect_gauge.py')


def clean(value):
    return sp.simplify(sp.expand_complex(value))


def matrix_clean(value):
    return value.applyfunc(clean)


def betti(d0, d1):
    if matrix_clean(d1*d0) != sp.zeros(d1.rows, d0.cols):
        raise ValueError('not a cochain complex')
    r0, r1 = d0.rank(), d1.rank()
    return [d0.cols-r0, d0.rows-r0-r1, d1.rows-r1, 0]


def glued(x, y, k=3, t=1, phases=None, attachment=None):
    # Reuse the old class validation and actual Fox computation, not copied ranks.
    old = hs.cochains(x, y, k, phases)
    x, y, t = map(sp.sympify, (x, y, t))
    if t.has(sp.Float):
        raise ValueError('exact attachment parameter required')
    r = sp.ones(k, 1) if phases is None else sp.Matrix(k, 1, phases)
    v = sp.Matrix([x-1, y-1])
    f = hs.identities()['fox'].subs({hs.X:x, hs.Y:y})
    T = t*sp.eye(k) if attachment is None else sp.Matrix(attachment)
    if T.shape != (k, k) or any(z.has(sp.Float) for z in T):
        raise ValueError('exact k by k attachment required')
    d0 = matrix_clean(v.row_join(sp.zeros(2,k)).col_join(r.row_join(T)))
    d1 = matrix_clean(f.row_join(sp.zeros(1,k)))
    return dict(d0=d0, d1=d1, betti=betti(d0,d1), base=old['base_betti'],
                relative=old['relative_T'], k=k, x=str(x), y=str(y), t=str(t))


@lru_cache(maxsize=None)
def contraction(k=3):
    if not isinstance(k,int) or k<0:
        raise ValueError('nonnegative integer number of components required')
    t=sp.symbols('t', nonzero=True, real=True)
    v=sp.Matrix([hs.X-1,hs.Y-1])
    r=sp.Matrix(k,1,sp.symbols(f'r0:{k}'))
    f=hs.identities()['fox']
    d0=v.row_join(sp.zeros(2,k)).col_join(r.row_join(t*sp.eye(k)))
    d1=f.row_join(sp.zeros(1,k))
    i0=sp.ones(1,1).col_join(-r/t)
    p0=sp.ones(1,1).row_join(sp.zeros(1,k))
    i1=sp.eye(2).col_join(sp.zeros(k,2))
    p1=sp.eye(2).row_join(sp.zeros(2,k))
    H=sp.zeros(1+k,2+k)
    H[1:,2:]=sp.eye(k)/t
    def z(M):
        return all(sp.cancel(x)==0 for x in M)
    return dict(nilpotent=z(d1*d0), retract=z(p0*i0-sp.eye(1)) and z(p1*i1-sp.eye(2)),
                chain0=z(d0*i0-i1*v), chain1=z(d1*i1-f),
                homotopy0=z(sp.eye(1+k)-i0*p0-H*d0),
                homotopy1=z(sp.eye(2+k)-i1*p1-d0*H),
                discarded_core_has_nonzero_homotopy=H != sp.zeros(1+k,2+k))


@lru_cache(maxsize=1)
def boundary_and_action():
    creation, annihilation, c, mass=mi.form_matrices()
    parity=sp.diag(*[(-1)**len(b) for b in mi.cd.BASIS])
    a=sp.symbols('a0:3',real=True)
    h=sp.symbols('h0:3',real=True)
    q=sp.symbols('q',real=True)
    B=sum((-sp.I*q*a[i]*c[i]+q*h[i]*mass[i] for i in range(3)),sp.zeros(8))
    rows=[]
    for i in range(3):
        P=sp.eye(8)-creation[i]*annihilation[i]
        rows.append(dict(rank=P.rank(), projector=P*P==P,
                         isotropic=P.T*c[i]*P==sp.zeros(8),
                         annihilator_dimension=8-(P.T*c[i]).rank(),
                         parity_preserved=P*parity==parity*P))
    n=2
    green=sp.diag(c[n],-c[n])
    match=sp.eye(8).col_join(sp.eye(8))
    # A normal jump is invisible to tangential pullback but not to the Green form.
    scalar=sp.zeros(8,1); scalar[mi.cd.BASIS.index(())]=1
    normal=creation[n]*scalar
    u=normal.col_join(sp.zeros(8,1))
    v=scalar.col_join(scalar)
    return dict(boundaries=rows, hermitian=B.H==B, odd=B*parity==-parity*B,
                full_transmission=match.T*green*match==sp.zeros(8),
                transmission_annihilator=16-(match.T*green).rank(),
                tangent_only_residual=(u.T*green*v)[0],
                gauge_current_matrices=[sp.diff(B,z) for z in a],
                higgs_current_matrices=[sp.diff(B,z) for z in h],
                q=q, c=c, mass=mass)


@lru_cache(maxsize=1)
def conjugacy():
    cd=mi.cd
    r,x,y=cd.COORDS
    F=r*r+r*x+x*y
    dF=cd.exterior({():F})
    eta={(1,):sp.I,(2,):2*sp.I}
    def dA(u):
        return cd.add(cd.exterior(u),cd.wedge(eta,u))
    rows=[]
    for b in cd.BASIS:
        u={b:1+r+x+y}
        dqu=cd.add(dA(u),cd.wedge(dF,u))
        rows.append(dict(degree=len(b),
                         identity=cd.add(dA(cd.scale(u,sp.exp(F))),cd.scale(dqu,-sp.exp(F)))=={},
                         wrong_sign_nonzero=cd.add(dA(cd.scale(u,sp.exp(-F))),cd.scale(dqu,-sp.exp(-F)))!={}))
    s=sp.symbols('s',real=True)
    f=sp.Function('F')(s)
    u=sp.exp(-f)
    return dict(rows=rows, robin=sp.simplify(sp.diff(u,s)+sp.diff(f,s)*u),
                undeformed_neumann=sp.diff(u,s),
                wrong_robin=sp.simplify(sp.diff(u,s)-sp.diff(f,s)*u))


@lru_cache(maxsize=1)
def radial():
    d=dg.core_and_cutoff()
    r,eps,R,beta=d['r'],d['eps'],d['R'],d['beta']
    Fout=beta*sp.log(sp.tanh(r)/sp.tanh(R))
    Fin=beta*(sp.log(sp.tanh(eps)/sp.tanh(R))
              +(sp.log(sp.cosh(r))-sp.log(sp.cosh(eps)))/sp.sinh(eps)**2)
    t=sp.symbols('t',positive=True)
    primitives={1:sp.log(t)-sp.log(1-t*t)/2+1/(2*(1-t*t)),
                2:2*sp.log(t)-sp.log(1-t*t)-1/(2*t*t)+1/(2*(1-t*t))}
    derivatives={a:sp.factor(sp.diff(P,t)-t**(1-2*a)/(1-t*t)**2) for a,P in primitives.items()}
    a=sp.symbols('a',real=True)
    f=sp.tanh(r)**(-a)
    return dict(core_derivative=dg.clean(sp.diff(Fin,r)-d['h_in']),
                exterior_derivative=dg.clean(sp.diff(Fout,r)-d['h_out']),
                join=dg.clean((Fin-Fout).subs(r,eps)),
                local_zero=dg.clean(sp.diff(f,r)+a*f/(sp.sinh(r)*sp.cosh(r))),
                wrong_sign=dg.clean(sp.diff(f,r)-a*f/(sp.sinh(r)*sp.cosh(r))),
                primitive_residuals=derivatives, primitives=primitives,t=t,
                positive_core_beta=d['beta'])


def tail_norm(epsilon,radius,a):
    if not 0<epsilon<radius or a not in (1,2):
        raise ValueError('0<epsilon<radius, a=1 or 2 required by exact comparator')
    def integrand(r):
        return math.sinh(r)*math.cosh(r)*(math.tanh(r)/math.tanh(radius))**(-2*a)
    value,error=quad(integrand,epsilon,radius,epsabs=1e-12,epsrel=1e-12)
    # Stable high-precision evaluation, independent from integration in r.
    e=sp.Float(epsilon,60); R=sp.Float(radius,60)
    P=radial()['primitives'][a]; t=radial()['t']
    exact=sp.tanh(R)**(2*a)*(P.subs(t,sp.tanh(R))-P.subs(t,sp.tanh(e)))
    result=float(exact.evalf(50))
    return dict(epsilon=epsilon,radius=radius,a=a,quadrature=value,
                primitive=result,relative_error=abs(value-result)/result,error=error)


def flat_norm(epsilon,radius,a):
    e,R,a=map(sp.sympify,(epsilon,radius,a))
    if not bool(0<e<R):
        raise ValueError('positive ordered radii required')
    return sp.log(R/e) if a==1 else (R**(2-2*a)-e**(2-2*a))/(2-2*a)


@lru_cache(maxsize=1)
def axial_and_current():
    z,L,N=sp.symbols('z L transverse_norm',positive=True)
    zeta=sp.sin(sp.pi*z/L)
    axial=sp.integrate(sp.diff(zeta,z)**2,(z,0,L))*N
    norm=sp.integrate(zeta**2,(z,0,L))*N
    g,V=sp.symbols('g7 volume',positive=True)
    charge=sp.symbols('charge',real=True)
    raw_norm=sp.symbols('raw_norm',positive=True)
    overlap=sp.simplify(g*charge*raw_norm/(sp.sqrt(V)*raw_norm))
    C=hs.e6_cartan()
    roots=hs.weyl_orbit(C,sp.eye(6)[:,0])
    spinor=[sp.Matrix(w) for w in roots if w[0]==1]
    # A right-handed R contributes as a left-handed conjugate, not another R.
    left_charges=[w[0] for w in spinor]
    conjugate_charges=[-w[0] for w in spinor]
    left_mixed=sum((w[0]*(C*w)[1:, :]*(C*w)[1:, :].T for w in spinor),sp.zeros(5))
    right_mixed=sum((-w[0]*(-C*w)[1:, :]*(-C*w)[1:, :].T for w in spinor),sp.zeros(5))
    return dict(axial_ratio=sp.simplify(axial/norm),L=L,overlap=overlap,
                expected=g*charge/sp.sqrt(V),normalization_residual=sp.diff(overlap,raw_norm),
                spinor_dimension=len(spinor),left_linear=sum(left_charges),
                anomaly_pair=[sum(left_charges+conjugate_charges),
                              sum(q**3 for q in left_charges+conjugate_charges)],
                mixed_pair=left_mixed+right_mixed,left_mixed=left_mixed)


def algebraic_spectrum(t):
    if not math.isfinite(t) or t<=0:
        raise ValueError('positive finite toy attachment required')
    d=glued(-1,1,3,sp.Rational(str(t)))
    A=np.array(d['d0'],dtype=complex); B=np.array(d['d1'],dtype=complex)
    even=block_diag(A.conj().T@A,B@B.conj().T)
    odd=A@A.conj().T+B.conj().T@B
    ev,od=eigvalsh(even),eigvalsh(odd)
    return dict(t=t,even=ev.tolist(),odd=od.tolist(),
                max_difference=float(np.max(np.abs(ev-od))),
                interpretation='Euclidean cochain Gram matrix, not a PDE mass spectrum')


def character_rows():
    omega=(-1+sp.I*sp.sqrt(3))/2
    chars=[(1,1),(-1,1),(sp.I,1),(omega,1),(sp.conjugate(omega),1)]
    chars.extend((z,z) for z in ((-3-sp.I*sp.sqrt(7))/4,(-3+sp.I*sp.sqrt(7))/4))
    rows=[]
    for x,y in chars:
        for k in range(5):
            for t in (0,1,sp.Rational(1,2)):
                d=glued(x,y,k,t)
                rows.append({key:value for key,value in d.items() if key not in ('d0','d1')})
    return rows


def main():
    start=time.monotonic()
    b,c,r,n=boundary_and_action(),conjugacy(),radial(),axial_and_current()
    rows=character_rows()
    spectra=[algebraic_spectrum(t) for t in (.1,.3,1.)]
    norms=[tail_norm(e,.2,a) for a in (1,2) for e in (.01,.003)]
    checks={
        'absolute_green':all(x['rank']==x['annihilator_dimension']==4 and x['projector']
                             and x['isotropic'] and x['parity_preserved'] for x in b['boundaries']),
        'hermitian_odd_action':b['hermitian'] and b['odd'],
        'transmission':b['full_transmission'] and b['transmission_annihilator']==8,
        'tangent_only_rejected':b['tangent_only_residual']!=0,
        'conjugacy':all(x['identity'] for x in c['rows']),
        'wrong_weight_rejected':any(x['wrong_sign_nonzero'] for x in c['rows']),
        'robin_not_neumann':c['robin']==0 and c['undeformed_neumann']!=0 and c['wrong_robin']!=0,
        'chain_contraction':all(all(v for key,v in contraction(k).items()
                                    if key!='discarded_core_has_nonzero_homotopy') for k in range(5)),
        'resolved_is_base':all(d['betti']==d['base'] for d in rows if d['t']!='0'),
        'split_keeps_cores':all(d['betti']==[d['relative'][0]+d['k'],*d['relative'][1:]]
                               for d in rows if d['t']=='0'),
        'radial_source':r['core_derivative']==r['exterior_derivative']==r['join']==0,
        'radial_zero_sign':r['local_zero']==0 and r['wrong_sign']!=0,
        'norm_primitives':all(v==0 for v in r['primitive_residuals'].values()),
        'independent_norm_integrals':all(x['relative_error']<3e-10 for x in norms),
        'paired_algebraic_spectra':all(x['max_difference']<2e-9 for x in spectra),
        'axial_leakage':sp.simplify(n['axial_ratio']-sp.pi**2/n['L']**2)==0,
        'constant_gauge_current':n['overlap']==n['expected'] and n['normalization_residual']==0,
        'anomaly_pair':n['anomaly_pair']==[0,0] and n['mixed_pair']==sp.zeros(5)
                      and n['left_linear']!=0 and n['left_mixed']!=sp.zeros(5),
    }
    print(json.dumps(dict(scope=__doc__,checks={k:bool(v) for k,v in checks.items()},
                          characters=rows,spectra=spectra,norm_controls=norms,
                          analytic_argument='RESOLVED_FERMION_PROOF.md; global well hypotheses not certified',
                          elapsed_seconds=time.monotonic()-start),default=str,indent=2,sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__=='__main__':
    main()
