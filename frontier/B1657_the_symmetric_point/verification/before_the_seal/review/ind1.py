# independent re-derivation (mpmath thetas, no import of the instrument)
import numpy as np, mpmath as mp
mp.mp.dps = 40
def th234(tau):
    q = mp.exp(1j*mp.pi*tau)
    return [mp.jtheta(j,0,q) for j in (2,3,4)]
def thp(tau):
    q = mp.exp(1j*mp.pi*tau)
    return mp.jtheta(1,0,q,1)   # d/dz theta1(z|q), z in radians; = pi * (d/d(pi z))
def T2(tau): return [t**2 for t in th234(tau)]
def Rv(tau):
    t2,t3,t4 = th234(tau)
    # B1654 convention: theta_r(z) = theta_r(pi z), theta1'(0)=d/dz = pi*jtheta1'(0) ... check = 2 pi eta^3
    tp = mp.jtheta(1,0,mp.exp(1j*mp.pi*tau),1)*mp.pi   # d/dz theta1(pi z) at 0
    return [-t2**2/tp, 1j*t3**2/tp, -t4**2/tp]
tau=mp.mpc(0.13,1.07)
q=mp.exp(1j*mp.pi*tau)
eta = mp.exp(1j*mp.pi*tau/12)*mp.nprod(lambda n:1-mp.exp(2j*mp.pi*tau*n),[1,mp.inf])
print("theta1'(0) vs 2 pi eta^3:", abs(mp.jtheta(1,0,q,1)*mp.pi - 2*mp.pi*eta**3))
# fit M in theta^2 basis exactly: M = B A^{-1} with 3 generic taus, check on a 4th
taus=[mp.mpc(0.13,1.07),mp.mpc(-0.21,0.93),mp.mpc(0.33,1.4),mp.mpc(0.05,0.8)]
A=mp.matrix(3,3);B=mp.matrix(3,3)
for k in range(3):
    t=taus[k]; a=T2(t); b=[x/(t+1) for x in T2(-1/(t+1))]
    for r in range(3): A[r,k]=a[r]; B[r,k]=b[r]
M = B*A**-1
print("M (theta^2 basis):"); mp.nprint(M,6)
t=taus[3]; a=mp.matrix(T2(t)); b=mp.matrix([x/(t+1) for x in T2(-1/(t+1))])
print("check 4th tau:", mp.norm(M*a-b))
Dg=mp.diag([-1,1j,-1]); MR=Dg*M*Dg**-1
print("M in R basis:"); mp.nprint(MR,6)
