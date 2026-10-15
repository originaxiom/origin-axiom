import sys, time; sys.path.insert(0,'.')
import numpy as np, math, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']
K = None
for y in (4.5,5.5,6.5):
    tau = complex(0,y); R=R_A(tau)
    c = {r: cA(r, tau, 1e-5, nth=160, ns=96) for r in (2,3,4)}
    q = math.exp(-math.pi*y)
    Dn = D_of(c,R)/nR2(R)
    pred = 8*math.pi**2*y - 44.5655
    print(f"y={y}: q={q:.3e} D/(q|R|^2)={Dn.real/q:.8f} (imag {Dn.imag/q:.1e}) vs 8pi^2 y + K(3.75) = {pred:.5f};  c2-pi^2y={c[2]-math.pi**2*y:.10f}  (c3-c4)/(-16 pi q)={(c[3]-c[4])/(-16*math.pi*q):.8f}")
