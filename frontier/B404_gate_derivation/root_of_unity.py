"""B404 -- L1/L2/L3: are class-1 cells roots of unity, with character-gated orders?"""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

W1 = build_theta_W(1); W2 = build_theta_W(2)
o1, p1 = matrix_order(W1); o2, p2 = matrix_order(W2)
def A(m): return [[(1+m*m)%15, m%15],[m%15,1]]
def mm(a,b): return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%15,(a[0][0]*b[0][1]+a[0][1]*b[1][1])%15],
                     [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%15,(a[1][0]*b[0][1]+a[1][1]*b[1][1])%15]]
G1=[[[1,0],[0,1]]]
for _ in range(o1-1): G1.append(mm(G1[-1],A(1)))
G2=[[[1,0],[0,1]]]
for _ in range(o2-1): G2.append(mm(G2[-1],A(2)))
def chi(x, q):
    x %= q
    if x == 0: return 0
    return 1 if pow(x, (q-1)//2, q) == 1 else -1

ZK = {k: E.zeta(k) for k in range(60)}
def as_root(C):
    for k in range(60):
        if C == ZK[k]: return k
        # also allow minus signs beyond zeta60? -zeta60^k = zeta60^{k+30} in zeta60 ✓ covered
    return None

viol1 = viol2 = 0; l3 = {"+1": set(), "-1": set()}
tot = 0
for j in range(o1):
    for l in range(o2):
        g = mm(G1[j],G2[l])
        d = ((-g[0][0]-1)*(-g[1][1]-1)-g[0][1]*g[1][0])%15
        if gcd(d,15)!=1: continue
        tot += 1
        C = par_trace(p1[j], p2[l])
        k = as_root(C)
        if k is None: viol1 += 1; continue
        order = 60 // gcd(k, 60)
        c3 = chi(d, 3)
        has3 = (order % 3 == 0)
        if (c3 == 1 and has3) or (c3 == -1 and not has3): viol2 += 1
        c5 = chi(d, 5)
        l3["+1" if c5 == 1 else "-1"].add(order % 5 == 0)
print(f"L1: class-1 cells that are roots of unity: {tot - viol1}/{tot}  (violations: {viol1})")
print(f"L2: Eisenstein order-gate violations: {viol2}/{tot}")
print(f"L3: chi5=+1 cells' 5-part-of-order values: {l3['+1']}; chi5=-1: {l3['-1']}")
json.dump(dict(tot=tot, not_root=viol1, gate_viol=viol2,
               l3_plus=sorted(map(str, l3["+1"])), l3_minus=sorted(map(str, l3["-1"]))),
          open(os.path.join(HERE, "root_of_unity.json"), "w"), indent=1)
print("DONE")
