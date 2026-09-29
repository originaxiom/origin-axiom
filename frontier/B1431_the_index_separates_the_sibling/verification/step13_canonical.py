"""Step 13.  The basis-choice caveat, faced head on.
The theorem of step 12 gives an ISOMORPHISM A of peripheral lattices, det 1, with
I_m003 = I_m004 o A.  Does any CANONICAL marking of the two cusps survive it?
The one canonical class a 1-cusped manifold always has is the HOMOLOGICAL LONGITUDE
(the primitive slope that dies in H_1(M;Q)) -- canonical up to sign, and I(-g)=I(g)."""
from fractions import Fraction as F
import snappy
from idx import index_class, rows
from tet_index import s_str, s_eq

for name in ["m004","m003","m015"]:
    M = snappy.Manifold(name)
    try:  hl = M.homological_longitude()
    except Exception as ex: hl = "n/a: "+str(ex)
    print(f"{name}: H1={M.homology()}  homological longitude (in snappy's (mu,lam) basis) = {hl}")
    for sl in [(1,0),(0,1),(1,1),(2,-1),(1,-2),(5,1),(1,5)]:
        N=snappy.Manifold(name); N.dehn_fill(sl)
        print(f"     filling {sl}: H1 = {N.homology()}", end="")
    print()

print("\n--- A in saturated coordinates: (c,d)_m003 -> (a,b)_m004 = (-c-d, -d)")
print("    m003 class (c,d) means (c/2)mu3 + d lam3 ;  m004 class (a,b) means a mu4 + (b/2) lam4")
A   = lambda c,d: (-c-d, -d)
Ainv= lambda a,b: (-a+b, -b)
print(f"    m004's homological longitude lam4 = (a,b)=(0,2)  <-- m003's (c,d)={Ainv(0,2)}"
      f"  = {F(Ainv(0,2)[0],2)}*mu3 + {Ainv(0,2)[1]}*lam3")
print(f"    m003's homological longitude lam3 = (c,d)=(0,1)  --> m004's (a,b)={A(0,1)}"
      f"  = {A(0,1)[0]}*mu4 + {F(A(0,1)[1],2)}*lam4")

X=70; CUT=64
print("\n--- THE CANONICALLY MARKED COMPARISON: the index on the homological longitude ---")
s4 = index_class("m004", ((F(0),F(1)),), X)        # lam4
s3 = index_class("m003", ((F(0),F(1)),), X)        # lam3
print(f"  I_m004(lambda_hom) = {s_str(s4, 40)}")
print(f"  I_m003(lambda_hom) = {s_str(s3, 40)}")
print(f"  EQUAL through q^{CUT//2}: {s_eq(s3,s4,CUT)}")
if not s_eq(s3,s4,CUT):
    d={k:s3.get(k,0)-s4.get(k,0) for k in set(s3)|set(s4)}
    first=min(k for k,v in d.items() if v)
    print(f"  first difference at x^{first} = q^{F(first,2)}:  m003 {s3.get(first,0)} vs m004 {s4.get(first,0)}")
print("\n  and the class of m003 that A sends to lambda_4, mu3-2lam3 = (x,y)=(1,-2):")
s3b = index_class("m003", ((F(1),F(-2)),), X)
print(f"  I_m003(mu-2lam)    = {s_str(s3b, 40)}")
print(f"  equals I_m004(lambda_hom) through q^{CUT//2}: {s_eq(s3b,s4,CUT)}")

print("\n--- is gamma -> -gamma a symmetry?  (needed for 'canonical up to sign' to be enough) ---")
for name,cl in [("m004",(F(1),F(1))),("m004",(F(2),F(F(1),2))),("m003",(F(1),F(-2))),("m003",(F(F(1),2),F(1)))]:
    a=index_class(name,(cl,),40); b=index_class(name,((-cl[0],-cl[1]),),40)
    print(f"   {name} {cl}: I(g)==I(-g): {s_eq(a,b,34)}")
