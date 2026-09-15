#!/usr/bin/env python3
"""#6 --- FRONT-OF-CENSUS BIAS. Every scan tonight walked the census from index 0.
Does the 2T-surjection rate differ between the front and a deeper slice?"""
import snappy, itertools, sys
E=[g for g in itertools.product(range(3),repeat=4) if (g[0]*g[3]-g[1]*g[2])%3==1]
def mul(g,h):
    a,b,c,d=g; e,f,x,y=h
    return ((a*e+b*x)%3,(a*f+b*y)%3,(c*e+d*x)%3,(c*f+d*y)%3)
def inv(g): a,b,c,d=g; return (d%3,(-b)%3,(-c)%3,a%3)
ID=(1,0,0,1)
def ev(w,m):
    r=ID
    for ch in w:
        g=m[ch.lower()]; r=mul(r, g if ch.islower() else inv(g))
    return r
def gen_size(gs):
    S={ID}; fr=[ID]
    while fr:
        x=fr.pop()
        for g in gs:
            y=mul(x,g)
            if y not in S: S.add(y); fr.append(y)
    return len(S)
def has_surj(G):
    gen=G.generators(); rel=G.relators(); n=len(gen)
    if n>3: return None
    for img in itertools.product(E,repeat=n):
        m={gen[i]:img[i] for i in range(n)}
        if all(ev(r,m)==ID for r in rel) and gen_size(img)==24: return True
    return False
lo,hi=int(sys.argv[1]),int(sys.argv[2])
C=snappy.OrientableCuspedCensus
n=0; hit=0; vols=[]
for i in range(lo,hi):
    try:
        M=C[i]; r=has_surj(M.fundamental_group())
        if r is None: continue
        n+=1; hit+=r; vols.append(float(M.volume()))
    except Exception: pass
print(f"  slice [{lo}:{hi}]  n={n}  surjects={hit}  rate={100*hit/max(n,1):.2f}%  "
      f"mean vol={sum(vols)/max(len(vols),1):.3f}")
