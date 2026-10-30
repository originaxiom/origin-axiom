import math
import numpy as np
from fractions import Fraction as Fr
from frame_lib import *
def Q01(M): return 4*abs(M[0,0])**2 + 2*abs(M[0,1])**2 + 2*abs(M[1,0])**2 + abs(M[1,1])**2
# E1: |r01/r00| and x from c's and L, at the base a-configuration (1/8, 1/4), b = 0
for im in (8.0, 10.0, 12.0):
    t = complex(1/3, im)
    P = sector_M(t, Fr(1,8), 0.0, "down")
    x, y = P["x"], P["y"]
    # blocks at u = 0 via the channel map inversion
    R = P["R"]; r01 = (R["1"] + 1j*R["i"])/2; r10 = (-R["1"] + 1j*R["i"])/2; r00 = (-R["j"] - 1j*R["k"])/2; r11 = (-R["j"] + 1j*R["k"])/2
    c = P["c"]; L = P["L"]; w = {s: math.sqrt(2*math.pi*L + c[s]) for s in c}
    xpred = ((w["1"] + w["i"])/(w["j"] + w["k"]))**2 * abs(r01/r00)**2
    xcl = (2*math.pi*L + c["1"])/(2*math.pi*L + (c["j"] + c["k"])/2)
    M = P["M"]
    print("Im %.0f: L=%.6f |r01/r00|=%.9f  x(M)=%.9f  x(weights)=%.9f  x(closed, c1, cbar)=%.9f  c1-ci=%.2e cj-ck=%.4f" % (
        im, L, abs(r01/r00), abs(M[0,1])**2/abs(M[0,0])**2, xpred, xcl, c["1"]-c["i"], c["j"]-c["k"]))
# E2: |det M0(bx, by)| depends on bx + by only?
t = complex(1/3, 10.0)
def M0(bx, by):
    a = (1/8, bx), (1/4, by)
    return sector_M(t, Fr(1,8), 0.0, "down", twists=((1/8, bx), (1/4, by)))
for (bx, by) in ((0.274, 0.548), (0.411, 0.411), (0.822, 0.0), (-0.822, 1.644), (0.274+0.3, 0.548-0.3), (0.0, 0.0), (0.3, -0.3)):
    P = M0(bx, by); M = P["M"]
    print("bx=%.3f by=%.3f bx+by=%.3f |detM|=%.6e |m00|=%.6f |m01|=%.6f cj-ck=%.5f" % (bx, by, bx+by, abs(np.linalg.det(M)), abs(M[0,0]), abs(M[0,1]), P["c"]["j"]-P["c"]["k"]))
