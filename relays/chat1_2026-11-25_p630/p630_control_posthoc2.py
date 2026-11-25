#!/usr/bin/env python3
"""POST HOC, second (written after p630_control_posthoc_out.txt was read): does the epsilon' read-out move toward
h = 3/5 at larger rings? Uses p630_control.py's chain. Data-free; reads no file except the sibling script.

    python3 -I p630_control_posthoc2.py

For V_mu = sum_i n_i and V_2 = sum_i n_i n_{i+2} (n_i = 1 - l_i; the two directions of p630_control_posthoc.py
whose epsilon' read-outs fell on either side of 3/5), at N = 24, 26, ..., 36 it prints <1|V|0>, <2|V|0> and the
local h between successive sizes, h = (1 - d ln|A| / d ln N) / 2.
Stated before the run, as a reading rule rather than an expectation with a probability: if both directions' local
h for level 2 approach 3/5 from either side as N grows, the failure of A2 is slow convergence; if either moves away
from 3/5, the read-out of epsilon' along that direction carries a second contribution with its own exponent.
"""
import importlib.util
import pathlib
import sys

import numpy as np

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("ctl", pathlib.Path(__file__).resolve().parent / "p630_control.py")
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def op_V2(X, A, i, N):
    return X, A * (1 - ((X >> (i % N)) & 1)) * (1 - ((X >> ((i + 2) % N)) & 1))


sizes = list(range(24, 37, 2))
rows = []
for N in sizes:
    ch = C.Chain(N)
    H0 = ch.matrix(0, C.op_H)
    E, U = C.low(H0, 3)
    g = U[:, 0]
    a = []
    for M in (ch.matrix(0, None), ch.matrix(0, op_V2)):
        Mg = M @ g
        a += [abs(U[:, 1] @ Mg), abs(U[:, 2] @ Mg)]
    rows.append(a)
    print("N=%d dim0 %d  x_2 = %.5f  V_mu: %.6e %.6e  V_2: %.6e %.6e"
          % (N, H0.shape[0], 0.2 * (E[2] - E[0]) / (E[1] - E[0]), *a), flush=True)
rows = np.array(rows)
print()
for k in range(1, len(sizes)):
    d = np.log(sizes[k]) - np.log(sizes[k - 1])
    h = [(1 - (np.log(rows[k, c]) - np.log(rows[k - 1, c])) / d) / 2 for c in range(4)]
    print("local h at N = %d, %d:  V_mu level 1 %.5f, level 2 %.5f;  V_2 level 1 %.5f, level 2 %.5f"
          % (sizes[k - 1], sizes[k], *h))
