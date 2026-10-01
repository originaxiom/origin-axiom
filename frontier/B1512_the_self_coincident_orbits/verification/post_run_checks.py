"""B1512 post-run checks (written and run after census_run.txt; not predictions, not sealed). Record: post_run_checks_run.txt.

(a) The closed forms in w = q + 1/q.  M5's one polynomial is palindromic, so P(q, s) = s^4 + c1 (s^3 + s) + c2 s^2 + 1 with c1, c2
    polynomials in w.  Each real exceptional polynomial at lam = +-1 (and gcd(Re, Im) at lam = +-i) is invariant under q -> 1/q (Lemma D
    with real coefficients), so it is q^d g(w) with g of degree d.  Its positive roots q != 1 are the real roots w > 2 of g.
(b) The firing points of the whole tower (levels 1-6), exactly, by their w-polynomials, and every coincidence between two families
    (the gcd of their w-polynomials).  The families:
    - the pullback (Theorem D, every level);
    - s961's triplet (B1511, levels 3 and 6);
    - M4's case (b) (B1511);
    - M5's and M6's case (b) (this run).
(c) M5's double point at w = 7 (lam = 1): every basis class and c1 + c2, for W1 and W2, from the record.
(d) The number of firing backgrounds per real q on M5 and M6: the members of every class, at every lam, at that q."""
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
q, s, w = sp.symbols("q s w")


def in_w(expr):
    """a Laurent polynomial in q invariant under q -> 1/q, rewritten as a polynomial in w = q + 1/q (exact)"""
    e = sp.expand(expr)
    P = sp.Poly(sp.expand(e * q ** 40), q)
    lo = min(m[0] for m in P.monoms()) - 40
    hi = max(m[0] for m in P.monoms()) - 40
    assert lo == -hi, ("not symmetric", lo, hi)
    out = 0
    rest = e
    for k in range(hi, 0, -1):
        c = sp.Poly(sp.expand(rest * q ** 40), q).coeff_monomial(q ** (k + 40))
        out += c * w ** k
        rest = sp.expand(rest - c * sp.expand((q + 1 / q) ** k))
    out += rest
    assert sp.simplify(sp.expand(out.subs(w, q + 1 / q)) - e) == 0
    return sp.expand(out)


def check_a(rec):
    out = {}
    for lv in ("level_5", "level_6"):
        rows = []
        for c in rec["B"][lv]["classes"]:
            P = sp.sympify(c["P(q,s)"], locals={"q": q, "s": s})
            cs = sp.Poly(sp.expand(P), s)
            row = {"class": c["class_orbits"]}
            if lv == "level_5":
                c1 = sp.expand(cs.coeff_monomial(s ** 3))
                row["c1 = c3 (in w)"] = str(sp.factor(in_w(c1)))
                row["c2 (in w)"] = str(sp.factor(in_w(cs.coeff_monomial(s ** 2))))
            for lam, name in [(1, "1"), (-1, "-1")]:
                f = sp.expand(P.subs(s, lam))
                row[f"P(q, {name}) in w"] = str(sp.factor(in_w(f)))
            if lv == "level_5":
                row["P(q, i) in w"] = str(sp.factor(in_w(sp.expand(P.subs(s, sp.I)))))
            rows.append(row)
        out[lv] = rows
    return out


def check_b(rec):
    fam = {}
    fam["pullback, every level (Theorem D), lam = (-1)^n"] = w - 34
    fam["s961 triplet (B1511), lam3 = -1; M6 lam6 = 1"] = sp.expand(w ** 3 - 3 * w - 34)
    fam["M4 case (b) (B1511), lam = 1"] = w - 7
    for x in rec["D"]:
        g = sp.Poly(sp.sympify(x["factor"], locals={"q": q}), q)
        gw = sp.factor(in_w(sp.expand(g.as_expr() / q ** (g.degree() // 2))))
        key = f"M{x['level']} case (b) class {x['class_orbits']}, lam = {x['lam']}"
        fam[key] = sp.expand(sp.Poly(gw, w).monic().as_expr())
    out = {"families (w-polynomials, monic)": {k: str(sp.factor(v)) for k, v in fam.items()}, "coincidences": []}
    keys = list(fam)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            g = sp.gcd(sp.Poly(fam[keys[i]], w), sp.Poly(fam[keys[j]], w))
            if g.degree() > 0:
                roots = [r for r in sp.real_roots(g) if r > 2]
                out["coincidences"].append({"a": keys[i], "b": keys[j], "common w-factor": str(g.as_expr()),
                                            "real w > 2": [str(sp.N(r, 12)) for r in roots]})
    return out


def check_c(rec):
    out = []
    for x in rec["D"]:
        if x["level"] == 5 and x["lam"] == "1":
            classes_w1 = sorted({k for m in x["mod_p"] for rr in m["rows"].values() for k in rr["counts"]["W1"]})
            classes_w2 = sorted({k for m in x["mod_p"] for rr in m["rows"].values() for k in rr["counts"]["W2"]})
            vals = sorted({(k, v["I"]) for m in x["mod_p"] for rr in m["rows"].values() for k, v in rr["counts"]["W1"].items()})
            vals2 = sorted({(k, v["I"]) for m in x["mod_p"] for rr in m["rows"].values() for k, v in rr["counts"]["W2"].items()})
            out.append({"class": x["class_orbits"], "W1 classes tried": classes_w1, "W2 classes tried": classes_w2,
                        "W1 (class, I)": vals, "W2 (class, I)": vals2, "h1 (L, V, V_eta, V_eta*)": x["h1 (L, V_nu, V_eta, V_eta*) values"]})
    return out


def check_d(rec):
    from collections import defaultdict
    per_q = defaultdict(list)
    for x in rec["D"]:
        nmem = x["members"]
        for r in x["positive_roots"]:
            if any(v != 0 for v in x["W1 values"]):
                per_q[(x["level"], r)].append({"class": x["class_orbits"], "lam": x["lam"], "members": nmem})
    out = []
    for (lvl, r), rows in sorted(per_q.items(), key=lambda t: (t[0][0], float(t[0][1]))):
        out.append({"level": lvl, "q": r, "families": rows, "backgrounds counting +1": sum(x["members"] for x in rows)})
    return out


def main():
    rec = json.loads((HERE / "census_run.txt").read_text(encoding="utf-8"))
    return {"a_closed_forms_in_w": check_a(rec), "b_coincidences_across_the_tower": check_b(rec),
            "c_M5_double_point_classes": check_c(rec), "d_backgrounds_per_q": check_d(rec)}


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    print(txt[:6000])
    if "--record" in sys.argv:
        (HERE / "post_run_checks_run.txt").write_text(txt + "\n", encoding="utf-8")
