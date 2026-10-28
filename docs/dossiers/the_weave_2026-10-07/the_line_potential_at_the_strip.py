#!/usr/bin/env python3
"""W167 — the plan's stage 2, is the line's condition forced? (the rule: W167_RULE.md, committed and pushed before this
script).  The one-loop potential of the hypercharge line w = a tau + b on the shared fibre, from the frame's own fields
on W59's joint-parity kernel at s = 3, minimised over the torus at W158's 38 strip rows; B1761's points ranked among
the census's 266 lines; the boson weight varied; a census over contents by linear programming.  No target is read.

  L0  the kernel: N = 48 against N = 64, evenness, the frame's T-law V(psi1, psi2; tau) = V(psi1, psi2 + psi1; tau + 1)
  L1  the global minimum at a = 0 at every row, none on B1761's set
  L2  B1761's 20 points above the 10th percentile of V over the 266 lines at every row
  L3  the minimum stays at a = 0 with the bosons' weight times 2, 5, 10
  R   read-outs; the census over contents

    python3 -B docs/dossiers/the_weave_2026-10-07/the_line_potential_at_the_strip.py
"""
import contextlib
import io
import json
import math
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_one_loop_potential_on_the_fibre as W59     # noqa: E402  (W59: the joint-parity kernel)
    import the_third_opinion_b1726 as T8                    # noqa: E402  (the census's 266 lines)

DOS = "docs/dossiers/the_weave_2026-10-07/"
ROWS_FROM = {"B1749": DOS + "third_opinion_b1749.json", "B1753": DOS + "third_opinion_b1753.json"}
OUT = HERE / "the_line_potential_at_the_strip.json"
N = 48
G = 192
# the frame's own fields: (name, 6Y charge, complex components over three generations, sigma: +1 boson, -1 fermion)
FIELDS = (("Q", 1, 18, -1), ("u", -4, 9, -1), ("d", 2, 9, -1), ("L", -3, 6, -1), ("e", 6, 3, -1),
          ("H_u", -3, 2, 1), ("H_d", 3, 2, 1))
QS = (1, 2, 3, 4, 6)
B1761 = [(Fr(i, 5), Fr(j, 10)) for i in (1, 2, 3, 4) for j in (1, 3, 5, 7, 9)]


def psi_of(a, b):
    """main's line (a, b), w = a tau + b: the character e^{2 pi i (n b - m a)}, so psi = (-a, b)"""
    return (-float(a), float(b))
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


class Kernel:
    """W59's Joint at sign +1 (a boson): k(psi) = -Sum cw cos 2 pi (m psi1 + n psi2); a fermion is -k"""

    def __init__(self, t, n=N):
        J = W59.Joint(t, 1, n)
        self.m, self.n, self.cw = J.m.astype(float), J.n.astype(float), J.cw

    def value(self, ps):
        return float(-np.sum(self.cw * np.cos(2 * np.pi * (self.m * ps[0] + self.n * ps[1]))))

    def grad(self, ps):
        s = np.sin(2 * np.pi * (self.m * ps[0] + self.n * ps[1])) * self.cw * 2 * np.pi
        return np.array([np.sum(s * self.m), np.sum(s * self.n)])

    def hess(self, ps):
        c = np.cos(2 * np.pi * (self.m * ps[0] + self.n * ps[1])) * self.cw * (2 * np.pi) ** 2
        return np.array([[np.sum(c * self.m * self.m), np.sum(c * self.m * self.n)],
                         [np.sum(c * self.m * self.n), np.sum(c * self.n * self.n)]])

    def grid(self, q, g=G):
        """k(q psi) on the g x g grid psi = (i/g, j/g), exactly, by cos(A + B) = cos A cos B - sin A sin B"""
        x = np.arange(g) / g
        A = 2 * np.pi * q * np.outer(self.m, x)
        B = 2 * np.pi * q * np.outer(self.n, x)
        cw = self.cw[:, None]
        return -((np.cos(A) * cw).T @ np.cos(B) - (np.sin(A) * cw).T @ np.sin(B))


class Content:
    """V(psi) = Sum_f n_f sigma_f k(q_f psi), with the bosons' weight times beta"""

    def __init__(self, K, beta=1.0, weights=None):
        self.K = K
        if weights is None:
            self.terms = [(q, n * s * (beta if s > 0 else 1.0)) for (_nm, q, n, s) in FIELDS]
        else:
            self.terms = [(q, c) for q, c in weights.items()]

    def value(self, ps):
        return sum(c * self.K.value(q * np.asarray(ps)) for q, c in self.terms)

    def grad(self, ps):
        return sum(c * q * self.K.grad(q * np.asarray(ps)) for q, c in self.terms)

    def hess(self, ps):
        return sum(c * q * q * self.K.hess(q * np.asarray(ps)) for q, c in self.terms)

    def grid(self, cache):
        return sum(c * cache[abs(q)] for q, c in self.terms)


def tdist(p, r):
    return max(abs(((a - b) + 0.5) % 1.0 - 0.5) for a, b in zip(p, r))


def global_min(V, grid_vals, g=G):
    """the grid's ten lowest local minima (periodic), each refined by Newton; the least converged point"""
    Z = grid_vals
    loc = np.ones_like(Z, dtype=bool)
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di or dj:
                loc &= Z <= np.roll(np.roll(Z, di, 0), dj, 1)
    idx = np.argwhere(loc)
    idx = idx[np.argsort(Z[loc])][:10]
    best = None
    for i, j in idx:
        p = np.array([i / g, j / g])
        for _ in range(80):
            gr = V.grad(p)
            if np.linalg.norm(gr) < 1e-11:
                break
            try:
                step = np.linalg.solve(V.hess(p), gr)
            except np.linalg.LinAlgError:
                break
            if np.linalg.norm(step) > 0.5 / g:
                step *= 0.5 / g / np.linalg.norm(step)
            p = p - step
        p = p % 1.0
        v = V.value(p)
        ev = np.linalg.eigvalsh(V.hess(p))
        rec = {"psi": [float(p[0]), float(p[1])], "value": v, "gradient norm": float(np.linalg.norm(V.grad(p))),
               "hessian eigenvalues": [float(e) for e in ev]}
        if best is None or v < best["value"]:
            best = rec
    best["grid least"] = float(Z.min())
    return best


def a_is_zero(psi):
    return abs(((psi[0]) + 0.5) % 1.0 - 0.5) < 1e-6


def on_b1761(psi):
    return any(tdist(psi, psi_of(a, b)) < 1e-6 or tdist(psi, tuple(-x for x in psi_of(a, b))) < 1e-6
               for a, b in B1761)


def rows_from_outputs(root):
    rows = []
    for name, path in ROWS_FROM.items():
        d = json.loads(T8.git_bytes(root, "HEAD", path).decode("utf-8"))
        for r in d["C1"]["rows"]:
            rows.append({"name": name, "line": r["line"], "x": r["Re_tau"], "y": r["Im_tau"]})
    return rows


def census(K, cache, psi_star, excl=0.02, g=96):
    """max t with Sum_q c_q [k(q psi_j) - k(q psi*)] >= t off the 0.02 neighbourhoods of +-psi*, c_q in [-1, 1]"""
    step = G // g
    pts = [(i * step, j * step) for i in range(g) for j in range(g)]
    keep = [(i, j) for (i, j) in pts if tdist((i / G, j / G), psi_star) > excl
            and tdist((i / G, j / G), (-psi_star[0], -psi_star[1])) > excl]
    ks = np.array([K.value(q * np.asarray(psi_star)) for q in QS])
    D = np.array([[cache[q][i, j] - ks[n] for n, q in enumerate(QS)] for (i, j) in keep])
    # variables (c_1..c_5, t); maximise t:  -D c + t <= 0
    A = np.hstack([-D, np.ones((len(D), 1))])
    res = linprog(c=[0] * len(QS) + [-1], A_ub=A, b_ub=np.zeros(len(D)),
                  bounds=[(-1, 1)] * len(QS) + [(None, None)], method="highs")
    if res.status != 0:
        return {"status": int(res.status), "message": res.message}
    c = res.x[:len(QS)]
    return {"t*": float(res.x[-1]), "c": {str(q): float(v) for q, v in zip(QS, c)},
            "signs (boson +, fermion -)": {str(q): int(np.sign(round(v, 9))) for q, v in zip(QS, c)},
            "grid points": len(D)}


def run(root, out):
    rows = rows_from_outputs(root)
    out["rows"] = len(rows)
    L = T8.own_lines()
    out["census lines"] = len(L)
    # ---------------------------------------------------------------- L0
    rng = np.random.default_rng(167)
    l0 = {"N48 vs N64 worst relative": 0.0, "minimum shift N48 vs N64": 0.0, "evenness worst": 0.0,
          "T-law worst": 0.0}
    for r in rows[:3]:
        t = complex(r["x"], r["y"])
        K48, K64, KT = Kernel(t, 48), Kernel(t, 64), Kernel(t + 1, 48)
        V48, V64, VT = Content(K48), Content(K64), Content(KT)
        for _ in range(10):
            p = rng.random(2)
            v = V48.value(p)
            l0["N48 vs N64 worst relative"] = max(l0["N48 vs N64 worst relative"], abs(V64.value(p) / v - 1))
            l0["evenness worst"] = max(l0["evenness worst"], abs(V48.value(-p) - v) / abs(v))
            l0["T-law worst"] = max(l0["T-law worst"], abs(VT.value([p[0], p[1] + p[0]]) - v) / abs(v))
        c48 = {q: K48.grid(q) for q in QS}
        c64 = {q: K64.grid(q) for q in QS}
        m48, m64 = global_min(V48, V48.grid(c48)), global_min(V64, V64.grid(c64))
        l0["minimum shift N48 vs N64"] = max(l0["minimum shift N48 vs N64"], tdist(m48["psi"], m64["psi"]))
    out["L0"] = l0
    # ---------------------------------------------------------------- L1, L2, L3, R per row
    per_row = []
    for r in rows:
        t = complex(r["x"], r["y"])
        K = Kernel(t)
        cache = {q: K.grid(q) for q in QS}
        V = Content(K)
        mn = global_min(V, V.grid(cache))
        vals = np.array([V.value(psi_of(a, b)) for (a, b) in L])
        p10 = float(np.percentile(vals, 10))
        b61 = [V.value(psi_of(a, b)) for (a, b) in B1761]
        two5 = [V.value(psi_of(a, b)) for (a, b) in B1761 if a in (Fr(2, 5), Fr(3, 5))]
        rec = {"row": [r["name"], r["line"], r["x"], r["y"]], "minimum": mn, "a = 0": a_is_zero(mn["psi"]),
               "on B1761's set": on_b1761(mn["psi"]), "266 lines: 10th percentile": p10,
               "266 lines: least": float(vals.min()), "266 lines: least line":
               [str(q) for q in L[int(np.argmin(vals))]],
               "B1761's least": float(min(b61)), "B1761's all above the 10th percentile": bool(min(b61) > p10),
               "B1761's least rank among the 266": int(np.sum(vals < min(b61))),
               "the 2/5 class's best above the minimum": float(min(two5) - mn["value"])}
        betas = {}
        for beta in (2, 5, 10, 20, 50):
            Vb = Content(K, beta=beta)
            mb = global_min(Vb, Vb.grid(cache))
            betas[str(beta)] = {"psi": mb["psi"], "a = 0": a_is_zero(mb["psi"]), "on B1761's set":
                                on_b1761(mb["psi"])}
        rec["boson weight"] = betas
        rec["census over contents at (2/5, 1/10)"] = census(K, cache, psi_of(Fr(2, 5), Fr(1, 10)))
        per_row.append(rec)
    out["per row"] = per_row
    l1 = all(p["a = 0"] and not p["on B1761's set"] for p in per_row)
    l2 = all(p["B1761's all above the 10th percentile"] for p in per_row)
    l3 = all(p["boson weight"][b]["a = 0"] for p in per_row for b in ("2", "5", "10"))
    first = None
    for b in ("2", "5", "10", "20", "50"):
        if any(not p["boson weight"][b]["a = 0"] for p in per_row):
            first = int(b)
            break
    ts = [p["census over contents at (2/5, 1/10)"].get("t*") for p in per_row]
    out["R"] = {"the least boson multiplier at which a != 0 wins somewhere (up to 50)": first,
                "census: rows with t* > 0": sum(1 for x in ts if x is not None and x > 1e-9),
                "census: t* range": [min(x for x in ts if x is not None), max(x for x in ts if x is not None)]
                if any(x is not None for x in ts) else None,
                "minima's distinct (a, b), rounded": sorted({(round(p["minimum"]["psi"][0], 6),
                                                              round(p["minimum"]["psi"][1], 6)) for p in per_row})}
    out["cells"] = {
        "L0": bool(l0["N48 vs N64 worst relative"] < 1e-6 and l0["minimum shift N48 vs N64"] < 1e-6
                   and l0["evenness worst"] < 1e-12 and l0["T-law worst"] < 1e-6),
        "L1": bool(l1), "L2": bool(l2), "L3": bool(l3)}


def main():
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W167", "rule": "W167_RULE.md", "status": "one run", "head": T8.resolve(root, "HEAD"),
           "python": sys.version.split()[0], "numpy": np.__version__, "machine": platform.machine()}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            run(root, out)
        except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
            out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["warnings"] = sorted({sanitize(f"{w.category.__name__}: {w.message}") for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out.get("cells"), indent=1))
    if "run_failed" in out:
        print("run failed")


if __name__ == "__main__":
    main()
