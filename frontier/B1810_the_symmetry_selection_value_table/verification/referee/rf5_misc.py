"""rf5: (1) first-launch vs current JSON: only the flag added?  (2) w -> -w at the fixed lines (a generic complex
direction, all sectors): (omega,(1/3,2/3)) vs (omega,(2/3,1/3)); (i,(1/2,1/2)) vs (i,(1/2,-1/2)).  (3) dtheta/dL of the
exception angle at L_max(i) and L_2(i) (a0 class, record's reading); where the '1'-channel weight 2 pi L + c_1 vanishes."""
import json, math
import numpy as np
from rf_common import *
P = pathlib.Path(__file__).resolve().parents[1]
a_, b_ = json.load(open(P / "symmetry_selection_table_first_launch.json")), json.load(open(P / "symmetry_selection_table_second_launch.json"))
ra, rb = a_["rows"], b_["rows"]
diffkeys = set(); numdiff = 0
for x, y in zip(ra, rb):
    for k in set(x) | set(y):
        if x.get(k) != y.get(k): diffkeys.add(k)
print("(1) rows", len(ra), len(rb), " keys that differ:", diffkeys)
a = np.array([0.3 + 0.7j, -1.1 + 0.2j, 0.4 - 0.9j])
for tau, p, q in ((W, (1/3, 2/3), (2/3, 1/3)), (I, (0.5, 0.5), (0.5, -0.5)), (I, (0.5, 0.5), (-0.5, -0.5))):
    for sn, (ql, qr) in SECT.items():
        L = RADII[tau][1]
        s1 = np.linalg.svd(Ymat(a, tau, p, ql, qr, L), compute_uv=False); s2 = np.linalg.svd(Ymat(a, tau, q, ql, qr, L), compute_uv=False)
        print("(2)", "omega" if tau == W else "i", p, "vs", q, sn, "max|ratio diff| %.1e" % np.max(abs(s1 / s1[0] - s2 / s2[0])))
def angle(L, d="a0"):
    av = direction(d, I)
    Uu, su, _ = svd_sorted(Ymat(av, I, (0.5, 0.5), 1, -4, L, True)); Ud, sd, _ = svd_sorted(Ymat(av, I, (0.5, 0.5), 1, 2, L, False))
    return np.abs(Uu.conj().T @ Ud)[0, 2], su[1] / su[2]
R, c = channels(I, (0.5, 0.5), 1, -4)
print("(3) '1'-channel weight vanishes at L =", -c["1"] / (2 * math.pi))
for L0 in RADII[I]:
    h = 1e-4; (v0, m0), (vp, mp_), (vm, mm) = angle(L0), angle(L0 + h), angle(L0 - h)
    print("(3) L=%.6f |V_ub|=%.6f m2/m3=%.6f  dlog|V_ub|/dlogL=%.3f  dlog(m2/m3)/dlogL=%.3f" % (L0, v0, m0, (math.log(vp) - math.log(vm)) / (2 * h) * L0, (math.log(mp_) - math.log(mm)) / (2 * h) * L0))
for L in (0.62, 0.65, 0.7, 1.0, 1.5, 2.0, 2.7193, 4, 8, 40, 2560):
    print("    L=%7.3f  a0-class |V_ub| = %.6f  m2/m3 = %.6f" % ((L,) + angle(L)))
