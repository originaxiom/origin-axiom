"""(the golden covers dossier, section 6: a draft for the next arc; not sealed, not run) the next arc's population, as structure: the covers of degree <= 12 of m004 and m003 where both supplies
already live at the trivial character (sm:B1536's banked post_run_rooms.json), or where the four alone has two; their H_1; and
the number of own characters of order dividing m (m = 12 on degree 5 and 9, 6 on degree 10), and of cyclic subgroups.
Nothing twisted is computed."""
import importlib.util
import json
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gc_own_chars as O  # noqa: E402

POP = O._load("b1536_population_popd", O.B1536V / "population.py")


def members():
    rooms = json.loads((O.B1536V / "post_run_rooms.json").read_text())
    out = []
    for st in ("m004", "m003"):
        for x in rooms[st]["trivial character supplies"]:
            if (x["n(1)"] >= 1 and x["n(rho)"] >= 1) or x["n(rho)"] >= 2:
                out.append((st, x["cover"], x["degree"], x["n(1)"], x["n(rho)"], x["cusps"]))
    return sorted(out, key=lambda r: (r[0] != "m004", r[2], r[1]))


def modulus(deg):
    return 12 if deg in (5, 9) else 6


def cyclic_subgroups(ab, m):
    """the cyclic subgroups of the characters of order dividing m, each by its lexicographically least generator"""
    seen, reps = set(), []
    for c in ab.characters(m):
        if c in seen:
            continue
        exps = c
        k = 1
        while True:
            pw = tuple((ci * k) % m for ci in exps)
            if not any(pw):
                break
            k += 1
        order = k
        gens = [tuple((ci * j) % m for ci in exps) for j in range(1, order) if gcd(j, order) == 1]
        for g in gens:
            seen.add(g)
        if order > 1:
            reps.append((min(gens), order))
        seen.add(c)
    return reps


def main():
    tot_chars = tot_cyc = 0
    for st, cid, deg, n1, nr, cus in members():
        S = O.CL.state(st)
        covs = dict(POP.covers(S))
        cov = O.R.PCover(S["G"], covs[cid])
        ab = O.Ab(cov)
        m = modulus(deg)
        nch = len(ab.characters(m))
        cyc = cyclic_subgroups(ab, m)
        tot_chars += nch
        tot_cyc += len(cyc)
        by_order = {}
        for _, k in cyc:
            by_order[k] = by_order.get(k, 0) + 1
        print(f"{st} {cid}: degree {deg}, cusps {cus}, (n(1), n(rho)) = ({n1}, {nr}); H_1 = Z^{len(ab.free)} + "
              f"{[d for _, d in ab.torsion]}; m = {m}: {nch} characters, cyclic subgroups by order {dict(sorted(by_order.items()))}")
    print(f"total: {tot_chars} own characters, {tot_cyc} cyclic subgroups")


if __name__ == "__main__":
    main()
