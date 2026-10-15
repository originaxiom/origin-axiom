import sys, time; sys.path.insert(0,'.')
import numpy as np, math, pre
ns = pre.load(); cA=ns['cA']; cB=ns['cB']
for tau in (0.31+1.58j, 0.45+0.9j, 0.1+4.9j):
    for r in (2,3,4):
        t0=time.time()
        a = cA(r, tau, 1e-5, nth=160, ns=96)
        b = cB(r, tau, 40)
        print("tau",tau,"r",r,"A",f"{a:.12f}","B",f"{b:.12f}","diff %.2e"%abs(a-b), f"[{time.time()-t0:.0f}s]", flush=True)
