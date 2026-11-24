#!/usr/bin/env python3
"""Post hoc, labelled, exploratory: M3 as agy-002 states and tests it takes H_u = conj(h) . sigma (the one-doublet
charge rule). This run asks whether the same floor holds when both sectors read the same Higgs, H_u = H_d = h . sigma,
as in the all-S world. It is outside M3's claim, so a violation would scope M3, not refute it. Expected before the
run: no violation (50 %). Data-free.
"""
import numpy as np

src = open(__file__.replace("_scope", "")).read().split("N = 240000")[0]
ns = {}
exec(src, ns)
SIG, Ymat, Ffloor = ns["SIG"], ns["Ymat"], ns["Ffloor"]


def evaluate_same(h, Mu, Md):
    H = sum(h[k] * SIG[k] for k in range(3))
    Uu, su, _ = np.linalg.svd(Ymat(H, Mu))
    Ud, sd, _ = np.linalg.svd(Ymat(H, Md))
    rho = max(su[1] / su[0], sd[1] / sd[0])
    a = abs(np.vdot(Uu[:, 0], Ud[:, 0]))
    r = abs(h @ h) / np.vdot(h, h).real
    t = r / (1 + np.sqrt(max(0.0, 1 - r * r)))
    _, _, Vhu = np.linalg.svd(Mu)
    _, _, Vhd = np.linalg.svd(Md)
    ru, rd = Vhu[0].conj(), Vhd[0].conj()
    return rho, Ffloor(t, abs(ru[0] * rd[1] - ru[1] * rd[0]), a), t, a


viol, worst, rec = 0, np.inf, None
for n in range(60000):
    h, Mu, Md = ns["sample"](n % 6)
    rho, F, t, a = evaluate_same(h, Mu, Md)
    if rho < F - 1e-9:
        viol += 1
    if rho - F < worst:
        worst, rec = rho - F, (rho, F, t, a)
print("same Higgs in both sectors: trials 60000, violations %d, least margin %.3e at (rho, F, t, a) = %s"
      % (viol, worst, tuple(round(float(v), 6) for v in rec)))
