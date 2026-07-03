"""B385 -- the commuting reformulation: field-level quasi-periods of the raw Par-tables.

Find all (dj,dl,r): C[j+dj, l+dl] = zeta60^r * C[j,l] for ALL cells (exact). Each induces the
support rule: t(a,b) != 0 => z1*dj*a + z2*dl*b == r (mod 60), z_i = 60/o_i -- commutes with
the DFT by construction."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

PAIRS = [((1,2),"bright"),((2,3),"bright"),((2,4),"bright"),((3,4),"bright"),
         ((1,7),"bright"),((3,7),"bright"),((2,7),"bright"),
         ((1,3),"dark"),((1,4),"dark"),((3,5),"dark"),((1,5),"dark"),((4,5),"dark")]

def table(m1, m2):
    W1 = build_theta_W(m1); W2 = build_theta_W(m2)
    o1, p1 = matrix_order(W1); o2, p2 = matrix_order(W2)
    return {(j,l): par_trace(p1[j], p2[l]) for j in range(o1) for l in range(o2)}, o1, o2

def qscan(C, o1, o2):
    out = []
    cells = list(C.items())
    nz = [(k,v) for k,v in cells if v != E.ZERO]
    for dj in range(o1):
        for dl in range(o2):
            if (dj,dl) == (0,0): continue
            # r from first nonzero cell
            (j0,l0), v0 = nz[0]
            w = C[((j0+dj)%o1, (l0+dl)%o2)]
            r = None
            for k in range(60):
                if w == E.mul(E.zeta(k), v0): r = k; break
            if r is None: continue
            zr = E.zeta(r)
            if all(C[((j+dj)%o1,(l+dl)%o2)] == E.mul(zr, v) for (j,l), v in cells):
                out.append((dj,dl,r))
    return out

res = {}
for (m1,m2), st in PAIRS:
    C,o1,o2 = table(m1,m2)
    Q = qscan(C,o1,o2)
    res[f"{m1},{m2}"] = dict(status=st, ords=[o1,o2], Q=[list(x) for x in Q])
    print(f"({m1},{m2}) {st:7s} ords {o1}x{o2}: quasi-periods {Q}")
json.dump(res, open(os.path.join(HERE,"quasiperiods.json"),"w"), indent=1)
print("DONE")
