import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']
vals=[]
for x in np.round(np.linspace(-0.5,0.5,21),4):
    tau=complex(x,2.0); R=R_A(tau); c={r:cA(r,tau,1e-5,nth=64,ns=48) for r in (2,3,4)}
    vals.append((abs(D_of(c,R))/nR2(R),x))
print("top row (Im tau = 2.0) |D|/|R|^2: min %.4f at x=%.2f ; max %.4f at x=%.2f"%(min(vals)+max(vals)))
