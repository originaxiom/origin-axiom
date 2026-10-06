#!/usr/bin/env python3
"""B1546 -- THE READ-OUT (PREREGISTRATION.md sections 7 and 9): the predictions from run.jsonl, once.

    python3 read_out.py [--record]    ->  read_out.json, read_out_log.txt

evaluate() is pure (control K4 calls it through selftest() on synthetic rows).  Coverage: complete only if every sealed task
(run.tasks()) has exactly two readings, route F and route R, each once.  A prediction a row can refute is False on that row
whatever the coverage; a population-wide one is True only on complete records, else None.
  P1  one count per subspace (every draw, both routes); the sets S that the deck group carries into one another read one count
      (X:S); Galois-conjugate eigen-lines read one count (u_1..u_4; w_1..w_4; v_a, v_b); and no eigen-line reads an I(W)
      below its family's generic one (u_j below Z1, w_j and v below Z2: Lemma G''').
  P2  the classes: every reading's rk delta1_W and support are the subspace's sealed ones (run.SUBSPACES).
  P3  the identities: route R's at every reading; Lemma F's ingredients in both routes at every reading.
  P4  Lemma M: I(W) <= -1 at every reading of an interior class.
  P5  the floor: I(W) >= -1 at every reading.
  P6  some subspace reads a generation-shaped count, I(W) = I(L2W) != 0, in both routes.
  P7  some subspace reads (-3, -3) in both routes.
  P8  the ten X:S read one count (a lifted mirror carries one deck orbit of the sets S to the other).
Verdict (section 9): PROVED if P1-P4 hold and P7 holds; NEGATIVE if P1-P4 hold on complete records, P7 is False and every
generic family (Z1, Z2, X:S) reads I(W) >= -2; OPEN otherwise."""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENERIC = ("Z1", "Z2")


def is_family(sub):
    return sub in GENERIC or sub.startswith("X:")


def parse_s(sub):
    return tuple(sorted(int(x) for x in sub.split("S=", 1)[1].split(",") if x != ""))


def orbit_key(S, tau):
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


def evaluate(rows, sealed_tasks, subspaces, tau, say=print):
    want = {t: ("F", "R") for t in sealed_tasks}
    got, dup, extra = {}, [], []
    for r in rows:
        key = (r["subspace"], r["draw"])
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
    for (sub, draw), slot in got.items():
        for route, x in slot.items():
            by.setdefault(sub, {}).setdefault(route, set()).add(tuple(x["count"]))
    allc = {sub: set().union(*d.values()) for sub, d in by.items()}
    p1 = all(len(v) == 1 for v in allc.values())
    one = {sub: next(iter(v)) for sub, v in allc.items() if len(v) == 1 and set(by[sub]) == {"F", "R"}}
    groups = {}
    for sub in allc:
        if sub.startswith("X:"):
            groups.setdefault(("tau", orbit_key(parse_s(sub), tau)), set()).update(allc[sub])
        elif sub[0] in "uw":
            groups.setdefault(("galois", sub[0]), set()).update(allc[sub])
        elif sub in ("va", "vb"):
            groups.setdefault(("galois", "v"), set()).update(allc[sub])
    if any(len(v) > 1 for v in groups.values()):
        p1 = False
    semi = []
    for sub, c in one.items():
        fam = "Z1" if sub[0] == "u" else ("Z2" if sub[0] in "wv" else None)
        if fam and fam in one and c[0] < one[fam][0]:
            semi.append([sub, list(c), fam, list(one[fam])])
    if semi:
        p1 = False
    readings = [(sub, route, x) for (sub, draw), slot in got.items() for route, x in slot.items()]
    p2 = all(x["rk delta1_W"] == subspaces[sub]["rank"] and list(x["support"]) == list(subspaces[sub]["support"])
             for sub, route, x in readings)
    p3 = all(lemma_f_holds(x) and (route != "R" or (x.get("all") is True and not x.get("failed")))
             for sub, route, x in readings)
    above = sorted([sub, route, x["count"]] for sub, route, x in readings if not subspaces[sub]["support"] and x["count"][0] > -1)
    below = sorted([sub, route, x["count"]] for sub, route, x in readings if x["count"][0] < -1)
    gen = sorted((sub, c) for sub, c in one.items() if c[0] == c[1] != 0)
    three = [g for g in gen if g[1] == (-3, -3)]
    xs = {c for sub, c in one.items() if sub.startswith("X:")}
    nX = sum(1 for sub in subspaces if sub.startswith("X:"))
    pred = {
        "P1": (p1 if complete else (False if not p1 else None)),
        "P2": (p2 if complete else (False if not p2 else None)),
        "P3": (p3 if complete else (False if not p3 else None)),
        "P4": (False if above else (True if complete else None)),
        "P5": (False if below else (True if complete else None)),
        "P6": (True if gen else (False if complete else None)),
        "P7": (True if three else (False if complete else None)),
        "P8": (False if len(xs) > 1 else (True if complete and len(xs) == 1 and
                                           sum(1 for s in one if s.startswith("X:")) == nX else None)),
    }
    for k, v in pred.items():
        say(f"{k}: {v}")
    fam_least = {sub: list(c) for sub, c in sorted(one.items()) if is_family(sub)}
    lowest = min((c[0] for sub, c in one.items() if is_family(sub)), default=None)
    counts = {sub: {route: sorted([list(c) for c in v]) for route, v in sorted(d.items())} for sub, d in sorted(by.items())}
    mu = {sub: -1 - c[0] for sub, c in sorted(one.items()) if not subspaces[sub]["support"]}
    return {"tasks": len(want), "tasks read in full": sum(1 for k in want if set(got.get(k, {})) == {"F", "R"}),
            "coverage problems": {kk: v for kk, v in (("missing", missing), ("duplicated", dup), ("extra", extra)) if v},
            "complete": complete, "the counts by subspace (route F; route R)": counts,
            "the generic families' counts (read alike in both routes)": fam_least,
            "the least I(W) over the generic families": lowest,
            "the Massey rank mu = -1 - I(W) at the interior subspaces": mu,
            "interior readings above -1 (Lemma M)": above, "readings below the floor": below,
            "eigen-lines below their family (Lemma G''')": semi,
            "generation-shaped subspaces": [[g[0], list(g[1])] for g in gen],
            "three-generation subspaces": [[g[0], list(g[1])] for g in three], "predictions": pred}


def verdict(ev):
    """section 9"""
    pred = ev["predictions"]
    if not all(pred[k] is True for k in ("P1", "P2", "P3", "P4")):
        return "OPEN"
    if pred["P7"] is True:
        return "PROVED"
    fams = ev["the generic families' counts (read alike in both routes)"]
    if pred["P7"] is False and ev["complete"] and fams and all(c[0] >= -2 for c in fams.values()):
        return "NEGATIVE"
    return "OPEN"


def selftest():
    """K4: the read-out's logic on synthetic rows"""
    tau = {0: 1, 1: 4, 4: 2, 2: 5, 5: 0}
    subspaces = {"Z1": {"rank": 1, "support": []}, "Z2": {"rank": 2, "support": []},
                 "X:S=0,1,2": {"rank": 1, "support": [0, 1, 2]}, "X:S=1,4,5": {"rank": 1, "support": [1, 4, 5]},
                 "X:S=0,1,4": {"rank": 1, "support": [0, 1, 4]},
                 "u1": {"rank": 1, "support": []}, "u2": {"rank": 1, "support": []},
                 "w1": {"rank": 2, "support": []}, "w2": {"rank": 2, "support": []},
                 "va": {"rank": 2, "support": []}, "vb": {"rank": 2, "support": []}}
    tasks = [(sub, d) for sub in subspaces for d in range(2)]

    def rows(counts, rk=None, supp=None, lf_bad=None, fail_r=None, drop=0):
        out = []
        for (sub, draw) in tasks:
            for route in ("F", "R"):
                c = counts[sub]
                if isinstance(c, dict):
                    c = c[route]
                S = list(subspaces[sub]["support"]) if not (supp and sub in supp) else supp[sub]
                m, k = 5, len(S)
                lf = {"m": m, "h0(dN;W*)": 2 * m, "h0(dN;W)": 2 * m - k, "r1(W)": 2 * m - 1 - c[0], "h1(dN;W)": 4 * m - k}
                if lf_bad == sub:
                    lf["h0(dN;W*)"] = 2 * m - 1
                x = {"count": list(c), "rk delta1_W": (rk[sub] if rk and sub in rk else subspaces[sub]["rank"]),
                     "support": S, "lemma F": lf}
                if route == "R":
                    bad = fail_r == sub
                    x.update({"all": not bad, "failed": ["cap"] if bad else []})
                out.append({"subspace": sub, "draw": draw, "route": route, "reading": x})
        return out[:len(out) - drop]
    base = {"Z1": (-1, -6), "Z2": (-1, -6), "X:S=0,1,2": (1, -2), "X:S=1,4,5": (1, -2), "X:S=0,1,4": (1, -2),
            "u1": (-1, -4), "u2": (-1, -4), "w1": (-1, -5), "w2": (-1, -5), "va": (-1, -5), "vb": (-1, -5)}
    quiet = lambda s: None  # noqa: E731
    ev = lambda r: evaluate(r, tasks, subspaces, tau, say=quiet)  # noqa: E731
    r0 = ev(rows(base))
    ok0 = (all(r0["predictions"][k] is True for k in ("P1", "P2", "P3", "P4", "P5", "P8"))
           and r0["predictions"]["P6"] is False and r0["predictions"]["P7"] is False and verdict(r0) == "NEGATIVE")
    b = dict(base, Z2=(-3, -3), w1=(-3, -3), w2=(-3, -3))                 # three at the rank-2 family
    r1 = ev(rows(b))
    ok1 = r1["predictions"]["P7"] is True and r1["predictions"]["P5"] is False and verdict(r1) == "PROVED"
    b = dict(base, Z2=(-3, -10))                                         # I(W) = -3 generic, L2W not: undecided
    r2 = ev(rows(b))
    ok2 = r2["predictions"]["P7"] is False and verdict(r2) == "OPEN"
    b = dict(base, **{"X:S=1,4,5": (0, -2)})                              # {0,1,2} and {1,4,5} are one deck orbit
    ok3 = ev(rows(b))["predictions"]["P1"] is False and verdict(ev(rows(b))) == "OPEN"
    b = dict(base, Z1={"F": (-1, -6), "R": (-2, -6)})                     # the routes disagree
    ok4 = ev(rows(b))["predictions"]["P1"] is False
    b = dict(base, u2=(-1, -3))                                          # Galois conjugates disagree
    ok5 = ev(rows(b))["predictions"]["P1"] is False
    b = dict(base, u1=(-2, -4), u2=(-2, -4))                              # an eigen-line below its family
    ok6 = ev(rows(b))["predictions"]["P1"] is False
    ok7 = ev(rows(base, rk={"Z2": 1}))["predictions"]["P2"] is False
    ok8 = ev(rows(base, supp={"X:S=0,1,2": [0, 1]}))["predictions"]["P2"] is False
    ok9 = ev(rows(base, lf_bad="w1"))["predictions"]["P3"] is False and ev(rows(base, fail_r="Z1"))["predictions"]["P3"] is False
    rs = ev(rows(base, drop=1))
    ok10 = rs["predictions"]["P1"] is None and rs["predictions"]["P7"] is None and verdict(rs) == "OPEN"
    b = dict(base, Z1=(0, -6))                                           # an interior class above -1: Lemma M fails
    r11 = ev(rows(b))
    ok11 = r11["predictions"]["P4"] is False and verdict(r11) == "OPEN"
    b = dict(base, **{"X:S=0,1,4": (2, -2)})                              # the two deck orbits differ: P8 only
    r12 = ev(rows(b))
    ok12 = r12["predictions"]["P8"] is False and r12["predictions"]["P1"] is True and verdict(r12) == "NEGATIVE"
    cases = [ok0, ok1, ok2, ok3, ok4, ok5, ok6, ok7, ok8, ok9, ok10, ok11, ok12]
    return {"cases": len(cases), "holds": bool(all(cases)), "each": cases}


def main():
    spec = importlib.util.spec_from_file_location("b1546_run", HERE / "run.py")    # by path, under its own name (E12)
    RUN = importlib.util.module_from_spec(spec)
    sys.modules["b1546_run"] = RUN
    spec.loader.exec_module(RUN)
    rows = [json.loads(x) for x in (HERE / "run.jsonl").read_text().splitlines() if x.strip()]
    log = []

    def say(s):
        log.append(s)
        print(s, flush=True)
    ev = evaluate(rows, RUN.tasks(), RUN.SUBSPACES, RUN.TAU, say=say)
    ev["verdict"] = verdict(ev)
    say(f"verdict: {ev['verdict']}")
    say(json.dumps({k: v for k, v in ev.items() if k != "the counts by subspace (route F; route R)"}))
    if "--record" in sys.argv:
        (HERE / "read_out.json").write_text(json.dumps(ev, indent=1) + "\n")
        (HERE / "read_out_log.txt").write_text("\n".join(log) + "\n")
    return ev


if __name__ == "__main__":
    main()
