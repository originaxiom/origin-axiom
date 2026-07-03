"""B401 P3 -- refine the slot's det-class partials by the GENUS CHARACTERS:
split class-1 cells by chi5(det(gamma'-I) mod 5) and chi_-3(det mod 3); the registered
question: does a character sector vanish (a genus selection rule) or do the characters
refine 1/16 into meaningful sub-constants?"""
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
def A(m): return [[(1+m*m)%15, m%15],[m%15,1]]
def mm(a,b): return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%15,(a[0][0]*b[0][1]+a[0][1]*b[1][1])%15],
                     [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%15,(a[1][0]*b[0][1]+a[1][1]*b[1][1])%15]]
G1=[[[1,0],[0,1]]]
for _ in range(o1-1): G1.append(mm(G1[-1],A(1)))
G2=[[[1,0],[0,1]]]
for _ in range(o2-1): G2.append(mm(G2[-1],A(2)))
def det_gm(j,l):
    g = mm(G1[j],G2[l])
    return ((-g[0][0]-1)*(-g[1][1]-1)-g[0][1]*g[1][0])%15
def chi5(x):
    x %= 5
    if x == 0: return 0
    return 1 if x in (1,4) else -1
def chi3(x):
    x %= 3
    if x == 0: return 0
    return 1 if x == 1 else -1
def hp(t): return SC.solve_H(SC.H_avg(t))

SLOT = [(6,2,1),(6,10,-1),(14,2,-1),(14,10,1)]
out = {}
for (c5, c3) in ((1,1),(1,-1),(-1,1),(-1,-1)):
    t = E.ZERO
    cnt = 0
    for (a,b,s) in SLOT:
        for j in range(o1):
            za = E.zeta((-3*j*a)%60)
            for l in range(o2):
                d = det_gm(j,l)
                if gcd(d,15)!=1: continue
                if chi5(d)!=c5 or chi3(d)!=c3: continue
                cnt += 1
                t = E.add(t, E.scal(Fr(s,240), E.mul(E.mul(za, E.zeta((-5*l*b)%60)), C[(j,l)])))
    out[f"chi5={c5},chi3={c3}"] = dict(partial=[str(x) for x in hp(t)], cells=cnt//4)
    print(f"class-1 sector chi5={c5:+d}, chi3={c3:+d}: partial {[str(x) for x in hp(t)]} ({cnt//4} cells)")
# also the class-5 cells refined by chi3 (det invertible mod 3 there)
for c3 in (1,-1):
    t = E.ZERO; cnt = 0
    for (a,b,s) in SLOT:
        for j in range(o1):
            za = E.zeta((-3*j*a)%60)
            for l in range(o2):
                d = det_gm(j,l)
                if gcd(d,15)!=5: continue
                if chi3(d)!=c3: continue
                cnt += 1
                t = E.add(t, E.scal(Fr(s,240), E.mul(E.mul(za, E.zeta((-5*l*b)%60)), C[(j,l)])))
    out[f"cls5,chi3={c3}"] = dict(partial=[str(x) for x in hp(t)], cells=cnt//4)
    print(f"class-5 sector chi3={c3:+d}: partial {[str(x) for x in hp(t)]} ({cnt//4} cells)")
json.dump(out, open(os.path.join(HERE, "p3_genus.json"), "w"), indent=1)
print("DONE")
