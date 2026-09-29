"""Step 17.  (a) minD grows: the enumeration {minD <= L} really is complete.
             (b) brute force, not relying on minD at all.
             (c) the exact topological identity on the shared index-2 sublattices."""
from fractions import Fraction as F
from idx import index_class, rows, bdry_vector, triples, J_mindeg
from tet_index import s_str, s_trunc, s_eq

def minD(name,x,y):
    M,n,r,E,Mr,Ln=rows(name)
    v=bdry_vector(n,Mr,Ln,((F(x),F(y)),)); R=60+8*max(abs(x),abs(y))
    vals=[]
    for k1 in range(-R,R+1):
        k=[0]*n;k[1]=k1
        vals.append((2*sum(k)+sum(J_mindeg(*t) for t in triples(E,n,k,v)),k1))
    b,a=min(vals); assert abs(a)<R-5; return b

print("(a) min of minD over the rim |(x,y)| = R  (must exceed 8 for R beyond the enumeration box)")
for nm in ["m004","m003"]:
    row=[]
    for R in [4,8,12,16,20,30,40,60,80]:
        rim=[minD(nm,x,y) for x in range(-R,R+1) for y in (-R,R)]+ \
            [minD(nm,x,y) for x in (-R,R) for y in range(-R+1,R)]
        row.append((R,min(rim)))
    print(f"   {nm}: {row}")

print("\n(b) BRUTE FORCE: is m004's meridian series attained anywhere on m003 with |x|,|y| <= 14, and vice versa?")
X,CUT=60,50
tgt4 = s_trunc(index_class("m004",((F(1),F(0)),),X),CUT)          # the published I(mu) of m004
tgt3 = s_trunc(index_class("m003",((F(0),F(1)),),X),CUT)          # I(lambda) of m003
print(f"   m004 meridian  I(mu)   = {s_str(tgt4,24)}")
print(f"   m003 longitude I(lam)  = {s_str(tgt3,24)}")
for nm,tgt,other in [("m003",tgt4,"m004's meridian"),("m004",tgt3,"m003's longitude")]:
    hit=[]
    for x in range(-14,15):
        for y in range(-14,15):
            if s_trunc(index_class(nm,((F(x),F(y)),),X),CUT)==tgt: hit.append((x,y))
    print(f"   {other} series found on {nm} at: {hit if hit else 'NOWHERE (841 integer classes scanned)'}")

print("\n(c) the exact identity on the shared sublattices:  y even  =>  I_m003(x,y) = I_m004(-(2x+y), -y/2)")
ok=bad=0
for x in range(-6,7):
    for y in range(-6,7,2):
        a,b = -(2*x+y), F(-y,2)
        s3=index_class("m003",((F(x),F(y)),),X); s4=index_class("m004",((F(a),b),),X)
        if s_eq(s3,s4,CUT): ok+=1
        else: bad+=1; print(f"     FAIL at m003{(x,y)} -> m004{(a,b)}")
print(f"   {ok} identities hold, {bad} fail   (image = {{a even}} c H_1(bdry m004))")
print("\n   and on the complementary cosets (y odd) the image is a HALF class of m004:")
for (x,y) in [(0,1),(1,1),(0,-1)]:
    a,b=-(2*x+y),F(-y,2)
    print(f"     m003{(x,y)} = m004({a}mu {b}lam):  {s_str(index_class('m003',((F(x),F(y)),),40),18)}")
