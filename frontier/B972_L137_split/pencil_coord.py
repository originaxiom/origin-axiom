#!/usr/bin/env python3
"""B972 / L137 addendum -- is a PENCIL cubic's verdict a property of the OBJECT?

A pencil A + t.B has a canonical 0 and a canonical infinity but NO canonical unit:
t -> t/c (c in Q*) is a symmetry of the object, not a change of object.  Under it
   (a3,a2,a1,a0) -> (a3, a2 c, a1 c^2, a0 c^3), re-primitivised.
So for a pencil cubic B947's statistic is only well-defined once a coordinate is
chosen.  This script asks, for each pencil cubic, whether the verdict changes
across that gauge orbit.  (For a VALUE family there is no such freedom: the
element is a specific number and its minimal polynomial is canonical.  That
asymmetry is the whole point.)

Also: the norm identity N(alpha) = -a0/a3, which re-reads B947's two extreme
clauses as a statement about the DIVISOR of alpha.
"""
import itertools
import json
import pathlib

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = {}
x, lam, bb = sp.symbols("x lambda b")
G = range(-80, 81)


def prim(co):
    co = [sp.Integer(int(c)) for c in co]
    g = sp.igcd(*[abs(int(c)) for c in co if c != 0])
    return [c // g for c in co]


def loc(v, g):
    w = [v[0], v[1] + g, v[2] + 2 * g, v[3] + 3 * g]
    m = min(w)
    return tuple(t - m > 0 for t in (w[0], max(w[1], w[2]), w[3]))


def orbit(co, bound=None):
    co = prim(co)
    P = set()
    for c in co:                       # coefficients here all factor completely
        if c != 0:
            P |= {int(p) for p in sp.factorint(abs(int(c)))}
    P = sorted(P)
    per, forced = {}, []
    for p in P:
        v = [sp.multiplicity(p, abs(int(c))) if c != 0 else 10 ** 9 for c in co]
        st = sorted(set(loc(v, g) for g in G))
        per[p] = st
        if not any((not a) and (not c) for a, _, c in st):
            forced.append(p)
    hold, witness = 0, None
    for combo in itertools.product(*[per[p] for p in P]):
        lead = [p for p, s in zip(P, combo) if s[0]]
        const = [p for p, s in zip(P, combo) if s[2]]
        mo = [p for p, s in zip(P, combo) if s[1] and p not in lead and p not in const]
        if len(lead) <= 2 and len(const) <= 2 and len(mo) >= 1:
            hold += 1
            witness = witness or {"P_lead": lead, "P_mid_only": mo, "P_const": const}
    return {"support": P, "F": len(forced), "forced": forced,
            "n_coordinates_in_the_gauge_orbit_that_HOLD": hold,
            "VERDICT_IS_COORDINATE_DEPENDENT": hold > 0, "witness": witness}


PEN = [("mu_charge  @ B941/B947 coord (rho=13t)", [500716339200, -2075673600, -4769856, 2197]),
       ("mu_charge  @ B866's own coord t", [500716339200, -159667200, -28224, 1]),
       ("kappa_compact @ B910 coord", [2771822592000, 3033676800, -56402640, -6859])]

S1 = json.load(open(ROOT / "frontier/B888_two_fields/pencil_factors.json"))
FL = [(sp.sympify(f["factor"].replace("lambda", "lam_"), locals={"lam_": lam, "x": x}), f["mult"])
      for f in S1["factor_structure"]]
for mult, nm in ((1, "vacuum_weight_cubic_B888"), (8, "generic_weight_cubic_B888")):
    F = [f for f, m in FL if m == mult][0]
    Fp = sp.Poly(F, x, lam)
    B = sp.expand(sum(cf * bb ** m[0] for m, cf in zip(Fp.monoms(), Fp.coeffs())
                      if m[0] + m[1] == 3))
    PEN.append((nm, [int(c) for c in sp.Poly(B, bb).all_coeffs()]))

# B888 banked-identity gate: its own squarefree discriminant part must be 77
d = [sp.factorint(sp.Poly(co, x).discriminant()) for nm, co in PEN[3:]]
sqfree = [int(sp.prod([p for p, e in f.items() if e % 2])) for f in d]
OUT["B888_gate_squarefree_disc_part"] = sqfree
print("GATE  B888 squarefree discriminant parts (banked value 77):", sqfree)

print("\nIS THE PENCIL VERDICT A PROPERTY OF THE OBJECT?\n")
rows = {}
for nm, co in PEN:
    r = orbit(co)
    rows[nm] = r
    print(f"  {nm:42s} F={r['F']} forced={r['forced']}")
    print(f"      {'':40s} verdict flips under t->t/c : {r['VERDICT_IS_COORDINATE_DEPENDENT']}"
          + (f"   witness {r['witness']}" if r['witness'] else ""))
OUT["pencil_gauge_orbit"] = rows

# ---- the norm re-reading: N(alpha) = -a0/a3
print("\nB947's TWO EXTREME CLAUSES, RE-READ AS THE DIVISOR OF alpha\n")
B947 = json.load(open(ROOT / "frontier/B947_thinning_law/results.json"))
FAM = {f: [int(c) for c in r["coeffs"]] for f, r in B947["families"].items()}
FAM.update({"m_A_flipmass": [42467328, -56070144, 19828224, -2113201],
            "X_cross_overlap_sq": [908209, 1049253, 253875, -15625],
            "u_B937": [28179280429056, -3057647616000, 53136000000, -244140625]})
norms = {}
for nm, co in FAM.items():
    N = sp.Rational(-co[3], co[0])
    num, den = sp.factorint(N.p), sp.factorint(N.q)
    norms[nm] = {"norm": str(N),
                 "norm_numerator": "*".join(f"{p}^{e}" for p, e in sorted(num.items())) or "1",
                 "norm_denominator": "*".join(f"{p}^{e}" for p, e in sorted(den.items())) or "1",
                 "zeros_over": sorted(num), "poles_over": sorted(den)}
    print(f"  {nm:22s} N = {norms[nm]['norm_numerator']} / {norms[nm]['norm_denominator']}")
OUT["norm_divisor_reading"] = norms

(HERE / "pencil_coord_out.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
