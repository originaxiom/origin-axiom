#!/usr/bin/env python3
"""Global numerical controls in ordinary double precision.
Charge is computed in three ways: holomorphic density, twisted spectral
three-vector derivatives, and oriented spherical triangles. No fitted input.
"""
import json
from pathlib import Path
import numpy as np

OUT=Path(__file__).resolve().parent/'results';OUT.mkdir(exist_ok=True)
checks=[];integrals=[];variations=[]
def check(name, value, target, tolerance):
    err=float(abs(value-target))
    checks.append({'name':name,'value':float(value),'target':float(target),'error':err,'tolerance':tolerance,'passed':err<tolerance})
    if err>=tolerance:raise AssertionError((name,value,target,err))

def wfun(z,tau,d=0):
    vals=[]
    for a in (0.,.5):
        out=np.zeros_like(z,dtype=np.complex128)
        for n in range(-15,16):
            q=n+a
            out+=(2j*np.pi*q)**d*np.exp(2j*np.pi*tau*q*q+2j*np.pi*q*z)
        vals.append(out)
    return np.array(vals)

def nfun(z,tau):
    u,v=wfun(z,tau);den=abs(u)**2+abs(v)**2
    return np.array([2*np.real(np.conj(u)*v)/den,2*np.imag(np.conj(u)*v)/den,(abs(u)**2-abs(v)**2)/den])

def density(z,tau):
    u,v=wfun(z,tau);du,dv=wfun(z,tau,1)
    return abs(u*dv-v*du)**2/(np.pi*(abs(u)**2+abs(v)**2)**2)

SHIFTS=[(.5,0),(.5,.5),(0,.5)]
def deriv(arr,tau,kind):
    N=arr.shape[1]; ss,tt=np.meshgrid(np.arange(N)/N,np.arange(N)/N,indexing='ij')
    rawfreq=np.fft.fftfreq(N,d=1/N)
    ds=np.zeros_like(arr,dtype=complex)
    for a,(ax,ay) in enumerate(SHIFTS):
        phase=np.exp(2j*np.pi*(ax*ss+ay*tt))
        fhat=np.fft.fft2(arr[a]/phase)
        kx=rawfreq[:,None]+ax; kt=rawfreq[None,:]+ay
        ky=(kt-tau.real*kx)/tau.imag
        factor={'x':2j*np.pi*kx,'y':2j*np.pi*ky,'lap':-4*np.pi**2*(kx*kx+ky*ky)}[kind]
        ds[a]=phase*np.fft.ifft2(factor*fhat)
    if np.max(np.abs(ds.imag))>2e-6 and N>=48:raise AssertionError('imaginary spectral derivative too large')
    return ds.real

def cross(a,b):return np.cross(a,b,axisa=0,axisb=0,axisc=0)
def dot(a,b):return np.sum(a*b,axis=0)
def energy(n,tau):
    nx=deriv(n,tau,'x');ny=deriv(n,tau,'y')
    return .5*tau.imag*np.mean(dot(nx,nx)+dot(ny,ny))

def solid_angle(a,b,c):
    return 2*np.arctan2(dot(a,cross(b,c)),1+dot(a,b)+dot(b,c)+dot(c,a))
def triangle_charge(N,tau,z0=0):
    ss,tt=np.meshgrid(np.arange(N+1)/N,np.arange(N+1)/N,indexing='ij')
    n=nfun(ss+tau*tt-z0,tau)
    a=n[:,:-1,:-1];b=n[:,1:,:-1];c=n[:,1:,1:];d=n[:,:-1,1:]
    return np.sum(solid_angle(a,b,c)+solid_angle(a,c,d))/(4*np.pi)

moduli=[1j,.23+1.1j,-.31+.87j,.5+np.sqrt(3)*1j/2]
for k,tau in enumerate(moduli):
    for N in (16,32,64):
        ss,tt=np.meshgrid(np.arange(N)/N,np.arange(N)/N,indexing='ij')
        z=ss+tau*tt;n=nfun(z,tau)
        nx=deriv(n,tau,'x');ny=deriv(n,tau,'y')
        qhol=tau.imag*np.mean(density(z,tau))
        qspec=tau.imag*np.mean(dot(n,cross(nx,ny)))/(4*np.pi)
        qtri=triangle_charge(N,tau)
        en=energy(n,tau)
        bps=nx+cross(n,ny)
        eom=deriv(n,tau,'lap')+(dot(nx,nx)+dot(ny,ny))*n
        item={'tau':[tau.real,tau.imag],'N':N,'Q_holomorphic':float(qhol),'Q_spectral':float(qspec),'Q_triangles':float(qtri),'g_squared_action':float(en),'BPS_L2':float(np.sqrt(tau.imag*np.mean(dot(bps,bps)))),'EOM_L2':float(np.sqrt(tau.imag*np.mean(dot(eom,eom))))}
        integrals.append(item)
        check(f'{k}/{N} topological triangle charge',qtri,.5,5e-13)
        if N==64:
            check(f'{k} holomorphic integrated charge',qhol,.5,2e-12)
            check(f'{k} spectral integrated charge',qspec,.5,2e-12)
            check(f'{k} integrated action',en,2*np.pi,2e-11)
            check(f'{k} translation metric xx',tau.imag*np.mean(dot(nx,nx)),2*np.pi,2e-11)
            check(f'{k} translation metric yy',tau.imag*np.mean(dot(ny,ny)),2*np.pi,2e-11)
            check(f'{k} translation metric xy',tau.imag*np.mean(dot(nx,ny)),0,2e-11)
            check(f'{k} translated action',energy(nfun(z-(.13+.27j),tau),tau),en,2e-11)
            check(f'{k} translated charge',triangle_charge(N,tau,.13+.27j),.5,5e-13)
            check(f'{k} reflected charge',tau.imag*np.mean(dot(n*np.array([1,-1,1])[:,None,None],cross(nx*np.array([1,-1,1])[:,None,None],ny*np.array([1,-1,1])[:,None,None])))/(4*np.pi),-.5,2e-12)

# Finite deformations of the direction field, preserving all twisted boundaries.
tau=.23+1.1j;N=96
ss,tt=np.meshgrid(np.arange(N)/N,np.arange(N)/N,indexing='ij')
z=ss+tau*tt;n=nfun(z,tau);nx=deriv(n,tau,'x');ny=deriv(n,tau,'y');e0=energy(n,tau)
for r in range(3):
    v=np.array([np.cos(2*np.pi*((ax+(r==1))*ss+(ay+(r==2))*tt)+.3*(a+1)) for a,(ax,ay) in enumerate(SHIFTS)])
    tangent=v-n*dot(n,v)
    lin=deriv(tangent,tau,'x')+cross(tangent,ny)+cross(n,deriv(tangent,tau,'y'))
    predicted=tau.imag*np.mean(dot(lin,lin))
    vals=[]
    for eps in (1e-2,3e-3,1e-3):
        pp=n+eps*tangent;pp/=np.sqrt(dot(pp,pp))
        mm=n-eps*tangent;mm/=np.sqrt(dot(mm,mm))
        ep=energy(pp,tau);em=energy(mm,tau)
        measured=(ep+em-2*e0)/(eps*eps)
        vals.append({'epsilon':eps,'E_plus_minus':[float(ep),float(em)],'second_variation':float(measured),'analytic_square_prediction':float(predicted),'relative_error':float(abs(measured-predicted)/max(1,abs(predicted)))})
        if min(ep,em)<e0-1e-11:raise AssertionError('energy decreased')
    variations.append(vals)
    check(f'finite variation {r} Hessian square agreement',vals[-1]['relative_error'],0,2e-5)

# A tempting arbitrary relative normalization violates the fixed second holonomy.
u,v=wfun(np.array(.23+.19j),tau);wc=np.array([u,2*v]);
def bloch(w):
    u,v=w;den=abs(u)**2+abs(v)**2
    return np.array([2*np.real(np.conj(u)*v),2*np.imag(np.conj(u)*v),abs(u)**2-abs(v)**2])/den
u1,v1=wfun(np.array(.23+.19j+tau),tau)
wrong_error=float(np.linalg.norm(bloch(np.array([u1,2*v1]))-np.diag([1,-1,-1])@bloch(wc)))
if wrong_error<.1:raise AssertionError('negative control was not discriminating')

result={'checks':checks,'count':len(checks),'integrals':integrals,'variations':variations,'wrong_relative_normalization_boundary_error':wrong_error,'scope':'Double precision mesh/spectral and spherical-triangle controls. These are neither interval certificates nor a full quantum fluctuation determinant.'}
(OUT/'global.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
