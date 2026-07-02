"""B368 (W2.4, corrected scope) — the cover tower: the seam sees the deck equivariantly.

Corrected premise (the equal-trace identification R^4L^4 ~ (RL)^3 was REFUTED exactly —
fixed-point forms of primitive discriminant 5 vs 20): the genuine k-fold fiber cover of
the golden bundle has monodromy (RL)^k, whose theta lift is the k-th POWER of the golden
lift, W_1^k. The registered question: does the seam see the generation deck?

THE ANSWER HAS A FORCED SHAPE, by projector algebra: gcd(k, 20) = 1 (k = 3, 7, ...) gives
    P_a(W_1^k) = P_{k^{-1} a mod 20}(W_1),
so the cover-pair table against any partner is the base-pair table RELABELED by the deck's
action on exponents (a -> k*a):
    t_cover(a, b) = t_base(k^{-1} a mod 20, b)      [k=3: k^{-1} = 7]
This module verifies the identity exactly against the banked B367 (1,2) table, checks the
cover-tower singles are clean (the wall), records the exponent-list arithmetic
(3*K1 mod 20 — matching the relayed independent list), and contrasts the trace-18 twins
at the seam level: the (RL)^3-cover pairing carries the base's values; the m=4 seed pairing
(banked (2,4)) carries different ones — same trace, same order, different exponent lists,
different seam forms.
"""
import json
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B358 = os.path.join(HERE, "..", "B358_seam_certification")
B367 = os.path.join(HERE, "..", "B367_value_map")
sys.path.insert(0, B358)
sys.path.insert(0, B367)
import cyclo_engine as E                              # noqa: E402
from step0_exact_matrices import (build_theta_W,      # noqa: E402
                                  matrix_order, pair_smatrix)
from concat_kill_shim import single_readout           # noqa: E402

K1 = [0, 1, 4, 5, 6, 9, 11, 14, 15, 16, 19]


def load_base_table():
    data = json.load(open(os.path.join(B367, "step0_tables.json")))
    return {tuple(int(x) for x in k.split(",")): tuple(Fr(s) for s in v)
            for k, v in data["1,2"].items()}


def run():
    report = {}
    W1 = build_theta_W(1)
    o1, pow1 = matrix_order(W1)
    assert o1 == 20

    # the cover lift W_1^3 and its powers
    W3cov = E.mmul(E.mmul(W1, W1), W1)
    o3, pow3 = matrix_order(W3cov)
    report["cover_order"] = o3                        # expect 20 (gcd(3,20)=1)

    # exponent list of the cover = 3*K1 mod 20 (pure arithmetic; matches the relayed list)
    report["cover_exponents"] = sorted((3 * a) % 20 for a in K1)

    # singles: the cover tower is clean (the wall) for k = 2..5
    Wk = W1
    clean = {}
    for k in range(2, 6):
        Wk = E.mmul(Wk, W1)
        ok, powk = matrix_order(Wk)
        r = single_readout(powk)
        clean[k] = all(v[2] == 0 and v[3] == 0 for v in r.values())
    report["tower_singles_clean_k2_k5"] = clean

    # THE DECK IDENTITY: t_cover(a,b) = t_base(7a mod 20, b), exactly, all (a,b)
    W2 = build_theta_W(2)
    o2, pow2 = matrix_order(W2)
    cover_pair = pair_smatrix(pow3, pow2)
    base = load_base_table()
    ok = True
    for a in range(20):
        for b in range(12):
            lhs = cover_pair.get((a, b))
            rhs = base.get(((7 * a) % 20, b))
            if lhs != rhs:
                ok = False
    report["deck_identity_exact"] = ok

    # the trace-18 twins at the seam level: cover values vs the m=4 seed values (banked)
    svals = lambda tab: sorted({str(v[3]) for v in tab.values() if v[3] != 0})
    report["cover_pair_svals"] = svals(cover_pair)     # = the base (1,2) value set
    data24 = json.load(open(os.path.join(B367, "step0_tables.json")))["2,4"]
    report["seed4_pair_svals"] = sorted({v[3] for v in data24.values() if Fr(v[3]) != 0})

    with open(os.path.join(HERE, "cover_tower.json"), "w") as fh:
        json.dump(report, fh, indent=1, default=str)
    return report


if __name__ == "__main__":
    rep = run()
    for k, v in rep.items():
        print(f"  {k}: {v}")
