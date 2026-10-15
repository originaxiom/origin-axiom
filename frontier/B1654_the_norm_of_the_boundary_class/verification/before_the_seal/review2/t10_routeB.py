# N2: route B vs route A at NON-named tau (the named six are blind). Timing + agreement vs the 1e-8 threshold.
import sys, time, math
import numpy as np, pre2
ns = pre2.load(); cA=ns['cA']; cB=ns['cB']
for tau in (0.21+0.97j, 2.6j, 0.35+1.4j, 3.4j):
    for r in (2,3,4):
        t0=time.time()
        a=cA(r,tau,1e-5); b=cB(r,tau,40)
        print(f"tau={tau} r={r}: A={a:.12f} B={b:.12f} |diff|={abs(a-b):.2e}  [{time.time()-t0:.0f}s]", flush=True)
