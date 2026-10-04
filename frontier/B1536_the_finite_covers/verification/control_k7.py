#!/usr/bin/env python3
"""B1536 control K7 (banked population only): Lemma G's strata, both routes, on sm:B1535 Part M's covers of m135.

At three members of m135 (kappa = 1, so nu is trivial on every cusp) on three of its finite abelian covers (two of order 2, one
of order 4 with four cusps), every stratum C_S is read in both routes at two random classes each: route N through Lemma O's
block-monomial modules (FLINT, p < 2^24), route R through the cover's own presentation and its own classes (PARI, p < 2^31).
Each stratum's readings must agree between the routes in count, k and every connecting rank, and every reading must carry its
identities.  This is the design-time test that exposed route R's overflow (PREREGISTRATION section 6), re-run on the final code.

    python3 control_k7.py [--record]   ->  k7.json"""
import json
import random
import sys
import time
import warnings
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cover_lib as CL  # noqa: E402
import gf  # noqa: E402
import route_n as N  # noqa: E402
import route_r as R  # noqa: E402
import control_k2 as K2  # noqa: E402

CASES = (((Fr(0), Fr(1, 2)), ["(0, 0; 0)", "(0, 1/2; 0)"]),
         ((Fr(0), Fr(0)), ["(0, 0; 0)", "(1/2, 1/2; 0)"]),
         ((Fr(0), Fr(1, 2)), ["(0, 0; 0)", "(0, 1/2; 0)", "(1/2, 0; 0)", "(1/2, 1/2; 0)"]))


def key(x):
    return [x["I(W)"], x["I(L2W)"], x["k"], x["rk d1"]["L2*"], x["rk d1"]["E*"], x["rk d1"]["E"], x["rk d1"]["L2"]]


def main():
    t0 = time.time()
    pN = gf.primes_1_mod(120, N.P_BOUND, 1)[0]
    pR = gf.primes_1_mod(120, 1 << 31, 1)[0]
    st = CL.state("m135")
    BN, BR = N.Base(st, gf.GF(pN, 120)), N.Base(st, gf.GF(pR, 120))
    out = {"primes": {"route N": pN, "route R": pR}, "cases": []}
    for u, H in CASES:
        perms = K2.cover_of(H, st["sign"])
        pa = N.perm_arrays(BN.G, perms)
        cus = [dict(c, trivial=True) for c in CL.cusps(BN.G, perms)]
        chiN, chiR = BN.character(u, Fr(0)), BR.character(u, Fr(0))
        cov = R.PCover(BR.G, perms)
        sN = N.strata_readings(BN, pa, chiN, cus, random.Random(1))
        sR = R.strata_readings(cov, BR.rho, chiR, pR, [True] * len(cus), random.Random(2))
        strata = []
        for (S1, r1), (S2, r2) in zip(sN, sR):
            a, b = [key(x) for x in r1], [key(x) for x in r2]
            strata.append({"S": S1, "S (R)": S2, "route N": a, "route R": b,
                           "identities": all(x["all"] for x in r1 + r2), "agree": S1 == S2 and a == b})
        rec = {"u": [str(x) for x in u], "H": H, "cusps": len(cus), "strata (N)": len(sN), "strata (R)": len(sR),
               "supplies (N)": N.supplies(BN, pa, chiN), "supplies (R)": R.supplies(cov, BR.rho, chiR, pR),
               "strata": strata}
        rec["ok"] = (len(sN) == len(sR) and rec["supplies (N)"] == rec["supplies (R)"] and
                     all(s["agree"] and s["identities"] for s in strata))
        out["cases"].append(rec)
        print(rec["u"], len(H), "cusps", len(cus), "strata", len(sN), len(sR), "ok", rec["ok"], f"{time.time() - t0:.0f}s",
              flush=True)
    out["strata read"] = sum(len(c["strata"]) for c in out["cases"])
    out["holds"] = all(c["ok"] for c in out["cases"])
    out["seconds"] = round(time.time() - t0)
    print(json.dumps({k: v for k, v in out.items() if k != "cases"}))
    if "--record" in sys.argv:
        (HERE / "k7.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    main()
