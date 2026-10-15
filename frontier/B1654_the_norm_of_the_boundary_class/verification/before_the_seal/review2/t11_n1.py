# N1 mechanics at NON-named tau
import math
import numpy as np, pre2
ns = pre2.load(); cA=ns['cA']
for tau in (0.21+0.97j, 2.6j, 0.4+1.3j, 1.7j, 3.4j):
    worst=0; worstc=0
    for r in (2,3,4):
        v=[cA(r,tau,e) for e in (1e-3,1e-4,1e-5)]
        w2=[cA(r,tau,e,scale=2.0) for e in (1e-3,1e-4)]
        worst=max(worst,max(v)-min(v)); worstc=max(worstc,abs(((w2[1]-w2[0])/math.log(10))/(6*math.pi)-1))
    print(f"tau={tau}: spread over eps = {worst:.2e} (needs <1e-9);  control drift/6pi - 1 = {worstc:.2e} (needs <1e-6)")
