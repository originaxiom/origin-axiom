#!/usr/bin/env python3
"""B1536 -- THE READ-OUT (PREREGISTRATION section 7): both routes' records, compared row by row, and the predictions.

    python3 read_out.py [--dir D] [--record]   ->  read_out.json

Inputs: run_N_m004.jsonl, run_R_m004.jsonl, run_N_m003.jsonl, run_R_m003.jsonl (run.py).  A row is (state, cover, u, kappa).
  - Route agreement (P1): every row both routes read has the same supplies; every Part P count, k and connecting rank agree;
    every Part O stratum has the same generic reading (count, k, connecting ranks) in both routes.
  - Identities (P2): every reading of either route has 'all' true (B1297, the annihilator identity, Lemma E on every module and
    piece, and Theorem C's identities and caps).
  - Completeness: each route's rows against the population (population.py): every cover done and every (u, kappa) read.
  - The caps, the supplies at kappa = 1, the counts, and the strata bounds of Lemma G:
        bound_L2(S) = rk_gen d1(L2*) - |S|,  bound_W(S) = b0 - |S| + rk_gen d1(E*),
    each generic rank the larger of the two draws' ranks, taken separately (so the bounds are never understated); a stratum
    whose classes can have k = |S| (some draw has k = |S|) is OPEN for three if both bounds are >= 3 and its generic count is
    not (-3, -3).
  - A count is generation-shaped when I(W) = I(L2W) != 0 (sm:B1509's dictionary, N = -I(W)); three is (-3, -3) (the other
    order reads W1 at the conjugate character, which is in the population).  P8 and P9 look at every reading of both routes
    (Part P, and both draws of every Part O stratum), not only at the generic ones."""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATES = ("m004", "m003")
TOWER_LINE = 4


def load(path):
    rows, done = {}, set()
    if not path.exists():
        return rows, done
    for line in path.read_text().splitlines():
        r = json.loads(line)
        if r.get("done"):
            done.add(r["cover"])
            continue
        rows[(r["state"], r["cover"], tuple(r["u"]), r["kappa"])] = r
    return {k: v for k, v in rows.items() if k[1] in done}, done


def expected_keys(st):
    """the population's (state, cover, u, kappa) keys, as run.py writes them"""
    sys.path.insert(0, str(HERE))
    import cover_lib as CL
    import population as POP
    s = CL.state(st)
    keys = set()
    for cid, perms in POP.covers(s):
        for (u, kap) in POP.characters(s, perms)[3]:
            keys.add((st, cid, (str(u[0]), str(u[1])), str(kap)))
    return keys


def gen_reading(readings):
    """the generic reading of a stratum: the draw with the largest connecting ranks (generic ranks are maximal)"""
    return max(readings, key=lambda x: (x["rk d1"]["L2*"], x["rk d1"]["E*"], x["rk d1"]["E"], x["k"]))


def main():
    d = Path(sys.argv[sys.argv.index("--dir") + 1]) if "--dir" in sys.argv else HERE
    out = {"routes": {}, "agreement": {}, "per state": {}}
    allrows = {}
    for st in STATES:
        for rt in ("N", "R"):
            rows, done = load(d / f"run_{rt}_{st}.jsonl")
            allrows[(st, rt)] = rows
            out["routes"][f"{rt} {st}"] = {"covers done": len(done), "rows": len(rows)}
    complete = {}
    for st in STATES:
        want = expected_keys(st)
        for rt in ("N", "R"):
            got = set(allrows[(st, rt)])
            complete[f"{rt} {st}"] = {"expected": len(want), "read": len(got & want), "missing": len(want - got),
                                      "unexpected": len(got - want)}
    out["completeness"] = complete
    out["complete"] = all(v["missing"] == 0 and v["unexpected"] == 0 for v in complete.values())
    # ---- P1: route agreement
    dis = defaultdict(list)
    compared = Counter()
    for st in STATES:
        A, B = allrows[(st, "N")], allrows[(st, "R")]
        for key in sorted(set(A) & set(B)):
            a, b = A[key], B[key]
            compared["rows"] += 1
            if a["S"] != b["S"]:
                dis["supplies"].append(list(key))
            if ("P" in a) != ("P" in b):
                dis["Part P presence"].append(list(key))
            elif "P" in a:
                compared["Part P"] += 1
                ka = (a["P"]["count"], a["P"]["k"], a["P"]["rk d1"])
                kb = (b["P"]["count"], b["P"]["k"], b["P"]["rk d1"])
                if ka != kb:
                    dis["Part P"].append(list(key))
            if ("O" in a) != ("O" in b):
                dis["Part O presence"].append(list(key))
            elif "O" in a:
                sa = {tuple(x["S"]): gen_reading(x["readings"]) for x in a["O"]}
                sb = {tuple(x["S"]): gen_reading(x["readings"]) for x in b["O"]}
                compared["Part O strata"] += len(sa)
                if set(sa) != set(sb):
                    dis["Part O strata sets"].append(list(key))
                for S in set(sa) & set(sb):
                    if (sa[S]["count"], sa[S]["k"], sa[S]["rk d1"]) != (sb[S]["count"], sb[S]["k"], sb[S]["rk d1"]):
                        dis["Part O generic readings"].append(list(key) + [list(S)])
    out["agreement"] = {"compared": dict(compared), "disagreements": {k: len(v) for k, v in dis.items()},
                        "first disagreements": {k: v[:10] for k, v in dis.items()}}
    # ---- per state: identities, supplies, caps, counts, strata
    gen_shaped, threes, open_strata, failed, pulled_shaped = [], [], [], [], []
    for st in STATES:
        rows = {**allrows[(st, "R")], **allrows[(st, "N")]}        # route N where both read
        ps = {"characters": 0, "members": 0, "caps": Counter(), "kappa = 1 supplies": {}, "Part P counts": Counter(),
              "Part O characters": 0, "Part O strata": 0}
        for rt in ("N", "R"):
            for key, r in allrows[(st, rt)].items():
                for part in ("P",):
                    if part in r and not r[part]["all"]:
                        failed.append([rt] + list(key) + [part, r[part]["failed"]])
                for o in r.get("O", []):
                    for x in o["readings"]:
                        if not x["all"]:
                            failed.append([rt] + list(key) + ["O", o["S"], x["failed"]])
        for key, r in rows.items():
            ps["characters"] += 1
            if not r["member"]:
                continue
            ps["members"] += 1
            ps["caps"][str((r["S"]["capW"], r["S"]["capL2"]))] += 1
            if r["kappa"] == "0" and r["u"] == ["0", "0"]:
                ps["kappa = 1 supplies"][r["cover"]] = {"n(1)": r["S"]["n(L)"], "n(rho)": r["S"]["n((VL)*)"],
                                                         "h1(rho)": r["S"]["h1(V_eta)"]}
            if "P" in r:
                c = tuple(r["P"]["count"])
                ps["Part P counts"][str(c)] += 1
                if c[0] == c[1] != 0:
                    gen_shaped.append({"state": st, "cover": r["cover"], "u": r["u"], "kappa": r["kappa"], "class": "pulled back",
                                       "count": list(c)})
            if "O" in r:
                ps["Part O characters"] += 1
                for o in r["O"]:
                    ps["Part O strata"] += 1
                    g = gen_reading(o["readings"])
                    c = tuple(g["count"])
                    if c[0] == c[1] != 0:
                        gen_shaped.append({"state": st, "cover": r["cover"], "u": r["u"], "kappa": r["kappa"],
                                           "class": ["generic", o["S"]], "count": list(c)})
                    nS = len(o["S"])
                    bL2 = max(x["rk d1"]["L2*"] for x in o["readings"]) - nS
                    bW = g["b0"] - nS + max(x["rk d1"]["E*"] for x in o["readings"])
                    if any(x["k"] == nS for x in o["readings"]) and bL2 >= 3 and bW >= 3 and c != (-3, -3):
                        open_strata.append({"state": st, "cover": r["cover"], "u": r["u"], "kappa": r["kappa"],
                                            "S": o["S"], "bounds": [bW, bL2], "generic count": list(c)})
        # P8 and P9: every reading of both routes
        for rt in ("N", "R"):
            for key, r in allrows[(st, rt)].items():
                where = {"route": rt, "state": st, "cover": r["cover"], "u": r["u"], "kappa": r["kappa"]}
                if "P" in r:
                    c = tuple(r["P"]["count"])
                    if c[0] == c[1] != 0:
                        pulled_shaped.append(dict(where, count=list(c)))
                    if c == (-3, -3):
                        threes.append(dict(where, **{"class": "pulled back", "count": list(c)}))
                for o in r.get("O", []):
                    for i, x in enumerate(o["readings"]):
                        if tuple(x["count"]) == (-3, -3):
                            threes.append(dict(where, **{"class": ["stratum", o["S"], "draw", i], "count": [-3, -3]}))
        ps["caps"] = dict(ps["caps"])
        ps["Part P counts"] = dict(ps["Part P counts"])
        out["per state"][st] = ps
    out["generation-shaped"] = gen_shaped
    out["generation-shaped at the pulled-back class (either route)"] = pulled_shaped
    out["three"] = threes
    out["open strata"] = open_strata
    out["failed readings"] = failed[:50]
    out["failed readings (number)"] = len(failed)
    # ---- the predictions
    P = {}
    P["P1"] = compared["rows"] > 0 and not dis
    P["P2"] = len(failed) == 0
    k1 = {st: out["per state"][st]["kappa = 1 supplies"] for st in STATES}
    cyc = {st: [c for c in k1[st] if c.startswith("d")] for st in STATES}
    caps3 = sum(v for st in STATES for cap, v in out["per state"][st]["caps"].items()
                if min(eval(cap)) >= 3)
    P["P3"] = all(r["S"]["n(L)"] == 0 for st in STATES for rt in ("N", "R") for r in allrows[(st, rt)].values()
                  if r.get("abelian"))
    P["P4"] = all(all(v["n(1)"] == 0 for c, v in k1[st].items() if c.startswith("d")) for st in STATES)
    tow = {st: [v["n(1)"] for c, v in k1[st].items() if c.startswith("Q8")] for st in STATES}
    P["P5"] = all(tow[st] and max(tow[st]) == TOWER_LINE for st in STATES)
    P["P6"] = all(all(v["n(rho)"] == 0 for c, v in k1[st].items() if c.startswith("d")) for st in STATES)
    P["P7"] = caps3 == 0
    P["P8"] = not threes
    P["P9"] = not pulled_shaped
    P["P10"] = not open_strata
    out["predictions"] = P
    out["the Q8 tower's n(1) at kappa = 1"] = {st: {c: v["n(1)"] for c, v in k1[st].items() if c.startswith("Q8")}
                                               for st in STATES}
    out["the Q8 tower's n(rho) at kappa = 1"] = {st: {c: v["n(rho)"] for c, v in k1[st].items() if c.startswith("Q8")}
                                                 for st in STATES}
    out["(N, nu) with both caps >= 3"] = caps3
    print(json.dumps({k: v for k, v in out.items() if k not in ("per state",)}, indent=1, default=str)[:6000])
    if "--record" in sys.argv:
        (HERE / "read_out.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    return out


if __name__ == "__main__":
    main()
