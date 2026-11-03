"""B1827 RECHECK, part 2 (data-free): on each of the 24 order-5 lines, the relation between the lepton and down channel
matrices, and the singlet's EFFECTIVE Clebsch: with a 4D Higgs S = a0 + h.Q entering down as S and leptons as
S_k = k a0 + h.Q, for which k are the down and lepton spectra identical (the 5's relation, Clebsch +1 in SU(5)'s sense)?
The identity Y(S, M) = -Y(adj S, M^T)^T (V2) predicts k = -1 wherever M_e = M_d^T up to a phase."""
import cmath, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1827_the_framing_ledger" / "verification" / "scans"))
from mirror_rule_probe import Z
from identities_and_order5 import M_of, S_of, B
lines5 = sorted({(F(a, 5), F(b, 5)) for a in range(5) for b in range(5) if math.gcd(math.gcd(a, b), 5) == 1})
for line in lines5:
    tau = complex(0.3, 2.6); L = Z.radii(tau)[1]
    Md, _ = M_of(tau, line, L, "down"); Me, _ = M_of(tau, line, L, "lepton")
    # M_e = lam * M_d^T ?  lam from least squares
    lam = np.vdot(Md.T.ravel(), Me.ravel()) / np.vdot(Md.T.ravel(), Md.T.ravel())
    res = np.linalg.norm(Me - lam * Md.T) / np.linalg.norm(Me)
    out = []
    for k in (-1, +1, -3, +3):
        dev = 0.0
        for d in ("DR", "F_6", "F_22"):
            h = np.array(Z.direction(d, tau)); a0 = cmath.sqrt(h @ h) * cmath.exp(0.7j)
            sd = np.sort(np.linalg.svd(B.coupling(S_of(a0, h), Md), compute_uv=False))
            se = np.sort(np.linalg.svd(B.coupling(S_of(k * a0, h), Me), compute_uv=False))
            dev = max(dev, np.abs(se / sd - 1).max())
        out.append("k=%+d %.1e" % (k, dev))
    print("(%s,%s)  M_e = lam M_d^T: lam %s, residual %.1e  | spectra e vs d, max rel dev: %s" % (
        line[0], line[1], np.round(lam, 4), res, "  ".join(out)), flush=True)
