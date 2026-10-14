#!/usr/bin/env python3
"""B1548 -- THE READ-OUT (PREREGISTRATION.md sections 7 and 9): the predictions from run.jsonl, once.

    python3 read_out.py [--record]    ->  read_out.json, read_out_log.txt

evaluate() is pure (control K7 calls it through selftest() on synthetic rows).  Coverage (R87): complete only if every sealed
task (run.tasks(): route R and route F at each of the circle's members) has exactly one row, and each row has run.DRAWS readings at each of its
distinct strata and none elsewhere.  A prediction a row can refute is False on that row whatever the coverage; a
population-wide one is True only on complete records, else None.

A stratum's generic reading is the least I(W1) and the least I(L2W1) over its draws (Lemma G: a generic class has the largest
ranks s and t, so the least of each), with the largest rk delta1_W and the set of the draws' supports.
  P1  the identity held: identity.json says controls K1-K8 reproduce and every sealed file hashes as sealed.
  P2  the routes agree at every member: its order, n(nu^4), structure, every stratum's dimension, the distinct strata, every
      generic reading.
  P3  Galois: in each route the members of every Galois class (run.galois_rep: the automorphisms fixing sqrt 3) read alike
      (n(nu^4), structure, strata, generic readings).
  P4  the theorems at every reading: rk delta1_W = 0 (the class lies in K0); the support lies in U; Lemma F' (I(W1) >= k - 5,
      k the support's size); the caps I(W1) >= -3 and I(L2W1) <= 0.  In route R also every identity and cap of sm:B1536's
      reading (`all`), b0 = 0, n(L) = 3, k = |support| and rk d1(E) = rk delta1_W.  And at every member, in both routes:
      n(L) = n(nu^4) = 3 (the room), X_U inside X_U' whenever U is inside U' (by dimension), and X_{} of the dimension of
      K0's interior part.
  P5  genericity: at every distinct stratum the draws read alike, each with support exactly U.
  P6  the floor: every stratum's generic reading has I(W1) >= -2.
  P7  I(W1) >= 0 at every reading.
  P8  three: some stratum's generic reading is (-3, -3) in both routes.
  P9  the load-bearing checks (route R, at a generic class of K0^nu and of H^1 at every member): every identity and cap of the
      reading (`all`), b0 = 0, n(L) = 3, k = |support|, rk d1(E) = rk delta1_W, Theorem C's cap I(W1) >= rk delta1_W - 3,
      Lemma F' (I(W1) >= k - 5), and rk delta1_W = 0 at K0's class.  They are what excludes three at every class the run does
      not read.
  P10 some stratum's generic reading is generation-shaped, I(W1) = I(L2W1) < 0, in both routes.
Verdict (section 9): PROVED if P1, P2, P4 and P9 hold and P8 is True; NEGATIVE if P1, P2, P4 and P9 hold on complete records
and no stratum's generic reading, in either route, has I(W1) = -3 with I(L2W1) <= -3; OPEN otherwise."""
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def generic(rs):
    return {"count": [min(r["count"][0] for r in rs), min(r["count"][1] for r in rs)],
            "rk delta1_W": max(r["rk delta1_W"] for r in rs), "supports": sorted({tuple(r["support"]) for r in rs})}


def u_set(U):
    return tuple(int(x) for x in U.split(",")) if U else ()


def reading_ok(route, U, r):
    """P4's checks at one reading"""
    k = len(r["support"])
    ok = (r["rk delta1_W"] == 0 and set(r["support"]) <= set(u_set(U)) and r["count"][0] >= k - 5
          and r["count"][0] >= -3 and r["count"][1] <= 0)
    if route == "R":
        ok = ok and (r["all"] is True and r["b0"] == 0 and r["n(L)"] == 3 and r["k"] == k
                     and r["rk d1"]["E"] == r["rk delta1_W"])
    return ok


def distinct(dims):
    """the U with dim X_U > 0 and larger than every X_U' with U' strictly inside U (member_lib.distinct_strata, again)"""
    return sorted(U for U, d in dims.items()
                  if d > 0 and all(d > dims[V] for V in dims if set(u_set(V)) < set(u_set(U))))


def check_ok(name, x):
    """P9 at one load-bearing check reading (route R)"""
    k = len(x["support"])
    return (x["all"] is True and x["b0"] == 0 and x["n(L)"] == 3 and x["k"] == k and x["rk d1"]["E"] == x["rk delta1_W"]
            and x["count"][0] >= x["rk delta1_W"] - 3 and x["count"][0] >= k - 5
            and (name != "K0" or x["rk delta1_W"] == 0))


def member_ok(row):
    """P4's checks at one member: n(L) = 3, the strata nested by dimension, X_{} the interior part of K0, the distinct strata
    as their dimensions say"""
    d = row["strata"]
    nested = all(d[U] <= d[V] for U in d for V in d if set(u_set(U)) <= set(u_set(V)))
    return (row["structure"]["n(L)"] == 3 and row["n(nu^4)"] == 3 and nested
            and d[""] == row["structure"]["dim K0 interior"] and sorted(row["distinct"]) == distinct(d))


def summary(row):
    """what the routes and the Galois conjugates must share"""
    return json.dumps({"order": row["order"], "n(nu^4)": row["n(nu^4)"], "structure": row["structure"],
                       "strata": row["strata"], "distinct": sorted(row["distinct"]),
                       "generic": {U: generic(rs) for U, rs in sorted(row["readings"].items())}}, sort_keys=True)


def evaluate(rows, sealed_tasks, draws, say=print):
    want = set(sealed_tasks)
    got, dup, extra = {}, [], []
    for r in rows:
        t = (r["route"], r["index"])
        if t not in want:
            extra.append(list(t))
            continue
        if t in got:
            dup.append(list(t))
        got[t] = r
    missing = sorted([list(t) for t in want if t not in got])
    shape = [list(t) for t, r in got.items()
             if set(r["readings"]) != set(r["distinct"]) or any(len(v) != draws for v in r["readings"].values())
             or set(r.get("checks", {})) != (({"H1", "K0"} if r["structure"]["dim K0"] > 0 else {"H1"}) if t[0] == "R"
                                              else set())]
    complete = not (missing or dup or extra or shape)
    out = {"tasks": len(want), "rows": len(rows), "complete": complete,
           "coverage problems": {k: v for k, v in (("missing", missing), ("duplicates", dup), ("unexpected", extra),
                                                   ("readings not as the strata", shape)) if v}}

    def whole(found_false):
        return False if found_false else (True if complete else None)
    # P2: the routes at each member
    idx = sorted({i for _, i in got})
    keyclash, disagree = [], []
    for i in idx:
        a, b = got.get(("R", i)), got.get(("F", i))
        if a is None or b is None:
            continue
        if (a["key"] != b["key"] or a["order"] != b["order"] or a["galois rep"] != b["galois rep"]
                or a["chi0"] != b["chi0"]):
            keyclash.append(i)
        if summary(a) != summary(b):
            disagree.append(i)
    # P3: Galois classes in each route
    gal = {}
    for (route, i), r in got.items():
        gal.setdefault((route, r["order"], r["galois rep"]), set()).add(summary(r))
    gal_bad = sorted({(m, g) for (_, m, g), v in gal.items() if len(v) > 1})
    sizes = Counter(len([1 for (rt, i), r in got.items() if rt == route and r["order"] == m and r["galois rep"] == g])
                    for route, m, g in gal)
    # P4, P5 and the readings
    bad_read, bad_member, not_generic, bad_check, check_low = [], [], [], [], []
    least, gens, zero_or_more, three, undecided, low, shaped = None, {}, True, {}, [], [], {}
    for (route, i), r in got.items():
        if not member_ok(r):
            bad_member.append([route, i])
        for name, x in r.get("checks", {}).items():
            if route != "R" or not check_ok(name, x):
                bad_check.append([route, i, name])
            if x["count"][0] <= -3:
                check_low.append([route, i, name, x["count"]])
        for U, rs in r["readings"].items():
            for x in rs:
                if not reading_ok(route, U, x):
                    bad_read.append([route, i, U])
                if x["count"][0] < 0:
                    zero_or_more = False
            if len({tuple(x["count"]) for x in rs}) > 1 or any(tuple(x["support"]) != u_set(U) for x in rs):
                not_generic.append([route, i, U])
            g = generic(rs)
            gens[(route, i, U)] = g
            c = g["count"]
            least = c[0] if least is None else min(least, c[0])
            if c[0] <= -2:
                low.append([route, i, r["key"], U, c])
            if c[0] == -3 and c[1] == -3:
                three.setdefault((i, U), set()).add(route)
            if c[0] == c[1] < 0:
                shaped.setdefault((i, U), set()).add(route)
            if c[0] == -3 and c[1] < -3:
                undecided.append([route, i, r["key"], U, c])
    pred = {"P1": None}
    pred["P2"] = False if (keyclash or disagree) else (True if complete else None)
    pred["P3"] = False if gal_bad else (True if complete else None)
    pred["P4"] = False if (bad_read or bad_member) else (True if complete else None)
    pred["P5"] = whole(bool(not_generic))
    pred["P6"] = whole(least is not None and least <= -3)
    pred["P7"] = whole(not zero_or_more)
    both = sorted([i, U] for (i, U), routes in three.items() if routes == {"R", "F"})
    pred["P8"] = True if both else (False if complete else None)
    pred["P9"] = whole(bool(bad_check))
    gshaped = sorted([i, U] for (i, U), routes in shaped.items() if routes == {"R", "F"})
    pred["P10"] = True if gshaped else (False if complete else None)
    out.update({"members read": len(idx), "Galois classes per route": dict(Counter(rt for rt, _, _ in gal)),
                "Galois class sizes": dict(sizes), "keys that differ between the routes": keyclash,
                "members where the routes differ": disagree, "Galois classes not read alike": gal_bad,
                "readings failing P4": bad_read, "members failing P4": bad_member, "strata not read alike by their draws":
                not_generic, "the least generic I(W1)": least, "strata with generic I(W1) <= -2": low,
                "strata with generic (-3, -3)": [[i, U, sorted(rt)] for (i, U), rt in sorted(three.items())],
                "strata with generic I(W1) = -3 and I(L2W1) < -3": undecided,
                "strata with a generation-shaped generic reading (both routes)": [
                    [i, U, gens[("R", i, U)]["count"]] for i, U in gshaped],
                "load-bearing checks failing P9": bad_check, "load-bearing check readings at I(W1) <= -3": check_low,
                "load-bearing check readings": sum(len(r.get("checks", {})) for r in got.values())})
    # descriptive: the members by structure, the strata, the generic readings
    by_struct = Counter()
    by_strata = Counter()
    by_count = Counter()
    for (route, i), r in got.items():
        if route != "R":
            continue
        s = r["structure"]
        by_struct[json.dumps([r["order"], s["h1(nu^5 rho)"], s["n(nu^5 rho)"], s["dim K0"], s["dim K0 interior"]])] += 1
        by_strata[json.dumps([r["order"], sorted(r["distinct"], key=lambda U: (len(U), U))])] += 1
        for U in r["readings"]:
            by_count[json.dumps([r["order"], len(u_set(U)), gens[("R", i, U)]["count"]])] += 1
    out["route R: members by (order, h1, n, dim K0, dim K0 interior)"] = dict(sorted(by_struct.items()))
    out["route R: members by (order, their distinct strata)"] = dict(sorted(by_strata.items()))
    out["route R: strata by (order, |U|, generic count)"] = dict(sorted(by_count.items()))
    out["readings"] = {rt: sum(len(v) for (r_, i), r in got.items() if r_ == rt for v in r["readings"].values())
                       for rt in ("R", "F")}
    out["predictions"] = pred
    return out


def verdict(res):
    p = res["predictions"]
    if not all(p[k] is True for k in ("P1", "P2", "P4", "P9")):
        return "OPEN"
    if p["P8"] is True:
        return "PROVED"
    if res["complete"] and not res["strata with generic I(W1) = -3 and I(L2W1) < -3"] and not any(
            c[0] == -3 and c[1] <= -3 for _, _, _, _, c in res["strata with generic I(W1) <= -2"]):
        return "NEGATIVE"
    return "OPEN"


def selftest():
    """synthetic rows: the logic of evaluate() and verdict() on cases built to each outcome"""
    labels = (0, 1, 2, 4, 5)
    import itertools
    Us = [",".join(map(str, U)) for size in range(3) for U in itertools.combinations(labels, size)]

    def row(route, i, gen_count=(0, -2), dist=("",), draws=3, struct_dims=2, rk=0, supp=None, all_ok=True, key=None,
            check_count=(0, -2)):
        dims = {U: struct_dims + (1 if "0" in dist and 0 in u_set(U) else 0) for U in Us}
        s = {"h1(nu^5 rho)": 9, "n(nu^5 rho)": 4, "h1(L)": 8, "n(L)": 3, "dim K0": 5, "dim K0 interior": struct_dims}
        rd = {}
        for U in dist:
            rr = []
            for d in range(draws):
                x = {"count": list(gen_count), "rk delta1_W": rk, "support": list(u_set(U)) if supp is None else supp}
                if route == "R":
                    x.update({"all": all_ok, "b0": 0, "n(L)": 3, "k": len(x["support"]), "rk d1": {"E": rk}})
                rr.append(x)
            rd[U] = rr
        k = key or f"k{i}"
        checks = {}
        if route == "R":
            base = {"count": [0, -2], "rk delta1_W": 0, "support": [0, 1, 2, 4, 5], "all": True, "b0": 0, "n(L)": 3, "k": 5,
                    "rk d1": {"E": 0}}
            checks = {"H1": dict(base, count=list(check_count)), "K0": dict(base)} if s["dim K0"] > 0 else {"H1": dict(base)}
        return {"route": route, "index": i, "order": 8, "n(nu^4)": 3, "key": k, "galois rep": f"g{i // 4}", "chi0": "c0",
                "structure": s,
                "strata": dims, "distinct": list(dist), "readings": rd, "checks": checks}

    tasks = [(rt, i) for i in range(8) for rt in ("R", "F")]

    def run(mod=None, drop=None, extra=None):
        rows = []
        for rt, i in tasks:
            if drop == (rt, i):
                continue
            kw = mod(rt, i) if mod else {}
            rows.append(row(rt, i, **(kw or {})))
        if extra:
            rows.append(extra)
        res = evaluate(rows, tasks, 3, say=lambda s: None)
        res["predictions"]["P1"] = True
        return res, verdict(res)

    cases = []
    r, v = run()
    cases.append(("all floor", v == "NEGATIVE" and r["predictions"]["P6"] is True and r["predictions"]["P8"] is False
                   and r["predictions"]["P7"] is True and r["predictions"]["P2"] is True and r["predictions"]["P5"] is True))
    r, v = run(lambda rt, i: {"gen_count": (-3, -3)} if i in (4, 5, 6, 7) else None)
    cases.append(("three", v == "PROVED" and r["predictions"]["P8"] is True and r["predictions"]["P6"] is False))
    r, v = run(lambda rt, i: {"gen_count": (-3, -4)} if i in (4, 5, 6, 7) else None)
    cases.append(("undecided", v == "OPEN" and r["predictions"]["P8"] is False))
    r, v = run(lambda rt, i: {"gen_count": (-3, -2)} if i in (4, 5, 6, 7) else None)
    cases.append(("room in W only", v == "NEGATIVE" and r["predictions"]["P6"] is False))
    r, v = run(lambda rt, i: {"gen_count": (-1, -2)} if (rt, i) == ("F", 2) else None)
    cases.append(("routes differ", v == "OPEN" and r["predictions"]["P2"] is False and r["predictions"]["P3"] is False))
    r, v = run(drop=("F", 3))
    cases.append(("missing", v == "OPEN" and r["complete"] is False and r["predictions"]["P6"] is None))
    r, v = run(lambda rt, i: {"all_ok": False} if (rt, i) == ("R", 1) else None)
    cases.append(("failed identity", v == "OPEN" and r["predictions"]["P4"] is False))
    r, v = run(lambda rt, i: {"rk": 1} if i == 0 else None)
    cases.append(("outside K0", v == "OPEN" and r["predictions"]["P4"] is False))
    r, v = run(lambda rt, i: {"gen_count": (-1, -2)} if i == 1 else None)
    cases.append(("Galois differs", v == "NEGATIVE" and r["predictions"]["P3"] is False and r["predictions"]["P2"] is True))
    r, v = run(lambda rt, i: {"dist": ("", "0"), "supp": [1]} if i == 2 else None)
    cases.append(("support outside U", v == "OPEN" and r["predictions"]["P4"] is False))
    r, v = run(lambda rt, i: {"dist": ("", "0")} if i in (0, 1, 2, 3) else None)
    cases.append(("a stratum off the interior", v == "NEGATIVE" and r["readings"] == {"R": 36, "F": 36}))
    odd = row("R", 0)
    odd["distinct"] = ["", "1"]
    odd["readings"]["1"] = [dict(x, support=[1], k=1) for x in odd["readings"][""]]
    r, v = run(drop=("R", 0), extra=odd)
    cases.append(("distinct strata not as the dimensions say", v == "OPEN" and r["predictions"]["P4"] is False))
    r, v = run(lambda rt, i: {"draws": 2} if (rt, i) == ("R", 5) else None)
    cases.append(("short stratum", v == "OPEN" and r["complete"] is False))
    r, v = run(extra=row("R", 3))
    cases.append(("duplicate", v == "OPEN" and r["complete"] is False))
    r, v = run(lambda rt, i: {"gen_count": (-4, -1)} if i == 6 else None)
    cases.append(("below the cap", v == "OPEN" and r["predictions"]["P4"] is False))
    r, v = run(lambda rt, i: {"dist": (), "struct_dims": 0} if i < 4 else None)
    cases.append(("no strata at some members", v == "NEGATIVE" and r["readings"] == {"R": 12, "F": 12}))
    r, v = run(lambda rt, i: {"gen_count": (-1, -2)})
    cases.append(("I(W1) = -1 everywhere", v == "NEGATIVE" and r["predictions"]["P7"] is False
                  and r["predictions"]["P6"] is True))
    r, v = run(lambda rt, i: (dict({"dist": ("", "0")}, **({"supp": []} if rt == "F" else {}))) if i == 6 else None)
    cases.append(("a draw off U's support", r["predictions"]["P5"] is False and r["predictions"]["P2"] is False))
    r, v = run(lambda rt, i: {"gen_count": (-1, -1)} if i in (0, 1, 2, 3) else None)
    cases.append(("one generation-shaped stratum", v == "NEGATIVE" and r["predictions"]["P10"] is True
                  and r["predictions"]["P8"] is False))
    r, v = run(lambda rt, i: {"check_count": (-3, -1)} if i == 3 else None)
    cases.append(("a load-bearing check below Lemma F'", v == "OPEN" and r["predictions"]["P9"] is False))
    r, v = run(lambda rt, i: {"gen_count": (-3, -3), "check_count": (-3, 0)} if i == 3 else None)
    cases.append(("three with a check failing", v == "OPEN" and r["predictions"]["P9"] is False))
    odd2 = row("F", 5)
    odd2["n(nu^4)"] = 1
    r, v = run(drop=("F", 5), extra=odd2)
    cases.append(("a member without room three", v == "OPEN" and r["predictions"]["P4"] is False))
    return {"cases": len(cases), "failed": [n for n, ok in cases if not ok], "holds": all(ok for _, ok in cases)}


def load(name, path):
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    return sys.modules[name]


def rows_of(V):
    p = V / "run.jsonl"
    if p.exists():
        text = p.read_text()
    else:
        import gzip
        text = gzip.decompress((V / "run.jsonl.gz").read_bytes()).decode()
    return [json.loads(x) for x in text.splitlines() if x.strip()]


def main():
    log = []

    def say(s):
        log.append(s)
        print(s)
    st = selftest()
    say(f"selftest: {st}")
    assert st["holds"], st
    run = load("b1548_run_ro", HERE / "run.py")
    res = evaluate(rows_of(HERE), run.tasks(), run.DRAWS, say)
    ident = json.loads((HERE / "identity.json").read_text()) if (HERE / "identity.json").exists() else {}
    res["predictions"]["P1"] = bool(ident.get("identity holds"))
    res["verdict"] = verdict(res)
    for k in sorted(res["predictions"], key=lambda x: int(x[1:])):
        say(f"{k}: {res['predictions'][k]}")
    say(f"verdict: {res['verdict']}")
    say(json.dumps({k: v for k, v in res.items() if k not in ("predictions", "verdict")}))
    res["log"] = log
    if "--record" in sys.argv:
        (HERE / "read_out.json").write_text(json.dumps(res, indent=1) + "\n")
        (HERE / "read_out_log.txt").write_text("\n".join(log) + "\n")
    return res


if __name__ == "__main__":
    main()
