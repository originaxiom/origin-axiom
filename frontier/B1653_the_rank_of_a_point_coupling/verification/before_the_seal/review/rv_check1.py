"""Reviewer check 1: the form, kappa, c1 across twists AND tau; U0's laws; the naive-frame control's true condition."""
import sys
sys.path.insert(0, ".")
from rv_core import *

taus = [mp.mpc("0.13", "1.07"), mp.mpc("-0.31", "0.88"), mp.exp(2 * J * mp.pi / 3)]
pts = [mp.mpc("0.21", "0.17"), mp.mpc("0.33", "-0.12"), mp.mpc("-0.4", "0.29")]
pairs = [((mp.mpf("0.13"), mp.mpf("0.31")), (mp.mpf("-0.07"), mp.mpf("0.22"))),
         ((mp.mpf("0.4"), mp.mpf("-0.15")), (mp.mpf("0.25"), mp.mpf("0.6"))),
         ((mp.mpf("-0.33"), mp.mpf("0.81")), (mp.mpf("0.12"), mp.mpf("-0.47"))),
         ((mp.mpf("2.3"), mp.mpf("-3.1")), (mp.mpf("-1.7"), mp.mpf("4.4")))]   # large twists, as at the lines

print("== form, kappa, c1 ==")
c1s = []
for t in taus:
    for (x, y) in pairs:
        A = x[0] + y[0]; ub = wpt(x, t) + wpt(y, t); de = wpt(x, t) - wpt(y, t)
        N = {}; spread = 0
        for s in "1ijk":
            vals = [pairings(x, y, z, t)[s] * thr(1, z, t) * mp.exp(-2 * J * mp.pi * A * z) / thr(RTH[s], z + ub, t) for z in pts]
            N[s] = vals[0]; spread = max(spread, max(abs(v / vals[0] - 1) for v in vals[1:]))
        kap = {s: N[s] / (CC[s] * thr(RTH[s], de, t)) for s in "ijk"}
        kspread = max(abs(kap[s] / kap["i"] - 1) for s in "ijk")
        c1 = N["1"] / (thr(1, de, t) * kap["i"])
        c1s.append(c1)
        print(f"tau={mp.nstr(t,4)} x={[float(v) for v in x]} y={[float(v) for v in y]}: form spread {mp.nstr(spread,3)}, "
              f"kappa spread {mp.nstr(kspread,3)}, c1 = {mp.nstr(c1,12)}")
print("c1 spread over all (tau, pair):", mp.nstr(max(abs(c / c1s[0] - 1) for c in c1s), 3))

print("\n== U0 laws (D frame) and the naive frame ==")
def hol(x, y, z, t, frame):
    (ax, bx), (ay, by) = x, y
    B0 = bil(x, y, z, t, frame); B1 = bil(x, y, z + 1, t, frame); Bt = bil(x, y, z + t, t, frame)
    la = mp.exp(2 * J * mp.pi * (ax + ay)); lb = mp.exp(2 * J * mp.pi * (-(bx + by) / 2))
    Ea = B1 - la * QI * B0 * QI.T; Eb = Bt - lb * QJ * B0 * QJ.T
    n = max(abs(B0[m, k]) for m in range(2) for k in range(2))
    ea = max(abs(Ea[m, k]) for m in range(2) for k in range(2)) / n
    eb = max(abs(Eb[m, k]) for m in range(2) for k in range(2)) / n
    # best scalar for the tau law in this frame (does ANY scalar work?)
    M = QJ * B0 * QJ.T
    lam = Bt[0, 0] / M[0, 0]
    ebest = max(abs(Bt[m, k] - lam * M[m, k]) for m in range(2) for k in range(2)) / n
    return ea, eb, ebest

t = taus[0]; z = pts[0]
cases = {"generic": pairs[0],
         "bx = by = 0.3": ((mp.mpf("0.1"), mp.mpf("0.3")), (mp.mpf("-0.2"), mp.mpf("0.3"))),
         "bx=1, by=-1 (odd ints, bx-by=2)": ((mp.mpf("0.1"), mp.mpf(1)), (mp.mpf("-0.2"), mp.mpf(-1))),
         "bx=2, by=0 (bx != by, even)": ((mp.mpf("0.1"), mp.mpf(2)), (mp.mpf("-0.2"), mp.mpf(0))),
         "bx=0.3, by=-1.7 (bx-by=2)": ((mp.mpf("0.1"), mp.mpf("0.3")), (mp.mpf("-0.2"), mp.mpf("-1.7")))}
for name, (x, y) in cases.items():
    ea, eb, _ = hol(x, y, z, t, True)
    na, nb, nbest = hol(x, y, z, t, False)
    print(f"{name:34s} D-frame: 1-law {mp.nstr(ea,3)}, tau-law {mp.nstr(eb,3)} | naive: 1-law {mp.nstr(na,3)}, "
          f"tau-law (coded lb) {mp.nstr(nb,3)}, tau-law best scalar {mp.nstr(nbest,3)}")

print("\n== the field's own tau-multiplier: psi2 = -b/2? ==")
# multiplier of the single-field pairing's U(1) part: compare pairing(x, y0) at z+tau / z for y0 untwisted and x twisted
x = (mp.mpf("0.17"), mp.mpf("0.29")); y0 = (mp.mpf(0), mp.mpf(0))
for s in "ijk":
    p0 = pairings(x, y0, z, t)[s]; p1 = pairings(x, y0, z + 1, t)[s]; pt_ = pairings(x, y0, z + t, t)[s]
    # spin-structure sign from the untwisted pairing
    q0 = pairings(y0, y0, z, t)[s]; q1 = pairings(y0, y0, z + 1, t)[s]; qt = pairings(y0, y0, z + t, t)[s]
    m1 = (p1 / p0) / (q1 / q0); mt = (pt_ / p0) / (qt / q0)
    print(s, "U(1) multiplier along 1:", mp.nstr(m1, 10), " e^{2pi i a} =", mp.nstr(mp.exp(2 * J * mp.pi * x[0]), 10),
          "| along tau:", mp.nstr(mt, 10), " e^{-i pi b} =", mp.nstr(mp.exp(-J * mp.pi * x[1]), 10))
