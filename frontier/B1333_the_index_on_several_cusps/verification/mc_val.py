"""Validate the multi-cusp index.

Representations are found HONESTLY by brute force: enumerate rho: pi_1 -> SL2(F_q) and keep the
tuples that kill every relator.  Then twist by F_q^x characters of H_1 (which breaks self-duality --
the whole point, since a self-dual V gives I = 0 by T3 and would test nothing) and take Sym^m.

GUARD: if no sector is actually tested, this reports FAILURE, not success.
"""
import sys, warnings, itertools; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from index_lib import *
from mc_lib import analyse_mc, check, dual_rho

def sl2(q):
    out=[]
    for a in range(q):
        for b in range(q):
            for c in range(q):
                for d in range(q):
                    if (a*d-b*c)%q==1: out.append([[a,b],[c,d]])
    return out

def find_reps(gens,rels,q,cap=40):
    S=sl2(q); out=[]
    for tup in itertools.product(S,repeat=len(gens)):
        rho=dict(zip(gens,tup))
        if all(word_eval(r,rho,q,2)==eye(2) for r in rels):
            out.append(rho)
            if len(out)>=cap: break
    return out

def expsum(word,gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v

def characters(gens,rels,q):
    """homs pi_1 -> F_q^x : assignments of (q-1)-th roots killing the relators"""
    out=[]
    for tup in itertools.product(range(1,q),repeat=len(gens)):
        ok=True
        for r in rels:
            v=expsum(r,gens); val=1
            for x,e in zip(tup,v): val=(val*pow(x,e%(q-1),q))%q
            if val!=1: ok=False; break
        if ok: out.append(tup)
    return out

def symp(A,m,q):
    from math import comb
    d=m+1; out=[[0]*d for _ in range(d)]
    a,b=A[0]; c,dd=A[1]
    for j in range(d):
        coef=[0]*d
        for s in range(m-j+1):
            for t in range(j+1):
                cf=comb(m-j,s)*pow(a,m-j-s,q)*pow(c,s,q)*comb(j,t)*pow(b,j-t,q)*pow(dd,t,q)
                coef[s+t]=(coef[s+t]+cf)%q
        for i in range(d): out[i][j]=coef[i]
    return out

if __name__=="__main__":
    Q=13
    names=sys.argv[1:] or ['m129']
    tested=0; failures=[]
    for nm in names:
        M=snappy.Manifold(nm); G=M.fundamental_group()
        gens=list(G.generators()); rels=list(G.relators()); per=list(G.peripheral_curves())
        print(f"\n=== {nm} === cusps={M.num_cusps()} gens={gens} rels={rels}", flush=True)
        reps=find_reps(gens,rels,Q,cap=25)
        chars=characters(gens,rels,Q)
        print(f"    honest SL2(F_{Q}) reps: {len(reps)}   characters: {len(chars)}", flush=True)
        seen=set()
        for rho2 in reps[:8]:
            for m in (1,2):
                base={g:symp(rho2[g],m,Q) for g in gens}; d=m+1
                for ch in chars[:6]:
                    rho={g:[[ (ch[i]*base[g][x][y])%Q for y in range(d)] for x in range(d)]
                         for i,g in enumerate(gens)}
                    if any(word_eval(r,rho,Q,d)!=eye(d) for r in rels): continue
                    key=tuple(tuple(map(tuple,rho[g])) for g in gens)
                    if key in seen: continue
                    seen.add(key)
                    A,B,ids=check(gens,rels,per,rho,Q,d)
                    tested+=1
                    if not all(ids.values()):
                        failures.append((nm,m,ch,[k for k,v in ids.items() if not v],A,B))
        print(f"    sectors tested so far: {tested}", flush=True)
    print(f"\n{'='*60}\nSECTORS TESTED: {tested}")
    if tested==0:
        print("** NOTHING WAS TESTED -- this is a FAILURE of the validator, not a pass **"); sys.exit(1)
    print(f"IDENTITY FAILURES: {len(failures)}")
    for f in failures[:5]: print("   ",f[0],"m",f[1],"chi",f[2],"->",f[3])
    print("ALL IDENTITIES HOLD" if not failures else "** IDENTITIES BROKEN **")
