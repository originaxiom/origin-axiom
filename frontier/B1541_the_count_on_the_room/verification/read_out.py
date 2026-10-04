#!/usr/bin/env python3
"""B1541 -- THE READ-OUT (PREREGISTRATION.md sections 7 and 9): the predictions from run.jsonl, once.

    python3 read_out.py [--record]    ->  read_out.json, read_out_log.txt

evaluate() is pure (control K6 calls it on synthetic rows).  Coverage: complete only if every sealed task (run.tasks()) has
exactly its readings (three per Part A or B task: route N, route R at p_N on the same class, route R's own class at p_R; two
for Part C), each once.  A prediction that a row can refute is False on that row whatever the coverage; a population-wide one
is True only on complete records, else None.  A positive needs the class's count in both routes.
  P1  the transport: at every class of Parts A and B, route R at p_N reads route N's count, k and connecting ranks exactly.
  P2  across primes: within every subspace, the counts of all draws in both routes (route N and route R's own) are one value.
  P3  every reading's identities hold (sm:B1536's B1297, annihilator and Lemma E checks, and Theorem C's).
  P4  some class read has a generation-shaped count: I(W) = I(L2W) != 0, in route N and in route R at p_N.
  P5  some class read has the count (-3, -3), in route N and in route R at p_N.
  P6  the class pulled back from m003 reads (0, 0) in both routes (fixed by the banked rows)."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def evaluate(rows, sealed_tasks, say=print):
    want = {}
    for (part, name, draw) in sealed_tasks:
        want[(part, name, draw)] = ("N", "R") if part == "C" else ("N", "R at p_N (the same class)", "R")
    got, dup, extra = {}, [], []
    for r in rows:
        key = (r["part"], r["subspace"], r["draw"])
        if key not in want:
            extra.append([*key])
            continue
        slot = got.setdefault(key, {})
        if r["route"] in slot:
            dup.append([*key, r["route"]])
        slot[r["route"]] = r["reading"]
    missing = [[*k] for k, routes in want.items() if set(got.get(k, {})) != set(routes)]
    complete = not (missing or dup or extra)
    out = {"tasks": len(want), "tasks read in full": sum(1 for k, routes in want.items() if set(got.get(k, {})) == set(routes)),
           "coverage problems": {k: v for k, v in (("missing", missing[:50]), ("duplicates", dup), ("unexpected", extra)) if v},
           "complete": complete}
    pred = {}

    def whole(bad):
        return False if bad else (True if complete else None)
    # P1: the same class in two routes
    p1 = []
    for key, slot in got.items():
        if key[0] in ("A", "B") and "N" in slot and "R at p_N (the same class)" in slot:
            a, b = slot["N"], slot["R at p_N (the same class)"]
            if (a["count"], a["k"], a["rk d1"]) != (b["count"], b["k"], b["rk d1"]):
                p1.append([*key, a["count"], b["count"]])
    pred["P1"] = whole(p1)
    # P2: one generic count per subspace, across draws, routes and primes
    by_sub = {}
    for key, slot in got.items():
        if key[0] in ("A", "B"):
            for route in ("N", "R"):
                if route in slot:
                    by_sub.setdefault((key[0], key[1]), set()).add(tuple(slot[route]["count"]))
    p2 = [[part, name, sorted(map(list, v))] for (part, name), v in sorted(by_sub.items()) if len(v) > 1]
    pred["P2"] = whole(p2)
    # P3: identities
    p3 = [[*key, route, rr["failed"]] for key, slot in got.items() for route, rr in slot.items() if not rr["all"]]
    pred["P3"] = whole(p3)
    # P4, P5: positives need route N and route R at p_N on the same class
    shaped, three = [], []
    for key, slot in got.items():
        if key[0] in ("A", "B") and "N" in slot and "R at p_N (the same class)" in slot:
            a, b = slot["N"]["count"], slot["R at p_N (the same class)"]["count"]
            if a == b and a[0] == a[1] != 0:
                shaped.append([*key, a])
                if a == [-3, -3]:
                    three.append([*key, a])
    pred["P4"] = True if shaped else (False if complete else None)
    pred["P5"] = True if three else (False if complete else None)
    # P6: the pulled-back class
    pb = got.get(("C", "pulled back", 0), {})
    p6_bad = [route for route, rr in pb.items() if rr["count"] != [0, 0]]
    pred["P6"] = False if p6_bad else (True if set(pb) == {"N", "R"} else None)
    out["the counts by subspace (route N; route R's own)"] = {
        f"{part} {name}": sorted(map(list, v)) for (part, name), v in sorted(by_sub.items())}
    out["transport disagreements"] = p1
    out["subspaces with more than one count"] = p2
    out["identity failures"] = p3[:50]
    out["generation-shaped classes"] = shaped
    out["three-generation classes"] = three
    out["the pulled-back class"] = {route: rr["count"] for route, rr in pb.items()}
    out["predictions"] = pred
    for k in ("P1", "P2", "P3", "P4", "P5", "P6"):
        say(f"{k}: {pred[k]}")
    return out


def verdict(pred):
    """section 9: PROVED (three at a class) if P1, P3, P6 hold and P5 holds; NEGATIVE (scoped: no generation-shaped count at the
    generic classes of the 42 subspaces read) if P1-P3 and P6 hold and P4 is False; else OPEN"""
    if not all(pred[k] is True for k in ("P1", "P3", "P6")):
        return "OPEN"
    if pred["P5"] is True:
        return "PROVED"
    if pred["P2"] is True and pred["P4"] is False:
        return "NEGATIVE"
    return "OPEN"


def main():
    import importlib.util
    spec = importlib.util.spec_from_file_location("b1541_run_ro", HERE / "run.py")
    RUN = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(RUN)
    log = []

    def say(s):
        log.append(s)
        print(s)
    rows = [json.loads(x) for x in (HERE / "run.jsonl").read_text().splitlines() if x.strip()]
    ident = json.loads((HERE / "identity.json").read_text())
    res = evaluate(rows, RUN.tasks(), say)
    res["identity holds"] = bool(ident.get("identity holds"))
    res["verdict"] = verdict(res["predictions"]) if res["identity holds"] else "OPEN"
    say(f"identity holds: {res['identity holds']}")
    say(f"verdict: {res['verdict']}")
    say(json.dumps({k: v for k, v in res.items() if k not in ("predictions",)})[:20000])
    res["log"] = log
    if "--record" in sys.argv:
        (HERE / "read_out.json").write_text(json.dumps(res, indent=1) + "\n")
        (HERE / "read_out_log.txt").write_text("\n".join(log) + "\n")
    return res


if __name__ == "__main__":
    main()
