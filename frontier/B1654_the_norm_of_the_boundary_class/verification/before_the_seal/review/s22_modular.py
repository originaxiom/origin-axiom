import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']
def Dn(tau):
    R=R_A(tau); c={r:cA(r,tau,1e-5,nth=128,ns=80) for r in (2,3,4)}
    return abs(D_of(c,R))/nR2(R)
tau=0.23+1.17j
for lab,t in (("tau",tau),("tau+1",tau+1),("-1/tau",-1/tau),("tau/(tau+1)",tau/(tau+1)),("(2tau+1)/(tau+1)",(2*tau+1)/(tau+1)),("-1/(tau+2)",-1/(tau+2))):
    print(f"{lab:18s} tau'={t:.4f}  |D|/|R|^2 = {Dn(complex(t)):.10f}")
