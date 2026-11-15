#!/usr/bin/env python3
"""W-A1, part 3, post hoc 2 (committed before its run; NOT blind: the sealed run, post hoc 1 and W-V1's referee read
are known).

W-V1's referee found that the act's axis crosses the cone point of order 2 twice per period: at i and at 1 + i (both on
the circle |tau - 1/2|^2 = 5/4). With the line kept, (1 + i, the mark) is (i, (2/5, 1/5)) by tau -> tau + 1 with
(a, b) -> (a, b - a) read backwards, and (2/5, 1/5) is the mark's mirror, b -> -b. So the second crossing is evaluated
at tau = i (within the author's ruling).

  G1  reported, with a prediction: frame C at (i, (2/5, 1/5)) differs from (i, the mark) (some ratio or |V| entry by
      more than 1e-3): the two crossings are a binary under the frame's covariance.
  G2  (a hypothesis) the mirror is complex conjugation: frame C at (i, (2/5, 1/5)) in the reading S* = conj(S) equals
      (i, the mark) in S (sector ratios and |V|, below 1e-6). If so, the two crossings are mirror images, exchanged by an
      orientation-reversing map that also exchanges S and S*.
  G3  reported: the outputs at (i, (2/5, 1/5)) in S.

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wa1_tau_i_posthoc2.py
"""
import math, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wa1_tau_i as A  # noqa: E402
W, V = A.W, A.V
NS = W.NS


def run(pt, reading):
    if W.LIN is None:
        W.LIN, W.NEAR, W.YMAX = W.end_tables(W.MAIN)
    t = 1j
    c3 = [complex(v) for v in NS["av"](W.mp.mpc(0, 1))]
    L2 = W.L2_of(t)
    S = c3[0] * NS["QI"] + c3[1] * NS["QJ"] + c3[2] * NS["QK"]
    Sr = {"S": S, "St": NS["EPS"] @ np.conj(S) @ NS["EPS"].T, "conjS": np.conj(S)}[reading]
    w = pt[0] * t + pt[1]
    rat, U = {}, {}
    for sec in ("up", "down", "lep"):
        lf, rf = W.SECT[sec]
        x, yy = NS["twist_of"](NS["SIXY"][lf] * w, t), NS["twist_of"](NS["SIXY"][rf] * w, t)
        R = NS["residues"](x, yy, t); c = NS["cA"](x, yy, t, R); a0 = NS["a0_of"](x, yy, t, R)
        u = {}
        for s in NS["UNITS"]:
            N = 2 * math.pi * L2 + c[s] - math.pi * abs(a0[s]) ** 2 * math.exp(-2 * L2) if c[s] is not None and a0[s] is not None else -1
            u[s] = math.sqrt(N) * R[s] if N > 0 else 0
        Y = NS["coupling"](Sr, NS["weighted_M"](u))
        sv = np.linalg.svd(Y, compute_uv=False)
        rat[sec] = (sv[1] / sv[0], sv[2] / sv[0])
        U[sec] = np.linalg.svd(Y)[0][:, ::-1]
    Vm = np.abs(np.conj(U["up"].T) @ U["down"])
    return rat, Vm


def dev(a, b):
    r = max(abs(a[0][s][i] / b[0][s][i] - 1) for s in a[0] for i in (0, 1))
    return r, float(np.max(np.abs(a[1] - b[1])))


def main():
    m = run(A.MARK, "S")
    x = run((0.4, 0.2), "S")
    xs = run((0.4, 0.2), "conjS")
    g1 = dev(x, m)
    g2 = dev(xs, m)
    A.say("G1: (i, (2/5, 1/5)) against (i, mark), reading S: ratios %.2e, |V| %.2e | differ: %s" % (g1[0], g1[1], max(g1) > 1e-3))
    A.say("G2: (i, (2/5, 1/5)) in S* against (i, mark) in S: ratios %.2e, |V| %.2e | holds: %s" % (g2[0], g2[1], max(g2) < 1e-6))
    A.say("G3: the outputs at (i, (2/5, 1/5)) in S, printed and compared with nothing:")
    for s in x[0]:
        A.say("   %-4s r2 %.6g  r3 %.6g" % (s, x[0][s][0], x[0][s][1]))
    A.say("   |V| (up S, down S): %s" % "  ".join(" ".join("%.4g" % v for v in row) for row in x[1]))


if __name__ == "__main__":
    main()
