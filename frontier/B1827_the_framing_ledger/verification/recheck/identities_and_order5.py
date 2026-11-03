"""B1827 RECHECK (main, 2026-11-03, the owner's 'make sure all claims are right'): exact identities behind S290 and the
order-5 claim over ALL order-5 lines.  Data-free.
V1  adj(S) = eps S^T eps^T = det(S) S^-1 = a0 - h.Q;  S~ = eps S* eps^T = a0* + h*.Q;  det S = a0^2 + h.h.
V2  the frame's coupling is linear in S, and Y(S, M) = -Y(adj S, M^T)^T for every S, M (its algebra).
V3  on every order-5 line (24), at three tau, both radii: M_e vs M_d^T, M_u vs M_u^T; R_1(up); Y_u(h.Q) symmetric;
    the singlet's part of Y_u antisymmetric; Y_e(S) = -Y_d(adj S)^T; down and lepton spectra (3D Higgs) equal.
V4  at a0 = +-i sqrt(h.h) det S = 0 and the lightest state of every sector is massless (why two phases had no points)."""
import cmath, itertools, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1827_the_framing_ledger" / "verification" / "scans"))
from mirror_rule_probe import Z
B = Z.mods()["B"]
Q3 = (B.QI, B.QJ, B.QK)
def S_of(a0, h): return a0 * np.eye(2) + sum(h[i] * Q3[i] for i in range(3))
def adj(S): return B.EPS @ S.T @ B.EPS.T
def M_of(tau, line, L, sector):
    sn, ql, qr = [s for s in Z.SECTORS if s[0] == sector][0]
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.weighted_M(u), R


if __name__ == "__main__":
    rng = np.random.default_rng(20261103)
    dev = 0.0
    for _ in range(500):
        h = rng.normal(size=3) + 1j * rng.normal(size=3); a0 = complex(*rng.normal(size=2)); S = S_of(a0, h)
        M = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        dev = max(dev, np.abs(adj(S) - np.linalg.det(S) * np.linalg.inv(S)).max(), np.abs(adj(S) - S_of(a0, -h)).max(),
                  np.abs(B.EPS @ S.conj() @ B.EPS.T - S_of(np.conj(a0), np.conj(h))).max(), abs(np.linalg.det(S) - (a0 ** 2 + h @ h)),
                  np.abs(B.coupling(-S, M) + B.coupling(S, M)).max(),
                  np.abs(B.coupling(S, M) + B.coupling(adj(S), M.T).T).max())
    print("V1+V2 max deviation over 500 random (S, M): %.1e  %s" % (dev, "PASS" if dev < 1e-12 else "FAIL"), flush=True)

    lines5 = sorted({(F(a, 5), F(b, 5)) for a in range(5) for b in range(5) if math.gcd(math.gcd(a, b), 5) == 1})
    assert len(lines5) == 24
    worst = dict(MeMdT=0.0, MuMuT=0.0, R1u=0.0, Yu_sym=0.0, Yu1_anti=0.0, Ye_adj=0.0, spec=0.0)
    specM = 0.0; n = 0
    for line in lines5:
        for tau in (complex(0.3, 2.6), complex(0.12, 1.9), complex(0.45, 3.2)):
            for L in Z.radii(tau):
                Mu, Ru = M_of(tau, line, L, "up"); Md, _ = M_of(tau, line, L, "down"); Me, _ = M_of(tau, line, L, "lepton")
                nd = np.linalg.norm(Md); nu = np.linalg.norm(Mu)
                worst["MeMdT"] = max(worst["MeMdT"], np.linalg.norm(Me - Md.T) / nd)
                worst["MuMuT"] = max(worst["MuMuT"], np.linalg.norm(Mu - Mu.T) / nu)
                worst["R1u"] = max(worst["R1u"], abs(Ru["1"]) / max(abs(Ru[k]) for k in Ru))
                for d in ("DR", "F_6", "F_22", "a0"):
                    h = np.array(Z.direction(d, tau)); a0 = cmath.sqrt(h @ h) * cmath.exp(0.7j)
                    for r in (0, 1):
                        S = S_of(a0, h); S3 = S_of(0, h)
                        if r: S, S3 = B.EPS @ S.conj() @ B.EPS.T, B.EPS @ S3.conj() @ B.EPS.T
                        Yu3 = B.coupling(S3, Mu); Yu1 = B.coupling(S - S3, Mu)
                        worst["Yu_sym"] = max(worst["Yu_sym"], np.linalg.norm(Yu3 - Yu3.T) / np.linalg.norm(Yu3))
                        worst["Yu1_anti"] = max(worst["Yu1_anti"], np.linalg.norm(Yu1 + Yu1.T) / max(np.linalg.norm(Yu1), 1e-300))
                        Ye = B.coupling(S, Me); Yd_adj = B.coupling(adj(S), Md)
                        worst["Ye_adj"] = max(worst["Ye_adj"], np.linalg.norm(Ye + Yd_adj.T) / np.linalg.norm(Ye))
                        sd = np.sort(np.linalg.svd(B.coupling(S3, Md), compute_uv=False)); se = np.sort(np.linalg.svd(B.coupling(S3, Me), compute_uv=False))
                        worst["spec"] = max(worst["spec"], np.abs(se / sd - 1).max()); n += 1
    print("V3 over %d (line, tau, radius, direction, reading) cases on the 24 order-5 lines:" % n)
    for k, v in worst.items(): print("   %-9s worst relative deviation %.1e  %s" % (k, v, "PASS" if v < 1e-9 else "FAIL"))
    # V4: c = +-i
    tau = complex(0.3, 2.6); line = (F(2, 5), F(1, 10)); L = Z.radii(tau)[1]
    for d in ("DR", "F_6", "F_22"):
        h = np.array(Z.direction(d, tau))
        for c in (1j, -1j, 1.0):
            S = S_of(c * cmath.sqrt(h @ h), h); out = []
            for sec in ("up", "down", "lepton"):
                M, _ = M_of(tau, line, L, sec); s = np.sort(np.linalg.svd(B.coupling(S, M), compute_uv=False)); out.append(s[0] / s[2])
            print("V4 %s c=%s: |det S| %.1e  m1/m3 (up, down, lepton) %s" % (d, c, abs(np.linalg.det(S)), " ".join("%.1e" % x for x in out)))
