#!/usr/bin/env python3
"""SM-C9, post hoc and labelled, written after the sealed run (outcome C) was committed.  Atiyah's identity pairs the
eta invariant with the Shimizu L-value, the sign-twisted ('odd') L-function; by the functional equation its value at 0
is carried by SM-C7's step-2 rational L_odd(1)/4pi^2 (relays/sm_c7/sm_c7_results.json, step2.c_odd), not by Z(0).
Here: rho_A (Bohn's (4.67), as in run_c9.py) against L_odd(1)/4pi^2, exactly, per level and across levels.
    python3 posthoc_c9_lodd.py [out.json]"""
import sys, json, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_c9 as C


def exact_affine(pairs):
    """is y = lam x + mu exactly on all pairs (Fractions)?  returns (lam, mu) or None"""
    xs = sorted({x for x, _ in pairs})
    if len(xs) < 2:
        ys = {y for _, y in pairs}
        return ("const", next(iter(ys))) if len(ys) == 1 else None
    (x0, y0) = next(p for p in pairs if p[0] == xs[0]); (x1, y1) = next(p for p in pairs if p[0] == xs[-1])
    lam = (y1 - y0) / (x1 - x0); mu = y0 - lam * x0
    return (lam, mu) if all(y == lam * x + mu for x, y in pairs) else None


def main():
    s7 = json.load(open(HERE.parent / "sm_c7" / "sm_c7_results.json"))
    pop = {(json.dumps(o["level"]), o["i"], o["j"]): o for o in json.load(open(HERE.parent / "sm_c7" / "population.json"))}
    lev = {}
    for r in s7["rows"]:
        key = (json.dumps(r["level"]), r["i"], r["j"]); o = pop[key]
        q = r["step2"]["c_odd"]["Lodd1/4pi2"]; L = Fr(q[0], q[1])
        N = o["N"]; nu = (Fr((-o["i"]) % N, N), Fr((-o["j"]) % N, N))
        rho = C.rho_467(o["M"], nu)
        lev.setdefault(key[0], []).append((L, rho, (o["i"], o["j"])))
    out = {}
    for k, P in lev.items():
        fit = exact_affine([(x, y) for x, y, _ in P])
        fit_neg = None
        out[k] = {"characters": len(P), "distinct_Lodd": len({x for x, _, _ in P}), "distinct_rho": len({y for _, y, _ in P}),
                  "exact_affine": None if fit is None else [str(fit[0]), str(fit[1])],
                  "sample": [[str(x), str(y)] for x, y, _ in P[:4]]}
    used = {k: v for k, v in out.items() if v["distinct_Lodd"] >= 3}
    slopes = sorted({v["exact_affine"][0] for v in used.values() if v["exact_affine"]})
    summ = {"levels": len(out), "levels_with_3_distinct": len(used),
            "exact_affine_on": [sum(v["exact_affine"] is not None for v in used.values()), len(used)], "slopes": slopes}
    json.dump({"summary": summ, "levels": out}, open(sys.argv[1] if len(sys.argv) > 1 else HERE / "c9_posthoc_lodd.json", "w"), indent=1)
    print(json.dumps(summ, indent=1)); print(json.dumps(out, indent=1)[:3000])


if __name__ == "__main__":
    main()
