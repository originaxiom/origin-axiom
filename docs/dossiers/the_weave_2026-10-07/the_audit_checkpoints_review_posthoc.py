#!/usr/bin/env python3
"""W144, POST HOC (after the one run's read-out, which found A2, A4, C1 and C2 failed and the other seven cells
held). Nothing here was in the rule.

  P1  the diagnosis: mpmath's jtheta(n, z, q) for n = 1, 2 carries the principal fourth root of q, which equals
      exp(pi i tau/4) only for -1 < Re tau <= 1. At every (n, tau) the failed cells evaluate, the ratio of jtheta to
      the explicit series sum exp(pi i tau (m + 1/2)^2) (...) is i^(-k), with k the integer that puts Re tau - 2k in
      (-1, 1]; theta_3 and theta_4 agree exactly
  P2  the eleven cells re-run unchanged, with theta_n and theta_1' replaced by the explicit series

    python3 -B the_audit_checkpoints_review_posthoc.py      # writes the_audit_checkpoints_review_posthoc.json
"""
import contextlib
import io
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_audit_checkpoints_review as W  # noqa: E402  (W144's committed script, its cells unchanged)

OUT = HERE / "the_audit_checkpoints_review_posthoc.json"
I = mp.mpc(0, 1)
JTH, JDTH1 = W.th, W.dth1


def _series(n, z, tau, deriv=False):
    """theta_n(z|tau) with periods 1 and tau, as explicit sums; deriv gives d/dz of theta_1"""
    eps = mp.mpf(10) ** (-(mp.mp.dps + 10))
    start = mp.ceil(abs(mp.im(z)) / mp.im(tau)) + 3
    s, m = mp.mpc(0), 0
    while True:
        if n in (1, 2):
            e = mp.exp(I * mp.pi * tau * (m + mp.mpf(1) / 2) ** 2)
            arg = (2 * m + 1) * mp.pi * z
            if n == 1:
                t = (-1) ** m * e * ((2 * m + 1) * mp.pi * mp.cos(arg) if deriv else mp.sin(arg))
            else:
                t = e * mp.cos(arg)
            t *= 2
        else:
            if m == 0:
                t = mp.mpc(1)
            else:
                t = 2 * mp.exp(I * mp.pi * tau * m * m) * mp.cos(2 * m * mp.pi * z) * ((-1) ** m if n == 4 else 1)
        s += t
        if m > start and abs(t) < eps * max(abs(s), 1):
            return s
        m += 1


def th_x(n, z, tau):
    return _series(n, z, tau)


def dth1_x(z, tau):
    return _series(1, z, tau, deriv=True)


def predicted_ratio(tau):
    k = 0
    while mp.re(tau) - 2 * k > 1:
        k += 1
    while mp.re(tau) - 2 * k <= -1:
        k -= 1
    return I ** (-k)


def P1():
    calls = []

    def logged(n, z, tau):
        calls.append((n, z, tau))
        return JTH(n, z, tau)

    W.th = logged
    with contextlib.redirect_stdout(io.StringIO()):
        for fn in (W.A2, W.A4):
            fn()
        W.C1C2()
    W.th = JTH
    seen, worst, off_strip, n34 = {}, mp.mpf(0), 0, mp.mpf(0)
    for n, z, tau in calls:
        key = (n, mp.nstr(tau, 12))
        if key in seen:
            continue
        seen[key] = True
        ratio = JTH(n, z, tau) / th_x(n, z, tau)
        if n in (1, 2):
            worst = max(worst, abs(ratio - predicted_ratio(tau)))
            off_strip += int(abs(predicted_ratio(tau) - 1) > 0)
        else:
            n34 = max(n34, abs(ratio - 1))
    return {"theta calls in A2, A4, C1 and C2": len(calls), "distinct (n, tau)": len(seen),
            "of them theta_1 or theta_2 with Re tau outside (-1, 1]": off_strip,
            "max |jtheta / series - i^(-k)| over theta_1 and theta_2": mp.nstr(worst, 3),
            "max |jtheta / series - 1| over theta_3 and theta_4": mp.nstr(n34, 3)}, worst < W.TOL and n34 < W.TOL


def P2():
    W.th, W.dth1 = th_x, dth1_x
    res, cells = {}, {}
    with contextlib.redirect_stdout(io.StringIO()):
        for name, fn in (("A1", W.A1), ("A2", W.A2), ("A3", W.A3), ("A4", W.A4), ("B1", W.B1), ("B2", W.B2)):
            res[name], cells[name] = fn()
        c1, cells["C1"], c2, cells["C2"] = W.C1C2()
        res["C1"], res["C2"] = c1, c2
        res["D1"], cells["D1"] = W.D1()
        e1, cells["E1"], e2, cells["E2"] = W.E1E2()
        res["E1"], res["E2"] = e1, e2
    W.th, W.dth1 = JTH, JDTH1
    return res, {k: bool(v) for k, v in cells.items()}


def main():
    p1, p1_ok = P1()
    p2, cells = P2()
    out = {"arc": "W144", "status": "POST HOC, after the read-out", "P1 the diagnosis": p1, "P1 holds": bool(p1_ok),
           "P2 cells with the explicit series": cells,
           "P2 the failed cells' read-outs": {k: p2[k] for k in ("A2", "A4", "C1", "C2")}}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"P1 holds": out["P1 holds"], "P2 cells": cells}, indent=1))


if __name__ == "__main__":
    main()
