"""rf1: (a) channel residues and weights 2 pi L + c_k at every configuration and sector (is any channel silently zeroed?);
(b) Y_up vs Y_down proportionality (up to a phase) at the four configurations; (c) full V for every (0,0,1)-pattern row
and every V-defined row: is it a permutation (all nine entries 0/1)?; min singular-value gaps over V-defined rows."""
import itertools, json, math
import numpy as np
from rf_common import *

CONF = [("(i, 0)", I, (0, 0)), ("(omega, 0)", W, (0, 0)), ("(i, (1/2, 1/2))", I, (0.5, 0.5)), ("(omega, (1/3, 2/3))", W, (1/3, 2/3))]
DIRS = ["DR", "a0", "R", "t", "F_6", "F_10", "F_14", "F_22"]
out = {"channels": {}, "proportional": {}, "rows": []}
for cn, tau, p in CONF:
    for sn, (ql, qr) in SECT.items():
        R, c = channels(tau, p, ql, qr)
        out["channels"][f"{cn} {sn}"] = {k: {"|R|": abs(R[k]), "c": c[k], "2piLmax+c": (2*math.pi*RADII[tau][0] + c[k]) if c[k] is not None else None} for k in R}
        print(cn, sn, {k: (round(abs(R[k]), 6), None if c[k] is None else round(c[k], 6)) for k in R}, flush=True)
    # (b) proportionality, for a generic complex direction
    a = np.array([0.3 + 0.7j, -1.1 + 0.2j, 0.4 - 0.9j])
    for L in RADII[tau]:
        Yu = Ymat(a, tau, p, 1, -4, L); Yd = Ymat(a, tau, p, 1, 2, L); Yl = Ymat(a, tau, p, -3, 6, L)
        def prop(A, Bm):
            z = np.vdot(A.ravel(), Bm.ravel()) / np.vdot(A.ravel(), A.ravel())
            return float(np.linalg.norm(Bm - z * A) / np.linalg.norm(Bm)), complex(z)
        out["proportional"][f"{cn} L={L:.4f}"] = {"down vs up": str(prop(Yu, Yd)), "lepton vs up": str(prop(Yu, Yl))}
        print(cn, "L=%.4f" % L, "down~up", prop(Yu, Yd), "lepton~up", prop(Yu, Yl), flush=True)

nonperm = []; mingap = 1.0
for cn, tau, p in CONF:
    if tau == W: continue
    for d in DIRS:
        a = direction(d, tau)
        for Ln, L in zip(("L_max", "L_2"), RADII[tau]):
            for rd in itertools.product((0, 1), repeat=2):
                Uu, su, _ = svd_sorted(Ymat(a, tau, p, 1, -4, L, rd[0])); Ud, sd, _ = svd_sorted(Ymat(a, tau, p, 1, 2, L, rd[1]))
                gaps = [(s[1] - s[0]) / s[2] for s in (su, sd)] + [(s[2] - s[1]) / s[2] for s in (su, sd)]
                if min(gaps) < 1e-8: continue
                mingap = min(mingap, min(gaps))
                Vm = Uu.conj().T @ Ud; A = np.abs(Vm)
                isperm = bool(np.all(np.minimum(A, np.abs(1 - A)) < 1e-6))
                J = float(np.imag(Vm[0, 1] * Vm[1, 2] * np.conj(Vm[0, 2]) * np.conj(Vm[1, 1])))
                rec = {"config": cn, "dir": d, "radius": Ln, "reading(up,down)": "".join("S~" if r else "S" for r in rd),
                       "|V|": np.round(A, 6).tolist(), "is_perm": isperm, "J": J, "min gap": min(gaps),
                       "3-entry": [round(float(A[0, 1]), 6), round(float(A[1, 2]), 6), round(float(A[0, 2]), 6)]}
                out["rows"].append(rec)
                if not isperm: nonperm.append(rec)
print("V-defined (up,down) reading pairs at i:", len(out["rows"]), "(x2 lepton readings = %d table rows)" % (2 * len(out["rows"])))
print("non-permutation (full 9-entry test):", len(nonperm), " min gap over V-defined:", mingap)
p001 = [r for r in out["rows"] if r["3-entry"] == [0.0, 0.0, 1.0] or (r["3-entry"][2] > 1 - 1e-6 and r["3-entry"][0] < 1e-6)]
for r in p001: print("(0,0,1) row:", r["config"], r["dir"], r["radius"], r["reading(up,down)"], "perm" if r["is_perm"] else "NOT PERM", r["|V|"])
for r in nonperm: print("NONPERM", r["config"], r["dir"], r["radius"], r["reading(up,down)"], r["|V|"], "J=%.2e" % r["J"])
json.dump(out, open(HERE / "rf1_channels_and_fullV.json", "w"), indent=1, default=str)
