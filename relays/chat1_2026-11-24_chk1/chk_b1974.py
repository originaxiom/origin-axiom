#!/usr/bin/env python3
"""Checks of B1974's two numerical inputs (data-free): c_0 = -theta_2^2 (theta_3^4 + theta_4^4) / (24 eta^3) against the
frame's triplet component, and the zeros of theta_3^4 + theta_4^4 in a box of the strip by the argument principle.
    python3 -I chk_b1974.py <a checkout of main>"""
import glob
import sys
MAIN = sys.argv[1]
sys.path.insert(0, glob.glob(MAIN + "/frontier/B1940_*/verification")[0])
sys.argv = ["x"]
import frame_mp as FM  # noqa: E402
import mpmath as mp  # noqa: E402
mp.mp.dps = 40
te = FM.te


def eta(t):
    return mp.exp(1j * mp.pi * t / 12) * mp.qp(mp.exp(2j * mp.pi * t))


def th(k, t):
    return mp.jtheta(k, 0, mp.exp(1j * mp.pi * t))


for t in (mp.mpc("0.13", "1.5"), mp.mpc("-0.31", "0.8"), mp.mpc("0.4", "2.2")):
    c = [te.ev(cc, t) for cc in te.B[1]]
    f = -th(2, t) ** 2 * (th(3, t) ** 4 + th(4, t) ** 4) / (24 * eta(t) ** 3)
    print("tau", mp.nstr(t, 3), " c0 / formula =", mp.nstr(c[0] / f, 15))
z = mp.mpc("0.5", "0.5")
print("theta3^4 + theta4^4 at (1+i)/2:", mp.nstr(th(3, z) ** 4 + th(4, z) ** 4, 5))


def g(t):
    return th(3, t) ** 4 + th(4, t) ** 4


def winding(f, pts, n=400):
    w = 0
    for i in range(len(pts)):
        a, b = pts[i], pts[(i + 1) % len(pts)]
        prev = f(a)
        for k in range(1, n + 1):
            cur = f(a + (b - a) * k / n)
            w += mp.im(mp.log(cur / prev))
            prev = cur
    return w / (2 * mp.pi)


box = [mp.mpc(-0.49, 0.35), mp.mpc(0.51, 0.35), mp.mpc(0.51, 3), mp.mpc(-0.49, 3)]
print("zeros of theta3^4 + theta4^4 in Re [-0.49, 0.51] x Im [0.35, 3]:", mp.nstr(winding(g, box), 6))
