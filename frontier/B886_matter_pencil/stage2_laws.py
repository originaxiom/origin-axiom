#!/usr/bin/env python3
"""B886 stage 2 -- the six Pi-weights of matter, their Galois structure, and the
two B885 laws as exact theorems.

From stage 1: P(x, lambda) = F1(x,lambda)^1 * F2(x,lambda)^8, both cubic in x.
Hence the 27 has SIX joint Pi-weights: the F1-orbit {w_k} (mult 1) and the
F2-orbit {u_k} (mult 8), each a size-3 Galois orbit of pairs (a, b) with
eigenvalue branch x = a + b*lambda.

This stage, all exact (sympy algebraic arithmetic):
  (a) extract the weight pairs; identify their field vs K = Q[rho]/mu
      (field_isomorphism);
  (b) certify the collision pattern at each mu-root: {1,1,1,8,8,8} ->
      {1, 1+1+8, 8+8} (which w's/u's collide where);
  (c) LAW 1: the lone (singlet) w-branch of root r_i, evaluated at r_j (i != j),
      equals the 10-value at r_j -- exact zero via minimal_polynomial;
  (d) LAW 2: it differs from the singlet value at r_j -- exact nonzero.
"""
import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
S1 = json.load(open(os.path.join(HERE, "results_stage1.json")))
x, lam, b = sp.symbols("x lambda b")
rho = sp.symbols("rho")
F1 = sp.sympify(S1["sing_factor"].replace("lambda", "lam_"), locals={"lam_": lam, "x": x})
FL = [sp.sympify(f["factor"].replace("lambda", "lam_"), locals={"lam_": lam, "x": x})
      for f in S1["factor_structure"]]
F1 = [f for f, meta in zip(FL, S1["factor_structure"]) if meta["mult"] == 1][0]
F2 = [f for f, meta in zip(FL, S1["factor_structure"]) if meta["mult"] == 8][0]
MU = 500716339200 * rho**3 - 2075673600 * rho**2 - 4769856 * rho + 2197

print("[a] weight pairs...")
def weight_pairs(F):
    """F(x, lam) = c * prod (x - a_k - b_k lam): return the cubic B(b) whose
    roots are the b_k, and a_k as a rational function of b_k."""
    Fp = sp.Poly(F, x, lam)
    # homogeneous degree-3 part, x -> b, lam -> 1:
    B = sp.expand(sum(c * b**m[0] for m, c in zip(Fp.monoms(), Fp.coeffs())
                      if m[0] + m[1] == 3))
    Bp = sp.Poly(B, b)
    # a(b): from dF: write F(a + b*lam + eps...) -- use: F as poly in x; the root
    # x(lam) = a + b lam; match the lam^2-coefficient of F(a + b lam, lam) = 0
    # expansion: solve for a symbolically: substitute x = a + b*lam, expand in lam,
    # require ALL coefficients zero; the top one gives B(b) = 0; the next gives a
    # linearly in terms of b:
    a = sp.symbols("a")
    E = sp.expand(F.subs(x, a + b * lam))
    Ep = sp.Poly(E, lam)
    c2 = Ep.coeff_monomial(lam**2)
    asol = sp.solve(sp.Eq(c2, 0), a)
    return Bp, sp.simplify(asol[0])

B1, a1_of_b = weight_pairs(F1)
B2, a2_of_b = weight_pairs(F2)
print(f"    F1 b-cubic: {sp.sstr(B1.as_expr())[:100]}")
print(f"    F2 b-cubic: {sp.sstr(B2.as_expr())[:100]}")

print("[b] fields...")
KM = sp.Poly(MU, rho)
from sympy.polys.numberfields import field_isomorphism
th_mu = sp.RootOf(MU, 0)
th_b1 = sp.RootOf(B1.as_expr(), 0)
th_b2 = sp.RootOf(B2.as_expr(), 0)
iso1 = field_isomorphism(th_b1, th_mu)
iso2 = field_isomorphism(th_b2, th_mu)
print(f"    Q(b of F1) isomorphic to K: {iso1 is not None}")
print(f"    Q(b of F2) isomorphic to K: {iso2 is not None}")

print("[c] collisions + [d] the laws, exactly over the splitting field...")
# work with the three real roots of mu as RootOf (indexed) and the branch values
r = [sp.RootOf(MU, k) for k in range(3)]
def branches(Bp, a_of_b):
    out = []
    for k in range(3):
        bk = sp.RootOf(Bp.as_expr(), k)
        ak = a_of_b.subs(b, bk)
        out.append((ak, bk))
    return out
W = branches(B1, a1_of_b)   # mult-1 weights
U = branches(B2, a2_of_b)   # mult-8 weights

def val(pair, rr):
    return sp.simplify(pair[0] + pair[1] * rr)

results = {"collisions": [], "law1": [], "law2": []}
for i in range(3):
    vals_w = [val(Wk, r[i]) for Wk in W]
    vals_u = [val(Uk, r[i]) for Uk in U]
    # find the lone w: the one NOT equal to any u-value at r_i
    eqmat = []
    for kw, vw in enumerate(vals_w):
        hits = []
        for ku, vu in enumerate(vals_u):
            d = sp.nsimplify(vw - vu)
            z = sp.minimal_polynomial(d, x) == sp.Poly(x, x).as_expr() or \
                sp.simplify(d) == 0 or sp.minimal_polynomial(d, x).subs(x, 0) == 0
            # robust exact-zero test:
            z = (sp.minimal_polynomial(vw - vu, x)).as_poly(x).all_coeffs()[-1] == 0
            if z:
                hits.append(ku)
        eqmat.append(hits)
    lone = [kw for kw, h in enumerate(eqmat) if not h]
    results["collisions"].append(dict(root=i, w_u_hits=eqmat, lone_w=lone))
    print(f"    root {i}: w-vs-u collisions {eqmat}, lone w: {lone}")

# LAW 1 & 2: the lone w of root i, at root j
for i in range(3):
    lw = results["collisions"][i]["lone_w"]
    if len(lw) != 1:
        continue
    Wi = W[lw[0]]
    for j in range(3):
        if j == i:
            continue
        vij = val(Wi, r[j])
        # the 10-value at r_j = the collided value: any u that collides with a w at j
        ej = results["collisions"][j]
        col_w = [kw for kw, h in enumerate(ej["w_u_hits"]) if h]
        u10 = ej["w_u_hits"][col_w[0]][0]
        d10 = vij - val(U[u10], r[j])
        z10 = sp.minimal_polynomial(d10, x).as_poly(x).all_coeffs()[-1] == 0
        lonej = ej["lone_w"][0]
        d1 = vij - val(W[lonej], r[j])
        z1 = sp.minimal_polynomial(d1, x).as_poly(x).all_coeffs()[-1] == 0
        results["law1"].append(dict(i=i, j=j, equals_10=bool(z10)))
        results["law2"].append(dict(i=i, j=j, equals_singlet=bool(z1)))
        print(f"    lone-w({i}) at r_{j}: = e10(r_{j})? {z10}   = e1(r_{j})? {z1}")

results["law1_all"] = all(e["equals_10"] for e in results["law1"])
results["law2_all"] = all(not e["equals_singlet"] for e in results["law2"])
results["fields_match_K"] = [iso1 is not None, iso2 is not None]
json.dump({k: v for k, v in results.items() if k != "collisions"} |
          {"collisions": [{kk: vv for kk, vv in c.items()} for c in results["collisions"]]},
          open(os.path.join(HERE, "results_stage2.json"), "w"), indent=1, default=str)
print(f"  LAW 1 (all pairs): {results['law1_all']}   LAW 2 (all pairs): {results['law2_all']}")
