#!/usr/bin/env python3
"""B479 addendum reproducer: the divisor-union law + closed-form field Delta_d=tau^2(tau^2-8)."""
import sympy as sp
z = sp.symbols('z')
def contributing_divisors(m):
    out=[]
    for d in range(3, m+1):
        if m % d: continue
        tau = sp.nsimplify(2*sp.cos(2*sp.pi/d))
        if tau == 0 or abs(complex(tau).real) >= 2-1e-9: continue
        out.append(d)
    return out
for m in [1,2,4,8,9,12,15]:
    print(f"m={m}: contributing d>=3 = {contributing_divisors(m)}")
for d in [3,8,12]:
    tau=sp.nsimplify(2*sp.cos(2*sp.pi/d))
    print(f"d={d}: Delta={sp.simplify(tau**2*(tau**2-8))}")

