#!/usr/bin/env python3
"""sm:B1551 -- the read-out, run once after run.jsonl is committed unread. evaluate() is pure.

    python3 read_out.py   ->  read_out.json and read_out_log.txt beside this file"""
import json
from collections import Counter

PRIORS = {"P1": 0.97, "P2": 0.90, "P3": 0.93, "P4": 0.95, "P5": 0.92, "P6": 0.97, "P7": 0.55, "P8": 0.40, "P9": 0.25}
ROOM = 4          # n(1) on the spin cover (K5)


def generic(row):
    d = row["draws"]
    if not d:
        return None
    return [min(x["count"][0] for x in d), min(x["count"][1] for x in d)]


def shaped(g):
    return g is not None and g[0] == g[1] < 0


def kind(orb):
    """the three kinds of member orbit the census found"""
    if orb["order"] == 2:
        return "fused sign"
    return "order 4, interior 4" if orb["P"]["n"] >= 4 else "order 4, interior 1"


def evaluate(rows, population, controls, identity_ok):
    out, log = {}, []
    tasks, info = {}, {}
    for oi, orb in enumerate(population["member orbits"]):
        draws = 3 if orb["P"]["n"] >= 2 else 1
        for ch in orb["orbit"]:
            info[tuple(ch)] = (oi, orb, draws)
            for route in ("P", "S"):
                tasks[(route, tuple(ch))] = oi
    seen, by = Counter(), {}
    for r in rows:
        k = (r["route"], tuple(r["character"]))
        seen[k] += 1
        by[k] = r
    complete = set(seen) == set(tasks) and all(v == 1 for v in seen.values()) and \
        all(len(r["draws"]) == info[k[1]][2] for k, r in by.items() if k[1] in info)
    out["complete"] = complete
    out["P1"] = bool(identity_ok and controls.get("all hold"))
    # P2 the routes agree at every member
    p2 = []
    for ch in info:
        a, b = by.get(("P", ch)), by.get(("S", ch))
        if a is None or b is None:
            continue
        sa = (a["structure"]["h1"], a["structure"]["r1"], a["structure"]["n"], a["interior dimension"])
        sb = (b["structure"]["h1"], b["structure"]["r1"], b["structure"]["n"], b["interior dimension"])
        if sa != sb or generic(a) != generic(b):
            p2.append([list(ch), sa, sb, generic(a), generic(b)])
    out["P2"] = complete and not p2
    out["P2 failures"] = p2
    # P3 the orbit law
    p3 = []
    for oi, orb in enumerate(population["member orbits"]):
        for route in ("P", "S"):
            vals = {(by[(route, tuple(ch))]["structure"]["n"], tuple(generic(by[(route, tuple(ch))]) or ()))
                    for ch in orb["orbit"] if (route, tuple(ch)) in by}
            if len(vals) > 1:
                p3.append([oi, route, sorted(map(list, vals))])
    out["P3"] = complete and not p3
    out["P3 failures"] = p3
    # P4 the theorems on S: Theorem C (I(W1) >= -b0 - n(1) = -1 - ROOM; -n <= I(L2) <= 0), Lemma F' with k = 0
    # (I(W1) >= -m_A - 1), the ceiling (I(W1) <= 2 m_A + (4 - m_A) - 1); the structure as the census; gaps clean
    p4 = []
    for k, r in by.items():
        oi, orb, _ = info[k[1]]
        n, mA = r["structure"]["n"], orb["m_A"]
        cen = orb[k[0]]
        if r["interior dimension"] != n or r["m_A (this character)"] != mA or \
                (r["structure"]["h1"], r["structure"]["r1"], n) != (cen["h1"], cen["r1"], cen["n"]):
            p4.append([list(k), "structure, interior dimension or m_A"])
        for x in r["draws"]:
            i1, i2 = x["count"]
            if not (i1 >= -1 - ROOM and i1 >= -mA - 1 and i1 <= mA + 3 and -n <= i2 <= 0):
                p4.append([list(k), x["count"], "a cap"])
            for mod in x["reads"].values():
                for g in mod["gaps"]:
                    if g and g[0] is not None and (g[0] < 1e-20 or g[1] > 1e-25):
                        p4.append([list(k), "gap", g])
        for g in r["structure"]["gaps"]:
            if g and g[0] is not None and (g[0] < 1e-20 or g[1] > 1e-25):
                p4.append([list(k), "gap", g])
    out["P4"] = complete and not p4
    out["P4 failures"] = p4[:50]
    # P5 the draws agree wherever there are several
    p5 = [[list(k), [x["count"] for x in r["draws"]]] for k, r in by.items()
          if len(r["draws"]) > 1 and len({tuple(x["count"]) for x in r["draws"]}) > 1]
    out["P5"] = complete and not p5
    out["P5 failures"] = p5
    # the generic count of every orbit (route P, its first member) and the generation-shaped orbits (both routes, all members)
    orbit_count, shaped_orbits = {}, []
    for oi, orb in enumerate(population["member orbits"]):
        gs = [generic(by[(route, tuple(ch))]) for ch in orb["orbit"] for route in ("P", "S") if (route, tuple(ch)) in by]
        orbit_count[oi] = {"kind": kind(orb), "size": orb["size"], "interior": orb["P"]["n"],
                           "counts": sorted({tuple(g) for g in gs if g})}
        if gs and all(shaped(g) for g in gs):
            shaped_orbits.append(oi)
    out["orbits"] = {str(k): {**v, "counts": [list(c) for c in v["counts"]]} for k, v in orbit_count.items()}
    out["generation-shaped orbits"] = shaped_orbits
    kinds = {oi: kind(orb) for oi, orb in enumerate(population["member orbits"])}
    out["P6"] = complete and not any(kinds[oi] == "order 4, interior 4" for oi in shaped_orbits)
    out["P7"] = complete and not any(kinds[oi] == "order 4, interior 1" for oi in shaped_orbits)
    fused = [oi for oi in kinds if kinds[oi] == "fused sign"]
    out["P8"] = complete and bool(fused) and all(oi in shaped_orbits for oi in fused)
    out["P9"] = bool(out["P6"] and out["P7"] and out["P8"] and len(fused) == 1 and shaped_orbits == fused)
    core = all(out[p] for p in ("P1", "P2", "P3", "P4", "P5")) and complete
    out["verdict"] = "OPEN" if not core else ("PROVED" if out["P9"] else "NEGATIVE")
    out["held"] = [p for p in PRIORS if out.get(p) is True]
    out["expected held"] = round(sum(PRIORS.values()), 2)
    log.append(f"complete {complete}; held {out['held']} of {list(PRIORS)}; verdict {out['verdict']}")
    log.append(f"orbits: {out['orbits']}")
    return out, log


def main():
    from pathlib import Path
    import gzip
    here = Path(__file__).resolve().parent
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
