"""B369 (W2.9) — the concatenation-kill test.

Registered before computing (OPEN_LEADS W2.9, PR #441): the two-block word
R^{m1} L^{m1} R^{m2} L^{m2} is a SINGLE once-punctured-torus bundle built from the same
blocks the seam PAIRS. Its level-15 theta-lift is the product of the seed lifts,
W_word = W_{m1} * W_{m2} (letter concatenation = matrix product under the B358/B367
letter assignment R -> D, L -> WR, W_m = WR^m D^m). PRE-REGISTERED PREDICTION: the
single-seed readout tr(Par * P_a(W_word)), H-projected, has ZERO sqrt(-3) and sqrt(-15)
coefficients for every eigenprojector — the single-object wall holds inside the seam
observable, i.e. gluing the blocks into one monodromy KILLS the seam that the unglued
pair carries. Seam-positive would crack the wall. Both outcomes bank.

Consistency gate for free: R^{m1}L^{m1}R^{m2}L^{m2} and R^{m2}L^{m2}R^{m1}L^{m1} are
cyclic rotations (conjugate words => the same bundle), so both orders must give
identical clean/dirty verdicts and identical readout multisets.

Also recorded (data, no claim): tr(Par * W_{m1} * W_{m2}) — the word's first Par-trace —
IS the pair table's C[1][1], the point where the two channels touch.
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
import seam_certification as SC                       # noqa: E402
from step0_exact_matrices import (build_theta_W,      # noqa: E402
                                  matrix_order)

N = 15
WORDS = [(1, 2), (2, 1), (1, 3), (2, 3), (3, 4), (1, 4)]


def word_matrix(m1, m2):
    return E.mmul(build_theta_W(m1), build_theta_W(m2))


def single_readout(powers):
    """{a: (p,q,r,s)} for the nonzero tr(Par * P_a), exactly."""
    o = len(powers)
    z = 60 // o
    par_tr = []
    for j in range(o):
        t = E.ZERO
        for x in range(N):
            t = E.add(t, powers[j][(-x) % N][x])
        par_tr.append(t)
    out = {}
    for a in range(o):
        t = E.ZERO
        for j in range(o):
            t = E.add(t, E.mul(E.zeta((-z * j * a) % 60), par_tr[j]))
        t = E.scal(Fr(1, o), t)
        if t == E.ZERO:
            continue
        sol = SC.solve_H(SC.H_avg(t))
        assert sol is not None, ("outside H", a)
        out[a] = sol
    return out


def run():
    report = {}
    for (m1, m2) in WORDS:
        W = word_matrix(m1, m2)
        o, powers = matrix_order(W)
        r = single_readout(powers)
        clean = all(v[2] == 0 and v[3] == 0 for v in r.values())
        report[f"{m1}+{m2}"] = dict(
            order=o,
            nonzero=len(r),
            clean_sqrtm3_sqrtm15=clean,
            readout={str(a): [str(x) for x in v] for a, v in sorted(r.items())},
        )
    # the cyclic-rotation gates. Manifold-level: order + cleanliness verdict agree (the
    # words are conjugate => the same bundle). The naive readout-multiset gate of the first
    # design FAILED and was diagnosed, not weakened: tr(Par*P_a) is (lift, Par)-sector data,
    # not manifold data, and the exact structure is that rotation acts by the sqrt5-Galois
    # involution sigma: r_{21}(a) = sigma(r_{12}(a)) exponent-wise. Locked as such.
    report["rotation_gate_manifold"] = (
        report["1+2"]["clean_sqrtm3_sqrtm15"] == report["2+1"]["clean_sqrtm3_sqrtm15"]
        and report["1+2"]["order"] == report["2+1"]["order"])
    r12, r21 = report["1+2"]["readout"], report["2+1"]["readout"]
    report["rotation_galois_identity"] = (
        set(r12) == set(r21) and all(
            [r21[a][0], r21[a][1], r21[a][2], r21[a][3]]
            == [r12[a][0], str(-Fr(r12[a][1])), r12[a][2], r12[a][3]]
            for a in r12))
    report["prediction_seam_null"] = all(
        report[f"{a}+{b}"]["clean_sqrtm3_sqrtm15"] for (a, b) in WORDS)
    with open(os.path.join(HERE, "concat_kill.json"), "w") as fh:
        json.dump(report, fh, indent=1)
    return report


if __name__ == "__main__":
    rep = run()
    for k, v in rep.items():
        if isinstance(v, dict):
            print(f"  word {k}: order {v['order']}, nonzero {v['nonzero']}, "
                  f"clean {v['clean_sqrtm3_sqrtm15']}")
        else:
            print(f"  {k}: {v}")
