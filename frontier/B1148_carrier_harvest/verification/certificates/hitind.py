#!/usr/bin/env python3
"""Memo-44 follow-up: hit-independence of the mirror's inner class.
For EVERY (0,8) hit (the 24 of memo 10/B1134), compute tr(theta_matrix) on the
78.  Involution classes: inner give trace -2 or 14; outer give 26 or -6.
PREREGISTERED: all 24 give -2 (the class is a property of the closing, not the
hit)."""
import importlib.util, itertools, random
from fractions import Fraction as F
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
exec(open(SCR+'/simul_verify.py').read().split("# principal triple of S0")[0])
traces={}
nhits=0
for gi,g in enumerate(G_swap):
    for c in solve_lift(g):
        if color_sig(g,c)==(0,8):
            T=theta_matrix(g,c)
            tt=0
            for j in range(DIM):
                bas=[F(0)]*DIM; bas[j]=F(1)
                tt+=apply(T,bas)[j]
            traces[tt]=traces.get(tt,0)+1
            nhits+=1
print(f"hits examined: {nhits};  tr(theta) multiset: {dict(traces)}")
assert nhits>=24 and set(traces)=={F(-2)}
print("ALL hits give tr(theta) = -2: the mirror's INNER (sl2+sl6) class is hit-independent")
