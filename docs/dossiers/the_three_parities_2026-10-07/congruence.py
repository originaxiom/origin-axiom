#!/usr/bin/env python3
"""The root's tetrahedral cover is its congruence cover of level sqrt(-3), and eps is the spin sign there. Structure only
(no count); traces recognised in Z[omega] at 60 digits from sm:B1527's holonomy of m004 (+LR).

  (1) pi_1(m004) maps ONTO PSL(2, F_3) = A4 under the holonomy mod sqrt(-3): tr a = 0 mod sqrt(-3) (an involution of
      PSL(2, F_3)) and tr t = +-1 mod sqrt(-3) (an element of order 3), and an involution with an element of order 3
      generate A4.
  (2) pi_1(m004) has exactly one normal subgroup with quotient A4 (the note's section 2), so that kernel is the tetrahedral
      cover N. Checked here: every generator of pi_1 N (route P's presentation) has trace = +-2 mod sqrt(-3).
  (3) The sign s(g) with tr g = 2 s(g) mod sqrt(-3), on those generators, is the A4-invariant sign character
      eps = [1, 1, 1, 0, 1 | 1] (orbit B = orbit A (x) eps): the central character of SL(2, F_3), the binary tetrahedral
      group, for this lift of the holonomy.

    python3 congruence.py   ->  congruence.json beside this file"""
import json
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent


def _root():
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    import os
    return Path(os.environ["ORIGIN_AXIOM_ROOT"])


import sys
sys.path.insert(0, str(_root() / "frontier" / "B1550_the_three_parities" / "verification"))
import tetra_lib as L  # noqa: E402

T = L.T


def main():
    FL = T.family_lib()
    mp.mp.dps = 60
    A, B, Tt, _ = FL.hyperbolic_sl2("+", "LR")
    M = {"a": A, "b": B, "t": Tt}
    w3 = mp.mpc(-0.5, mp.sqrt(3) / 2)

    def tr_omega(w):
        X = FL.sl2_word(w, M)
        z = X[0, 0] + X[1, 1]
        y = 2 * mp.im(z) / mp.sqrt(3)
        x = mp.re(z) + y / 2
        xi, yi = int(mp.nint(x)), int(mp.nint(y))
        assert abs(z - (xi + yi * w3)) < mp.mpf(10) ** -40, w
        return xi, yi, (xi + yi) % 3                     # omega = 1 mod sqrt(-3)

    out = {"traces (x + y omega; mod sqrt(-3))": {w: tr_omega(w) for w in ("a", "b", "ab", "t", "abAB", "ttt")}}
    a_mod, t_mod = out["traces (x + y omega; mod sqrt(-3))"]["a"][2], out["traces (x + y omega; mod sqrt(-3))"]["t"][2]
    out["onto PSL(2, F_3)"] = a_mod == 0 and t_mod in (1, 2)
    wl, C = L.tetra_cover("+LR")
    Pr = T.RP.Presentation(C)
    words = [w.replace("t", "ttt").replace("T", "TTT") for (_, _, w) in Pr.gens]   # the root: t_3 = t^3 (twist c = 1)
    mods = [tr_omega(w)[2] for w in words]
    out["generators of pi_1 N"] = len(words)
    out["every generator = +-I mod sqrt(-3) by trace"] = all(r in (1, 2) for r in mods)
    sigma = [0 if r == 2 else 1 for r in mods]           # tr = 2 s mod 3: s = +1 <-> 2, s = -1 <-> 1
    eps = list(Pr.values((1, 1, 1, 0, 1), 1, 2))
    eps0 = list(Pr.values((1, 1, 1, 0, 1), 0, 2))
    out["the spin sign on the generators (exponents mod 2)"] = sigma
    out["eps = [1,1,1,0,1|1] on the generators"] = eps
    out["the spin sign is eps"] = sigma == eps
    out["the spin sign is eps0 = [1,1,1,0,1|0]"] = sigma == eps0
    (HERE / "congruence.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out))


if __name__ == "__main__":
    main()
