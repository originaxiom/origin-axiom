#!/usr/bin/env python3
"""Section 1 of QUESTION_R29: twisted cohomology is not a character invariant."""
import sympy as sp, itertools
I2=sp.eye(2)
a=sp.Matrix([[1,1],[0,1]]); b=sp.Matrix([[1,2],[0,1]]); ass=bss=I2
def word(A,B,w):
    M=I2
    for c in w: M=M*(A if c=='a' else A.inv() if c=='A' else B if c=='b' else B.inv())
    return M
W=[''.join(t) for n in (1,2,3,4) for t in itertools.product('abAB',repeat=n)]
same=all(sp.simplify(word(a,b,w).trace()-word(ass,bss,w).trace())==0 for w in W)
h0  =2-sp.Matrix.vstack(a-I2,b-I2).rank()
h0ss=2-sp.Matrix.vstack(ass-I2,bss-I2).rank()
print(f"  traces agree on all {len(W)} words of length <=4 : {same}")
print(f"  dim H^0(F_2;V) = {h0}   dim H^0(F_2;V^ss) = {h0ss}   differ: {h0!=h0ss}")
raise SystemExit(0 if (same and h0!=h0ss) else 1)
