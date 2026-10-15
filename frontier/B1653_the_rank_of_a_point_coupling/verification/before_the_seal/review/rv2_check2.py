"""Reviewer, v2 review, check 2: (i) U4(a)'s float comparison; (ii) the mean-value property: which profiles lift."""
import sys
sys.path.insert(0, ".")
exec(open("rv2_check1.py").read().split("# U0(b): the control")[0])      # reuse the seeded setup and helpers

print("== (i) U4(a) as coded: float(overlap) against 1 - 1e-25 ==")
ov_mp = 1 - mp.mpf(10) ** -60
print("  1 - 1e-25 in float:", repr(1 - 1e-25), "| float(1 - 1e-60 as mpf):", repr(float(abs(ov_mp))),
      "| test float(ov) > 1 - 1e-25:", float(abs(ov_mp)) > 1 - 1e-25)
# the actual overlap at one seeded random line, as the instrument computes it (float of the mp value)
t = TAUS[0]; wl = U4LINES[0]
nu = left_null(coupling(SS[3], res_bil(twist_of(wl, t), twist_of(-4 * wl, t), t)))
nd = left_null(coupling(SS[5], res_bil(twist_of(wl, t), twist_of(2 * wl, t), t)))
o = overlap(nu, nd)
print("  seeded line 0: 1 - overlap (mp) =", mp.nstr(1 - o, 3), "| float(overlap) =", repr(float(o)), "| coded test passes:", float(o) > 1 - 1e-25)

print("\n== (ii) which spread profiles lift (pair 0, generic tau) ==")
x, y = PAIRS[0]; t = TAUS[0]; c0 = mp.mpc(0.3, 0.2)
def M_of(nodes, wfun):
    M = mp.matrix(2, 2)
    for z in nodes: M += wfun(z) * bilf(x, y, z, t)
    return M
def report(name, M):
    print(f"  {name:62s} |det M|/max^2 = {mp.nstr(abs(det2(M))/mx(M)**2, 4)};  min ratio over 20 S = {mp.nstr(min(ratio(coupling(S, M)) for S in SS), 4)}")
radii = [mp.mpf("0.03"), mp.mpf("0.06"), mp.mpf("0.1")]
g = lambda z: mp.exp(-abs(z - c0) ** 2 / mp.mpf("0.0025"))
for nper in (8, 12, 16):
    nodes = [c0 + r * mp.exp(2 * J * mp.pi * k / nper) for r in radii for k in range(nper)]
    report(f"radial weight about c0, {nper} nodes per circle", M_of(nodes, g))
nodes = [c0 + r * mp.exp(2 * J * mp.pi * k / 8) for r in radii for k in range(8)]
report("tilted weight g(z)(1 + 0.5 Re((z-c0)/0.1)), same 24 nodes", M_of(nodes, lambda z: g(z) * (1 + mp.re((z - c0) / mp.mpf("0.1")) / 2)))
report("elliptical weight exp(-(dx^2/0.0025 + dy^2/0.01)), same 24 nodes",
       M_of(nodes, lambda z: mp.exp(-(mp.re(z - c0) ** 2 / mp.mpf("0.0025") + mp.im(z - c0) ** 2 / mp.mpf("0.01")))))
report("off-centre radial weight about c0 + 0.04 on the same nodes", M_of(nodes, lambda z: mp.exp(-abs(z - c0 - mp.mpf("0.04")) ** 2 / mp.mpf("0.0025"))))
nodes0 = [r * mp.exp(2 * J * mp.pi * (k + mp.mpf(1) / 2) / 16) for r in radii for k in range(16)]
report("radial weight about the PUNCTURE (16 nodes per circle)", M_of(nodes0, lambda z: mp.exp(-abs(z) ** 2 / mp.mpf("0.0025"))))
