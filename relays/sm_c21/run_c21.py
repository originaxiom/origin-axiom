#!/usr/bin/env python3
"""SM-C21: frame D1's cusp mixing with the tick-fixed Higgs vacuum v+- (card relays/cards/SM_C21_the-d1-cusp-mixing-at-
the-ticks-higgs.md, pushed before this run).  Main's cim_closed.py (Y, Y_mp) and level6_higgs.py (U_M) imported
unchanged; main's gate-5 contraction M = Y(xi) . v.  Frame-internal structure only; nothing set beside data.
    python3 run_c21.py MAIN_CHECKOUT"""
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
DELTA = {"up": 5, "down": -1, "lep": -9}
P5 = [(Fr(a, 5), Fr(b, 5)) for a in range(5) for b in range(5) if gcd(gcd(a, b), 5) == 1]
LIFTS = ((0, 0), (1, 0), (0, 1), (1, 1))

ev, V = np.linalg.eig(L6.UM); ph = np.angle(ev) / np.pi
VP = V[:, np.argmin(abs(ph - 1 / 6))]; VM = V[:, np.argmin(abs(ph + 1 / 6))]
VP, VM = VP / np.linalg.norm(VP), VM / np.linalg.norm(VM)


def tensor(tau, xi, mp=False):
    if not mp:
        return CC.Y(tau, xi)
    d = CC.Y_mp(tau, xi, dps=60); T = np.zeros((3, 3, 6), complex)
    for (i, j, k), v in d.items():
        T[i, j, k] = complex(v)
    return T


def mats(tau, a, b, v, mp=False):
    w = float(a) * tau + float(b)
    return {s: np.einsum("ijk,k->ij", tensor(tau, D * w / 2, mp), v) for s, D in DELTA.items()}


def svd_desc(M):
    U, s, Vh = np.linalg.svd(M)
    return U, s


def classify(Mu, Md):
    Uu, su = svd_desc(Mu); Ud, sd = svd_desc(Md)
    ru = int((su > su[0] * 1e-12).sum()); rd = int((sd > sd[0] * 1e-12).sum())
    Vm = np.abs(Uu.conj().T @ Ud)             # rows: up, cols: down, ordered by descending singular value
    v33 = Vm[0, 0]                           # the top directions
    if v33 > 0.99 and min(Vm[i, i] for i in range(3)) > 0.9:
        c = "aligned"
    elif v33 > 0.99:
        c = "top-aligned"
    elif all(Vm[i].max() > 0.99 for i in range(3)):
        c = "permutation"
    else:
        c = "other"
    return c, ru, rd, float(v33)


def main():
    out = {"v+ . v- (should be 0)": float(abs(np.vdot(VP, VM)))}
    for hy, mp in ((4, False), (8, True)):
        tau = complex(0.13, hy)
        for vn, v in (("v+", VP), ("v-", VM)):
            for lift in LIFTS:
                cnt, ranks, v33s = {}, set(), []
                for a, b in P5:
                    M = mats(tau, a + lift[0], b + lift[1], v, mp)
                    c, ru, rd, v33 = classify(M["up"], M["down"])
                    cnt[c] = cnt.get(c, 0) + 1; ranks.add((ru, rd)); v33s.append(v33)
                key = "height %d, %s, lift %s" % (hy, vn, lift)
                out[key] = {"classes": cnt, "ranks (up, down)": sorted(ranks), "|V33| min/max": [min(v33s), max(v33s)]}
                print(key, cnt, sorted(ranks), "|V33| %.3f..%.3f" % (min(v33s), max(v33s)), flush=True)
    # K3, K4: exponents at the mark, heights 6, 8, 10 (extended precision)
    a, b = Fr(2, 5), Fr(4, 5)
    ex = {}
    for vn, v in (("v+", VP), ("v-", VM)):
        logs = {}
        for hy in (6, 8, 10):
            M = mats(complex(0.13, hy), a, b, v, True)
            for s in DELTA:
                sv = np.linalg.svd(M[s], compute_uv=False)
                logs.setdefault(s, []).append([math.log(sv[1] / sv[0]) if sv[1] > 0 else float("nan"),
                                               math.log(sv[2] / sv[0]) if sv[2] > 0 else float("nan")])
        for s in DELTA:
            L = np.array(logs[s])
            E = [-(L[2, r] - L[1, r]) / (2 * math.pi) for r in (0, 1)]          # slope over heights 8 -> 10
            Eprev = [-(L[1, r] - L[0, r]) / (2 * math.pi) for r in (0, 1)]
            rat = []
            for e in E:
                f = Fr(e).limit_denominator(10) if e == e else None
                rat.append([str(f), abs(e - float(f)) if f is not None else None])
            ex["%s %s" % (vn, s)] = {"E(s2/s1), E(s3/s1) 8->10": E, "6->8": Eprev, "nearest p/q (q<=10), distance": rat}
    out["exponents at the mark"] = ex
    (HERE / "c21_results.json").write_text(json.dumps(out, indent=1, default=str))
    print(json.dumps(ex, indent=1))


if __name__ == "__main__":
    main()
