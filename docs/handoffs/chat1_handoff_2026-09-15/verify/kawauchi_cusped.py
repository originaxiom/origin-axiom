#!/usr/bin/env python3
"""Does Kawauchi's CLOSED conclusion (Tor H_1 = A + A, tau even) still hold for the
orientation double covers of the CUSPED nonorientable census?

Kawauchi's Thm I/III are stated for closed manifolds. R040 uses them for step 1 of the
closed proof. If the conclusion ALSO holds cusped, the cusped gap is narrowed to the
peripheral-framing/eta half. If it FAILS, step 1 does not extend and the cusped case
needs a different mechanism. Either answer is worth having."""
import snappy, json
from collections import Counter

def primary_factors(divs):
    """elementary divisors -> multiset of prime-power cyclic factors"""
    out = []
    for d in divs:
        if d == 0: continue
        n = d; p = 2
        while n > 1:
            if n % p == 0:
                k = 0
                while n % p == 0: n //= p; k += 1
                out.append(p**k)
            p += 1
            if p*p > n and n > 1: out.append(n); break
    return Counter(out)

C = snappy.NonorientableCuspedCensus
N = len(C); res = {"n":0,"AA":0,"notAA":[],"tau_even":0,"tau_odd":[],"trivial":0}
for i, M in enumerate(C):
    try:
        D = M.orientation_cover()
        H = D.homology()
        divs = [d for d in H.elementary_divisors() if d != 0]
        pf = primary_factors(divs)
        res["n"] += 1
        if not pf: res["trivial"] += 1
        isAA = all(v % 2 == 0 for v in pf.values())
        if isAA: res["AA"] += 1
        else: res["notAA"].append((M.name(), str(H), dict(pf)))
        tau = sum(v for k,v in pf.items() if k % 2 == 0)     # 2-primary cyclic summands
        if tau % 2 == 0: res["tau_even"] += 1
        else: res["tau_odd"].append((M.name(), str(H), tau))
    except Exception as e:
        pass
    if (i+1) % 300 == 0: print(f"  {i+1}/{N}  AA={res['AA']}  notAA={len(res['notAA'])}", flush=True)

print("\n=== KAWAUCHI TORSION STRUCTURE ON THE CUSPED ORIENTATION COVERS ===")
print(f"  computed                         : {res['n']}/{N}")
print(f"  Tor H1 has the A+A form          : {res['AA']}")
print(f"  ...trivial torsion (vacuously)   : {res['trivial']}")
print(f"  NOT of A+A form                  : {len(res['notAA'])}")
for x in res["notAA"][:8]: print(f"      {x[0]:14s} H1={x[1]:28s} primary={x[2]}")
print(f"  tau (2-primary count) even       : {res['tau_even']}")
print(f"  tau ODD                          : {len(res['tau_odd'])}")
for x in res["tau_odd"][:8]: print(f"      {x[0]:14s} H1={x[1]:28s} tau={x[2]}")
json.dump({k:(v if not isinstance(v,list) else v[:50]) for k,v in res.items()},
          open('../out/r040/kawauchi.json','w'))
print()
if res["notAA"]:
    print("  => Kawauchi's CLOSED conclusion does NOT extend verbatim to the cusped covers.")
    print("     Step 1 of R040's proof is genuinely closed-only. The cusped universal needs")
    print("     a different route to tau, not just a fix to the peripheral framing.")
else:
    print("  => The conclusion HOLDS on all computed cusped covers. The cusped gap narrows")
    print("     to the peripheral-framing / eta half, as R040 conjectured.")
