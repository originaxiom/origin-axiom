#!/usr/bin/env python3
"""W-C7: B1913 (the flat area is not on the curve) computed a second time, on this seat's own code.

Data-free. The state is this seat's own construction of 2026-11-11 (relays/chat1_2026-11-11_golden_state/
golden_state_peak.py, imported unchanged): Maass's form f of the golden field at level 5, character (d/5).
No value of tau on record is read or compared; no frame is evaluated anywhere.

ORDER, disclosed: this seat read B1913's FINDINGS (§ 1) through the mask before writing this file, to judge the card
against its firewall. So the expectations below are not blind to main's result; they are committed before this run.

    python3 -I -u wc7_checks.py

DEFINITIONS:
  g1 = (1, 0, 5, 1), g2 = (2, -1, 5, -2) in Gamma_0(5). g z = (a z + b)/(c z + d). Im(g z) = y / |c z + d|^2.
  The hyperbolic density: |f|^2. The flat density: |f|^2 / y^2.
  The flat density "in the chart moved by g1", carried back: the function z -> |f(g1 z)|^2 / Im(g1 z)^2
  = |f(z)|^2 |5 z + 1|^4 / y^2.  Its local maximum near the peak, compared with that of |f|^2 / y^2.

EXPECTATIONS, written before the run:
  E1  |f(g z)|^2 / |f(z)|^2 = 1 within 1e-20 for g1 and g2 at three points.
  E2  (|f|^2/y^2)(g z) / (|f|^2/y^2)(z) = |c z + d|^4 within 1e-20 at the same points.
  E3  |f|^2 and |f(g1 z)|^2 have the same local maximum near z* (distance below 1e-12).
  E4  The local maxima of |f|^2/y^2 and of |f(g1 z)|^2/Im(g1 z)^2 near z* are two strict local maxima more than 1e-3
      apart. (B1913 prints them 0.065 apart, near (0.2562, 0.3141) and (0.3149, 0.3430).)
  E5  Control: with the factor |5 z + 1|^4 replaced by 1, the two maxima coincide (distance below 1e-12).
"""
import os, sys
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "chat1_2026-11-11_golden_state"))
import golden_state_peak as g  # noqa: E402

mp.mp.dps = 30
g.C = g.euler_coefficients(g.NCOEF)
G1, G2 = (1, 0, 5, 1), (2, -1, 5, -2)


def moeb(m, z):
    a, b, c, d = m
    return (a * z + b) / (c * z + d)


def say(*a):
    print(*a, flush=True)


def d_hyp(z):
    return abs(g.f(z)) ** 2


def d_flat(z):
    return abs(g.f(z)) ** 2 / mp.im(z) ** 2


def d_moved(z):
    w = moeb(G1, z)
    return abs(g.f(w)) ** 2 / mp.im(w) ** 2


def d_moved_ctrl(z):
    w = moeb(G1, z)
    return abs(g.f(w)) ** 2 / mp.im(z) ** 2


def localmax(F, z0):
    def gr(x, y):
        return [mp.diff(lambda t: F(mp.mpc(t, y)), x), mp.diff(lambda t: F(mp.mpc(x, t)), y)]
    x, y = mp.findroot(gr, (mp.re(z0), mp.im(z0)), tol=mp.mpf(10) ** -24)
    z = mp.mpc(x, y)
    h = mp.mpf(10) ** -6
    fxx = (F(z + h) - 2 * F(z) + F(z - h)) / h ** 2
    fyy = (F(z + 1j * h) - 2 * F(z) + F(z - 1j * h)) / h ** 2
    fxy = (F(z + h + 1j * h) - F(z + h - 1j * h) - F(z - h + 1j * h) + F(z - h - 1j * h)) / (4 * h ** 2)
    strict = fxx < 0 and fxx * fyy - fxy ** 2 > 0
    return z, strict


def gridstart(F, z0):
    with mp.workdps(15):
        best = None
        for i in range(-12, 13):
            for j in range(-10, 11):
                z = z0 + mp.mpc(0.01 * i, 0.01 * j)
                v = F(z)
                if best is None or v > best[0]:
                    best = (v, z)
    return best[1]


ZS = mp.mpc("0.251539778143593605266", "0.369767142958202424432")  # this seat's peak of 2026-11-11
pts = [ZS, mp.mpc("0.31", "0.42"), mp.mpc("0.18", "0.55")]
e1 = e2 = True
for z in pts:
    for m in (G1, G2):
        w = moeb(m, z)
        r1 = d_hyp(w) / d_hyp(z)
        r2 = (d_flat(w) / d_flat(z)) / abs(m[2] * z + m[3]) ** 4
        say("E1/E2 z", mp.nstr(z, 6), "g", m, "|f|^2 ratio - 1 %s" % mp.nstr(r1 - 1, 3),
            "flat ratio / |cz+d|^4 - 1 %s" % mp.nstr(r2 - 1, 3), "|cz+d|^4 %s" % mp.nstr(abs(m[2] * z + m[3]) ** 4, 8))
        e1 &= abs(r1 - 1) < 1e-20
        e2 &= abs(r2 - 1) < 1e-20
say("E1 |f|^2 unchanged by g1 and g2:", e1)
say("E2 the flat density changes by |cz+d|^4:", e2)

zh, sh = localmax(d_hyp, ZS)
zm, sm = localmax(lambda z: d_hyp(moeb(G1, z)), ZS)
say("E3 max of |f|^2:", mp.nstr(zh, 20), "strict", sh, "; in the moved chart:", mp.nstr(zm, 20), "strict", sm,
    "; distance", mp.nstr(abs(zh - zm), 3), "; held:", abs(zh - zm) < 1e-12)

zf, sf = localmax(d_flat, gridstart(d_flat, ZS))
say("E4 max of the flat density, standard chart:", mp.nstr(zf, 12), "strict", sf)
zg, sg = localmax(d_moved, gridstart(d_moved, ZS))
say("E4 max of the flat density, moved chart, carried back:", mp.nstr(zg, 12), "strict", sg)
say("E4 distance:", mp.nstr(abs(zf - zg), 6), "; held:", bool(sf and sg and abs(zf - zg) > 1e-3))
say("E4 distance of the standard-chart flat maximum from z*:", mp.nstr(abs(zf - ZS), 6))
zc, sc = localmax(d_moved_ctrl, gridstart(d_moved_ctrl, ZS))
say("E5 control, factor removed:", mp.nstr(zc, 12), "; distance from the standard flat maximum",
    mp.nstr(abs(zc - zf), 3), "; held:", abs(zc - zf) < 1e-12)
