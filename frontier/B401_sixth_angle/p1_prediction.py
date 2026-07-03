"""B401 P1's falsifiable consequence: the 3-block constant's det-class split must be
sigma_cl-conjugate to the slot's: class-1 -> (0,0,-1/16,+1/16), class-5 -> (0,0,-1/48,+1/48)."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

W1 = build_theta_W(1); W2 = build_theta_W(2)
o1, p1 = matrix_order(W1); o2, p2 = matrix_order(W2)
C = {(j,l): par_trace(p1[j], p2[l]) for j in range(o1) for l in range(o2)}
def A(m): return [[(1+m*m)%15, m%15],[m%15, 1]]
def mm(a,b): return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%15,(a[0][0]*b[0][1]+a[0][1]*b[1][1])%15],
                     [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%15,(a[1][0]*b[0][1]+a[1][1]*b[1][1])%15]]
G1=[[[1,0],[0,1]]]
for _ in range(o1-1): G1.append(mm(G1[-1],A(1)))
G2=[[[1,0],[0,1]]]
for _ in range(o2-1): G2.append(mm(G2[-1],A(2)))
def cls(j,l):
    g = mm(G1[j],G2[l])
    d = ((-g[0][0]-1)*(-g[1][1]-1)-g[0][1]*g[1][0])%15
    return gcd(d,15)
def hp(t): return SC.solve_H(SC.H_avg(t))

BLK = [(4,8,1),(4,4,-1),(0,8,-1),(0,4,1)]     # the banked 3-block grading (P66-era)
out = {}
for K in (1,3,5,15):
    t = E.ZERO
    for (a,b,s) in BLK:
        for j in range(o1):
            za = E.zeta((-3*j*a)%60)
            for l in range(o2):
                if cls(j,l)!=K: continue
                t = E.add(t, E.scal(Fr(s,240), E.mul(E.mul(za, E.zeta((-5*l*b)%60)), C[(j,l)])))
    out[str(K)] = [str(x) for x in hp(t)]
    print(f"3-block class-{K} partial:", out[str(K)])
pred = {"1": ["0","0","-1/16","1/16"], "5": ["0","0","-1/48","1/48"], "3": ["0","0","0","0"], "15": ["0","0","0","0"]}
match = all(out[k]==v for k,v in pred.items())
print("CLASS-GROUP PREDICTION:", "CONFIRMED" if match else "REFUTED")
json.dump(dict(partials=out, predicted=pred, match=match),
          open(os.path.join(HERE,"p1_prediction.json"),"w"), indent=1)
