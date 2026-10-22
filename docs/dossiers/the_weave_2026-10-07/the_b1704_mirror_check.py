#!/usr/bin/env python3
"""POST HOC, not a cell: a check of main's B1704 (S176, 22b7d5739), where a holding content would hold tau.

B1704 searches the minima of V = -F on Re tau = 0 and Re tau = 1/2. Its contents include the Higgs's three copies at
the line (1/2, 1/2), which B1686's copies() places at the characteristics (0, 1/2), (1/2, 0) and (0, 0). W62 (A2)
recorded that this sum is invariant only under the theta group <S, T^2>. This script asks which lines are mirror
lines of V, and where the critical points are. It uses main's own functions (B1686's S_c and E_cs, B1704's contents),
read from main's commit with git show into a temporary directory. No data.

Parts:
- A (exact): the action of each reflection on the four half-period characteristics, and whether the copies' set is
  kept. tau -> -conj(tau) (Re 0), tau -> 1 - conj(tau) (Re 1/2), tau -> 2 - conj(tau) (Re 1), tau -> 1/conj(tau) (the
  unit arc).
- B: V at mirror pairs about each line, for B1704's three contents.
- C: dV/dx at the Re 1/2 line minima B1704 lists (hold_run.txt, hold_rho_run.txt).
- D: the trivial-fermion contents: the Hessian at i, and the minima on the unit arc with the radial curvature there.
- E: the band contents: the axis minima's curvatures, and the minima on Re 1 and on the unit arc.
- F: grid minima of V inside the theta group's domain (0 <= x <= 1, |tau| >= 1, y <= 4, step 0.02, away from the arc).
- G (exact): the cusp coefficient of the copies at the theta group's second cusp, tau = 1; V along Re 1 toward it.

This seat ran parts B to F as scratch before writing this script (disclosed); the committed run reproduces them.

    python3 -B the_b1704_mirror_check.py      # writes the_b1704_mirror_check.json beside itself
"""
import cmath, contextlib, importlib.util, io, json, math, subprocess, tempfile
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MAIN = "22b7d5739"
FILES = ["frontier/B1686_w60_w62_on_main/verification/main_w62.py", "frontier/B1704_what_holds_tau/verification/hold.py"]
M_SUM = 120          # lattice cut for S_c (main's default is 60)

tmp = Path(tempfile.mkdtemp())
for f in FILES:
    p = tmp / f; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(subprocess.run(["git", "show", f"{MAIN}:{f}"], cwd=ROOT, check=True, capture_output=True, text=True).stdout)
spec = importlib.util.spec_from_file_location("hold", tmp / FILES[1]); H = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(H)
W = H.W


def V(c, t):
    tot = 0.0
    for k, w in c.items():
        if k == ("m",): tot += w * (31 / 1024) * (W.E_cs(t, 3) - W.E_cs(t, 2))
        elif k == (0.0, 0.0): tot += w * W.E_cs(t, 3)
        else: tot += w * W.S_c(t, k, M=M_SUM)
    return -tot


def content(name, key, n):
    c = dict(H.CONT[name]); c[key] = c.get(key, 0) + (-2) * n
    return c


def hess(c, t, h=0.03):
    vx = (V(c, t + h) + V(c, t - h) - 2 * V(c, t)) / h ** 2
    vy = (V(c, t + 1j * h) + V(c, t - 1j * h) - 2 * V(c, t)) / h ** 2
    return vx, vy


def grad(c, t, h=1e-3):
    return (V(c, t + h) - V(c, t - h)) / (2 * h), (V(c, t + 1j * h) - V(c, t - 1j * h)) / (2 * h)


out = {"status": "post hoc check of main's B1704, not a cell", "main commit": MAIN, "S_c lattice cut": M_SUM}
log = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); log.append(s)

# ---- A: the reflections on the characteristics (exact) ----
H4 = [(Fr(0), Fr(0)), (Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2)), (Fr(1, 2), Fr(1, 2))]
def md(p): return (p[0] % 1, p[1] % 1)
REFL = {"Re 0: tau -> -conj(tau)": lambda a, b: (a, -b),
        "Re 1/2: tau -> 1 - conj(tau)": lambda a, b: (a, a - b),
        "Re 1: tau -> 2 - conj(tau)": lambda a, b: (a, 2 * a - b),
        "unit arc: tau -> 1/conj(tau)": lambda a, b: (b, a)}
copies = sorted(md((Fr(p[0]).limit_denominator(4), Fr(p[1]).limit_denominator(4))) for p in H.cps)
A = {"copies": [[str(x) for x in p] for p in copies]}
for name, f in REFL.items():
    img = sorted(md(f(*p)) for p in copies)
    A[name] = {"map": {f"({p[0]}, {p[1]})": "(%s, %s)" % md(f(*p)) for p in H4}, "keeps the copies": img == copies}
    say("A", name, "keeps the copies:", img == copies)
out["A"] = A

# ---- B: mirror pairs ----
B = []
for name in H.CONT:
    c = H.CONT[name]
    for y in (1.0, 2.5):
        row = {"content": name, "y": y,
               "Re 0": V(c, complex(0.1, y)) - V(c, complex(-0.1, y)),
               "Re 1/2": V(c, complex(0.6, y)) - V(c, complex(0.4, y)),
               "Re 1": V(c, complex(1.1, y)) - V(c, complex(0.9, y))}
        B.append(row); say("B", name, "y", y, "V(x0+0.1)-V(x0-0.1) at Re 0, 1/2, 1: %.3g %.3g %.3g" % (row["Re 0"], row["Re 1/2"], row["Re 1"]))
    t = cmath.exp(1j * 1.2)
    row = {"content": name, "arc pair at theta 1.2, r 1.1": V(c, 1.1 * t) - V(c, t / 1.1)}
    B.append(row); say("B", name, "arc: V(1.1 e^{1.2i}) - V(e^{1.2i}/1.1) = %.3g" % row["arc pair at theta 1.2, r 1.1"])
out["B"] = B

# ---- C: the gradient at B1704's Re 1/2 line minima ----
C = []
listed = [("(a)", ("m",), 89, 3.08), ("(a)", ("m",), 92, 2.5), ("(a)", ("m",), 95, 2.14), ("(b)", ("m",), 634, 2.51),
          ("(a)", (0.0, 0.0), 3, 1.02), ("(a)", (0.0, 0.0), 7, 0.91), ("(b)", (0.0, 0.0), 15, 1.02), ("(c)", (0.0, 0.0), 17, 1.05)]
for name, key, n, y in listed:
    c = content(name, key, n); gx, gy = grad(c, complex(0.5, y)); vx, vy = hess(c, complex(0.5, y))
    C.append({"content": name, "added": str(key), "n": n, "y": y, "dV/dx": gx, "dV/dy": gy, "d2V/dx2": vx, "d2V/dy2": vy})
    say("C", name, key, n, "at 1/2 + %.2fi: dV/dx %.4g, dV/dy %.4g, d2V/dx2 %.4g" % (y, gx, gy, vx))
out["C"] = C

# ---- D, E: arc, Re 1 and axis ----
ths = np.linspace(0.30, math.pi / 2, 128)
def arc_minima(c):
    v = np.array([V(c, cmath.exp(1j * th)) for th in ths]); d = np.diff(v); res = []
    for i in [i + 1 for i in range(len(d) - 1) if d[i] < 0 <= d[i + 1]]:
        t = cmath.exp(1j * ths[i]); h = 0.02
        vr = (V(c, t * (1 + h)) + V(c, t * (1 - h)) - 2 * V(c, t)) / (h * h)
        res.append({"theta/pi": ths[i] / math.pi, "x": t.real, "y": t.imag, "V": v[i], "radial curvature": vr})
    return res, bool(v[-1] <= v.min())
yl = np.round(np.arange(0.30, 4.0001, 0.01), 3)
def line_minima(c, x0):
    v = np.array([V(c, complex(x0, y)) for y in yl]); d = np.diff(v)
    return [{"y": float(yl[i + 1]), "V": float(v[i + 1]), "d2V/dx2": hess(c, complex(x0, yl[i + 1]))[0]}
            for i in range(len(d) - 1) if d[i] < 0 <= d[i + 1]]
D = []
for name, ns in (("(a)", (3, 5, 7, 14)), ("(b)", (15, 17, 19)), ("(c)", (17, 19, 22))):
    for n in ns:
        c = content(name, (0.0, 0.0), n); vx, vy = hess(c, 1j); am, i_low = arc_minima(c)
        D.append({"content": name, "trivial Weyl fermions added": n, "at i: d2V/dx2": vx, "at i: d2V/dy2": vy,
                  "arc minima": am, "i lowest on the arc": i_low})
        say("D", name, "+%d trivial fermions: at i Vxx %.3f Vyy %.3f; arc minima %s; i lowest on the arc: %s" % (
            n, vx, vy, [(round(m["x"], 3), round(m["y"], 3), round(m["radial curvature"], 1)) for m in am], i_low))
out["D"] = D
E = []
for name, n in (("(a)", 89), ("(a)", 92), ("(a)", 95), ("(b)", 595), ("(b)", 634), ("(b)", 672), ("(c)", 735)):
    c = content(name, ("m",), n); ax = line_minima(c, 0.0); r1 = line_minima(c, 1.0); am, _ = arc_minima(c)
    for m in ax: m["d2V/dy2"] = hess(c, complex(0.0, m["y"]))[1]
    E.append({"content": name, "scalars in rho_Q added": n, "Re 0 minima": ax, "Re 1 minima": r1, "arc minima": am})
    say("E", name, "+%d rho_Q scalars: axis %s; Re 1 %s; arc %s" % (
        n, [(m["y"], round(m["V"], 2), round(m["d2V/dx2"], 3), round(m["d2V/dy2"], 2)) for m in ax],
        [(m["y"], round(m["V"], 2), round(m["d2V/dx2"], 3)) for m in r1],
        [(round(m["x"], 3), round(m["y"], 3), round(m["V"], 2)) for m in am]))
out["E"] = E

# ---- F: interior grid minima ----
xs = np.round(np.arange(-0.04, 1.0401, 0.02), 3); ys = np.round(np.arange(0.30, 4.0001, 0.02), 3)
BAS = {k: np.full((len(xs), len(ys)), np.nan) for k in ["E3", "E2", (0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]}
for i, x in enumerate(xs):
    for j, y in enumerate(ys):
        if x * x + y * y < 0.97: continue
        t = complex(x, y); BAS["E3"][i, j] = W.E_cs(t, 3); BAS["E2"][i, j] = W.E_cs(t, 2)
        for p in [(0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]: BAS[p][i, j] = W.S_c(t, p, M=M_SUM)
def Vgrid(c):
    tot = 0.0
    for k, w in c.items():
        if k == ("m",): tot = tot + w * (31 / 1024) * (BAS["E3"] - BAS["E2"])
        elif k == (0.0, 0.0): tot = tot + w * BAS["E3"]
        else: tot = tot + w * BAS[k]
    return -tot
F = []
for name, key, n in (("(a)", (0.0, 0.0), 3), ("(a)", (0.0, 0.0), 7), ("(c)", (0.0, 0.0), 17), ("(a)", ("m",), 89),
                     ("(a)", ("m",), 92), ("(a)", ("m",), 95), ("(b)", ("m",), 634)):
    v = Vgrid(content(name, key, n)); mins = []
    for i in range(1, len(xs) - 1):
        for j in range(1, len(ys) - 1):
            if not (0 <= xs[i] <= 1 and xs[i] ** 2 + ys[j] ** 2 >= 1): continue
            blk = v[i - 1:i + 2, j - 1:j + 2]
            if not np.isnan(blk).any() and v[i, j] <= blk.min(): mins.append([float(xs[i]), float(ys[j]), float(v[i, j])])
    F.append({"content": name, "added": str(key), "n": n, "grid minima (x, y, V)": mins})
    say("F", name, key, n, "grid minima:", [(a, b, round(w, 3)) for a, b, w in mins])
out["F"] = F

# ---- G: the second cusp (exact), and V along Re 1 ----
TW_INF = {(Fr(1, 2), Fr(0)), (Fr(1, 2), Fr(1, 2))}          # twisted along the cycle that shrinks at infinity (1)
TW_ONE = {p for p in H4 if (p[1] - p[0]) % 1 == Fr(1, 2)}  # at tau = 1 the shrinking cycle is (m, n) = (-1, 1)
def kap(p, tw): return Fr(-31, 16) if p in tw else Fr(2)
k_inf = 2 * sum(kap(p, TW_INF) for p in copies); k_one = 2 * sum(kap(p, TW_ONE) for p in copies)
G = {"copies' cusp coefficient at infinity": str(k_inf), "at tau = 1": str(k_one), "difference": str(k_inf - k_one), "Re 1 lines": []}
say("G copies' cusp coefficient: at infinity", k_inf, "; at tau = 1", k_one, "; difference", k_inf - k_one)
for name, key, n in (("(a)", (0.0, 0.0), 3), ("(a)", ("m",), 92), ("(b)", ("m",), 634)):
    c = content(name, key, n); row = [(y, V(c, complex(1.0, y))) for y in (1.0, 0.7, 0.5, 0.35, 0.25, 0.18)]
    G["Re 1 lines"].append({"content": name, "added": str(key), "n": n, "V(1 + iy)": row})
    say("G", name, key, n, "V on Re 1 at y = 1, .7, .5, .35, .25, .18:", [round(w, 2) for _, w in row])
out["G"] = G

(HERE / "the_b1704_mirror_check.json").write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
(HERE / "the_b1704_mirror_check_run.txt").write_text("\n".join(log) + "\n", encoding="utf-8")
