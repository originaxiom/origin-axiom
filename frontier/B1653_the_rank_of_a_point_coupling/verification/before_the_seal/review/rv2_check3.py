"""Reviewer, v2 review, check 3: continuum-robustness by a dense polar quadrature (area element r dr dtheta)."""
import sys
sys.path.insert(0, ".")
exec(open("rv2_check1.py").read().split("# U0(b): the control")[0])
x, y = PAIRS[0]; t = TAUS[0]; c0 = mp.mpc(0.3, 0.2)
mp.mp.dps = 30
def polar_M(centre, wfun, nr, nth, rmax=mp.mpf("0.15")):
    M = mp.matrix(2, 2); dr = rmax / nr
    for i in range(nr):
        r = (i + mp.mpf(1) / 2) * dr
        for k in range(nth):
            z = centre + r * mp.exp(2 * J * mp.pi * (k + mp.mpf(1) / 3) / nth)
            M += wfun(z) * r * dr * (2 * mp.pi / nth) * bilf(x, y, z, t)
    return M
def rep(name, M): print(f"  {name:58s} |det M|/max^2 = {mp.nstr(abs(det2(M))/mx(M)**2, 4)}")
for (nr, nth) in [(6, 16), (8, 24)]:
    print(f"-- polar grid {nr} radii x {nth} angles, rmax 0.15 --")
    rep("radial about c0", polar_M(c0, lambda z: mp.exp(-abs(z - c0) ** 2 / mp.mpf("0.0025")), nr, nth))
    rep("elliptical about c0 (dx^2/0.0025 + dy^2/0.01)", polar_M(c0, lambda z: mp.exp(-(mp.re(z - c0) ** 2 / mp.mpf("0.0025") + mp.im(z - c0) ** 2 / mp.mpf("0.01"))), nr, nth))
    rep("tilted radial about c0, (1 + 0.5 Re((z-c0)/0.1))", polar_M(c0, lambda z: mp.exp(-abs(z - c0) ** 2 / mp.mpf("0.0025")) * (1 + mp.re((z - c0) / mp.mpf("0.1")) / 2), nr, nth))
    rep("radial about the puncture", polar_M(mp.mpc(0, 0), lambda z: mp.exp(-abs(z) ** 2 / mp.mpf("0.0025")), nr, nth))
