import math
import numpy as np
from fractions import Fraction as Fr
from frame_lib import *
t = complex(1/3, 10.0)
S, _ = S_of(t)
def Q01(M): return 4*abs(M[0,0])**2 + 2*abs(M[0,1])**2 + 2*abs(M[1,0])**2 + abs(M[1,1])**2
for b in (0.0, 0.137, 0.311):
    res = {}
    for a in (Fr(1,8), Fr(3,8)):
        for sec in ("down", "lep"):
            P = sector_M(t, a, b, sec); M = P["M"]
            r2, r1, sv = ratios(Ymat(S, M))
            pred = 2*abs(np.linalg.det(M))/Q01(M)
            res[(a,sec)] = (r2, pred)
            print("b=%.3f a=%s %-4s  m2/m3=%.9e  pred=%.9e  rel=%.1e | |m00| %.4e |m01| %.4e |m10| %.4e |m11| %.4e |detM| %.4e | c=%s" % (
                b, a, sec, r2, pred, pred/r2-1, abs(M[0,0]), abs(M[0,1]), abs(M[1,0]), abs(M[1,1]), abs(np.linalg.det(M)), {k: round(v,5) for k,v in P["c"].items()}))
    R18 = res[(Fr(1,8),"lep")][1]/res[(Fr(1,8),"down")][1]; R38 = res[(Fr(3,8),"lep")][1]/res[(Fr(3,8),"down")][1]
    print("   leading-order R2(1/8)=%.7f R2(3/8)=%.7f ratio=%.7f" % (R18, R38, R18/R38))
