"""TIER 1. Consistency cannot fix the chirality sign: every anomaly is parity-odd, so 0 -> 0."""
from fractions import Fraction as F
gen=[(3,2,F(1,6)),(-3,1,F(-2,3)),(-3,1,F(1,3)),(1,2,F(-1,2)),(1,1,F(1)),(1,1,F(0))]
def an(G):
    return {"U1^3":sum(abs(c)*d*Y**3 for c,d,Y in G),"grav^2U1":sum(abs(c)*d*Y for c,d,Y in G),
            "SU3^2U1":sum(d*Y for c,d,Y in G if abs(c)==3),"SU2^2U1":sum(abs(c)*Y for c,d,Y in G if d==2),
            "SU3^3":sum(d*(1 if c==3 else -1) for c,d,Y in G if abs(c)==3),
            "Witten_doublets":sum(abs(c) for c,d,Y in G if d==2)}
mir=[(-c if abs(c)==3 else c,d,-Y) for c,d,Y in gen]
a,b=an(gen),an(mir)
for k in a: print(f"  {k:16s} ours {str(a[k]):>4s}   mirror {str(b[k]):>4s}")
assert all(a[k]==0==b[k] for k in a if k!="Witten_doublets")
print("both hands anomaly-free -> sign SURVIVES consistency")
