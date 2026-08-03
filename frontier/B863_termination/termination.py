#!/usr/bin/env python3
"""B863 -- the cascade TERMINATES at the SM: the terminal-registerability theorem.

The completeness critic's G1 (the referee's opening shot): a descent rule selects nothing until
it halts, and no arc had asked why the cascade stops. Answer: EVERY proper descent of the SM
kills registerability -- the SM is the TERMINAL registerable algebra, and the halt is principled:
the (3,2) is the last unpaired complex structure.

Descent menu inside SM = su(3)+su(2)+u(1) at the cascade's levels (su(3)_1 c=2, su(2)_1 c=1):
  (a) su(2) -> u(1)          : su(3) content of the generation is {3:2, 3bar:2, 1:3} vector-like
  (b) su(3) -> su(2)xu(1)    : every surviving rep pseudoreal/real (su(2) reps pseudoreal)
  (b') su(3)_1 -> su(2)_4    : the GENUINE conformal embedding (principal, index 4, c = 12/6 = 2)
                               -- the 3 branches to the su(2) TRIPLET, which is REAL
  (c) full abelianization    : dial only
  (d) dropping u(1)_Y alone  : not a proper descent of the non-abelian core (same carrier)

KIND check: what survives electroweak breaking -- QCD+QED -- is vector-like: the same fact from
physics. The cascade stops exactly where nature's chiral gauge structure stops.

Mathematics scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from collections import Counter
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))

CONJ = {"3": "3bar", "3bar": "3", "1": "1", "2": "2",
        "(2,2)": "(2,2)", "(1,2)": "(1,2)", "(2,1)": "(2,1)", "(1,1)": "(1,1)",
        "t3": "t3"}          # t3 = the real su(2) triplet from the principal embedding


def chiral(multiset):
    conj = Counter({CONJ[r]: n for r, n in multiset.items()})
    return conj != Counter(multiset)


def main():
    res = {}
    # the SM generation, dial-stripped (B860): (3,2)+2(3bar,1)+(1,2)+(1,1)
    # (a) drop su(2): under su(3) alone
    a = Counter({"3": 2, "3bar": 2, "1": 3})
    # (b) drop su(3) -> su(2)_c x su(2)_w (colour su(2) + weak su(2)); all pseudoreal
    b = Counter({"(2,2)": 1, "(1,2)": 2, "(2,1)": 2, "(1,1)": 3})
    # (b') su(3)_1 -> su(2)_4, principal: 3 -> triplet (real); generation under su(2)_4 x su(2)_w
    bp = Counter({"(t3;2)": 0})  # build explicitly:
    # (3,2) -> (t3, 2); (3bar,1)x2 -> (t3,1)x2; (1,2) -> (1,2); (1,1) -> (1,1)
    bp = Counter({"(t3,2)": 1, "(t3,1)": 2, "(1,2)": 1, "(1,1)": 1})
    CONJ.update({"(t3,2)": "(t3,2)", "(t3,1)": "(t3,1)"})   # t3 real, 2 pseudoreal: self-conj

    res["conformality_bprime"] = dict(c_su2_4=str(Fr(3 * 4, 4 + 2)), c_su3_1=str(Fr(8, 1 + 3)),
                                      match=Fr(3 * 4, 4 + 2) == Fr(8, 1 + 3))
    res["descents"] = {
        "a_drop_su2": dict(multiset=dict(a), chiral=chiral(a)),
        "b_drop_su3_regular": dict(multiset=dict(b), chiral=chiral(b)),
        "bprime_su2_4_principal_CONFORMAL": dict(multiset=dict(bp), chiral=chiral(bp)),
    }
    res["all_descents_dead"] = not any(d["chiral"] for d in res["descents"].values())
    # the SM itself, for contrast (the positive control: the test CAN pass)
    sm = Counter({"(3,2)": 1, "(3bar,1)": 2, "(1,2)": 1, "(1,1)": 1})
    CONJ.update({"(3,2)": "(3bar,2)", "(3bar,2)": "(3,2)", "(3bar,1)": "(3,1)", "(3,1)": "(3bar,1)"})
    res["sm_itself_chiral"] = chiral(sm)
    res["terminal"] = res["all_descents_dead"] and res["sm_itself_chiral"]

    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)

    print("=" * 74)
    print("B863 -- the termination theorem")
    print("=" * 74)
    print(f"\n  (b') su(2)_4 in su(3)_1 conformality: c = {res['conformality_bprime']['c_su2_4']}"
          f" = {res['conformality_bprime']['c_su3_1']}: {res['conformality_bprime']['match']}")
    for k, d in res["descents"].items():
        print(f"  {k:36} chiral: {d['chiral']}")
    print(f"\n  positive control -- the SM itself is chiral: {res['sm_itself_chiral']}")
    print(f"  ALL proper descents dead + SM chiral => TERMINAL: {res['terminal']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
