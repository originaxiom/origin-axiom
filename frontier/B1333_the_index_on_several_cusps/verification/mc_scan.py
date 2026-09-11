"""Phase 1 -- the PRIOR question the wall names: is the index ever non-zero at all?

Not the trigger (that needs m004's own covers, phase 2). This asks the general question on
whatever manifolds are handed to it, with honest SL2(F_q) reps twisted by characters, and reports
ANY sector with I != 0 AND its identities intact -- which is exactly falsifier 6's condition.

Also reproduces the one-cusped case, where it must agree with B1297.
"""
import sys, warnings, itertools; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from collections import Counter
from index_lib import *
from mc_lib import check
from mc_val import find_reps, characters, symp

Q=int(__import__('os').environ.get('Q','13'))
NREP=int(__import__('os').environ.get('NREP','6'))
NCH=int(__import__('os').environ.get('NCH','8'))
MS=[1,2,3]
tally=Counter(); hits=[]; tested=0; broken=0
for nm in sys.argv[1:]:
    try:
        M=snappy.Manifold(nm); G=M.fundamental_group()
    except Exception as e:
        print(f"{nm}: {e}"); continue
    gens=list(G.generators()); rels=list(G.relators()); per=list(G.peripheral_curves())
    if len(gens)>3: print(f"{nm}: {len(gens)} generators -- skipped (search too wide)"); continue
    reps=find_reps(gens,rels,Q,cap=NREP); chars=characters(gens,rels,Q)
    seen=set(); n_here=0
    for rho2 in reps:
        for m in MS:
            base={g:symp(rho2[g],m,Q) for g in gens}; d=m+1
            for ch in chars[:NCH]:
                rho={g:[[(ch[i]*base[g][x][y])%Q for y in range(d)] for x in range(d)]
                     for i,g in enumerate(gens)}
                if any(word_eval(r,rho,Q,d)!=eye(d) for r in rels): continue
                key=tuple(tuple(map(tuple,rho[g])) for g in gens)
                if key in seen: continue
                seen.add(key)
                A,B,ids=check(gens,rels,per,rho,Q,d)
                tested+=1; n_here+=1
                if not all(ids.values()): broken+=1; continue
                I=A['I_exact']
                tally[(A['c'],A['inD'],A['t0'],I)]+=1
                if I!=0: hits.append((nm,m,ch,A,B))
    print(f"{nm}: cusps={M.num_cusps()} sectors={n_here}  nonzero so far={len(hits)}", flush=True)
print(f"\n{'='*66}\nTESTED {tested} sectors | identity-broken {broken}")
if tested==0: print("** NOTHING TESTED -- failure, not a pass **"); sys.exit(1)
live=sum(v for (c,dD,t0,I),v in tally.items() if t0>=1)
live2=sum(v for (c,dD,t0,I),v in tally.items() if t0>=2)
print(f"LIVE sectors (t0>=1; T5 forces I=0 when t0=0): {live}    of which t0>=2: {live2}")
print("(cusps, inDomain, t0, I) -> count")
for k in sorted(tally): print("   ",k,"->",tally[k])
print(f"\nNON-ZERO INDEX SECTORS: {len(hits)}")
for nm,m,ch,A,B in hits[:12]:
    print(f"   {nm} Sym^{m} chi={ch}: c={A['c']} t0={A['t0']}{A['t0s']} t1={A['t1']} "
          f"r1={A['r1']} I={A['I_exact']} inD={A['inD']} a0={A['a0']} a0*={B['a0']}")
