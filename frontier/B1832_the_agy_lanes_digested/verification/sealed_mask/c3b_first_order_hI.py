"""SEALED-DIGEST CHECK c3b (value-free; main's M_of / coupling / census directions).
Claim (agy relay l.294, Theorem 21 Part A): on a single order-10 strip line, turning on h_I != 0 moves D linearly while the
third-generation lepton/down relation is preserved 'to O(|h_i|^2)'.
By main's T-HALF-LIFT (B1832 1.3) the lepton sector's heaviest singular value at h equals the down sector's at Sigma_10 h
(h_I -> -h_I).  So the claim is a statement about the down sector alone: does f(h_I) = s3(Y_d(Sigma h)) - s3(Y_d(h)) start
at first order?  f is odd in h_I; f'(0) = -2 Re(h_I z3) with z3 = u3^+ Y_I v3 at h_I = 0 (Y_I = coupling(QI, M_d)).
FIREWALL: neither f nor any singular value is printed.  Printed: (i) doubling ratios f(2e)/f(e) (2 = first order, 8 = third)
for random phases of h_I; (ii) cos(arg h_I + arg z3) for main's census directions (both readings) -- 0 would mean the census
phase kills the first-order term."""
import math, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/recheck"))
from identities_and_order5 import M_of, S_of, B
from mirror_rule_probe import Z
rng = np.random.default_rng(1104)

def s3(S, M): return np.linalg.svd(B.coupling(S, M), compute_uv=False).max()
print("(i) doubling ratios f(2e)/f(e), random h with random phase of h_I (2 = linear in h_I)")
for tau in (0.3 + 2.6j, 0.18 + 1.7j):
    L = Z.radii(tau)[0]
    for p2 in (0.1, 0.3, 0.5):
        Md, _ = M_of(tau, (0.4, p2), L, "down")
        rr = []
        for _ in range(3):
            hjk = rng.normal(size=2) + 1j * rng.normal(size=2); ph = np.exp(1j * rng.uniform(0, 2 * np.pi))
            def f(e):
                h = np.array([e * ph, hjk[0], hjk[1]]); hs = np.array([-e * ph, hjk[0], hjk[1]])
                return s3(S_of(0, hs), Md) - s3(S_of(0, h), Md)
            rr.append(f(2e-4) / f(1e-4))
        print("  tau=%s line (2/5,%.1f): %s" % (tau, p2, " ".join("%.3f" % r for r in rr)))

print("(ii) census directions (main's Z.direction): cos(arg h_I + arg z3) at h_I -> 0, readings S and S~")
cs = []
for tau in (0.1 + 1.6j, 0.25 + 1.6j, 0.4 + 2.4j, 0.25 + 2.4j):
    L = Z.radii(tau)[0]
    for p2 in (0.1, 0.3, 0.5):
        Md, _ = M_of(tau, (0.4, p2), L, "down"); YI = B.coupling(B.QI, Md)
        for d in Z.DIRS:
            a = np.array(Z.direction(d, tau))
            for rd in ("S", "S~"):
                h = a if rd == "S" else np.conj(a)
                if abs(h[0]) < 1e-300: continue
                h0 = h.copy(); h0[0] = 0
                Yd = B.coupling(S_of(0, h0), Md); U, s, Vh = np.linalg.svd(Yd); k = int(np.argmax(s))
                z3 = U[:, k].conj() @ YI @ Vh.conj().T[:, k]
                c = math.cos(np.angle(h[0]) + np.angle(z3)); cs.append((abs(c), d, rd, tau, p2))
cs.sort()
print("  cases:", len(cs), "; smallest |cos|:", ["%.2e %s %s %s %.1f" % c for c in cs[:4]], "; median |cos|: %.3f" % cs[len(cs) // 2][0])
print("  fraction with |cos| < 1e-6:", sum(c[0] < 1e-6 for c in cs) / len(cs))
