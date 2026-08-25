#!/usr/bin/env python3
"""Stage 1 of the ONE-BIT cell: extract the closing's mirror T = theta_matrix(g,c)
(the memo-10/B1134 hit used in spacetime64/memo 33) as an exact rational 78x78
matrix, together with the ccb basis fingerprint (the ROOTS list), for the
stage-2 inner-vs-outer decision in the twisted_double stack."""
import importlib.util, itertools, random
from fractions import Fraction as F
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
exec(open(SCR+'/simul_verify.py').read().split("# principal triple of S0")[0])

hit=None
for gi,g in enumerate(G_swap):
    for c in solve_lift(g):
        if color_sig(g,c)==(0,8): hit=(g,c); break
    if hit: break
g,c=hit
T=theta_matrix(g,c)
# T as columns on the standard basis
cols=[]
for j in range(DIM):
    bas=[F(0)]*DIM; bas[j]=F(1)
    cols.append(apply(T,bas))
Tmat=[[cols[j][i] for j in range(DIM)] for i in range(DIM)]
with open(SCR+'/theta_dump.py','w') as f:
    f.write("from fractions import Fraction as F\n")
    f.write("ROOTS_FP=%r\n"%(list(ROOTS),))
    f.write("N_FP=%d\nDIM_FP=%d\n"%(N,DIM))
    f.write("TMAT=[\n")
    for row in Tmat:
        f.write(" [%s],\n"%(",".join("F(%d,%d)"%(x.numerator,x.denominator) for x in row)))
    f.write("]\n")
print("theta dumped: swapper #%d, %dx%d rational matrix, ROOTS fingerprint %d entries"%(gi,DIM,DIM,len(ROOTS)))
