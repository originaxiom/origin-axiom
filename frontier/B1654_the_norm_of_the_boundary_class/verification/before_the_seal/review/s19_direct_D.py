# D = sum_r c_r R_r^2 equals the convergent integral of W(z) = sum_r R_r^2 |S_r(z)|^2 over the torus (no cutoff needed)
import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
from numpy.polynomial.legendre import leggauss
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; S_A=ns['S_A']; rmax_np=ns['rmax_np']; vertex_angles=ns['vertex_angles']
def D_direct(tau, nth=96, nr=64):
    R=R_A(tau); br=vertex_angles(tau); xg,wg=leggauss(nth); xr,wr=leggauss(nr); tot=0.0
    for a,b in zip(br[:-1],br[1:]):
        th=0.5*(b-a)*xg+0.5*(b+a); wt=0.5*(b-a)*wg; rm=rmax_np(th,tau)
        r=0.5*rm[:,None]*(xr[None,:]+1); wrr=0.5*rm[:,None]*wr[None,:]
        z=r*np.exp(1j*th)[:,None]
        W=sum(R[k]**2*np.abs(S_A(k,z,tau))**2 for k in (2,3,4))
        tot+=np.sum(wt[:,None]*wrr*W*r)
    return tot, R
for tau in (0.21+1.33j, 1j, 0.13+1.07j, 2.6j, 0.5+0.9j):
    Dd,R=D_direct(tau)
    c={r:cA(r,tau,1e-5) for r in (2,3,4)}
    D=D_of(c,R)
    print(f"tau={tau}: D(c-sum)={D:.10f}  D(direct int of W)={Dd:.10f}  |diff|/|R|^2={abs(D-Dd)/nR2(R):.2e}")
