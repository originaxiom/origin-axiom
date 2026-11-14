#!/usr/bin/env python3
"""SM-C12 T1 (W5, SM-C9b): eta_A(T^2_M) = -L_odd(1, chi_c)/pi^2 on 13 fresh levels (card
relays/cards/SM_C12_the-principle-note-tested.md, pushed before this run).  M by main's abel_M (B1737, imported from a
checkout of main, first argument); eta_A by SM-C9's exact Bohn (4.67) plus Bohn (7); L_odd(1)/4pi^2 by SM-C7's period of
the v-twisted weight-2 series along the geodesic, recognised as a rational with denominator <= 24 N^2; second computation
by SM-C7's cone sum (sm_c7_lib.L_odd1) on the first five characters of each level.  Plants P1-P3 as the card.
    python3 t1_w5.py MAIN_CHECKOUT [out.json]"""
import sys, json, math, time, pathlib, importlib.util
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(HERE.parent / "sm_c7")); sys.path.insert(0, str(HERE.parent / "sm_c9"))
import sm_c7_lib as L
import run_c7 as R7
import run_c9 as C9
spec = importlib.util.spec_from_file_location("b1737", MAIN / "frontier/B1737_the_slope_is_a_zeta_value/verification/the_slope_is_a_zeta_value.py")
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
SL = B._sl()
FRESH = [("+LR", 6), ("-LR", 5), ("+LLR", 2), ("+LLR", 4), ("-LLR", 4), ("+LLLR", 2), ("+LLRLR", 1), ("+LLRR", 1),
         ("+LLLLR", 1), ("+LLLRR", 1), ("-LLLRR", 1), ("+LLRLRR", 1), ("-LLRRLR", 1)]
CAP = 600


def exponent(M):
    (a, b), (c, d) = M
    det = abs((a - 1) * (d - 1) - b * c); g = math.gcd(math.gcd(a - 1, b), math.gcd(c, d - 1))
    return det // g if det else 0


def lodd_rat(geo, c, N):
    P = R7.period(geo, c, "v"); x = P.real / (4 * math.pi ** 2)
    q = Fr(x).limit_denominator(24 * N * N)
    return q, abs(x - float(q)), abs(P.imag)


def main():
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "t1_results.json"
    used = {tuple(l) for l in B.LEVELS}
    assert not any(f in used for f in FRESH), "a fresh level is in SM-C7's population"
    res = {"levels": {}, "rows": []}; t0 = time.time()
    for st, k in FRESH:
        eps = 1 if st[0] == "+" else -1; word = st[1:]
        M = [[int(x) for x in r] for r in B.abel_M(SL, eps, word, k)]
        N = exponent(M)
        chars = [(i, j) for i in range(N) for j in range(N) if (i, j) != (0, 0) and R7.fixed(M, i, j, N)]
        lev = {"M": M, "N": N, "characters": len(chars)}
        if len(chars) > CAP:
            lev["skipped"] = "over %d characters" % CAP; res["levels"][st + " %d" % k] = lev; continue
        geo = L.Geodesic(M); (a, b), (c_, d) = M; Minv = [[d, -b], [-c_, a]]
        eta = C9.eta_untw(M); eta_inv = C9.eta_untw(Minv)
        ok = p1 = p2 = p3 = nz = 0; maxres = 0.0; second = []
        for n_, (i, j) in enumerate(chars):
            nu = (Fr((-i) % N, N), Fr((-j) % N, N))
            etaA = C9.rho_467(M, nu) + eta
            c = (Fr(i, N), Fr(j, N)); q, resid, im = lodd_rat(geo, c, N); maxres = max(maxres, resid)
            hold = etaA == -4 * q; ok += hold; nz += q != 0
            p1 += (C9.rho_467(Minv, nu) + eta_inv) != -4 * q and q != 0
            p2 += (etaA - eta) != -4 * q and eta != 0
            Jc = (-c[1], c[0]); qJ, _, _ = lodd_rat(geo, Jc, N); p3 += etaA != -4 * qJ
            if n_ < 5:
                # DEVIATION (disclosed): the cone sum runs over M^2 when tr < 0; past |tr| = 60 it takes hours per character,
                # so there the second computation is the period at 96 nodes in place of 48 (weaker: a convergence check)
                if geo.tr > 0 or abs(geo.tr) <= 60:
                    cone = L.L_odd1(geo, i, j, N); val = cone.real / (4 * math.pi ** 2); how = "cone sum"
                else:
                    P96 = R7.period(geo, c, "v", n=96); val = P96.real / (4 * math.pi ** 2); how = "period at 96 nodes"
                second.append({"i": i, "j": j, "period_q": str(q), "second/4pi2": val, "how": how,
                               "agree": abs(val - float(q)) < 1e-6})
            res["rows"].append({"level": [st, k], "i": i, "j": j, "eta_A": str(etaA), "Lodd1/4pi2": str(q), "holds": hold, "resid": resid})
        lev.update({"holds": ok, "nonzero_L": nz, "max_rational_resid": maxres, "P1_fails": p1, "P2_fails": p2, "P3_fails": p3,
                    "eta_untw": str(eta), "second_computation": second, "seconds": round(time.time() - t0, 1)})
        res["levels"][st + " %d" % k] = lev
        print(st, k, "N", N, "chars", len(chars), "holds", ok, "P1", p1, "P2", p2, "P3", p3, "second", all(s["agree"] for s in second), round(time.time() - t0, 1), "s", flush=True)
    run = [v for v in res["levels"].values() if "holds" in v]
    res["summary"] = {"levels_run": len(run), "levels_skipped": [k for k, v in res["levels"].items() if "skipped" in v],
                      "characters": sum(v["characters"] for v in run), "holds_on": sum(v["holds"] for v in run),
                      "identity_on_every_fresh_character": all(v["holds"] == v["characters"] for v in run),
                      "max_rational_resid": max(v["max_rational_resid"] for v in run),
                      "second_computation_agrees": all(s["agree"] for v in run for s in v["second_computation"]),
                      "plants": {"P1": sum(v["P1_fails"] for v in run), "P2": sum(v["P2_fails"] for v in run), "P3": sum(v["P3_fails"] for v in run)}}
    json.dump(res, open(out_path, "w"), indent=1, default=str)
    print(json.dumps(res["summary"], indent=1))


if __name__ == "__main__":
    main()
