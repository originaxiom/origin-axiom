import sys, time; sys.path.insert(0,'.')
import numpy as np, math, pre
ns = pre.load(); cA = ns['cA']
t0=time.time()
# convergence of route A at a non-sealed tau
tau = 0.21+1.33j
for r in (2,3,4):
    base = cA(r, tau, 1e-5)
    print("tau",tau,"r",r,"c(1e-5,96,64) =", repr(base))
    for (e,nth,ns_) in [(1e-3,96,64),(1e-4,96,64),(1e-5,160,96),(1e-5,48,32),(1e-5,32,24),(1e-8,96,64)]:
        v = cA(r, tau, e, nth=nth, ns=ns_)
        print("    eps",e,"nth",nth,"ns",ns_," diff from base:", v-base)
print("time", time.time()-t0)
