"""Reviewer check 3: U2(d)'s slopes (closed form, the instrument's own inputs), mp.diff's precision for th1'(0),
jtheta-built thetas at omega against the series, and the cost of one jtheta-built pairing at 40 digits."""
import sys, time
sys.path.insert(0, ".")
from rv_core import *

t = mp.mpc(0.13, 1.07)                       # TAUS[0] as the instrument builds it (from doubles)
yb = (mp.mpf("0.11"), mp.mpf("0.37")); u0 = mp.mpc(0.6, 0.35)
wy = wpt(yb, t)
print("== U2(d) slopes, closed form, delta = eps u0 - 2 w_y (NOT fixed) ==")
epss = [mp.mpf(10) ** (-k) for k in (1, 2, 3, 4)]
vals = []
for ep in epss:
    ub = ep * u0; de = ep * u0 - 2 * wy
    vals.append(rel_rr(closed_R(ub, de, t)))
sl = [(mp.log(vals[k + 1]) - mp.log(vals[k])) / (mp.log(epss[k + 1]) - mp.log(epss[k])) for k in range(3)]
print("  rel_rr:", [mp.nstr(v, 6) for v in vals]); print("  slopes:", [mp.nstr(s, 6) for s in sl])
print("== with delta truly fixed at -2 w_y ==")
vals2 = [rel_rr(closed_R(ep * u0, -2 * wy, t)) for ep in epss]
sl2 = [(mp.log(vals2[k + 1]) - mp.log(vals2[k])) / (mp.log(epss[k + 1]) - mp.log(epss[k])) for k in range(3)]
print("  slopes:", [mp.nstr(s, 6) for s in sl2])

print("\n== th1'(0): mp.diff of a jtheta-built th1 vs 2 pi eta^3 ==")
def th_j(n, u, tt):
    q = mp.exp(J * mp.pi * tt); x = mp.pi * u
    if n in (3, 4): return mp.jtheta(n, x, q)
    q4 = mp.exp(J * mp.pi * tt / 4); s = x + mp.pi * tt / 2
    if n == 2: return q4 * mp.exp(J * x) * mp.jtheta(3, s, q)
    return -J * q4 * mp.exp(J * x) * mp.jtheta(4, s, q)
for tt in (t, mp.mpc(-0.31, 0.88), mp.exp(2 * J * mp.pi / 3)):
    d = mp.diff(lambda u: th_j(1, u, tt), 0)
    print("  tau", mp.nstr(tt, 4), " |d/(2 pi eta^3) - 1| =", mp.nstr(abs(d / th1p(tt) - 1), 3))

print("\n== jtheta-built thetas vs series at omega (the plumbing check only runs at TAUS[0]) ==")
om = mp.exp(2 * J * mp.pi / 3)
for z in (mp.mpc("0.21", "0.17"), mp.mpc("0.33", "-0.12"), mp.mpc("1.7", "2.9")):
    print("  z", mp.nstr(z, 3), [mp.nstr(abs(th_j(n, z, om) / thr(n, z, om) - 1), 3) for n in (1, 2, 3, 4)])

print("\n== cost: one jtheta-built bilinear set (4 shifted thetas at 2tau + 2 th1) at 40 digits ==")
def thc(a, b, u, T): return mp.exp(J * mp.pi * a * a * T + 2 * J * mp.pi * a * (u + b)) * th_j(3, u + a * T + b, T)
z = mp.mpc("0.02", "0.0")
for (a, b) in [(mp.mpf("0.13"), mp.mpf("0.31")), (mp.mpf("5.3333"), mp.mpf("10.667"))]:
    t0 = time.time(); n = 30
    for _ in range(n):
        _ = [thc(a, b, z, 2 * om), thc(a, b, z + om, 2 * om), thc(-a, b, z, 2 * om), thc(-a, b, z + om, 2 * om),
             th_j(1, z, om), th_j(1, z + om, om)]
    dt = (time.time() - t0) / n
    print(f"  twist {float(a):.3f}: {dt*1e3:.2f} ms per bilinear set; the instrument recomputes it per unit (x4) per contour point")
