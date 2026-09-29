"""Step 15.  THE HONEST QUESTION: classes in H_1(boundary torus; Z), not the saturated lattice.
The step-12 isomorphism A maps Lambda(m003) -> Lambda(m004) with det 1, BUT
   m003's H_1  = {(a,b) in Lambda(m004) : a = b mod 2}   while   m004's H_1 = {b even}.
Those are DIFFERENT index-2 sublattices, so the two honest collections need not coincide."""
import itertools
from fractions import Fraction as F
from idx import index_class, rows, bdry_vector, triples, J_mindeg
from tet_index import s_str, s_trunc, s_eq

X, CUT, B = 56, 48, 8

def minD(name, x, y, box=400):
    M,n,r,E,Mr,Ln = rows(name)
    v = bdry_vector(n,Mr,Ln,((x,y),))
    best=None
    for k1 in range(-box,box+1):
        k=[0]*n; k[1]=k1
        D=2*sum(k)+sum(J_mindeg(*t) for t in triples(E,n,k,v))
        if best is None or D<best: best=D
    return best

print("="*84)
print("STEP 15: integer boundary classes only.  minD = exact lower bound on the leading x-degree")
print("="*84)
COL={}
for nm in ["m004","m003"]:
    d={}
    for x in range(-B,B+1):
        for y in range(-B,B+1):
            d[(x,y)] = (minD(nm,F(x),F(y)), None)
    COL[nm]=d
    lo = sorted(set(v[0] for v in d.values()))[:8]
    small = {k:v[0] for k,v in d.items() if v[0]<=6}
    print(f"\n{nm}: minD values over |x|,|y|<={B}: smallest are {lo}")
    print(f"   classes with minD <= 6: {sorted(small.items(), key=lambda t:t[1])}")
    rim=[v[0] for k,v in d.items() if max(abs(k[0]),abs(k[1]))==B]
    print(f"   minD on the rim |.|={B}: min {min(rim)}  (grows quadratically: delta_x is a positive quadratic form)")

print("\n--- the series of every integer class with minD <= 8, both manifolds ---")
SER={}
for nm in ["m004","m003"]:
    SER[nm]={}
    for k,(mD,_) in COL[nm].items():
        if mD<=8:
            SER[nm][k]=s_trunc(index_class(nm,(F(k[0]),F(k[1])),X),CUT)
    print(f"\n  {nm}: {len(SER[nm])} classes with minD<=8")
    seen={}
    for k in sorted(SER[nm], key=lambda t:(COL[nm][t][0],t)):
        s=SER[nm][k]
        key=tuple(sorted(s.items()))
        seen.setdefault(key,[]).append(k)
    for key,ks in sorted(seen.items(), key=lambda t:(min(x[0] for x in t[0]) if t[0] else 999)):
        print(f"    {str(ks):<58} {s_str(dict(key),22)}")

print("\n" + "="*84)
print("DOES ANY INTEGER CLASS OF ONE FAIL TO OCCUR ON THE OTHER?")
print("="*84)
def leading(s): return min(s) if s else None
# exhaustive: a series with leading x-degree L can only be matched by a class with minD <= L
for a,b in [("m003","m004"),("m004","m003")]:
    print(f"\n  classes of {a} whose series occurs at NO integer class of {b}:")
    hits=0
    for k,s in sorted(SER[a].items(), key=lambda t:COL[a][t[0]][0]):
        L=leading(s)
        if L is None: continue
        cands=[kk for kk,(mD,_) in COL[b].items() if mD<=L]
        assert all(max(abs(c[0]),abs(c[1]))<B for c in cands), "candidate set touches the box rim"
        found=None
        for c in cands:
            sc = SER[b].get(c)
            if sc is None: sc = s_trunc(index_class(b,(F(c[0]),F(c[1])),X),CUT)
            if sc==s: found=c; break
        if found is None:
            hits+=1
            if hits<=4:
                print(f"    {a} at {k} (minD={COL[a][k][0]}, leading x^{L}):  {s_str(s,24)}")
                print(f"       -> {len(cands)} integer classes of {b} have minD <= {L}: {sorted(cands)}")
                for c in sorted(cands):
                    sc=SER[b].get(c) or s_trunc(index_class(b,(F(c[0]),F(c[1])),X),CUT)
                    print(f"          {b}{c}: {s_str(sc,16)}")
    print(f"    TOTAL such classes of {a} (among minD<=8): {hits}")
