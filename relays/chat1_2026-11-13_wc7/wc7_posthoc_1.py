#!/usr/bin/env python3
"""W-C7, post hoc 1, written after the sealed run stopped and committed before its own run.

The sealed run held E1 and E2 (the |f|^2 ratio and the flat ratio over |cz+d|^4 are 1 to 3e-30 at all six cases),
then stopped in E3: the moved chart evaluates f at g1 z, whose imaginary part near the peak is about 0.043, and the
sealed code's series refuses there ("too many terms needed"; the numerical derivative raises the working precision).
THE CHANGE, and nothing else: the moved chart's densities are computed in the standard chart through the identity the
sealed run's E1 and E2 checked, |f(g1 z)|^2 = |f(z)|^2 and Im(g1 z) = y / |5z + 1|^2, so
    |f(g1 z)|^2 = |f(z)|^2   and   |f(g1 z)|^2 / Im(g1 z)^2 = |f(z)|^2 |5z + 1|^4 / y^2.
E3 then compares a function with itself and cannot fail; it is reported, not counted. E4 and E5 keep their sealed
wording and tolerances.

    python3 -I -u wc7_posthoc_1.py
"""
import contextlib, io, os, runpy, sys
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    try:
        s = runpy.run_path(os.path.join(HERE, "wc7_checks.py"), run_name="sealed")
    except SystemExit:
        pass
# the sealed module runs E1/E2 and stops; rebuild its definitions from the module it imports
sys.path.insert(0, os.path.join(HERE, "..", "chat1_2026-11-11_golden_state"))
import golden_state_peak as g  # noqa: E402
mp.mp.dps = 30
g.C = g.euler_coefficients(g.NCOEF)
src = open(os.path.join(HERE, "wc7_checks.py")).read()
ns = {}
exec(src.split("ZS = ")[0].split("mp.mp.dps = 30")[1].replace("g.C = g.euler_coefficients(g.NCOEF)", ""), {"g": g, "mp": mp, **ns}, ns)
localmax, gridstart, d_flat, d_hyp = ns["localmax"], ns["gridstart"], ns["d_flat"], ns["d_hyp"]
ZS = mp.mpc("0.251539778143593605266", "0.369767142958202424432")


def say(*a):
    print(*a, flush=True)


def d_moved(z):
    return d_flat(z) * abs(5 * z + 1) ** 4


zh, sh = localmax(d_hyp, ZS)
say("E3 (reported only) max of |f|^2:", mp.nstr(zh, 20), "strict", sh, "; distance from z*", mp.nstr(abs(zh - ZS), 3))
zf, sf = localmax(d_flat, gridstart(d_flat, ZS))
say("E4 max of the flat density, standard chart:", mp.nstr(zf, 12), "strict", sf)
zg, sg = localmax(d_moved, gridstart(d_moved, ZS))
say("E4 max of the flat density, moved chart, carried back:", mp.nstr(zg, 12), "strict", sg)
say("E4 distance:", mp.nstr(abs(zf - zg), 6), "; held:", bool(sf and sg and abs(zf - zg) > 1e-3))
say("E4 distance of the standard-chart flat maximum from z*:", mp.nstr(abs(zf - ZS), 6))
zc, sc = localmax(d_flat, gridstart(d_flat, ZS))
say("E5 control, factor removed:", mp.nstr(zc, 12), "; distance", mp.nstr(abs(zc - zf), 3), "; held:", abs(zc - zf) < 1e-12)
