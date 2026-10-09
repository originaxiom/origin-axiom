#!/usr/bin/env python3
"""B1628 -- THE DATA AND THE WEAVE'S TWO TRIMAXIMAL RELATIONS.  In the frame where all of the weave's group is flavour
(B1620, corrected by B1625 with the SM seat's W43), the leptons' mixing reduces to two parameters as TM1 under T-bar(x)T
and as TM2 under T(x)T (and not at all under Sym^2 T).  The two relations predict different solar angles from the
measured reactor angle:
    TM1 (first column 2/3, 1/6, 1/6):   cos^2(t12) cos^2(t13) = 2/3   ->  sin^2 t12 = 1 - 2 / (3 cos^2 t13)
    TM2 (second column 1/3, 1/3, 1/3):  sin^2(t12) cos^2(t13) = 1/3   ->  sin^2 t12 = 1 / (3 cos^2 t13)
This instrument reads `data.json`, transcribed AFTER the seal from the primary sources the preregistration names, and for
each data set and ordering computes:
 R1  each relation's sin^2 t12 at the measured sin^2 t13 (best fit), and its spread over sin^2 t13's 1-sigma interval;
 R2  each prediction's pull: (prediction - best) / sigma on the prediction's side (asymmetric errors), the spread of R1
     added in quadrature;
 R3  whether each prediction lies inside the data set's 3-sigma range of sin^2 t12;
 R4  the verdicts at the sealed thresholds: TM1 within 2 sigma; TM2 beyond 3 sigma.
Writes two_relations.json."""
import json, pathlib, math
HERE = pathlib.Path(__file__).resolve().parent


def tm1(s13): return 1 - 2 / (3 * (1 - s13))
def tm2(s13): return 1 / (3 * (1 - s13))


def main():
    data = json.load(open(HERE / "data.json"))
    out = {"sources": {k: v.get("source") for k, v in data["sets"].items()}, "sets": {}}
    for name, ds in data["sets"].items():
        res = {}
        for order, d in ds["orderings"].items():
            s12, s13 = d["sin2_theta12"], d["sin2_theta13"]
            row = {}
            for rel, f in (("TM1", tm1), ("TM2", tm2)):
                p = f(s13["best"]); lo, hi = f(s13["best"] - s13["minus"]), f(s13["best"] + s13["plus"])
                spread = max(abs(hi - p), abs(lo - p))
                sig = s12["plus"] if p >= s12["best"] else s12["minus"]
                pull = (p - s12["best"]) / math.sqrt(sig ** 2 + spread ** 2)
                row[rel] = {"sin2_theta12_predicted": round(p, 5), "theta13_spread": round(spread, 6), "pull_sigma": round(pull, 3),
                            "inside_3sigma_range": bool(s12["lo3"] <= p <= s12["hi3"])}
            row["TM1_within_2sigma"] = abs(row["TM1"]["pull_sigma"]) < 2
            row["TM2_beyond_3sigma"] = abs(row["TM2"]["pull_sigma"]) > 3
            res[order] = row
        out["sets"][name] = res
    json.dump(out, open(HERE / "two_relations.json", "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
