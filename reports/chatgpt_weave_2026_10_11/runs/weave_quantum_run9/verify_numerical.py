#!/usr/bin/env python3
"""Independent numerical checks of Run 9 endpoint blocks.

Direct theta series (period-one argument), oscillator products with explicit
analytic q exponents, and independently summed cylinder mode kernels.
No code is imported from preceding reports. Truncations are conservative but
not interval certified. Strict identities and finite-distance limits are
reported separately.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parent
pa=argparse.ArgumentParser();pa.add_argument('--dps',type=int,default=70)
a=pa.parse_args();mp.mp.dps=a.dps
if a.dps<30:raise ValueError('Use at least 30 digits.')
checks=[]
TOL=mp.power(10,-a.dps+12)

def residual(x,y):
    if isinstance(x,mp.matrix):return mp.norm(x-y)/max(1,mp.norm(y))
    return abs(x-y)/max(1,abs(y))
def test(name,x,y,kind='strict',tol=None):
    r=residual(x,y);t=TOL if tol is None else tol
    if r>t:raise AssertionError(f'{name}: {mp.nstr(r,20)} > {mp.nstr(t,8)}')
    checks.append({'name':name,'kind':kind,'residual':mp.nstr(r,20)})

def cut(tau,z=0):
    yy=mp.im(tau)
    if yy<=0:raise ValueError('tau must lie in the upper half plane')
    return int(mp.ceil(mp.sqrt((a.dps+25)*mp.log(10)/(mp.pi*yy))+abs(mp.im(z))/yy+6))

def theta(n,z,tau,derivative=0):
    sh=mp.mpf('.5') if n in [1,2] else mp.mpf(0)
    N=cut(tau,z)
    def term(j):
        r=j+sh
        v=mp.exp(mp.pi*1j*tau*r*r+2*mp.pi*1j*r*z)
        if n==1:v*=(-1j)*((-1)**j)
        if n==4:v*=(-1)**j
        if derivative:v*=(2*mp.pi*1j*r)**derivative
        return v
    return mp.fsum(term(j) for j in range(-N,N+1))

def prodcut(tau):return int(mp.ceil((a.dps+25)*mp.log(10)/(2*mp.pi*mp.im(tau))))+5

def eta(tau):
    p=mp.exp(mp.pi*1j*tau/12)
    for n in range(1,prodcut(tau)+1):p*=1-mp.exp(2*mp.pi*1j*tau*n)
    return p

def spinZ(n,tau,N=5):
    # No principal fractional powers of the nome or theta functions.
    if n==2:
        p=mp.power(2,mp.mpf(N)/2)*mp.exp(2*mp.pi*1j*tau*N/24)
        for j in range(1,prodcut(tau)+1):p*=(1+mp.exp(2*mp.pi*1j*tau*j))**N
    else:
        p=mp.exp(-2*mp.pi*1j*tau*N/48)
        sign=1 if n==3 else -1
        for j in range(1,prodcut(tau)+1):p*=(1+sign*mp.exp(2*mp.pi*1j*tau*(mp.mpf(j)-mp.mpf('.5'))))**N
    return p

def szego(n,z,tau):
    return theta(n,z,tau)*theta(1,0,tau,1)/(theta(n,0,tau)*theta(1,z,tau))
def g(z,tau):return theta(1,z,tau,1)/theta(1,z,tau)

def mode_kernel(n,z,tau):
    """Cylinder ordered kernel for -Im(tau)<Im(z)<0.
    n=1 is the periodic supertrace (zero-mode removed only in the pairing).
    n=2 is R ordinary; n=3 NS ordinary; n=4 NS graded.
    """
    yy=mp.im(tau);iz=mp.im(z)
    if not (-yy<iz<0):raise ValueError('mode sum needs the ordered convergence strip')
    rate=min(-iz,yy+iz)
    bound=int(mp.ceil((a.dps+25)*mp.log(10)/(2*mp.pi*rate)))+8
    isR=n in [1,2]
    sign=1 if n in [2,3] else -1
    vals=[]
    for j in range(1,bound+1):
        r=mp.mpf(j) if isR else mp.mpf(j)-mp.mpf('.5')
        qq=mp.exp(2*mp.pi*1j*tau*r)
        zz=mp.exp(-2*mp.pi*1j*r*z)
        vals.append((zz+sign*qq/zz)/(1+sign*qq))
    return 2*mp.pi*1j*((mp.mpf('.5') if isR else 0)+mp.fsum(vals))

def odd_cyclic(x,z,w,tau):return g(z-w,tau)-g(x-w,tau)+g(x-z,tau)
def central(x,z,w,tau):return eta(tau)**5*odd_cyclic(x,z,w,tau)
def rawpair(z,tau):return mp.matrix([spinZ(n,tau)*szego(n,z,tau) for n in [2,3,4]])
def mono(p,e):
    M=mp.matrix(3)
    for i in range(3):M[i,p[i]]=mp.exp(2*mp.pi*1j*e[i]/48)
    return M
SP=mono([2,1,0],[0,0,0]);TP=mono([0,2,1],[10,43,43]);RP=SP*TP**-1*SP**-1
Ssource=mono([2,1,0],[6,6,6]);Tsource=mono([0,2,1],[6,42,42])
C=mp.matrix([[0,mp.mpf('.5'),mp.mpf('.5')],[0,mp.mpf('.5'),-mp.mpf('.5')],[1/mp.sqrt(2),0,0]])
Saff=C*SP*C**-1;Taff=C*TP*C**-1

samples=[('0','1'),('0.13','1.11'),('-0.24','0.83'),('0.19','0.68')]
x=mp.mpc('.03','.02');z=mp.mpc('.16','.14');w=mp.mpc('-.10','.32');u=z-w
negative=[]
for k,(re,im) in enumerate(samples):
    tau=mp.mpc(re,im)
    # Independent trace products vs direct theta identities (squared removes only
    # the analytic square root; generator checks below retain its actual sign).
    for n in [2,3,4]:
        test(f'{k}: spin {n} product squared',spinZ(n,tau)**2,(theta(n,0,tau)/eta(tau))**5)
        test(f'{k}: Szego {n} vs oscillator mode sum',szego(n,u,tau),mode_kernel(n,u,tau))
        test(f'{k}: Szego {n} antisymmetry',szego(n,-u,tau),-szego(n,u,tau))
    test(f'{k}: odd kernel vs independent mode sum',g(u,tau),mode_kernel(1,u,tau))
    cyc=odd_cyclic(x,z,w,tau)
    cyc_mode=mode_kernel(1,z-w,tau)-mode_kernel(1,x-w,tau)+mode_kernel(1,x-z,tau)
    test(f'{k}: cyclic odd kernel from three independent mode sums',cyc,cyc_mode)
    test(f'{k}: odd cyclic endpoint antisymmetry',odd_cyclic(x,w,z,tau),-cyc)
    test(f'{k}: odd cyclic z-period',odd_cyclic(x,z+1,w,tau),cyc)
    test(f'{k}: odd cyclic z-tau-period',odd_cyclic(x,z+tau,w,tau),cyc)
    test(f'{k}: odd cyclic common translation',odd_cyclic(x+mp.mpc('.09','.07'),z+mp.mpc('.09','.07'),w+mp.mpc('.09','.07'),tau),cyc)
    pp=rawpair(u,tau)
    test(f'{k}: pair full T transport',rawpair(u,tau+1),TP*pp)
    test(f'{k}: pair full S transport',rawpair(u/tau,-1/tau),tau*SP*pp)
    test(f'{k}: pair full R transport',rawpair(u/(tau+1),tau/(tau+1)),(tau+1)*RP*pp)
    test(f'{k}: affine pair S transport',C*rawpair(u/tau,-1/tau),tau*Saff*(C*pp))
    test(f'{k}: affine pair T transport',C*rawpair(u,tau+1),Taff*(C*pp))
    # Retain the full central puncture as the singlet H5 insertion.
    cc=central(x,z,w,tau)
    test(f'{k}: central H5 pair T transport',central(x,z,w,tau+1),mp.exp(5*mp.pi*1j/12)*cc)
    test(f'{k}: central H5 pair S transport',central(x/tau,z/tau,w/tau,-1/tau),mp.exp(-5*mp.pi*1j/4)*tau**(mp.mpf(7)/2)*cc)
    test(f'{k}: central H5 pair R transport',central(x/(tau+1),z/(tau+1),w/(tau+1),tau/(tau+1)),mp.exp(-5*mp.pi*1j/12)*(tau+1)**(mp.mpf(7)/2)*cc)
    # Actual flavour tensor is delta; geometry acts on channel only.
    A=mp.eye(5)*cc
    test(f'{k}: full five-vector central tensor transport',mp.eye(5)*central(x/tau,z/tau,w/tau,-1/tau),mp.exp(-5*mp.pi*1j/4)*tau**(mp.mpf(7)/2)*A)
    eps=mp.power(10,-a.dps//3)*mp.mpc('1','.2')
    ftol=mp.power(10,-a.dps//3+3)
    for n in [2,3,4]:
        test(f'{k}: pair spin {n} fusion residue',eps*spinZ(n,tau)*szego(n,eps,tau),spinZ(n,tau),'finite_limit',ftol)
    test(f'{k}: central pair fusion residue',eps*central(x,w+eps,w,tau),eta(tau)**5,'finite_limit',ftol)
    # Negative controls use a nonzero vector and are not rounded to a pass.
    r=residual(Tsource*pp,TP*pp)
    if r<mp.mpf('.01'):raise AssertionError('negative target test unexpectedly small')
    negative.append({'sample':k,'wrong_target_T_residual':mp.nstr(r,20)})
    # Replacing an internal index with source O genuinely rotates polarization.
    O=mp.matrix([[1,0,0],[0,0,1],[0,-1,0]])
    e2=mp.matrix([0,1,0]);diff=mp.norm(O*e2-e2)
    test(f'{k}: imposed flavour rotation negative magnitude',diff,mp.sqrt(2))

strict=[mp.mpf(c['residual']) for c in checks if c['kind']=='strict']
limits=[mp.mpf(c['residual']) for c in checks if c['kind']=='finite_limit']
out={'dps':a.dps,'number_of_comparisons':len(checks),'strict_comparisons':len(strict),'finite_limit_comparisons':len(limits),
 'max_strict_normalized_residual':mp.nstr(max(strict),25),'max_finite_limit_normalized_residual':mp.nstr(max(limits),25),
 'checks':checks,'negative_controls':negative,
 'scope':'four generic/sample moduli; no interval-certified bounds; fixed rational coset boundary and framed transport, not a singular Dirac Quillen calculation'}
(ROOT/'results'/f'numerical_{a.dps}.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['checks','negative_controls']},indent=2))
