import re, numpy as np, pre2
ns = pre2.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']
m=re.search(r"(?m)^def D_direct\(.*?(?=^n2b = \{\})", pre2.SRC, re.S); exec(compile(m.group(0),"D_direct","exec"), ns); D_direct=ns['D_direct']
for tau in (0.4+3.0j, 0.5+2.5j, -0.37+4.4j, 0.45+1.0j, -0.5+0.95j):
    R=R_A(tau); c={r:cA(r,tau,1e-5) for r in (2,3,4)}; Dc=D_of(c,R); Dd=D_direct(tau); Dd2=D_direct(tau,192,192)
    print(f"{tau}: |D|/|R|^2={abs(Dc)/nR2(R):.3e}  N2b stat |Dd-Dc|/|R|^2 = {abs(Dd-Dc)/nR2(R):.2e}   quad (96 vs 192) = {abs(Dd2-Dd)/nR2(R):.2e}")
