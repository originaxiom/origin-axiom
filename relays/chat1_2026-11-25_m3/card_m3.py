#!/usr/bin/env python3
"""The decisive script of this seat's refiled claim card for P-879: agy-002's two-sector floor M3 holds under the
one-doublet rule it states and fails when one Higgs is read alike in both sectors (written 2026-11-28 for the queue's
form; data-free).

    python3 relays/chat1_2026-11-25_m3/card_m3.py              # decisive: exit 0 when the claim holds
    python3 relays/chat1_2026-11-25_m3/card_m3.py --control    # the failing control: must exit 1

It imports m3_scope.py from this folder (the sealed script of the old card, SHA-256 e8f8a1176532215f, at 1d84abee8,
unchanged). That script computes on import: its 120 000 trials in both readings, with seed 20261125. What it prints
is captured and not shown; its counts are read from the module, and the decisive lines restate them.

THE CLAIM. With M3's floor F (m3_scope.py's docstring states it) and rho the larger second-to-first singular value
ratio of the two sectors' couplings: (i) under H_u = conj(h).sigma, H_d = h.sigma, rho >= F - 1e-9 on all 120 000
trials; (ii) under H_u = H_d = h.sigma, rho < F - 1e-9 on more than 10 of them.

CONDITION, written before this script's first run (its expectation is the sealed output m3_scope_out.txt, SHA-256
6523a5f54c7d7fad):
  D1 reading (i): 120 000 trials, 0 violations, least margin 4.247e-03;
  D2 reading (ii): 120 000 trials, 58 violations, least margin -5.207e-02 at (rho, F, t, |V33|) = (0.021562,
     0.073636, 0.03122, 0.999632);
  D3 the verdict: (i) holds and (ii) fails, so the script exits 0.
  The control: the same verdict on reading (i) with the floor made wrong on purpose, F replaced by 4 F, on 6 000
  trials of the same six modes (seed 20261128). An over-strong floor must be violated, so "(i) holds" fails and the
  control exits 1, with no traceback. Any other pattern is reported as found, and the card is not filed.

Five lines are marked "DECISIVE:".
"""
import contextlib
import io
import sys

import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    import m3_scope as M3

MARGIN = 1e-9


def verdict(viol_i, viol_ii):
    """the claim's verdict: no violation in reading (i), more than 10 in reading (ii)"""
    return viol_i == 0 and viol_ii > 10


def decisive():
    rows = []
    for same, name in ((False, "(i) H_u = conj(h).sigma, H_d = h.sigma"), (True, "(ii) H_u = H_d = h.sigma")):
        v, m, rec = M3.res[same]
        rows.append(v)
        print("DECISIVE: %s: trials %d, violations %d, least margin rho - F %.3e" % (name, M3.N, v, m))
        if same:
            print("DECISIVE: (ii) its least margin at (rho, F, t, |V33|) = (%.6f, %.6f, %.5f, %.6f)"
                  % tuple(float(x) for x in rec))
    ok = verdict(*rows)
    print("DECISIVE: M3 holds in reading (i): %s; M3 fails in reading (ii): %s" % (rows[0] == 0, rows[1] > 10))
    print("DECISIVE: verdict: %s" % ("the claim holds" if ok else "the claim FAILS"))
    return 0 if ok else 2


def control():
    M3.rng = np.random.default_rng(20261128)       # m3_scope.sample() draws from the module's rng
    n, v = 6000, 0
    for k in range(n):
        h, Mu, Md = M3.sample(k % 6)
        rho, F, _, _ = M3.evaluate(h, Mu, Md, False)
        if rho < 4 * F - MARGIN:
            v += 1
    ok = verdict(v, M3.res[True][0])
    print("control: reading (i) with the floor made 4 F on purpose: %d trials, %d violations; the claim's verdict: %s"
          % (n, v, "holds (the control has FAILED to fail)" if ok else "fails, as it must"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(control() if sys.argv[1:] == ["--control"] else decisive())
