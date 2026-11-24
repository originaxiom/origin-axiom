#!/usr/bin/env python3
"""The control that must fail if fd_rank.py's measure cannot see rank one. Sealed and dependency-free like fd_rank.py,
which it imports from the same folder. Data-free.

    python3 -I fd_rank_control.py

The same measure (gradients in Re tau and Im tau, the same drops, the largest |sin| between two kept gradients) is
applied to the frame's outputs with Re tau frozen at the base point, so that every output depends on tau through
Im tau alone. Then every branch has rank one.

Expectation, written before the run: on the lines (1/7, 2/7) and (2/5, 1/10) at tau = 0.13 + 2.2i, every branch's
largest |sin| is below 1e-6 (95 %).
"""
import contextlib
import importlib.util
import io
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("fd_rank", pathlib.Path(__file__).resolve().parent / "fd_rank.py")
FD = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FD)


def frozen(tau, line, x0):
    with contextlib.redirect_stdout(io.StringIO()):
        return FD.outs(complex(x0, tau.imag), line)


h = 1e-5
worst = 0.0
count = 0
for line in ((Fr(1, 7), Fr(2, 7)), (Fr(2, 5), Fr(1, 10))):
    tau = complex(0.13, 2.2)
    o0 = frozen(tau, line, tau.real)
    ox = (frozen(tau + h, line, tau.real), frozen(tau - h, line, tau.real))
    oy = (frozen(tau + 1j * h, line, tau.real), frozen(tau - 1j * h, line, tau.real))
    for k in o0:
        if not all(k in d for d in (*ox, *oy)):
            continue
        keep = np.array([v > 1e-6 for v in o0[k][1]] + [True])
        G = np.stack([(ox[0][k][0] - ox[1][k][0]) / (2 * h), (oy[0][k][0] - oy[1][k][0]) / (2 * h)], 1)[keep]
        n = np.linalg.norm(G, axis=1)
        G = G[n > 1e-8] / n[n > 1e-8][:, None]
        s = max((abs(G[i, 0] * G[j, 1] - G[i, 1] * G[j, 0]) for i in range(len(G)) for j in range(i + 1, len(G))),
                default=0.0)
        worst = max(worst, s)
        count += 1
print("control: %d branches with Re tau frozen; largest |sin| between two kept gradients %.2e; rank one seen on all: %s"
      % (count, worst, worst < 1e-6))
