#!/usr/bin/env python3
"""B893 -- W7 opening cell: the Chevalley involution vs the measurement structure.

omega: e_alpha -> -e_{-alpha}, h -> -h -- exact, linear, the canonical Cartan-type
involution of the split build (fixed set = the maximal compact direction data).
Computed exactly over Q:
  (a) omega on the four torus charges x8, x14, x16, x22 (are they eigenvectors?);
  (b) omega on the plane Pi = tri(C) (the c-on-C question: does omega realize the
      side-of-C flip as an eigen-structure on the plane?);
  (c) omega vs the pencil: omega(x8 + t x16) -- does the compact conjugation fix,
      negate, or permute the enhancement points (the Galois triple)?
All exact; brackets verified: omega is an automorphism check on 2000 random pairs.
"""
import json
import os
import random
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
g = {"__file__": B854, "__name__": "b854"}
exec(compile(open(B854).read(), B854, "exec"), g)
DIM, N = g["DIM"], g["N"]
br, ROOTS, IDX = g["br"], g["ROOTS"], g["IDX"]

NEG = {}
for r, k in IDX.items():
    NEG[N + k] = N + IDX[tuple(-x for x in r)]


def omega(v):
    # d == 1 lattice character: omega(e_alpha) = e_{-alpha}, h -> -h.
    # (A global -1 on root vectors is NOT a lattice character -- first-run bug;
    # this build's cocycle has eps(a,-a) = eps(-a,a), so d == 1 closes.)
    out = [Fr(0)] * DIM
    for i in range(N):
        out[i] = -v[i]
    for p in range(N, DIM):
        out[NEG[p]] = v[p]
    return out


print("[1] omega is an automorphism (random exact check)...")
random.seed(3)
ok = True
for _ in range(2000):
    p, q_ = random.randrange(DIM), random.randrange(DIM)
    ep = [Fr(0)] * DIM; ep[p] = Fr(1)
    eq = [Fr(0)] * DIM; eq[q_] = Fr(1)
    lhs = omega(br(ep, eq))
    rhs = br(omega(ep), omega(eq))
    if lhs != rhs:
        ok = False
        break
print(f"    omega([x,y]) == [omega x, omega y]: {ok}")

print("[2] omega on the four charges...")
res = dict(automorphism=ok, charges={})
evals = {}
for n in (8, 14, 16, 22):
    v = list(g["INV"][n])
    w = omega(v)
    # eigenvector test: w == c*v?
    lam = None
    for a, b in zip(w, v):
        if b != 0:
            lam = Fr(a) / Fr(b)
            break
    is_eig = all(Fr(w[i]) == lam * Fr(v[i]) for i in range(DIM)) if lam is not None else False
    evals[n] = str(lam) if is_eig else "NOT-EIGEN"
    res["charges"][f"x{n}"] = evals[n]
    print(f"    omega(x{n}) = {evals[n]} * x{n}" if is_eig
          else f"    omega(x{n}): NOT an eigenvector")

print("[3] omega vs the pencil / the Galois triple...")
# omega(x8 + t x16) = e8*x8 + t*e16*x16 where e = the eigenvalues above (if eigen)
if evals.get(8) not in (None, "NOT-EIGEN") and evals.get(16) not in (None, "NOT-EIGEN"):
    e8, e16 = Fr(evals[8]), Fr(evals[16])
    # pencil point t maps to: e8*(x8 + (t*e16/e8) x16) -> parameter t' = t*e16/e8
    ratio = e16 / e8
    res["pencil_action"] = f"t -> {ratio} * t (overall scale {e8})"
    print(f"    omega: s(t) -> {e8} * s({ratio} * t): the enhancement set maps by t -> {ratio}*t")
    if ratio == 1:
        print("    => omega FIXES each enhancement line individually")
        res["triple_action"] = "each line fixed"
    elif ratio == -1:
        print("    => omega maps the line at t to the line at -t: the triple maps to the NEGATED cubic's roots")
        res["triple_action"] = "t -> -t (check: is the root set symmetric?)"
    else:
        res["triple_action"] = f"t -> {ratio} t"
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1)
print("done")

# ---- [4] does omega preserve the TORUS, and what is its 4x4 action there?
print("[4] omega on the torus C as a whole...")
import sympy as sp
INVv = {n: [sp.Rational(c.numerator, c.denominator) for c in g["INV"][n]]
        for n in (8, 14, 16, 22)}
OM = {n: omega(g["INV"][n]) for n in (8, 14, 16, 22)}
B = sp.Matrix([[INVv[n][i] for n in (8, 14, 16, 22)] for i in range(DIM)])
M4 = {}
preserved = True
for n in (8, 14, 16, 22):
    w = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in OM[n]])
    sol = B.solve_least_squares(w)
    res_ = sp.simplify((B * sol - w).norm())
    if res_ != 0:
        preserved = False
        print(f"    omega(x{n}) NOT in span(C) (residual {res_})")
    else:
        M4[n] = [sp.nsimplify(x) for x in sol]
        print(f"    omega(x{n}) = {M4[n]} . (x8,x14,x16,x22)")
res["torus_preserved"] = preserved
if preserved:
    Mm = sp.Matrix([M4[n] for n in (8, 14, 16, 22)]).T
    ev = Mm.eigenvals()
    res["omega_on_C_matrix"] = str(Mm.tolist())
    res["omega_on_C_eigenvalues"] = {str(k): int(v) for k, v in ev.items()}
    print(f"    eigenvalues of omega|C: {res['omega_on_C_eigenvalues']}")
    # action on the plane span(x8,x16)?
    sub = Mm.extract([0, 2], [0, 2])
    offd = Mm.extract([1, 3], [0, 2])
    plane_pres = all(x == 0 for x in offd)
    res["plane_preserved"] = bool(plane_pres)
    print(f"    plane span(x8,x16) preserved: {plane_pres}"
          + (f"; omega|plane = {sub.tolist()}" if plane_pres else ""))
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1)
