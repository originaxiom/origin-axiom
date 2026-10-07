#!/usr/bin/env python3
"""W13 of the weave: main's F-CI orbits of three at the weave's resolving tick, read with this seat's own engine.

Main's B1434 (the architecture census, sealed 2026-10-01) carries the E6/27 frame (F-CI) to every signed word state to
length six. At the three-fold level it finds generation-shaped backgrounds in deck orbits of three on ten of the twelve
levels in range. All six odd-trace states in range carry them. This script reads four of those rows (+-LR, +-LLLR) with
this seat's code: sm:B1506's census engine (`frontier/B1506_the_level/verification/the_level.py`, built on sm:B1374's index_lib), carried
from m004's tower to any state's mapping torus.

The presentation of a state's level n: <a, b, t | t x t^-1 = phi^n(x)>, with phi the state's automorphism in the weave's
marking (the dossier's word_aut), the peripheral pair (u^-1 t, [a, b]) with phi^n([a, b]) = u [a, b] u^-1, and the deck
x -> phi(x), t -> t. Everything else is sm:B1506's engine unchanged:
  - the loci (characters with h^1 = 1) and every candidate module;
  - the index at three primes, each firing module re-checked at the other two;
  - the generation-shaped backgrounds (the five charged sectors equal and non-zero), their lifts and deck orbits.

The comparison is with B1434's banked table (main, `frontier/B1434_the_architecture_census/FINDINGS.md`, section 2b):
backgrounds, of which lift, and of which carry nu^c with the generation's sign.

The two remaining rows, +-LLLLLR, cost about an hour each on this engine; W14 (`the_slope_law.py`) reads all six rows,
and the six odd-trace states beyond B1434's range, through the slope law, and its census agrees with every B1434 row.

    python3 the_class_index_orbits.py   ->  the_class_index_orbits.json beside it (the four states in parallel)
"""
import importlib.util
import json
import sys
import time
from collections import defaultdict
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "frontier" / "B1552_the_chiral_triplets_count" / "verification"))
import chiral_lib as CL  # noqa: E402  (the moves in the weave's marking, powers, the peripheral word)

CP = CL.CP
_spec = importlib.util.spec_from_file_location("b1506_the_level",
                                               ROOT / "frontier" / "B1506_the_level" / "verification" / "the_level.py")
LV = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(LV)
IL = LV.IL

# main's B1434, section 2(b): state -> (backgrounds, of which lift, nu^c with the generation's sign)
B1434 = {"+LR": (48, 0, 48), "-LR": (96, 0, 0), "+LLLR": (72, 0, 24), "-LLLR": (48, 0, 48),
         "+LLLLLR": (720, 240, 48), "-LLLLLR": (360, 0, 96)}


def to_str(w):
    return "".join({1: "a", 2: "b", -1: "A", -2: "B"}[x] for x in w)


class StatePres:
    """a level of a state's tower, with its characters and the deck on them (sm:B1506's Pres, any state)"""

    def __init__(self, sw, n):
        sign = 1 if sw[0] == "+" else -1
        self.kind, self.n = sw, n
        phi1 = CP.word_aut(sw[1:], sign)
        phin = CL.power(phi1, n)
        u = CL.peripheral_u(phin)
        self.gens = ["a", "b", "t"]
        self.rels = ["taT" + LV.inv(to_str(phin[1])), "tbT" + LV.inv(to_str(phin[2]))]
        self.mu, self.lam = LV.inv(to_str(u)) + "t", "abAB"
        self.deck_img = {"a": to_str(phi1[1]), "b": to_str(phi1[2]), "t": "t"}
        self.words = None
        self.tors, self.free = LV.h1_of(self.gens, self.rels)
        self.e = LV.lcm(*self.tors) if self.tors else 1
        self.N = LV.lcm(12, self.e)
        self.chars = LV.characters(self.gens, self.rels, self.N)
        self.cset = set(self.chars)
        G = self.gens
        self.D = [[IL.abelian_exponents(self.deck_img[g], G)[h] for h in G] for g in G]
        self.mu_ex = [IL.abelian_exponents(self.mu, G)[h] for h in G]
        self.lam_ex = [IL.abelian_exponents(self.lam, G)[h] for h in G]
        self.squares = set(tuple(2 * x % self.N for x in c) for c in self.chars)
        self.sqrt = defaultdict(list)
        self.fifth = defaultdict(list)
        for c in self.chars:
            self.sqrt[tuple(2 * x % self.N for x in c)].append(c)
            self.fifth[tuple(5 * x % self.N for x in c)].append(c)

    val = LV.Pres.val
    pull = LV.Pres.pull
    add = LV.Pres.add


def read(sw, n=3):
    t = time.time()
    P = StatePres(sw, n)
    C = LV.Census(P, verbose=False)
    row, classes = LV.census_summary(C)
    nu_with_sign = sum(1 for Is in classes.values() if Is[5] == Is[0])
    out = {k: row[k] for k in ("H1_torsion", "N", "primes", "hom", "loci", "t1_exceptions", "candidates", "firing",
                               "rechecked", "differing", "deck_invariant_index", "generation_shaped",
                               "generation_shaped_lifted", "background_orbit_sizes", "background_signs",
                               "background_max_abs")}
    out["nu^c with the generation's sign"] = nu_with_sign
    mine = (row["generation_shaped"], row["generation_shaped_lifted"], nu_with_sign)
    out["B1434"] = list(B1434[sw])
    out["agrees with B1434"] = mine == B1434[sw]
    out["seconds"] = round(time.time() - t, 1)
    print(sw, json.dumps(out), flush=True)
    return sw, out


if __name__ == "__main__":
    states = ["+LR", "-LR", "+LLLR", "-LLLR"]
    with Pool(min(4, len(states))) as pool:
        rows = dict(pool.map(read, states))
    res = {"the states (odd trace, in B1434's range; the engine route), tick 3": rows,
           "all agree with B1434": bool(all(r["agrees with B1434"] for r in rows.values())),
           "every background in a deck orbit of three": bool(all(set(r["background_orbit_sizes"]) == {"3"}
                                                                for r in rows.values())),
           "every count one in absolute value": bool(all(r["background_max_abs"] == 1 for r in rows.values())),
           "signs split equally": bool(all(len(set(r["background_signs"].values())) == 1 for r in rows.values()))}
    with open(HERE / "the_class_index_orbits.json", "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps({k: v for k, v in res.items() if not k.startswith("the states")}))
