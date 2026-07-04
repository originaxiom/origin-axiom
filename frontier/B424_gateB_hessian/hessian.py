"""B424 -- the Gate B Hessian spectrum on H^1(4_1, e6): the six frequencies, blind."""
import json, os
from fractions import Fraction as Fr
def F(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
exps=[1,4,5,7,8,11]
# the six Hessian eigenvalues = the per-exponent regularized torsions tau_m
tau={m: (-5)**m * (__import__('math').prod(F(2*j) for j in range(1,m+1)))**2 for m in exps}
print("the six Hessian eigenvalues (per-exponent torsions):")
for m in exps: print(f"  tau_{m} = {tau[m]}")
spectrum=[tau[m] for m in exps]
# the mass-ratio candidates: |tau_m2 / tau_m1| for all pairs
import itertools
ratios={}
for a,b in itertools.combinations(exps,2):
    r=Fr(abs(tau[b]),abs(tau[a]))
    ratios[f"{a}->{b}"]=r
# frequencies = log|tau_m|
import math
freqs={m: math.log(abs(tau[m])) for m in exps}
print("\nfrequencies log|tau_m|:", {m: round(freqs[m],3) for m in exps})
# BAR CHECK: do any ratios match SM mass ratios? (exact rationals of PDG central values)
SM_RATIOS={  # dimensionless SM mass ratios, central values
 "me/mmu":0.004836,"mmu/mtau":0.05946,"me/mtau":0.0002875,
 "mu/mc":0.00058,"mc/mt":0.00737,"md/ms":0.0503,"ms/mb":0.0233,
 "mu/md":0.47,"mtau/mt":0.01027,
}
matches=[]
allr=list(ratios.items())+[(f"1/{k}",Fr(1,1)/v if v!=0 else 0) for k,v in ratios.items()]
for name,r in allr:
    rf=float(r)
    for sm,val in SM_RATIOS.items():
        if val>0 and abs(rf-val)/val < 0.02:   # within 2%
            matches.append((name,str(r),sm,val,rf))
print("\nSM mass-ratio matches (<2%):", matches if matches else "NONE")
# characterize golden
def pc(n):
    n=abs(int(n)); s=set(); d=2
    while d*d<=n:
        while n%d==0: s.add(d); n//=d
        d+=1
    if n>1: s.add(n)
    return sorted(s)
allprimes=set()
for m in exps: allprimes|=set(pc(tau[m]))
print("prime content of the spectrum:", sorted(allprimes))
res=dict(spectrum={str(m):str(tau[m]) for m in exps},
         frequencies={str(m):freqs[m] for m in exps},
         sm_matches=[[a,b,c,d,e] for a,b,c,d,e in matches],
         prime_content=sorted(allprimes),
         verdict=("STRUCTURE/MATCH: an SM mass ratio matched -- ESCALATE" if matches
                  else "GOLDEN/NO-SM: Fibonacci spectrum, no SM mass ratio -- terminal confirmed"))
print("\nVERDICT:", res["verdict"])
json.dump(res, open("hessian.json","w"), indent=1)
print("DONE")
