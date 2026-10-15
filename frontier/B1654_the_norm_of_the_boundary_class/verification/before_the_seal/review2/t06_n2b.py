# Item 5: N2b. Exec the instrument's own D_direct (text-extracted) at NON-named tau; compare with sum c_r R_r^2 (route A, eps=1e-5).
import re, math, time, sys, os
import numpy as np, pre2
ns = pre2.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']
SRC=pre2.SRC
m=re.search(r"(?m)^def D_direct\(.*?(?=^n2b = \{\})", SRC, re.S)
code=m.group(0)
exec(compile(code,"D_direct","exec"), ns)
D_direct=ns['D_direct']
taus=[0.21+0.97j, 0.4+1.3j, 1.7j, 2.6j, 3.4j, 4.5j, -0.45+0.93j, 0.5+0.9j, 0.35+1.05j, 0.17+2.4j]
print("tau | D_direct(96,96)/|R|^2 | c-sum D/|R|^2 | |diff|/|R|^2 (N2b stat) | direct(192,192) - direct(96,96) /|R|^2 | c-sum(160,96,eps1e-5) - c-sum(default) /|R|^2")
for tau in taus:
    R=R_A(tau)
    c={r:cA(r,tau,1e-5) for r in (2,3,4)}; Dc=D_of(c,R)
    Dd=D_direct(tau); Dd2=D_direct(tau,192,192)
    c2={r:cA(r,tau,1e-5,nth=160,ns=96) for r in (2,3,4)}; Dc2=D_of(c2,R)
    print(f"{tau}: {Dd/nR2(R):.10f} | {Dc/nR2(R):.10f} | {abs(Dd-Dc)/nR2(R):.2e} | {abs(Dd2-Dd)/nR2(R):.2e} | {abs(Dc2-Dc)/nR2(R):.2e}")
