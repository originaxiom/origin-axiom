import snappy, warnings, itertools; warnings.filterwarnings("ignore")
G=[g for g in itertools.product(range(3),repeat=4) if (g[0]*g[3]-g[1]*g[2])%3==1]
ID=(1,0,0,1)
def mul(g,h):
    a,b,c,d=g;e,f,x,y=h
    return ((a*e+b*x)%3,(a*f+b*y)%3,(c*e+d*x)%3,(c*f+d*y)%3)
def inv(g):
    a,b,c,d=g; return (d%3,(-b)%3,(-c)%3,a%3)
def ev(w,m):
    r=ID
    for ch in w:
        g=m[ch.lower()]; r=mul(r, g if ch.islower() else inv(g))
    return r
def gsz(gs):
    S={ID}; fr=[ID]
    while fr:
        x=fr.pop()
        for g in gs:
            y=mul(x,g)
            if y not in S: S.add(y); fr.append(y)
    return len(S)
def hs(Gp):
    gen=Gp.generators(); rel=Gp.relators(); n=len(gen)
    if n>3: return None,n
    for img in itertools.product(G,repeat=n):
        m={gen[i]:img[i] for i in range(n)}
        if all(ev(r,m)==ID for r in rel) and gsz(img)==24: return True,n
    return False,n
for label,C in [("FULL orientable cusped census", snappy.OrientableCuspedCensus()),
                ("ONE-CUSPED census", snappy.OrientableCuspedCensus(cusps=1))]:
    print("--- %s ---" % label, flush=True)
    for lo in (0,20000,80000):
        n=hit=sk=0; bg={}
        for i in range(lo,lo+800):
            try:
                M=C[i]; r,ng=hs(M.fundamental_group())
            except Exception:
                sk+=1; continue
            if r is None:
                sk+=1; bg.setdefault(ng,[0,0])[0]+=1; continue
            n+=1; hit+=r; b=bg.setdefault(ng,[0,0]); b[0]+=1; b[1]+=r
        strata=", ".join("%dgen %d/%d=%.2f%%" % (k,v[1],v[0],100*v[1]/v[0]) for k,v in sorted(bg.items()))
        print("  depth %d: %d/%d = %.2f%%  skipped %d  %s" % (lo,hit,n,100*hit/max(n,1),sk,strata), flush=True)
print("record/paper: 34.25%% -> 29.38%% -> 21.12%% ; 2gen 34.23%% -> 15.36%% ; 3gen flat near 33%%")
