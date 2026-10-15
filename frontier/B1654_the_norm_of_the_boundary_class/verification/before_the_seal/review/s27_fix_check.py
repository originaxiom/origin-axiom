import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); R_A=ns['R_A']; nR2=ns['nR2']; TAUS=ns['TAUS']
for lam in ({2:1.0,3:2.0,4:4.0},{2:1.0,3:2.0,4:1.0}):
    out=[]
    for name,tau in TAUS.items():
        R=R_A(tau); shift=abs(-2*np.pi*sum(math.log(lam[r])*R[r]**2 for r in (2,3,4)))
        out.append(f"{name}:{shift/nR2(R):.3f}")
    print("lambda =",lam," shift/|R|^2 at named points:", "  ".join(out))
