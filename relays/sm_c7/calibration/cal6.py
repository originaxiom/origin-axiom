import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import math, cmath, sm_c7_lib as L
from fractions import Fraction as Fr
exec(open('cal5.py').read().split('geo = L.Geodesic')[0].split('from fractions import Fraction as Fr')[1])
for z in (complex(0.13, 1.1), complex(-0.31, 0.95)):
    for c in [(Fr(1,8),Fr(5,8)), (Fr(1,3),Fr(0)), (Fr(0),Fr(2,5))]:
        a = (-c[1], c[0]); hh = 1e-6
        dlog = (siegel_log(a, z + hh) - siegel_log(a, z - hh)) / (2*hh)
        print(c, "G_v(c)/dlog g_Jc =", L.G_v(c, z) / dlog)
