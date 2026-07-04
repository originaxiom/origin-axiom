"""B411 -- the hint from the negatives: is a cell's H-FIELD-TYPE a FUNCTION of gamma'
arithmetic invariants (det, trace mod 15)? P68 did the sqrt-3 part via chi_-3(det).
If (chi_-3(det), chi_5(det), tr class) -> the cell's (z-active?, s-active?, y-active?)
is DETERMINISTIC across ALL pairs, that's a local field-content dictionary: predict a
cell's field from gamma' WITHOUT computing the value. Cheap, banked-data, could ease
every future value computation."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

def chi(x, q):
    x %= q
    return 0 if x == 0 else (1 if pow(x, (q-1)//2, q) == 1 else -1)

def gdata(m1, m2):
    o1, p1 = matrix_order(build_theta_W(m1)); o2, p2 = matrix_order(build_theta_W(m2))
    def A(m): return [[(1+m*m)%15, m%15],[m%15,1]]
    def mm(a,b): return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%15,(a[0][0]*b[0][1]+a[0][1]*b[1][1])%15],
                         [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%15,(a[1][0]*b[0][1]+a[1][1]*b[1][1])%15]]
    G1=[[[1,0],[0,1]]]
    for _ in range(o1-1): G1.append(mm(G1[-1],A(m1)))
    G2=[[[1,0],[0,1]]]
    for _ in range(o2-1): G2.append(mm(G2[-1],A(m2)))
    rows = {}
    for a in range(o1):
        za = 60//o1
        for b in range(o2):
            zb = 60//o2
            g = mm(G1[a],G2[b])
            gm = ((-g[0][0]-1)%15,(-g[0][1])%15,(-g[1][0])%15,(-g[1][1]-1)%15)  # gamma'-I
            det = (gm[0]*gm[3]-gm[1]*gm[2])%15
            tr = (gm[0]+gm[3])%15
            # the cell value type
            t = E.ZERO
            for j in range(o1):
                zja = E.zeta((-za*j*a)%60)
                for l in range(o2):
                    t = E.add(t, E.mul(E.mul(zja, E.zeta((-zb*l*b)%60)), par_trace(p1[j],p2[l])))
            sol = SC.solve_H(SC.H_avg(E.scal(Fr(1,o1*o2), t)))
            if sol is None or all(x==0 for x in sol): continue
            htype = (int(sol[1]!=0), int(sol[2]!=0), int(sol[3]!=0))  # (sqrt5, sqrt-3, sqrt-15)
            key = (chi(det,3), chi(det,5), gcd(det,15))
            rows.setdefault(key, set()).add(htype)
    return rows

PAIRS = [(1,2),(1,3),(2,3),(3,4)]
agg = {}
for (m1,m2) in PAIRS:
    for key, types in gdata(m1,m2).items():
        agg.setdefault(key, set()).update(types)
print("dictionary: (chi_-3(det), chi_5(det), gcd(det,15)) -> {H-types (s5,s-3,s-15) observed}")
deterministic = True
for key in sorted(agg):
    ts = sorted(agg[key])
    det_ok = len(ts) == 1
    deterministic = deterministic and det_ok
    print(f"  {key}: {ts}  {'FUNCTION' if det_ok else 'MULTI-VALUED'}")
print("\nH-field-type is a DETERMINISTIC function of gamma' invariants:", deterministic)
json.dump({str(k): sorted(map(list,v)) for k,v in agg.items()},
          open(os.path.join(HERE,"dictionary.json"),"w"), indent=1)
print("DONE")
