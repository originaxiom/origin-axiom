"""Referee B1799, check 1(b): B1736's channel form Y = u h^T + h u^T - (u.h)1 + u1[h]_x + h0(u1 1 + [u]_x) against
b1656_funcs.coupling() with this code's conventions (BLOCKS = [QJ, QI, QK], so the generation order is (j, i, k), not
B1736's unit order (i, j, k)); then the symmetry claim: h0 = 0 for S and S~, u1 = 0 for equal twists; and an independent
route: M = sum u_s E^s is symmetric iff u1 = 0, and for traceless S, coupling(S, M) is symmetric iff M is.
Read-only; imports B1723's b1656_funcs and B1795's split.py."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
sys.path.insert(0, str(ROOT / "frontier/B1723_the_golden_valley/verification")); _a = sys.argv; sys.argv = ["x"]
import b1656_funcs as B
sys.argv = _a
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
rng = np.random.default_rng(7102)
Q = {"1": np.eye(2, dtype=complex), "i": B.QI, "j": B.QJ, "k": B.QK}


def hvec(S):  # S = h0 1 + h_i i + h_j j + h_k k ; Q_s^2 = -1 for s in i, j, k
    return S.trace() / 2, np.array([-np.trace(Q[s] @ S) / 2 for s in "ijk"])


def uvec(M):  # by duality sum(EC_t * E^s) = delta
    return {s: np.sum(B.EC[s] * M) for s in B.UNITS}


def cross(v): return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


def formula(h0, h, u1, u, sgn):
    return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3) + sgn * u1 * cross(h) + h0 * (u1 * np.eye(3) + sgn * cross(u))


P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])   # (i, j, k) -> (j, i, k)
best = {}
for order in ("ijk", "jik"):
    for sgn in (1, -1):
        err = 0.0
        for _ in range(50):
            S = sum((rng.normal() + 1j * rng.normal()) * Q[s] for s in Q)
            uu = {s: rng.normal() + 1j * rng.normal() for s in B.UNITS}
            M = B.weighted_M(uu); Y = B.coupling(S, M)
            h0, h = hvec(S); ud = uvec(M); u = np.array([ud[s] for s in "ijk"])
            F = formula(h0, h, ud["1"], u, sgn)
            if order == "jik": F = P @ F @ P.T
            err = max(err, np.linalg.norm(Y - F) / np.linalg.norm(Y))
        best[(order, sgn)] = err
for k, v in best.items(): print("B1736 form, generation order %s, sign of the cross terms %+d: max rel err %.2e" % (k[0], k[1], v))
# the dual basis: which E^s carry an antisymmetric (eps) part?
for s in B.UNITS:
    E = B.EDUAL[s]; print("E^%s: |E - E^T| = %.3e" % (s, np.linalg.norm(E - E.T)))
# independent route: traceless S and symmetric M give symmetric Y
e1 = e2 = 0.0
for _ in range(50):
    S = sum((rng.normal() + 1j * rng.normal()) * Q[s] for s in "ijk")
    uu = {s: rng.normal() + 1j * rng.normal() for s in B.UNITS}; uu0 = dict(uu, **{"1": 0})
    Y0 = B.coupling(S, B.weighted_M(uu0)); e1 = max(e1, np.linalg.norm(Y0 - Y0.T) / np.linalg.norm(Y0))
    S1 = S + (rng.normal() + 1j * rng.normal()) * np.eye(2)          # a partner with a '1' component
    Y1 = B.coupling(S1, B.weighted_M(uu0)); e2 = max(e2, np.linalg.norm(Y1 - Y1.T) / np.linalg.norm(Y1))
print("u1 = 0, traceless S: max |Y - Y^T|/|Y| %.2e;  u1 = 0 but h0 != 0: min-over-draws of max asym %.2e (not symmetric)" % (e1, e2))
# the frame's S and S~ at the three points: h0
for pk, (re_t, im_t) in SP.POINTS.items():
    t = complex(re_t, im_t); H = SP.higgs(t)
    for rn, Sx in H.items():
        h0, h = hvec(Sx); print("point %s reading %s: |h0|/|h| = %.2e, det S = %.3e" % (pk, rn, abs(h0) / np.linalg.norm(h), abs(np.linalg.det(Sx))))
# actual rows: u1 on LL and nucnuc, and the B1736 form reproduces coupling() there
t = complex(0.37, 2.2); Ls = SP.Ls_at(2.2); H = SP.higgs(t)
for (a, b) in ((Fr(2, 5), Fr(49, 60)), (Fr(1, 7), Fr(3, 7)), (Fr(1, 4), Fr(0))):
    w = float(a) * t + float(b)
    for nm, (ql, qr) in (("LL", (-3, -3)), ("nucnuc", (0, 0)), ("Lnuc", (-3, 0))):
        x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
        L = Ls["L_max"]; u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u); Y = B.coupling(H["S"], Mw)
        un = math.sqrt(sum(abs(u[s]) ** 2 for s in B.UNITS))
        print("line (%s, %s) %-6s |u1|/|u| %.1e  |M - M^T|/|M| %.1e  |Y - Y^T|/|Y| %.1e" % (a, b, nm, abs(u["1"]) / un, np.linalg.norm(Mw - Mw.T) / np.linalg.norm(Mw), np.linalg.norm(Y - Y.T) / np.linalg.norm(Y)))
print("r2 exit 0")
