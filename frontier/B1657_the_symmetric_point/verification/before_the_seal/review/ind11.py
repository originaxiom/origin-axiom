import numpy as np, math, json
src=open('run_copy.py').read().split("# ================================================================ S0 plumbing")[0]
import os; os.environ["OA_ROOT"]="."
exec(src)
# negative control for the isotropy: first-order variation of D at i and at t1 by direction
for name,t0 in (("i",1j),("t1",0.13+1.07j)):
    D0=D_over_R2(t0); d=2.5e-4; out=[]
    for j in range(6):
        phi=j*np.pi/3+np.pi/7
        Dv=D_over_R2(complex(t0+d*np.exp(1j*phi)))
        out.append(abs(Dv-D0)/d)
    print(name,"|dD|/delta by direction:",np.round(out,4)," spread:",np.ptp(out)/np.mean(out))
# graded control for S1: residual of P-eigen relation at omega+delta
P=np.array([[0,1,0],[0,0,-1],[1,0,0.]])
for d in (1e-1,1e-2,1e-3,1e-4):
    t=complex(W+d); R=Rvec(t); lam=(P@R)@R.conj()/np.linalg.norm(R)**2
    print(d, np.abs(P@R-lam*R).max()/np.linalg.norm(R))
