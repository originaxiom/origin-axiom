import time, numpy as np, pre2
ns = pre2.load(); cA=ns['cA']; cB=ns['cB']
for tau in (-0.5+0.88j, 0.5+0.9j, 0.01+1.02j):
    for r in (2,3,4):
        t0=time.time(); a=cA(r,tau,1e-5); b=cB(r,tau,40)
        print(f"tau={tau} r={r}: |A-B|={abs(a-b):.2e} [{time.time()-t0:.0f}s]", flush=True)
