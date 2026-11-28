#!/usr/bin/env python3
"""The decisive script of this seat's refiled claim card for P-596 and P-568's first half (written 2026-11-28 for the
queue's form; data-free: no measured value is used, and no inter-sector value is printed).

    python3 relays/chat1_2026-11-25_p596/card_p596.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-25_p596/card_p596.py --control    # the failing control: must exit 1

It imports fd_rank.py from this folder (the sealed script of the old card, SHA-256 7ee9b7152570c2cb, at b53dce702,
unchanged) and runs its main() as it stands, capturing what it prints. Nothing of fd_rank.py is changed or copied,
except the control's loop below, which is fd_rank_control.py's (fbdf7cc3d) with Re tau frozen, written out here
because that script loads fd_rank.py by importlib, which the queue's rerun refuses.

THE CLAIM. On each of the 16 (line, tau) samples of fd_rank.py (8 lines of FR-FIB, tau = 0.13 + 2.2i and 0.31 + 3.1i),
every branch's ten outputs (logs of the six within-sector ratios and of |V_us|, |V_cb|, |V_ub|; J itself) have two
gradients in (Re tau, Im tau) that are not parallel: the largest |sin| between two kept gradients is above 1e-3 on every
branch. So f(d) = 2, and the ten obey 8 relations per branch.

CONDITION, written before this script's first run (its expectation is the sealed output fd_rank_out.txt, SHA-256
bd4ce5f9bb081b8f, at fbdf7cc3d):
  D1 the 16 per-sample lines print, in order, the branch counts (208 each), minima and counts below 0.1 of that
     output: minima 0.515, 0.480, 0.483, 0.129, 0.129, 0.300, 0.921, 0.402, 0.748, 0.247, 0.043, 0.099, 0.083,
     0.065, 0.110, 0.116; below 0.1: 0 on all but (1/12, 0) (8 and 2) and (5/12, 1/4) (8 and 8);
  D2 the total: 3328 rows, 1284 with an output below 1e-6 dropped, minimum 0.043, 26 below 0.1, 0 below 1e-3;
  D3 the verdict: rank two on every row (minimum above 1e-3), so the script exits 0. (The 3328 rows are 16 samples of
     208; the old card's 1 536 distinct branches rest on its reading that two of the evaluator's rows per line repeat a
     branch, which this script does not check, so it is not claimed here.)
  The control: the same verdict on the same measure with Re tau frozen at the base point, on fd_rank_control.py's two
  lines at tau = 0.13 + 2.2i, sees rank one on all 416 branches (largest |sin| below 1e-6), so the claim's verdict fails
  there and the control exits 1, with no traceback. Any other pattern is reported as found, and the card is not filed.

Nineteen lines are marked "DECISIVE:": the 16 samples, the total, the relation count and the verdict.
"""
import contextlib
import io
import re
import sys
from fractions import Fraction as Fr

import numpy as np

import fd_rank as FD

SAMPLE = re.compile(r"line \((\S+), (\S+)\), tau (\S+): +(\d+) branches; max \|sin\| between two kept gradients: "
                    r"median \S+, minimum (\S+), below 0\.1: (\d+)$")
TOTAL = re.compile(r"all: (\d+) branches \((\d+) with an output below 1e-6 dropped\); minimum (\S+); below 0\.1: (\d+); "
                   r"below 1e-3: (\d+)$")
FLOOR = 1e-3


def rank_two_everywhere(minimum, n_below_floor, n_branches):
    """the claim's verdict: there are branches, and on every one two kept gradients are not parallel"""
    return n_branches > 0 and minimum > FLOOR and n_below_floor == 0


def decisive():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        FD.main()
    text = buf.getvalue()
    samples = [m.groups() for m in map(SAMPLE.search, text.splitlines()) if m]
    total = [m.groups() for m in map(TOTAL.search, text.splitlines()) if m]
    if len(samples) != 16 or len(total) != 1:
        print("fd_rank.py's output did not parse: %d samples, %d totals" % (len(samples), len(total)))
        return 2
    for p1, p2, tau, n, mn, b01 in samples:
        print("DECISIVE: line (%s, %s), tau %s: %s branches; least largest |sin| %s; below 0.1: %s" % (p1, p2, tau, n, mn,
                                                                                                    b01))
    n, dropped, mn, b01, b3 = total[0]
    print("DECISIVE: all: %s rows, %s with an output below 1e-6 dropped; least largest |sin| %s; below 0.1: %s; "
          "below 1e-3: %s" % (n, dropped, mn, b01, b3))
    ok = rank_two_everywhere(float(mn), int(b3), int(n))
    print("DECISIVE: f(d) = 2 on every row, so the ten outputs obey 10 - 2 = 8 relations per branch: %s" % ok)
    print("DECISIVE: verdict: %s" % ("the claim holds" if ok else "the claim FAILS"))
    return 0 if ok else 2


def frozen(tau, line, x0):
    with contextlib.redirect_stdout(io.StringIO()):
        return FD.outs(complex(x0, tau.imag), line)


def control():
    """fd_rank_control.py's loop, with the claim's verdict applied to what it measures"""
    h = 1e-5
    per_branch = []
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
            per_branch.append(s)
    s = np.array(per_branch)
    ok = rank_two_everywhere(s.min() if len(s) else 0.0, int(np.sum(s < FLOOR)), len(s))
    print("control: %d branches with Re tau frozen; largest |sin| between two kept gradients at most %.2e; %d below "
          "1e-3; the claim's verdict on them: %s" % (len(s), s.max() if len(s) else 0.0, int(np.sum(s < FLOOR)),
                                                     "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(control() if sys.argv[1:] == ["--control"] else decisive())
