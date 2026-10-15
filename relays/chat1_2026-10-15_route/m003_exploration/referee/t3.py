import sys; sys.path.insert(0,'.')
from ref2 import *
SECT = {"up":(-3,5),"down":(3,-1),"lepton":(3,-9)}
taus = [mp.mpc(0.3,1.1), mp.mpc(-0.2,0.9), mp.mpc(0.71,0.43), mp.mpc(-1.37,2.6), mp.mpc(2.2,0.6), mp.mpc(0.05,0.35)]
for tau in taus:
    law = Rlaw(tau)
    print("tau",mp.nstr(tau,4),"R law s<-t, factor:",{s:(t,mp.nstr(f,6)) for s,(t,f) in law.items()})
    for (a,b) in ((1,2),(2,4)):
        for nm,(qu,qd) in SECT.items():
            vu = (mp.mpf(qu*b)/5, mp.mpf(qu*a)/5); vd = (mp.mpf(qd*b)/5, mp.mpf(qd*a)/5)
            _, o0, o = closure(tau, vu, vd, law)
            print(f"  ({a},{b}) {nm:6s} id:{ph5(o0)}  ijk:", [ph5(x) for x in o])
