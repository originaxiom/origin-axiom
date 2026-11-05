"""P-562 data-free (exploration tier, labelled; no measured value read): the singlet Higgs at its natural magnitude, BOTH sign
families from one pass -- same (c up, c down) and opposite (c up, -c down; a Higgs twisted like the matter has an identity
channel odd in the twist, and the up and down twists are opposite) -- for twelve phases c and c = 0.  Per point the residues
and channel norms of each sector are computed once (they do not depend on the Higgs), then every (family, c) is a cheap SVD.
Kept per (family, c): points where both quark sectors are hierarchical (m2/m3 < 0.1, m1/m3 < 0.01) and up is steeper than
down (two coarse facts of the measured world, disclosed).  Equal readings for up and down (B1739).  Writes a JSON beside it."""
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


def hier(s):
    return s[2] > 0 and 1e-12 < s[0] / s[2] < 0.01 and s[1] / s[2] < 0.1


def one(seed):
    from mirror_rule_probe import Z
    B = Z.mods()["B"]
    rng = np.random.default_rng(seed); L_ = lines(); dirs = [d for d in Z.DIRS if d not in ("F_-2", "R", "t=-5/288")]; res = []
    for _ in range(25):
        line = L_[int(rng.integers(len(L_)))]; tau = complex(float(rng.uniform(0.0, 0.5)), float(rng.uniform(1.0, 4.0)))
        d = dirs[int(rng.integers(len(dirs)))]; L = Z.radii(tau)[int(rng.integers(2))]; r = int(rng.integers(2))
        try:
            a = np.array(Z.direction(d, tau)); hh = complex(a @ a); Mm = {}
            w = B.line_w(line[0], line[1], tau)
            for sn, ql, qr in Z.SECTORS:
                if sn == "lepton": continue
                x, yy = B.sector_twists(w, tau, ql, qr); R = B.residues(x, yy, tau); cc = B.cA(x, yy, tau, R)
                u = {k: (math.sqrt(2 * math.pi * L + cc[k]) * R[k] if cc[k] is not None and 2 * math.pi * L + cc[k] > 0 else 0) for k in B.UNITS}
                Mm[sn] = B.weighted_M(u)
        except Exception:
            continue
        def U_of(sector, c):
            a0 = c * cmath.sqrt(hh) if c != 0 else 0.0
            Sm = a0 * np.eye(2) + a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
            if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
            u_, s, _ = np.linalg.svd(B.coupling(Sm, Mm[sector])); o = np.argsort(s); return u_[:, o], s[o]
        for fam, sign in (("same", 1), ("opposite", -1)):
            for ci, c in enumerate(PHASES):
                Uu, su = U_of("up", c); Ud, sd = U_of("down", sign * c)
                if not (hier(su) and hier(sd) and su[1] / su[2] < sd[1] / sd[2] / 2 and su[0] / su[2] < sd[0] / sd[2]): continue
                A = np.abs(Uu.conj().T @ Ud)
                res.append((fam, ci, float(A[0, 0]), float(A[0, 2]), float(A[2, 0])))
    return res


if __name__ == "__main__":
    seeds = range(int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else range(900, 980)
    with Pool(4) as P:
        R = [x for chunk in P.map(one, seeds) for x in chunk]
    out = []
    for fam in ("same", "opposite"):
        for ci, c in enumerate(PHASES):
            v = np.array([x[2:] for x in R if x[0] == fam and x[1] == ci])
            lab = "0" if c == 0 else "exp(2 pi i %d/12)" % (ci - 1)
            if not len(v): out.append({"family": fam, "c": lab, "n": 0}); continue
            good = (v[:, 1] < v[:, 2]) & (v[:, 0] > 0.9)
            out.append({"family": fam, "c": lab, "n": len(v), "frac_nature_order_and_Vud": float(good.mean()),
                        "frac_Vub_lt_Vtd": float((v[:, 1] < v[:, 2]).mean()), "frac_Vud_gt_0.9": float((v[:, 0] > 0.9).mean()),
                        "median_Vub_over_Vtd": float(np.median(v[:, 1] / np.maximum(v[:, 2], 1e-300)))})
    for o in out:
        if o["n"]: print("%-8s c %-18s n %4d  |V_ub|<|V_td| %.2f  |V_ud|>0.9 %.2f  both %.3f  median ratio %.3g" % (
            o["family"], o["c"], o["n"], o["frac_Vub_lt_Vtd"], o["frac_Vud_gt_0.9"], o["frac_nature_order_and_Vud"], o["median_Vub_over_Vtd"]))
    pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
