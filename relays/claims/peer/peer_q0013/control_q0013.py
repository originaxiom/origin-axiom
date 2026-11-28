#!/usr/bin/env python3
"""Standalone non-vacuous failing control for peer review of Q0013 (P-631).

Evaluates the stationary point of V(i y) = -E_3(i y) + 0.01 E_2(i y)^2 via elementary rational
q-series Newton iteration on y in [1.2, 300] under the deliberately corrupted selection bound
|V_2 / V_1| <= 1 (instead of <= 1/3). Finds y_* = 102.3138 with |V_2 / V_1| = 0.750002 <= 1,
violating the exclusion claim as required, and exits 1 with zero stderr bytes and zero file writes.
"""
import math
import sys
import mpmath as mp

mp.mp.dps = 30


def eis_q(s: int, y_val: mp.mpf) -> mp.mpf:
    m = s - 1
    binom_2m = math.comb(2 * m, m)
    c0 = (
        2 * mp.zeta(2 * s) * ((y_val / mp.pi) ** s)
        + 2 * (mp.pi * mp.mpf(binom_2m) / (4 ** m)) * mp.zeta(2 * s - 1) / (mp.pi ** s) * (y_val ** (1 - s))
    )
    q = mp.exp(-2 * mp.pi * y_val)
    osc = mp.mpf(0)
    qd = q
    for d in range(1, 25):
        if qd < mp.mpf("1e-32"):
            break
        if s == 2:
            osc += (qd / ((1 - qd) ** 2)) / (d ** 2) + (qd / (1 - qd)) / (2 * mp.pi * y_val * (d ** 3))
        else:
            osc += (
                (qd * (1 + qd) / ((1 - qd) ** 3)) / (d ** 3)
                + 3 * (qd / ((1 - qd) ** 2)) / (2 * mp.pi * y_val * (d ** 4))
                + 3 * (qd / (1 - qd)) / (4 * (mp.pi ** 2) * (y_val ** 2) * (d ** 5))
            )
        qd *= q
    return c0 + (mp.mpf(4) / math.factorial(m)) * osc


def main() -> int:
    r = mp.mpf("0.01")
    c3 = 2 * mp.zeta(6) / (mp.pi ** 3)
    c2 = 2 * mp.zeta(4) / (mp.pi ** 2)
    y = (3 * c3) / (4 * r * (c2 ** 2))
    h = mp.mpf("1e-6")
    for _ in range(6):
        vp = -eis_q(3, y + h) + r * (eis_q(2, y + h) ** 2)
        v0 = -eis_q(3, y) + r * (eis_q(2, y) ** 2)
        vm = -eis_q(3, y - h) + r * (eis_q(2, y - h) ** 2)
        dv = (vp - vm) / (2 * h)
        d2v = (vp - 2 * v0 + vm) / (h * h)
        y = y - dv / d2v
    ratio = float(abs(r * (eis_q(2, y) ** 2) / eis_q(3, y)))
    corrupted_bound_satisfied = (1.2 <= float(y) <= 300.0) and (ratio <= 1.0)
    if corrupted_bound_satisfied:
        print(f"CONTROL_Q0013: stationary y={float(y):.4f} has |V2/V1|={ratio:.6f} <= 1.0 (expected exit 1)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
