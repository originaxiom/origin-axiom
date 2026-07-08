#!/usr/bin/env python3
"""B483: SU(2)_3 anyon data + Fibonacci fusion = golden substitution; figure-eight WRT golden."""
import mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps=30
phi=(1+mp.sqrt(5))/2
for a in range(4):
    print(f"a={a}: h={Fr(a*(a+2),20)}, qdim={mp.nstr(mp.sin((a+1)*mp.pi/5)/mp.sin(mp.pi/5),8)}")
print("phi^2=phi+1:", mp.nstr(phi**2,6),"=",mp.nstr(phi+1,6),"-> tau x tau = 1+tau = a->ab")
print("3:8:15 = a(a+2) for a=1,2,3 (conformal numerators, FORCED arithmetic, not gauge)")
