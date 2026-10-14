"""W70: the cusp condensate's charge map. In the audit lane's registered E8 embedding (colour the SU(3) factor, the weak
SU(2) on e3 - e4, the 6 of SU(6) read as rho_Q (x) 3 in three blocks), every admissible hypercharge (block-scalar on the
6, so unbroken by the weave's quaternion holonomies, and reproducing the Standard Model's five fields) is found, and
the lane's 112 condensate roots are read under each. The rule (W70_RULE.md) was committed before this script.

  N1  the branching: the 112 p-odd roots are the weak doublets, and their 40 colour singlets are (20,1,2)
  N2  the admissible hypercharges: the six permutations of (1/6, -5/6, 2/3)
  N3  the generations: every admissible Y gives the three blocks three different charges
  N4  the Higgs-like condensates: four neutral colour-singlet doublets with |Y| = 1/2 per admissible Y
  N5  the published root alpha = e3 + e5: neutral (Y = -1/2) under exactly one admissible Y
  plus the read-outs: the table of the 112 roots, the union, the unbroken Standard Model subgroup at alpha

Coordinates are the lane's (`weave_registered_embedding_2026_10_13/probe.py`, `roots`, `a5_roster`; the field map's
weights of the 6 and its puncture vector), 0-indexed, exact.

Run: python3 the_cusp_condensate_charge_map.py  ->  the_cusp_condensate_charge_map.json beside it.
"""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sy

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_cusp_condensate_charge_map.json"


def vec(*pairs):
    v = [F(0)] * 8
    for i, x in pairs:
        v[i] = F(x)
    return tuple(v)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b, s=1):
    return tuple(x + s * y for x, y in zip(a, b))


def scale(a, s):
    return tuple(s * x for x in a)


def roots():
    out = set()
    for i, j in itertools.combinations(range(8), 2):
        for a, b in itertools.product((-1, 1), repeat=2):
            out.add(vec((i, a), (j, b)))
    for signs in itertools.product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            out.add(tuple(F(s, 2) for s in signs))
    return out


RR = roots()
CHAIN = [vec((6, 1), (7, -1)), vec((5, 1), (6, -1)), vec((6, 1), (7, 1)), tuple(F(-1, 2) for _ in range(8)),
         vec((3, 1), (4, 1))]
COLOUR = [vec((0, 1), (1, -1)), vec((1, 1), (2, -1))]
WEAK = vec((3, 1), (4, -1))
ALPHA = vec((3, 1), (5, 1))                       # the lane's vector(3, 5, 1), its "e4 + e6"


def weights_of_six():
    """the lane's field-map construction: omega_1 dual to the chain, then successive subtraction"""
    C = sy.Matrix([[sy.Rational(x.numerator, x.denominator) for x in c] for c in CHAIN]).T     # 8 x 5
    w1 = C * (C.T * C).inv() * sy.Matrix([1, 0, 0, 0, 0])
    ws = [tuple(F(int(sy.fraction(x)[0]), int(sy.fraction(x)[1])) for x in w1)]
    for c in CHAIN:
        ws.append(add(ws[-1], c, -1))
    return ws


WS = weights_of_six()
HQ = tuple(sum(s * w[k] for s, w in zip((1, -1, 1, -1, 1, -1), WS)) for k in range(8))


def ycartan(y):
    c = (y[0], y[0], y[1], y[1], y[2], y[2])
    return tuple(sum(ci * w[k] for ci, w in zip(c, WS)) for k in range(8))


THREE = {(1, 0), (-1, 1), (0, -1)}
THREEBAR = {(0, 1), (1, -1), (-1, 0)}


def colour(r):
    return (dot(r, COLOUR[0]), dot(r, COLOUR[1]))


def main():
    checks = {}
    # sanity of the lane's conventions
    gram = [[dot(a, b) for b in CHAIN] for a in CHAIN]
    a5_ok = all(gram[i][j] == (2 if i == j else (-1 if abs(i - j) == 1 else 0)) for i in range(5) for j in range(5))
    six_ok = all(dot(WS[i], WS[j]) == (F(5, 6) if i == j else F(-1, 6)) for i in range(6) for j in range(6))
    hq_eigen = [dot(HQ, w) for w in WS]
    # N1: the branching
    odd = {r for r in RR if dot(r, HQ).denominator == 1 and dot(r, HQ) % 2 != 0}
    doublets = {r for r in RR if abs(dot(r, WEAK)) == 1}
    singlet_doublets = {r for r in doublets if colour(r) == (0, 0)}
    twenty = {tuple(sorted(c)) for c in itertools.combinations(range(6), 3)}
    proj = {}
    for r in singlet_doublets:
        v = [dot(r, w) for w in WS]                # for r with SU(6) weight sum_{k in S} ws_k: v_j = [j in S] - 1/2
        S = tuple(j for j in range(6) if v[j] - F(-1, 2) == 1)
        ok = all(v[j] == (F(1, 2) if j in S else F(-1, 2)) for j in range(6)) and len(S) == 3
        proj[r] = S if ok else None
    twenty_ok = (all(proj[r] is not None for r in singlet_doublets)
                 and sorted(map(tuple, proj.values())) == sorted(list(twenty) * 2))
    checks["N1"] = {"the A5 chain is a Cartan matrix": a5_ok, "the six weights have the standard Gram matrix": six_ok,
                    "the puncture's eigenvalues on the 6": [str(x) for x in hq_eigen],
                    "roots": len(RR), "p-odd roots": len(odd), "weak doublets": len(doublets),
                    "p-odd equals weak doublet": odd == doublets,
                    "colour-singlet doublets": len(singlet_doublets),
                    "their SU(6) weights are the 20 weights of the 6's cube, each twice": twenty_ok,
                    "holds": bool(a5_ok and six_ok and len(RR) == 240 and odd == doublets and len(odd) == 112
                                  and len(singlet_doublets) == 40 and twenty_ok)}
    # N2: admissible hypercharges
    cands = [(F(a, 6), F(b, 6), F(-a - b, 6)) for a in range(-12, 13) for b in range(-12, 13) if abs(a + b) <= 12]

    def passes(y):
        Y = ycartan(y)
        has = {"Q": False, "u^c": False, "d^c": False, "L": False, "e^c": False}
        for r in RR:
            yr, c, w = dot(r, Y), colour(r), abs(dot(r, WEAK))
            if c in THREE and w == 1 and yr == F(1, 6):
                has["Q"] = True
            if c in THREEBAR and w == 0 and yr == F(-2, 3):
                has["u^c"] = True
            if c in THREEBAR and w == 0 and yr == F(1, 3):
                has["d^c"] = True
            if c == (0, 0) and w == 1 and yr == F(-1, 2):
                has["L"] = True
            if c == (0, 0) and w == 0 and yr == 1:
                has["e^c"] = True
        return all(has.values())
    admissible = [y for y in cands if passes(y)]
    target = {tuple(p) for p in itertools.permutations((F(1, 6), F(-5, 6), F(2, 3)))}
    checks["N2"] = {"candidates": len(cands), "admissible": [[str(x) for x in y] for y in admissible],
                    "holds": bool(len(admissible) == 6 and set(admissible) == target)}
    # N3: the generations
    checks["N3"] = {"every admissible Y separates the three blocks": all(len(set(y)) == 3 for y in admissible),
                    "holds": bool(admissible and all(len(set(y)) == 3 for y in admissible))}
    # N4 and the table
    per_y, union = {}, set()
    for y in admissible:
        Y = ycartan(y)
        rows = []
        for r in sorted(odd):
            if colour(r) != (0, 0):
                continue
            t3, yr = dot(r, WEAK) / 2, dot(r, Y)
            if abs(yr) == F(1, 2) and t3 + yr == 0:
                rows.append({"root": [str(x) for x in r], "Y": str(yr), "T3": str(t3), "blocks": proj[r]})
                union.add(r)
        per_y[",".join(str(x) for x in y)] = rows
    counts = {k: len(v) for k, v in per_y.items()}
    signs_ok = all(sum(1 for row in v if row["Y"] == "1/2") == 2 and sum(1 for row in v if row["Y"] == "-1/2") == 2
                   for v in per_y.values())
    checks["N4"] = {"neutral Higgs-like roots per admissible Y": counts,
                    "holds": bool(per_y and all(c == 4 for c in counts.values()) and signs_ok)}
    # N5: the published root
    a_in = ALPHA in RR and ALPHA in odd and colour(ALPHA) == (0, 0)
    t3a = dot(ALPHA, WEAK) / 2
    under = {",".join(str(x) for x in y): {"Y": str(dot(ALPHA, ycartan(y))),
                                           "Q": str(t3a + dot(ALPHA, ycartan(y)))} for y in admissible}
    neutral_under = [k for k, v in under.items() if v["Q"] == "0"]
    checks["N5"] = {"alpha is a colour-singlet weak-doublet root": a_in, "T3": str(t3a), "blocks": proj.get(ALPHA),
                    "under each admissible Y": under, "neutral under": neutral_under,
                    "holds": bool(a_in and t3a == F(1, 2) and neutral_under == ["1/6,2/3,-5/6"]
                                  and under["1/6,2/3,-5/6"]["Y"] == "-1/2")}
    # read-outs: the unbroken Standard Model subgroup at alpha under its neutral Y
    ro = {}
    if neutral_under:
        y = tuple(F(x) for x in neutral_under[0].split(","))
        Y = ycartan(y)
        sm_roots = [r for r in RR if (colour(r) != (0, 0) and abs(dot(r, WEAK)) == 0 and all(
            dot(r, c) == 0 for c in CHAIN) and dot(r, Y) == 0)] + [WEAK, scale(WEAK, -1)]
        kept = [r for r in sm_roots if add(ALPHA, r) not in RR and add(ALPHA, r, -1) not in RR]
        cartan = sy.Matrix([[sy.Rational(x.numerator, x.denominator) for x in v]
                            for v in (COLOUR[0], COLOUR[1], WEAK, Y)])
        a_row = sy.Matrix([[sy.Rational(x.numerator, x.denominator) for x in ALPHA]])
        # Cartan combinations h = sum_i c_i v_i with alpha(h) = 0
        coeffs = (a_row * cartan.T)
        kernel = coeffs.nullspace()
        ro["the Standard Model roots kept by E_alpha (colour, weak)"] = {
            "colour": sum(1 for r in kept if colour(r) != (0, 0)), "weak": sum(1 for r in kept if r in (WEAK,
                                                                                                    scale(WEAK, -1)))}
        ro["the Standard Model Cartan directions kept (of colour 2, T3, Y)"] = len(kernel)
        ro["kept Cartan combinations (coefficients of colour1, colour2, T3-axis, Y)"] = [[str(x) for x in k]
                                                                                        for k in kernel]
        ro["the Standard Model roots counted"] = len(sm_roots)
    ro["the union over the admissible Y of neutral Higgs-like roots"] = len(union)
    ro["the 40 colour-singlet doublets, by SU(6) blocks and T3"] = sorted(
        [[list(proj[r]), str(dot(r, WEAK) / 2)] for r in singlet_doublets])
    out = {"status": "W70: the cusp condensate's charge map (the rule W70_RULE.md first; one run)"}
    out.update(checks)
    out["cells"] = {k: checks[k]["holds"] for k in ("N1", "N2", "N3", "N4", "N5")}
    out["read-outs"] = ro
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
