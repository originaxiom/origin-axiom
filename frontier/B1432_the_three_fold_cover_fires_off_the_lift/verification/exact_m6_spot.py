import os, sys, json, time
os.environ['OA_CYC'] = '40'
import exact_lib as E
import cover_census as cc
from myindex import index as pindex
n, N = 6, 40
cases = [("1721-only firing (majority 0)", [0,7,18,7,3,2,3], [0,22,18,32,38,2,8]),
         ("1721-only firing (majority 0)", [0,4,11,29,36,39,1], [0,10,5,5,10,25,25])]
# add two modules that fire at the five good primes: take them from a fresh look at one locus at p=1481
ng, rels, mu, lam, tau = cc.cover(n); chars = cc.characters(rels, mu, ng, N)
Lr=[cc.letters(r) for r in rels]; Lm=cc.letters(mu); Ll=cc.letters(lam)
p=1481; z=pow(cc.primroot(p),(p-1)//N,p); got=0
for lc in chars:
    h1, ct = cc.cocycle(lc, rels, ng, N, z, p)
    for al in chars[:60]:
        i,_,_ = pindex(cc.module(lc, al, ct, ng, N, z, p), Lr, Lm, Ll)
        if i: cases.append(("fires at the good primes (I=%d)" % i, list(lc), list(al))); got+=1; break
    if got==2: break
out=[]
for label, lc, al in cases:
    t=time.time(); I = E.exact_index(n, N, tuple(lc), tuple(al))
    out.append(dict(case=label, lam=lc, alpha=al, exact_index_over_Q_zeta40=I, seconds=round(time.time()-t,1)))
    print(out[-1], flush=True)
json.dump(out, open("exact_m6_spot.json","w"), indent=1)
