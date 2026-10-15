import sys, time; sys.path.insert(0,'.')
import numpy as np, math, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']
vals={}
for y in (2.0,2.5,3.0,3.25,3.5,3.75):
    tau = complex(0,y); R=R_A(tau)
    c = {r: cA(r, tau, 1e-5, nth=160, ns=96) for r in (2,3,4)}
    q = math.exp(-math.pi*y)
    Dn = D_of(c,R)/nR2(R)
    vals[y] = (Dn.real/q, c)
    print(f"y={y}: q={q:.3e} D/(q|R|^2)={Dn.real/q:.8f} (imag {Dn.imag:.1e})  c2={c[2]:.8f} c3={c[3]:.10f} c4={c[4]:.10f}  (c3-c4)/q={(c[3]-c[4])/q:.6f}  c2-pi^2 y={c[2]-math.pi**2*y:.8f}")
ys = sorted(vals)
for a,b in zip(ys[:-1], ys[1:]):
    print(f"slope between {a} and {b}: {(vals[b][0]-vals[a][0])/(b-a)/(8*math.pi**2):.6f} x 8pi^2")
