#!/usr/bin/env python3
"""B1529 read-out: the sealed predictions (PREREGISTRATION section 7) read from census.jsonl and crossings_<name>.json.
Written and committed with PREREGISTRATION.md before either instrument ran on any outcome.  Writes read_out.json and prints it.

P1  SR for Lambda^2 at every base point of every word state and every level M_2 .. M_6: am(C; 1) = am(C'; 1) = 2 at every
    character, and e = am(D; 1) = 2.
P2  the four's base condition at every base point of every word state: (h1, h1*, t0, s0) = (1, 1, 1, 1).
P3  the theorems' controls, everywhere (word states and levels): Lambda^2's (h1, h1*, t0, s0) = (2, 2, 2, 2) (Lemma B); I = 0 for
    both modules (Part H); e = am(D; 1) = 2 for both modules; route T's hypothesis holds; no manifold failed to compute; the levels
    reproduce sm:B1515's banked h1 of the four (1 throughout M_2 .. M_5; on M_6, 1 at 292, 2 at 24, 3 at 4).
P4  the crossings' structure on the ten rings: at least 90% of the brackets located; at every located crossing, per module the
    crossing concerns, e = 1 (the four at E1, E2, E3) or 2 (Lambda^2 at E1, E4), with 1 or 2 distinct special twists (Lambda^2's
    two with product 1 to 1e-30), and (t0, s0) = (1, 1) on every route-T row at a special twist.
P5  the index at the crossings: I = 0 on every route-T row; on every Fox and route-W row, I = 0, every identity holds, and Fox,
    W and T agree on (h1, h1*, t0, s0, I).
P6  the mechanism: at every Lambda^2 special twist, the interior value |chi_K(kappa*)| (relative) exceeds 1e-20.
G   the golden form: P1 and P2 hold on every golden word state (|trace| in {3, 7, 18, 47, 123, 322}), and P5 holds on the
    golden states among the ten (+-LR, +-L^4RL^3R^2, +-L^4RLR^3LR^2).
Recorded, not predicted: the four's am(C; 1) by character; the crossings by kind; the interior values of the four."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEN = [("+", "LR"), ("-", "LR"), ("+", "LLRLRR"), ("-", "LLRLRR"), ("+", "LLLRLRR"), ("-", "LLLRLRR"), ("+", "LLLLRLLLRR"),
       ("-", "LLLLRLLLRR"), ("+", "LLLLRLRRRLRR"), ("-", "LLLLRLRRRLRR")]
GOLDEN_TEN = {"+LR", "-LR", "+LLLLRLLLRR", "-LLLLRLLLRR", "+LLLLRLRRRLRR", "-LLLLRLRRRLRR"}
B1515_M6 = {"1": 292, "2": 24, "3": 4}


def name_of(sign, word):
    return ("p" if sign == "+" else "m") + word


def census():
    recs = [json.loads(line) for line in (HERE / "census.jsonl").read_text().splitlines()]
    errors = [r["state"] for r in recs if "error" in r]
    ok = [r for r in recs if "error" not in r]
    words = [r for r in ok if not r.get("level")]
    levels = {r["state"]: r for r in ok if r.get("level")}

    def sr_fails(r):
        s = r["L2"]
        return not (set(s["am(C; 1) values"]) == {"2"} and set(s["am(C'; 1) values"]) == {"2"} and s["e"] == 2
                    and s["am(D; 1)"] == 2)

    def base_fails(r):
        return set(r["4"]["(h1, h1*, t0, s0) values"]) != {"(1, 1, 1, 1)"}

    p1_fail = [r["state"] for r in ok if sr_fails(r)]
    p2_fail = [r["state"] for r in words if base_fails(r)]
    p3 = {"Lambda^2 base condition everywhere": all(set(r["L2"]["(h1, h1*, t0, s0) values"]) == {"(2, 2, 2, 2)"} for r in ok),
          "I = 0 everywhere, both modules": all(set(r[m]["I values"]) == {"0"} for r in ok for m in ("4", "L2")),
          "e = am(D; 1) = 2, both modules": all(r[m]["e"] == 2 and r[m]["am(D; 1)"] == 2 for r in ok for m in ("4", "L2")),
          "route T's hypothesis everywhere": all(r[m]["hypothesis fails"] == 0 for r in ok for m in ("4", "L2")),
          "no manifold failed": not errors,
          "536 word states and 5 levels": len(words) == 536 and len(levels) == 5,
          "levels reproduce sm:B1515": all(levels.get("+" + "LR" * n, {}).get("4", {}).get("(h1, h1*, t0, s0) values", {}).keys()
                                           == {"(1, 1, 1, 1)"} for n in range(2, 6))
          and {k.split(",")[0].strip("(") : v for k, v in levels["+" + "LR" * 6]["4"]["(h1, h1*, t0, s0) values"].items()}
          == B1515_M6 if "+" + "LR" * 6 in levels else False}
    golden_words = [r for r in words if r["golden"]]
    four_am = {}
    for r in words:
        for k, v in r["4"]["am(C; 1) values"].items():
            four_am[k] = four_am.get(k, 0) + v
    return {
        "P1": {"holds": not p1_fail, "failing manifolds": p1_fail,
               "base points": sum(r["L2"]["rows"] for r in ok)},
        "P2": {"holds": not p2_fail, "failing word states": p2_fail,
               "base points": sum(r["4"]["rows"] for r in words)},
        "P3": {"holds": all(p3.values()), "checks": p3, "errors": errors},
        "G (census part)": {"golden word states": len(golden_words),
                            "P1 and P2 hold on all of them": not any(sr_fails(r) or base_fails(r) for r in golden_words),
                            "golden among P1 failures": [s for s in p1_fail if any(r["state"] == s and r["golden"] for r in ok)],
                            "golden among P2 failures": [s for s in p2_fail if any(r["state"] == s and r["golden"] for r in ok)]},
        "recorded: the four's am(C; 1) over the word states' base points": four_am,
    }


def crossings():
    out = {"states": {}, "P4": True, "P5": True, "P6": True, "missing": []}
    brackets = located = 0
    for sign, word in TEN:
        f = HERE / ("crossings_" + name_of(sign, word) + ".json")
        if not f.exists():
            out["missing"].append(sign + word)
            out["P4"] = out["P5"] = out["P6"] = False
            continue
        d = json.loads(f.read_text())
        st = {"brackets": d["brackets"], "by kind": d["brackets by kind"], "located": 0, "rows T": 0, "rows Fox/W": 0,
              "I != 0": 0, "structure fails": [], "index fails": [], "mechanism fails": []}
        brackets += d["brackets"]
        for c in d["crossings"]:
            if "read" not in c:
                continue
            st["located"] += 1
            located += 1
            rd = c["read"]
            for mod, rec in rd.items():
                if mod not in ("4", "L2"):
                    continue
                want_e = 1 if mod == "4" else 2
                ks = rec["kappa*"]
                if rec["e"] != want_e or len(ks) != want_e:
                    st["structure fails"].append([c["kind"], mod, "e", rec["e"], "twists", len(ks)])
                if mod == "L2" and len(ks) == 2 and float(rec["|kappa1 kappa2 - 1|"]) > 1e-30:
                    st["structure fails"].append([c["kind"], mod, "|kappa1 kappa2 - 1|", rec["|kappa1 kappa2 - 1|"]])
                for tw in rec["twists"]:
                    rt = tw["route T"]
                    st["rows T"] += rt["rows"]
                    if set(rt["rows by (t0, s0)"]) != {"(1, 1)"}:
                        st["structure fails"].append([c["kind"], mod, "(t0, s0)", rt["rows by (t0, s0)"]])
                    if rt["I != 0"] or rt["hypothesis fails"]:
                        st["index fails"].append([c["kind"], mod, "route T", rt["I values"], rt["hypothesis fails"]])
                        st["I != 0"] += rt["I != 0"]
                    if mod == "L2" and (rt["smallest |chi_K(kappa*)| rel"] is None
                                        or float(rt["smallest |chi_K(kappa*)| rel"]) <= 1e-20):
                        st["mechanism fails"].append([c["kind"], tw["kappa*"], rt["smallest |chi_K(kappa*)| rel"]])
                    for row in tw["Fox and W"]:
                        st["rows Fox/W"] += 1
                        F, W, T = row["Fox"], row["W"], row["T"]
                        agree = ((F["h1"], F["h1*"], F["t0"], F["s0"], F["I"])
                                 == (W["h1(V)"], W["h1(V*)"], W["t0"], W["s0"], W["I"])
                                 == (T["h1"], T["h1*"], T["t0"], T["s0"], T["I"]))
                        if F["I"] != 0 or not all(F["checks"].values()) or not agree:
                            st["index fails"].append([c["kind"], mod, row["u"], "Fox", F["I"], "W", W["I"], "T", T["I"],
                                                      "agree", agree])
        out["states"][sign + word] = st
        if st["structure fails"]:
            out["P4"] = False
        if st["index fails"]:
            out["P5"] = False
        if st["mechanism fails"]:
            out["P6"] = False
    out["brackets"], out["located"] = brackets, located
    if brackets and located < 0.9 * brackets:
        out["P4"] = False
    out["G (crossing part)"] = all(not out["states"].get(s, {"index fails": [1]})["index fails"] for s in GOLDEN_TEN)
    return out


def main():
    c = census()
    x = crossings()
    res = {"census": c, "crossings": x,
           "predictions": {"P1": c["P1"]["holds"], "P2": c["P2"]["holds"], "P3": c["P3"]["holds"], "P4": x["P4"],
                           "P5": x["P5"], "P6": x["P6"],
                           "G": c["G (census part)"]["P1 and P2 hold on all of them"] and x["G (crossing part)"]}}
    (HERE / "read_out.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps(res["predictions"], indent=1))
    print(json.dumps({k: v for k, v in c.items()}, indent=1, default=str)[:4000])
    print(json.dumps({k: v for k, v in x.items() if k != "states"}, indent=1, default=str))


if __name__ == "__main__":
    main()
