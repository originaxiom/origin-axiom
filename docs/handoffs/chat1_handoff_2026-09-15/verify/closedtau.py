import snappy, json
# Closed case: eta = 0 from ANY orientation-reversing symmetry (Reid, via Neumann-Yang).
# APS: 3 eta = 2 cs + tau mod 2  =>  cs = tau/2 mod 1.
#   tau EVEN -> cs = 0 mod 1   (R040's conclusion)
#   tau ODD  -> cs = 1/2 mod 1 (R040's conclusion FAILS)
# R040 gets tau even from Kawauchi, which needs FREENESS.
# QUESTION: is there a closed amphichiral hyperbolic manifold with tau ODD?
#   none  -> freeness is decorative in the closed theorem
#   some  -> freeness (or a substitute) is load-bearing, and those manifolds sit at 1/2
def tau_of(divs):
    t=0
    for d in divs:
        if d==0: continue
        n=d
        while n%2==0: n//=2
        if n!=d: t+=1
    return t
C=snappy.OrientableClosedCensus
N=len(C); print("closed census size",N,flush=True)
amph=[]; odd=[]; n=0
for i,M in enumerate(C):
    try:
        if not M.symmetry_group().is_amphicheiral(): continue
        n+=1
        divs=[d for d in M.homology().elementary_divisors() if d!=0]
        t=tau_of(divs)
        amph.append((M.name(),str(M.homology()),t))
        if t%2: odd.append((M.name(),str(M.homology()),t))
    except Exception: pass
    if (i+1)%1500==0: print(f"  {i+1}/{N} amph={n} tau_odd={len(odd)}",flush=True)
json.dump({"amph":amph,"odd":odd},open('closedtau.json','w'))
print(f"\n=== CLOSED amphichiral manifolds ===")
print(f"  amphichiral found : {len(amph)}")
print(f"  tau EVEN          : {len(amph)-len(odd)}")
print(f"  tau ODD           : {len(odd)}")
for x in odd[:12]: print(f"      {x[0]:22s} H1={x[1]:26s} tau={x[2]}")
print()
if odd:
    print("  => There ARE closed amphichiral manifolds with tau ODD. For those, eta=0 + APS")
    print("     gives cs = 1/2 mod 1, NOT 0. So R040's conclusion genuinely needs something")
    print("     that forces tau even -- freeness is LOAD-BEARING closed too, not decorative.")
    print("     Prediction: none of these admits a FREE orientation-reversing involution.")
else:
    print("  => No closed amphichiral manifold has tau odd in this census. Consistent with")
    print("     freeness being REMOVABLE in the closed theorem (Reid's eta argument alone).")
