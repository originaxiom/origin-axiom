#!/usr/bin/env python3
"""B481 reading-2 reproducer: SU(2)_k modular T-matrix det (exact rational phase)."""
from fractions import Fraction as Fr
def Tdet(k, framing=True):
    r=k+2; hs=[Fr(a*(a+2),4*r) for a in range(k+1)]; c=Fr(3*k,r)
    ph=sum(hs)-(Fr(k+1)*c/24 if framing else 0)
    return ph%1
for k in (3,13):
    print(f"k={k}: det T (framed)={Tdet(k)} , (theta only)={Tdet(k,False)} ; zeta5 phase in {{1/5..4/5}}")
print("h_2 at k=3 =", Fr(2*4,20), "-> twist theta_2 = zeta5^2 (eigenvalue, not det)")
