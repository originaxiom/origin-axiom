import math
import numpy as np, pre2
ns = pre2.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']
def Dn(tau, nth=128, nss=80):
    R=R_A(tau); c={r:cA(r,tau,1e-5,nth=nth,ns=nss) for r in (2,3,4)}
    return abs(D_of(c,R))/nR2(R)
tau=0.23+1.17j
base=Dn(tau)
print("base", base)
for lab,t in (("tau+1",tau+1),("-conj(tau)",-np.conj(tau)),("-1/tau",-1/tau),("tau/(tau+1)",tau/(tau+1)),("(2tau+1)/(tau+1)",(2*tau+1)/(tau+1)),("-1/(tau+2)",-1/(tau+2))):
    t=complex(t)
    v=Dn(t, 160, 96)
    print(f"{lab:18s} tau'={t:.4f}  |D|/|R|^2 = {v:.10f}   diff = {abs(v-base):.2e}")
