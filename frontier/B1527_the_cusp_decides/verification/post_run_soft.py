#!/usr/bin/env python3
"""B1527 post-run check (written after X2 was read; disclosed in FINDINGS §4.5): the type-one Jacobian's soft singular value.

FINDINGS says the frame's soft singular value of the type-one system (the smallest kept one, relative to the largest)
scales with a: the equations see the frame only through b, which moves at order a (X1's weight-3 law). This reads it at
a = 1e-5, 4e-5 and 1.6e-4 on +LR (frame 60) and +LLLRLRR (frame 68.2555), each point rebuilt as X2 rebuilds X1's points
(the pinned solve, then the b = 0 system in float64) and polished at 50 digits with X1's polish_gn. The ratios to a = 1e-5
should be 4 and 16. Writes nothing; prints one line per reading.
Usage: python3 post_run_soft.py"""
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

import family_lib as FL  # noqa: E402
import post_run_x1 as X1  # noqa: E402
import run as R  # noqa: E402
import scan_lib as S  # noqa: E402

CASES = (("+", "LR", 60.0), ("+", "LLLRLRR", 68.2555))
SCALES = (1e-5, 4e-5, 1.6e-4)


def soft(sign, word, frame_deg, a):
    X1.A = a          # X1's pinned residual reads its module's A
    R.A_SCAN = a
    P = X1.Pinned(sign, word)
    rec = P.solve(np.radians(frame_deg))
    u1, f1, _ = X1.gauss_newton(lambda v: S.residual(v, a, rec["W"], False).real,
                                lambda v: S.jacobian(v, a, rec["W"], False), rec["u"][:52], 0.3 * rec["threshold"])
    mp.mp.dps = 50
    G, img = FL.word_group(sign, word)
    U = mp.matrix([mp.mpf(float(x)) for x in u1])
    Up, fp, _, _ = X1.polish_gn(U, mp.mpf(a), G, img, tol=mp.mpf(10) ** -40, maxit=40)
    sv = sorted([abs(x) for x in mp.svd_r(FL.jacobian(Up, mp.mpf(a), G, img), compute_uv=False)], reverse=True)
    rel = [x / sv[0] for x in sv]
    kept = sorted(x for x in rel if x >= mp.mpf(10) ** -30)
    return float(f1), fp, sum(1 for x in rel if x < mp.mpf(10) ** -30), kept[0], kept[1]


def main():
    print(f"start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}", flush=True)
    for sign, word, frame in CASES:
        base = None
        for a in SCALES:
            f1, fp, n, s1, s2 = soft(sign, word, frame, a)
            base = base or s1
            print(f"{sign}{word} a = {a:g}: float64 |F| {f1:.2e}, polished |F| {mp.nstr(fp, 3)}, nullity {n}, "
                  f"soft / top {mp.nstr(s1, 4)} (ratio to a = 1e-5: {mp.nstr(s1 / base, 6)}), next / top {mp.nstr(s2, 4)}",
                  flush=True)
    print(f"end {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}", flush=True)


if __name__ == "__main__":
    main()
