#!/usr/bin/env python3
"""B1544 -- THE READ-OUT (PREREGISTRATION.md sections 7 and 9): the predictions from run.jsonl, once.

    python3 read_out.py [--record]    ->  read_out.json, read_out_log.txt

evaluate() is pure (control K4 calls it through selftest() on synthetic rows).  Coverage: complete only if every sealed task
(run.tasks()) has exactly two readings, route F and route R, each once.  A prediction a row can refute is False on that row
whatever the coverage; a population-wide one is True only on complete records, else None.
  P1  one count per subspace: within each (cover, subspace) every draw in both routes reads one count; and the subspaces of a
      cover that the deck group's action on the cusps carries into one another read one count.
  P2  the classes: at every reading rk delta1_W = 0 (the class lies in K0) and the class's support is the subspace's S.
  P3  the identities: route R's (sm:B1536's checks, Theorem C's caps) at every reading; and Lemma F's ingredients in both routes
      at every reading: h0(dN; W*) = 2m, h1(dN; W) = 4m - k, r1(W) <= 3m - k, I(W) = -1 + h0(dN; W*) - r1(W), I(W) >= k - m - 1
      (m the number of cusps, k the size of the support).
  P4  the floor on K0: I(W) >= -1 at every reading.
  P5  some subspace reads a generation-shaped count, I(W) = I(L2W) != 0, in both routes.
  P6  some subspace reads (-3, -3) in both routes."""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOM3 = ("d10.13", "d10.36")


def parse_s(name):
    return tuple(sorted(int(x) for x in name.split("S=", 1)[1].split(",") if x != ""))


def orbit_key(S, tau):
    """the deck group's orbit of the cusp set S, as a canonical tuple"""
    seen, cur = set(), tuple(sorted(S))
    while cur not in seen:
        seen.add(cur)
        cur = tuple(sorted(tau[x] for x in cur))
    return min(seen)


def lemma_f_holds(x):
    lf, k = x["lemma F"], len(x["support"])
    m = lf["m"]
    return (lf["h0(dN;W*)"] == 2 * m and lf["h1(dN;W)"] == 4 * m - k and lf["r1(W)"] <= 3 * m - k
            and x["count"][0] == -1 + lf["h0(dN;W*)"] - lf["r1(W)"] and x["count"][0] >= k - m - 1)


def evaluate(rows, sealed_tasks, taus, say=print):
    want = {t: ("F", "R") for t in sealed_tasks}
    got, dup, extra = {}, [], []
    for r in rows:
        key = (r["cover"], r["subspace"], r["draw"])
        if key not in want:
            extra.append([*key])
            continue
        slot = got.setdefault(key, {})
        if r["route"] in slot:
            dup.append([*key, r["route"]])
        slot[r["route"]] = r["reading"]
    missing = [[*k] for k, routes in want.items() if set(got.get(k, {})) != set(routes)]
    complete = not (missing or dup or extra)
    by = {}
    for (cid, sub, draw), slot in got.items():
        for route, x in slot.items():
            by.setdefault((cid, sub), {}).setdefault(route, set()).add(tuple(x["count"]))
    p1 = all(len(set().union(*d.values())) == 1 for d in by.values())
    orbits = {}
    for (cid, sub), d in by.items():
        orbits.setdefault((cid, orbit_key(parse_s(sub), taus[cid])), set()).update(set().union(*d.values()))
    if any(len(v) > 1 for v in orbits.values()):
        p1 = False
    readings = [(cid, sub, route, x) for (cid, sub, draw), slot in got.items() for route, x in slot.items()]
    p2 = all(x["rk delta1_W"] == 0 and tuple(x["support"]) == parse_s(sub) for cid, sub, route, x in readings)
    p3 = all(lemma_f_holds(x) and (route != "R" or (x.get("all") is True and not x.get("failed")))
             for cid, sub, route, x in readings)
    below = sorted([cid, sub, route, x["count"]] for cid, sub, route, x in readings if x["count"][0] < -1)
    p4 = not below
    one = {k: next(iter(d["F"])) for k, d in by.items() if "F" in d and "R" in d and d["F"] == d["R"] and len(d["F"]) == 1}
    gen = sorted((cid, sub, c) for (cid, sub), c in one.items() if c[0] == c[1] != 0)
    three = [g for g in gen if g[2] == (-3, -3)]
    pred = {
        "P1": (p1 if complete else (False if not p1 else None)),
        "P2": (p2 if complete else (False if not p2 else None)),
        "P3": (p3 if complete else (False if not p3 else None)),
        "P4": (False if not p4 else (True if complete else None)),
        "P5": (True if gen else (False if complete else None)),
        "P6": (True if three else (False if complete else None)),
    }
    for k, v in pred.items():
        say(f"{k}: {v}")
    counts = {f"{cid} {sub}": {route: sorted([list(c) for c in v]) for route, v in sorted(d.items())}
              for (cid, sub), d in sorted(by.items())}
    least = {}
    for (cid, sub), c in sorted(one.items()):
        if cid not in least or c[0] < least[cid][0]:
            least[cid] = [c[0], sub]
    room3 = {}
    for cid in ROOM3:
        cands = [(sub, c) for (cc, sub), c in one.items() if cc == cid and 1 <= len(parse_s(sub)) <= 4]
        room3[cid] = {"the subspaces where three can live (Proposition D)": [[sub, list(c)] for sub, c in sorted(cands)],
                      "a class with I(W) = -3": any(c[0] == -3 for sub, c in cands),
                      "complete": complete}
    return {"tasks": len(want), "tasks read in full": sum(1 for k in want if set(got.get(k, {})) == {"F", "R"}),
            "coverage problems": {kk: v for kk, v in (("missing", missing), ("duplicated", dup), ("extra", extra)) if v},
            "complete": complete, "the counts by subspace (route F; route R)": counts,
            "the least I(W) on K0, by cover [I(W), subspace] (subspaces read alike in both routes)": least,
            "readings below the floor": below, "the room-3 covers": room3,
            "generation-shaped subspaces": [list(g[:2]) + [list(g[2])] for g in gen],
            "three-generation subspaces": [list(g[:2]) + [list(g[2])] for g in three], "predictions": pred}


def verdict(pred):
    """section 9: PROVED if the floor breaks (P4 False) with P1-P3; NEGATIVE if it holds (P4 True) with P1-P3; else OPEN"""
    if pred["P1"] is True and pred["P2"] is True and pred["P3"] is True:
        if pred["P4"] is False:
            return "PROVED"
        if pred["P4"] is True:
            return "NEGATIVE"
    return "OPEN"


def selftest():
    """K4: the read-out's logic on synthetic rows"""
    taus = {"N45": {0: 1, 1: 4, 4: 2, 2: 5, 5: 0}, "d10.13": {0: 1, 1: 0, 3: 13, 13: 3, 5: 7, 7: 5}}
    subs = [("N45", "S=0,1,2"), ("N45", "S=1,2,4"), ("N45", "S=0,1,2,4,5"), ("d10.13", "S="), ("d10.13", "S=0,1,3,5"),
            ("d10.13", "S=0,1,7,13"), ("d10.13", "S=0,1,3,5,7,13")]
    tasks = [(cid, sub, 0) for cid, sub in subs]
    mcount = {"N45": 5, "d10.13": 6}

    def rows(counts, rk=0, supp=None, lf_bad=None, fail_r=None):
        out = []
        for (cid, sub, draw) in tasks:
            for route in ("F", "R"):
                c = counts[(cid, sub)]
                if isinstance(c, dict):
                    c = c[route]
                S = list(parse_s(sub))
                if supp and (cid, sub) in supp:
                    S = supp[(cid, sub)]
                m, k = mcount[cid], len(S)
                lf = {"m": m, "h0(dN;W*)": 2 * m, "h0(dN;W)": 2 * m - k, "r1(W)": 2 * m - 1 - c[0], "h1(dN;W)": 4 * m - k}
                if lf_bad and (cid, sub) == lf_bad:
                    lf["h0(dN;W*)"] = 2 * m - 1
                x = {"count": list(c), "rk delta1_W": rk, "support": S, "lemma F": lf}
                if route == "R":
                    bad = bool(fail_r and (cid, sub) == fail_r)
                    x.update({"all": not bad, "failed": ["cap"] if bad else []})
                out.append({"cover": cid, "subspace": sub, "draw": draw, "route": route, "reading": x})
        return out
    base = {("N45", "S=0,1,2"): (0, -6), ("N45", "S=1,2,4"): (0, -6), ("N45", "S=0,1,2,4,5"): (0, 0),
            ("d10.13", "S="): (-1, -3), ("d10.13", "S=0,1,3,5"): (-1, -3), ("d10.13", "S=0,1,7,13"): (-1, -3),
            ("d10.13", "S=0,1,3,5,7,13"): (0, -3)}
    quiet = lambda s: None  # noqa: E731
    ev = lambda r: evaluate(r, tasks, taus, say=quiet)  # noqa: E731
    r0 = ev(rows(base))
    ok0 = (r0["predictions"] == {"P1": True, "P2": True, "P3": True, "P4": True, "P5": False, "P6": False}
           and verdict(r0["predictions"]) == "NEGATIVE" and r0["the room-3 covers"]["d10.13"]["a class with I(W) = -3"] is False)
    b3 = dict(base)
    b3[("d10.13", "S=0,1,3,5")] = (-3, -3)
    b3[("d10.13", "S=0,1,7,13")] = (-3, -3)
    r3 = ev(rows(b3))
    ok3 = (r3["predictions"]["P4"] is False and r3["predictions"]["P6"] is True and r3["predictions"]["P5"] is True
           and verdict(r3["predictions"]) == "PROVED" and r3["the room-3 covers"]["d10.13"]["a class with I(W) = -3"] is True)
    bo = dict(base)                                     # tau carries S=0,1,3,5 to S=0,1,7,13: the two must agree
    bo[("d10.13", "S=0,1,7,13")] = (-2, -3)
    ro = ev(rows(bo))["predictions"]
    oko = ro["P1"] is False and verdict(ro) == "OPEN"
    bl = dict(base)
    bl[("N45", "S=0,1,2,4,5")] = {"F": (0, 0), "R": (1, 0)}
    rl = ev(rows(bl))["predictions"]
    okl = rl["P1"] is False and verdict(rl) == "OPEN"
    rk = ev(rows(base, rk=1))["predictions"]
    okk = rk["P2"] is False and verdict(rk) == "OPEN"
    rs = ev(rows(base, supp={("d10.13", "S=0,1,3,5"): [0, 1, 3]}))["predictions"]
    oks = rs["P2"] is False and verdict(rs) == "OPEN"
    rf = ev(rows(base, lf_bad=("N45", "S=0,1,2")))["predictions"]
    okf = rf["P3"] is False and verdict(rf) == "OPEN"
    rr = ev(rows(base, fail_r=("d10.13", "S=")))["predictions"]
    okr = rr["P3"] is False and verdict(rr) == "OPEN"
    short = ev(rows(base)[:-1])["predictions"]
    oks2 = short["P4"] is None and short["P1"] is None and short["P5"] is None and verdict(short) == "OPEN"
    b2 = dict(base)
    b2[("N45", "S=0,1,2")] = (-2, -6)
    b2[("N45", "S=1,2,4")] = (-2, -6)
    r2 = ev(rows(b2))
    ok2 = (r2["predictions"]["P4"] is False and r2["predictions"]["P6"] is False and verdict(r2["predictions"]) == "PROVED"
           and r2["the least I(W) on K0, by cover [I(W), subspace] (subspaces read alike in both routes)"]["N45"][0] == -2)
    cases = [ok0, ok3, oko, okl, okk, oks, okf, okr, oks2, ok2]
    return {"cases": len(cases), "holds": bool(all(cases)), "each": cases}


def main():
    spec = importlib.util.spec_from_file_location("b1544_run", HERE / "run.py")    # by path, under its own name (E12)
    RUN = importlib.util.module_from_spec(spec)
    sys.modules["b1544_run"] = RUN
    spec.loader.exec_module(RUN)
    rows = [json.loads(x) for x in (HERE / "run.jsonl").read_text().splitlines() if x.strip()]
    taus = {cid: {int(a): int(b) for a, b in v["tau"].items()} for cid, v in RUN.STRUCTURE.items()}
    log = []

    def say(s):
        print(s, flush=True)
        log.append(s)
    res = evaluate(rows, RUN.tasks(), taus, say=say)
    res["verdict"] = verdict(res["predictions"])
    say(f"verdict: {res['verdict']}")
    say(json.dumps({k: v for k, v in res.items() if k != "predictions"}))
    if "--record" in sys.argv:
        (HERE / "read_out.json").write_text(json.dumps(res, indent=1) + "\n")
        (HERE / "read_out_log.txt").write_text("\n".join(log) + "\n")


if __name__ == "__main__":
    main()
