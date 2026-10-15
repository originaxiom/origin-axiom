import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']
pi=math.pi
c2_0=-2*pi*math.log(2*pi); c34_0=-2*pi*math.log(pi/2); K=8*pi*(1-4*math.log(2))
print("closed forms: c2^0 = -2pi ln(2pi) =",c2_0," c3^0=c4^0 = -2pi ln(pi/2) =",c34_0," K = 8pi(1-4 ln2) =",K)
for y in (3.0,4.5,5.5):
    tau=complex(0,y); R=R_A(tau)
    c={r:cA(r,tau,1e-5,nth=160,ns=96) for r in (2,3,4)}
    q=math.exp(-pi*y)
    Dq=(D_of(c,R)/nR2(R)).real/q
    print(f"y={y}: c2-pi^2 y - c2^0 = {c[2]-pi**2*y-c2_0:.2e};  (c3+c4)/2 - c34^0 = {(c[3]+c[4])/2-c34_0:.2e};  (c3-c4)/q + 16 pi = {(c[3]-c[4])/q+16*pi:.2e};  D/(q|R|^2) - 8pi^2 y - K = {Dq-8*pi**2*y-K:.5f}   (516*y*q = {516*y*q:.5f})")
