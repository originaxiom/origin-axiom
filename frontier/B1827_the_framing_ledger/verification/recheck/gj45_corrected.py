"""B1827 RECHECK, part 3 (data-free; replaces gj45_probe.py's labels): the singlet's EFFECTIVE Clebsch kappa = -k (exact on
all 24 order-5 lines: M_e = lam M_d^T with lam^5 = 1, so Y_e(k a0 + h.Q) = lam [Y_d^(3)T - k Y_d^(1)T]).  SU(5)'s 5 is
kappa = +1 (k = -1: must give exactly 1, a check), its 45 is kappa = -3 (k = +3).  Also kappa = +3 (k = -3, what S290
reported as 'the 45') and kappa = -1 (k = +1, the frame's own singlet entering down and lepton equally).
Grid: all 24 order-5 lines x Im tau in {1.9, 2.6, 3.2} (Re 0.3) x both radii x three directions x both readings x phases
c in {1, e^(i pi/3), e^(i pi/6)}, |a0| = |sqrt(h.h)|.  Reported per kappa: the median and quartiles of
D2 = (m_mu/m_tau)/(m_s/m_b) and D1 = (m_e/m_tau)/(m_d/m_b); the fraction with 2 < D2 < 4.5 and with 1/4.5 < D1 < 1/2."""
import cmath, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1827_the_framing_ledger" / "verification" / "scans"))
from mirror_rule_probe import Z
from identities_and_order5 import M_of, S_of, B
lines5 = sorted({(F(a, 5), F(b, 5)) for a in range(5) for b in range(5) if math.gcd(math.gcd(a, b), 5) == 1})
K = {+1: -1, -3: +3, +3: -3, -1: +1}          # kappa -> code k
res = {kap: [] for kap in K}
for line in lines5:
    for tau in (complex(0.3, 1.9), complex(0.3, 2.6), complex(0.3, 3.2)):
        for L in Z.radii(tau):
            Md, _ = M_of(tau, line, L, "down"); Me, _ = M_of(tau, line, L, "lepton")
            for d in ("DR", "F_6", "F_22"):
                h = np.array(Z.direction(d, tau))
                for r in (0, 1):
                    for c in (1, cmath.exp(1j * math.pi / 3), cmath.exp(1j * math.pi / 6)):
                        a0 = c * cmath.sqrt(h @ h)
                        def sv(S, M):
                            if r: S = B.EPS @ S.conj() @ B.EPS.T
                            s = np.sort(np.linalg.svd(B.coupling(S, M), compute_uv=False)); return s / s[2]
                        sd = sv(S_of(a0, h), Md)
                        for kap, k in K.items():
                            se = sv(S_of(k * a0, h), Me)
                            if sd[0] > 1e-14 and se[0] > 1e-14: res[kap].append((se[1] / sd[1], se[0] / sd[0]))
print("cases per kappa:", {k: len(v) for k, v in res.items()})
for kap in (+1, -1, -3, +3):
    v = np.array(res[kap]); D2, D1 = v[:, 0], v[:, 1]
    q = lambda x: "median %.3g  [%.3g, %.3g]" % tuple(np.percentile(x, [50, 25, 75]))
    print("kappa %+d (code k %+d): D2 %s  frac(2<D2<4.5) %.2f | D1 %s  frac(1/4.5<D1<1/2) %.2f | both %.3f" % (
        kap, K[kap], q(D2), ((D2 > 2) & (D2 < 4.5)).mean(), q(D1), ((D1 > 1 / 4.5) & (D1 < 0.5)).mean(),
        ((D2 > 2) & (D2 < 4.5) & (D1 > 1 / 4.5) & (D1 < 0.5)).mean()))
