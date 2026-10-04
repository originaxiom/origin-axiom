"""TIER 2 (FRAGILE). One-loop unification through a parity-symmetric LR stage.
FRAGILITY: ONE-LOOP, ONE IMPLEMENTATION. Needs two-loop running, threshold corrections, and an
independent code. Proton lifetime is inherently uncertain by ~1 order; tau ~ M_U^4 amplifies it."""
import numpy as np, math
k=1/(2*math.pi); a1i=(3/5)*(1-0.23122)*127.952; a2i=0.23122*127.952; a3i=1/0.1179
b1e=3/5*(-7/3)+2/5*7
A=np.array([[-7*k,-7*k,1],[-19/6*k,-7/3*k,1],[41/10*k,b1e*k,1]]); t1,t2,aUi=np.linalg.solve(A,[a3i,a2i,a1i])
MR=91.1876*math.exp(t1); MU=MR*math.exp(t2)
tau=MU**4/((1/aUi)**2*0.938272**5)*6.582e-25/3.156e7
print(f"M_R={MR:.2e} GeV  M_U={MU:.2e} GeV  alpha_U^-1={aUi:.2f}  tau_p~{tau:.1e} yr (order of magnitude)")
