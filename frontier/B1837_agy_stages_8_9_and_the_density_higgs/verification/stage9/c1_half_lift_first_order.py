"""S303 check c1 (value-free; main's frame code only: B1827 recheck M_of / S_of / B, B1821 cm_zero_line Z).
Decides rebuttal R1 of the agy lane's Theorem 71 (b66bfdf42) against B1832 S300 ('the QI admixture acts at first order').
On the five order-10 strip lines (2/5, (2j+1)/10), two tau inside 0 <= Re tau < 1, main's L_max radius:
 (a) the matrix identity Y_e(S) = lam * D * Y_d(Sigma10 S)^T * D  (Sigma10 flips h_I; D a sign diagonal, found by search);
 (b) for each generation k (light to heavy) f_k(e) = s_k(Y_d(Sigma10 h_e)) - s_k(Y_d(h_e)), h_e = h with h_I = e*phase:
     by (a) this is the same-Higgs lepton-minus-down difference.  Printed: doubling ratios f(2e)/f(e) only (2 = first
     order in h_I, 8 = third), at a0 = 0 and a0 != 0;
 (c) the same for |det Y|: g(e) = |det Y_d(Sigma10 h_e)| - |det Y_d(h_e)|: doubling ratios only, plus a YES/NO whether g
     vanishes identically (relative 1e-10);
 (d) the lane's Sigma10-even quantities (symmetrised spectra, |det(Y(+)Y(-))|): residuals (expected tautologies of (a)).
FIREWALL: no singular value, no cross-sector ratio, no deviation magnitude of a cross-sector quantity is printed."""
import itertools, math, os, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/recheck"))
from identities_and_order5 import M_of, S_of, B
from mirror_rule_probe import Z

rng = np.random.default_rng(3031104)
TAUS = (0.3 + 2.6j, 0.62 + 1.9j)
LINES = [(0.4, (2 * j + 1) / 10) for j in range(5)]


def Y(S, M):
    return B.coupling(S, M)


def sig(h):  # Sigma10: flip h_I (main's Q3 order is (QI, QJ, QK))
    g = np.array(h, dtype=complex).copy(); g[0] = -g[0]; return g


def sv(A):
    return np.sort(np.linalg.svd(A, compute_uv=False))


# (a) find D among sign diagonals and check the identity
Ds = [np.diag(s) for s in itertools.product((1, -1), repeat=3)]
worst_a = 0.0; Dfound = set(); ctrl = []
for tau in TAUS:
    L = Z.radii(tau)[0]
    for line in LINES:
        Md, _ = M_of(tau, line, L, "down"); Me, _ = M_of(tau, line, L, "lepton")
        for _ in range(4):
            h = rng.normal(size=3) + 1j * rng.normal(size=3); a0 = complex(*rng.normal(size=2))
            Ye = Y(S_of(a0, h), Me); Yd_s = Y(S_of(a0, sig(h)), Md)
            best = None
            for D in Ds:
                Bm = D @ Yd_s.T @ D
                lam = np.vdot(Bm.ravel(), Ye.ravel()) / np.vdot(Bm.ravel(), Bm.ravel()).real
                r = np.linalg.norm(Ye - lam * Bm) / np.linalg.norm(Ye)
                if best is None or r < best[0]: best = (r, tuple(np.diag(D)), abs(lam))
            worst_a = max(worst_a, best[0], abs(best[2] - 1)); Dfound.add(best[1] if best[1][0] > 0 else tuple(-x for x in best[1]))
            # control: without Sigma10 (same h in both)
            Bm = np.diag(best[1]) @ Y(S_of(a0, h), Md).T @ np.diag(best[1])
            lam = np.vdot(Bm.ravel(), Ye.ravel()) / np.vdot(Bm.ravel(), Bm.ravel()).real
            ctrl.append(np.linalg.norm(Ye - lam * Bm) / np.linalg.norm(Ye))
print("(a) Y_e(S) = lam D Y_d(Sigma10 S)^T D on 5 order-10 lines x 2 tau x 4 random S (a0 != 0): worst residual (incl. ||lam|-1|) %.1e; "
      "D (up to sign) = %s; control without Sigma10: min residual %.2f" % (worst_a, sorted(Dfound), min(ctrl)))

# (b)/(c) doubling ratios, down sector only
print("(b) doubling ratios f_k(2e)/f_k(e), f_k = s_k(Y_d(Sigma10 h)) - s_k(Y_d(h)), k = light, middle, heavy; (c) same for |det Y_d|")
allr = {0: [], 1: [], 2: [], "det": []}; det_zero = 0; ncase = 0
for tau in TAUS:
    L = Z.radii(tau)[0]
    for line in LINES:
        Md, _ = M_of(tau, line, L, "down")
        for a0mode in ("a0=0", "a0!=0"):
            for _ in range(2):
                hjk = rng.normal(size=2) + 1j * rng.normal(size=2); ph = np.exp(1j * rng.uniform(0, 2 * np.pi))
                a0 = 0 if a0mode == "a0=0" else complex(*rng.normal(size=2))
                def parts(e):
                    h = np.array([e * ph, hjk[0], hjk[1]]); hs = sig(h)
                    s1, s2 = sv(Y(S_of(a0, hs), Md)), sv(Y(S_of(a0, h), Md))
                    d1, d2 = abs(np.linalg.det(Y(S_of(a0, hs), Md))), abs(np.linalg.det(Y(S_of(a0, h), Md)))
                    return s1 - s2, d1 - d2, d2
                f1, g1, dd = parts(1e-4); f2, g2, _ = parts(2e-4)
                ncase += 1
                for k in range(3): allr[k].append(f2[k] / f1[k])
                if abs(g1) < 1e-10 * dd and abs(g2) < 1e-10 * dd: det_zero += 1
                else: allr["det"].append(g2 / g1)
for k in (0, 1, 2):
    a = np.array(allr[k]); print("   generation %d: %d cases, doubling ratio min %.4f max %.4f" % (k + 1, len(a), a.min(), a.max()))
a = np.array(allr["det"])
print("   |det|: vanishes identically in %d of %d cases; doubling ratio over the rest: %s" % (
    det_zero, ncase, ("min %.4f max %.4f" % (a.min(), a.max())) if len(a) else "-"))

# (d) the lane's Sigma10-even quantities (same lines, a0 != 0)
w_sym = 0.0; w_det = 0.0
for tau in TAUS:
    L = Z.radii(tau)[0]
    for line in LINES:
        Md, _ = M_of(tau, line, L, "down"); Me, _ = M_of(tau, line, L, "lepton")
        for _ in range(3):
            h = rng.normal(size=3) + 1j * rng.normal(size=3); a0 = complex(*rng.normal(size=2))
            ep, em = Y(S_of(a0, h), Me), Y(S_of(a0, sig(h)), Me); dp, dm = Y(S_of(a0, h), Md), Y(S_of(a0, sig(h)), Md)
            se, sd = sv(ep) + sv(em), sv(dp) + sv(dm)
            w_sym = max(w_sym, np.abs(se - sd).max() / sd.max())
            w_det = max(w_det, abs(abs(np.linalg.det(ep @ em)) - abs(np.linalg.det(dp @ dm))) / abs(np.linalg.det(dp @ dm)))
print("(d) Sigma10-symmetrised spectra and |det(Y(+)Y(-))|, lepton vs down: worst relative residuals %.1e, %.1e (tautologies of (a))" % (w_sym, w_det))
