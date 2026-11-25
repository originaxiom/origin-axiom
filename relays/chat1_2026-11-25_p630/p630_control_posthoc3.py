#!/usr/bin/env python3
"""POST HOC, third (written after p630_control_posthoc2_out.txt was read): arithmetic on the recorded level-2
amplitudes only; reads no file, the numbers are copied from p630_control_out.txt and p630_control_posthoc2_out.txt.

    python3 -I p630_control_posthoc3.py

The reading after the second diagnostic: <2|V|0> = a N^(-1/5) + b + c / N, a constant term b besides epsilon''s
N^(-1/5), with b of either sign by direction. The script fits, for V_mu (N = 12 to 36) and V_2 (N = 24 to 36):
  (i)   the three-term model with the exponent fixed at -1/5;
  (ii)  the same with the exponent free (scanned in [-0.6, -0.01], step 1e-4);
  (iii) a model without the constant, a N^s + c / N + d / N^2, s free.
and prints the rms residuals. No expectation is stated: this is a reading, not a test.
"""
import numpy as np

VMU = {12: 1.118025e-01, 14: 1.144703e-01, 16: 1.164112e-01, 18: 1.178792e-01, 20: 1.190223e-01,
       22: 1.199325e-01, 24: 1.206701e-01, 26: 1.212761e-01, 28: 1.217796e-01, 30: 1.222015e-01,
       32: 1.225577e-01, 34: 1.228600e-01, 36: 1.231177e-01}
V2 = {24: 3.013054e-01, 26: 2.942344e-01, 28: 2.877582e-01, 30: 2.817991e-01, 32: 2.762917e-01,
      34: 2.711812e-01, 36: 2.664212e-01}


def lsq(cols, y):
    A = np.stack(cols, 1)
    c = np.linalg.lstsq(A, y, rcond=None)[0]
    return c, np.sqrt(np.mean((y - A @ c) ** 2))


for name, d in (("V_mu", VMU), ("V_2", V2)):
    N = np.array(sorted(d), float)
    y = np.array([d[k] for k in sorted(d)])
    c, r = lsq([N ** -0.2, np.ones_like(N), 1 / N], y)
    print("%-4s (i)   s = -0.2 fixed: a %+.5f  b %+.5f  c %+.5f   rms %.1e" % (name, *c, r))
    best = min(((lsq([N ** s, np.ones_like(N), 1 / N], y)[1], s) for s in np.arange(-0.6, -0.01, 1e-4)))
    c, r = lsq([N ** best[1], np.ones_like(N), 1 / N], y)
    print("%-4s (ii)  s free: s %.4f (h %.4f)  a %+.5f  b %+.5f  c %+.5f   rms %.1e"
          % (name, best[1], (1 - best[1]) / 2, *c, r))
    best = min(((lsq([N ** s, 1 / N, 1 / N ** 2], y)[1], s) for s in np.arange(-0.6, 0.3, 1e-4)))
    print("%-4s (iii) no constant, s free: s %.4f (h %.4f)   rms %.1e" % (name, best[1], (1 - best[1]) / 2, best[0]))
