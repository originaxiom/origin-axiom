import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import math, sm_c7_lib as L, random
from fractions import Fraction as Fr
random.seed(3); worst = [0, 0, 0]
for _ in range(40):
    N = random.choice([5, 8, 12, 48]); c = (Fr(random.randrange(N), N), Fr(random.randrange(N), N))
    if c == (0, 0): continue
    z = complex(random.uniform(-.5, .5), random.uniform(.87, 1.6))
    worst[0] = max(worst[0], abs(L.E_fast(c, z, 2) - L.E_fourier(c, z, 2)))
    worst[1] = max(worst[1], abs(L.G_u_fast(c, z) - L.G_u(c, z)))
    worst[2] = max(worst[2], abs(L.G_v_fast(c, z) - L.G_v(c, z)))
print("fast vs calibrated (E s=2, G_u, G_v):", worst)
