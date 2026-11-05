"""The agy lane's framing, tested data-free (exploration tier, labelled; no measured value read): a singlet (identity-channel)
Higgs component at its natural magnitude, a0 = c * sqrt(h.h) (|a0|^2 = |h.h|, so |det S| = |1 + c^2| |h.h|), one FIXED phase c
for both quark sectors.  At random addresses (a line of order <= 12, tau in the band, a direction of the twelve, a radius, ONE
reading for up and down -- equal readings, B1739), for each c in twelve phases (c = 0 the frame itself), the up and down
singular vectors of the coupling with S = a0 I + a.Q.  Kept per c: points where both sectors are hierarchical (m2/m3 < 0.1,
m1/m3 < 0.01) and up is steeper than down (two coarse facts, disclosed).  Reported per c: the fraction with |V_ub| < |V_td| and
|V_ud| > 0.9, and the median corner ratio.  Writes a JSON beside it."""
import cmath, json, math, pathlib, sys
from fractions import Fraction as F
from multiprocessing import Pool
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

PHASES = [0] + [cmath.exp(2j * math.pi * k / 12) for k in range(12)]


def lines():
    out = set()
    for N in range(1, 13):
        for a in range(N):
            for b in range(N):
                if math.gcd(math.gcd(a, b), N) == 1: out.add((F(a, N), F(b, N)))
    return sorted(out)


def sector_U4(tau, line, d, L, r, sector, c):
    from mirror_rule_probe import Z
    B = Z.mods()["B"]
    sn, ql, qr = [s for s in Z.SECTORS if s[0] == sector][0]
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); cc = B.cA(x, yy, tau, R)
    a = np.array(Z.direction(d, tau)); hh = complex(a @ a); a0 = c * cmath.sqrt(hh) if c != 0 else 0.0
    Sm = a0 * np.eye(2) + a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    u = {k: (math.sqrt(2 * math.pi * L + cc[k]) * R[k] if cc[k] is not None and 2 * math.pi * L + cc[k] > 0 else 0) for k in B.UNITS}
    Y = B.coupling(Sm, B.weighted_M(u)); u_, s, _ = np.linalg.svd(Y); o = np.argsort(s)
    return u_[:, o], s[o]


def hier(s):
    return s[2] > 0 and 1e-12 < s[0] / s[2] < 0.01 and s[1] / s[2] < 0.1


def one(seed):
    from mirror_rule_probe import Z
    rng = np.random.default_rng(seed); L_ = lines(); dirs = [d for d in Z.DIRS if d not in ("F_-2", "R", "t=-5/288")]; res = []
    for _ in range(25):
        line = L_[int(rng.integers(len(L_)))]; tau = complex(float(rng.uniform(0.0, 0.5)), float(rng.uniform(1.0, 4.0)))
        d = dirs[int(rng.integers(len(dirs)))]; L = Z.radii(tau)[int(rng.integers(2))]; r = int(rng.integers(2))
        for ci, c in enumerate(PHASES):
            try:
                Uu, su = sector_U4(tau, line, d, L, r, "up", c); Ud, sd = sector_U4(tau, line, d, L, r, "down", c)
            except Exception:
                continue
            if not (hier(su) and hier(sd) and su[1] / su[2] < sd[1] / sd[2] / 2 and su[0] / su[2] < sd[0] / sd[2]): continue
            A = np.abs(Uu.conj().T @ Ud)
            res.append((ci, float(A[0, 0]), float(A[0, 2]), float(A[2, 0])))
    return res


if __name__ == "__main__":
    with Pool(4) as P:
        R = [x for chunk in P.map(one, range(700, 780)) for x in chunk]
    out = []
    for ci, c in enumerate(PHASES):
        v = np.array([x[1:] for x in R if x[0] == ci])
        if not len(v): out.append({"c": str(c), "n": 0}); continue
        good = (v[:, 1] < v[:, 2]) & (v[:, 0] > 0.9)
        out.append({"c": "0" if c == 0 else "exp(2 pi i %d/12)" % (ci - 1), "n": len(v), "frac_nature_order_and_Vud": float(good.mean()),
                    "frac_Vub_lt_Vtd": float((v[:, 1] < v[:, 2]).mean()), "frac_Vud_gt_0.9": float((v[:, 0] > 0.9).mean()),
                    "median_Vub_over_Vtd": float(np.median(v[:, 1] / np.maximum(v[:, 2], 1e-300)))})
    for o in out:
        if o["n"]: print("c %-18s n %4d  |V_ub|<|V_td| %.2f  |V_ud|>0.9 %.2f  both %.2f  median ratio %.3g" % (
            o["c"], o["n"], o["frac_Vub_lt_Vtd"], o["frac_Vud_gt_0.9"], o["frac_nature_order_and_Vud"], o["median_Vub_over_Vtd"]))
    pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
