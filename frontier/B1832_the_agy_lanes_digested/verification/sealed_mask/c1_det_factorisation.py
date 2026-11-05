"""SEALED-DIGEST CHECK c1 (value-free; main's code only).
Claim (agy relay 18c607040 l.224, 'by Theorem 9'; used by Theorem 18 Part C.2): at a0 = 0,
    det Y_s = kappa (h.h) (u_1^2 + m.m) (h.m),   m = (u_j, u_i, u_k) paired with h = (h_j, h_i, h_k),
and under FR-FIB's (S~, S, S) reading h_up = conj(h_down), so (h_up.h_up)(h_down.h_down) = |h.h|^2 and the Higgs's
quadratic phase cancels from arg det(Y_u Y_d).
Main's coupling: B.coupling(S, B.weighted_M(u)), S = a0 + h_I QI + h_J QJ + h_K QK (B1691's b1656_funcs).
Prints only identity residuals and the fitted constant; no mass, no ratio of masses, no sector comparison of scales."""
import pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
B = Z.mods()["B"]
rng = np.random.default_rng(20261104)
Q = {"i": B.QI, "j": B.QJ, "k": B.QK}

def S_of(a0, h): return a0 * np.eye(2) + h["i"] * B.QI + h["j"] * B.QJ + h["k"] * B.QK
def Y(a0, h, u): return B.coupling(S_of(a0, h), B.weighted_M(u))
def cplx(n=None): return rng.normal(size=n) + 1j * rng.normal(size=n)

# (1) the factorisation at a0 = 0, random h and random channel weights u (any u: the identity is algebraic)
ratios, worst_null = [], 0.0
for _ in range(400):
    h = dict(zip("ijk", cplx(3))); u = dict(zip(["1", "i", "j", "k"], cplx(4)))
    hh = sum(h[s] ** 2 for s in "ijk"); mm = sum(u[s] ** 2 for s in "ijk"); hm = sum(h[s] * u[s] for s in "ijk")
    ratios.append(np.linalg.det(Y(0, h, u)) / (hh * (u["1"] ** 2 + mm) * hm))
ratios = np.array(ratios); kappa = ratios.mean()
print("c1.1 det Y / [(h.h)(u1^2+m.m)(h.m)] at a0=0: constant =", np.round(kappa, 12), " max rel spread =", float(np.abs(ratios - kappa).max() / abs(kappa)))
# null-vector control: h.h = 0 must give det Y = 0; h.m = 0 must give det Y = 0
for _ in range(50):
    u = dict(zip(["1", "i", "j", "k"], cplx(4)))
    hn = {"i": 1.0, "j": 1j, "k": 0.0}
    a = np.cross(np.array([u["i"], u["j"], u["k"]]), cplx(3)); hp = dict(zip("ijk", a))     # h.m = 0
    sc = np.abs(Y(0, hn, u)).max() ** 3 + 1e-300
    worst_null = max(worst_null, abs(np.linalg.det(Y(0, hn, u))) / sc, abs(np.linalg.det(Y(0, hp, u))) / (np.abs(Y(0, hp, u)).max() ** 3))
print("c1.2 control: det Y on h.h = 0 and on h.m = 0 (relative):", worst_null)
# alternative wordings fail (vacuity control): u1^2 - m.m, and (h.h)^2 without (h.m)
alt = []
for _ in range(100):
    h = dict(zip("ijk", cplx(3))); u = dict(zip(["1", "i", "j", "k"], cplx(4)))
    hh = sum(h[s] ** 2 for s in "ijk"); mm = sum(u[s] ** 2 for s in "ijk"); hm = sum(h[s] * u[s] for s in "ijk")
    alt.append(np.linalg.det(Y(0, h, u)) / (hh * (u["1"] ** 2 - mm) * hm))
alt = np.array(alt); print("c1.3 control (u1^2 - m.m wording): rel spread =", float(np.abs(alt - alt.mean()).max() / abs(alt.mean())))
# a0 != 0: no such factorisation (det picks up a0 terms)
dev = []
for _ in range(100):
    h = dict(zip("ijk", cplx(3))); u = dict(zip(["1", "i", "j", "k"], cplx(4))); a0 = complex(cplx())
    hh = sum(h[s] ** 2 for s in "ijk"); mm = sum(u[s] ** 2 for s in "ijk"); hm = sum(h[s] * u[s] for s in "ijk")
    dev.append(abs(np.linalg.det(Y(a0, h, u)) - kappa * hh * (u["1"] ** 2 + mm) * hm) / abs(np.linalg.det(Y(a0, h, u))))
print("c1.4 at a0 != 0 the a0 = 0 formula fails: min rel dev =", float(min(dev)))

# (2) the reading: S~ = eps S* eps^T has coefficients (conj a0, conj h)
worst = 0.0
for _ in range(100):
    h = dict(zip("ijk", cplx(3))); a0 = complex(cplx())
    St = B.EPS @ S_of(a0, h).conj() @ B.EPS.T
    worst = max(worst, np.abs(St - S_of(np.conj(a0), {s: np.conj(h[s]) for s in "ijk"})).max())
print("c1.5 S~ = S(conj a0, conj h):", worst)

# (3) the Higgs-phase cancellation in arg det(Y_u Y_d) under (S~, S, S) at a0 = 0, on frame points (main's M_of route)
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/recheck"))
from identities_and_order5 import M_of
worst_inv, worst_hh = 0.0, 0.0
for tau, line in ((0.25 + 1.6j, (0.4, 0.1)), (0.13 + 2.2j, (0.4, 0.3)), (0.3 + 2.6j, (1 / 3, 1 / 6))):
    L = Z.radii(tau)[0]
    Mu, _ = M_of(tau, line, L, "up"); Md, _ = M_of(tau, line, L, "down")
    for _ in range(20):
        h = cplx(3); phi = rng.uniform(0, 2 * np.pi)
        def th(hv):
            Sd = hv[0] * B.QI + hv[1] * B.QJ + hv[2] * B.QK; Su = B.EPS @ Sd.conj() @ B.EPS.T
            return np.angle(np.linalg.det(B.coupling(Su, Mu)) * np.linalg.det(B.coupling(Sd, Md)))
        d = abs((th(np.exp(1j * phi) * h) - th(h) + np.pi) % (2 * np.pi) - np.pi)
        worst_inv = max(worst_inv, d)
        hu = np.conj(h); worst_hh = max(worst_hh, abs(np.imag(np.dot(hu, hu) * np.dot(h, h))) / abs(np.dot(h, h)) ** 2)
print("c1.6 arg det(Y_u Y_d) under (S~,S,S), a0=0: invariant under h -> e^{i phi} h, worst shift (rad):", worst_inv)
print("c1.7 Im[(h_up.h_up)(h_down.h_down)] / |h.h|^2:", worst_hh)
