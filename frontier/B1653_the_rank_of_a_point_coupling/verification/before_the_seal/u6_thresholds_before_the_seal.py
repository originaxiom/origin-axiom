"""Main's pre-seal computation for B1653 v3's U6 thresholds (DISCLOSED in the seal): the exploration's series code
(not the instrument), three random twist pairs, B1644's coupling, mpmath SVD. Profiles on a polar grid with 64 angles:
(a) radially symmetric about the regular point c0 (must act as the point: rank one); (b) tilted about c0
(w = g(r) (1 + Re(z - c0)/0.05)); (c) elliptical about c0 (a = 0.1, b = 0.03); (d) radially symmetric about the puncture
(an annulus 0.02-0.1). Reported: |det M|/max^2 and the coupling's min sigma ratio over 20 draws."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import mpmath as mp
from check_rank_one import Bt, Y, svals, rt, ONE
mp.mp.dps = 40
I = mp.mpc(0, 1)
random.seed(165303)
t = mp.mpc(0.13, 1.07); c0 = mp.mpc(0.3, 0.2)
NT = 64; RADII = [mp.mpf(x) for x in ("0.01", "0.025", "0.04", "0.055", "0.07", "0.085", "0.1")]
def grid(center, radii):
    for r in radii:
        for k in range(NT):
            yield center + r * mp.exp(2 * I * mp.pi * k / NT), r
def g(r): return mp.exp(-r ** 2 / mp.mpf("0.0025"))
profiles = {
 "a_radial_regular": (c0, RADII, lambda z, r: g(r)),
 "b_tilted_regular": (c0, RADII, lambda z, r: g(r) * (1 + mp.re(z - c0) / mp.mpf("0.05"))),
 "c_elliptic_regular": (c0, RADII, lambda z, r: mp.exp(-(mp.re(z - c0) / mp.mpf("0.1")) ** 2 - (mp.im(z - c0) / mp.mpf("0.03")) ** 2)),
 "d_radial_puncture": (mp.mpc(0, 0), [mp.mpf(x) for x in ("0.02", "0.035", "0.05", "0.065", "0.08", "0.1")], lambda z, r: g(r)),
}
def rnd_S():
    return mp.matrix([[mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(2)] for _ in range(2)])
SS = [rnd_S() for _ in range(20)]
for name, (cen, radii, w) in profiles.items():
    dets, rats = [], []
    for _ in range(3):
        x, y = rt(), rt()
        M = mp.matrix(2, 2)
        for z, r in grid(cen, radii):
            M += w(z, r) * r * Bt(x, y, z, t)
        mxv = max(abs(M[m, n]) for m in range(2) for n in range(2))
        dets.append(abs(M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]) / mxv ** 2)
        rats.append(min(svals(Y(S, M))[2] / svals(Y(S, M))[0] for S in SS))
    print(name, " det/max^2 min", mp.nstr(min(dets), 3), "max", mp.nstr(max(dets), 3), "  min sigma ratio", mp.nstr(min(rats), 3))
