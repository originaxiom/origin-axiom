"""B910 independent cross-check: re-verify the two new cube certificates and
one non-cube witness through sympy radical / polynomial arithmetic, sharing
NO code with kappa_class.py's 4-vector algebra.

- gamma3^3 * alpha_kappa == alpha_mu   (the headline [alpha_kappa]=[alpha_mu])
- gamma4^3 == alpha_vac * alpha_kappa  (vacuum + kappa = split)
- the stored chi_3 witness for alpha_mu*alpha_kappa (twist (0,0)) re-embedded
  from scratch: chi_3 != 1 proves the product is not a cube in F.

Alphas are recomputed here from the cubics' coefficients (mu, kappa pinned;
vacuum rebuilt from B888's pencil_factors.json).
"""
import json, os
import sympy as sp

R = sp.Rational
HERE = os.path.dirname(os.path.abspath(__file__))
s77, sm3 = sp.sqrt(77), sp.sqrt(-3)
s231 = s77 * sm3

def alpha(poly, g):
    P = sp.Poly(poly, g).monic()
    a2 = P.all_coeffs()[1]
    Q = sp.Poly(P.as_expr().subs(g, g - a2/3), g)
    p_, q_ = R(Q.all_coeffs()[2]), R(Q.all_coeffs()[3])
    D = -4*p_**3 - 27*q_**2
    sv = sp.sqrt(R(D, 77))
    assert sv.is_Rational
    return R(-27*q_, 2) + R(3*sv, 2) * s231

rho, s = sp.symbols("rho s")
a_mu = alpha(500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197, rho)
a_k = alpha(2771822592000*s**3 + 3033676800*s**2 - 56402640*s - 6859, s)

x, lam, b = sp.symbols("x lambda b")
S1 = json.load(open(os.path.join(HERE, "..", "B888_two_fields",
                                 "pencil_factors.json")))
Fv = [sp.sympify(f["factor"].replace("lambda", "lam_"),
                 locals={"lam_": lam, "x": x})
      for f in S1["factor_structure"]]
F1 = [f for f, m in zip(Fv, S1["factor_structure"]) if m["mult"] == 1][0]
Fp = sp.Poly(F1, x, lam)
B = sp.expand(sum(c*b**m[0] for m, c in zip(Fp.monoms(), Fp.coeffs())
                  if m[0] + m[1] == 3))
a_vac = alpha(B, b)

g3 = (1 + sm3) * (R(5239, 48013) - R(5239, 192052) * s231)
g4 = (1 + sm3) * (R(-1247616, 403) - R(311904, 403) * s231)

c1 = sp.simplify(sp.expand(g3**3 * a_k - a_mu)) == 0
c2 = sp.simplify(sp.expand(g4**3 - a_vac * a_k)) == 0
print("gamma3^3 * alpha_kappa == alpha_mu :", c1)
print("gamma4^3 == alpha_vac * alpha_kappa:", c2)
assert c1 and c2

# ---- the non-cube witness, re-embedded from scratch ----
res = json.load(open(os.path.join(HERE, "results.json")))
w = res["pairs"]["mu__kappa"]["product"]["noncube_witnesses"]["(0, 0)"]
p, r77, rm3 = w["p"], w["r77"], w["rm3"]
assert (r77*r77 - 77) % p == 0 and (rm3*rm3 + 3) % p == 0 and p % 3 == 1
t = sp.Symbol("t")   # t stands for sqrt(-231), t^2 = -231
def to_t(a):         # alphas live in Q(sqrt(-231))
    ex = sp.expand(a).rewrite(sp.Pow)
    A = ex.subs(s231, 0)
    Bc = sp.expand((ex - A) / s231)
    return sp.Poly(R(A) + R(Bc)*t, t)
prod = (to_t(a_mu) * to_t(a_k)).rem(sp.Poly(t**2 + 231, t))
Bc, A = [R(c) for c in prod.all_coeffs()]
tot = 0
for c, base in zip((A, Bc), (1, r77*rm3 % p)):
    tot = (tot + c.p * pow(c.q, -1, p) * base) % p
chi = pow(int(tot), (p-1)//3, p)
print(f"witness p={p}: embed(alpha_mu*alpha_kappa) = {tot} "
      f"(stored {w['val']}), chi_3 = {chi}")
assert tot == w["val"] and chi != 1
print("INDEPENDENT CHECK PASSED")
