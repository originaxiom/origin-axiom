#!/usr/bin/env python3
"""B1535 read-out (PREREGISTRATION section 7): the sealed predictions on part_m.jsonl and part_w.json.

    python3 read_out.py [--record]   ->  read_out.json (and read_out_log.txt)"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYS = ("I(W)", "I(L2W)", "k", "b0", "n((VL)*)", "n(V)", "n(L)", "rk d1")


def T(r):
    return (r["I(W)"], r["I(L2W)"])


def main(d=HERE):
    rows = [json.loads(x) for x in (d / "part_m.jsonl").read_text().splitlines() if x.strip()]
    W = json.loads((d / "part_w.json").read_text())
    pure = [r for r in rows if r["class"].startswith("pure-")]
    mixed = [r for r in rows if r["class"].startswith("mixed")]
    p = {}
    # P1: pure classes equal sm:B1534's banked sums, both primes (and route Ind where read)
    p1_bad = [r for r in pure if not (list(T(r["RS p1"])) == list(T(r["RS p2"])) == r["banked"])]
    p["P1 pure classes = banked sums"] = not p1_bad
    # P2: Theorem C's identities and the cap at every reading, every route
    p2_bad = [r for r in rows if not (r["RS p1"]["all"] and r["RS p2"]["all"] and r.get("Ind", {"all": True})["all"])]
    p["P2 Theorem C at every reading"] = not p2_bad
    # P3: the routes agree on every quantity
    p3_bad = [r for r in rows if any(r["RS p1"][k] != r["RS p2"][k] for k in KEYS) or
              ("Ind" in r and any(r["Ind"][k] != r["RS p1"][k] for k in KEYS))]
    p["P3 the routes agree"] = not p3_bad
    # P4: no reading is two or more generations (the readings are W1's; the other order is W1 at the conjugate member)
    p4_bad = [r for r in rows if r["RS p1"]["I(W)"] == r["RS p1"]["I(L2W)"] and abs(r["RS p1"]["I(W)"]) >= 2]
    p["P4 at most one generation"] = not p4_bad
    # P5: mixing adds no new value: every mixed reading's value occurs among the pure readings at the same (state, nu, B)
    pure_vals = defaultdict(set)
    for r in pure:
        pure_vals[(r["state"], tuple(r["nu"]), json.dumps(r["B"]))].add(T(r["RS p1"]))
    p5_new = [r for r in mixed if T(r["RS p1"]) not in pure_vals[(r["state"], tuple(r["nu"]), json.dumps(r["B"]))]]
    p["P5 mixing adds no new value"] = not p5_new
    # P6: the two generic mixed classes read alike at every (nu, B)
    gen = defaultdict(dict)
    for r in mixed:
        if r["class"].startswith("mixed-generic"):
            gen[(r["state"], tuple(r["nu"]), json.dumps(r["B"]))][r["class"]] = T(r["RS p1"])
    p6_bad = [k for k, v in gen.items() if len(set(v.values())) > 1]
    p["P6 generic mixed classes agree"] = not p6_bad
    # P7: every cancellation class vanishes on at least one cover cusp (route RS's k below the number of cusps)
    canc = [r for r in mixed if r["class"] == "mixed-cancel"]
    p7_bad = [r for r in canc if not r["RS p1"]["k"] < r["RS p1"]["cusps"]]
    p["P7 the cancellation stratum"] = not p7_bad
    # P8: Lemma W's census
    p["P8 Lemma W census"] = bool(W.get("Lemma W holds"))
    # P9: at m135's non-simple member u1 = (0, 1/2) on the cover <(1/2, 1/2)>, a mixed generic class reaches the cap, -2
    p9 = [r for r in mixed if r["state"] == "-LLRR" and r["nu"] == ["0", "1/2", "0"] and len(r["B"]) == 2 and
          ["1/2", "1/2", "0"] in r["B"] and r["class"].startswith("mixed-generic")]
    p["P9 a mixed generic class at u1 on <(1/2,1/2)> reads I(L2W) = -2"] = any(r["RS p1"]["I(L2W)"] == -2 for r in p9)
    out = {
        "rows": len(rows), "pure": len(pure), "mixed": len(mixed),
        "values (all readings)": dict(Counter(str(T(r["RS p1"])) for r in rows)),
        "values (mixed)": dict(Counter(str(T(r["RS p1"])) for r in mixed)),
        "generation-shaped readings": dict(Counter(str(T(r["RS p1"])) for r in rows
                                               if r["RS p1"]["I(W)"] == r["RS p1"]["I(L2W)"] != 0)),
        "route Ind readings": sum(1 for r in rows if "Ind" in r),
        "covers by order": dict(Counter(len(r["B"]) for r in rows)),
        "failures (first 10)": {"P1": [(r["state"], r["nu"], r["class"]) for r in p1_bad[:10]],
                                "P2": [(r["state"], r["nu"], r["class"], r["RS p1"]["failed"]) for r in p2_bad[:10]],
                                "P3": [(r["state"], r["nu"], r["class"]) for r in p3_bad[:10]],
                                "P4": [(r["state"], r["nu"], r["class"], T(r["RS p1"])) for r in p4_bad[:10]],
                                "P5 new values": [(r["state"], r["nu"], r["B"], r["class"], T(r["RS p1"])) for r in p5_new[:10]],
                                "P6": p6_bad[:10], "P7": [(r["state"], r["nu"], r["class"]) for r in p7_bad[:10]]},
        "Part W": W, "predictions": p,
        "verdict rule (section 9)": "PROVED if P2, P3 and P8 hold" + (": they do" if p["P2 Theorem C at every reading"] and
                                                                       p["P3 the routes agree"] and p["P8 Lemma W census"]
                                                                       else ": they do not"),
    }
    print(json.dumps(out, indent=1, default=str))
    if "--record" in sys.argv:
        (d / "read_out.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    return out


if __name__ == "__main__":
    main()
