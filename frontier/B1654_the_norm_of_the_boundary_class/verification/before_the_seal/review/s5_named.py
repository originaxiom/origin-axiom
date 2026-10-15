import sys, time; sys.path.insert(0,'.')
import numpy as np, math, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; TAUS=ns['TAUS']
for name in ("t1","t2","t3"):
    tau = TAUS[name]
    c = {r: cA(r, tau, 1e-5) for r in (2,3,4)}
    R = R_A(tau); D = D_of(c,R)
    pw = sorted([abs(c[2]-c[3]), abs(c[3]-c[4]), abs(c[2]-c[4])])
    print(name, "c=", {r: round(v,8) for r,v in c.items()}, " pairwise:", [round(x,5) for x in pw], " |D|/|R|^2 =", round(abs(D)/nR2(R),6))
    lam = {2:1.0,3:2.0,4:4.0}
    shift = abs(-2*np.pi*sum(math.log(lam[r])*R[r]**2 for r in (2,3,4)))
    print("    N4(a) shift/|R|^2 =", shift/nR2(R))
