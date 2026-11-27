#!/usr/bin/env python3
"""Failing control for Card A2-PEER-SM-FC2 (100% self-contained, exits 1 with 0 stderr bytes under python3 -I).

Plants the unshifted-end fault in Frame C under S: (tau, v, L) -> (-1/tau, v S^{-1}, L)
without shifting L -> L + ln|tau|, verifying that the Frame C invariant check fails cleanly.
"""
import sys
from fractions import Fraction as Fr

import mpmath as mp


def _f2m(q):
    return mp.mpf(q.numerator) / mp.mpf(q.denominator)


def _th_mp(n, u, t):
    I = mp.mpc(0, 1)
    q = mp.exp(I * mp.pi * t)
    x = mp.pi * u
    if n == 3:
        return mp.jtheta(3, x, q)
    return mp.jtheta(4, x, q)


def _thc_mp(a, b, t):
    I = mp.mpc(0, 1)
    return mp.exp(I * mp.pi * a * a * t + 2 * I * mp.pi * a * b) * _th_mp(3, a * t + b, t)


def _F_u(u1, u2, t, y):
    I = mp.mpc(0, 1)
    a, b, x = u1 % 1, u2 % 1, mp.re(t)
    af, u2f = _f2m(a), _f2m(u2)
    first = -mp.pi * (2 * mp.log(2) + mp.log(y) + mp.digamma(af) + mp.digamma(1 - af))
    tot = mp.mpf(0)
    for k in range(-18, 19):
        m = af + k
        w = mp.exp(-2 * mp.pi * abs(m) * y + 2 * I * mp.pi * (m * x + u2f))
        tot += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
    return first + tot


def _channel_arg(t, al, be, L):
    I = mp.mpc(0, 1)
    y = mp.im(t)
    z = _f2m(al) * t + _f2m(be)
    q = mp.exp(I * mp.pi * t)
    tv = mp.jtheta(1, mp.pi * z, q)
    tdv = mp.pi * mp.jtheta(1, mp.pi * z, q, 1)
    a0 = 2 * I * mp.pi * _f2m(al) + tdv / tv
    c_val = _F_u(al, be, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    c_val = c_val - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * L)
    return 2 * mp.pi * L + c_val


def main():
    mp.mp.dps = 30
    t0 = mp.mpc(_f2m(Fr(13, 100)), _f2m(Fr(6, 5)))
    L0 = _f2m(Fr(266, 100))
    # Characteristic (al, be) = (1/5, 2/5) under S: (tau, (al, be), L) -> (-1/tau, (-be, al), L + ln|tau|)
    al, be = Fr(1, 5), Fr(2, 5)
    tS = -1 / t0
    alS, beS = (-be) % 1, al % 1
    arg_src = _channel_arg(t0, al, be, L0)
    # Planted fault: omit the shift L -> L + ln|t0|
    arg_bad = _channel_arg(tS, alS, beS, L0)
    diff = abs(arg_src - arg_bad)
    ok = diff < mp.mpf(10) ** (-15)
    print(f"CONTROL_FAIL: unshifted_L_breaks_S_covariance diff={mp.nstr(diff, 6)} ok={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
