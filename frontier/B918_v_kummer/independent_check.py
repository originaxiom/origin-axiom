"""B918 independent check: re-verify the headline certificate and one
witness through sympy radical arithmetic -- no code shared with the
4-vector algebra of v_kummer.py.

1. gamma(V/mu)^3 * alpha_mu == alpha_V as radicals in Q(sqrt-231).
2. The recorded chi_3 witness for alpha_V*alpha_mu at twist (0,0):
   the embedding value reproduces and is a non-cube mod p.
"""
import json, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
r = json.load(open(os.path.join(HERE, "results.json")))
s231 = sp.sqrt(-231)

aV = sp.Rational("971519719161915524236273846912397869056/"
                 "561196311142728775801553144034942241") \
     + sp.Rational("46841873111221379530752000/"
                   "680366944138463534957761")*s231
amu = 13**6*(sp.Rational(1, 25443808051200) + s231/299873452032000)

g = [sp.sympify(t) for t in
     r["pairs"]["V__mu"]["ratio"]["cube_proofs"]["(0, 0)"]]
assert g[1] == 0 and g[2] == 0, "gamma(V/mu) must lie in Q(sqrt-231)"
gam = g[0] + g[3]*s231
assert sp.simplify(sp.expand(gam**3 * amu) - aV) == 0
print("gamma(V/mu)^3 * alpha_mu == alpha_V  (radical arithmetic): OK")

w = r["pairs"]["V__mu"]["product"]["noncube_witnesses"]["(0, 0)"]
p, r77, rm3, val = w["p"], w["r77"], w["rm3"], w["val"]
assert (r77*r77 - 77) % p == 0 and (rm3*rm3 + 3) % p == 0
beta = sp.expand(aV * amu)
a, bq = beta.as_independent(s231)
a = sp.Rational(a); bq = sp.Rational(bq/s231)
emb = (a.p*pow(a.q, -1, p) + bq.p*pow(bq.q, -1, p)*r77*rm3) % p
assert emb == val % p
assert pow(emb, (p-1)//3, p) != 1
print(f"chi_3 witness at p={p} reproduces and is a non-cube: OK")
