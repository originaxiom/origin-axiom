#!/usr/bin/env python3
"""W-A3, labelled post hoc 2, written after reading main's M39 (the card's text on main) and before this run.

M39 says the up-sector question's three-body coupling is "wedged to the top degree": the degrees are exterior degrees in
Lambda*(W) (two fields in Lambda^2, the Higgs in Lambda^1, wedged into Lambda^5), not the cover's cusp degrees, which is
how the sealed script read them. This file also tests whether a class shows in the frame's lines at all.

    python3 -I -u wa3_posthoc_wedge.py

W1  for both Weil classes c = 1, 2 (rho_c(T) = diag(e(c x^2/5))): det rho_c over the whole group generated (Lambda^5 is
    det); a numerical check that alpha ^ beta ^ gamma, alpha, beta in Lambda^2, gamma in Lambda^1, picks up det rho(g)
    under g = T, S; the T-spectra of Lambda^k, k = 0..5 (5th roots or not).
W2  the trace signature r = tr R(T^2) / tr R(T)^2, which does not change if R(T) is multiplied by a scalar:
    - for rho_c (x) conj(rho_c'), c, c' in {1, 2};
    - for the frame's line representation on the 25 lines: T moves (a, b) to (a, b - a) with phase zeta^(c_T a^2), and
      c_T = 4 (down) and 1 (lepton), as computed in post hoc 1.
    Same class gives r = +1/5, mixed classes -1/5.
W3  the Weil 3's T-phases in both classes.
"""
import itertools
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {}


def say(*a):
    print(*a, flush=True)


def e(x):
    return np.exp(2j * np.pi * x)


def weil(c):
    T_ = np.diag([e(c * x * x / 5) for x in range(5)])
    S0 = np.array([[e(-2 * c * x * y / 5) for y in range(5)] for x in range(5)]) / np.sqrt(5)
    lhs = np.linalg.matrix_power(S0 @ T_, 3); rhs = S0 @ S0
    k = np.argmax(np.abs(rhs))
    S_ = (rhs.flat[k] / lhs.flat[k]) * S0
    return T_, S_


def group(gens):
    key = lambda M: tuple(np.round(M.flatten(), 8))
    G = {key(np.eye(5)): np.eye(5, dtype=complex)}
    fr = [np.eye(5, dtype=complex)]
    while fr:
        nx = []
        for M in fr:
            for g in gens:
                N = M @ g
                if key(N) not in G:
                    G[key(N)] = N; nx.append(N)
        fr = nx
    return list(G.values())


def wedge_mat(M, k):
    idx = list(itertools.combinations(range(5), k))
    out = np.zeros((len(idx), len(idx)), dtype=complex)
    for i, I in enumerate(idx):
        for j, J in enumerate(idx):
            out[i, j] = np.linalg.det(M[np.ix_(I, J)]) if k else 1
    return out, idx


def top_wedge(al, be, ga):
    # al, be: dicts {(i, j): coeff} for i < j; ga: vector; coefficient of e0^e1^e2^e3^e4
    tot = 0
    for (i, j), x in al.items():
        for (k, l), y in be.items():
            for m in range(5):
                perm = [i, j, k, l, m]
                if len(set(perm)) < 5:
                    continue
                sgn = np.linalg.det(np.eye(5)[perm])
                tot += sgn * x * y * ga[m]
    return tot


rng = np.random.default_rng(7)
OUT["W1"] = {}
for c in (1, 2):
    T_, S_ = weil(c)
    G = group([T_, S_])
    dets = [complex(np.linalg.det(g)) for g in G]
    spectra = {}
    for k in range(6):
        Wk, _ = wedge_mat(T_, k)
        ph = np.angle(np.linalg.eigvals(Wk)) / (2 * np.pi)
        spectra[k] = bool(np.max(np.abs(5 * ph - np.round(5 * ph))) < 1e-9)
    checks = []
    idx2 = list(itertools.combinations(range(5), 2))
    for g in (T_, S_):
        W2g, _ = wedge_mat(g, 2)
        for _ in range(3):
            a = rng.normal(size=10) + 1j * rng.normal(size=10)
            b = rng.normal(size=10) + 1j * rng.normal(size=10)
            cvec = rng.normal(size=5) + 1j * rng.normal(size=5)
            lhs = top_wedge(dict(zip(idx2, W2g @ a)), dict(zip(idx2, W2g @ b)), g @ cvec)
            rhs = np.linalg.det(g) * top_wedge(dict(zip(idx2, a)), dict(zip(idx2, b)), cvec)
            checks.append(abs(lhs - rhs) / abs(rhs))
    OUT["W1"][c] = {"group_order": len(G), "max_det_minus_1": float(max(abs(d - 1) for d in dets)),
                    "wedge_covariance": float(max(checks)), "fifth_root_spectra_k0_5": spectra}
    say("W1: class c = %d: group order %d; max |det rho(g) - 1| over the group = %.1e; top wedge picks up det rho(g)"
        " (worst %.1e); T-spectrum of Lambda^k in 5th roots, k = 0..5: %s" % (c, len(G), max(abs(d - 1) for d in dets),
                                                                              max(checks), spectra))

OUT["W2"] = {}
for c, cp in ((1, 1), (2, 2), (1, 2), (2, 1)):
    Tc, _ = weil(c); Tcp, _ = weil(cp)
    R = np.kron(Tc, np.conj(Tcp))
    r = np.trace(R @ R) / np.trace(R) ** 2
    OUT["W2"]["rho%d x conj rho%d" % (c, cp)] = [float(r.real), float(r.imag)]
    say("W2: rho_%d (x) conj(rho_%d): tr T^2 / (tr T)^2 = %.6f %+.1ei" % (c, cp, r.real, r.imag))
pj = json.load(open(os.path.join(HERE, "wa3_posthoc_word_output.json")))
for sec in ("down", "lep"):
    cT = pj["D_C"][sec]["T_coeff"][0]
    lines = [(a, b) for a in range(5) for b in range(5)]
    pos = {v: i for i, v in enumerate(lines)}
    R = np.zeros((25, 25), dtype=complex)
    for (a, b) in lines:
        R[pos[(a, (b - a) % 5)], pos[(a, b)]] = e(cT * a * a / 5)
    r = np.trace(R @ R) / np.trace(R) ** 2
    OUT["W2"]["frame_" + sec] = {"c_T": cT, "trT": [float(np.trace(R).real), float(np.trace(R).imag)], "ratio": [float(r.real), float(r.imag)]}
    say("W2: frame C %s lines (c_T = %d): tr R(T) = %.3f, tr R(T)^2 / (tr R(T))^2 = %.6f %+.1ei" % (sec, cT, np.trace(R).real, r.real, r.imag))

OUT["W3"] = {}
for c in (1, 2):
    ph = sorted({(c * x * x) % 5 for x in range(5)})
    OUT["W3"][c] = ph
    say("W3: class c = %d: the Weil 3's T-phases (even functions delta0, delta1+delta4, delta2+delta3) = %s / 5" % (c, ph))
with open(os.path.join(HERE, "wa3_posthoc_wedge_output.json"), "w") as fh:
    json.dump(OUT, fh, indent=1, default=str)
