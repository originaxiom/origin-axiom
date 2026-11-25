#!/usr/bin/env python3
"""POST HOC (written after p630_control_out.txt was read): why cell A2 failed. Uses p630_control.py's chain.
Data-free; reads no file except the sibling script it imports.

    python3 -I p630_control_posthoc.py

A2 expected <2| V_mu |0> ~ N^(-1/5) (epsilon', x = 6/5) and found a nearly constant amplitude (fitted h = 0.509).
This script asks three questions, with no expectation stated (it is diagnostic only):
  1. the k = 0 levels 0 to 9: their x = (1/5)(E_n - E_0)/(E_1 - E_0) and the components <n| V_mu |0>;
  2. whether other Y-breaking directions show the same behaviour on level 2:
       V_2 = sum_i n_i n_{i+2}, V_3 = sum_i n_i n_{i+3} (n_i = 1 - l_i), and V_c = sum_i (n_i P_{i+1} + P_{i+1} n_i);
  3. the k = 0 spectrum's x values against the tricritical Ising table, to find any level the labels missed.
"""
import importlib.util
import pathlib
import sys

import numpy as np
import scipy.sparse as sp

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("ctl", pathlib.Path(__file__).resolve().parent / "p630_control.py")
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def diag_op(fn):
    """A diagonal translation-invariant operator sum_i fn(X, i, N) in the k = 0 block, by the same orbit rule."""
    def op(X, A, i, N):
        return X, A * fn(X, i, N)
    return op


def nn(X, i, N, d):
    return (1 - ((X >> (i % N)) & 1)) * (1 - ((X >> ((i + d) % N)) & 1))


def op_Vc(X, A, i, N):
    j = (i + 1) % N
    n_i = lambda Y: 1 - ((Y >> (i % N)) & 1)
    X1, A1 = C.apply_P(X, A, j, N)
    A1 = A1 * n_i(X1)
    X2, A2 = C.apply_P(X, A * n_i(X), j, N)
    return np.concatenate([X1, X2]), np.concatenate([A1, A2])


ops = {"V_2": diag_op(lambda X, i, N: nn(X, i, N, 2)), "V_3": diag_op(lambda X, i, N: nn(X, i, N, 3)),
       "V_c": op_Vc}
sizes = list(range(12, 31, 2))
rec = {k: [] for k in ("V_mu", *ops)}
for N in sizes:
    ch = C.Chain(N)
    H0 = ch.matrix(0, C.op_H)
    E, U = C.low(H0, 10)
    g = U[:, 0]
    x = 0.2 * (E - E[0]) / (E[1] - E[0])
    mats = {"V_mu": ch.matrix(0, None)}
    for k, op in ops.items():
        M = ch.matrix(0, op)
        assert abs(M - M.T).max() < 1e-12
        mats[k] = M
    comps = {k: [U[:, n] @ (M @ g) for n in range(10)] for k, M in mats.items()}
    for k in rec:
        rec[k].append((abs(comps[k][1]), abs(comps[k][2])))
    if N in (12, 20, 30):
        print("N=%d  x_n: %s" % (N, " ".join("%.4f" % v for v in x)))
        for k in mats:
            print("      %-4s <n|V|0>: %s" % (k, " ".join("%+.2e" % v for v in comps[k])))


def slope(F):
    Ns = np.asarray(sizes, float)
    A = np.stack([np.ones_like(Ns), np.log(Ns), 1 / Ns, 1 / Ns ** 2], 1)
    return np.linalg.lstsq(A, np.log(np.asarray(F)), rcond=None)[0][1]


print()
for k, v in rec.items():
    v = np.array(v)
    s1, s2 = slope(v[:, 0]), slope(v[:, 1])
    print("%-4s level 1: h = %.4f   level 2: h = %.4f   (|<2|V|0>| at N = 12 and 30: %.4e, %.4e)"
          % (k, (1 - s1) / 2, (1 - s2) / 2, v[0, 1], v[-1, 1]))
