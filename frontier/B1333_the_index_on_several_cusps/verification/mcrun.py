"""Evaluate the multi-cusp index on m004's chiral multi-cusped covers, exactly over Q(zeta_12).

Reports per sector: the live-cusp count (psi trivial there), every identity, and I.
Tests the derivation's prediction that a psi-nontrivial cusp is invisible (t_0 = t_1 = 0).
"""
import sys, warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from fractions import Fraction as Fr
from collections import Counter
from q12 import *
from fi_lib import sym, blockdiag, wev
from recogmc import exact_rho
from mcexact import analyse_exact, all_order3_chars, chi_on

mI=scal((Fr(-1),Fr(0),Fr(0),Fr(0)),eye(2))
EVEN=[(2,),(4,),(2,2),(2,4),(2,2,2)]
ALL =[(1,),(2,),(3,),(4,),(1,1),(2,2),(2,4),(1,2),(2,2,2)]

def dual(rho,gens,d):
    out={}
    for x in gens:
        Ai=minv(rho[x]); out[x]=[[Ai[j][i] for j in range(d)] for i in range(d)]
    return out

M0=snappy.Manifold('m004')
tally=Counter(); hits=[]; pred_viol=[]; tested=0; broken=0; done=0
LIMIT=int(__import__('os').environ.get('LIMIT','8'))
for deg in range(int(__import__('os').environ.get('DMIN','5')),
                 int(__import__('os').environ.get('DMAX','11'))):
    for k,C in enumerate(M0.covers(deg)):
        if C.num_cusps()<2: continue
        try:
            if C.symmetry_group().is_amphicheiral(): continue
        except Exception: continue
        got=exact_rho(C)
        if got is None: print(f"d{deg}_{k}: unrecognised",flush=True); continue
        Mh,G,gens,rels,per,rho=got
        proj=any(wev(r,rho,2)==mI for r in rels)
        assert all(wev(r,rho,2) in (eye(2),mI) for r in rels)
        germs=EVEN if proj else ALL
        chars=all_order3_chars(gens,rels)
        nontriv=[p for p in chars if any(p)]
        print(f"d{deg}_{k}: cusps={C.num_cusps()} gens={len(gens)} "
              f"lift={'-I' if proj else '+I'} order-3 chars={len(nontriv)}",flush=True)
        for ms in germs:
            base={g:blockdiag([sym(rho[g],m) for m in ms]) for g in gens}
            d=sum(m+1 for m in ms)
            for psi in chars:
                V ={g:scal(powe(OMEGA,psi[i]),base[g]) for i,g in enumerate(gens)}
                Vd={g:scal(powe(OMEGA,(-psi[i])%3),base[g]) for i,g in enumerate(gens)}
                A=analyse_exact(gens,rels,per,V,d)
                B=analyse_exact(gens,rels,per,Vd,d)
                tested+=1
                I=A['n']-B['n']
                ids={"r1+r1*=t1":A['r1']+B['r1']==A['t1'],
                     "t1=t0+t0*":A['t1']==A['t0']+B['t0'],
                     "I=(a0-a0*)+t0*-r1":I==(A['a0']-B['a0'])+B['t0']-A['r1'],
                     "I(V*)=-I(V)":(B['n']-A['n'])==-I}
                if not all(ids.values()): broken+=1; continue
                # the prediction: cusp live  <=>  psi trivial on that cusp
                trivial=[i for i,(mu,lam) in enumerate(per)
                         if chi_on(mu,gens,psi)==0 and chi_on(lam,gens,psi)==0]
                livecusps=[i for i,t in enumerate(A['t0s']) if t>0]
                if set(livecusps)-set(trivial): pred_viol.append((deg,k,ms,psi,A))
                inD=(A['a0']==B['a0']) and (A['t0']==B['t0'])
                tally[(A['c'],len(trivial),A['live'],A['t0'],I,inD)]+=1
                if I!=0: hits.append((deg,k,ms,psi,A,B,I))
        done+=1
        if done>=LIMIT: break
    if done>=LIMIT: break
print(f"\n{'='*70}\nCOVERS EVALUATED {done} | SECTORS {tested} | identity-broken {broken}")
if tested==0: print("** NOTHING TESTED -- failure **"); sys.exit(1)
live2=sum(v for (c,tr,lv,t0,I,inD),v in tally.items() if lv>=2)
print(f"sectors with >=2 LIVE cusps (where cusp-cancellation is possible): {live2}")
print(f"prediction violations (a live cusp where psi is nontrivial): {len(pred_viol)}")
print("(cusps, psi-trivial cusps, live cusps, t0, I, inD) -> count")
for k in sorted(tally): print("   ",k,"->",tally[k])
print(f"\nNON-ZERO INDEX: {len(hits)}")
for h in hits[:10]: print("   d",h[0],"#",h[1],"Sym",h[2],"psi",h[3],"t0",h[4]['t0s'],"r1",h[4]['r1'],"I",h[6])
