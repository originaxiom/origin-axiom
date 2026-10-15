# Item 6: cusp law at non-sealed heights (4.5, 5.5, 3.4, 6.0); convergence in (nth, ns); remainder fit.
import sys, math, time
import numpy as np, pre2
ns = pre2.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']
pi=math.pi
c2_0=-2*pi*math.log(2*pi); c34_0=-2*pi*math.log(pi/2); K=8*pi*(1-4*math.log(2))
print("K =",K)
res={}
for y in (3.4,4.5,5.5,6.0):
    tau=complex(0,y); R=R_A(tau); q=math.exp(-pi*y)
    t0=time.time()
    out={}
    for (nth,nss) in ((160,96),(240,144)):
        c={r:cA(r,tau,1e-5,nth=nth,ns=nss) for r in (2,3,4)}
        Dq=(D_of(c,R)/nR2(R)).real/q
        out[(nth,nss)]=(Dq,c)
    Dq1,c1=out[(160,96)]; Dq2,c2=out[(240,144)]
    print(f"y={y}: q={q:.3e}  D/(q|R|^2) [160,96]={Dq1:.8f} [240,144]={Dq2:.8f} diff={Dq1-Dq2:.2e}")
    print(f"      rem = D/(q|R|^2)-8pi^2 y-K = {Dq2-8*pi**2*y-K:.6f};  rem/(y q) = {(Dq2-8*pi**2*y-K)/(y*q):.2f}; rem/q = {(Dq2-8*pi**2*y-K)/q:.2f}")
    print(f"      c2-pi^2 y-c2_0={c2[2]-pi**2*y-c2_0:.3e}; (c3+c4)/2-c34_0={(c2[3]+c2[4])/2-c34_0:.3e}; (c3-c4)/q+16pi={(c2[3]-c2[4])/q+16*pi:.3e}   c-diff(160 vs 240): {max(abs(c1[r]-c2[r]) for r in c1):.2e}   [{time.time()-t0:.0f}s]")
    res[y]=Dq2-8*pi**2*y-K
