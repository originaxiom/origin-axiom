#!/usr/bin/env python3
"""SM-C1, harvest rows 1420 (UNIVERSAL_SU5_END_AND_RELATIVE_GAUGE_THRESHOLD @ 0a8082283) and 1421
(WILSON_CHARGE_RESOLVED_RELATIVE_THRESHOLD_MAP @ 7dfe63e26): this seat's own exact check. The representations 5, 10 =
wedge^2 5 and 24 are built from the weights of 5; each state carries (colour T3, weak T3, t1 = sqrt(3/5) Y) eigenvalues and
its charge q = 6Y. The normalised index of a factor on a set of states is the sum of its squared eigenvalue
(generators with Tr_5 = 1/2). Exact fractions; t1^2 = (3/5) Y^2."""
import json
import sys
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

# the 5: three colour states (T3c = 1/2, -1/2, 0), two weak states (T3w = 1/2, -1/2); Y = -1/3 colour, +1/2 weak
FIVE = [(F(1, 2), F(0), F(-1, 3)), (F(-1, 2), F(0), F(-1, 3)), (F(0), F(0), F(-1, 3)),
        (F(0), F(1, 2), F(1, 2)), (F(0), F(-1, 2), F(1, 2))]


def wedge2(states):
    return [tuple(a + b for a, b in zip(x, y)) for x, y in combinations(states, 2)]


def adjoint(states):
    # e_i (x) e_j^* for i != j, plus the Cartan: 4 neutral states; their contribution to every index is that of the
    # traceless diagonal generators -- for an index the Cartan states carry zero eigenvalue under any Cartan generator
    out = [tuple(a - b for a, b in zip(states[i], states[j])) for i in range(5) for j in range(5) if i != j]
    return out + [(F(0), F(0), F(0))] * 4


def color_index(states):
    # colour index via the full SU(3) Casimir would need all generators; with one Cartan generator H3 = T3c the index of
    # a representation equals sum of (T3c)^2 over its states (Tr_R H^2 = T(R) for a normalised H)
    return sum(s[0] ** 2 for s in states)


def indices(states):
    return (color_index(states), sum(s[1] ** 2 for s in states), sum(F(3, 5) * s[2] ** 2 for s in states))


REPS = {"5": FIVE, "10": wedge2(FIVE), "24": adjoint(FIVE)}
out = {"row1420_indices": {}, "row1421": {}}
for name, st in REPS.items():
    c, w, h = indices(st)
    out["row1420_indices"][name] = {"colour": str(c), "weak": str(w), "hyper": str(h), "equal": c == w == h, "dim": len(st)}

# row 1421: per charge q = 6Y, the pieces' indices; D_a = sum_q T_a(q) H(q); D21 = D2 - D1, D31 = D3 - D1
def by_charge(states):
    g = defaultdict(lambda: [F(0), F(0), F(0)])
    for s in states:
        q = int(6 * s[2])
        g[q][0] += s[0] ** 2
        g[q][1] += s[1] ** 2
        g[q][2] += F(3, 5) * s[2] ** 2
    return dict(g)


CLAIM = {  # the item's stated coefficients, as {q: coefficient of H_q}
    "5": {"D21": {3: F(1, 5), -2: F(-1, 5)}, "D31": {3: F(-3, 10), -2: F(3, 10)}},
    "10": {"D21": {1: F(7, 5), -4: F(-4, 5), 6: F(-3, 5)}, "D31": {1: F(9, 10), -4: F(-3, 10), 6: F(-6, 10)}},
    "24": {"D21": {0: F(2), 5: F(-1), -5: F(-1)}, "D31": {0: F(3), 5: F(-3, 2), -5: F(-3, 2)}},
}
allok = True
for name, st in REPS.items():
    g = by_charge(st)
    mine = {"D21": {q: v[1] - v[2] for q, v in g.items()}, "D31": {q: v[0] - v[2] for q, v in g.items()}}
    rec = {}
    for d in ("D21", "D31"):
        mine_nz = {q: c for q, c in mine[d].items() if c != 0}
        ok = mine_nz == CLAIM[name][d]
        allok &= ok
        rec[d] = {"mine": {str(q): str(c) for q, c in sorted(mine_nz.items())}, "claimed": {str(q): str(c) for q, c in
                  sorted(CLAIM[name][d].items())}, "equal": ok, "sum_of_coefficients": str(sum(mine_nz.values()))}
    out["row1421"][name] = rec
out["row1421_all_six_reproduced"] = bool(allok)
out["row1421_differences_vanish_for_equal_H"] = all(
    sum(F(c) for c in out["row1421"][n][d]["mine"].values()) == 0 for n in REPS for d in ("D21", "D31"))
# planted errors
dbl = FIVE[3:]
c, w, h = indices(dbl)
out["PLANTED_doublet_alone"] = {"indices": [str(c), str(w), str(h)], "caught_as_unequal": not (c == w == h)}
bad = dict(CLAIM["10"]["D21"])
bad[1] = F(8, 5)
g10 = by_charge(REPS["10"])
mine10 = {q: v[1] - v[2] for q, v in g10.items() if v[1] - v[2] != 0}
out["PLANTED_wrong_D21_10_caught"] = mine10 != bad
out["all_claims_hold_and_plants_caught"] = bool(
    all(v["equal"] for v in out["row1420_indices"].values()) and allok and out["row1421_differences_vanish_for_equal_H"]
    and out["PLANTED_doublet_alone"]["caught_as_unequal"] and out["PLANTED_wrong_D21_10_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out["row1420_indices"]), out["row1421_all_six_reproduced"], out["PLANTED_doublet_alone"],
      out["all_claims_hold_and_plants_caught"])
