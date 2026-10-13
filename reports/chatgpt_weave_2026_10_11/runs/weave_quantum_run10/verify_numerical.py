#!/usr/bin/env python3
"""Independent direct theta-series tests, using analytic tau branches.
Numbers are high-precision corroborations, NOT interval-certified bounds.
"""
import argparse,json,math
from pathlib import Path
import mpmath as mp

ap=argparse.ArgumentParser();ap.add_argument('--dps',type=int,default=50);args=ap.parse_args()
mp.mp.dps=args.dps
out=Path(__file__).resolve().parent/'results';out.mkdir(exist_ok=True)
records=[]
def norm(x):
    try:return mp.norm(x)
    except TypeError:return abs(x)
def check(name,lhs,rhs,tol=None):
    residual=norm(lhs-rhs)/max(mp.mpf(1),norm(rhs))
    tol=tol or mp.mpf(10)**(-args.dps+9)
    records.append({'name':name,'residual':mp.nstr(residual,14),'passed':bool(residual<tol)})
    if residual>=tol:raise AssertionError((name,mp.nstr(residual,25)))

def theta(a,b,z,tau,d=0):
    a=mp.mpf(a);b=mp.mpf(b)
    K=max(18,int(mp.ceil(mp.sqrt((args.dps+25)/mp.im(tau))+abs(mp.im(z))/mp.im(tau)+8)))
    return mp.fsum((2j*mp.pi*(n+a))**d*mp.exp(mp.pi*1j*tau*(n+a)**2+2j*mp.pi*(n+a)*(z+b)) for n in range(-K,K+1))
def theta1(z,tau,d=0):return -theta('.5','.5',z,tau,d)
def eta(tau):
    N=max(25,int(mp.ceil((args.dps+20)*mp.log(10)/(2*mp.pi*mp.im(tau)))))
    return mp.exp(mp.pi*1j*tau/12)*mp.fprod(1-mp.exp(2j*mp.pi*tau*n) for n in range(1,N+1))
def W(z,tau,d=0):return mp.matrix([theta(0,0,z,2*tau,d),theta('.5',0,z,2*tau,d)])
def bloch_from(w):
    u,v=w;N=abs(u)**2+abs(v)**2
    return mp.matrix([2*mp.re(mp.conj(u)*v)/N,2*mp.im(mp.conj(u)*v)/N,(abs(u)**2-abs(v)**2)/N])
def nfield(z,tau):return bloch_from(W(z,tau))
def cross(a,b):return mp.matrix([a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]])
Z=mp.matrix([[1,0],[0,-1]]);X=mp.matrix([[0,1],[1,0]]);H=mp.matrix([[1,1],[1,-1]])/mp.sqrt(2);D=mp.matrix([[1,0],[0,1j]])
QA=mp.diag([-1,-1,1]); QB=mp.diag([1,-1,-1])
OT=mp.matrix([[0,-1,0],[1,0,0],[0,0,1]])
OS=mp.matrix([[0,0,1],[0,-1,0],[1,0,0]])
OR=OS*(OT**-1)*OS
moduli=[mp.j,mp.mpc('.23','1.1'),mp.mpc('-.31','.87'),mp.mpf('.5')+mp.sqrt(3)*mp.j/2,mp.mpc('1.31','.73')]
points=[mp.mpc('.17','.23'),mp.mpc('.37','.19')]
for k,tau in enumerate(moduli):
    for j,z in enumerate(points):
        tag=f'tau{k}/point{j}'
        w=W(z,tau);dw=W(z,tau,1); nn=nfield(z,tau)
        check(tag+' unit direction',mp.fdot(nn,nn),mp.mpf(1))
        check(tag+' A period spinor',W(z+1,tau),Z*w)
        check(tag+' B period spinor',W(z+tau,tau),mp.exp(-mp.pi*1j*tau/2-mp.pi*1j*z)*X*w)
        check(tag+' A period direction',nfield(z+1,tau),QA*nn)
        check(tag+' B period direction',nfield(z+tau,tau),QB*nn)
        check(tag+' smooth numerator Wronskian',w[0]*dw[1]-w[1]*dw[0],-mp.pi*eta(tau)**3*theta1(z,tau))
        check(tag+' target-independent scale cancellation',bloch_from(mp.exp(mp.mpc('.13','.29'))*w),nn)
        check(tag+' old half-pole profile same projector',bloch_from(w/mp.sqrt(theta1(z,tau))),nn)
        check(tag+' T field transformation',nfield(z,tau+1),OT*nn)
        check(tag+' S field transformation',nfield(z/tau,-1/tau),OS*nn)
        check(tag+' R field transformation',nfield(z/(tau+1),tau/(tau+1)),OR*nn)
        check(tag+' S spinor transformation',W(z/tau,-1/tau),mp.sqrt(-1j*tau)*mp.exp(mp.pi*1j*z*z/(2*tau))*H*w)
        nx=mp.diff(lambda r:nfield(z+r,tau),mp.mpf(0))
        ny=mp.diff(lambda r:nfield(z+1j*r,tau),mp.mpf(0))
        nxx=mp.diff(lambda r:nfield(z+r,tau),mp.mpf(0),2)
        nyy=mp.diff(lambda r:nfield(z+1j*r,tau),mp.mpf(0),2)
        check(tag+' first order minimum equation',nx+cross(nn,ny),mp.zeros(3,1))
        check(tag+' nonlinear Euler Lagrange',nxx+nyy+(norm(nx)**2+norm(ny)**2)*nn,mp.zeros(3,1))
        dens=abs(w[0]*dw[1]-w[1]*dw[0])**2/(mp.pi*(norm(w)**2)**2)
        check(tag+' three-vector topological density',mp.fdot(nn,cross(nx,ny))/(4*mp.pi),dens)
        check(tag+' action density saturates bound',(norm(nx)**2+norm(ny)**2)/2,4*mp.pi*dens)
        check(tag+' conformality metric',norm(nx)**2,norm(ny)**2)
        check(tag+' orthogonal translation zero modes',mp.fdot(nx,ny),mp.mpf(0))
        # Independent log-norm curvature expression.
        dlog=mp.diff(lambda r:mp.log(norm(W(z+r,tau))**2),mp.mpf(0),2)+mp.diff(lambda r:mp.log(norm(W(z+1j*r,tau))**2),mp.mpf(0),2)
        check(tag+' curvature density',dlog/(4*mp.pi),dens)
    check(f'tau{k} puncture is regular critical point',norm(W(0,tau,1)),mp.mpf(0))
    # Antilinear reflection of target gives the conjugate topological sector,
    # NOT an oriented modular transformation.
    ref=mp.diag([1,-1,1]);z=points[0]
    nn=nfield(z,tau);nx=mp.diff(lambda r:nfield(z+r,tau),mp.mpf(0));ny=mp.diff(lambda r:nfield(z+1j*r,tau),mp.mpf(0))
    check(f'tau{k} anti texture charge reverses',mp.fdot(ref*nn,cross(ref*nx,ref*ny)),-mp.fdot(nn,cross(nx,ny)))

result={'dps':args.dps,'count':len(records),'max_residual':max(float(r['residual']) for r in records),'checks':records,'scope':'Direct-series, finite-cutoff numerical corroboration; no interval/tail certification. Analytic global integrals and Hessian theorem are separate.'}
(out/f'numerical_{args.dps}.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
