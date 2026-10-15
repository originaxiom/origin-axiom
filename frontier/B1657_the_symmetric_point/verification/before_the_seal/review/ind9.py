import numpy as np, math, json
src=open('run_copy.py').read().split("# ================================================================ S0 plumbing")[0]
import os; os.environ["OA_ROOT"]="."
exec(src)
w=W
# convergence of D_over_R2
for d in (1e-3,2.5e-4):
    phi=np.pi/7
    t=complex(w+d*np.exp(1j*phi))
    vals=[D_over_R2(t,n,n) for n in (24,48,96,160)]
    print(d,[abs(v-vals[-1]) for v in vals[:-1]], abs(vals[-1]))
# D at named taus vs stored
B=json.load(open('./frontier/B1654_the_norm_of_the_boundary_class/verification/the_norm_of_the_boundary_class.json'))
for k in ("i","t1","t2","t3"):
    print(k, abs(D_over_R2(TAUS[k])-complex(*B['N5']['D_over_R2'][k])))
# covariance of |D|/|R|^2 under gamma: tau -> -1/(tau+1) at a few generic tau
for t in (0.13+1.07j,0.3+1.6j,-0.2+0.95j):
    g=-1/(t+1)
    print("modular inv |D|/|R|^2:", abs(D_over_R2(t)), abs(D_over_R2(g)))
# phase covariance: D(g t) = e * D(t)?
for t in (0.13+1.07j,0.3+1.6j,-0.2+0.95j):
    g=-1/(t+1); R=Rvec(t); Rg=Rvec(g)
    D1=D_over_R2(t)*np.sum(np.abs(R)**2); D2=D_over_R2(g)*np.sum(np.abs(Rg)**2)
    print("D(gt)/D(t) =",D2/D1, " vs (t+1)^-1 =",1/(t+1), " ratio:",D2/D1*(t+1))
