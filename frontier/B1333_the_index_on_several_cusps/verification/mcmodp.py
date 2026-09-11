"""Fast sweep of all 54 covers: recognise the holonomy EXACTLY over Q(zeta_12), then reduce
mod p for the linear algebra.  Recognition stays exact; only the ranks are mod p.

Direction of the error, stated: rank mod p <= rank over char 0, so r_1(mod p) <= r_1(exact),
hence I(mod p) >= I(exact).  A mod-p ZERO across several primes is therefore strong evidence of an
exact zero; a mod-p NON-zero is a lead to confirm exactly, never a result on its own.

p must be = 1 mod 12 so that sqrt3 and i both exist in F_p.
"""
import sys, warnings, itertools, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from fractions import Fraction as Fr
from collections import Counter
from index_lib import *
from mc_lib import check
from recogmc import exact_rho
from mcexact import all_order3_chars, chi_on
from q12 import eye as qeye, mm as qmm, minv as qminv, scal as qscal
from fi_lib import wev

def roots(p):
    s=next((x for x in range(p) if (x*x-3)%p==0), None)
    t=next((x for x in range(p) if (x*x+1)%p==0), None)
    return s,t
def red(z,p,s,t):
    a,b,c,d=z
    def f(q): return (q.numerator*pow(q.denominator,p-2,p))%p
    return (f(a)+f(b)*s + t*(f(c)+f(d)*s))%p
def redm(Mx,p,s,t): return [[red(x,p,s,t) for x in row] for row in Mx]

def sym_p(A,m,p):
    from math import comb
    d=m+1; out=[[0]*d for _ in range(d)]
    a,b=A[0]; c,dd=A[1]
    for j in range(d):
        coef=[0]*d
        for u in range(m-j+1):
            for v in range(j+1):
                cf=comb(m-j,u)*pow(a,m-j-u,p)*pow(c,u,p)*comb(j,v)*pow(b,j-v,p)*pow(dd,v,p)
                coef[u+v]=(coef[u+v]+cf)%p
        for i in range(d): out[i][j]=coef[i]
    return out
def blockdiag_p(ms):
    d=sum(len(m) for m in ms); out=[[0]*d for _ in range(d)]; o=0
    for m in ms:
        k=len(m)
        for i in range(k):
            for j in range(k): out[o+i][o+j]=m[i][j]
        o+=k
    return out

PRIMES=[int(x) for x in os.environ.get('PRIMES','13,37,61').split(',')]
EVEN=[(2,),(4,),(2,2),(2,4),(2,2,2)]
ALLG=[(1,),(2,),(3,),(4,),(1,1),(2,2),(1,2),(2,4),(2,2,2)]
mI=qscal((Fr(-1),Fr(0),Fr(0),Fr(0)),qeye(2))

M0=snappy.Manifold('m004')
tally=Counter(); hits=[]; viol=[]; tested=0; broken=0; covs=0; unrec=0
for deg in range(2,11):
    for k,C in enumerate(M0.covers(deg)):
        if C.num_cusps()<2: continue
        try:
            if C.symmetry_group().is_amphicheiral(): continue
        except Exception: continue
        got=exact_rho(C)
        if got is None: unrec+=1; continue
        Mh,G,gens,rels,per,rho=got
        proj=any(wev(r,rho,2)==mI for r in rels)
        germs=EVEN if proj else ALLG
        chars=all_order3_chars(gens,rels); covs+=1
        nh=0
        for p in PRIMES:
            s,t=roots(p)
            if s is None or t is None: continue
            w=(pow(3,(p-1)//3,p))            # primitive cube root of unity in F_p
            om=next((x for x in range(2,p) if pow(x,3,p)==1 and x!=1), None)
            if om is None: continue
            rp={g:redm(rho[g],p,s,t) for g in gens}
            if any(word_eval(r,rp,p,2)!=eye(2) and
                   word_eval(r,rp,p,2)!=[[p-1,0],[0,p-1]] for r in rels): continue
            for ms in germs:
                base={g:blockdiag_p([sym_p(rp[g],m,p) for m in ms]) for g in gens}
                d=sum(m+1 for m in ms)
                for psi in chars:
                    V={g:[[(pow(om,psi[i],p)*base[g][x][y])%p for y in range(d)] for x in range(d)]
                       for i,g in enumerate(gens)}
                    if any(word_eval(r,V,p,d)!=eye(d) for r in rels): continue
                    A,B,ids=check(gens,rels,per,V,p,d)
                    tested+=1; nh+=1
                    if not all(ids.values()): broken+=1; continue
                    I=A['I_exact']
                    trivial=[i for i,(mu,lam) in enumerate(per)
                             if chi_on(mu,gens,psi)==0 and chi_on(lam,gens,psi)==0]
                    livec=[i for i,x in enumerate(A['t0s']) if x>0]
                    if set(livec)-set(trivial): viol.append((deg,k,p,ms,psi,A))
                    tally[(A['c'],len(trivial),A['live'],A['t0'],I)]+=1
                    if I!=0: hits.append((deg,k,p,ms,psi,A,B,I))
        print(f"d{deg}_{k}: cusps={C.num_cusps()} gens={len(gens)} lift={'-I' if proj else '+I'} "
              f"chars={len(chars)} sectors={nh} nonzero_so_far={len(hits)}", flush=True)
print(f"\n{'='*70}\nCOVERS {covs} (unrecognised {unrec}) | SECTORS {tested} | identity-broken {broken}")
if tested==0: print("** NOTHING TESTED -- failure **"); sys.exit(1)
live=sum(v for (c,tr,lv,t0,I),v in tally.items() if t0>=1)
live2=sum(v for (c,tr,lv,t0,I),v in tally.items() if lv>=2)
print(f"LIVE sectors (t0>=1): {live}   sectors with >=2 LIVE CUSPS: {live2}")
print(f"prediction violations (live cusp where psi nontrivial): {len(viol)}")
print("(cusps, psi-trivial cusps, live cusps, t0, I) -> count")
for k in sorted(tally): print("   ",k,"->",tally[k])
print(f"\nNON-ZERO INDEX (mod p, leads to confirm exactly): {len(hits)}")
for h in hits[:15]:
    print(f"   d{h[0]}_{h[1]} p={h[2]} Sym{h[3]} psi={h[4]} t0s={h[5]['t0s']} r1={h[5]['r1']} I={h[7]}")
