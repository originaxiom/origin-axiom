"""W81: the audit lane's relay of 2026-10-14 (dd2a54119, item 4) checked with this seat's own E8 code. The lane says
that under the continuous SU(2) whose Cartan is the quaternion Cartan H_Q (diag(1, -1, 1, -1, 1, -1) on the 6 of the
lane's SU(6), so the 2 of rho_Q times 1_3), the 248 is 55 singlets + 52 doublets + 27 triplets + 2 quartets; that its
Q8 restriction still has 56 doublets; and that the root of the lane's sl2 (beta = e3 + e5 here, 0-indexed; W70's alpha)
has H_Q weight -1. Section 92 of this seat's relay called the electroweak condensate "a doublet of the weave's SU(2)"
from the Q8 branching. This script was committed before its one run; the predictions and priors are here.

  B1  the H_Q weights of the 240 roots and the 8 Cartan directions give 55 + 52 x 2 + 27 x 3 + 2 x 4      prior 90%
  B2  the odd part (odd H_Q weight) is 112-dimensional, so 56 copies of Q8's 2                          prior 99%
  B3  beta has H_Q weight -1                                                                            prior 85%
  B4  beta lies in the doublets: E_Q^2 e_beta = 0, i.e. no pair of the three block roots a_i, a_j       prior 75%
      (i != j) with beta + a_j and beta + a_i + a_j both roots; likewise F_Q^2 e_beta = 0
  plus the read-outs: the roots with |H_Q| = 3, the embedding index of the SU(2), and the same test at -beta

E_Q is the sum of the three block step operators for the SU(6) roots a_i = w_{2i-1} - w_{2i} (i = 1, 2, 3, with the
lane's weights of the 6, `the_cusp_condensate_charge_map.WS`). The a_i are mutually orthogonal, so the E_i commute and
E_i^2 kills every root vector (simply-laced strings have length at most two). So E_Q^2 e_beta is the sum over i != j
of 2 N N e_{beta + a_i + a_j}, distinct roots for distinct pairs, with no cancellation: it vanishes exactly when no such
path exists. Exact arithmetic throughout.

Run: python3 the_lane_su2_branching.py  ->  the_lane_su2_branching.json beside it.
"""
import itertools
import json
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_cusp_condensate_charge_map as CM  # noqa: E402

OUT = HERE / "the_lane_su2_branching.json"


def irreps(weights):
    """the SU(2) irreps from a multiset of integer H weights (the 2 has weights +-1): d copies of dimension n + 1 where
    d = mult(n) - mult(n + 2), n >= 0"""
    m = Counter(weights)
    top = max(abs(w) for w in weights)
    return {n + 1: m[n] - m[n + 2] for n in range(top + 1) if m[n] - m[n + 2]}


def is_root(v):
    return CM.dot(v, v) == 2 and v in CM.RR


def reach(beta, steps):
    """the pairs i != j with beta + s_j and beta + s_i + s_j both roots (the paths E_i E_j e_beta)"""
    out = []
    for i, j in itertools.permutations(range(3), 2):
        b1 = CM.add(beta, steps[j])
        b2 = CM.add(b1, steps[i])
        if is_root(b1) and is_root(b2):
            out.append([i, j])
    return out


def in_doublets(beta, A):
    up = reach(beta, A)
    down = reach(beta, [CM.scale(a, -1) for a in A])
    return {"E_Q^2 paths": up, "F_Q^2 paths": down, "in the doublets": not up and not down}


def main_():
    WS, HQ = CM.WS, CM.HQ
    A = [CM.add(WS[2 * i], WS[2 * i + 1], -1) for i in range(3)]
    checks = {"the block roots are roots": all(is_root(a) for a in A),
              "mutually orthogonal": all(CM.dot(A[i], A[j]) == 0 for i in range(3) for j in range(3) if i != j),
              "H_Q(a_i) = 2": [CM.dot(HQ, a) for a in A]}
    wts = [CM.dot(r, HQ) for r in CM.RR] + [F(0)] * 8
    assert all(w.denominator == 1 for w in wts)
    wts = [int(w) for w in wts]
    ir = irreps(wts)
    odd = sum(1 for w in wts if w % 2)
    index = sum(c * (n - 1) * n * (n + 1) // 6 for n, c in ir.items()) // 60
    beta = CM.ALPHA
    hb = CM.dot(beta, HQ)
    b4 = in_doublets(beta, A)
    out = {"status": "W81: the audit lane's continuous-SU(2) branching checked (script committed before its one run)",
           "checks": checks, "irreps (dimension: copies)": {str(k): v for k, v in sorted(ir.items())},
           "odd part dimension": odd, "embedding index": index,
           "roots with |H_Q| = 3": [[str(x) for x in r] for r in sorted(CM.RR) if abs(CM.dot(r, HQ)) == 3],
           "beta (the root)": [str(x) for x in beta], "H_Q(beta)": str(hb), "beta: the doublet test": b4,
           "-beta: the doublet test": in_doublets(CM.scale(beta, -1), A)}
    want = {2: 52, 4: 2, 1: 55, 3: 27}
    out["B1"] = {"holds": ir == want}
    out["B2"] = {"holds": odd == 112}
    out["B3"] = {"holds": hb == -1}
    out["B4"] = {"holds": b4["in the doublets"]}
    out["cells"] = {k: out[k]["holds"] for k in ("B1", "B2", "B3", "B4")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main_()
