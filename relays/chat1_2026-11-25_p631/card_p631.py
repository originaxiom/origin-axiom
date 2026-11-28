#!/usr/bin/env python3
"""The decisive script of this seat's refiled claim card for P-631 (written 2026-11-28 for the queue's form;
data-free).

    python3 relays/chat1_2026-11-25_p631/card_p631.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-25_p631/card_p631.py --control    # the failing control: must exit 1

It imports p631_two_loop.py from this folder (the sealed script of the old card, SHA-256 aa5c850a33237e43, at
852afb281, unchanged), runs its main() as it stands, and reads what it prints.

THE CLAIM, in p631_two_loop.py's terms (E_s the real-analytic Eisenstein series of the fibre's modulus tau, normalised
as there; C111 the two-loop sunset sum; V_1 = -alpha E_3 the one-loop term, V_2 = beta E_2^2 the two-loop term of the
quartic figure-eight):
  K1 the Fourier and lattice evaluations of E_2 and E_3 agree (worst relative difference below 1e-6);
  K2 the lattice sunset C111, extrapolated in its cutoff, equals E_3 + zeta(3) within 2e-3 at tau = i, omega and
     0.2 + 1.7i (the cubic sunset repeats the one-loop shape);
  K3 E_2^2 is not a combination of 1, E_2, E_3, E_4, E_5: its least-squares residual on 40 points is above 1e-8
     (relative rms);
  K4 on the imaginary axis, for beta/alpha = 1e-2, 1e-3, 1e-4, V_1 + V_2 has one stationary point, where
     |V_2/V_1| is within 0.1 of 3/4;
  K5 over beta/alpha in +-[1e-4, 10] (60 values) and the lines Re tau = 0 and 1/2, no stationary point of V_1 + V_2
     with Im tau in [1.2, 20] has |V_2| <= |V_1| / 3, the bound of the principle sealed for Im tau (P-373).
  Its scope is that search: the claim is not made for other lines of the fundamental domain, nor outside [1.2, 20]
  except on the imaginary axis as K4 says.

CONDITION, written before this script's first run (its expectation is the sealed output p631_two_loop_out.txt,
SHA-256 0c9f970bcab17a05):
  D1 K1 worst relative difference 2.89e-10; K2 differences 5.63e-05, -1.48e-05, 6.19e-05; K3 residual 1.278e-04;
  D2 K4 stationary points at y = 102.7, 1030, 1.02e+04 with |V_2/V_1| = 0.7525, 0.7553, 0.7479;
  D3 K5: 12 stationary points found, none with |V_2| <= |V_1| / 3;
  D4 the verdict: K1 to K5 hold, so the script exits 0.
  The control: K5's check with its bound made wrong on purpose, |V_2| <= |V_1| (in place of |V_1| / 3), on K4's
  first case (Re tau = 0, beta/alpha = 1e-2, Im tau in [1.2, 300]). Its stationary point at y = 102.7 has
  |V_2/V_1| = 0.75, inside the wrong bound, so K5's verdict fails there and the control exits 1, with no traceback.
  Any other pattern is reported as found, and the card is not filed.

Eleven lines are marked "DECISIVE:".
"""
import contextlib
import io
import re
import sys

import numpy as np

import p631_two_loop as P

K1 = re.compile(r"^K1 worst relative difference (\S+)$")
K2 = re.compile(r"^K2 C111\((\S+)\): cutoffs .*, extrapolated (\S+); E_3 \+ zeta\(3\) = (\S+); difference (\S+)$")
K3 = re.compile(r"^K3 E_2\^2 fitted by \{1, E_2, E_3, E_4, E_5\} on 40 points: relative rms residual (\S+)$")
K4 = re.compile(r"^K4 beta/alpha = (\S+): stationary points at y = \[(.*)\]; \|V_2/V_1\| there \[(.*)\]$")
K5 = re.compile(r"^K5 stationary points with Im tau in \[1\.2, 20\] found: (\d+); any with \|V_2\| <= \|V_1\|/3: (\w+)$")
SUMMARY = re.compile(r"^(K1 \w+, K2 \w+, K3 \w+, K4 \w+, K5 \w+)$")


def verdict(summary, k5_inside):
    """the claim's verdict: every cell holds, and no stationary point lies inside the bound"""
    return summary == "K1 holds, K2 holds, K3 holds, K4 holds, K5 holds" and not k5_inside


def decisive():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        P.main()
    lines = buf.getvalue().splitlines()
    got = [[m.groups() for m in map(p.match, lines) if m] for p in (K1, K2, K3, K4, K5, SUMMARY)]
    if [len(g) for g in got] != [1, 3, 1, 3, 1, 1]:
        print("p631_two_loop.py's output did not parse: %s" % [len(g) for g in got])
        return 2
    k1, k2, k3, k4, k5, summary = got
    print("DECISIVE: K1 E_2 and E_3, Fourier against lattice: worst relative difference %s" % k1[0])
    for tau, ext, target, diff in k2:
        print("DECISIVE: K2 C111 at tau = %s: extrapolated %s; E_3 + zeta(3) = %s; difference %s" % (tau, ext, target,
                                                                                                    diff))
    print("DECISIVE: K3 E_2^2 against {1, E_2, E_3, E_4, E_5} on 40 points: relative rms residual %s" % k3[0])
    for r, ys, qs in k4:
        print("DECISIVE: K4 beta/alpha = %s: stationary points at y = %s; |V_2/V_1| there %s"
              % (r, ys.replace("'", ""), qs.replace("'", "")))
    print("DECISIVE: K5 stationary points with Im tau in [1.2, 20] found: %s; any with |V_2| <= |V_1|/3: %s" % k5[0])
    ok = verdict(summary[0][0], k5[0][1] == "True")
    print("DECISIVE: verdict: %s (%s)" % ("the claim holds" if ok else "the claim FAILS", summary[0][0]))
    return 0 if ok else 2


def control():
    """K5's check with the bound made |V_2| <= |V_1| on purpose, on K4's first case"""
    r, x = 1e-2, 0.0
    fun = lambda y: -P.eis(3, complex(x, y)) + r * P.eis(2, complex(x, y)) ** 2
    inside = []
    for y in P.stationary_points(fun, np.geomspace(1.2, 3.0 / r, 400)):
        q = abs(r * P.eis(2, complex(x, y)) ** 2 / P.eis(3, complex(x, y)))
        if q <= 1.0:
            inside.append((y, q))
    ok = verdict("K1 holds, K2 holds, K3 holds, K4 holds, K5 holds", bool(inside))
    print("control: the bound made |V_2| <= |V_1| on purpose; stationary points inside it: %s; the claim's verdict: %s"
          % (["y %.4g, |V_2/V_1| %.4f" % p for p in inside],
             "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(control() if sys.argv[1:] == ["--control"] else decisive())
