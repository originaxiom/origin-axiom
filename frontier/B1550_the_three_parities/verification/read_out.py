#!/usr/bin/env python3
"""sm:B1550 -- the read-out, run once after run.jsonl is committed unread. evaluate() is pure.

    python3 read_out.py   ->  read_out.json and read_out_log.txt beside this file"""
import json
from collections import Counter

PRIORS = {"P1": 0.97, "P2": 0.90, "P3": 0.93, "P4": 0.95, "P5": 0.92, "P6": 0.95, "P7": 0.70, "P8": 0.65, "P9": 0.70}
ROOT, PARTNER = "+LR", "-LR"


def generic(row):
    """a task's generic count: the draws must agree (P5); the least I(W1) and the least I(Lambda^2) otherwise"""
    d = row["draws"]
    if not d:
        return None
    return [min(x["count"][0] for x in d), min(x["count"][1] for x in d)]


def shaped(g):
    return g is not None and g[0] == g[1] < 0


def evaluate(rows, population, controls, identity_ok):
    out, log = {}, []
    tasks, info = {}, {}
    for oi, orb in enumerate(population["member orbits"]):
        for ch in orb["orbit"]:
            info[(orb["state"], tuple(ch))] = (oi, orb, orb["members"][json.dumps(ch)])
            for route in ("P", "S"):
                tasks[(route, orb["state"], tuple(ch))] = oi
    seen = Counter()
    by = {}
    for r in rows:
        k = (r["route"], r["state"], tuple(r["character"]))
        seen[k] += 1
        by[k] = r
    complete = set(seen) == set(tasks) and all(v == 1 for v in seen.values()) and \
        all(len(r["draws"]) == 3 for r in by.values())
    out["complete"] = complete
    # P1 the identity and the controls
    out["P1"] = bool(identity_ok and controls.get("all hold"))
    # P2 the routes agree at every member: (h1, r1, n), the interior dimension and the generic count
    p2_bad = []
    for (sw, ch) in info:
        a, b = by.get(("P", sw, ch)), by.get(("S", sw, ch))
        if a is None or b is None:
            continue
        sa = (a["structure"]["h1"], a["structure"]["r1"], a["structure"]["n"], a["interior dimension"])
        sb = (b["structure"]["h1"], b["structure"]["r1"], b["structure"]["n"], b["interior dimension"])
        if sa != sb or generic(a) != generic(b):
            p2_bad.append([sw, list(ch), sa, sb, generic(a), generic(b)])
    out["P2"] = complete and not p2_bad
    out["P2 failures"] = p2_bad
    # P3 the A4 orbit law: in each route every member of an orbit reads alike (structure and generic count)
    p3_bad = []
    for oi, orb in enumerate(population["member orbits"]):
        for route in ("P", "S"):
            vals = set()
            for ch in orb["orbit"]:
                r = by.get((route, orb["state"], tuple(ch)))
                if r is not None:
                    vals.add((r["structure"]["h1"], r["structure"]["r1"], r["structure"]["n"], tuple(generic(r) or ())))
            if len(vals) > 1:
                p3_bad.append([orb["state"], oi, route, sorted(map(list, vals))])
    out["P3"] = complete and not p3_bad
    out["P3 failures"] = p3_bad
    # P4 the theorems at every reading (Theorem C: I(W1) >= -b0 - n(1) = -1, -n(nu^3 rho) = -n <= I(L2) <= 0; Lemma F':
    # I(W1) >= -m_A - 1; the ceiling: I(W1) <= 2 m_A + m_B - b0 = m_A + 3 with m_B = 4 - m_A), the structure as the census,
    # every gap clean
    p4_bad = []
    for k, r in by.items():
        oi, orb, mem = info[(k[1], k[2])]
        mA, n = mem["m_A"], r["structure"]["n"]
        cen = orb[k[0]]
        if r["interior dimension"] != n or r["m_A (this character)"] != mA or \
                (r["structure"]["h1"], r["structure"]["r1"], n) != (cen["h1"], cen["r1"], cen["n"]):
            p4_bad.append([list(k), "structure, interior dimension or m_A"])
        for x in r["draws"]:
            i1, i2 = x["count"]
            if not (i1 >= -1 and i1 >= -mA - 1 and i1 <= mA + 3 and -n <= i2 <= 0):
                p4_bad.append([list(k), x["count"], "a cap"])
            for mod in x["reads"].values():
                for g in mod["gaps"]:
                    if g and g[0] is not None and (g[0] < 1e-20 or g[1] > 1e-25):
                        p4_bad.append([list(k), "gap", g])
        for g in r["structure"]["gaps"]:
            if g and g[0] is not None and (g[0] < 1e-20 or g[1] > 1e-25):
                p4_bad.append([list(k), "gap", g])
    out["P4"] = complete and not p4_bad
    out["P4 failures"] = p4_bad[:50]
    # P5 genericity: the three draws read alike at every task
    p5_bad = [[list(k), [x["count"] for x in r["draws"]]] for k, r in by.items()
              if len({tuple(x["count"]) for x in r["draws"]}) > 1]
    out["P5"] = complete and not p5_bad
    out["P5 failures"] = p5_bad
    # the generation-shaped members: generation-shaped in both routes
    gs = {}
    for (sw, ch), (oi, orb, mem) in info.items():
        a, b = by.get(("P", sw, ch)), by.get(("S", sw, ch))
        if a and b and shaped(generic(a)) and shaped(generic(b)):
            gs[(sw, ch)] = generic(a)
    out["generation-shaped members"] = sorted([sw, list(ch), g, info[(sw, ch)][2]["label"], info[(sw, ch)][1]["order"]]
                                              for (sw, ch), g in gs.items())
    # P6 every sign member of the root reads (-1, -1) in both routes
    root_sign = [(sw, ch) for (sw, ch), (oi, orb, mem) in info.items() if sw == ROOT and orb["order"] == 2]
    p6_bad = [[list(ch), generic(by.get((rt, sw, ch)) or {"draws": []})] for (sw, ch) in root_sign for rt in ("P", "S")
              if generic(by.get((rt, sw, ch)) or {"draws": []}) != [-1, -1]]
    out["P6"] = complete and len(root_sign) == 24 and not p6_bad
    out["P6 failures"] = p6_bad
    # P7 no order-4 member of the root is generation-shaped (in either route)
    p7_bad = [[list(ch), rt, generic(by[(rt, sw, ch)])] for (sw, ch), (oi, orb, mem) in info.items()
              if sw == ROOT and orb["order"] == 4 for rt in ("P", "S")
              if (rt, sw, ch) in by and shaped(generic(by[(rt, sw, ch)]))]
    out["P7"] = complete and not p7_bad
    out["P7 failures"] = p7_bad
    # P8 THE THREE: the root's generation-shaped members are exactly its 24 sign members; each has an edge's label; eight
    # carry each non-zero parity; and the golden map, which carries generation-shaped members to generation-shaped
    # members, permutes the three labels as a 3-cycle
    root_gs = {ch for (sw, ch) in gs if sw == ROOT}
    labels = Counter(tuple(info[(ROOT, ch)][2]["label"] or ()) for ch in root_gs)
    lab_map, closed = {}, True
    for ch in root_gs:
        orb = info[(ROOT, ch)][1]
        img = tuple(orb["golden"][json.dumps(list(ch))])
        if img not in root_gs:
            closed = False
            continue
        a, b = tuple(info[(ROOT, ch)][2]["label"] or ()), tuple(info[(ROOT, img)][2]["label"] or ())
        lab_map.setdefault(a, set()).add(b)
    cyc = (len(lab_map) == 3 and all(len(v) == 1 for v in lab_map.values()) and
           all(next(iter(v)) != k for k, v in lab_map.items()) and len({next(iter(v)) for v in lab_map.values()}) == 3)
    out["labels on the root"] = {str(list(k)): v for k, v in labels.items()}
    out["the golden map on the labels"] = {str(list(k)): [list(x) for x in v] for k, v in lab_map.items()}
    out["P8"] = bool(complete and out["P6"] and out["P7"] and root_gs == {ch for (sw, ch) in root_sign} and
                     sorted(labels.values()) == [8, 8, 8] and () not in labels and closed and cyc)
    # P9 the family: -LR's sign members are not generation-shaped, so of the four tetrahedral covers only the root's
    # carries generation-shaped members
    others = sorted({sw for (sw, ch) in gs if sw != ROOT})
    out["states with generation-shaped members"] = sorted({sw for (sw, ch) in gs})
    out["P9"] = complete and not others
    # the verdict (section 9)
    core = all(out[p] for p in ("P1", "P2", "P3", "P4", "P5")) and complete
    out["verdict"] = "OPEN" if not core else ("PROVED" if out["P8"] else "NEGATIVE")
    held = [p for p in PRIORS if out.get(p) is True]
    out["held"] = held
    out["expected held"] = round(sum(PRIORS.values()), 2)
    tab = Counter()
    for k, r in by.items():
        oi, orb, mem = info[(k[1], k[2])]
        tab[(r["route"], r["state"], orb["order"], orb["size"], mem["m_A"], r["structure"]["n"],
             tuple(generic(r) or ()))] += 1
    out["generic counts by (route, state, order, orbit size, m_A, n, count)"] = {str(list(k)): v
                                                                                 for k, v in sorted(tab.items())}
    log.append(f"complete {complete}; held {held} of {list(PRIORS)}; verdict {out['verdict']}")
    log.append(f"states with generation-shaped members: {out['states with generation-shaped members']}")
    log.append(f"labels on the root: {out['labels on the root']}; the golden map on them: "
               f"{out['the golden map on the labels']}")
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
