import sys, time, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); cA=ns['cA']
for tau in (2.1j, 2.9j, 1.03j, 0.31+1.58j):
    for r in (2,3,4):
        v=[cA(r,tau,e) for e in (1e-3,1e-4,1e-5)]
        w=[cA(r,tau,e,scale=2.0) for e in (1e-3,1e-4)]
        ref=cA(r,tau,1e-5,nth=200,ns=120)
        print(tau,r,"spread=%.2e"%(max(v)-min(v)),"ctrl drift/6pi-1=%.2e"%(((w[1]-w[0])/math.log(10))/(6*math.pi)-1),"vs fine quadrature: %.2e"%abs(v[2]-ref))
