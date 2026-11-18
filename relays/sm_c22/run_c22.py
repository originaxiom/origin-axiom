#!/usr/bin/env python3
"""SM-C22: every Higgs vector in frame D1 (card relays/cards/SM_C22_every-higgs-vector-in-d1.md, pushed before this run).
Main's cim_closed.py and level6_higgs.py imported unchanged.  Frame-internal; nothing set beside data.
    python3 run_c22.py MAIN_CHECKOUT"""
import importlib.util
import json
import math
import pathlib
import sys
from fractions import Fraction as Fr
from math import gcd

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
CHK = pathlib.Path(sys.argv[1]).resolve() / "frontier/B1957_the_seats_claims_register/verification/checks"
sys.path.insert(0, str(CHK))


def load(name):
    spec = importlib.util.spec_from_file_location(name, CHK / (name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


CC = load("cim_closed"); L6 = load("level6_higgs")
Z3, X3, UM = L6.Z3, L6.X3, L6.UM
P5 = [(Fr(a, 5), Fr(b, 5)) for a in range(5) for b in range(5) if gcd(gcd(a, b), 5) == 1]
MARK = P5.index((Fr(2, 5), Fr(4, 5)))


def Ymp(tau, xi):
    d = CC.Y_mp(tau, xi, dps=60); T = np.zeros((3, 3, 6), complex)
    for (i, j, k), v in d.items():
        T[i, j, k] = complex(v)
    return T


def phase_defect(A, B):
    i = np.unravel_index(np.argmax(abs(B)), B.shape); ph = A[i] / B[i]
    return float(np.abs(A - ph * B).max() / np.abs(B).max())


def main():
    out = {"T1 ||Z3 X3 + X3 Z3||": float(np.abs(Z3 @ X3 + X3 @ Z3).max())}
    # T1 numerically: least defect over random v (double precision, moderate height)
    rng = np.random.default_rng(22)
    tau = 0.13 + 1.2j; w = 0.4 * tau + 0.8
    Yd0, Yd1, Ydt = CC.Y(tau, -0.5 * w), CC.Y(tau, -0.5 * (w + 1)), CC.Y(tau, -0.5 * (w + tau))
    best = 9.0
    for _ in range(2000):
        v = rng.normal(size=6) + 1j * rng.normal(size=6); v /= np.linalg.norm(v)
        M0 = np.einsum("ijk,k->ij", Yd0, v)
        dfc = max(phase_defect(np.einsum("ijk,k->ij", Yd1, v), M0), phase_defect(np.einsum("ijk,k->ij", Ydt, v), M0))
        best = min(best, dfc)
    out["T1 least defect over 2000 random v (down sector)"] = best
    # the tensors once
    T = {}
    for hy in (8, 10):
        tau = complex(0.13, hy)
        for idx, (a, b) in enumerate(P5):
            wv = float(a) * tau + float(b)
            T[(hy, idx, "up")] = Ymp(tau, 2.5 * wv)
            T[(hy, idx, "down")] = Ymp(tau, -0.5 * wv)
        print("tensors at height", hy, flush=True)
    # the vectors
    vecs = {}
    for k in range(6):
        e = np.zeros(6, complex); e[k] = 1; vecs["mode %d" % k] = e
    ev, V = np.linalg.eig(UM)
    for n in range(6):
        vecs["U_M eigvec phase %.3f pi" % (np.angle(ev[n]) / np.pi)] = V[:, n] / np.linalg.norm(V[:, n])
    for k in range(3):
        for s in (1, -1):
            e = np.zeros(6, complex); e[k] = 1; e[k + 3] = s; vecs["e%d %s e%d" % (k, "+" if s > 0 else "-", k + 3)] = e / np.sqrt(2)
    for n in range(5000):
        v = rng.normal(size=6) + 1j * rng.normal(size=6); vecs["random %d" % n] = v / np.linalg.norm(v)

    def stats(v):
        top = 0; E3 = []; Emark = None
        for idx in range(24):
            Mu = {hy: np.einsum("ijk,k->ij", T[(hy, idx, "up")], v) for hy in (8, 10)}
            Md = {hy: np.einsum("ijk,k->ij", T[(hy, idx, "down")], v) for hy in (8, 10)}
            Uu = np.linalg.svd(Mu[10])[0]; Ud = np.linalg.svd(Md[10])[0]
            if abs(np.vdot(Uu[:, 0], Ud[:, 0])) > 0.99:
                top += 1
            s8 = np.linalg.svd(Md[8], compute_uv=False); s10 = np.linalg.svd(Md[10], compute_uv=False)
            e = lambda s, r: math.log(max(s[r] / s[0], 1e-300))
            E = [-(e(s10, r) - e(s8, r)) / (2 * math.pi) for r in (1, 2)]
            E3.append(E[1])
            if idx == MARK:
                Emark = E
        return top / 24, float(np.median(E3)), Emark

    rows = {}
    for name, v in vecs.items():
        rows[name] = stats(v)
    both = {k: r for k, r in rows.items() if r[0] >= 0.5 and r[1] >= 0.1}
    named = {k: r for k, r in rows.items() if not k.startswith("random")}
    rnd = np.array([r[:2] for k, r in rows.items() if k.startswith("random")])
    out["named vectors (top-aligned share, median E(s3/s1) down, E at the mark)"] = named
    out["random: max top-aligned share"] = float(rnd[:, 0].max())
    out["random: max median E(s3/s1)"] = float(rnd[:, 1].max())
    out["random: max median E among those with top-aligned share >= 0.5"] = float(rnd[rnd[:, 0] >= 0.5][:, 1].max()) if (rnd[:, 0] >= 0.5).any() else None
    out["random: max top-aligned share among those with median E >= 0.1"] = float(rnd[rnd[:, 1] >= 0.1][:, 0].max()) if (rnd[:, 1] >= 0.1).any() else None
    out["S1 vectors with both"] = {k: r for k, r in both.items()}
    out["S1 count with both"] = len(both)
    (HERE / "c22_results.json").write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps({k: v for k, v in out.items() if k != "named vectors (top-aligned share, median E(s3/s1) down, E at the mark)"}, indent=1, default=str))
    for k, r in named.items():
        print("%-28s top-aligned %.2f  median E3 %.3f  mark E %s" % (k, r[0], r[1], [round(x, 3) for x in r[2]]))


if __name__ == "__main__":
    main()
