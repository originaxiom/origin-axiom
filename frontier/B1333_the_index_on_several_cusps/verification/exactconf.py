"""EXACT confirmation over Q(zeta_12) on the richest sectors -- the ones with the most LIVE cusps,
where cusp-cancellation is possible and the mod-p answer most needs checking.

mod p is not a proof: r_1 is a DIFFERENCE of two ranks, each of which can drop mod p, so there is
no clean one-sided bound. These sectors are therefore redone in exact arithmetic.
"""
import sys, warnings, json, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
from collections import Counter
from q12 import *
from fi_lib import sym, blockdiag
from mcexact import analyse_exact, all_order3_chars, chi_on

GERMS=[tuple(int(c) for c in g) for g in os.environ.get('G','2,22').split(',')]
db=json.load(open('/tmp/sweep/covcache.json'))
def unser(r): return tuple(Fr(x) for x in r)
tally=Counter(); hits=[]; tested=0; broken=0
for tag in sys.argv[1:]:
    v=db[tag]; gens=v['gens']; rels=v['rels']; per=[tuple(x) for x in v['per']]
    rho={g:[[unser(v['rho'][g][i][j]) for j in range(2)] for i in range(2)] for g in gens}
    chars=all_order3_chars(gens,rels)
    print(f"{tag}: cusps={v['cusps']} gens={len(gens)} lift={'-I' if v['proj'] else '+I'} chars={len(chars)}",flush=True)
    for ms in GERMS:
        if v['proj'] and any(m%2 for m in ms):
            print(f"   germ {ms} skipped: odd power under a -I lift"); continue
        base={g:blockdiag([sym(rho[g],m) for m in ms]) for g in gens}
        d=sum(m+1 for m in ms)
        for psi in chars:
            V ={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
            Vd={g:scal(powe(OMEGA,(-psi[i])%3),base[g]) for i,g in enumerate(gens)}
            A=analyse_exact(gens,rels,per,V,d); B=analyse_exact(gens,rels,per,Vd,d)
            I=A['n']-B['n']; tested+=1
            ids={"r1+r1*=t1":A['r1']+B['r1']==A['t1'],
                 "t1=t0+t0*":A['t1']==A['t0']+B['t0'],
                 "I=(a0-a0*)+t0*-r1":I==(A['a0']-B['a0'])+B['t0']-A['r1'],
                 "I(V*)=-I(V)":(B['n']-A['n'])==-I}
            if not all(ids.values()): broken+=1; print("   ** identity failure **",[k for k,x in ids.items() if not x]); continue
            tally[(A['c'],A['live'],A['t0'],I)]+=1
            if I!=0: hits.append((tag,ms,psi,A,I))
        print(f"   germ Sym^{ms} done; running total {tested} sectors, {len(hits)} nonzero",flush=True)
print(f"\nEXACT SECTORS {tested} | identity-broken {broken}")
if tested==0: print("** NOTHING TESTED -- failure **"); sys.exit(1)
print(f"with >=2 live cusps: {sum(c for (cc,lv,t0,I),c in tally.items() if lv>=2)}")
print("(cusps, live cusps, t0, I) -> count")
for k in sorted(tally): print("   ",k,"->",tally[k])
print(f"NON-ZERO (EXACT): {len(hits)}")
for h in hits[:10]: print("   ",h[0],h[1],h[2],"t0s",h[3]['t0s'],"r1",h[3]['r1'],"I",h[4])
