#!/usr/bin/env python3
"""W-C6, post hoc 1, written after the sealed run and committed before its own run.

The sealed run's A1 failed as written: the residual N - [F_u + pi log y - 2 pi (gamma + log pi)] was the same
constant, -4.355172, at all twelve points (fit misfit 9e-12). 2 pi log 2 = 4.3551721806... This file tests the one
reading, written here before the run: N(c, tau) = F_u(tau) + pi log y - 2 pi (gamma + log 2 pi), within 1e-9 at every
point, with this seat's definitions of the sealed file unchanged (they are imported from it, so the sealed run's
B part runs again too and its output is ignored).

    python3 -I -u wc6_posthoc_1.py
"""
import contextlib, io, runpy, pathlib
import numpy as np, mpmath as mp

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    g = runpy.run_path(str(pathlib.Path(__file__).with_name("wc6_checks.py")))
EG = float(mp.euler)
worst = 0.0
for c, tau, n2, *_ in g["rows"]:
    claim = g["F"](c[0] - 0.5, c[1] - 0.5, tau) + np.pi * np.log(tau.imag) - 2 * np.pi * (EG + np.log(2 * np.pi))
    print("c", c, "tau", tau, "N - claim %.2e" % (n2 - claim), flush=True)
    worst = max(worst, abs(n2 - claim))
print("constant -2 pi (gamma + log 2 pi) holds within 1e-9 at all points:", worst < 1e-9, "; largest %.2e" % worst)
