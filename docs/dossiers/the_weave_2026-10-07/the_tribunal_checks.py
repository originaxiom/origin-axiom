"""W82: two checks for main's frame tribunal (main's relay of 2026-10-14, passed to this seat by the owner; main's by-hand
lemma A and its hook from section 92). This script was committed before its one run; the predictions and priors are here.

  L1  lemma A's two halves, by explicit matrices on the family 3 (the three imaginary units). A charge commuting with the
      holonomy's V4 (the inner automorphisms of Q8 on the units: diag(1, -1, -1) and its permutations) is diagonal; one
      commuting also with the moves' S3 on the labels is scalar. The commutant dimensions:
        V4 and S3 together  1   (lemma A)                                                               prior 99%
        S3 alone            2   (a + bJ: transitivity alone allows a democratic split, 1 + 2)            prior 99%
        V4 alone            3   (diagonal: the holonomy alone allows unalike charges)                   prior 99%
        a non-transitive control, V4 and one transposition   2                                          prior 99%
  L2  the hook's condensates. Under each of the six admissible hypercharges of W70 (N2), the colour-singlet weak-doublet
      roots among the lane's 112 that are electrically neutral with |Y| = 1/2: their Y, weak T3 and H_Q weight, and
      whether each lies in the doublets of the continuous SU(2) of the quaternion Cartan (W81's test).
        two with Y = +1/2 and two with Y = -1/2 under every admissible Y (W70's N4 checked this; re-read) prior 99%
        all four in the doublets of the continuous SU(2), under every admissible Y                       prior 60%
  plus the read-outs: the roots themselves, and the weak-doublet partners of the neutral ones

Exact arithmetic with this seat's E8 code (`the_cusp_condensate_charge_map.py`, W70) and W81's doublet test
(`the_lane_su2_branching.py`).

Run: python3 the_tribunal_checks.py  ->  the_tribunal_checks.json beside it.
"""
import itertools
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as sy

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_cusp_condensate_charge_map as CM  # noqa: E402
import the_lane_su2_branching as W81  # noqa: E402

OUT = HERE / "the_tribunal_checks.json"


def commutant_dim(mats):
    """the dimension of {X in M_3 : X g = g X for every g}"""
    xs = sy.symbols("x0:9")
    X = sy.Matrix(3, 3, xs)
    eqs = []
    for g in mats:
        eqs += list(X * g - g * X)
    A = sy.Matrix([[sy.diff(e, x) for x in xs] for e in eqs])
    return 9 - A.rank()


def perm(p):
    M = sy.zeros(3, 3)
    for i, j in enumerate(p):
        M[j, i] = 1
    return M


V4 = [sy.diag(1, -1, -1), sy.diag(-1, 1, -1), sy.diag(-1, -1, 1)]
S3 = [perm(p) for p in itertools.permutations(range(3))]
TRANSPOSITION = [perm((1, 0, 2))]


def main_():
    out = {"status": "W82: two checks for main's frame tribunal (script committed before its one run)"}
    dims = {"V4 and S3": commutant_dim(V4 + S3), "S3 alone": commutant_dim(S3), "V4 alone": commutant_dim(V4),
            "V4 and one transposition (non-transitive)": commutant_dim(V4 + TRANSPOSITION)}
    out["L1"] = {"commutant dimensions": dims,
                 "holds": dims == {"V4 and S3": 1, "S3 alone": 2, "V4 alone": 3,
                                   "V4 and one transposition (non-transitive)": 2}}
    WS, HQ = CM.WS, CM.HQ
    A = [CM.add(WS[2 * i], WS[2 * i + 1], -1) for i in range(3)]
    rows, signs_ok, all_doublets = {}, True, True
    for y in itertools.permutations((F(1, 6), F(-5, 6), F(2, 3))):
        Yc = CM.ycartan(y)
        found = []
        for r in sorted(CM.RR):
            t3 = CM.dot(r, CM.WEAK) / 2
            if abs(t3) != F(1, 2) or CM.colour(r) != (0, 0):
                continue
            yy = CM.dot(r, Yc)
            if t3 + yy != 0 or abs(yy) != F(1, 2):
                continue
            hq = CM.dot(r, HQ)
            test = W81.in_doublets(r, A)
            partner = CM.add(r, CM.WEAK, -1 if t3 > 0 else 1)
            found.append({"root": [str(x) for x in r], "Y": str(yy), "T3": str(t3), "H_Q": str(hq),
                          "in the doublets": test["in the doublets"],
                          "weak partner is a root": W81.is_root(partner)})
        ys = sorted(f["Y"] for f in found)
        signs_ok = signs_ok and ys == ["-1/2", "-1/2", "1/2", "1/2"]
        all_doublets = all_doublets and all(f["in the doublets"] for f in found)
        rows[",".join(str(v) for v in y)] = found
    out["L2"] = {"per admissible Y": rows, "two of each sign everywhere": signs_ok,
                 "all in the doublets everywhere": all_doublets}
    out["L2a"] = {"holds": signs_ok}
    out["L2b"] = {"holds": all_doublets}
    out["cells"] = {"L1": out["L1"]["holds"], "L2a": signs_ok, "L2b": all_doublets}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main_()
