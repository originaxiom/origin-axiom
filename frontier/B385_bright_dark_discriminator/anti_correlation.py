"""B385 -- the joint-label correlation: which (class(gamma'), v_word) labels carry anti-content
in the bright riddle table (3,4), and does the dark twin (1,3) ever visit those labels?"""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace
from vword_probe import word_shift, ORDS

def anti_cells(m1, m2):
    W1 = build_theta_W(m1); W2 = build_theta_W(m2)
    o1, p1 = matrix_order(W1); o2, p2 = matrix_order(W2)
    out = {}
    for j in range(o1):
        for l in range(o2):
            C = par_trace(p1[j], p2[l])
            sol = SC.solve_H(SC.H_avg(C))
            g, v = word_shift(m1, m2, j, l)
            d = ((-g[0][0]-1)*(-g[1][1]-1) - g[0][1]*g[1][0]) % 15
            cls = gcd(d, 15)
            has_anti = sol is not None and (sol[2] != 0 or sol[3] != 0)
            out[(j,l)] = dict(cls=cls, v5=(v[0]%5, v[1]%5), v3=(v[0]%3, v[1]%3),
                              anti=has_anti,
                              anti_vals=(str(sol[2]), str(sol[3])) if has_anti else None)
    return out

B = anti_cells(3,4)   # bright
D = anti_cells(1,3)   # dark
nb = sum(1 for r in B.values() if r["anti"])
nd = sum(1 for r in D.values() if r["anti"])
print(f"(3,4) anti-carrying cells: {nb}/{len(B)};  (1,3): {nd}/{len(D)} (expect 0)")

lab_b_anti = {(r["cls"], r["v5"]) for r in B.values() if r["anti"]}
lab_b_all  = {(r["cls"], r["v5"]) for r in B.values()}
lab_d_all  = {(r["cls"], r["v5"]) for r in D.values()}
print("bright anti labels (cls, v5):", sorted(lab_b_anti))
print("dark grid visits those labels:", sorted(lab_b_anti & lab_d_all))
print("bright-anti labels NOT in dark grid:", sorted(lab_b_anti - lab_d_all))
# finer: with v3 too
lab_b_anti3 = {(r["cls"], r["v5"], r["v3"]) for r in B.values() if r["anti"]}
lab_d_all3  = {(r["cls"], r["v5"], r["v3"]) for r in D.values()}
print("with v3: bright-anti labels missed by dark:", sorted(lab_b_anti3 - lab_d_all3))
json.dump(dict(bright_anti=sorted([[list(x[0]) if isinstance(x[0],tuple) else x[0], list(x[1])] for x in lab_b_anti], key=str),
               nb=nb, nd=nd,
               missed=[[x[0], list(x[1])] for x in sorted(lab_b_anti - lab_d_all, key=str)]),
          open(os.path.join(HERE,"anti_correlation.json"),"w"), indent=1)
print("DONE")
