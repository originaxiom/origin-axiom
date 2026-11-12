#!/usr/bin/env python3
"""SM-R79b: the numbers of B1726's and B1753's corrected dated notes (Review 79), recomputed by this seat's own code from
B1882's committed card output (card/v1_null.json at main 896cae025): random targets only, no measured value read.
Usage (from a clone that has the commit): notes_check.py OUT.json"""
import json, subprocess, sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from fractions import Fraction
REV = "896cae025"
card = json.loads(subprocess.run(["git", "show", REV + ":frontier/B1882_the_v1_card_run_on_main/card/v1_null.json"],
                                 capture_output=True, text=True, check=True).stdout)["instruments"]
out = {"main": REV, "cells": {}}
for n in ("N1", "N2"):
    for k, c in card[n]["cells"].items():
        pops = c["all_seeds"]["populations"]
        hits = lambda depth, layer: pops[depth]["share"][layer]["hits"]
        lo = c["leave_out"]
        b = lo["best 0.1%"]["bottom layer 1"]
        exact = Fraction(b["lost"], b["n"]) / Fraction(b["rows_share"]).limit_denominator(10 ** 6)
        dec = Decimal(exact.numerator) / Decimal(exact.denominator)
        out["cells"][f"{n} {k}"] = {
            "bottom_exact": str(exact), "bottom_half_up": str(dec.quantize(Decimal("0.01"), ROUND_HALF_UP)),
            "bottom_half_even": str(dec.quantize(Decimal("0.01"), ROUND_HALF_EVEN)),
            "bottom_ratio_best_0.1%": float(exact),
            "top_ratio_best_0.1%": round(lo["best 0.1%"]["top layer 1"]["ratio_to_rows_share"], 4),
            "top_ratio_best_1%": round(lo["best 1%"]["top layer 1"]["ratio_to_rows_share"], 4),
            "top_layer_1_vs_2": {d: [hits(d, "top layer 1"), hits(d, "top layer 2")] for d in ("best 5%", "best 1%", "best 0.1%", "best 0.01%")},
            "top_layer_1_all": hits("all", "top layer 1"),
        }
C = out["cells"]
r = lambda x: float(Decimal(repr(x)).quantize(Decimal("0.01"), ROUND_HALF_UP))   # half up, as B1882's page
checks = {
 # B1726 (the first null, N1)
 "B1726 bottom end 0.06 is the seat's menu": r(C["N1 wf|seat"]["bottom_ratio_best_0.1%"]) == 0.06,
 "B1726 covariant bottom end 0.18 (half up)": C["N1 wf|cov"]["bottom_half_up"] == "0.18",
 "B1726 free bottom end 0.04 (half up, the rounding of B1882's page and lock)": C["N1 wf|free"]["bottom_half_up"] == "0.04",
 "B1726 free bottom end 0.04 (half even)": C["N1 wf|free"]["bottom_half_even"] == "0.04",
 "B1726 205,881 in the top layer, all targets, seat's menu": C["N1 wf|seat"]["top_layer_1_all"] == 205881,
 "B1726 5,925 of them in the best 5%": C["N1 wf|seat"]["top_layer_1_vs_2"]["best 5%"][0] == 5925,
 "B1726 below its neighbour at 5%, 1%, 0.1%, seat's menu": all(a < b for d, (a, b) in C["N1 wf|seat"]["top_layer_1_vs_2"].items() if d != "best 0.01%"),
 "B1726 not at 0.01%: 17 against 10": C["N1 wf|seat"]["top_layer_1_vs_2"]["best 0.01%"] == [17, 10],
 "B1726 covariant above at 0.1%: 130 against 123": C["N1 wf|cov"]["top_layer_1_vs_2"]["best 0.1%"] == [130, 123],
 "B1726 1.64 and 1.46, seat's menu": [r(C["N1 wf|seat"]["top_ratio_best_0.1%"]), r(C["N1 wf|seat"]["top_ratio_best_1%"])] == [1.64, 1.46],
 "B1726 '1.5 to 2' under the covariant and free menus": all(1.5 <= C[f"N1 wf|{m}"][f"top_ratio_best_{d}"] <= 2.0 for m in ("cov", "free") for d in ("0.1%", "1%")),
 # B1753 (the second null, N2)
 "B1753 bottom end 0.08 under the seat's menu": [r(C["N2 chi2|seat"]["bottom_ratio_best_0.1%"]), r(C["N2 wf|seat"]["bottom_ratio_best_0.1%"])] == [0.08, 0.08],
 "B1753 over the six cells 0.06 to 0.10": (min(r(v["bottom_ratio_best_0.1%"]) for k, v in C.items() if k.startswith("N2")),
                                           max(r(v["bottom_ratio_best_0.1%"]) for k, v in C.items() if k.startswith("N2"))) == (0.06, 0.10),
 "B1753 below its neighbour under every menu at 5%, 1%, 0.1%": all(a < b for k, v in C.items() if k.startswith("N2")
                                                                   for d, (a, b) in v["top_layer_1_vs_2"].items() if d != "best 0.01%"),
 "B1753 at 0.01%, seat's menu: 17 against 18 and 16 against 21": [C["N2 chi2|seat"]["top_layer_1_vs_2"]["best 0.01%"], C["N2 wf|seat"]["top_layer_1_vs_2"]["best 0.01%"]] == [[17, 18], [16, 21]],
 "B1753 at 0.01%, chi2 covariant: 16 against 15": C["N2 chi2|cov"]["top_layer_1_vs_2"]["best 0.01%"] == [16, 15],
 "B1753 1.99, 1.96 at 0.1% and 1.90, 1.89 at 1%, seat's menu": [r(C["N2 chi2|seat"]["top_ratio_best_0.1%"]), r(C["N2 wf|seat"]["top_ratio_best_0.1%"]),
                                                                 r(C["N2 chi2|seat"]["top_ratio_best_1%"]), r(C["N2 wf|seat"]["top_ratio_best_1%"])] == [1.99, 1.96, 1.90, 1.89],
 "B1753 '2.0 to 2.4' under the covariant and free menus": all(2.0 <= round(C[f"N2 {s}|{m}"][f"top_ratio_best_{d}"], 2) <= 2.4
                                                             for s in ("chi2", "wf") for m in ("cov", "free") for d in ("0.1%", "1%")),
}
out["checks"] = checks
json.dump(out, open(sys.argv[1], "w"), indent=1)
print(json.dumps(checks, indent=1))
for k, v in C.items():
    print(k, v["bottom_ratio_best_0.1%"], v["top_ratio_best_0.1%"], v["top_ratio_best_1%"], v["top_layer_1_vs_2"])
