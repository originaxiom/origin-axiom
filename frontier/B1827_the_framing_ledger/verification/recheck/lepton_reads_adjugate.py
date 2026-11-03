"""B1827 RECHECK, part 4 (data-free): the matrix identity Y_e(S) = -lam Y_d(adj S)^T on all 24 order-5 lines (lam the fifth
root of unity of down_lepton_relation.py), for 4D Higgs S at random singlet phases, every direction of four, both radii,
three tau; the reading applied as in the scans (S -> S~ first).  It follows from M_e = lam M_d^T and V2's
Y(S, M) = -Y(adj S, M^T)^T; checked here on the frame's own matrices."""
import cmath, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1827_the_framing_ledger" / "verification" / "scans"))
from mirror_rule_probe import Z
from identities_and_order5 import M_of, S_of, B, adj
lines5 = sorted({(F(a, 5), F(b, 5)) for a in range(5) for b in range(5) if math.gcd(math.gcd(a, b), 5) == 1})
rng = np.random.default_rng(5); worst = 0.0; n = 0; lam1 = 0
for line in lines5:
    for tau in (complex(0.3, 1.9), complex(0.12, 2.6), complex(0.45, 3.2)):
        for L in Z.radii(tau):
            Md, _ = M_of(tau, line, L, "down"); Me, _ = M_of(tau, line, L, "lepton")
            lam = np.vdot(Md.T.ravel(), Me.ravel()) / np.vdot(Md.T.ravel(), Md.T.ravel())
            assert abs(abs(lam) - 1) < 1e-9 and abs(lam ** 5 - 1) < 1e-9
            for d in ("DR", "F_6", "F_22", "a0"):
                h = np.array(Z.direction(d, tau))
                for r in (0, 1):
                    S = S_of(cmath.sqrt(h @ h) * cmath.exp(2j * math.pi * rng.random()), h)
                    if r: S = B.EPS @ S.conj() @ B.EPS.T
                    Ye, Yd_adj = B.coupling(S, Me), B.coupling(adj(S), Md)
                    worst = max(worst, np.linalg.norm(Ye + lam * Yd_adj.T) / np.linalg.norm(Ye)); n += 1
    lam1 += abs(lam - 1) < 1e-9
print("Y_e(S) = -lam Y_d(adj S)^T over %d cases on the 24 order-5 lines: worst relative deviation %.1e  %s; lam = 1 on %d lines" % (
    n, worst, "PASS" if worst < 1e-9 else "FAIL", lam1))
