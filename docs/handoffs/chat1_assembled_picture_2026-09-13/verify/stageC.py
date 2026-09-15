#!/usr/bin/env python3
"""STAGE C --- census-scale claims, re-derived from scratch."""
import snappy, json, math, time
from collections import Counter
R_=[]; t0=time.time()
def rec(tag,claim,ok,detail=""):
    R_.append((tag,claim,ok,detail)); print(f"  [{'PASS' if ok else 'FAIL'}] {tag:10s} {claim:50s} {detail}",flush=True)
def tau_of(divs):
    t=0
    for d in divs:
        if d==0: continue
        n=d
        while n%2==0: n//=2
        if n!=d: t+=1
    return t

# --- F2: R040 census + Kawauchi failure, ONE pass
C=snappy.NonorientableCuspedCensus; n=0; zero=0; maxr=0.0; tauodd=0; notAA=0; ctl=0
for i,M in enumerate(C):
    try:
        D=M.orientation_cover()
        if D.is_orientable(): ctl+=1
        cs=float(D.chern_simons())%0.5; r=min(cs,0.5-cs); maxr=max(maxr,r)
        n+=1; zero+= (r<1e-9)
        divs=[d for d in D.homology().elementary_divisors() if d!=0]
        if tau_of(divs)%2: tauodd+=1
        pf=Counter()
        for d in divs:
            m=d;p=2
            while m>1:
                if m%p==0:
                    k=0
                    while m%p==0: m//=p;k+=1
                    pf[p**k]+=1
                p+=1
                if p*p>m and m>1: pf[m]+=1;break
        if not all(v%2==0 for v in pf.values()): notAA+=1
    except Exception: pass
    if (i+1)%400==0: print(f"    ...{i+1}/{len(C)}",flush=True)
rec("F2.1","R040 census cs=0 mod 1/2", n==1260 and zero==1260, f"{zero}/{n}, max residue {maxr:.2e}")
rec("F2.2","C-ALIVE all covers orientable", ctl==1260, f"{ctl}/1260")
rec("F2.3","Kawauchi tau EVEN fails cusped", tauodd==251, f"tau-odd = {tauodd} (claimed 251)")
rec("F2.4","A+A form fails cusped", notAA==697, f"notAA = {notAA} (claimed 697)")
print(f"  [stage C1 {time.time()-t0:.0f}s]",flush=True)

# --- F3: amphichiral population, quarter class, freeness separation
amph=[]; 
for i,M in enumerate(snappy.OrientableCuspedCensus):
    try:
        G=M.symmetry_group()
        if not G.is_amphicheiral(): continue
        cs=float(M.chern_simons())%0.5
        cls=0 if min(cs,0.5-cs)<1e-8 else (1 if abs(cs-0.25)<1e-8 else 9)
        isos=G.isometries()
        def dt(g):
            m=g.cusp_maps()[0]; return int(m[0,0]*m[1,1]-m[0,1]*m[1,0])
        rev=[k for k,g in enumerate(isos) if dt(g)==-1]
        def order(k):
            cur=k
            for j in range(2,40):
                cur=G.multiply_elements(cur,k)
                if cur==0: return j
            return None
        has2 = 2 in ({order(k) for k in rev}-{None})
        amph.append((str(M).split('(')[0], cls, has2))
    except Exception: pass
    if (i+1)%40000==0: print(f"    ...cusped {i+1} amph={len(amph)}",flush=True)
z=[a for a in amph if a[1]==0]; q=[a for a in amph if a[1]==1]; o=[a for a in amph if a[1]==9]
rec("F3.1","amphichiral population", len(amph)==283, f"{len(amph)} (claimed 283)")
rec("F3.2","classes are 0 and 1/4 ONLY", len(o)==0, f"class0={len(z)} class1/4={len(q)} OTHER={len(o)}")
rec("F3.3","quarter class populated", len(q)==88, f"{len(q)} (claimed 88)")
rec("F3.4","involution does NOT discriminate", sum(1 for a in q if a[2])==21,
    f"{sum(1 for a in q if a[2])} quarter-class WITH an involution (claimed 21)")
cov=set()
for M in snappy.NonorientableCuspedCensus:
    try:
        for nm in M.orientation_cover().identify(): cov.add(str(nm).split('(')[0])
    except Exception: pass
qf=[a for a in q if a[0] in cov]; zf=[a for a in z if a[0] in cov]
rec("F3.5","NO quarter-class manifold is a cover", len(qf)==0, f"{len(qf)}/{len(q)}")
rec("F3.6","C-ALIVE: class-0 covers exist", len(zf)>0, f"{len(zf)}/{len(z)} are covers")
m4=snappy.Manifold('m004'); m3=snappy.Manifold('m003')
rec("F3.7","m004 class 0, m003 class 1/4, same volume",
    abs(float(m4.volume())-float(m3.volume()))<1e-9
    and min(float(m4.chern_simons())%0.5,0.5-float(m4.chern_simons())%0.5)<1e-8
    and abs(float(m3.chern_simons())%0.5-0.25)<1e-8)
print(f"  [stage C2 {time.time()-t0:.0f}s]",flush=True)

# --- closed side
ca=[]; 
for M in snappy.OrientableClosedCensus:
    try:
        if not M.symmetry_group().is_amphicheiral(): continue
        ca.append(tau_of([d for d in M.homology().elementary_divisors() if d!=0]))
    except Exception: pass
rec("F3.8","closed amphichiral, tau split", len(ca)==37 and sum(1 for t in ca if t%2)==11,
    f"{len(ca)} amphichiral, tau-odd {sum(1 for t in ca if t%2)} (claimed 37/11)")
json.dump(R_, open('../out/stageC.json','w'))
f=[r for r in R_ if not r[2]]
print(f"\n  STAGE C: {len(R_)-len(f)}/{len(R_)} PASS   elapsed {time.time()-t0:.0f}s")
