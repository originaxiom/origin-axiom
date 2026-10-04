#!/usr/bin/env python3
"""B1535: Theorem C's prediction for sm:B1532 (committed at 5c6a4225, before sm:B1532's read-out), checked on sm:B1532's terms.

Run after sm:B1532's read_out.py --record.  For every term of both routes (terms_T.jsonl, terms_L.jsonl), at every class read
(the one class; c_int, the generic class and every special class at two-class members):
  - the Lambda^2 cap: -n(nu^-3 chi (x) rho) <= I(Lambda^2 W1 (x) chi) <= 0, with n = h^1 - 1 from sm:B1515's banked h^1 at the
    lambda = 1 character nu^-3 chi (r1 = 1 there: the character is unitary and trivial on the cusp);
  - the W bound: I(W1 (x) chi) >= -[chi = nu^4] (n(L) = 0 by Lemma W on a once-punctured-torus bundle).
And the counts: at most one generation in either order (read_out.json's census: no N values).  Writes check_b1532.json."""
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1532V = ROOT / "frontier" / "B1532_three_from_the_cusps" / "verification"


def lab_pair(lab):
    a, b = lab.split(",")
    return Fraction(a), Fraction(b)


def lab_str(pr):
    return ",".join(str(x % 1) for x in pr)


def banked_h1():
    """sm:B1515's banked h^1(psi (x) rho) at every lambda = 1 character, by label, at each level's first prime (own loader)"""
    rec = json.loads((ROOT / "frontier/B1515_the_hyperbolic_point/verification/census_t_run.txt").read_text(encoding="utf-8"))
    out = defaultdict(dict)
    for r in rec["A"]:
        first = rec["primes"]["M%d" % r["level"]][0]
        if r["lam"] == "1" and r["field"] == f"GF({first})":
            out[r["level"]][",".join(r["char"])] = r["row"]["h1"]["V"]
    return out


def readings(r):
    if r["kind"] == "one":
        return [("c", r["c"])]
    return [("int", r["int"]), ("gen", r["gen"][1])] + [("special", t) for pt, f, t in r["special"]]


def main():
    h1 = banked_h1()
    out = {"routes": {}, "violations": []}
    for route in ("T", "L"):
        cnt = Counter()
        lam_vals = defaultdict(Counter)
        w_vals = Counter()
        n_terms = 0
        with open(B1532V / f"terms_{route}.jsonl") as f:
            for line in f:
                r = json.loads(line)
                if "done" in r or "kind" not in r:
                    continue
                n, nu, chi = int(r["n"]), r["nu"], r["chi"]
                a, b = lab_pair(nu)
                c, d = lab_pair(chi)
                q = lab_str((-3 * a + c, -3 * b + d))                 # nu^-3 chi
                nQ = h1[n][q] - 1
                nu4 = lab_str((4 * a, 4 * b)) == lab_str((c, d))
                for cname, t in readings(r):
                    n_terms += 1
                    w, l = t[0][0], t[1][0]
                    lam_vals[n][l] += 1
                    w_vals[w] += 1
                    ok_l = -nQ <= l <= 0
                    ok_w = w >= -(1 if nu4 else 0)
                    cnt["Lambda^2 cap holds" if ok_l else "Lambda^2 cap FAILS"] += 1
                    cnt["W bound holds" if ok_w else "W bound FAILS"] += 1
                    if l != 0:
                        cnt[f"non-zero Lambda^2 on M{n} at n(nu^-3 chi rho) = {nQ}"] += 1
                    if not (ok_l and ok_w):
                        out["violations"].append({"route": route, "n": n, "nu": nu, "chi": chi, "class": cname, "T": [w, l],
                                                  "n(nu^-3 chi rho)": nQ, "chi = nu^4": nu4})
        out["routes"][route] = {"terms": n_terms, "counts": dict(cnt), "Lambda^2 values by level":
                                {f"M{k}": dict(v) for k, v in sorted(lam_vals.items())}, "W values": dict(w_vals)}
    ro = json.loads((B1532V / "read_out.json").read_text())
    out["read_out census"] = {k: {x: v for x, v in ro["census"][k].items() if x != "degree law (S = |B| T(nu, 1, c))"} for k in ("T", "L")}
    out["holds"] = not out["violations"]
    (HERE / "check_b1532.json").write_text(json.dumps(out, indent=1))
    print(json.dumps({k: v for k, v in out.items() if k != "violations"}, indent=1))
    print("violations:", len(out["violations"]), out["violations"][:5])
    print("THEOREM C's PREDICTION FOR sm:B1532 HOLDS" if out["holds"] else "THEOREM C's PREDICTION FAILS")


if __name__ == "__main__":
    main()
