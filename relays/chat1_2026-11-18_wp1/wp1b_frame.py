#!/usr/bin/env python3
"""W-P1, step 2: frame C's own Gramians in both Weil classes (W-P1b-H). Data-free: nothing is compared with data or with
any value on record (the author's ruling of 2026-11-15, morning: frame C's outputs may be computed and printed).

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wp1b_frame.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, "Step 2, frame C's own Gramians in both classes" (committed
before this script). The frame is this seat's transcription (W-F24's wf24_run.py, W-F26's couplings, as W-A1 used
them); main's code is not run, and main's JSON tables of the end are read as W-F24 reads them. The Weil
representations and the Weyl operators are wp1b_class_test.py's and B1953's: D(a, b) = psi(3ab) X^a Z^b.

  K1  Y(tau, -w) = Y(tau, w); the 15 singular values of O_K at tau + 1 against tau, K = I (class 2) and
      K = diag(1, 3) (class 1); the same without the table (a plant: it must move);
  K2  ||S_1 - S_2|| / ||S_1|| (largest entries);
  K3  the ratios of G_3, G_2 and the plain Gramian, in both classes; the largest difference of the classes' G_3 ratios.
At tau = 0.13 + 1.7i and 0.31 + 1.2i, the down sector, readings S and St.
"""
import math
import os
import sys
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(R, "chat1_2026-11-15_wf24"))
sys.path.insert(0, os.path.join(R, "chat1_2026-11-15_wf26"))
import wf24_run as W  # noqa: E402
import wf26_run as V  # noqa: E402

CT = {"__file__": os.path.join(HERE, "wp1b_class_test.py")}
_src = open(CT["__file__"]).read()
exec(compile(_src[:_src.index("Gs = {a: group(a)")], "wp1b_class_test.py", "exec"), CT)
z, Xs, Zs, P = CT["z"], CT["Xs"], CT["Zs"], CT["P"]
psi = lambda x: z ** (x % 5)
PTS = [(i, j) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
E3, E2 = (np.eye(5) + P) / 2, (np.eye(5) - P) / 2
KS = {"class 2 (K = I)": np.eye(2, dtype=int), "class 1 (K = diag(1, 3))": np.array([[1, 0], [0, 3]])}
BASES = (0.13 + 1.7j, 0.31 + 1.2j)


def Dw(v):
    p, q = int(v[0]) % 5, int(v[1]) % 5
    return psi(3 * p * q) * np.linalg.matrix_power(Xs, p) @ np.linalg.matrix_power(Zs, q)


def say(*a):
    print(*a, flush=True)


def job(arg):
    t, i, j, L2, c3 = arg
    Y = V.couplings(t, i / 5, j / 5, L2, c3)
    return (t, i, j), (np.array(Y[("down", "S")], complex), np.array(Y[("down", "St")], complex))


def O_of(A, K):
    return sum(np.kron(A[v], Dw(K @ np.array(v))) for v in PTS)


def gram(O, E):
    return np.einsum("ixkx->ik", (O @ np.kron(np.eye(3), E) @ O.conj().T).reshape(3, 5, 3, 5))


def ratios(H):
    e = np.sort(np.abs(np.linalg.eigvalsh((H + H.conj().T) / 2)))[::-1]
    return [float(np.sqrt(e[1] / e[0])), float(np.sqrt(e[2] / e[0]))]


def omega(v, w):
    return (v[0] * w[1] - v[1] * w[0]) % 5


def S_j(A, j):
    return sum(A[v] @ A[w].conj().T for v in PTS for w in PTS if omega(v, w) in (j, (-j) % 5))


def sv(O):
    return np.linalg.svd(O, compute_uv=False)


def main():
    W.LIN, W.NEAR, W.YMAX = W.end_tables(W.MAIN)
    jobs = []
    for t0 in BASES:
        L2 = W.L2_of(t0)
        for t in (t0, t0 + 1):
            c3 = [complex(v) for v in W.NS["av"](W.mp.mpc(t.real, t.imag))]
            jobs += [(t, i, j, L2, c3) for i, j in PTS]
    with Pool(max(1, min(4, os.cpu_count() or 1))) as pool:
        res = dict(pool.map(job, jobs, chunksize=1))
    for t0 in BASES:
        for k, rd in enumerate(("S", "St")):
            Y0 = {v: res[(t0, v[0], v[1])][k] for v in PTS}
            Y1 = {v: res[(t0 + 1, v[0], v[1])][k] for v in PTS}
            scale = max(np.abs(Y0[v]).max() for v in PTS)
            even = max(np.abs(Y0[((-v[0]) % 5, (-v[1]) % 5)] - Y0[v]).max() for v in PTS) / scale
            A0 = {v: psi(-v[0] * v[1]) * Y0[v] for v in PTS}
            A1 = {v: psi(-v[0] * v[1]) * Y1[v] for v in PTS}
            head = "tau = %.2f%+.2fi, down, %-2s" % (t0.real, t0.imag, rd)
            say("%s: K1 Y(tau, -w) against Y(tau, w): %.1e (relative)" % (head, even))
            for name, K in KS.items():
                s0, s1 = sv(O_of(A0, K)), sv(O_of(A1, K))
                p0, p1 = sv(O_of(Y0, K)), sv(O_of(Y1, K))
                say("%s: K1 %s: singular values at tau + 1 against tau: %.1e; without the table (the plant): %.1e" % (
                    head, name, np.abs(s1 - s0).max() / s0[0], np.abs(p1 - p0).max() / p0[0]))
            s1m, s2m = S_j(A0, 1), S_j(A0, 2)
            say("%s: K2 ||S_1 - S_2|| / ||S_1||: %.3e" % (head, np.abs(s1m - s2m).max() / np.abs(s1m).max()))
            g = {}
            for name, K in KS.items():
                O = O_of(A0, K)
                g[name] = (gram(O, E3), gram(O, E2))
            plain = sum(A0[v] @ A0[v].conj().T for v in PTS)
            n2, n1 = list(KS)
            cf = np.abs((g[n1][0] - g[n2][0]) - np.sqrt(5) / 4 * (s1m - s2m)).max() / np.abs(g[n2][0]).max()
            d3 = max(abs(x - y) for x, y in zip(ratios(g[n1][0]), ratios(g[n2][0])))
            d2 = max(abs(x - y) for x, y in zip(ratios(g[n1][1]), ratios(g[n2][1])))
            say("%s: K3 plain Gramian ratios %s" % (head, ["%.6f" % x for x in ratios(plain)]))
            for name in KS:
                say("%s: K3 %s: G_3 ratios %s, G_2 ratios %s" % (head, name, ["%.6f" % x for x in ratios(g[name][0])],
                                                                 ["%.6f" % x for x in ratios(g[name][1])]))
            say("%s: K3 the classes' G_3 ratios differ by at most %.3e, G_2's by %.3e; the closed form "
                "(sqrt 5/4)(S_1 - S_2) holds to %.1e (relative)" % (head, d3, d2, cf))


if __name__ == "__main__":
    main()
