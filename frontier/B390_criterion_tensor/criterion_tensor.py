"""B390 -- G1 (tensor gate all pairs), G2 (s-classification from local data), the
attribution, and the out-of-sample prediction machinery for (2,5)."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B386_crt_closed_form"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace
from tensor_gate import local_partrace_table, local_model

PAIRS = [((1,2),"bright"),((2,3),"bright"),((2,4),"bright"),((3,4),"bright"),
         ((1,7),"bright"),((3,7),"bright"),((2,7),"bright"),
         ((1,3),"dark"),((1,4),"dark"),((3,5),"dark"),((1,5),"dark"),((4,5),"dark")]

def hproj(t): return SC.solve_H(SC.H_avg(t))

def analyze(m1, m2, check_global=True):
    W1 = build_theta_W(m1); W2 = build_theta_W(m2)
    o1, p1 = matrix_order(W1); o2, p2 = matrix_order(W2)
    T3 = local_partrace_table(3, 2, m1, m2, o1, o2)
    T5 = local_partrace_table(5, 2, m1, m2, o1, o2)
    g1_ok = True
    if check_global:
        for j in range(o1):
            for l in range(o2):
                if par_trace(p1[j], p2[l]) != E.mul(T3[(j,l)], T5[(j,l)]):
                    g1_ok = False; break
            if not g1_ok: break
    # s-table from LOCAL data alone: t(a,b) = (1/(o1 o2)) sum w * T3 * T5, Pi_H, s-component
    z1, z2 = 60 // o1, 60 // o2
    s_bright = False
    s_cells = []
    for a in range(o1):
        for b in range(o2):
            t = E.ZERO
            for j in range(o1):
                za = E.zeta((-z1*j*a) % 60)
                for l in range(o2):
                    t = E.add(t, E.mul(E.mul(za, E.zeta((-z2*l*b) % 60)),
                                       E.mul(T3[(j,l)], T5[(j,l)])))
            sol = hproj(E.scal(Fr(1, o1*o2), t))
            if sol and sol[3] != 0:
                s_bright = True; s_cells.append((a, b))
    # side contents: does the 3-side spectrum carry sqrt-3? the 5-side sqrt5?
    def side_content(T, which):
        for a in range(o1):
            for b in range(o2):
                t = E.ZERO
                for j in range(o1):
                    za = E.zeta((-z1*j*a) % 60)
                    for l in range(o2):
                        t = E.add(t, E.mul(E.mul(za, E.zeta((-z2*l*b) % 60)), T[(j,l)]))
                sol = hproj(E.scal(Fr(1, o1*o2), t))
                if sol is None: continue
                if which == "sqrt-3" and sol[2] != 0: return True
                if which == "sqrt5" and sol[1] != 0: return True
        return False
    c3 = side_content(T3, "sqrt-3")
    c5 = side_content(T5, "sqrt5")
    return dict(ords=[o1,o2], G1=g1_ok, s_bright=s_bright, n_s_cells=len(s_cells),
                side3_sqrt3=c3, side5_sqrt5=c5)

out = {}
ok12 = True
for (m1,m2), st in PAIRS:
    r = analyze(m1, m2)
    pred = "bright" if r["s_bright"] else "dark"
    match = (pred == st)
    ok12 = ok12 and match and r["G1"]
    attribution = ("D-a (5-side dead)" if not r["side5_sqrt5"] else
                   "D-b (3-side dead)" if not r["side3_sqrt3"] else
                   ("D-c (convolution null)" if pred == "dark" else "both-sides-live"))
    r.update(status=st, predicted=pred, match=match, attribution=attribution)
    out[f"{m1},{m2}"] = r
    print(f"({m1},{m2}) {st:7s}: G1={r['G1']} pred={pred} {'OK' if match else 'MISS'} "
          f"s-cells={r['n_s_cells']:3d} side3(√-3)={r['side3_sqrt3']} side5(√5)={r['side5_sqrt5']} -> {attribution}")
print("G1+G2 12/12:", ok12)
json.dump(out, open(os.path.join(HERE, "criterion.json"), "w"), indent=1)
print("DONE")
