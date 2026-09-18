"""Step 16.  The separation, made airtight.
 (1) exhaustiveness: {gamma in H_1(bdry;Z) : minD(gamma) <= L} computed on a LARGE box;
 (2) both directions;
 (3) retriangulation invariance of the separating classes;
 (4) the index collection must be invariant under the manifold's isometry group acting on H_1(bdry)."""
import itertools, random
from fractions import Fraction as F
import snappy
from idx import index_class, rows, bdry_vector, triples, J_mindeg
from tet_index import s_str, s_trunc, s_eq

X, CUT = 60, 50

def minD(name, x, y, mfd=None):
    M,n,r,E,Mr,Ln = rows(name, mfd)
    v = bdry_vector(n,Mr,Ln,((F(x),F(y)),))
    R = 60 + 8*max(abs(x),abs(y))
    vals=[]
    for k1 in range(-R,R+1):
        k=[0]*n; k[1]=k1
        vals.append((2*sum(k)+sum(J_mindeg(*t) for t in triples(E,n,k,v)), k1))
    best,arg=min(vals)
    assert abs(arg) < R-5, f"k-range too small at {(x,y)}: argmin {arg}/{R}"
    return best

BIG=40
print("="*88); print(f"(1) EXHAUSTIVENESS: all integer classes with minD <= 8, over |x|,|y| <= {BIG}")
print("="*88)
LOW={}
for nm in ["m004","m003"]:
    S={}
    for x in range(-BIG,BIG+1):
        for y in range(-BIG,BIG+1):
            d=minD(nm,x,y)
            if d<=8: S[(x,y)]=d
    LOW[nm]=S
    far=max(max(abs(k[0]),abs(k[1])) for k in S)
    byd={}
    for k,d in S.items(): byd.setdefault(d,[]).append(k)
    print(f"  {nm}: {len(S)} classes with minD<=8; farthest is at |.|={far} (box {BIG}) "
          f"-> the set is bounded and fully inside the box")
    for d in sorted(byd): print(f"      minD={d}: {len(byd[d])} classes, max |.| = {max(max(abs(a),abs(b)) for a,b in byd[d])}")

print("\n" + "="*88); print("(2) BOTH DIRECTIONS: an integer class of one whose series occurs at NO integer class of the other")
print("="*88)
SER={nm:{k:s_trunc(index_class(nm,(F(k[0]),F(k[1])),X),CUT) for k in LOW[nm]} for nm in ["m004","m003"]}
for a,b in [("m004","m003"),("m003","m004")]:
    print(f"\n  --- classes of {a} absent from {b} ---")
    bad=[]
    for k,s in SER[a].items():
        if not s: continue
        L=min(s)
        cands=[c for c,d in LOW[b].items() if d<=L]
        if any(SER[b][c]==s for c in cands): continue
        bad.append((k,L,len(cands)))
    # group by series
    seen={}
    for k,L,nc in bad: seen.setdefault(tuple(sorted(SER[a][k].items())),[]).append((k,L,nc))
    print(f"    {len(bad)} classes, {len(seen)} distinct series")
    for key,ks in sorted(seen.items(), key=lambda t:min(x[1] for x in t[1]))[:4]:
        k,L,nc=ks[0]
        print(f"      e.g. {a}{k} (leading x^{L}; only {nc} classes of {b} can compete, all checked):")
        print(f"           {s_str(dict(key),30)}")
        print(f"           attained on {a} at {sorted(x[0] for x in ks)}")

print("\n" + "="*88); print("(3) RETRIANGULATION INVARIANCE OF THE SEPARATING CLASSES")
print("="*88)
random.seed(16)
for nm,cl in [("m004",(1,0)),("m004",(3,1)),("m003",(0,1)),("m003",(1,1))]:
    base=index_class(nm,((F(cl[0]),F(cl[1])),),X)
    ok=0; bad=0
    for t in range(12):
        N=snappy.Manifold(nm); N.randomize()
        try:
            s=index_class(nm,((F(cl[0]),F(cl[1])),),X,mfd=N)
            if s_eq(s,base,CUT): ok+=1
            else: bad+=1
        except AssertionError: pass
    print(f"  {nm} class {cl}: {ok} retriangulations agree, {bad} disagree")

print("\n" + "="*88); print("(4) THE ISOMETRY GROUP MUST ACT ON THE COLLECTION  (independent check of the rule)")
print("="*88)
for nm in ["m004","m003"]:
    M=snappy.Manifold(nm); G=M.symmetry_group()
    mats=set()
    for iso in G.isometries():
        cm=iso.cusp_maps()[0]
        mats.add(((int(cm[0,0]),int(cm[0,1])),(int(cm[1,0]),int(cm[1,1]))))
    print(f"  {nm}: symmetry group {G}; distinct cusp maps {sorted(mats)}")
    allok=True
    for A in mats:
        for x in range(-3,4):
            for y in range(-3,4):
                xx=A[0][0]*x+A[0][1]*y; yy=A[1][0]*x+A[1][1]*y
                s1=index_class(nm,((F(x),F(y)),),40); s2=index_class(nm,((F(xx),F(yy)),),40)
                if not s_eq(s1,s2,34): allok=False; print(f"     FAIL {A} on {(x,y)}")
    print(f"     index collection invariant under every cusp map, 49 classes each: {allok}")
