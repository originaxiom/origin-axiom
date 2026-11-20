#!/usr/bin/env python3
"""W-H1, post hoc (labelled; written after H3 was seen to fail, committed before this script is run). Data-free.
For each component c_i of the frame's triplet: the ratio conj(c_i(tau)) / c_i(-conj(tau)) at three values of tau.
If every ratio is a constant of modulus 1, S~ is S at the mirror point up to a fixed phase per component.

    python3 -I wh1_posthoc.py <a checkout of main>
"""
import os
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wh1_run as R  # noqa: E402

mp.mp.dps = 40
for tau in (mp.mpc("0.13", "1.5"), mp.mpc("0.31", "3"), mp.mpc("0.13", "6")):
    c = [R.te.ev(cc, tau) for cc in R.te.B[1]]
    cm = [R.te.ev(cc, mp.mpc(-mp.re(tau), mp.im(tau))) for cc in R.te.B[1]]
    print("tau = %s:" % mp.nstr(tau, 4), "  ".join("c%d: %s" % (i + 1, mp.nstr(mp.conj(c[i]) / cm[i], 10))
                                             for i in range(3)))
