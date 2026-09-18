"""Step 14.  CONTROLS IN BOTH DIRECTIONS for the class-indexed comparison.
   The comparison used for m003/m004 is: does some A in GL_2(Z) of the saturated peripheral
   lattices carry one index collection onto the other?  That test must be able to FAIL,
   and must succeed where it should."""
import itertools, time, random
from fractions import Fraction as F
import snappy
from idx import index_class, rows
from lat import sat_basis
from tet_index import s_str, s_eq, s_trunc

X, CUT, BOX = 48, 40, 4

def collection(name, box=BOX, mfd=None, X=X):
    g1,g2,cov = sat_basis(name, mfd)
    out={}
    for i in range(-box,box+1):
        for j in range(-box,box+1):
            cls=(i*g1[0]+j*g2[0], i*g1[1]+j*g2[1])
            out[(i,j)] = s_trunc(index_class(name,(cls,),X,mfd=mfd), CUT)
    return out,(g1,g2,cov)

def matches(C1,C2,rng=1,ent=2):
    found=[]
    for a,b,c,d in itertools.product(range(-ent,ent+1),repeat=4):
        if a*d-b*c not in (1,-1): continue
        ok=True; used=0
        for i in range(-rng,rng+1):
            for j in range(-rng,rng+1):
                img=(a*i+b*j, c*i+d*j)
                if img not in C2: ok=False; break
                if C1[(i,j)]!=C2[img]: ok=False; break
                if C1[(i,j)]: used+=1
            if not ok: break
        if ok: found.append(((a,b,c,d),used))
    return found

print("="*80); print("STEP 14: can the class-indexed comparison FAIL?  and does it succeed where it must?")
print(f"   series to q^{CUT//2}, classes |i|,|j| <= {BOX} in the SATURATED basis, A entries <= 2")
print("="*80)
C={}
for nm in ["m004","m003","m015","m006","m007","m016","m017"]:
    t=time.time(); C[nm],info=collection(nm); print(f"  {nm}: {len(C[nm])} classes computed in {time.time()-t:.1f}s   basis {info[0]},{info[1]} covol {info[2]}")

print("\n  --- (0,0) alone ---")
for nm in C: print(f"    {nm}: {s_str(C[nm][(0,0)],20)}")

PAIRS=[("m004","m003","MUST MATCH (step 12 theorem)"),
       ("m004","m015","MUST FAIL (different volume)"),
       ("m004","m006","MUST FAIL (different volume)"),
       ("m006","m007","same I(0,0) -- do classes separate?"),
       ("m015","m016","same I(0,0) -- do classes separate?"),
       ("m015","m017","same I(0,0) -- do classes separate?"),
       ("m016","m017","same I(0,0) -- do classes separate?")]
print("\n  --- pairwise GL_2(Z) matching ---")
for a,b,note in PAIRS:
    same00 = C[a][(0,0)]==C[b][(0,0)]
    m=matches(C[a],C[b])
    print(f"    {a} vs {b:5s}: I(0,0) equal: {str(same00):5s}   matching A's found: {len(m)}"
          f"  {[x[0] for x in m][:4]}   [{note}]")
    if not m and same00:
        # exhibit a separating class
        for i in range(-2,3):
            for j in range(-2,3):
                pass
print("\n  --- a separating class, exhibited, for each pair with equal I(0,0) but no matching A ---")
for a,b,note in PAIRS:
    if C[a][(0,0)]!=C[b][(0,0)] or matches(C[a],C[b]): continue
    # find the class where EVERY A fails; report the multiset difference
    s1={k:tuple(sorted(v.items())) for k,v in C[a].items()}
    s2={k:tuple(sorted(v.items())) for k,v in C[b].items()}
    only1=set(s1.values())-set(s2.values())
    print(f"    {a} vs {b}: {len(set(s1.values()))} vs {len(set(s2.values()))} distinct series; "
          f"{len(only1)} occur for {a} and for no class of {b} in the box")
    for s in sorted(only1,key=lambda t:(t[0][0] if t else 99))[:2]:
        k=[kk for kk,v in s1.items() if v==s][0]
        print(f"       {a} at class {k}: {s_str(dict(s),20)}")

print("\n  --- retriangulation: identical manifold must match with A = identity ---")
random.seed(3)
for nm in ["m004","m003"]:
    N=snappy.Manifold(nm); N.randomize()
    Cr,info=collection(nm, box=2, mfd=N)
    ident=all(Cr[(i,j)]==C[nm][(i,j)] for i in range(-2,3) for j in range(-2,3))
    print(f"    {nm} vs randomized ({N.num_tetrahedra()} tets): saturated basis {info[0]},{info[1]} "
          f"covol {info[2]};  all 25 classes identical: {ident}")
