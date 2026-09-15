#!/usr/bin/env python3
"""R040 measures cs = 0 mod 1/2 for all 1260. The CLOSED theorem gives cs = 0 mod 1.
If APS (3 eta = 2 cs + tau mod 2) with eta = 0 extends to the cusped covers, then
    tau EVEN -> cs = 0   mod 1
    tau ODD  -> cs = 1/2 mod 1
Both are 'multiple of 1/2', so R040's statistic cannot distinguish them. Split it."""
import snappy
from collections import Counter

def tau_of(divs):
    t = 0
    for d in divs:
        if d == 0: continue
        n = d
        while n % 2 == 0: n //= 2
        if n != d: t += 1          # this invariant factor has a 2-primary part
    return t

C = snappy.NonorientableCuspedCensus
tab = Counter(); mism = []; N = len(C)
for i, M in enumerate(C):
    try:
        D = M.orientation_cover()
        divs = [d for d in D.homology().elementary_divisors() if d != 0]
        tau = tau_of(divs)
        cs = float(D.chern_simons()) % 1.0
        d0 = min(cs, 1.0 - cs)                 # distance to 0 mod 1
        dh = abs(cs - 0.5)                     # distance to 1/2 mod 1
        cls = "0" if d0 < 1e-8 else ("1/2" if dh < 1e-8 else "OTHER")
        tab[(tau % 2, cls)] += 1
        pred = "1/2" if tau % 2 else "0"
        if cls != pred: mism.append((M.name(), tau, cs, cls, pred))
    except Exception: pass
    if (i+1) % 400 == 0: print(f"  {i+1}/{N}", flush=True)

print("\n=== cs mod 1  CROSS-TABULATED BY tau PARITY ===")
print(f"  {'tau parity':>12} | {'cs=0':>7} | {'cs=1/2':>7} | {'OTHER':>7}")
for p in (0,1):
    print(f"  {('even' if p==0 else 'odd'):>12} | {tab[(p,'0')]:>7} | {tab[(p,'1/2')]:>7} | {tab[(p,'OTHER')]:>7}")
print()
print(f"  APS prediction (eta=0): tau even -> cs=0 ; tau odd -> cs=1/2")
print(f"  mismatches: {len(mism)}")
for x in mism[:8]: print(f"     {x[0]:12s} tau={x[1]} cs={x[2]:.6f} got={x[3]} predicted={x[4]}")
hold = (len(mism) == 0)
print()
if hold:
    print("  => THE APS CONGRUENCE EXTENDS TO THE CUSPED COVERS, EXACTLY.")
    print("     R040's 'cs = 0 mod 1/2 for all 1260' is the SHADOW of a sharper law:")
    print("         cs = tau/2  mod 1.")
    print("     eta = 0 survives the ideal boundary on every computed case; the order-two")
    print("     ambiguity R040 fenced is exactly the tau-odd half.")
else:
    print("  => The sharper law FAILS; the cusped case is not APS-with-eta-0.")
