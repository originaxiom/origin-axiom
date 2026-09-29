"""Step 10.  VALIDATE the general boundary-class rule against the eight published m004 series,
   using ONLY snappy's edge+cusp rows (no hand-written formula)."""
from fractions import Fraction as F
from idx import index_class, rows, bdry_vector
from tet_index import s_str, s_trunc

X = 44
PUB = {   # GHRS 2016 pp.297-298, as {x-exponent : coeff};  class = x*mu + y*lam
    ("0",         F(0), F(0)):   {0:1,2:-2,4:-3,6:2,8:8,10:18,12:18,14:14,16:-12,18:-52,20:-106},
    ("mu",        F(1), F(0)):   {2:-2,4:-2,6:2,8:8,10:16,12:16,14:10,16:-14,18:-52,20:-102},
    ("2mu",       F(2), F(0)):   {2:-1,4:-1,6:3,8:6,10:12,12:9,14:3,16:-19,18:-50,20:-88},
    ("lam",       F(0), F(1)):   {6:1,8:2,10:5,12:2,14:-3,16:-16,18:-32,20:-52},
    ("4mu+lam",   F(4), F(1)):   {2:1,8:-1,10:-2,12:-5,14:-8,16:-10,18:-11,20:-6},
    ("lam/2",     F(0), F(1,2)): {3:-2,7:4,9:10,11:14,13:10,15:-2,17:-32,19:-68},
    ("mu+lam/2",  F(1), F(1,2)): {2:-1,4:-1,6:2,8:7,10:11,12:11,14:3,16:-17,18:-49,20:-88},
    ("2mu+lam/2", F(2), F(1,2)): {1:-1,5:1,7:4,9:7,11:7,13:3,15:-12,17:-31,19:-62},
}
print("="*78); print("STEP 10: the general rule  v(gamma) = -(cusp row)  vs the 8 published m004 series")
print("="*78)
allok=True
for (lab,x,y),pub in PUB.items():
    ser = index_class("m004", ((x,y),), X)
    hi = max(pub)
    mine = {k:v for k,v in s_trunc(ser,hi).items() if v}
    ok = mine == {k:v for k,v in pub.items() if v}
    allok &= ok
    print(f"\n I({lab:<10}) x={x} y={y}   {'MATCH' if ok else '*** MISMATCH ***'}")
    print(f"   {s_str(ser, hi)}")
    if not ok:
        print(f"   pub: {pub}")
        print(f"   diff:{ {k: mine.get(k,0)-pub.get(k,0) for k in set(mine)|set(pub) if mine.get(k,0)!=pub.get(k,0)} }")
print("\nALL EIGHT REPRODUCED FROM SNAPPY ROWS ALONE:", allok)

print("\n--- the edge-row lemma, checked numerically:  v -> v + E_i  multiplies I by q^{-1} ---")
import snappy, itertools
from idx import index_class, triples, J_mindeg, J_normalised
from tet_index import s_mul, s_add, s_shift, s_eq
M,n,r,E,Mr,Ln = rows("m004")
def raw_index(v, Xmax=30, zero_edges=(0,)):
    free=[i for i in range(n) if i not in zero_edges]
    tot={}
    for kk in itertools.product(range(-200,201),repeat=len(free)):
        k=[0]*n
        for idx,i in enumerate(free): k[i]=kk[idx]
        D=2*sum(k)+sum(J_mindeg(*t) for t in triples(E,n,k,v))
        if D>Xmax: continue
        b=Xmax-D; prod={0:1}
        for t in triples(E,n,k,v): prod=s_mul(prod,J_normalised(*t,budget=b),b)
        tot=s_add(tot,s_shift(prod,D,Xmax))
    return tot
v0=bdry_vector(n,Mr,Ln,((F(1),F(0)),))
for i in range(n):
    vi=[v0[s]+E[i][s] for s in range(3*n)]
    a=raw_index(v0); b=raw_index(vi)
    print(f"   v+E_{i}:  I(v+E_i) == q^-1 I(v) through q^12 :",
          s_eq(b, s_shift(a,-2,30), 24))
