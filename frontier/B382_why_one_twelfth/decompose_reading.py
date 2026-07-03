"""B382 leg 3b -- (i) the det-class decomposition of the slot constant (THE READING),
(ii) the 3-block grading search on the banked table (which +-combination gives the
banked (0,0,-1/12,+1/12)), (iii) window-support bookkeeping."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

N = 15
W1 = build_theta_W(1); W2 = build_theta_W(2)
o1,pow1 = matrix_order(W1); o2,pow2 = matrix_order(W2)
ID = [[E.ONE if i==j else E.ZERO for j in range(N)] for i in range(N)]
g1 = [[2,1],[1,1]]; g2 = [[5,2],[2,1]]
def m2(A,B): return [[(A[i][0]*B[0][j]+A[i][1]*B[1][j])%15 for j in range(2)] for i in range(2)]
G1=[[[1,0],[0,1]]]
for _ in range(19): G1.append(m2(G1[-1],g1))
G2=[[[1,0],[0,1]]]
for _ in range(11): G2.append(m2(G2[-1],g2))

table = {}; cls_of = {}
for j in range(o1):
    for l in range(o2):
        table[(j,l)] = par_trace(pow1[j], pow2[l])
        gp = m2(G1[j],G2[l])
        det = ((-gp[0][0]-1)*(-gp[1][1]-1) - gp[0][1]*gp[1][0]) % 15
        cls_of[(j,l)] = gcd(det,15)

def hproj(t): return SC.solve_H(SC.H_avg(t))
def combo(cells, classes=None):
    """sum over graded cells of the DFT restricted to det-classes."""
    t = E.ZERO
    for (a,b,sgn) in cells:
        for j in range(o1):
            za = E.zeta((-3*j*a)%60)
            for l in range(o2):
                if classes and cls_of[(j,l)] not in classes: continue
                t = E.add(t, E.scal(Fr(sgn,o1*o2), E.mul(E.mul(za, E.zeta((-5*l*b)%60)), table[(j,l)])))
    return t

SLOT = [(6,2,1),(6,10,-1),(14,2,-1),(14,10,1)]
print("slot total:", hproj(combo(SLOT)))
for c in (1,3,5,15):
    print(f"  det-class {c:2d} partial:", hproj(combo(SLOT, {c})))

# window support: w1(j)=0 iff j=0 mod 5; w2(l)=0 iff l=0 mod 3 -> counts
dom = [(j,l) for j in range(20) for l in range(12) if j%5 and l%3]
print("window-support cells:", len(dom), "of 240; classes there:",
      {c: sum(1 for x in dom if cls_of[x]==c) for c in (1,3,5,15)})

# 3-block grading search on the SAME table (rows {0,4,16}, cols {0,4,8})
import itertools
target = (Fr(0),Fr(0),Fr(-1,12),Fr(1,12))
rows=[0,4,16]; colsb=[0,4,8]
found=[]
for rs in itertools.product([-1,0,1],repeat=3):
    if sorted(rs)!=[-1,0,1] and sorted(rs)!=[-1,1,0] and set(rs)!={-1,1,0}: 
        if not (rs.count(1)==1 and rs.count(-1)==1): continue
    for cs in itertools.product([-1,0,1],repeat=3):
        if not (cs.count(1)==1 and cs.count(-1)==1): continue
        cells=[(rows[i],colsb[k],rs[i]*cs[k]) for i in range(3) for k in range(3) if rs[i]*cs[k]]
        if hproj(combo(cells))==target: found.append((rs,cs))
print("3-block gradings hitting the banked (0,0,-1/12,+1/12):", found)
partials = {str(c): [str(x) for x in hproj(combo(SLOT, {c}))] for c in (1,3,5,15)}
json.dump(dict(found_3blk=[[list(a),list(b)] for a,b in found],
               slot_partials=partials,
               support=dict(cells=len(dom), classes={str(c): sum(1 for x in dom if cls_of[x]==c) for c in (1,3,5,15)})),
          open(os.path.join(HERE,"reading.json"),"w"), indent=1)
print("DONE")
