#!/usr/bin/env python3
"""B972 / L137 BOUNDED WORK.

Three jobs, in order:

  GATE   reproduce the banked identity B947 itself required (B946's V-table
         factorisation) and reproduce B947's own seven-family verdict with an
         independently-written implementation of its criterion.  If either
         fails this is an INSTRUMENT FAILURE and nothing below is read.

  CENSUS enlarge the sample.  B941's seven were not the banked census; the same
         defining arcs bank SIBLING cubics of the same kind (m_A beside m_S,
         X_cross beside W, ...).  For every additional banked cubic found by a
         repo scan, compute B947's statistic at its banked normalisation.

  MB12   vacuity: show the criterion can PASS and can FAIL on this material,
         and show which side of the value/pencil line each outcome lands on.

Nothing here is sealed.  Design + measurement only.
"""
import json
import pathlib

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = {}
x = sp.Symbol("x")


# --------------------------------------------------------------------- helpers
def primitive(co):
    co = [sp.Integer(int(c)) for c in co]
    g = sp.igcd(*[abs(int(c)) for c in co if c != 0])
    return [c // g for c in co], int(g)


def support(n, trial_only=False, bound=10 ** 6):
    """Prime support.  Returns (set_of_primes, unfactored_cofactor)."""
    n = abs(int(n))
    if n in (0, 1):
        return set(), 1
    if not trial_only:
        return set(int(p) for p in sp.factorint(n)), 1
    P, m = set(), n
    for p in sp.primerange(2, bound):
        if m % p == 0:
            P.add(int(p))
            while m % p == 0:
                m //= p
        if m == 1:
            break
    return P, m


def b947_statistic(coeffs, big=False):
    """B947's sealed criterion, re-implemented from PREREGISTRATION.md verbatim:
       P_lead / P_const / P_mid_only ; holds iff |lead|<=2, |const|<=2, |mid_only|>=1 ;
       EXCLUDED-as-vacuous iff total support size <= 3."""
    co, cont = primitive(coeffs)
    Pl, cl = support(co[0], big)
    Pc, cc = support(co[-1], big)
    Pm, cm = set(), 1
    for c in co[1:-1]:
        s, r = support(c, big)
        Pm |= s
        cm *= r
    Pmo = Pm - Pl - Pc
    tot = Pl | Pc | Pm
    # a surviving cofactor > 1 contributes at least one further prime
    lead_lb = len(Pl) + (1 if cl > 1 else 0)
    const_lb = len(Pc) + (1 if cc > 1 else 0)
    holds = (lead_lb <= 2) and (const_lb <= 2) and (len(Pmo) >= 1)
    decided = (cl == 1 and cc == 1 and cm == 1) or (lead_lb > 2 or const_lb > 2)
    return {
        "content_removed": cont,
        "P_lead": sorted(Pl), "P_lead_size_lower_bound": lead_lb,
        "P_const": sorted(Pc), "P_const_size_lower_bound": const_lb,
        "P_mid_only": sorted(Pmo),
        "total_support_size_lower_bound": len(tot) + (1 if cl * cc * cm > 1 else 0),
        "unfactored_cofactors": {"lead": int(cl), "const": int(cc), "mid": int(cm)},
        "EXCLUDED_vacuous": (cl * cc * cm == 1) and len(tot) <= 3,
        "HOLDS": bool(holds),
        "verdict_decidable": bool(decided),
    }


# ------------------------------------------------------------------- GATE 1/2
gate = {}
B947 = json.load(open(ROOT / "frontier/B947_thinning_law/results.json"))
V = [int(c) for c in B947["families"]["V_hierarchy"]["coeffs"]]
want = [sp.Integer(953) ** 4,
        -sp.Integer(2) ** 8 * sp.Integer(3) ** 9 * 13 * 421493,
        sp.Integer(2) ** 21 * sp.Integer(3) ** 8 * 17 * 1129,
        -sp.Integer(2) ** 32 * sp.Integer(3) ** 11]
gate["B946_V_table_factorisation_reproduced"] = [int(w) for w in want] == V
gate["V_coeffs"] = V

B918 = json.load(open(ROOT / "frontier/B918_v_kummer/results.json"))
gate["B918_hier_cubic_agrees"] = [int(c) for c in B918["hier_cubic"]["coeffs"]] == V

# reproduce B947's own seven-family verdict with this independent implementation
seven, repro = {}, {}
for fam, rec in B947["families"].items():
    st = b947_statistic([int(c) for c in rec["coeffs"]])
    seven[fam] = st
    banked = rec.get("holds", rec.get("pattern_holds"))
    repro[fam] = {"mine": st["HOLDS"], "banked": banked,
                  "agree": (banked is None) or (bool(banked) == st["HOLDS"])}
gate["B947_seven_reproduced"] = all(r["agree"] for r in repro.values())
gate["B947_reproduction_detail"] = repro
gate["B947_5_2_split_reproduced"] = sum(s["HOLDS"] for s in seven.values()) == 5
OUT["GATE"] = gate
OUT["the_seven"] = seven

print("GATE  B946 V-table factorisation reproduced :", gate["B946_V_table_factorisation_reproduced"])
print("GATE  B918 hier cubic agrees                :", gate["B918_hier_cubic_agrees"])
print("GATE  B947 seven-family verdict reproduced  :", gate["B947_seven_reproduced"])
print("GATE  5/2 split reproduced                  :", gate["B947_5_2_split_reproduced"])
for f, s in seven.items():
    print(f"      {f:16s} lead={s['P_lead']} const={s['P_const']} mid_only={s['P_mid_only']} HOLDS={s['HOLDS']}")

# ------------------------------------------------------------------- CENSUS
# Every additional banked cubic located by scanning frontier/*/results.json.
# class:  VALUE  = intrinsically-normalised element of K (a ratio/overlap/weight)
#         PENCIL = root-locus of a determinant along a line A + t.B (free Q*-scale)
#         SPECTRAL = charpoly factor / trace-of-operator (carries the operator's scale)
CENSUS = [
    # --- VALUE-layer siblings of the seven, from the SAME defining arcs -------
    ("m_A_flipmass", "VALUE", "B928 sheet entry 2: m_A in K, the A-branch partner of m_S",
     [42467328, -56070144, 19828224, -2113201]),
    ("X_cross_overlap_sq", "VALUE", "B930/B937: cross-generation overlap^2, partner of W",
     [908209, 1049253, 253875, -15625]),
    ("u_B937", "VALUE", "B937 partA u",
     [28179280429056, -3057647616000, 53136000000, -244140625]),
    # --- VALUE-layer, normalisation-free by its own banked theorem ------------
    # T and T_row_products loaded below from B914 (coefficients are ~200 digits)
    # --- PENCIL cubics -------------------------------------------------------
    ("mu_at_B866_own_t", "PENCIL-ALT", "B866's own pencil coordinate for the SAME locus as mu",
     [500716339200, -159667200, -28224, 1]),
    # --- SPECTRAL ------------------------------------------------------------
    ("h_S_B883", "SPECTRAL", "B914: charpoly factor of Mc (monic)",
     [1, 0, -535623511707648, 2928461724187049852928]),
    ("colored_twist_trace", "SPECTRAL", "B928 colored twist trace",
     [256, -768, -828, 2859]),
    ("colored_twist_det", "SPECTRAL", "B928 colored twist det",
     [12230590464, -10239934464, 255728448, 865523177]),
    ("octet_flip_trace", "SPECTRAL", "B928 octet flip trace",
     [5308416, -45868032, 78736896, -38004841]),
    ("A_kappa_B938", "SPECTRAL", "B938 part A kappa Kummer element",
     [557339020487762273068236, 0, -215575686144, 1]),
    # --- field-canonical control --------------------------------------------
    ("K_generator_s3_12s_5", "CONTROL", "B937 monogenic generator of K",
     [1, 0, -12, -5]),
]

# B888's two further pencil cubics, rebuilt from B888's own stored factors
try:
    lam, bb = sp.symbols("lambda b")
    S1 = json.load(open(ROOT / "frontier/B888_two_fields/pencil_factors.json"))
    for mult, nm in ((1, "vacuum_weight_cubic_B888"), (8, "generic_weight_cubic_B888")):
        rec = [f for f in S1["factor_structure"] if f["mult"] == mult][0]
        F = sp.sympify(rec["factor"].replace("lambda", "lam_"), locals={"lam_": lam, "x": x})
        Fp = sp.Poly(F, x, lam)
        B = sp.expand(sum(cf * bb ** m[0] for m, cf in zip(Fp.monoms(), Fp.coeffs())
                          if m[0] + m[1] == 3))
        CENSUS.append((nm, "PENCIL", "B888 weight pencil (banked normalisation)",
                       [int(c) for c in sp.Poly(B, bb).all_coeffs()]))
except Exception as e:  # pragma: no cover
    OUT["B888_rebuild_error"] = repr(e)

rows = []
print("\nCENSUS (B947 statistic at each family's banked normalisation)")
for name, cls, prov, co in CENSUS:
    st = b947_statistic(co)
    st.update({"family": name, "class": cls, "provenance": prov, "coeffs": [int(c) for c in co]})
    rows.append(st)
    print(f"  {cls:12s} {name:26s} lead={st['P_lead']} const={st['P_const']} "
          f"mid_only={st['P_mid_only']} tot={st['total_support_size_lower_bound']} "
          f"HOLDS={st['HOLDS']} EXCL={st['EXCLUDED_vacuous']}")

# -------------------------------------------------- T and T_row_products (B914)
B914 = json.load(open(ROOT / "frontier/B914_ratio_table/results.json"))
for key, nm in (("T_single", "T_colorless_coupling_B914"),
                ("T_row_products", None)):
    rec = B914[key]
    subs = {nm: rec} if nm else {f"T_row_products[{k}]": v for k, v in rec.items()}
    for label, r in subs.items():
        co = [int(c) for c in r["minpoly_desc_coeffs"]]
        # GATE: the banked 50-digit value must be a root of the banked cubic
        val = sp.Float(r["value_50d"], 60)
        P = sum(sp.Integer(c) * val ** (3 - i) for i, c in enumerate(co))
        scale = max(abs(sp.Integer(c) * val ** (3 - i)) for i, c in enumerate(co))
        resid = float(abs(P) / scale)
        st = b947_statistic(co, big=True)
        st.update({"family": label, "class": "VALUE",
                   "provenance": "B914: normalisation-free colorless coupling invariant "
                                 "(LAW_MAP SS F, THE ONE-NUMBER TABLE)",
                   "gate_root_relative_residual": resid,
                   "coeff_digit_lengths": [len(str(abs(c))) for c in co]})
        rows.append(st)
        print(f"  {'VALUE':12s} {label:26s} lead>={st['P_lead_size_lower_bound']} "
              f"({st['P_lead']}+cof) const={st['P_const']} HOLDS={st['HOLDS']} "
              f"decidable={st['verdict_decidable']} root_resid={resid:.2e}")

OUT["census"] = rows

# ------------------------------------------------------------------- SUMMARY
allrows = ([dict(seven[f], family=f, class_="VALUE" if f not in ("mu_charge", "kappa_compact")
                 else "PENCIL") for f in seven]
           + [dict(r, class_=r["class"]) for r in rows])
val = [r for r in allrows if r["class_"] == "VALUE"]
pen = [r for r in allrows if r["class_"].startswith("PENCIL")]
summary = {
    "VALUE_n": len(val), "VALUE_holds": sum(r["HOLDS"] for r in val),
    "VALUE_fails": [r["family"] for r in val if not r["HOLDS"]],
    "PENCIL_n": len(pen), "PENCIL_holds": [r["family"] for r in pen if r["HOLDS"]],
    "criterion_can_PASS": any(r["HOLDS"] for r in allrows),
    "criterion_can_FAIL": any(not r["HOLDS"] for r in allrows),
}
OUT["summary"] = summary
print("\nSUMMARY")
print("  VALUE families:", summary["VALUE_n"], "hold:", summary["VALUE_holds"],
      "FAIL:", summary["VALUE_fails"])
print("  PENCIL families:", summary["PENCIL_n"], "that HOLD:", summary["PENCIL_holds"])
print("  MB12: can pass:", summary["criterion_can_PASS"], "/ can fail:", summary["criterion_can_FAIL"])

(HERE / "bounded_work_out.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
