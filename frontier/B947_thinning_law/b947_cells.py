#!/usr/bin/env python3
"""B947 / L130 -- is the thinning law a LAW?  Sealed 610fa711..., before compute.

Normalisation-FREE restatement: for each banked value family, take the
integer-primitive minimal polynomial and ask whether the EXTREME coefficients
are thin while the extra primes live in the MIDDLE.  No lambda anywhere.
"""
import json
import pathlib

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
B941 = json.load(open(HERE.parent / "B941_branch_symmetric" / "results.json"))
R = {}

# ---------------- CELL 0: the banked-identity gate --------------------------
e1, e2, e3 = [sp.Rational(x) for x in B941["symmetric_functions"]["V_hierarchy"]]
lam = sp.Rational(2304, 953)
gate = (sp.simplify(e1/lam**4 - sp.Rational(3*13*421493, 2**24)) == 0 and
        sp.simplify(e2/lam**4 - sp.Rational(17*1129, 2**11)) == 0 and
        sp.simplify(e3/lam**4 - 27) == 0)
R["banked_identity_gate"] = bool(gate)
assert gate, "INSTRUMENT FAILURE: B946's V-table not reproduced; no verdict is read"
print("CELL 0 banked-identity gate: PASSED")

# ---------------- the test --------------------------------------------------
x = sp.symbols('x')


def support(n):
    n = abs(int(n))
    return set(sp.factorint(n)) if n not in (0, 1) else set()


rows = {}
for fam, ee in B941["symmetric_functions"].items():
    E = [sp.Rational(v) for v in ee]
    poly = sp.Poly(x**3 - E[0]*x**2 + E[1]*x - E[2], x)
    prim = sp.Poly(poly.as_expr() * sp.lcm([c.q for c in poly.all_coeffs()]), x)
    co = [sp.Integer(c) for c in prim.all_coeffs()]
    co = [c // sp.igcd(*[abs(int(t)) for t in co if t != 0]) for c in co]  # primitive
    P_lead, P_const = support(co[0]), support(co[-1])
    P_mid = set().union(*[support(c) for c in co[1:-1]]) if len(co) > 2 else set()
    P_mid_only = P_mid - P_lead - P_const
    total = P_lead | P_const | P_mid
    excluded = len(total) <= 3
    holds = (len(P_lead) <= 2 and len(P_const) <= 2 and len(P_mid_only) >= 1)
    rows[fam] = {"coeffs": [int(c) for c in co],
                 "P_lead": sorted(P_lead), "P_const": sorted(P_const),
                 "P_mid_only": sorted(P_mid_only),
                 "total_support_size": len(total),
                 "excluded_vacuous": excluded, "pattern_holds": holds}
    print(f"  {fam:18s} lead={sorted(P_lead)} const={sorted(P_const)} "
          f"mid_only={sorted(P_mid_only)} excl={excluded} holds={holds}")

R["families"] = rows
live = {k: v for k, v in rows.items() if not v["excluded_vacuous"]}
R["excluded"] = sorted(k for k, v in rows.items() if v["excluded_vacuous"])
R["live"] = sorted(live)
R["n_live"] = len(live)
R["all_live_hold"] = all(v["pattern_holds"] for v in live.values()) if live else None
R["failures"] = sorted(k for k, v in live.items() if not v["pattern_holds"])
R["verdict"] = "LAW" if R["all_live_hold"] else "SPECIAL"

print()
print("excluded (vacuous, support <= 3):", R["excluded"])
print("live families:", R["live"])
print("failures:", R["failures"])
print("VERDICT:", R["verdict"])
pathlib.Path(HERE / "results.json").write_text(json.dumps(R, indent=1) + "\n")
