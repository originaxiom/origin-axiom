#!/usr/bin/env python3
"""HELD instrument for DESIGN_FOR_REVIEW.md (main reviews before any seal). It builds the frame's modules at the weave's
spin vacuum on a state's own presentation (sm:B1538's route-P presentation of the degree-one cover, as W7 used) and
reads their structure. It does not read a count on the design's population.

What it runs:
  control()    the count path itself, on a banked reading outside the population: sm:B1530's m135 = -LLRR members at
               the fibre characters (0, 1/2) and (1/2, 0), which read (I(W1), I(L2 W1)) = (-1, -1), with the
               hyperbolic module (sm:B1549's module_P), at a generic interior class (sm:B1549's count_of);
  structure()  the spin modules (a) lambda_p (x) (rho_Q + rho_Q) and (b) lambda_p (x) rho_Q + conj(lambda_p) (x) rho_Q on
               the twelve odd-trace states at tick 3: h0, h1, r1, n at every kappa in mu_8, to compare with W10.
The lift of the common point to the tick's stable letter is found from the tick's own relators (an element of 2O).

    python3 instrument.py control
    python3 instrument.py structure
"""
import json
import random
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
DOSSIER = HERE.parent
sys.path.insert(0, str(DOSSIER))
import the_parity_sectors as S  # noqa: E402  (the states, the resolving tick, the banked libraries at raised precision)
import the_common_point as CP  # noqa: E402

T = S.T
PC = S.PC
M = 8                                     # kappa in mu_8 (the doublet's eigenvalues are eighth roots of unity)
PARITY = {(1, 0): "(1/2, 0)", (0, 1): "(0, 1/2)", (1, 1): "(1/2, 1/2)"}
Q2 = {"1": np.eye(2, dtype=complex), "i": np.array([[1j, 0], [0, -1j]]),
      "j": np.array([[0, 1], [-1, 0]], dtype=complex), "k": np.array([[0, 1j], [1j, 0]])}


def qmat(q):
    w, x, y, z = q
    return w * Q2["1"] + x * Q2["i"] + y * Q2["j"] + z * Q2["k"]


def tick_state(sw):
    w = sw[1:]
    k = S.resolving_tick(w)
    sign = sw[0] if k % 2 else "+"
    return k, sign + w * k


def word_matrix(word, gens):
    X = np.eye(2, dtype=complex)
    for c in word:
        X = X @ (gens[c] if c.islower() else np.linalg.inv(gens[c.lower()]))
    return X


def lifts(swk):
    """the elements g of 2O with rho_Q(a) = i, rho_Q(b) = j, rho_Q(t) = g a representation of the tick's group"""
    st = PC.State(swk)
    out = []
    for g in CP.TWO_O.values():
        gens = {"a": Q2["i"], "b": Q2["j"], "t": qmat(g)}
        if all(np.allclose(word_matrix(r, gens), np.eye(2), atol=1e-9) for r in st.G.rels):
            out.append(g)
    return out


def exact(x):
    """the entries of 2O's elements are 0, +-1/2, +-1/sqrt 2, +-1: rebuilt at mpmath precision"""
    for v in (0, 0.5, 1):
        if abs(abs(x) - v) < 1e-9:
            return mp.mpf(v) * (1 if x >= 0 else -1)
    assert abs(abs(x) - 2 ** -0.5) < 1e-9, x
    return mp.sqrt(2) / 2 * (1 if x >= 0 else -1)


def qmat_mp(q):
    w, x, y, z = (exact(v) for v in q)
    return mp.matrix([[w + 1j * x, y + 1j * z], [-y + 1j * z, w - 1j * x]])


QMP = {"i": mp.matrix([[1j, 0], [0, -1j]]), "j": mp.matrix([[0, 1], [-1, 0]])}


def spin_module(Pr, p, kappa_exp, g, variant):
    """the four on each presentation generator, exact at mpmath precision:
    (a) lambda (x) (rho + rho); (b) lambda rho + conj(lambda) rho"""
    G = qmat_mp(g)
    assert mp.norm(G * QMP["i"] * G ** -1 - G * QMP["i"] * G ** -1) == 0
    gens = {"a": QMP["i"], "b": QMP["j"], "t": G}
    kap = mp.expjpi(mp.mpf(2 * kappa_exp) / M)
    chi = {"a": mp.mpf((-1) ** p[0]), "b": mp.mpf((-1) ** p[1]), "t": kap}
    mats = []
    for (_, _, word) in Pr.gens:
        R = mp.eye(2)
        lam = mp.mpc(1)
        for c in word:
            R = R * (gens[c] if c.islower() else gens[c.lower()] ** -1)
            lam *= chi[c] if c.islower() else 1 / chi[c.lower()]
        lam2 = lam if variant == "a" else mp.conj(lam)
        A = [[mp.mpc(0)] * 4 for _ in range(4)]
        for i in range(2):
            for j in range(2):
                A[i][j] = lam * R[i, j]
                A[2 + i][2 + j] = lam2 * R[i, j]
        mats.append(A)
    return mats


def control():
    out = []
    swk = "-LLRR"
    C = PC.Cover(PC.State(swk), (1, 0, 1), 0)
    for ez in ((0, 6), (6, 0)):
        r = T.read_P(swk, C, ez, 6, 12, rngs=[random.Random(1530)])
        out.append({"state": swk, "fibre character (twelfths)": list(ez), "kappa (twelfths)": 6,
                    "structure": r["structure"], "count at a generic interior class": r["draws"][0]["count"]})
    return out


def structure():
    out = []
    for sw in S.states():
        k, swk = tick_state(sw)
        if k != 3:
            continue
        C = PC.Cover(PC.State(swk), (1, 0, 1), 0)
        Pr, P = T.presentation_P(C)
        row = {"state": sw, "the tick's state": swk, "lifts": []}
        for g in lifts(swk):
            per = {}
            for p, name in PARITY.items():
                for variant in ("a", "b"):
                    hits = []
                    for e in range(M):
                        s = T.cohom(T.Mod(spin_module(Pr, p, e, g, variant)), P)
                        if s["h1"]:
                            hits.append({"kappa (eighths)": e, "h0": s["h0"], "h1": s["h1"], "r1": s["r1"], "n": s["n"]})
                    per[f"{name} ({variant})"] = hits
            row["lifts"].append({"g": [round(v, 6) for v in g], "readings": per})
        out.append(row)
        print(sw, json.dumps(row["lifts"][0]["readings"])[:400], flush=True)
    return out


if __name__ == "__main__":
    what = sys.argv[1]
    res = control() if what == "control" else structure()
    with open(HERE / f"instrument_{what}.json", "w") as f:
        json.dump(res, f, indent=1, default=str)
    if what == "control":
        print(json.dumps(res, default=str))
