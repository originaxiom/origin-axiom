"""Referee B1795, r3: own implementation of the coupling (no b1656 coupling()/weighted_M()), and the algebraic structure of
det Y.  (i) test det Y = kappa * det S * det M * tr(eps S M^T) on random complex S (quaternion span) and M; (ii) the slot-swap
identity at the level of Y; (iii) det S / |S|^2 for the frame's section at the three points (pair-independent factor);
(iv) the SM sectors' sv3/sv1 at the strip on the six's carriers (B1726 compute()), against the pairs'."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, json, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
rng = np.random.default_rng(7)
# --- my own quaternion units and coupling (written from the definition, not imported)
QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
BL = [QJ, QI, QK]
def Ymine(S, M): return np.array([[np.trace(Ca.T @ EPS @ S @ Cb @ M.T) for Cb in BL] for Ca in BL])
def rc(*s): return rng.normal(size=s) + 1j * rng.normal(size=s)
ratios = []
for _ in range(200):
    s = rc(3); S = s[0] * QI + s[1] * QJ + s[2] * QK; M = rc(2, 2)
    dY = np.linalg.det(Ymine(S, M)); f = np.linalg.det(S) * np.linalg.det(M) * np.trace(EPS @ S @ M.T)
    ratios.append(dY / f)
ratios = np.array(ratios)
print("det Y / (det S det M tr(eps S M^T)) over 200 random draws: mean %s, max |dev| %.2e" % (np.round(ratios.mean(), 12), np.max(np.abs(ratios - ratios.mean()))))
# general S (not in the quaternion span)?
r2 = []
for _ in range(50):
    S = rc(2, 2); M = rc(2, 2)
    r2.append(np.linalg.det(Ymine(S, M)) / (np.linalg.det(S) * np.linalg.det(M) * np.trace(EPS @ S @ M.T)))
print("same with general 2x2 S: spread %.2e" % (np.ptp(np.abs(r2))))
# slot swap: Y(S, M^T) vs Y(S, M): singular values equal?
d = 0.0
for _ in range(100):
    s = rc(3); S = s[0] * QI + s[1] * QJ + s[2] * QK; M = rc(2, 2)
    a, b = np.linalg.svd(Ymine(S, M), compute_uv=False), np.linalg.svd(Ymine(S, M.T), compute_uv=False)
    d = max(d, np.max(np.abs(a - b)) / a[0])
print("random S (quaternion span), M: max rel sv difference Y(S,M) vs Y(S,M^T): %.2e" % d)
# with the S~ reading
d = 0.0
for _ in range(100):
    s = rc(3); S = s[0] * QI + s[1] * QJ + s[2] * QK; St = EPS @ np.conj(S) @ EPS.T; M = rc(2, 2)
    a, b = np.linalg.svd(Ymine(St, M), compute_uv=False), np.linalg.svd(Ymine(St, M.T), compute_uv=False)
    d = max(d, np.max(np.abs(a - b)) / a[0])
print("random S~: max rel sv difference Y(S~,M) vs Y(S~,M^T): %.2e" % d)
# --- the frame's section at the three points (imports the repo's theta constants for S only)
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
for pk, (x, y) in SP.POINTS.items():
    H = SP.higgs(complex(x, y))
    for rn, S in H.items():
        print("point %-5s reading %-2s |det S|/(|S|_F^2/2) = %.3e   (S entries %s)" % (pk, rn, abs(np.linalg.det(S)) / (np.linalg.norm(S) ** 2 / 2), np.round(S.ravel(), 4)))
# --- SM sectors at the strip on the carriers (B1726 compute(), sv2/sv1, sv3/sv1)
c1726 = SP._modules()["c1726"]
CARR = [(Fr(2, 5), Fr(k, 60)) for k in (7, 29, 41, 47, 49, 55)]
for a, b in CARR:
    out = c1726.compute(SP.STRIP[0], SP.STRIP[1], a, b)
    print("strip (%s, %s): SM sv3/sv1 min over h,rn: up %.1e down %.1e lep %.1e" % (a, b, *[min(out["%s|%s|%s" % (sec, h, rn)][1] for h in ("L_max", "L_2") for rn in ("S", "St")) for sec in ("up", "down", "lep")]))
