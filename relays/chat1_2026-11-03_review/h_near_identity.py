"""The web seat's check for its review of B1825 (a robustness check of the sealed run's own read address, on its own
targets; not a test, and no new measured value is read).

B1825's least-chi2_ten address (line (3/8, 3/8), tau = 0.093359375 + 2.742578125i, direction DR, radius L_2, reading
S~ S~ S; run.json) is computed at the generations' metric H = I, which B1822 shows the flat structure does not force
(8 real parameters per field). How far must H depart from I before chi2_ten falls below the sealed 23.21?
Y' = P_L Y P_R with P = exp(K), K hermitian traceless, so H = P^-2 up to transposition and conjugation (the same family).
Targets and sigma: B1825's referee output node_scan.json (t10, sigma), with c = 3 as B1825 applies it.

(a) the chi2_ten at the address reproduced; (b) a diagonal metric on the quark doublet alone: the corner ratio
|V_ub|/|V_td|; (c) chi2_ten minimised with the metrics' norm budget ||K|| <= r (BFGS, a penalty for the budget, seeded;
a local search at one address), on the quark fields (Q, u, d) and on all five, reported with the largest condition
number of H over the fields.

Usage: python3 h_near_identity.py <main checkout>   (main at e1e3c6c2f)
"""
import contextlib
import io
import json
import math
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]

NS = json.loads((ROOT / "frontier" / "B1825_step_b_the_nine_from_one_address" / "verification" / "referee" / "node_scan.json").read_text())
t10 = np.array(NS["t10"]); sig = np.array(NS["sigma"])
tt = t10.copy(); tt[4] -= math.log(3); tt[5] += math.log(3)

tau = complex(0.093359375, 2.742578125); line = (Fr(3, 8), Fr(3, 8)); reading = (1, 1, 0)
with contextlib.redirect_stdout(io.StringIO()):
    L = Z.radii(tau)[1]
    a = Z.direction("DR", tau)
    Y = {}
    for (sn, ql, qr), r in zip(Z.SECTORS, reading):
        w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
        R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
        Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
        if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T
        u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
        Y[sn] = B.coupling(Sm, B.weighted_M(u))


def outputs(Yu, Yd, Ye):
    f = []; U = {}
    for sn, M in (("up", Yu), ("down", Yd), ("lepton", Ye)):
        u_, s, _ = np.linalg.svd(M); o = np.argsort(s); s = s[o]; U[sn] = u_[:, o]
        f += [s[1] / s[2], s[0] / s[2]]
    V = U["up"].conj().T @ U["down"]
    J = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
    f += [abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), abs(J)]
    return np.log(np.array(f)), np.abs(V)


def chi2(f):
    z = (f - tt) / sig; return float(z @ z)


f0, V0 = outputs(Y["up"], Y["down"], Y["lepton"])
print("(a) chi2_ten at the address, H = I: %.4f (B1825's fresh value 291.4867); |V_ub|/|V_td| = %.3f" % (chi2(f0), V0[0, 2] / V0[2, 0]))

print("(b) a diagonal metric on the quark doublet (P_Q = diag(d)), up and down together:")
for d in ([2, 1, 0.5], [0.3, 1, 3], [5, 1, 0.2]):
    P = np.diag(d).astype(complex); _, V = outputs(P @ Y["up"], P @ Y["down"], Y["lepton"])
    print("    P_Q = diag%s: |V_ub|/|V_td| = %.3f" % (tuple(d), V[0, 2] / V[2, 0]))

G = []
for i in range(3):
    for j in range(i + 1, 3):
        E = np.zeros((3, 3), complex); E[i, j] = E[j, i] = 1; G.append(E)
        E = np.zeros((3, 3), complex); E[i, j] = -1j; E[j, i] = 1j; G.append(E)
G.append(np.diag([1, -1, 0]).astype(complex)); G.append(np.diag([1, 1, -2]).astype(complex) / math.sqrt(3))


def P_of(k): return expm(sum(ki * g for ki, g in zip(k, G)))


def build(k, nf):
    Ks = [k[8 * i: 8 * i + 8] for i in range(nf)]
    PQ, Pu, Pd = (P_of(v) for v in Ks[:3])
    PL, Pe = (P_of(Ks[3]), P_of(Ks[4])) if nf == 5 else (np.eye(3), np.eye(3))
    return outputs(PQ @ Y["up"] @ Pu, PQ @ Y["down"] @ Pd, PL @ Y["lepton"] @ Pe)


def cond_H(k, nf): return max(np.linalg.cond(P_of(k[8 * i: 8 * i + 8])) ** 2 for i in range(nf))


print("(c) chi2_ten minimised under a norm budget on the metrics (fields: 3 = Q, u, d; 5 = Q, u, d, L, e)")
print("    fields  budget  chi2_ten  cond(H)max  |V_ub|/|V_td|")
for nf in (3, 5):
    rng = np.random.default_rng(1103); best = None
    for r in (0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5):
        cands = []
        for trial in range(5):
            k0 = (best[1] if best is not None else np.zeros(8 * nf)) + rng.normal(0, 0.02, 8 * nf)
            fun = lambda k: chi2(build(k, nf)[0]) + 1e4 * max(0.0, np.linalg.norm(k) - r) ** 2
            m = minimize(fun, k0, method="BFGS", options={"maxiter": 500, "gtol": 1e-7})
            k = m.x
            if np.linalg.norm(k) > r: k = k * r / np.linalg.norm(k)
            cands.append((chi2(build(k, nf)[0]), k))
        cands.sort(key=lambda t: t[0]); best = cands[0]
        _, V = build(best[1], nf)
        print("    %d       %4.2f    %8.2f  %9.1f   %6.3f" % (nf, r, best[0], cond_H(best[1], nf), V[0, 2] / V[2, 0]), flush=True)
