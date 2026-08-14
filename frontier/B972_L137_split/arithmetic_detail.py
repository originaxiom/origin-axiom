#!/usr/bin/env python3
"""B972 / L137 -- the arithmetic shown, plus the four load-bearing checks.

  A  full prime factorisation of every census family's four coefficients
  B  is T_row_products an INDEPENDENT family, or is it T^3 ?
  C  does T lie in the same cubic field K as the seven?  (mod-p splitting types)
  D  can ANY rescaling rescue T?  (the tilt-invariant F)
"""
import itertools
import json
import pathlib

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = {}
x = sp.Symbol("x")
B914 = json.load(open(ROOT / "frontier/B914_ratio_table/results.json"))
B947 = json.load(open(ROOT / "frontier/B947_thinning_law/results.json"))


def fs(n, bound=10 ** 6):
    """Readable factorisation; trial division only for the huge ones."""
    n = int(n)
    sgn = "-" if n < 0 else ""
    n = abs(n)
    if n == 0:
        return "0"
    if n == 1:
        return sgn + "1"
    if n < 10 ** 30:
        f = sp.factorint(n)
        return sgn + "*".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(f.items()))
    f, m = {}, n
    for p in sp.primerange(2, bound):
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
        if m == 1:
            break
    s = "*".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(f.items()))
    if m > 1:
        s += f"*C{len(str(m))}" if s else f"C{len(str(m))}"
    return sgn + s


# ------------------------------------------------------------------- A
print("A. THE ARITHMETIC, SHOWN\n")
FAMS = []
for f, r in B947["families"].items():
    FAMS.append((f, "seven", [int(c) for c in r["coeffs"]]))
FAMS += [
    ("m_A_flipmass", "NEW-VALUE", [42467328, -56070144, 19828224, -2113201]),
    ("X_cross_overlap_sq", "NEW-VALUE", [908209, 1049253, 253875, -15625]),
    ("u_B937", "NEW-VALUE", [28179280429056, -3057647616000, 53136000000, -244140625]),
    ("colored_twist_trace", "NEW-SPECTRAL", [256, -768, -828, 2859]),
    ("colored_twist_det", "NEW-SPECTRAL", [12230590464, -10239934464, 255728448, 865523177]),
    ("octet_flip_trace", "NEW-SPECTRAL", [5308416, -45868032, 78736896, -38004841]),
    ("h_S_B883", "NEW-SPECTRAL", [1, 0, -535623511707648, 2928461724187049852928]),
    ("A_kappa_B938", "NEW-SPECTRAL", [557339020487762273068236, 0, -215575686144, 1]),
]
tab = []
for nm, cls, co in FAMS:
    row = {"family": nm, "class": cls, "factorisations": [fs(c) for c in co]}
    tab.append(row)
    print(f"  {nm:22s} [{cls}]")
    for lab, c in zip(("a3 (lead)", "a2", "a1", "a0 (const)"), co):
        print(f"      {lab:11s} {c:>28} = {fs(c)}")
OUT["A_factorisations"] = tab

# ------------------------------------------------------------------- B
print("\nB. IS T_row_products INDEPENDENT OF T ?\n")
Tv = sp.Float(B914["T_single"]["value_50d"], 60)
Rv = sp.Float(B914["T_row_products"]["rows"]["value_50d"], 60)
Cv = sp.Float(B914["T_row_products"]["cols"]["value_50d"], 60)
rel3 = float(abs(Rv - Tv ** 3) / abs(Rv))
OUT["B_T_row_products"] = {
    "T_50d": str(Tv), "rows_50d": str(Rv), "cols_50d": str(Cv),
    "rows_equals_cols": bool(abs(Rv - Cv) == 0),
    "rel_diff_rows_vs_T_cubed": rel3,
    "rows_IS_T_cubed": rel3 < 1e-40,
    "same_minpoly_rows_cols": B914["T_row_products"]["rows"]["minpoly_desc_coeffs"]
                              == B914["T_row_products"]["cols"]["minpoly_desc_coeffs"],
}
print(f"   rows == cols                      : {OUT['B_T_row_products']['rows_equals_cols']}")
print(f"   |rows - T^3|/|rows|               : {rel3:.3e}")
print(f"   => T_row_products IS T^3          : {OUT['B_T_row_products']['rows_IS_T_cubed']}")
print("   => it is a DEPENDENT corroboration of T, NOT an independent family.")

# ------------------------------------------------------------------- C
print("\nC. DOES T LIE IN THE SAME CUBIC FIELD K AS THE SEVEN ?\n")
K = sp.Poly(x ** 3 - 12 * x - 5, x)   # B937's monogenic model of the charge field
dK = int(K.discriminant())
OUT["C_field"] = {"K_minpoly": "x^3 - 12x - 5", "disc": dK, "disc_factored": fs(dK)}
print(f"   K = Q[s]/(s^3-12s-5),  disc = {dK} = {fs(dK)}   [re-derived here]")


def splitting_type(co, p):
    P = sp.Poly([int(c) % p for c in co], x, modulus=p)
    if P.degree() < 3:
        return None
    try:
        fac = sp.factor_list(P.as_expr(), x, modulus=p)[1]
    except Exception:
        return None
    return tuple(sorted(sp.Poly(f, x, modulus=p).degree() for f, m in fac for _ in range(m)))


TCO = [int(c) for c in B914["T_single"]["minpoly_desc_coeffs"]]
TARGETS = [("T (B914)", TCO)] + [(f, [int(c) for c in r["coeffs"]])
                                 for f, r in B947["families"].items()]
res = {}
for nm, co in TARGETS:
    bad = tested = 0
    for p in sp.primerange(5, 900):
        if int(co[0]) % p == 0 or int(co[-1]) % p == 0 or dK % p == 0:
            continue
        if int(sp.Poly(co, x).discriminant()) % p == 0:
            continue
        a, b_ = splitting_type(co, p), splitting_type([1, 0, -12, -5], p)
        if a is None or b_ is None:
            continue
        tested += 1
        bad += (a != b_)
    res[nm] = {"primes_tested": tested, "splitting_type_mismatches": bad}
    print(f"   {nm:22s} primes={tested:4d}  mismatches vs K = {bad}")
OUT["C_splitting"] = res

# ------------------------------------------------------------------- D
print("\nD. CAN ANY RESCALING RESCUE T ?  (the tilt-invariant F)\n")
G = range(-80, 81)


def loc(v, g):
    w = [v[0], v[1] + g, v[2] + 2 * g, v[3] + 3 * g]
    m = min(w)
    w = [t - m for t in w]
    return (w[0] > 0, any(t > 0 for t in w[1:3]), w[3] > 0)


def F_and_satisfiable(co, bound=10 ** 6):
    co = [sp.Integer(int(c)) for c in co]
    g0 = sp.igcd(*[abs(int(c)) for c in co if c != 0])
    co = [c // g0 for c in co]
    P = set()
    for p in sp.primerange(2, bound):
        if any(int(c) % p == 0 for c in co):
            P.add(int(p))
    P = sorted(P)
    per, forced = {}, []
    for p in P:
        v = [sp.multiplicity(p, abs(int(c))) if c != 0 else 10 ** 9 for c in co]
        st = sorted(set(loc(v, g) for g in G))
        per[p] = st
        if not any((not a) and (not c) for a, _, c in st):
            forced.append(p)
    ok = False
    for combo in itertools.product(*[per[p] for p in P]):
        lead = [p for p, s in zip(P, combo) if s[0]]
        const = [p for p, s in zip(P, combo) if s[2]]
        mo = [p for p, s in zip(P, combo) if s[1] and p not in lead and p not in const]
        if len(lead) <= 2 and len(const) <= 2 and len(mo) >= 1:
            ok = True
            break
    return len(forced), forced, ok


fT, listT, okT = F_and_satisfiable(TCO)
OUT["D_T_invariance"] = {"F_lower_bound": fT, "forced_primes_found": listT,
                         "satisfiable_by_some_rescaling": okT,
                         "note": "F counted over primes < 10^6 only; a lower bound"}
print(f"   T: F >= {fT}   forced primes (p<10^6) = {listT}")
print(f"   |P_lead|<=2 and |P_const|<=2 can hold at most 4 forced primes"
      f"  =>  F>={fT} means NO rescaling satisfies the pattern: {not okT}")

for nm, co in [(f, [int(c) for c in r["coeffs"]]) for f, r in B947["families"].items()]:
    f_, l_, o_ = F_and_satisfiable(co)
    OUT.setdefault("D_seven", {})[nm] = {"F": f_, "forced": l_, "satisfiable": o_}
    print(f"   {nm:22s} F={f_}  forced={l_}  satisfiable={o_}")

(HERE / "arithmetic_detail_out.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
