#!/usr/bin/env python3
"""B972 SCOUT -- the consolidated table.

For every family with a banked minimal polynomial that this scout could find:
  (i)   B947's sealed statistic AT THE BANKED NORMALISATION (reproduced verbatim);
  (ii)  the NORMALISATION-INVARIANT version:  does there EXIST c in Q* with
        P(t/c) primitive satisfying the pattern?  (the pencil parameter's scale
        is the only freedom a pencil cubic has; g_p may be chosen per prime);
  (iii) the per-prime Newton datum that decides (ii):  F(P) = # primes that
        cannot be pushed out of BOTH extremes by any reparameterisation.

Scouting only.  No seal.  Nothing here is banked.
"""
import itertools
import json
import pathlib

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
x, lam, b = sp.symbols("x lambda b")
G = range(-60, 61)


def support(n):
    n = abs(int(n))
    return set(int(p) for p in sp.factorint(n)) if n not in (0, 1) else set()


def prim(co):
    co = [sp.Integer(c) for c in co]
    g = sp.igcd(*[abs(int(c)) for c in co if c != 0])
    return [c // g for c in co]


def b947(co, name, cls):
    co = prim(co)
    Pl, Pc = support(co[0]), support(co[-1])
    Pm = set().union(*[support(c) for c in co[1:-1]])
    Pmo = Pm - Pl - Pc
    tot = Pl | Pc | Pm
    return {"family": name, "class": cls,
            "P_lead": sorted(Pl), "P_const": sorted(Pc), "P_mid_only": sorted(Pmo),
            "total_support_size": len(tot), "excluded_vacuous": len(tot) <= 3,
            "B947_pattern_holds_at_banked_normalisation":
                len(Pl) <= 2 and len(Pc) <= 2 and len(Pmo) >= 1}


def loc(v, g):
    w = [v[0], v[1] + g, v[2] + 2 * g, v[3] + 3 * g]
    m = min(w)
    w = [t - m for t in w]
    return (w[0] > 0, any(t > 0 for t in w[1:3]), w[3] > 0)


def invariant(co, name):
    co = prim(co)
    P = sorted(set().union(*[support(c) for c in co]))
    per, forced = {}, 0
    for p in P:
        v = [sp.multiplicity(p, abs(int(c))) if c != 0 else 10**9 for c in co]
        st = sorted(set(loc(v, g) for g in G))
        per[p] = st
        if not any((not a) and (not c) for a, _, c in st):
            forced += 1
    n_hold, ex = 0, None
    for combo in itertools.product(*[per[p] for p in P]):
        lead = [p for p, s in zip(P, combo) if s[0]]
        mid = [p for p, s in zip(P, combo) if s[1]]
        const = [p for p, s in zip(P, combo) if s[2]]
        mo = [p for p in mid if p not in lead and p not in const]
        if len(lead) <= 2 and len(const) <= 2 and len(mo) >= 1:
            n_hold += 1
            ex = ex or {"P_lead": lead, "P_mid_only": mo, "P_const": const}
    return {"F_primes_forced_into_an_extreme": forced,
            "n_normalisations_satisfying_pattern": n_hold,
            "PATTERN_SATISFIABLE_BY_SOME_NORMALISATION": n_hold > 0,
            "witness": ex}


# ------------------------------------------------------------------ families
B941 = json.load(open(ROOT / "frontier/B941_branch_symmetric/results.json"))
FAMS = []
for fam, ee in B941["symmetric_functions"].items():
    E = [sp.Rational(v) for v in ee]
    poly = sp.Poly(x**3 - E[0] * x**2 + E[1] * x - E[2], x)
    P = sp.Poly(poly.as_expr() * sp.lcm([c.q for c in poly.all_coeffs()]), x)
    cls = "PENCIL" if fam in ("mu_charge", "kappa_compact") else "VALUE"
    FAMS.append(([int(c) for c in prim(P.all_coeffs())], fam + " (B941)", cls))

# the two further PENCIL cubics (B888) -- rebuilt with B888's own bcubic()
S1 = json.load(open(ROOT / "frontier/B888_two_fields/pencil_factors.json"))
FL = [sp.sympify(f["factor"].replace("lambda", "lam_"),
                 locals={"lam_": lam, "x": x}) for f in S1["factor_structure"]]
for mult, nm in ((1, "vacuum_weight_cubic (B888)"), (8, "generic_weight_cubic (B888)")):
    F = [f for f, m in zip(FL, S1["factor_structure"]) if m["mult"] == mult][0]
    Fp = sp.Poly(F, x, lam)
    B = sp.expand(sum(cf * b**m[0] for m, cf in zip(Fp.monoms(), Fp.coeffs())
                      if m[0] + m[1] == 3))
    FAMS.append(([int(c) for c in sp.Poly(B, b).all_coeffs()], nm, "PENCIL"))

# alternate banked normalisations of the SAME two loci (the invariance probe)
FAMS.append(([500716339200, -159667200, -28224, 1], "mu @ B866's own t", "PENCIL-ALT"))
FAMS.append(([1, 0, -12, -5], "K's canonical monogenic generator s (B937)", "FIELD-CANONICAL"))

ROWS = []
for co, nm, cls in FAMS:
    r = b947(co, nm, cls)
    r.update(invariant(co, nm))
    r["coeffs"] = co
    ROWS.append(r)
    print(f"{r['class']:16s} {nm:42s} banked_holds={str(r['B947_pattern_holds_at_banked_normalisation']):5s} "
          f"F={r['F_primes_forced_into_an_extreme']} satisfiable={r['PATTERN_SATISFIABLE_BY_SOME_NORMALISATION']}")

print()
for cls in ("VALUE", "PENCIL"):
    sub = [r for r in ROWS if r["class"] == cls]
    print(f"{cls}: n={len(sub)}  banked-holds={sum(r['B947_pattern_holds_at_banked_normalisation'] for r in sub)}"
          f"  satisfiable={sum(r['PATTERN_SATISFIABLE_BY_SOME_NORMALISATION'] for r in sub)}"
          f"  F values={sorted(r['F_primes_forced_into_an_extreme'] for r in sub)}")

(HERE / "final_probe_out.json").write_text(json.dumps(ROWS, indent=1) + "\n")
