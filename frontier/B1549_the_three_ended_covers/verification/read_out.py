#!/usr/bin/env python3
"""sm:B1549 -- the read-out, run once after run.jsonl is committed unread. evaluate() is pure.

    python3 read_out.py   ->  read_out.json and read_out_log.txt beside this file"""
import json
from collections import Counter, defaultdict

PRIORS = {"P1": 0.97, "P2": 0.90, "P3": 0.93, "P4": 0.95, "P5": 0.92, "P6": 0.80, "P7": 0.55, "P8": 0.25}


def generic(row):
    """a task's generic count: the draws must agree (P5); the least I(W1) and the least I(Lambda^2) otherwise"""
    d = row["draws"]
    if not d:
        return None
    return [min(x["count"][0] for x in d), min(x["count"][1] for x in d)]


def evaluate(rows, population, controls, identity_ok):
    out, log = {}, []
    tasks = {}
    for oi, orb in enumerate(population["member orbits"]):
        for ch in orb["orbit"]:
            for route in ("P", "S"):
                tasks[(route, orb["state"], tuple(orb["lattice"]), orb["wbar"], tuple(ch))] = (oi, orb)
    seen = Counter()
    by = {}
    for r in rows:
        k = (r["route"], r["state"], tuple(r["lattice"]), r["wbar"], tuple(r["character"]))
        seen[k] += 1
        by[k] = r
    complete = set(seen) == set(tasks) and all(v == 1 for v in seen.values()) and \
        all(len(r["draws"]) == 3 for r in by.values())
    out["complete"] = complete
    # P1 identity and controls
    out["P1"] = bool(identity_ok and controls.get("all hold"))
    # P2 routes agree at every member: structure (h1, r1, n), interior dimension and generic count
    p2_bad = []
    for (route, sw, lat, wl, ch), (oi, orb) in tasks.items():
        if route != "P":
            continue
        a, b = by.get(("P", sw, lat, wl, ch)), by.get(("S", sw, lat, wl, ch))
        if a is None or b is None:
            continue
        sa = (a["structure"]["h1"], a["structure"]["r1"], a["structure"]["n"], a["interior dimension"])
        sb = (b["structure"]["h1"], b["structure"]["r1"], b["structure"]["n"], b["interior dimension"])
        if sa != sb or generic(a) != generic(b):
            p2_bad.append([sw, list(lat), wl, list(ch), sa, sb, generic(a), generic(b)])
    out["P2"] = (not p2_bad) and complete if not p2_bad else False
    out["P2 failures"] = p2_bad
    # P3 orbit law: in each route, every member of an orbit reads alike (structure and generic count)
    p3_bad = []
    for oi, orb in enumerate(population["member orbits"]):
        for route in ("P", "S"):
            vals = set()
            for ch in orb["orbit"]:
                r = by.get((route, orb["state"], tuple(orb["lattice"]), orb["wbar"], tuple(ch)))
                if r is not None:
                    vals.add((r["structure"]["h1"], r["structure"]["r1"], r["structure"]["n"], tuple(generic(r) or ())))
            if len(vals) > 1:
                p3_bad.append([orb["state"], orb["lattice"], orb["wbar"], oi, route, sorted(map(list, vals))])
    out["P3"] = (not p3_bad) and complete if not p3_bad else False
    out["P3 failures"] = p3_bad
    # P4 theorems at every reading: Theorem C's caps (I(W1) >= -1 since b0 = 1 and n(1) = 0; I(L2) in [-n(nu^3 rho), 0],
    # n(nu^3 rho) = n(nu rho) at these characters), Lemma F' (I(W1) >= k - m_A - b0 = -m_A - 1), the ceiling
    # (I(W1) <= 2 m_A + m_B - b0 with m_B = 3 - m_A), the structure as the census, the gaps clean
    p4_bad = []
    for k, r in by.items():
        mA = r["m_A (this character)"]
        n = r["structure"]["n"]
        if r["interior dimension"] != n or r["m_A (this character)"] != r["m_A"]:
            p4_bad.append([list(k), "interior dimension or m_A"])
        for x in r["draws"]:
            i1, i2 = x["count"]
            if not (i1 >= -1 and i1 >= -mA - 1 and i1 <= 2 * mA + (3 - mA) - 1 and -n <= i2 <= 0):
                p4_bad.append([list(k), x["count"], "a cap"])
            for mod in x["reads"].values():
                for g in mod["gaps"]:
                    if g and g[0] is not None and (g[0] < 1e-20 or g[1] > 1e-25):
                        p4_bad.append([list(k), "gap", g])
    out["P4"] = (not p4_bad) and complete if not p4_bad else False
    out["P4 failures"] = p4_bad[:50]
    # P5 genericity: the three draws read alike at every task
    p5_bad = [[list(k), [x["count"] for x in r["draws"]]] for k, r in by.items()
              if len({tuple(x["count"]) for x in r["draws"]}) > 1]
    out["P5"] = (not p5_bad) and complete if not p5_bad else False
    out["P5 failures"] = p5_bad
    # P6 main's law: every generic reading has I(W1) = -1
    p6_bad = [[list(k), generic(r)] for k, r in by.items() if generic(r) is not None and generic(r)[0] != -1]
    out["P6"] = (not p6_bad) and complete if not p6_bad else False
    out["P6 failures"] = p6_bad
    # P7 the shape follows the square: order 2 -> (-1, -1), order 4 -> (-1, 0)
    p7_bad = []
    for k, r in by.items():
        g = generic(r)
        want = [-1, -1] if r["order"] == 2 else ([-1, 0] if r["order"] == 4 else None)
        if g is not None and g != want:
            p7_bad.append([list(k), r["order"], g])
    out["P7"] = (not p7_bad) and complete if not p7_bad else False
    out["P7 failures"] = p7_bad
    # the generation-shaped members by cover (both routes generation-shaped)
    gs = defaultdict(list)
    for (oi, orb) in {v[0]: v[1] for v in tasks.values()}.items():
        for ch in orb["orbit"]:
            a = by.get(("P", orb["state"], tuple(orb["lattice"]), orb["wbar"], tuple(ch)))
            b = by.get(("S", orb["state"], tuple(orb["lattice"]), orb["wbar"], tuple(ch)))
            if a and b and generic(a) and generic(b) and generic(a)[0] == generic(a)[1] < 0 and \
                    generic(b)[0] == generic(b)[1] < 0:
                gs[(orb["state"], tuple(orb["lattice"]), orb["wbar"])].append({"character": ch, "orbit index": oi,
                                                                             "count": generic(a)})
    out["generation-shaped members by cover"] = {f"{k[0]} {list(k[1])} w{k[2]}": v for k, v in gs.items()}
    exactly_three = sorted(f"{k[0]} {list(k[1])} w{k[2]}" for k, v in gs.items() if len(v) == 3)
    out["covers with exactly three generation-shaped members"] = exactly_three
    lllr = [c for c in exactly_three if c.startswith("+LLLR ")]
    out["P8"] = complete and len(exactly_three) == 1 and len(lllr) == 1
    # the verdict (section 9)
    core = all(out[p] for p in ("P1", "P2", "P3", "P4", "P5")) and complete
    if not core:
        out["verdict"] = "OPEN"
    elif out["P8"]:
        out["verdict"] = "PROVED"
    else:
        out["verdict"] = "NEGATIVE"
    held = [p for p in PRIORS if out.get(p) is True]
    out["held"] = held
    out["expected held"] = round(sum(PRIORS.values()), 2)
    # tables
    tab = Counter()
    for k, r in by.items():
        tab[(r["route"], r["state"], r["order"], r["m_A"], r["structure"]["n"], tuple(generic(r) or ()))] += 1
    out["generic counts by (route, state, order, m_A, n, count)"] = {str(list(k)): v for k, v in sorted(tab.items())}
    log.append(f"complete {complete}; held {held} of {list(PRIORS)}; verdict {out['verdict']}")
    log.append(f"covers with exactly three generation-shaped members: {exactly_three}")
    return out, log


def main():
    from pathlib import Path
    here = Path(__file__).resolve().parent
    import gzip
    raw = here / "run.jsonl"
    lines = raw.read_text().splitlines() if raw.exists() else gzip.open(str(raw) + ".gz", "rt").read().splitlines()
    rows = [json.loads(x) for x in lines if x.strip()]
    population = json.loads((here / "population.json").read_text())
    controls = json.loads((here / "controls.json").read_text())
    identity = json.loads((here / "identity.json").read_text())
    out, log = evaluate(rows, population, controls, identity.get("holds", False))
    (here / "read_out.json").write_text(json.dumps(out, indent=1) + "\n")
    (here / "read_out_log.txt").write_text("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    main()
