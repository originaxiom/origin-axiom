import snappy, json
"""Large-scale test of R040's STEP 1 (Kawauchi): a closed orientable manifold with a FREE
orientation-reversing involution has Tor H_1 = A + A, hence tau EVEN.
Construction: fill the 1260 cusped nonorientable census -> closed nonorientable N ->
orientation double cover D. The deck transformation is a FREE orientation-reversing
involution, so Kawauchi applies to D. PREDICTION: tau(D) is ALWAYS even."""
def tau_of(divs):
    t=0
    for d in divs:
        if d==0: continue
        n=d
        while n%2==0: n//=2
        if n!=d: t+=1
    return t
SLOPES=[(1,0),(2,1),(3,1),(1,1),(4,1),(3,2)]
n=0; even=0; odd=[]; errs=0; AA=0; notAA=[]
C=snappy.NonorientableCuspedCensus
for i,M in enumerate(C):
    for s in SLOPES:
        try:
            N=M.copy()
            if N.num_cusps()!=1: continue
            N.dehn_fill(s)
            if N.solution_type()!='all tetrahedra positively oriented': continue
            if N.is_orientable(): continue
            D=N.orientation_cover()
            divs=[d for d in D.homology().elementary_divisors() if d!=0]
            t=tau_of(divs); n+=1
            if t%2==0: even+=1
            else: odd.append((str(N),str(D.homology()),t))
            # also the full Kawauchi form A+A on the primary decomposition
            from collections import Counter
            pf=Counter()
            for d in divs:
                m=d; p=2
                while m>1:
                    if m%p==0:
                        k=0
                        while m%p==0: m//=p; k+=1
                        pf[p**k]+=1
                    p+=1
                    if p*p>m and m>1: pf[m]+=1; break
            if all(v%2==0 for v in pf.values()): AA+=1
            else: notAA.append((str(N),str(D.homology())))
        except Exception: errs+=1
    if (i+1)%200==0: print(f"  {i+1}/{len(C)} tested={n} tau_even={even} tau_odd={len(odd)} notAA={len(notAA)}",flush=True)
json.dump({"n":n,"even":even,"odd":odd[:60],"notAA":notAA[:60],"AA":AA,"errs":errs},open('kawauchi_scale.json','w'))
print(f"\n=== KAWAUCHI STEP 1 AT SCALE ===")
print(f"  closed nonorientable fillings tested : {n}")
print(f"  tau EVEN                             : {even}")
print(f"  tau ODD                              : {len(odd)}   {odd[:6]}")
print(f"  Tor H1 of the A+A form               : {AA}")
print(f"  NOT of A+A form                      : {len(notAA)}  {notAA[:4]}")
print(f"  errors/skips                         : {errs}")
print()
print("  Kawauchi predicts tau EVEN and A+A for every one of these (the deck is free).")
