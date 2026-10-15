import sys, time; sys.path.insert(0,'.')
import numpy as np, math, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; TAUS=ns['TAUS']
for name in ("omega","i"):
    tau = TAUS[name]
    c = {r: cA(r, tau, 1e-5) for r in (2,3,4)}
    R = R_A(tau)
    D = D_of(c,R)
    print(name, "c =", {r: repr(v) for r,v in c.items()})
    print("   spread:", max(c.values())-min(c.values()), " c2-c4:", c[2]-c[4], " c3-c2:", c[3]-c[2])
    print("   D/|R|^2 =", D/nR2(R), " |D|/|R|^2 =", abs(D)/nR2(R))
    # N4 control (a) shift
    lam = {2:1.0,3:2.0,4:4.0}
    shift = abs(-2*np.pi*sum(math.log(lam[r])*R[r]**2 for r in (2,3,4)))
    print("   N4(a) shift =", shift, " vs 1e-3|R|^2 =", 1e-3*nR2(R), "->", shift>1e-3*nR2(R))
    # general: |R_k^2 + 2 R_j^2|
    print("   |R_k^2 + 2 R_j^2| =", abs(R[3]**2+2*R[4]**2), "|R_j^2-R_i^2| =", abs(R[4]**2-R[2]**2))
