"""Referee check: base rate of surjections onto 2T = SL(2,3) over the one-cusped census."""
import snappy, warnings, sys, itertools, time; warnings.filterwarnings("ignore")
from snappy import Manifold
from collections import Counter

# ---- SL(2,3) ----
G=[]
for a,b,c,d in itertools.product(range(3),repeat=4):
    if (a*d-b*c)%3==1: G.append((a,b,c,d))
assert len(G)==24
idx={g:i for i,g in enumerate(G)}
def mul(x,y):
    a,b,c,d=x; e,f,g_,h=y
    return ((a*e+b*g_)%3,(a*f+b*h)%3,(c*e+d*g_)%3,(c*f+d*h)%3)
MUL=[[idx[mul(G[i],G[j])] for j in range(24)] for i in range(24)]
INV=[idx[next(g for g in G if mul(G[i],g)==(1,0,0,1))] for i in range(24)]
E=idx[(1,0,0,1)]

def word_eval(word, imgs):
    r=E
    for (gi,e) in word:
        x=imgs[gi]
        if e<0: x=INV[x]
        for _ in range(abs(e)): r=MUL[r][x]
    return r

def parse(rel, ngens):
    "SnapPy relator string like 'aabAB' -> list of (gen_index, exponent+-1)"
    out=[]
    for ch in rel:
        if ch.islower(): out.append((ord(ch)-97, 1))
        elif ch.isupper(): out.append((ord(ch)-65, -1))
        else: raise ValueError(ch)
    return out

def count_surjections(M, maxgens=3):
    fg=M.fundamental_group()
    n=fg.num_generators()
    if n>maxgens: return None, n
    rels=[parse(r,n) for r in fg.relators()]
    nsurj=0
    for imgs in itertools.product(range(24),repeat=n):
        ok=True
        for w in rels:
            if word_eval(w,imgs)!=E: ok=False; break
        if not ok: continue
        # surjective?
        gen=set([E]); frontier=[E]
        S=set(imgs)
        seen={E}; stack=[E]
        while stack:
            x=stack.pop()
            for s in S:
                y=MUL[x][s]
                if y not in seen: seen.add(y); stack.append(y)
        if len(seen)==24: nsurj+=1
    return nsurj, n

census=list(snappy.OrientableCuspedCensus(cusps=1))
print("one-cusped orientable census size:", len(census))
t0=time.time()
N=int(sys.argv[1]) if len(sys.argv)>1 else 400
counts=Counter(); admits=0; skipped=[]; genhist=Counter()
names=[]
for i,M in enumerate(census[:N]):
    ns,ng=count_surjections(M)
    genhist[ng]+=1
    if ns is None: skipped.append(M.name()); continue
    assert ns%24==0, (M.name(),ns)
    k=ns//24
    counts[k]+=1
    if k>0: admits+=1
    if k==2: names.append(M.name())
    if (i+1)%100==0: print(f"   ...{i+1} done ({time.time()-t0:.0f}s)", flush=True)
print(f"\nFirst {N} one-cusped orientable census manifolds:")
print("  generator-count histogram:", dict(genhist), " skipped (>3 gens):", len(skipped), skipped[:10])
print("  admit a surjection onto SL(2,3):", admits, f"({100*admits/N:.2f}%)")
print("  class-count distribution:", dict(sorted(counts.items())))
print("  admit exactly two:", counts[2], f"({100*counts[2]/N:.2f}%)")
print("  m004 count:", count_surjections(Manifold('m004'))[0]//24)
print("  tie list at count 2 (first 12):", names[:12])
