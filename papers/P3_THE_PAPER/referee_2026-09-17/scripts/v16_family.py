"""Referee check: the 112-member Q(sqrt-3)-shape family, its chirality and 2T split."""
import snappy, warnings, math, time; warnings.filterwarnings("ignore")
from fractions import Fraction
warnings.filterwarnings("ignore")
S3=math.sqrt(3)
def in_Qsqrt3(z, tol=1e-9, maxden=400):
    x,y=z.real,z.imag
    fx=Fraction(x).limit_denominator(maxden); fy=Fraction(y/S3).limit_denominator(maxden)
    return abs(float(fx)-x)<tol and abs(float(fy)-y/S3)<tol
cen=snappy.OrientableCuspedCensus()
t0=time.time(); fam=[]
for i,M in enumerate(cen):
    try:
        sh=M.tetrahedra_shapes('rect')
    except Exception: continue
    if all(in_Qsqrt3(complex(z)) for z in sh): fam.append((M.name(),M.num_cusps(),M.num_tetrahedra()))
    if (i+1)%50000==0: print(f"  {i+1} ({time.time()-t0:.0f}s) family so far {len(fam)}",flush=True)
print("FAMILY SIZE (all tetrahedron shapes in Q(sqrt-3)):",len(fam)," (paper: 112)")
from collections import Counter
print("  by cusps:",dict(Counter(c for _,c,_ in fam)))
print("  m004 in family:", any(n=='m004' for n,_,_ in fam), "; m003:", any(n=='m003' for n,_,_ in fam))
print("  first 20:",[n for n,_,_ in fam[:20]])
# chirality split
amph=0; chir=0; bad=[]
for n,c,t in fam:
    M=snappy.Manifold(n)
    try:
        a=M.symmetry_group().is_amphicheiral()
    except Exception:
        try:
            M.canonize(); a=M.symmetry_group().is_amphicheiral()
        except Exception as e: bad.append(n); continue
    if a: amph+=1
    else: chir+=1
print("  amphichiral:",amph," chiral:",chir," undetermined:",bad)
print("  paper: 38 amphichiral, 74 chiral")
# 2T door split
import itertools
G=[(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1]
idx={g:i for i,g in enumerate(G)}
def mul(x,y):
    a,b,c,d=x;e,f,g,h=y
    return ((a*e+b*g)%3,(a*f+b*h)%3,(c*e+d*g)%3,(c*f+d*h)%3)
MUL=[[idx[mul(G[i],G[j])] for j in range(24)] for i in range(24)]
INV=[idx[next(g for g in G if mul(G[i],g)==(1,0,0,1))] for i in range(24)]
E=idx[(1,0,0,1)]
adm=0; notadm=0; skip=0
for n,c,t in fam:
    M=snappy.Manifold(n); fg=M.fundamental_group(); ng=fg.num_generators()
    if ng>3: skip+=1; continue
    rels=[[(ord(ch)-97,1) if ch.islower() else (ord(ch)-65,-1) for ch in r] for r in fg.relators()]
    found=False
    for imgs in itertools.product(range(24),repeat=ng):
        ok=True
        for w in rels:
            r=E
            for gi,e in w:
                x=imgs[gi]
                if e<0: x=INV[x]
                r=MUL[r][x]
            if r!=E: ok=False;break
        if not ok: continue
        seen={E}; st=[E]
        while st:
            x=st.pop()
            for s in imgs:
                y=MUL[x][s]
                if y not in seen: seen.add(y); st.append(y)
        if len(seen)==24: found=True;break
    if found: adm+=1
    else: notadm+=1
print("  admit 2T surjection:",adm," do not:",notadm," >3 generators (not enumerated):",skip)
print("  paper: 59 admit, 35 do not, 18 with more than three generators not reached")
