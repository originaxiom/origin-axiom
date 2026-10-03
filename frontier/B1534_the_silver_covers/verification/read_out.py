#!/usr/bin/env python3
"""B1534 read-out: the sealed predictions (PREREGISTRATION section 7) read from terms.json.  Written and committed with the
PREREGISTRATION before run_terms.py read any outcome.  Writes read_out.json and prints it.

P1  Corollary I' at m135's interior class: every term with nu chi simple is (0, 0), and every cover's count there lies in
    {(-1, -1), (0, -1), (-1, -2), (0, -2)}.
P2  the term at chi = (1/2, 1/2) at m135's interior class is (0, 0), so every abelian cover counts (-1, -1) there.
P3  Proposition H': the pencils of m135's two-class members have special points only at chi with nu chi or nu^-3 chi
    non-simple, i.e. chi in {1, (1/2, 1/2)} (in turns of t': 0).
P4  THE QUESTION: no finite abelian cover of m135 or m136 carries three generations at a pulled-back member of sm:B1515's
    frame, in either order: no (state, member, class, subgroup H) with count (a, a), |a| = 3.
P5  every twisted Lambda^2 term at a simple twist nu chi (chi != 1) at a boundary-type class is 0.
P6  every generation-shaped count that occurs has |a| = 1.
P7  the routes agree: E and N on every term and every special point; route C on every cover it reads.
P8  conjugation (Lemma D's input): T(nu-bar, chi-bar, c-bar) = T(nu, chi, c) on m135's members of order 4, as multisets of
    terms per class kind.
Reads terms.json and route_c.json (run_route_c.py runs first).
The verdict rule (section 9): WITHHELD if P7 fails (ERROR_LEDGER first); else NEGATIVE if P4 holds (no three on any
abelian cover of the silver squares at a pulled-back member); else PROVED (three found, both routes)."""
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent

NONSIMPLE_M135 = {("0", "1/2"), ("1/2", "0")}


def chi_parts(ck):
    """'(w0, w1; k)' -> ((w0, w1), k)"""
    inner = ck.strip("()")
    w, k = inner.split(";")
    w0, w1 = (x.strip() for x in w.split(","))
    return (Fraction(w0), Fraction(w1)), Fraction(k.strip())


def add_u(u, w):
    return (str((Fraction(u[0]) + w[0]) % 1), str((Fraction(u[1]) + w[1]) % 1))


def main():
    T = json.loads((HERE / "terms.json").read_text())
    st135, st136 = T["states"]["-LLRR"], T["states"]["+LLRR"]
    preds = {}
    # P1, P2: m135's interior classes
    p1 = p2 = True
    for m in st135["members"]:
        if tuple(m["u"]) not in NONSIMPLE_M135:
            continue
        terms = m["terms"]["c_int"]
        for ck, t in terms.items():
            w, k = chi_parts(ck)
            nu_chi = add_u(m["u"], w)
            simple = nu_chi not in NONSIMPLE_M135
            if simple and ck != "(0, 0; 0)":
                p1 &= tuple(t) == (0, 0)
            if (w, k) == ((Fraction(1, 2), Fraction(1, 2)), Fraction(0)):
                p2 &= tuple(t) == (0, 0)
        allowed = {(-1, -1), (0, -1), (-1, -2), (0, -2)}
        p1 &= all(tuple(r["count"]) in allowed for r in m["counts"]["c_int"])
    preds["P1"], preds["P2"] = p1, p2
    # P3: special points only at chi in {1, (1/2, 1/2)}
    p3 = True
    for m in st135["members"]:
        for key, pen in m["pencils"].items():
            ck = key.split(") ")[0] + ")"
            w, k = chi_parts(ck)
            if pen["special (E)"] and not ((w == (Fraction(0), Fraction(0)) or w == (Fraction(1, 2), Fraction(1, 2)))
                                           and k == 0):
                p3 = False
    preds["P3"] = p3
    # P4, P6: the counts
    three, shapes = [], Counter()
    for state, st in T["states"].items():
        for m in st["members"]:
            for cname, rows in m["counts"].items():
                for r in rows:
                    a, b = r["count"]
                    if a == b != 0:
                        shapes[abs(a)] += 1
                        if abs(a) == 3:
                            three.append([state, m["u"], m["kappa"], cname, r["H"], r["count"]])
    preds["P4"] = not three
    preds["P6"] = set(shapes) <= {1}
    # P5: simple Lambda^2 terms at boundary-type classes
    p5 = True
    for state, st in T["states"].items():
        for m in st["members"]:
            for cname, terms in m["terms"].items():
                if cname == "c_int" or (cname == "the class" and m["n"] == 1):
                    continue
                for ck, t in terms.items():
                    if ck == "(0, 0; 0)":
                        continue
                    w, k = chi_parts(ck)
                    if k != 0:
                        continue
                    nu_chi = add_u(m["u"], w)
                    simple = (state == "+LLRR" and m["kappa"] == "0") or (state == "-LLRR" and nu_chi not in NONSIMPLE_M135)
                    if simple:
                        p5 &= t[1] == 0
    preds["P5"] = p5
    # P7: the routes
    rc = json.loads((HERE / "route_c.json").read_text())
    preds["P7"] = all(m["agree"] for st in T["states"].values() for m in st["members"]) and rc["agree"]
    # P8: conjugation on m135's order-4 members
    p8 = True
    by_u = {tuple(m["u"]): m for m in st135["members"]}
    for u, m in by_u.items():
        ubar = (str((-Fraction(u[0])) % 1), str((-Fraction(u[1])) % 1))
        if ubar == u or ubar not in by_u:
            continue
        mb = by_u[ubar]
        for cname in m["terms"]:
            if cname not in mb["terms"]:
                continue
            p8 &= Counter(tuple(t) for t in m["terms"][cname].values()) == Counter(tuple(t) for t in
                                                                                 mb["terms"][cname].values())
    preds["P8"] = p8
    if not preds["P7"]:
        verdict = "WITHHELD: the routes disagree (ERROR_LEDGER first)"
    elif preds["P4"]:
        verdict = ("NEGATIVE: no finite abelian cover of m135 or m136 carries three generations at a pulled-back member of "
                   "sm:B1515's frame, in either order")
    else:
        verdict = "PROVED: three generations on an abelian cover of a silver square (both routes)"
    res = {"predictions": preds, "verdict": verdict, "three": three,
           "generation-shaped counts by |a|": {str(k): v for k, v in sorted(shapes.items())},
           "per member": [{"state": s, "u": m["u"], "kappa": m["kappa"], "classes": list(m["terms"]),
                           "generation-shaped counts": m["generation-shaped counts"]}
                          for s, st in T["states"].items() for m in st["members"]]}
    (HERE / "read_out.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps(res, indent=1, default=str))


if __name__ == "__main__":
    main()
