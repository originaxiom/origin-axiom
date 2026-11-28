#!/usr/bin/env python3
"""The decisive script of this seat's refiled claim card for P-632 (written 2026-11-28 for the queue's form;
data-free).

    python3 relays/chat1_2026-11-25_p632/card_p632.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-25_p632/card_p632.py --control    # the failing control: must exit 1

It imports p632_modes.py from this folder (the sealed script of the old card, SHA-256 e5d9879e6a3dda93, at
8fadd3f3e, unchanged), runs its main() as it stands (which also rewrites p632_modes.json beside it), and reads what it
prints.

THE CLAIM, in p632_modes.py's terms: F_s is the Farey operator of B1813's s-family, (F_s f)(x) = (1 + x)^(-2s)
[f(x / (1 + x)) + f(1 / (1 + x))] on [0, 1], discretised by collocation at N Chebyshev nodes (N = 64, 128, 256);
lambda_1(s) its leading eigenvalue and h_s its eigenfunction, read on a grid of 2001 points.
  M0 at s = 0, lambda_1 = 2 and h_0 = 1 (both to 1e-12), and F_1 maps 1/x to itself (to 1e-14);
  M2 for s = 0.1, ..., 0.9, h_s is positive and strictly decreasing on [0, 1], and lambda_1 agrees between N = 128
     and 256 to 1e-8;
  M3 lambda_1 is strictly decreasing in s on 0, 0.1, ..., 0.9, 0.95, with lambda_1(0.95) < 1.1, and h_s's mass on
     [0, 0.05] strictly increasing on 0, ..., 0.9;
  M1 at s = 0.25 and 0.5, the ratio of B1813's word sums Z_18 / Z_17 is lambda_1 within 3 %;
  and at every s of the grid the next three eigenvalues at N = 128 have modulus below 1.
  So the fastest-growing mode has no interior extremum for 0 <= s <= 0.95: it is constant at s = 0 and largest at
  x = 0 (the parabolic point) for 0.1 <= s <= 0.9, and picks no interior locus. What is not claimed: the theorems the
  old card cites (complete monotonicity, the continuous spectrum), and the route through a dynamics for tau.

CONDITION, written before this script's first run (its expectation is the sealed output p632_modes_out.txt, SHA-256
670c188fbe92a356):
  D1 M0 within its tolerances; lambda_1 at the 11 values of s, to 6 decimals: 2.000000, 1.848487, 1.710186, 1.584087,
     1.469311, 1.365112, 1.270911, 1.186353, 1.111484, 1.047292, 1.020343; masses 0.0500, 0.0546, 0.0601, 0.0667,
     0.0749, 0.0855, 0.0998, 0.1204, 0.1539, 0.2215, 0.2968;
  D2 h positive at every s; strictly decreasing at every s but 0 (where h is constant); next moduli below 1;
  D3 M2, M3 and M1 hold (M1's differences 6.99e-05 and 6.28e-04); the verdict holds, so the script exits 0.
  The control: the same check of a fastest-growing mode (positive and strictly decreasing on the grid) applied, on
  purpose, to the second eigenfunction at s = 0.5 and N = 128, which changes sign. The check fails, and the control
  exits 1, with no traceback. Any other pattern is reported as found, and the card is not filed.

Fifteen lines are marked "DECISIVE:".
"""
import contextlib
import io
import re
import sys

import numpy as np

import p632_modes as P

M0 = re.compile(r"^M0: \|lambda_1\(0\) - 2\| (\S+), max \|h_0 - 1\| (\S+); F_1\(1/x\) = 1/x to (\S+)$")
S = re.compile(r"^s = (\S+): lambda_1 (\S+) \(N 64, 128, 256 spread (\S+)\), mass on \[0, 0\.05\] (\S+) \(spread \S+\); "
               r"h positive (\w+), strictly decreasing (\w+); next \|lambda\| at N = 128: (.*)$")
M2 = re.compile(r"^M2: h_s positive and strictly decreasing for s = 0\.1 \.\. 0\.9: (\w+); N = 128 vs 256 worst (\S+)$")
M3 = re.compile(r"^M3: lambda_1 strictly decreasing (\w+), lambda_1\(0\.95\) = (\S+); mass fraction strictly increasing "
                r"(\w+)$")
M1 = re.compile(r"^M1 s = (\S+): Z_18 / Z_17 = (\S+), lambda_1 = (\S+), relative difference (\S+)$")
SUMMARY = re.compile(r"^(M0 \w+, M2 \w+, M3 \w+, M1 \w+)$")
GRID = np.linspace(0.0, 1.0, 2001)


def mode_check(values):
    """a fastest-growing mode with no interior extremum: positive, and strictly decreasing on the grid"""
    return bool(np.all(values > 0)) and bool(np.all(np.diff(values) < 0))


def verdict(summary, rows):
    """the claim's verdict: the four cells hold; h positive everywhere, strictly decreasing for s > 0; next moduli < 1"""
    return (summary == "M0 holds, M2 holds, M3 holds, M1 holds"
            and all(pos and (dec or s == 0.0) and nxt < 1 for s, pos, dec, nxt in rows))


def decisive():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        P.main()
    lines = buf.getvalue().splitlines()
    got = [[m.groups() for m in map(p.match, lines) if m] for p in (M0, S, M2, M3, M1, SUMMARY)]
    if [len(g) for g in got] != [1, 11, 1, 1, 2, 1]:
        print("p632_modes.py's output did not parse: %s" % [len(g) for g in got])
        return 2
    m0, srows, m2, m3, m1, summary = got
    a, b, c = (float(v) for v in m0[0])
    print("DECISIVE: M0 |lambda_1(0) - 2| < 1e-12: %s; max |h_0 - 1| < 1e-12: %s; F_1(1/x) = 1/x to 1e-14: %s"
          % (a < 1e-12, b < 1e-12, c < 1e-14))
    rows = []
    for s, lam, spread, mass, pos, dec, nxt in srows:
        top = max(float(v) for v in nxt.split(", "))
        rows.append((float(s), pos == "True", dec == "True", top))
        print("DECISIVE: s = %s: lambda_1 %.6f, mass on [0, 0.05] %s; h positive %s, strictly decreasing %s; next "
              "three moduli below 1: %s" % (s, float(lam), mass, pos, dec, top < 1))
    print("DECISIVE: M2 h_s positive and strictly decreasing for s = 0.1 .. 0.9: %s; N = 128 against 256 within 1e-8: "
          "%s" % (m2[0][0], float(m2[0][1]) < 1e-8))
    print("DECISIVE: M3 lambda_1 strictly decreasing %s, lambda_1(0.95) = %s; mass strictly increasing %s" % m3[0])
    ok = verdict(summary[0][0], rows)
    print("DECISIVE: verdict: %s (%s; M1's relative differences %s)" % ("the claim holds" if ok else "the claim FAILS",
                                                                       summary[0][0], ", ".join(r[3] for r in m1)))
    return 0 if ok else 2


def control():
    """the mode check applied, on purpose, to the second eigenfunction at s = 0.5, N = 128"""
    ev, V, h, x, bw = P.spectrum(0.5, 128)
    second = P.interp_matrix(x, bw, GRID) @ np.real(V[:, 1])
    second = second if second[0] > 0 else -second              # an eigenvector's sign is free: take it positive at 0
    ok = mode_check(second)
    print("control: the second eigenfunction at s = 0.5 in place of the first: positive %s, strictly decreasing %s; "
          "the claim's check: %s" % (bool(np.all(second > 0)), bool(np.all(np.diff(second) < 0)),
                                     "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(control() if sys.argv[1:] == ["--control"] else decisive())
