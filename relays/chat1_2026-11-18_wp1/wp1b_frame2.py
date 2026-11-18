#!/usr/bin/env python3
"""W-P1, step 2: the direct tests (W-P1b-I). Data-free: nothing is compared with data or with any value on record (the
author's ruling of 2026-11-15, morning).

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wp1b_frame2.py

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, "Step 2, the direct tests" (committed before this script).
The couplings and the operators are wp1b_frame.py's: its text is run up to its main.

  L1  Gamma(tau) = tr_families(O_K O_K^dagger) at tau + 1 against rho_a(T) Gamma(tau) rho_a(T)^dagger, for
      K in {I, diag(1, 3), diag(1, 4)} and a in {1, 2};
  L2  rho_a(gamma) D(Kv) rho_a(gamma)^-1 against D(K A(gamma) v) for K in {I, diag(1, 3)}; the counts of K in GL(2, F_5)
      passing gamma (class 1 only, class 2 only, neither) and passing T and S;
  L3  Parseval in each class on frame C;
  L4  O's 15 singular values, each over the largest, in both classes.
"""
import itertools
import os
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HERE, "wp1b_frame.py")).read()
exec(compile(_src[:_src.index("def main():")], "wp1b_frame.py", "exec"))

weil = CT["weil"]
AT = np.array([[1, 0], [-1, 1]]) % 5
AS = np.array([[0, -1], [1, 0]]) % 5


def inv5(M):
    a, b, c, d = (int(x) for x in M.ravel())
    det = (a * d - b * c) % 5
    return (pow(det, -1, 5) * np.array([[d, -b], [-c, a]])) % 5


AG = (AT @ AS @ inv5(AT) @ inv5(AS)) % 5


def rho(a):
    S, T = weil(a)
    return S, T, T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)


def passes(M, Ag, K):
    return max(np.abs(M @ Dw(K @ np.array(v)) @ np.linalg.inv(M) - Dw(K @ (Ag @ np.array(v)))).max() for v in PTS)


def wgram(O):
    return np.einsum("ixiy->xy", (O @ O.conj().T).reshape(3, 5, 3, 5))


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
    R = {a: rho(a) for a in (1, 2)}
    LK = {"I": np.eye(2, dtype=int), "diag(1, 3)": np.array([[1, 0], [0, 3]]), "diag(1, 4)": np.array([[1, 0], [0, 4]])}
    worst = {}
    for t0 in BASES:
        for k, rd in enumerate(("S", "St")):
            A0 = {v: psi(-v[0] * v[1]) * res[(t0, v[0], v[1])][k] for v in PTS}
            A1 = {v: psi(-v[0] * v[1]) * res[(t0 + 1, v[0], v[1])][k] for v in PTS}
            head = "tau = %.2f%+.2fi, down, %-2s" % (t0.real, t0.imag, rd)
            out = []
            for kn, K in LK.items():
                G0, G1 = wgram(O_of(A0, K)), wgram(O_of(A1, K))
                for a in (1, 2):
                    T = R[a][1]
                    r = np.abs(G1 - T @ G0 @ T.conj().T).max() / np.abs(G0).max()
                    worst[(kn, a)] = max(worst.get((kn, a), 0), r)
                    out.append("K = %s, class %d: %.1e" % (kn, a, r))
            say("%s: L1 %s" % (head, "; ".join(out)))
            plain = sum(A0[v] @ A0[v].conj().T for v in PTS)
            sv = {}
            for name, K in KS.items():
                O = O_of(A0, K)
                par = np.abs(gram(O, E3) + gram(O, E2) - 5 * plain).max() / np.abs(plain).max()
                s = np.linalg.svd(O, compute_uv=False)
                sv[name] = s / s[0]
                say("%s: L3 %s: Parseval %.1e" % (head, name, par))
            n2, n1 = list(KS)
            say("%s: L4 O's singular values over the largest, class 2: %s" % (head, " ".join("%.4f" % x for x in sv[n2])))
            say("%s: L4 O's singular values over the largest, class 1: %s" % (head, " ".join("%.4f" % x for x in sv[n1])))
            say("%s: L4 their largest difference: %.3e" % (head, np.abs(sv[n1] - sv[n2]).max()))
    say("L1 worst over both points and readings: %s" % ", ".join("K = %s, class %d: %.1e" % (k[0], k[1], v) for k, v in worst.items()))
    for kn in ("I", "diag(1, 3)"):
        say("L2 gamma, K = %s: class 1 residual %.1e, class 2 residual %.1e" % (
            kn, passes(R[1][2], AG, LK[kn]), passes(R[2][2], AG, LK[kn])))
    cnt_g = {"1 only": 0, "2 only": 0, "both": 0, "neither": 0}
    cnt_ts = dict(cnt_g)
    for e in itertools.product(range(5), repeat=4):
        K = np.array(e).reshape(2, 2)
        if (K[0, 0] * K[1, 1] - K[0, 1] * K[1, 0]) % 5 == 0:
            continue
        pg = [passes(R[a][2], AG, K) < 1e-9 for a in (1, 2)]
        pts = [passes(R[a][1], AT, K) < 1e-9 and passes(R[a][0], AS, K) < 1e-9 for a in (1, 2)]
        for c, p in ((cnt_g, pg), (cnt_ts, pts)):
            c["both" if all(p) else "1 only" if p[0] else "2 only" if p[1] else "neither"] += 1
    say("L2 labellings passing gamma: %s; passing T and S: %s" % (cnt_g, cnt_ts))


if __name__ == "__main__":
    main()
