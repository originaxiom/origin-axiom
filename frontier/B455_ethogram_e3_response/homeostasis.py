#!/usr/bin/env python3
"""B455 (part) — the homeostasis card's computation: perturb off kappa=-2, does the
dynamics return? kappa is CONSERVED by T1, so the prediction (S055 card): NO return —
the card retires with a computation. Verified exactly + the distance profile."""
from fractions import Fraction as F

def T1(v):
    x,y,z=v
    return (z,x,x*z-y)

def kappa(v):
    x,y,z=v
    return x*x+y*y+z*z-x*y*z-2

# start at the Markov point (3,3,3) on kappa=-2, perturb by eps in x
for eps in [F(1,10), F(1,100)]:
    v=(3+eps, F(3), F(3))
    k0=kappa(v)
    ks=[]
    for n in range(12):
        v=T1(v)
        ks.append(kappa(v))
    drift=[float(abs(k-k0)) for k in ks]
    print(f"eps={eps}: kappa(perturbed)={float(k0):+.6f} (vs -2); |kappa_n - kappa_0| over 12 steps: max={max(drift):.2e}")
    print(f"   -> kappa EXACTLY conserved along the orbit: {all(k==k0 for k in ks)}")
print()
print("VERDICT: the perturbed orbit NEVER returns to kappa=-2 (conserved off-surface, exactly).")
print("The homeostasis card RETIRES as predicted: no restoring response exists (conservative dynamics).")
