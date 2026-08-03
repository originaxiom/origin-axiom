#!/usr/bin/env python3
"""B864 -- the anomaly ledger: the dial/gauge split is DERIVED, and hypercharge is the unique
gaugeable abelian direction.

The critic's G3, run in full. Three exact results:
  (1) Over the FULL 27 (and the full 16) every U(1) of the chain is anomaly-free -- E6 is
      anomaly-safe, and nothing at the parent level forces a truncation.
  (2) Over the CHIRAL matter (the re-anchored generation), the dial U(1)s become anomalous:
      psi over the 16 (Tr = 16, Tr^3 = 16, [SO(10)]^2 = 2); chi over 10+5bar (Tr = 5,
      Tr^3 = 125). AN ANOMALOUS U(1) CANNOT BE GAUGED: the framework's claim that these are
      observer DIALS is now a consequence, not an assertion.
  (3) UNIQUENESS: writing Q = aY + b*chi + c*psi over the generation, the linear anomaly
      conditions (grav^2-Q, [SU(3)]^2-Q, [SU(2)]^2-Q) force b = c = 0 exactly -- hypercharge
      is the UNIQUE gaugeable abelian direction, and its cubic then vanishes for free (the
      "textbook miracle", here inherited and forced).

THE DERIVATION ARROW: the cascade's dial-stripping rule = anomaly consistency of the chiral
sector. Mathematics scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))

# multiplets of the generation 10+5bar: (name, dim, Y, chi, psi, T_SU3, T_SU2)
GEN = [("Q(3,2)", 6, Fr(1, 6), -1, 1, 2 * Fr(1, 2), 3 * Fr(1, 2)),
       ("uc(3b,1)", 3, Fr(-2, 3), -1, 1, Fr(1, 2), Fr(0)),
       ("ec(1,1)", 1, Fr(1, 1), -1, 1, Fr(0), Fr(0)),
       ("dc(3b,1)", 3, Fr(1, 3), 3, 1, Fr(1, 2), Fr(0)),
       ("L(1,2)", 2, Fr(-1, 2), 3, 1, Fr(0), Fr(1, 2))]


def parent_level():
    """(1): the full 27 and full 16 are anomaly-free for the dials."""
    psi27 = dict(tr=16 * 1 + 10 * (-2) + 1 * 4,
                 tr3=16 * 1 + 10 * (-8) + 1 * 64,
                 so10sq=2 * 1 + 1 * (-2))
    chi16 = dict(tr=10 * (-1) + 5 * 3 + 1 * (-5),
                 tr3=10 * (-1) + 5 * 27 + 1 * (-125),
                 su5sq=Fr(3, 2) * (-1) + Fr(1, 2) * 3)
    return psi27, chi16


def truncated_level():
    """(2): the dials over the chiral matter."""
    psi16 = dict(tr=16, tr3=16, so10sq=2)
    chi_gen = dict(tr=10 * (-1) + 5 * 3, tr3=10 * (-1) + 5 * 27)
    return psi16, chi_gen


def uniqueness():
    """(3): b = c = 0 forced; Y unique."""
    a, b, c = sp.symbols('a b c')
    Q = {n: a * sp.Rational(y) + b * ch + c * ps for n, d, y, ch, ps, t3, t2 in GEN}
    dims = {n: d for n, d, *_ in GEN}
    t3s = {n: t3 for n, d, y, ch, ps, t3, t2 in GEN}
    t2s = {n: t2 for n, d, y, ch, ps, t3, t2 in GEN}
    grav = sp.expand(sum(dims[n] * Q[n] for n in Q))
    su3 = sp.expand(sum(sp.Rational(t3s[n]) * Q[n] for n in Q))
    su2 = sp.expand(sum(sp.Rational(t2s[n]) * Q[n] for n in Q))
    sols = sp.solve([grav, su3, su2], [b, c], dict=True)
    cube_pure_Y = sp.expand(sum(dims[n] * Q[n] ** 3 for n in Q).subs({b: 0, c: 0}))
    return dict(grav=str(grav), su3sq=str(su3), su2sq=str(su2),
                forced=str(sols), b_c_zero=(sols == [{b: 0, c: 0}]),
                cubic_pure_Y=str(cube_pure_Y), miracle=(cube_pure_Y == 0))


def sm_hypercharge_free():
    """The SM generation is completely anomaly-free in Y (all four conditions)."""
    trY = sum(d * y for _, d, y, *_ in GEN)
    trY3 = sum(d * y ** 3 for _, d, y, *_ in GEN)
    su3Y = sum(t3 * y for _, d, y, ch, ps, t3, t2 in GEN)
    su2Y = sum(t2 * y for _, d, y, ch, ps, t3, t2 in GEN)
    return dict(trY=str(trY), trY3=str(trY3), su3Y=str(su3Y), su2Y=str(su2Y),
                all_zero=(trY == 0 and trY3 == 0 and su3Y == 0 and su2Y == 0))


def main():
    psi27, chi16 = parent_level()
    psi16, chi_gen = truncated_level()
    res = dict(
        parent=dict(psi_over_27=psi27, chi_over_16={k: str(v) for k, v in chi16.items()}),
        parent_all_free=(all(v == 0 for v in psi27.values())
                         and all(v == 0 for v in chi16.values())),
        truncated=dict(psi_over_16=psi16, chi_over_gen=chi_gen),
        dials_anomalous_over_chiral_matter=(any(v != 0 for v in psi16.values())
                                            and any(v != 0 for v in chi_gen.values())),
        uniqueness=uniqueness(),
        sm_Y=sm_hypercharge_free())
    res["derivation_arrow"] = ("the cascade's dial-stripping rule = anomaly consistency of the "
                               "chiral sector: the stripped U(1)s are exactly the ungaugeable "
                               "ones, and Y is the unique gaugeable direction")
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True,
              default=str)
    print("=" * 74)
    print("B864 -- the anomaly ledger")
    print("=" * 74)
    print(f"\n  (1) parent level all anomaly-free : {res['parent_all_free']}")
    print(f"  (2) dials anomalous over chiral matter: {res['dials_anomalous_over_chiral_matter']}")
    print(f"      psi over 16: {psi16}   chi over 10+5bar: {chi_gen}")
    u = res["uniqueness"]
    print(f"  (3) linear conditions: grav = {u['grav']}, [SU3]^2 = {u['su3sq']}, [SU2]^2 = {u['su2sq']}")
    print(f"      forced: {u['forced']}  -> b = c = 0: {u['b_c_zero']}")
    print(f"      cubic at pure Y: {u['cubic_pure_Y']} (miracle: {u['miracle']})")
    print(f"  SM generation fully Y-anomaly-free: {res['sm_Y']['all_zero']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
