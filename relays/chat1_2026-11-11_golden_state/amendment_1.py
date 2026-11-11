#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
AMENDMENT 1 to the sealed card golden_state_peak.py (sha256 03d96e37...; sealed and pushed at f89d8f78c).
The web seat (chat1), 2026-11-11.  In its own file, committed before it is run.

WHAT HAPPENED.  The sealed run stopped at its first cell and declared the card void: control G0(c) compares the
coefficients c(n), n <= 60, computed two ways, and found them agreeing to 2.1e-25 against a sealed tolerance of
1e-30.  Controls G0(a) and G0(b) held.  Nothing after G0 ran, so no cell on the form, its zeros or its peak has
been seen.

THE FAULT, which is the seat's.  The enumeration in G0(c) rounds a logarithm to 25 digits so that two generators
of one ideal get the same key.  It then computed the coefficient from the rounded number.  So the control itself
could not agree with the Euler product to better than about 1e-25, and its tolerance of 1e-30 could not be met.

THE CHANGE, and nothing else.  The enumeration keeps the rounded number for the key and computes the coefficient
from the unrounded one.  The sealed script is imported unchanged, with every cell, prediction and tolerance as
sealed; only this helper of the control is replaced.  If the two computations still disagree beyond 1e-30 the card
is void and stays so.
"""
import os
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import golden_state_peak as g  # noqa: E402


def direct_coefficients(nmax, box=48):
    seen = {}
    scale = mp.mpf(10) ** 25
    for a in range(-box, box + 1):
        for b in range(-box, box + 1):
            n = g.norm(a, b)
            if n == 0 or abs(n) > nmax:
                continue
            al = a + b * g.PHI
            alc = a + b * g.PHIC
            u = mp.log(abs(al / alc)) / (2 * g.LNPHI)
            ur = mp.nint(u * scale) / scale
            k = mp.floor(ur)
            s0 = (1 if n > 0 else -1) * (1 if int(k) % 2 == 0 else -1)
            key = (abs(n), mp.nstr(ur - k, 22))
            val = s0 * mp.cos(mp.pi * (u - k))
            if key in seen:
                if abs(seen[key] - val) > mp.mpf(10) ** -30:
                    raise SystemExit('enumeration: two generators of one ideal disagree at norm %d' % abs(n))
            else:
                seen[key] = val
    count = [0] * (nmax + 1)
    coef = [mp.mpf(0)] * (nmax + 1)
    for (n, _), val in seen.items():
        count[n] += 1
        coef[n] += val
    return count, coef


if __name__ == '__main__':
    print('AMENDMENT 1: the sealed card with the control\'s enumeration corrected; all else as sealed')
    g.direct_coefficients = direct_coefficients
    sys.exit(g.main())
