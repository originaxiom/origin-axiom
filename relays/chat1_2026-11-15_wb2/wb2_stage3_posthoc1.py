#!/usr/bin/env python3
"""W-B2, stage 3, post hoc 1 (committed before its run; NOT blind: stage 3's output has been read).

Stage 3's U1 failed only on the test w -> w + tau ("Pt"), which compared s1 as well as r2 = s2/s1. Under w -> w + tau
the Higgs's pole moves by c q_H tau and the residues pick up the thetas' quasi-periodicity multiplier, a common factor
of the whole coupling, so s1 is not expected to be invariant (its ratio came out of order 1e183 at c = +-2). This run
repeats Pt on r2 alone.
  U1'  c = +2 and -2: Pt on r2 below 1e-8. Reported for c = +1 and -1.

    python3 -I -u wb2_stage3_posthoc1.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wb2_stage3 as W  # noqa: E402


def pt(c, rd):
    wv = 0.0
    for sec in ("up", "down", "lep"):
        for a, b in W.PTS:
            for t in W.K.TAUS:
                wv = max(wv, W.d2(W.sv_of(t, a, b, sec, c, rd), W.sv_of(t, a + 1, b, sec, c, rd), with_s1=False))
    return float(wv)


res = {(c, rd): pt(c, rd) for c in (2, -2, 1, -1) for rd in ("S", "St")}
for k, v in res.items():
    W.K.say("Pt on r2, c %+d %-2s: %.1e" % (k[0], k[1], v))
W.K.say("U1' holds:", all(res[(c, rd)] < 1e-8 for c in (2, -2) for rd in ("S", "St")))
