"""W101, POST HOC: why C1 failed, and C1 recomputed with theta2's branch taken explicitly.

Written after W101's single run was read (b1f77ade9). It changes no cell: C1 stays FAILED as worded.
- (i) Every C1 mismatch is checked against |Re(gamma tau)| > 1. mpmath's jtheta(2, 0, q) takes the nome q = e^{i pi tau}
  and uses the principal q^{1/4}, which equals e^{i pi tau / 4} only when |Re tau| < 1.
- (ii) C1 is recomputed with theta2(tau) = 2 sum_{n>=0} e^{i pi tau (n + 1/2)^2}, which carries no branch.

Run from the repository root: python3 docs/dossiers/the_weave_2026-10-07/the_weaves_anomaly_posthoc.py
"""
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 30
HERE = Path(__file__).resolve().parent
RUN = json.loads((HERE / "the_weaves_anomaly.json").read_text(encoding="utf-8"))
C1 = RUN["C1 det Y1(gamma tau) / ((c tau + d)^3 det Y1(tau)) against det rho(gamma)^-2"]["words"]


def th2_branchfree(tau):
    return 2 * mp.nsum(lambda n: mp.exp(1j * mp.pi * tau * (n + mp.mpf(1) / 2) ** 2), [0, mp.inf])


def detY1(tau, branchfree):
    q = mp.exp(1j * mp.pi * tau)
    t2 = th2_branchfree(tau) if branchfree else mp.jtheta(2, 0, q)
    t3, t4 = mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    a, b, c = t4 ** 2, t3 ** 2, t2 ** 2
    return mp.det(mp.matrix([[0, a, b], [a, 0, c], [b, c, 0]]))


w24 = lambda k: mp.exp(2j * mp.pi * mp.mpf(k) / 24)
RT = mp.matrix([[w24(21) * 1j, 0, 0], [0, 0, w24(21)], [0, w24(21), 0]])
RS = mp.exp(-1j * mp.pi * 21 / 4) * (-1j) * mp.matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
T2, S2, R2 = mp.matrix([[1, 1], [0, 1]]), mp.matrix([[0, -1], [1, 0]]), mp.matrix([[1, 0], [1, 1]])
GEN = {"t": (T2, RT), "s": (S2, RS), "L": (T2, RT), "R": (R2, RS * RT ** -1 * RS ** -1)}
TAUS = [mp.mpc(0.137, 1.291), mp.mpc(-0.284, 2.173), mp.mpc(0.41, 0.95)]

out, pattern_ok, worst_bf, n = {}, True, mp.mpf(0), 0
for key in C1:
    w, inv = (key[:-3], True) if key.endswith("^-1") else (key, False)
    M, P = mp.eye(2), mp.eye(3)
    for ch in w:
        A, B = GEN[ch]
        M, P = M * A, P * B
    if inv:
        M, P = M ** -1, P ** -1
    pred = mp.det(P) ** -2
    rows = []
    for tau, rec in zip(TAUS, C1[key]["measured at three tau"]):
        a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
        gt = (a * tau + b) / (c * tau + d)
        recorded = mp.mpc(complex(rec.strip("()").replace(" ", "")))
        mismatch = abs(recorded - pred) > mp.mpf("1e-6")
        pattern_ok &= mismatch == (abs(mp.re(gt)) > 1)
        bf = detY1(gt, True) / ((c * tau + d) ** 3 * detY1(tau, True))
        worst_bf = max(worst_bf, abs(bf - pred))
        n += 1
        rows.append({"Re(gamma tau)": mp.nstr(mp.re(gt), 6), "recorded mismatch": bool(mismatch),
                     "branch-free measurement": mp.nstr(bf, 8)})
    out[key] = {"det rho^-2": mp.nstr(pred, 8), "at the three tau": rows}

OUT = {"what": "W101 POST HOC: C1's failure explained and C1 recomputed branch-free (no cell changed)",
       "cases": n, "every recorded mismatch is exactly a case with |Re(gamma tau)| > 1": bool(pattern_ok),
       "branch-free: worst |measured - det rho^-2| over all cases": mp.nstr(worst_bf, 3), "cases detail": out}
(HERE / "the_weaves_anomaly_posthoc.json").write_text(json.dumps(OUT, indent=1, ensure_ascii=False) + "\n",
                                                      encoding="utf-8")
print(json.dumps({k: v for k, v in OUT.items() if k != "cases detail"}, indent=1))
