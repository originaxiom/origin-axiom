"""Step 11.  Controls on NON-TRIVIAL boundary classes:
   (a) which edge weight is gauged to zero,
   (b) cyclic slot order (a rotation is a symmetry of J; the odd permutation = the MIRROR),
   (c) random retriangulation with the SAME peripheral curves,
   (d) the saturated lattice of admissible (x,y) for each manifold."""
from fractions import Fraction as F
import snappy, random
from idx import index_class, rows, bdry_vector
from tet_index import s_str, s_eq, s_trunc

X, CUT = 40, 32

def saturation(name):
    M,n,r,E,Mr,Ln = rows(name)
    assert r==1
    good=[]
    for a in range(0,3):
        for b in range(0,3):
            x,y=F(a,2),F(b,2)
            if (a,b)==(0,0): continue
            try:
                bdry_vector(n,Mr,Ln,((x,y),)); good.append((x,y))
            except AssertionError: pass
    return good

print("="*78); print("STEP 11 (d): the SATURATED lattice of admissible classes")
print("="*78)
for name in ["m004","m003","m015"]:
    M,n,r,E,Mr,Ln = rows(name)
    print(f"  {name}: Mr={Mr[0]}  Ln={Ln[0]}")
    print(f"      half-classes (x,y) in (1/2)Z^2 with |.|<=1 that are ADMISSIBLE: {saturation(name)}")

print()
print("="*78); print("STEP 11 (a)(b): gauge + orientation independence on non-trivial classes")
print("="*78)
CLASSES = [(F(1),F(0)),(F(0),F(1)),(F(1),F(1)),(F(2),F(1)),(F(-1),F(2)),(F(3),F(-2))]
for name in ["m004","m003"]:
    M,n,r,E,Mr,Ln = rows(name)
    print(f"\n  {name} ({n} tets):")
    for (x,y) in CLASSES:
        sers = [index_class(name, ((x,y),), X, zero_edges=[z]) for z in range(n)]
        same = all(s_eq(sers[0],t,CUT) for t in sers)
        mir  = index_class(name, ((x,y),), X, order=(0,2,1))
        print(f"    ({x},{y}): gauge-independent over {n} choices: {same};  "
              f"odd-permutation(=mirror) equals it: {s_eq(sers[0],mir,CUT)}")
        if not same:
            for z,t in enumerate(sers): print(f"        z={z}: {s_str(t,CUT)}")

print()
print("="*78); print("STEP 11 (c): random retriangulation, SAME peripheral curves")
print("="*78)
random.seed(11)
for name in ["m004","m003"]:
    base = {}
    for (x,y) in CLASSES[:4]:
        base[(x,y)] = index_class(name, ((x,y),), X)
    nok=nfail=0; fails=[]
    for trial in range(8):
        M = snappy.Manifold(name); M.randomize()
        if M.num_cusps()!=1: continue
        try:
            for (x,y),b in base.items():
                s = index_class(name, ((x,y),), X, mfd=M)
                if s_eq(s,b,CUT): nok+=1
                else: nfail+=1; fails.append((trial,M.num_tetrahedra(),(x,y)))
        except AssertionError as ex:
            fails.append((trial,M.num_tetrahedra(),"ASSERT "+str(ex)[:60]))
    print(f"  {name}: {nok} agreements, {nfail} disagreements; anomalies: {fails}")
