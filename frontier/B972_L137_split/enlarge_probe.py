#!/usr/bin/env python3
"""B972 SCOUT -- enlarge the B947 sample beyond the seven.

Fresh families found by repo grep, with banked coefficients:
  PENCIL side (+2): B888's vacuum-weight and generic-weight b-cubics, rebuilt
                    here from B888's own pencil_factors.json with B888's own
                    bcubic() -- and cross-checked against B888's banked
                    discriminant squarefree part 77.
  VALUE side  (+1): B914's T, the colorless coupling invariant (deg 3, banked
                    minpoly_desc_coeffs), plus its row-product T^3.

B947's sealed statistic is applied verbatim.  NOTHING here is sealed; this is
scouting for whether an L137 cell would have a sample worth sealing.
"""
import json
import pathlib

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
x, lam, b = sp.symbols("x lambda b")
OUT = {}


def support(n):
    n = abs(int(n))
    return set(int(p) for p in sp.factorint(n)) if n not in (0, 1) else set()


def b947(co, name):
    co = [sp.Integer(c) for c in co]
    g = sp.igcd(*[abs(int(c)) for c in co if c != 0])
    co = [c // g for c in co]
    Pl, Pc = support(co[0]), support(co[-1])
    Pm = set().union(*[support(c) for c in co[1:-1]])
    Pmo = Pm - Pl - Pc
    tot = Pl | Pc | Pm
    return {"name": name, "P_lead": sorted(Pl), "P_const": sorted(Pc),
            "P_mid_only": sorted(Pmo), "total_support_size": len(tot),
            "excluded_vacuous": len(tot) <= 3,
            "pattern_holds": len(Pl) <= 2 and len(Pc) <= 2 and len(Pmo) >= 1,
            "lead_digits": len(str(abs(int(co[0])))),
            "const_digits": len(str(abs(int(co[-1]))))}


# ---- PENCIL side: B888's two further cubics --------------------------------
S1 = json.load(open(ROOT / "frontier/B888_two_fields/pencil_factors.json"))
FL = [sp.sympify(f["factor"].replace("lambda", "lam_"),
                 locals={"lam_": lam, "x": x}) for f in S1["factor_structure"]]
F1 = [f for f, m in zip(FL, S1["factor_structure"]) if m["mult"] == 1][0]
F2 = [f for f, m in zip(FL, S1["factor_structure"]) if m["mult"] == 8][0]


def bcubic(F):                       # B888's own function, copied verbatim
    Fp = sp.Poly(F, x, lam)
    B = sp.expand(sum(cf * b**m[0] for m, cf in zip(Fp.monoms(), Fp.coeffs())
                      if m[0] + m[1] == 3))
    return sp.Poly(B, b)


for nm, F in (("vacuum_weight_cubic (B888, mult-1, field != K)", F1),
              ("generic_weight_cubic (B888, mult-8, field = K)", F2)):
    P = bcubic(F)
    co = [int(c) for c in P.all_coeffs()]
    row = b947(co, nm)
    d = sp.discriminant(P.as_expr(), b)
    sf = sp.Integer(1)
    for pr, e in sp.factorint(sp.Integer(abs(d))).items():
        if e % 2:
            sf *= pr
    row["coeffs"] = co
    row["disc_squarefree_part"] = int(sf)
    row["REPRODUCES_B888_BANKED_77"] = bool(sf == 77)
    OUT[nm] = row
    print(json.dumps(row, indent=1))

# ---- VALUE side: B914's T ---------------------------------------------------
B914 = json.load(open(ROOT / "frontier/B914_ratio_table/results.json"))
for key, nm in (("T_single", "T colorless coupling invariant (B914)"),):
    co = [int(c) for c in B914[key]["minpoly_desc_coeffs"]]
    print(f"\nfactoring {nm} (lead has {len(str(abs(co[0])))} digits) ...")
    row = b947(co, nm)
    OUT[nm] = row
    print(json.dumps(row, indent=1))

(HERE / "enlarge_probe_out.json").write_text(json.dumps(OUT, indent=1) + "\n")
