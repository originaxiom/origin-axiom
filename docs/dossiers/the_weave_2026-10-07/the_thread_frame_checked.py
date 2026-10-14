"""W84: chat1's thread frame (chat1/web-seat @ 39bfc86fe) checked on this seat's own integrator at 60 digits, and the
Lagrange law's slope read deep in the cusp along L^n R. The rule (W84_RULE.md) was committed before this script.

  V1   five threads (LR, LLRR, LLR, LLRLR, LLLR): |d ln(m2/m3)|, |d ln(m1/m3)| against chat1's banked values < 1e-5
  V2a  along L^n R, n = 1..8: the local slopes of -ln(m2/m3) against y_max vary by more than 0.3
  V2b  the last local slope of -ln(m2/m3) within 5% of 2 pi
  V2c  the last local slope of -ln(m1/m3) within 5% of 3 pi
  V2d  F+ carries weight >= 0.99 of the heaviest state at every n
  V2e  at n = 8, |K_ab| / sqrt(K_aa K_bb) < 1e-3 for every a != b
  V2f  at n = 8, N = 512 and N = 1024 agree on ln(m2/m3) and ln(m1/m3) to 1e-8
  plus the read-outs: every thread's ratios, K's eigenvalues, the states' weights, the local slopes, a fit s_inf + c / y

The forms are W72's (`the_surface_yukawa.py`: best_section, solve_twisted, G_series, to_series), evaluated at 60 digits
at each point's image in the standard fundamental domain. The integrals use the trapezoid rule over one period of the
thread's closed geodesic, with nodes at half steps. chat1's numbers are read only from its committed JSON.

Run: python3 the_thread_frame_checked.py  ->  the_thread_frame_checked.json beside it.
"""
import json
import math
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_surface_yukawa as SY  # noqa: E402

OUT = HERE / "the_thread_frame_checked.json"
CHAT1 = "39bfc86fe"
DPS = 60
L_ = ((1, 0), (1, 1))
R_ = ((1, 1), (0, 1))


def mat_mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def word_matrix(w):
    M = ((1, 0), (0, 1))
    for ch in w:
        M = mat_mul(M, L_ if ch == "L" else R_)
    return M


def reduce_tau(t):
    for _ in range(100000):
        t = t - mp.nint(t.real)
        if abs(t) < 1:
            t = -1 / t
        else:
            return t
    raise RuntimeError("no reduction")


class Forms:
    """the W72 forms as (exponent in eighths -> coefficient vector) tables, evaluated at 60 digits"""

    def __init__(self):
        mp.mp.dps = DPS
        sec = {}
        for name, u in SY.MATTER:
            terms, r, line = SY.best_section(u, Fraction(3, 2))
            sec[name] = SY.to_series(terms, SY.E8)
        terms, r, line = SY.best_section((0, 1, 0), Fraction(-1, 2))
        self.R = SY.to_series(terms, SY.E8)
        best = None
        for line in ("v+", "e_i", "v-"):
            terms, r = SY.solve_twisted(Fraction(5, 2), line)
            if best is None or r < best[1]:
                best = (terms, r, line)
        self.h_residual, self.h_line = best[1], best[2]
        self.h = SY.to_series(best[0], SY.E8P)
        self.F = [sec[n] for n, _ in SY.MATTER]
        self.pairs = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
        self.G = {p: SY.G_series(self.F[p[0]], self.F[p[1]], self.R) for p in self.pairs}
        self.tables = {}
        for key, s in [("F0", self.F[0]), ("F1", self.F[1]), ("F2", self.F[2]), ("h", self.h)] + \
                [(("G",) + p, self.G[p]) for p in self.pairs]:
            tab = {}
            for (l, n8), a in s.items():
                v = tab.setdefault(n8, [mp.mpc(0)] * 3)
                for k in range(3):
                    v[k] += a * SY.SU.B[l][k]
            self.tables[key] = tab
        self.exps = sorted({n8 for tab in self.tables.values() for n8 in tab})

    def at(self, t):
        e = {n8: mp.exp(2 * mp.pi * mp.mpc(0, 1) * mp.mpf(n8) / 8 * t) for n8 in self.exps}
        out = {}
        for key, tab in self.tables.items():
            v = [mp.mpc(0)] * 3
            for n8, c in tab.items():
                z = e[n8]
                v = [v[k] + c[k] * z for k in range(3)]
            out[key] = v
        return out


def herm(u, v):
    return sum(u[k] * mp.conj(v[k]) for k in range(3))


def cycle(forms, word, N):
    best = None
    for k in range(len(word)):
        rot = word[k:] + word[:k]
        M = word_matrix(rot)
        if best is None or abs(M[1][0]) < abs(best[1][1][0]):
            best = (rot, M)
    rot, M = best
    (a, b), (c, d) = M
    tr = a + d
    x0 = mp.mpf(a - d) / (2 * c)
    rho = mp.sqrt(tr * tr - 4) / (2 * abs(c))
    P = 2 * mp.acosh(mp.mpf(tr) / 2)
    K = [[mp.mpc(0)] * 3 for _ in range(3)]
    Y = [[mp.mpc(0)] * 3 for _ in range(3)]
    ysmax = mp.mpf(0)
    for j in range(N):
        s = -P / 2 + (j + mp.mpf(1) / 2) * P / N
        t = reduce_tau(x0 + rho * (mp.tanh(s) + mp.mpc(0, 1) / mp.cosh(s)))
        y = t.imag
        ysmax = max(ysmax, y)
        val = forms.at(t)
        y32, y52 = y ** mp.mpf(1.5), y ** mp.mpf(2.5)
        for (p, q) in forms.pairs:
            K[p][q] += herm(val["F%d" % p], val["F%d" % q]) * y32
            Y[p][q] += herm(val[("G", p, q)], val["h"]) * y52
    w = P / N
    for (p, q) in forms.pairs:
        K[p][q] *= w
        Y[p][q] *= w
        if p != q:
            K[q][p] = mp.conj(K[p][q])
            Y[q][p] = Y[p][q]
    return {"rotation": rot, "trace": tr, "period": P, "sampled y_max": ysmax, "K": K, "Y": Y}


def masses(K, Y):
    Km = mp.matrix(K)
    ev, U = mp.eighe(Km)
    D = mp.diag([1 / mp.sqrt(x) for x in ev])
    Kmh = U * D * U.H
    Yh = Kmh.T * mp.matrix(Y) * Kmh
    Us, S, Vh = mp.svd_c(Yh)
    order = sorted(range(3), key=lambda i: S[i])
    s = [S[i] for i in order]
    weights = []
    for i in order:
        v = mp.matrix([mp.conj(Vh[i, j]) for j in range(3)])
        cvec = Kmh * v
        weights.append([float(abs(cvec[j]) ** 2 * K[j][j].real) for j in range(3)])
    return {"m": s, "ln m2/m3": mp.log(s[1] / s[2]), "ln m1/m3": mp.log(s[0] / s[2]),
            "K eigenvalues": [float(x) for x in ev], "weights on (F_i, F+, F-), light to heavy": weights}


def main_():
    t0 = time.time()
    out = {"status": "W84: chat1's thread frame checked at 60 digits (the rule W84_RULE.md first; one run)"}
    forms = Forms()
    out["forms"] = {"h residual": forms.h_residual, "h line": forms.h_line, "dps": DPS}
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, check=True,
                         text=True).stdout.strip()
    banked = json.loads(subprocess.run(["git", "show", f"{CHAT1}:relays/chat1_2026-10-14_selection/thread_frame.json"],
                                       cwd=top, capture_output=True, check=True, text=True).stdout)
    per_c1 = banked["readouts"]["per thread"]
    v1 = {}
    worst = 0.0
    for w in ("LR", "LLRR", "LLR", "LLRLR", "LLLR"):
        r = cycle(forms, w, 512)
        m = masses(r["K"], r["Y"])
        d2 = abs(float(m["ln m2/m3"]) - math.log(per_c1[w]["m2/m3"]))
        d1 = abs(float(m["ln m1/m3"]) - math.log(per_c1[w]["m1/m3"]))
        worst = max(worst, d2, d1)
        v1[w] = {"m2/m3": float(mp.e ** m["ln m2/m3"]), "m1/m3": float(mp.e ** m["ln m1/m3"]),
                 "chat1 m2/m3": per_c1[w]["m2/m3"], "chat1 m1/m3": per_c1[w]["m1/m3"], "|d ln m2/m3|": d2,
                 "|d ln m1/m3|": d1}
        print(w, v1[w], round(time.time() - t0, 1), flush=True)
    out["V1"] = {"threads": v1, "worst |d ln|": worst, "holds": bool(worst < 1e-5)}
    fam = {}
    for n in range(1, 9):
        w = "L" * n + "R"
        r = cycle(forms, w, 512)
        m = masses(r["K"], r["Y"])
        K = r["K"]
        offd = max(float(abs(K[a][b]) / mp.sqrt(abs(K[a][a]) * abs(K[b][b]))) for a in range(3) for b in range(3)
                   if a != b)
        fam[n] = {"word": w, "y_max": float(mp.sqrt(n * n + 4 * n) / 2), "sampled y_max": float(r["sampled y_max"]),
                  "ln m2/m3": float(m["ln m2/m3"]), "ln m1/m3": float(m["ln m1/m3"]),
                  "K eigenvalues": m["K eigenvalues"], "weights": m["weights on (F_i, F+, F-), light to heavy"],
                  "K off-diagonal, normalised (largest)": offd}
        print(n, {k: fam[n][k] for k in ("y_max", "ln m2/m3", "ln m1/m3")}, round(time.time() - t0, 1), flush=True)
    ys = [fam[n]["y_max"] for n in range(1, 9)]
    s2 = [-(fam[n + 1]["ln m2/m3"] - fam[n]["ln m2/m3"]) / (ys[n] - ys[n - 1]) for n in range(1, 8)]
    s1 = [-(fam[n + 1]["ln m1/m3"] - fam[n]["ln m1/m3"]) / (ys[n] - ys[n - 1]) for n in range(1, 8)]
    ymid = [(ys[n] + ys[n - 1]) / 2 for n in range(1, 8)]
    r8 = cycle(forms, "L" * 8 + "R", 1024)
    m8 = masses(r8["K"], r8["Y"])
    ctl = max(abs(float(m8["ln m2/m3"]) - fam[8]["ln m2/m3"]), abs(float(m8["ln m1/m3"]) - fam[8]["ln m1/m3"]))

    def fit(sl):
        # s = s_inf + c / y over the last four local slopes
        X = [(1.0, 1.0 / ymid[i]) for i in range(3, 7)]
        a11 = sum(x[0] * x[0] for x in X); a12 = sum(x[0] * x[1] for x in X); a22 = sum(x[1] * x[1] for x in X)
        b1 = sum(x[0] * sl[i + 3] for i, x in enumerate(X)); b2 = sum(x[1] * sl[i + 3] for i, x in enumerate(X))
        det = a11 * a22 - a12 * a12
        return {"s_inf": (a22 * b1 - a12 * b2) / det, "c": (a11 * b2 - a12 * b1) / det}
    out["V2"] = {"family": fam, "local slopes of -ln m2/m3": s2, "local slopes of -ln m1/m3": s1, "y midpoints": ymid,
                 "fit m2/m3 (last four)": fit(s2), "fit m1/m3 (last four)": fit(s1),
                 "2 pi": 2 * math.pi, "3 pi": 3 * math.pi, "7 pi / 3": 7 * math.pi / 3}
    out["V2a"] = {"spread": max(s2) - min(s2), "holds": bool(max(s2) - min(s2) > 0.3)}
    out["V2b"] = {"last": s2[-1], "rel to 2 pi": abs(s2[-1] / (2 * math.pi) - 1),
                  "holds": bool(abs(s2[-1] / (2 * math.pi) - 1) < 0.05)}
    out["V2c"] = {"last": s1[-1], "rel to 3 pi": abs(s1[-1] / (3 * math.pi) - 1),
                  "holds": bool(abs(s1[-1] / (3 * math.pi) - 1) < 0.05)}
    heavy = [fam[n]["weights"][2][1] for n in range(1, 9)]
    out["V2d"] = {"F+ weight of the heaviest, by n": heavy, "holds": bool(min(heavy) >= 0.99)}
    out["V2e"] = {"largest normalised off-diagonal at n = 8": fam[8]["K off-diagonal, normalised (largest)"],
                  "holds": bool(fam[8]["K off-diagonal, normalised (largest)"] < 1e-3)}
    out["V2f"] = {"N = 1024 against 512 at n = 8": ctl, "holds": bool(ctl < 1e-8)}
    out["cells"] = {k: out[k]["holds"] for k in ("V1", "V2a", "V2b", "V2c", "V2d", "V2e", "V2f")}
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main_()
