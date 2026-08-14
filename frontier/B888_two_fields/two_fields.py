#!/usr/bin/env python3
"""B888 -- the identity card of the matter fields: three cubics, one quadratic resolvent.

From B886: the 27's weight orbits live in two cubic fields (the vacuum orbit's field
NOT isomorphic to K; the generic orbit's isomorphic to K). This arc computes the
exact discriminant data and finds: ALL THREE cubics (vacuum, generic, and mu itself)
share the SAME squarefree discriminant part 77 = 7 * 11 -- one quadratic resolvent
Q(sqrt(77)) inside all three S3-closures. The exponent echo (7, 11 = the exponents
of the two UNMEASURED torus charges x14, x22, while the measured plane is built from
the exponent-(4, 8) charges) is recorded as an OBSERVATION, unweighted.
"""
import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
x, lam, b, rho = sp.symbols("x lambda b rho")
S1 = json.load(open(os.path.join(HERE, "pencil_factors.json")))
FL = [sp.sympify(f["factor"].replace("lambda", "lam_"), locals={"lam_": lam, "x": x})
      for f in S1["factor_structure"]]
F1 = [f for f, m in zip(FL, S1["factor_structure"]) if m["mult"] == 1][0]
F2 = [f for f, m in zip(FL, S1["factor_structure"]) if m["mult"] == 8][0]


def bcubic(F):
    Fp = sp.Poly(F, x, lam)
    B = sp.expand(sum(c * b ** m[0] for m, c in zip(Fp.monoms(), Fp.coeffs())
                      if m[0] + m[1] == 3))
    return sp.Poly(B, b)


def card(P, gen):
    d = sp.discriminant(P.as_expr(), gen)
    fac = sp.factorint(sp.Integer(abs(d)))
    sf = sp.Integer(1)
    for pr, e in fac.items():
        if e % 2:
            sf *= pr
    return dict(disc_factorization={str(k): int(v) for k, v in fac.items()},
                disc_sign=1 if d > 0 else -1,
                squarefree_part=int(sf if d > 0 else -sf),
                irreducible=bool(sp.Poly(P).is_irreducible))


B1, B2 = bcubic(F1), bcubic(F2)
MU = sp.Poly(500716339200 * rho ** 3 - 2075673600 * rho ** 2
             - 4769856 * rho + 2197, rho)
res = dict(vacuum_cubic=card(B1, b), generic_cubic=card(B2, b),
           mu=card(MU, rho))
res["shared_resolvent"] = (res["vacuum_cubic"]["squarefree_part"]
                           == res["generic_cubic"]["squarefree_part"]
                           == res["mu"]["squarefree_part"] == 77)
res["exponent_echo"] = ("77 = 7*11; E6 exponents (1,4,5,7,8,11); the 2T charges "
                        "live in degrees 2*(4,7,8,11); the measured plane uses "
                        "(4,8); the resolvent remembers (7,11) -- OBSERVATION, "
                        "unweighted")
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          sort_keys=True)
for k in ("vacuum_cubic", "generic_cubic", "mu"):
    print(f"  {k}: disc {res[k]['disc_factorization']}, "
          f"sqfree {res[k]['squarefree_part']}")
print(f"  ONE RESOLVENT Q(sqrt(77)) for all three: {res['shared_resolvent']}")
