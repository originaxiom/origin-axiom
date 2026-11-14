#!/usr/bin/env python3
"""SM-C9: SM-C7's Z(0, chi_c) against Bohn's U(1) rho invariant of the closed torus bundle T^2_M (card
relays/cards/SM_C9_the-L-value-as-a-rho-invariant.md, pushed before this run).  Exact rationals for rho; SM-C7's Z(0)
read as committed (relays/sm_c7/population.json).  Data-free.
    python3 run_c9.py [out.json]"""
import sys, json, math, random, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
POP = HERE.parent / "sm_c7" / "population.json"


def frac(x): return x - math.floor(x)
def P1(x): return Fr(0) if x.denominator == 1 else x - math.floor(x) - Fr(1, 2)
def P2(x): f = x - math.floor(x); return f * f - f + Fr(1, 6)
def sgn(x): return (x > 0) - (x < 0)
def delta(x): return 0 if Fr(x).denominator == 1 else 1


def dedekind(a, c):
    return sum(P1(Fr(a * k, c)) * P1(Fr(k, c)) for k in range(1, abs(c)))


def s_nu(a, c, n1, n2):
    return sum(P1((k + n1) / c) * P1(a * (k + n1) / c + n2) for k in range(abs(c)))


def rho_467(M, nu):
    (a, b), (c, d) = M; n1, n2 = nu
    return Fr(2 * (a + d), c) * (P2(n1) - Fr(1, 6)) - 4 * sgn(c) * (s_nu(a, c, n1, n2) - dedekind(a, c)) + sgn(c * (a + d))


def m_of(M, nu):
    (a, b), (c, d) = M; n1, n2 = nu
    return (n1 - (a * n1 + c * n2), n2 - (b * n1 + d * n2))           # (Id - M^t) nu


def rho_4420(M, nu, reading):
    """Theorem 4.4.20 expanded; nu1 in [0, 1).  Readings of the bracket: R1 as printed; R2 with sgn(c) on the sum;
    R3 with the sum to r in place of |c| - r"""
    (a, b), (c, d) = M; n1, n2 = nu; m1, m2 = m_of(M, nu)
    m1 = int(m1); r = m1 % abs(c)
    top = abs(c) - r if reading in ("R1", "R2") else r
    S = sum(P1(Fr(d * k, c)) for k in range(1, top + 1))
    lead = Fr(2 * (a + d) - 4, c) * (P2(n1) - Fr(1, 6))
    sfac = sgn(c) if reading == "R2" else 1
    return (lead - 4 * sfac * S + sgn(c * (a + d)) - sgn(c) * delta(n1) * (1 - delta(Fr(m1, c)))
            - 2 * P1(Fr(d * m1, c)) - 2 * delta(n1) * (P1(Fr(m1, c)) - P1(Fr(d * m1, c))))


def eta_untw(M):
    (a, b), (c, d) = M
    return Fr(a + d, 3 * c) - 4 * sgn(c) * dedekind(a, c) - sgn(c * (a + d))


def affine(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    if sxx < 1e-24: return None, None, None
    lam = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx; mu = my - lam * mx
    return lam, mu, max(abs(y - (lam * x + mu)) for x, y in zip(xs, ys))


def main():
    out_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "c9_results.json"
    pop = json.load(open(POP)); rows = []; bad_hyp = []
    for o in pop:
        M = o["M"]; N = o["N"]; nu = (Fr((-o["i"]) % N, N), Fr((-o["j"]) % N, N))
        m = m_of(M, nu)
        if any(x.denominator != 1 for x in m): bad_hyp.append([o["level"], o["i"], o["j"]]); continue
        (a, b), (c, d) = M
        Minv = [[d, -b], [-c, a]]
        r = rho_467(M, nu); rinv = rho_467(Minv, nu)
        D = (a + d) ** 2 - 4
        rows.append({"level": o["level"], "N": N, "i": o["i"], "j": o["j"], "M": M, "rho": str(r), "rho_f": float(r),
                     "x": math.sqrt(D) * o["Z0"][0], "Z0": o["Z0"][0],
                     "T1": {R: rho_4420(M, nu, R) == r for R in ("R1", "R2", "R3")},
                     "T2": ((r - 2 * (nu[1] * m[0] - nu[0] * m[1])) % 1) == 0,
                     "T3": rinv == -r, "rho_inv_f": float(rinv), "eta_untw": str(eta_untw(M))})
    T1 = {R: sum(r["T1"][R] for r in rows) for R in ("R1", "R2", "R3")}
    T = {"hypothesis_fails": len(bad_hyp), "T1_by_reading": T1, "T1_agreeing_reading": [R for R, v in T1.items() if v == len(rows)],
         "T2": sum(r["T2"] for r in rows), "T3": sum(r["T3"] for r in rows), "n": len(rows)}
    stop = not (T["T1_agreeing_reading"] and T["T2"] == len(rows) and T["T3"] == len(rows))
    res = {"transcription": T, "hypothesis_fails": bad_hyp[:20], "stopped": stop, "levels": {}}
    if not stop:
        lev = {}
        for r in rows: lev.setdefault(json.dumps(r["level"]), []).append(r)
        rnd = random.Random(20261114)
        for k, L in lev.items():
            xs = [r["x"] for r in L]; ys = [r["rho_f"] for r in L]
            distinct = len({round(x, 9) for x in xs})
            lam, mu, resid = affine(xs, ys)
            row = {"characters": len(L), "distinct_Z0": distinct, "slope": lam, "intercept": mu, "max_resid": resid,
                   "slope_rational": str(Fr(lam).limit_denominator(1000)) if lam is not None else None,
                   "eta_untw": L[0]["eta_untw"], "M": L[0]["M"]}
            if lam is not None:
                # P1: the flipped orientation with the unflipped fit
                row["P1_resid_flipped"] = max((abs(r["rho_inv_f"] - (lam * r["x"] + mu)) for r in L if r["rho_f"] != 0), default=0.0)
                # P2: Z0 permuted among the level's distinct values (a cyclic shift of the sorted distinct values)
                dv = sorted({round(x, 9) for x in xs}); shift = {v: dv[(t + 1) % len(dv)] for t, v in enumerate(dv)}
                xp = [shift[round(x, 9)] for x in xs]
                row["P2_resid_permuted"] = affine(xp, ys)[2] if distinct >= 3 else None
                eta = float(Fr(L[0]["eta_untw"]))
                row["intercept_over_eta"] = (mu / eta) if abs(eta) > 1e-12 else None
            res["levels"][k] = row
        used = {k: v for k, v in res["levels"].items() if v["distinct_Z0"] >= 3}
        slopes = [v["slope"] for v in used.values()]
        res["summary"] = {
            "levels": len(res["levels"]), "levels_with_3_distinct": len(used),
            "X1_exact_affine_on": [sum(v["max_resid"] <= 1e-9 for v in used.values()), len(used)],
            "X2_one_slope": (max(slopes) - min(slopes) <= 1e-9) if slopes else None,
            "slopes": sorted({v["slope_rational"] for v in used.values()}),
            "X3_intercept_over_eta": sorted({round(v["intercept_over_eta"], 9) for v in used.values() if v["intercept_over_eta"] is not None}),
            "P1_fails_on": [sum(v["P1_resid_flipped"] > 1e-6 for v in used.values()), len(used)],
            "P2_fails_on": [sum((v["P2_resid_permuted"] or 0) > 1e-6 for v in used.values()), len(used)]}
        s = res["summary"]
        s["outcome"] = ("A" if s["X1_exact_affine_on"][0] == s["X1_exact_affine_on"][1] and s["X2_one_slope"] else
                        "B" if s["X1_exact_affine_on"][0] == s["X1_exact_affine_on"][1] else "C")
    res["rows"] = [{k: v for k, v in r.items() if k not in ("T1",)} for r in rows]
    json.dump(res, open(out_path, "w"), indent=1, default=str)
    print(json.dumps({"transcription": T, "stopped": stop, "summary": res.get("summary")}, indent=1, default=str))


if __name__ == "__main__":
    main()
