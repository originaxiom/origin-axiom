import time, math, numpy as np, sys
sys.path.insert(0,'.')
import b1654_routeA as B
t0=time.time()
for tau in (1j, 0.13+1.07j):
    c={r:B.cA(r,tau,1e-5) for r in (2,3,4)}
print('cA 6 evals', time.time()-t0)
# modular covariance: S: tau -> -1/tau ; T: tau -> tau+1
def cs(tau): return {r:B.cA(r,tau,1e-5) for r in (2,3,4)}
tau=0.13+1.07j
c0=cs(tau); cS=cs(-1/tau); cT=cs(tau+1)
print('c(tau)',c0); print('c(-1/tau)',cS); print('c(tau+1)',cT)
print('log|tau|*2pi', 2*math.pi*math.log(abs(tau)), ' pi log Im', math.pi*math.log(tau.imag), math.pi*math.log((-1/tau).imag))
