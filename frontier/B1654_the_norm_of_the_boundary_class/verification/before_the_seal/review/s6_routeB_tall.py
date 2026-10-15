import sys, time; sys.path.insert(0,'.')
import numpy as np, math, pre
ns = pre.load(); cA=ns['cA']; cB=ns['cB']
for tau in (2.9j, 2.1j):
    for r in (2,3):
        t0=time.time()
        a = cA(r, tau, 1e-5)
        b = cB(r, tau, 40)
        print("tau",tau,"r",r,"A",repr(a),"B",repr(b),"diff",abs(a-b), f"[{time.time()-t0:.0f}s]", flush=True)
