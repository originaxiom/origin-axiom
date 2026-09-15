#!/usr/bin/env python3
"""Does B993's '1 in 3' hold beyond its 400-manifold sample?
Counts surjections pi_1(M) ->> 2T = SL(2,3) for census manifolds."""
import snappy, itertools, sys
# --- SL(2,3): 2x2 over F_3, det 1
E=[]
for a,b,c,d in itertools.product(range(3),repeat=4):
    if (a*d-b*c)%3==1: E.append((a,b,c,d))
assert len(E)==24
IDX={g:i for i,g in enumerate(E)}
def mul(g,h):
    a,b,c,d=g; e,f,x,y=h
    return ((a*e+b*x)%3,(a*f+b*y)%3,(c*e+d*x)%3,(c*f+d*y)%3)
def inv(g):
    a,b,c,d=g; return ((d)%3,(-b)%3,(-c)%3,(a)%3)   # det=1
ID=(1,0,0,1)
def evalword(w, img):
    r=ID
    for ch in w:
        g = img[ch.lower()]
        r = mul(r, g if ch.islower() else inv(g))
    return r
def gens_subgroup(gs):
    S={ID}; frontier=[ID]
    while frontier:
        x=frontier.pop()
        for g in gs:
            y=mul(x,g)
            if y not in S: S.add(y); frontier.append(y)
    return len(S)
def surj_count(G):
    gen=G.generators(); rel=G.relators()
    n=len(gen)
    if n>3: return None
    cnt=0
    for img in itertools.product(E, repeat=n):
        m={gen[i]:img[i] for i in range(n)}
        if all(evalword(r,m)==ID for r in rel):
            if gens_subgroup(img)==24: cnt+=1
    return cnt
LIM=int(sys.argv[1]) if len(sys.argv)>1 else 2000
n=0; hit=0; skipped=0
for i,M in enumerate(snappy.OrientableCuspedCensus):
    if i>=LIM: break
    try:
        c=surj_count(M.fundamental_group())
        if c is None: skipped+=1; continue
        n+=1; hit += (c>0)
    except Exception: skipped+=1
    if (i+1)%500==0:
        print(f"  {i+1}: n={n} hit={hit} ({100*hit/max(n,1):.1f}%) skipped={skipped}", flush=True)
print(f"\n=== pi_1(M) ->> 2T = SL(2,3) over the first {LIM} census manifolds ===")
print(f"  evaluated : {n}   (skipped, >3 generators: {skipped})")
print(f"  with a surjection : {hit}   =  {100*hit/max(n,1):.2f}%")
print(f"  B993's figure: ~1 in 3  = 33.3%")
# control
m4=snappy.Manifold('m004'); c4=surj_count(m4.fundamental_group())
print(f"\n  C-ALIVE  m004 raw surjections = {c4}   /|Aut(2T)|=24 -> {c4/24 if c4 else 0}")
print(f"           B993 records 48 raw -> exactly 2.   match: {c4==48}")
