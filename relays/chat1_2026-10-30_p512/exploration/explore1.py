import math, sys
import numpy as np
from fractions import Fraction as Fr
from frame_lib import *
t = complex(1/3, 10.0)
S, av = S_of(t)
St = EPS @ np.conj(S) @ EPS.T
print("av (QI, QJ, QK) coefficients:", [complex(v) for v in av])
print("S entries:", S[0,0], S[0,1], S[1,0], S[1,1])
f = math.exp(2 * math.pi * t.imag / 8)
for b in (0.0, 0.137, 0.311):
    for a in (Fr(1, 8), Fr(3, 8)):
        out = {}
        for sec in ("down", "lep"):
            P = sector_M(t, a, b, sec)
            for rn, SS in (("S", S), ("St", St)):
                r2, r1, sv = ratios(Ymat(SS, P["M"]))
                out[(sec, rn)] = r2
        print("b=%.3f a=%s  R2(S)=%.7f R2(St)=%.7f | down(S)*f=%.6f lep(S)*f=%.6f" % (b, a, out[("lep","S")]/out[("down","S")], out[("lep","St")]/out[("down","St")], out[("down","S")]*f, out[("lep","S")]*f))
