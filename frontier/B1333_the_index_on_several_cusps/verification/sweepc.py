"""The evaluation, off the cache. Recognition already done and exact; here only the ranks.

mod p: rank(mod p) <= rank(char 0), so r_1(mod p) <= r_1(exact) and I(mod p) >= I(exact).
A mod-p ZERO across several primes is strong evidence of an exact zero; a mod-p NON-zero is a
lead to confirm exactly, never a result on its own.
"""
import sys, warnings, json, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
from collections import Counter
from index_lib import *
from mc_lib import check
from mcexact import all_order3_chars, chi_on

def roots(p):
    return (next((x for x in range(p) if (x*x-3)%p==0),None),
            next((x for x in range(p) if (x*x+1)%p==0),None))
class Bad(Exception): pass
def red(z,p,s,t):
    a,b,c,d=[Fr(x) for x in z]
    def f(q):
        if q.denominator%p==0: raise Bad()
        return (q.numerator*pow(q.denominator,p-2,p))%p
    return (f(a)+f(b)*s+t*(f(c)+f(d)*s))%p
def sym_p(A,m,p):
    from math import comb
    d=m+1; out=[[0]*d for _ in range(d)]
    a,b=A[0]; c,dd=A[1]
    for j in range(d):
        coef=[0]*d
        for u in range(m-j+1):
            for v in range(j+1):
                coef[u+v]=(coef[u+v]+comb(m-j,u)*pow(a,m-j-u,p)*pow(c,u,p)
                           *comb(j,v)*pow(b,j-v,p)*pow(dd,v,p))%p
        for i in range(d): out[i][j]=coef[i]
    return out
def bd(ms):
    d=sum(len(m) for m in ms); out=[[0]*d for _ in range(d)]; o=0
    for m in ms:
        k=len(m)
        for i in range(k):
            for j in range(k): out[o+i][o+j]=m[i][j]
        o+=k
    return out

PRIMES=[int(x) for x in os.environ.get('PRIMES','13,37,61').split(',')]
_G=os.environ.get('GERMS','lean')
if _G=='lean':  EVEN=[(2,),(2,2)];              ALLG=[(1,),(2,),(2,2)]
elif _G=='mid': EVEN=[(2,),(4,),(2,2),(2,4)];   ALLG=[(1,),(2,),(3,),(1,1),(2,2),(2,4)]
else:
    EVEN=[(2,),(4,),(2,2),(2,4),(4,4),(2,2,2)]
    ALLG=[(1,),(2,),(3,),(4,),(1,1),(1,2),(2,2),(2,4),(4,4),(2,2,2)]
db=json.load(open('/tmp/sweep/covcache.json'))
tags=sorted([t for t,v in db.items() if v.get('ok')],
            key=lambda t:(int(t.split('_')[0][1:]),int(t.split('_')[1])))
only=os.environ.get('ONLY')
if only: tags=[t for t in tags if t in only.split(',')]
tally=Counter(); hits=[]; viol=[]; tested=0; broken=0; skipped=0; covs=0
for tag in tags:
    v=db[tag]; gens=v['gens']; rels=v['rels']; per=[tuple(x) for x in v['per']]
    germs=EVEN if v['proj'] else ALLG
    chars=all_order3_chars(gens,rels); covs+=1; n=0
    for p in PRIMES:
        s,t=roots(p)
        if s is None or t is None: continue
        om=next((x for x in range(2,p) if pow(x,3,p)==1),None)
        if om is None: continue
        try: rp={g:[[red(v['rho'][g][i][j],p,s,t) for j in range(2)] for i in range(2)] for g in gens}
        except Bad: skipped+=1; continue
        if any((rp[g][0][0]*rp[g][1][1]-rp[g][0][1]*rp[g][1][0])%p==0 for g in gens): skipped+=1; continue
        if any(word_eval(r,rp,p,2) not in (eye(2),[[p-1,0],[0,p-1]]) for r in rels): skipped+=1; continue
        for ms in germs:
            base={g:bd([sym_p(rp[g],m,p) for m in ms]) for g in gens}; d=sum(m+1 for m in ms)
            for psi in chars:
                V={g:[[(pow(om,psi[i],p)*base[g][x][y])%p for y in range(d)] for x in range(d)]
                   for i,g in enumerate(gens)}
                if any(word_eval(r,V,p,d)!=eye(d) for r in rels): continue
                A,B,ids=check(gens,rels,per,V,p,d); tested+=1; n+=1
                if not all(ids.values()): broken+=1; continue
                I=A['I_exact']
                triv=[i for i,(mu,lam) in enumerate(per)
                      if chi_on(mu,gens,psi)==0 and chi_on(lam,gens,psi)==0]
                livec=[i for i,x in enumerate(A['t0s']) if x>0]
                if set(livec)-set(triv): viol.append((tag,p,ms,psi,A['t0s'],triv))
                tally[(A['c'],A['live'],A['t0'],I)]+=1
                if I!=0: hits.append((tag,p,ms,psi,A,B,I))
    print(f"{tag}: cusps={v['cusps']} gens={len(gens)} lift={'-I' if v['proj'] else '+I'} "
          f"chars={len(chars)} sectors={n} nonzero={len(hits)}",flush=True)
print(f"\n{'='*72}\nCOVERS {covs} | SECTORS {tested} | identity-broken {broken} | prime-skips {skipped}")
if tested==0: print("** NOTHING TESTED -- failure, not a pass **"); sys.exit(1)
live=sum(c for (cc,lv,t0,I),c in tally.items() if t0>=1)
l2  =sum(c for (cc,lv,t0,I),c in tally.items() if lv>=2)
print(f"LIVE sectors (t0>=1): {live}    sectors with >=2 LIVE CUSPS: {l2}")
print(f"prediction violations (live cusp where psi nontrivial): {len(viol)}")
print("(cusps, live cusps, t0, I) -> count")
for k in sorted(tally): print("   ",k,"->",tally[k])
print(f"\nNON-ZERO INDEX: {len(hits)}")
for h in hits[:15]: print(f"   {h[0]} p={h[1]} Sym{h[2]} psi={h[3]} t0s={h[4]['t0s']} r1={h[4]['r1']} I={h[6]}")
