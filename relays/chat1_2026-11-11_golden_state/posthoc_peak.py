#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
POST HOC, after amendment 1's output was read.  The web seat (chat1), 2026-11-11.  In its own file, committed
before it is run.  It imports the sealed script unchanged and seals no expectation; every line of its output is
labelled post hoc.  Two cells of the card failed, and these questions ask why.

  Q1  G6: the seat's peak and the point the lane reports differ by 1.5e-9.  Which of the two is a critical point
      of the density?  The gradient of f^2 at each, at 60 digits with a fourth-order difference; the value of the
      density at the lane's point relative to the peak; and a Newton iteration in two dimensions started from the
      lane's point.
  Q2  The peak along the arc found a second way: the root of the derivative along the circle at 60 digits.
  Q3  G5 failed on its count clause.  The grid point nearest the peak lies just inside the circle, so the clause
      as sealed excluded it.  The count of local maxima on the whole grid of the rectangle, above one twentieth of
      the peak.
  Q4  The Hessian of f^2 at the peak, relative to the peak, in Cartesian coordinates and in polar coordinates
      (radius, angle) about the origin.
"""
import os
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import golden_state_peak as g  # noqa: E402


def main():
    mp.mp.dps = 60
    g.C = g.euler_coefficients(g.NCOEF)

    def dens(z):
        return g.f(z) ** 2

    def grad(z, h):
        # fourth-order central differences
        gx = (-dens(z + 2 * h) + 8 * dens(z + h) - 8 * dens(z - h) + dens(z - 2 * h)) / (12 * h)
        gy = (-dens(z + 2j * h) + 8 * dens(z + 1j * h) - 8 * dens(z - 1j * h) + dens(z - 2j * h)) / (12 * h)
        return gx, gy

    def hess(z, h):
        d0 = dens(z)
        fxx = (dens(z + h) - 2 * d0 + dens(z - h)) / h ** 2
        fyy = (dens(z + 1j * h) - 2 * d0 + dens(z - 1j * h)) / h ** 2
        fxy = (dens(z + h + 1j * h) - dens(z + h - 1j * h) - dens(z - h + 1j * h) + dens(z - h - 1j * h)) / (4 * h ** 2)
        return fxx, fyy, fxy

    print('POST HOC to the golden state card (60 digits)')
    # Q2 first: the arc's maximum by a root of the derivative
    def along(th):
        return g.f(g.on_circle(th)) ** 2
    th0 = mp.mpf('0.9734382368308418226')
    th = mp.findroot(lambda t: mp.diff(along, t, h=mp.mpf(10) ** -15), th0, tol=mp.mpf(10) ** -40)
    z_seat = g.on_circle(th)
    peak = dens(z_seat)
    print('Q2  root of the derivative along the circle: theta = %s' % mp.nstr(th, 30))
    print('    z = %s + %s i' % (mp.nstr(mp.re(z_seat), 30), mp.nstr(mp.im(z_seat), 30)))
    print('    difference from the amended run\'s theta: %s' % mp.nstr(abs(th - th0), 3))
    # Q1
    h = mp.mpf(10) ** -8
    for name, z in (('the seat\'s point', z_seat), ('the lane\'s point', g.LANE)):
        gx, gy = grad(z, h)
        print('Q1  %s: gradient of f^2 relative to the peak = (%s, %s);  density / peak - 1 = %s'
              % (name, mp.nstr(gx / peak, 5), mp.nstr(gy / peak, 5), mp.nstr(dens(z) / peak - 1, 5)))
    z = g.LANE
    for it in range(6):
        gx, gy = grad(z, h)
        fxx, fyy, fxy = hess(z, h)
        det = fxx * fyy - fxy ** 2
        dx = -(fyy * gx - fxy * gy) / det
        dy = -(-fxy * gx + fxx * gy) / det
        z = z + dx + 1j * dy
        print('    Newton from the lane\'s point, step %d: moved %s; now %s from the seat\'s point' % (it + 1, mp.nstr(abs(dx + 1j * dy), 3), mp.nstr(abs(z - z_seat), 3)))
    print('    after Newton: z = %s + %s i;  |z|^2 - 1/5 = %s' % (mp.nstr(mp.re(z), 25), mp.nstr(mp.im(z), 25), mp.nstr(abs(z) ** 2 - mp.mpf(1) / 5, 3)))
    print('    the lane\'s point: |z|^2 - 1/5 = %s;  distance from the seat\'s point %s' % (mp.nstr(abs(g.LANE) ** 2 - mp.mpf(1) / 5, 3), mp.nstr(abs(g.LANE - z_seat), 5)))
    # Q4
    fxx, fyy, fxy = hess(z_seat, h)
    tr = fxx + fyy
    dt = fxx * fyy - fxy ** 2
    e1 = (tr + mp.sqrt(tr ** 2 - 4 * dt)) / 2
    e2 = (tr - mp.sqrt(tr ** 2 - 4 * dt)) / 2
    print('Q4  Hessian of f^2 at the peak, relative to the peak, Cartesian eigenvalues: %s, %s' % (mp.nstr(e1 / peak, 10), mp.nstr(e2 / peak, 10)))
    r = abs(z_seat)
    hr = mp.mpf(10) ** -8
    th_s = mp.arg(z_seat)

    def pol(rr, tt):
        return dens(rr * (mp.cos(tt) + 1j * mp.sin(tt)))
    p0 = pol(r, th_s)
    prr = (pol(r + hr, th_s) - 2 * p0 + pol(r - hr, th_s)) / hr ** 2
    ptt = (pol(r, th_s + hr) - 2 * p0 + pol(r, th_s - hr)) / hr ** 2
    prt = (pol(r + hr, th_s + hr) - pol(r + hr, th_s - hr) - pol(r - hr, th_s + hr) + pol(r - hr, th_s - hr)) / (4 * hr ** 2)
    print('    in polar coordinates (radius, angle): d2/dr2 = %s, d2/dtheta2 = %s, mixed = %s (each relative to the peak)'
          % (mp.nstr(prr / peak, 10), mp.nstr(ptt / peak, 10), mp.nstr(prt / peak, 5)))
    # Q3
    with mp.workdps(20):
        ys = [mp.mpf('0.16') + mp.mpf('0.01') * i for i in range(45)] + [mp.mpf('0.65') + mp.mpf('0.05') * i for i in range(28)]
        xs = [mp.mpf('0.01') * i for i in range(1, 50)]
        grid = {}
        for iy, y in enumerate(ys):
            n_max = g.nterms(y)
            ks = [(n, g.C[n] * mp.re(mp.besselk(1j * g.R, 2 * mp.pi * n * y))) for n in range(1, n_max + 1) if g.C[n] != 0]
            for ix, x in enumerate(xs):
                s = mp.mpf(0)
                for n, kv in ks:
                    s += kv * mp.sin(2 * mp.pi * n * x)
                grid[(ix, iy)] = y * s * s
        locs = []
        for (ix, iy), v in grid.items():
            if v < peak / 20:
                continue
            nb = [grid.get((ix + a, iy + b)) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
            if all(w is None or w < v for w in nb):
                locs.append((mp.nstr(xs[ix], 4), mp.nstr(ys[iy], 4), mp.nstr(v / peak, 8)))
    print('Q3  local maxima on the whole grid above one twentieth of the peak (x, y, value/peak): %s' % locs)
    return 0


if __name__ == '__main__':
    sys.exit(main())
