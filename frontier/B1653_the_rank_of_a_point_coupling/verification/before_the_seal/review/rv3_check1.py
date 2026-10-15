"""Reviewer, third pass: U6 exactly as v3 codes it, on the instrument's seeded draws, with the reviewer's series code."""
import sys
sys.path.insert(0, ".")
exec(open("rv2_check1.py").read().split("# U0(b): the control")[0])      # seeded PAIRS, SS; bilf, coupling, ratio, det2, mx

NT = 64
c0 = mp.mpc(0.3, 0.2)
RADII_REG = [mp.mpf(v) for v in ("0.01", "0.025", "0.04", "0.055", "0.07", "0.085", "0.1")]
RADII_PUN = [mp.mpf(v) for v in ("0.02", "0.035", "0.05", "0.065", "0.08", "0.1")]
def g(r): return mp.exp(-r ** 2 / mp.mpf("0.0025"))
PROFILES = {
 "a_radial_regular": (c0, RADII_REG, lambda z, r: g(r)),
 "b_tilted_regular": (c0, RADII_REG, lambda z, r: g(r) * (1 + mp.re(z - c0) / mp.mpf("0.05"))),
 "c_elliptic_regular": (c0, RADII_REG, lambda z, r: mp.exp(-(mp.re(z - c0) / mp.mpf("0.1")) ** 2 - (mp.im(z - c0) / mp.mpf("0.03")) ** 2)),
 "d_radial_puncture": (mp.mpc(0, 0), RADII_PUN, lambda z, r: g(r)),
}
TH = {"a_radial_regular": ("<", 1e-30, 1e-30), "b_tilted_regular": (">", 1e-5, 1e-6),
      "c_elliptic_regular": (">", 1e-4, 1e-6), "d_radial_puncture": (">", 1e-2, 1e-3)}
for name, (cen, radii, w) in PROFILES.items():
    dets, rats = [], []
    for (x, y) in PAIRS[:3]:
        M = mp.matrix(2, 2)
        for r in radii:
            for k in range(NT):
                z = cen + r * mp.exp(2 * J * mp.pi * k / NT); M += w(z, r) * r * bilf(x, y, z, TAUS[0])
        dets.append(abs(det2(M)) / mx(M) ** 2); rats.append(min(ratio(coupling(S, M)) for S in SS))
    op, td, tr = TH[name]
    if op == "<":
        md, mr = td / max(dets), tr / max(rats)
        print(f"{name:20s} det max {mp.nstr(max(dets),3)} (< {td}: margin {mp.nstr(md,2)}x); ratio max {mp.nstr(max(rats),3)} (< {tr}: margin {mp.nstr(mr,2)}x)")
    else:
        md, mr = min(dets) / td, min(rats) / tr
        print(f"{name:20s} det {mp.nstr(min(dets),3)}..{mp.nstr(max(dets),3)} (> {td}: margin {mp.nstr(md,3)}x); "
              f"ratio min {mp.nstr(min(rats),3)} (> {tr}: margin {mp.nstr(mr,3)}x)")
