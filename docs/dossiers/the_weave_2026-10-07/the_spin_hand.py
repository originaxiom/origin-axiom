#!/usr/bin/env python3
"""W9's hand rule, checked on every state of GENESIS to length 12 (758): when does the weave's spin doublet split into its
two complex-conjugate lines at different values of kappa?

On the doublet H1(F2; rho_Q) the moves act by commuting rotations (the_spin_room.py): with a lift, L by 45 degrees, R by
135 and the sign by 90. A state's act is then a rotation by 45 (n_L + 3 n_R) + 90 [sign -] degrees, up to the lift's 180.
Its two eigenlines, the same for every L,R-thread, carry kappa = e^{+- i theta}: equal (the lines together) when theta is
0 or 180, different (the lines apart) otherwise. So the lines are apart exactly when n_L - n_R + 2 [sign -] is not 0 mod 4.

The rule is checked against the act's eigenvalues computed directly, and read on the states that are their own mirror (the
swapped word is a rotation of the word or of its reverse), where main's B1479 finds that the - state is the one on which
a hand can be registered.

    python3 the_spin_hand.py   ->  the_spin_hand.json beside it
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_common_point as CP  # noqa: E402
import the_spin_room as SR  # noqa: E402
import the_weaves_laws as WL  # noqa: E402


def run():
    total, agree, split_count, amph = 0, 0, {"apart": 0, "together": 0}, {"+": [0, 0], "-": [0, 0]}
    disagree = []
    for w in WL.states(12):
        nL, nR = w.count("L"), w.count("R")
        sw = w.translate(str.maketrans("LR", "RL"))
        rots = lambda x: {x[i:] + x[:i] for i in range(len(x))}  # noqa: E731
        own_mirror = sw in rots(w) or sw in rots(w[::-1])
        for sign in (1, -1):
            phi = CP.word_aut(w, sign)
            g = CP.extend(phi)[0]
            ev = np.linalg.eigvals(SR.act_matrix(phi, g, (0, 0)))
            apart = abs(ev[0] - ev[1]) > 1e-8
            rule = (nL - nR + (2 if sign < 0 else 0)) % 4 != 0
            total += 1
            agree += int(apart == rule)
            if apart != rule:
                disagree.append(("+" if sign > 0 else "-") + w)
            split_count["apart" if apart else "together"] += 1
            if own_mirror:
                amph["+" if sign > 0 else "-"][0 if apart else 1] += 1
    return {"states (both signs) to length 12": total, "the rule agrees on": agree, "disagreements": disagree,
            "lines apart / together": split_count,
            "states that are their own mirror: + state [apart, together]": amph["+"],
            "states that are their own mirror: - state [apart, together]": amph["-"]}


if __name__ == "__main__":
    res = run()
    with open(HERE / "the_spin_hand.json", "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res))
