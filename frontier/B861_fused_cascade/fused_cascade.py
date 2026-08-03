#!/usr/bin/env python3
"""B861 -- the fused cascade: ONE principle runs all three steps, and the SM is the extremal path.

The handoff's cascade needed Michel's principle at every step PLUS a deviation clause ("the world's
chain deviates from the extremal path exactly once, at the chiral step"). B859 repaired its gate;
B860 reduced the trit to a bit with a theorem-grade asymmetry. This arc fuses the imports:

    MAXIMAL RESIDUAL SYMMETRY AMONG REGISTERABLE OPTIONS

where registerable = the generation stays chiral with the theta-odd abelian factors stripped
(B860's criterion: exhibited intertwiner on the failing side, Schur obstruction on the surviving
side). Under this single principle the cascade E6 -> SO(10)xU(1) -> SU(5)xU(1) -> SM is UNIQUE at
every step, and the deviation clause DISSOLVES: the world's chain IS the extremal registerable
path. Mathematics scope; nothing to CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

CONJ = {"3": "3bar", "3bar": "3", "4": "4bar", "4bar": "4", "6": "6", "1": "1",
        "2": "2", "16": "16bar", "16bar": "16", "10": "10", "5": "5bar", "5bar": "5",
        "15": "15bar", "15bar": "15", "6bar": "6c", "6c": "6bar", "27sd": "27sd"}
# NOTE "6" = Lambda^2(4) of SU(4), SELF-dual; "6bar"/"6c" = the (anti)fundamental-type 6 of
# SU(6), COMPLEX. Same numeral, different algebra, opposite duality -- named apart to avoid
# exactly the collision that would silently break this table.


def chiral(reps):
    """True iff the multiset of (non-abelian) irreps differs from its conjugate."""
    conj = [tuple(CONJ[x] for x in r) for r in reps]
    return Counter(conj) != Counter(reps)


# THE UNIFORM OBJECT IS THE GENERATION -- the 27's matter content under each subgroup --
# NOT the coset. (First draft used coset multisets at step 1: VACUOUS, since every coset of
# the adjoint is self-conjugate as a multiset. The arc's own run exposed it: it returned
# SU(3)^3 as the step-1 winner because 16+16bar cancels as a multiset. Criteria must not
# switch between steps; the generation is the one object present at every level.)
STEPS = [
    ("step1_E6", [   # 27 under each chain (u1 charges stripped; non-abelian content)
        ("SO(10)xU(1)", 46, [("16",), ("10",), ("1",)]),
        ("SU(6)xSU(2)", 38, [("15", "1"), ("6bar", "2")]),
        ("SU(3)^3", 24, [("3", "3bar", "1"), ("1", "3", "3bar"), ("3bar", "1", "3")]),
        ("Sp(8)", 36, [("27sd",)]),          # traceless Lambda^2(8) of C4: self-dual
        # SU(3)_9 (dim 8): 27-branching under the level-9 special embedding UNRESOLVED here;
        # cannot affect the winner (8 < 46 regardless of verdict). Flagged, not decided.
    ]),
    ("step2_SO10", [  # the 16 under each option
        ("SU(5)xU(1)", 25, [("10",), ("5bar",), ("1",)]),
        ("Pati-Salam", 21, [("4", "2", "1"), ("4bar", "1", "2")]),
    ]),
    ("step3_SU5", [   # the generation 10+5bar under each option (B860)
        ("SU(4)xU(1)", 16, [("6",), ("4",), ("4bar",), ("1",)]),
        ("SM", 12, [("3", "2"), ("3bar", "1"), ("3bar", "1"), ("1", "2"), ("1", "1")]),
    ]),
]

def main():
    res = {"principle": "maximal residual symmetry among REGISTERABLE options",
           "registerable_defn": "generation chiral with theta-odd abelian factors stripped "
                                "(B860: intertwiner/Schur dichotomy)"}
    chain = []
    for key, menu in STEPS:
        rows = []
        for name, dim, gen in menu:
            rows.append(dict(option=name, dim=dim, registerable=chiral(gen)))
        reg = [r for r in rows if r["registerable"]]
        winner = max(reg, key=lambda r: r["dim"])
        unique = len([r for r in reg if r["dim"] == winner["dim"]]) == 1
        res[key] = dict(menu=rows, winner=winner["option"], unique=unique)
        chain.append(winner["option"])
    res["chain"] = ["E6"] + chain
    res["chain_is_sm"] = (chain == ["SO(10)xU(1)", "SU(5)xU(1)", "SM"])
    res["deviation_clause_dissolves"] = res["chain_is_sm"]
    # the criterion is NOT vacuous: it can fail (SU(4)xU(1) fails it) and can pass
    res["criterion_can_fail"] = any(not r["registerable"]
                                    for r in res["step3_SU5"]["menu"])
    res["criterion_can_pass"] = any(r["registerable"]
                                    for r in res["step3_SU5"]["menu"])

    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)

    print("=" * 74)
    print("B861 -- the fused cascade")
    print("=" * 74)
    for key, _ in STEPS:
        s = res[key]
        print(f"\n  {key}:")
        for r in s["menu"]:
            mark = "  <== WINNER" if r["option"] == s["winner"] else ""
            print(f"    {r['option']:14} dim {r['dim']:>3}  registerable {str(r['registerable']):5}{mark}")
        print(f"    unique: {s['unique']}")
    print(f"\n  CHAIN: {' -> '.join(res['chain'])}")
    print(f"  chain is the SM chain: {res['chain_is_sm']}")
    print(f"  the deviation clause dissolves: {res['deviation_clause_dissolves']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
