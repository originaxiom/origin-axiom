#!/usr/bin/env python3
"""The thread frame (PREREGISTRATION_THREAD_FRAME.md, sealed at 0cf01ff11, sha256 71aa2bcd...).

In the vacuum thread W, tau runs over W's closed geodesic; the four-dimensional couplings are cycle integrals of the SM
seat's surface-frame integrands (its W72 forms, built by its own modules at 87cf7f551, read-only):
  K_ab = int <F_a, F_b> y^{3/2} ds,  Y_ab = int <G_ab, h> y^{5/2} ds,  K_h = int <h, h> y^{5/2} ds,
  G_ab = (R.F_b) F_a + (R.F_a) F_b - (F_a.F_b) R   (B1644's coupling: a.G_ab = F_a^T Y(a; R) F_b),
masses = singular values of (K^-1/2)^T Y K^-1/2. Threads: Lyndon words of length 2..5 in L = [[1,0],[1,1]],
R = [[1,1],[0,1]]. Each invariant integrand is evaluated at the point's image in the standard fundamental domain.

  Q0  controls: h's first coefficients = W72's; invariance f(tau) = f(gamma tau) (relative, floored at 1e-12 of the
      largest of the 13 values at that point; fixed before the run); trapezoid N = 96 vs 192
  TF1 the root's rank 3, K positive definite      TF2 the root hierarchical: m2/m3 < 0.2 and m1/m2 < 0.2
  TF3 the root's lightest mostly F+               TF4 mirror pairs equal      TF5 Spearman(y_max, log m1/m3) < -0.5

Run once:  python3 -B thread_frame.py > thread_frame_run.txt 2>&1    (writes thread_frame.json beside itself)
"""
import io, json, math, os, pathlib, subprocess, sys, tarfile, tempfile, time
from fractions import Fraction
import numpy as np
import mpmath as mp
from scipy.stats import spearmanr

t0 = time.time()
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
SMC = "87cf7f55111ec1f4019f302ffaa578376a9143e6"
TMP = pathlib.Path(tempfile.mkdtemp(prefix="thread_frame_sm_"))
blob = subprocess.run(["git", "-C", str(REPO), "archive", SMC, "docs/dossiers/the_weave_2026-10-07", "frontier"],
                      check=True, capture_output=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP, filter="data")
DOSS = TMP / "docs" / "dossiers" / "the_weave_2026-10-07"
sys.path.insert(0, str(DOSS))
os.chdir(DOSS)
import the_surface_yukawa as SY  # noqa: E402  (W72: sections, G, h, np_eval)
SU = SY.SU
mp.mp.dps = 40
out = {"sm_seat_commit": SMC, "status": "the thread frame (sealed 0cf01ff11; one run)"}
print("modules loaded", round(time.time() - t0, 1), file=sys.stderr, flush=True)

# ------------------------------------------------------------------ the forms (W72's construction, unchanged)
sec = {}
for name, u in SY.MATTER:
    terms, r, line = SY.best_section(u, Fraction(3, 2)); sec[name] = SY.to_series(terms, SY.E8)
terms, r, line = SY.best_section((0, 1, 0), Fraction(-1, 2)); sec["R"] = SY.to_series(terms, SY.E8)
hbest = None
for line in ("v+", "e_i", "v-"):
    terms, r = SY.solve_twisted(Fraction(5, 2), line)
    if hbest is None or r < hbest[1]: hbest = (terms, r, line)
hs = SY.to_series(hbest[0], SY.E8P)
F = [sec[n] for n, _ in SY.MATTER]
PAIRS = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
G = {p: SY.G_series(F[p[0]], F[p[1]], sec["R"]) for p in PAIRS}
Fnp = [SY.np_eval(s) for s in F]
Gnp = {p: SY.np_eval(G[p]) for p in PAIRS}
hnp = SY.np_eval(hs)
print("forms built", round(time.time() - t0, 1), file=sys.stderr, flush=True)

banked = json.loads((DOSS / "the_surface_yukawa.json").read_text())
bh = banked["read-outs"]["h's first coefficients"]
mine = {f"{l}:{Fraction(n8, 8)}": complex(a) for (l, n8), a in hs.items() if n8 < 24}
q0a = max(abs(complex(*bh[k]) - mine[k]) for k in bh)


def integrands(T):
    """the 13 invariant scalars at the points T (array of complex tau): K (6), Y (6), Kh"""
    y = T.imag
    Fv = [f(T) for f in Fnp]
    hv = hnp(T)
    res = {}
    for a, b in PAIRS:
        res[("K", a, b)] = np.sum(Fv[a] * np.conj(Fv[b]), axis=1) * y ** 1.5
        res[("Y", a, b)] = np.sum(Gnp[(a, b)](T) * np.conj(hv), axis=1) * y ** 2.5
    res[("Kh",)] = np.sum(np.abs(hv) ** 2, axis=1) * y ** 2.5
    return res


def reduce(t):
    for _ in range(10000):
        t = t - round(t.real)
        if abs(t) < 1 - 1e-14:
            t = -1 / t
        else:
            return t
    raise RuntimeError("reduction did not terminate")


# ------------------------------------------------------------------ Q0(b): invariance
rng = np.random.default_rng(20261014)
S_ = np.array([[0, -1], [1, 0]]); T_ = np.array([[1, 1], [0, 1]]); Ti = np.array([[1, -1], [0, 1]])
GAMMAS = [S_, T_ @ S_, S_ @ T_, Ti @ S_, S_ @ Ti, T_ @ S_ @ T_]
mob = lambda g, t: (g[0, 0] * t + g[0, 1]) / (g[1, 0] * t + g[1, 1])
inv_worst, ntests = 0.0, 0
while ntests < 20:
    t = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.8, 1.2))
    g = GAMMAS[rng.integers(len(GAMMAS))]
    tg = mob(g, t)
    if tg.imag < 0.75 or t.imag < 0.75:
        continue
    A, B = integrands(np.array([t])), integrands(np.array([tg]))
    floor = 1e-12 * max(abs(A[k][0]) for k in A)          # relative, floored at 1e-12 of the largest value there
    for k in A:
        inv_worst = max(inv_worst, float(abs(A[k][0] - B[k][0]) / max(abs(A[k][0]), abs(B[k][0]), floor)))
    ntests += 1

# ------------------------------------------------------------------ threads
L = np.array([[1, 0], [1, 1]]); R = np.array([[1, 1], [0, 1]])


def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()


def matrix(word):
    M = np.eye(2, dtype=np.int64)
    for ch in word:
        M = M @ (L if ch == "L" else R)
    return M


def thread_integrals(word, N):
    best = None
    for k in range(len(word)):
        rot = word[k:] + word[:k]; M = matrix(rot)
        if best is None or abs(M[1, 0]) < abs(best[1][1, 0]): best = (rot, M)
    rot, M = best
    a, b, c, d = (int(x) for x in M.flatten()); tr = a + d
    x0 = (a - d) / (2 * c); rho = math.sqrt(tr * tr - 4) / (2 * abs(c)); P = 2 * math.acosh(tr / 2)
    s = -P / 2 + P * np.arange(N) / N
    T = x0 + rho * (np.tanh(s) + 1j / np.cosh(s))
    Tr = np.array([reduce(t) for t in T])
    vals = integrands(Tr)
    w = P / N
    K = np.zeros((3, 3), dtype=complex); Y = np.zeros((3, 3), dtype=complex)
    for a_, b_ in PAIRS:
        K[a_, b_] = w * np.sum(vals[("K", a_, b_)]); K[b_, a_] = np.conj(K[a_, b_])
        Y[a_, b_] = Y[b_, a_] = w * np.sum(vals[("Y", a_, b_)])
    Kh = float(np.real(w * np.sum(vals[("Kh",)])))
    return {"rotation": rot, "M": M.tolist(), "trace": tr, "period": P, "y_max": float(np.max(Tr.imag)),
            "K": K, "Y": Y, "Kh": Kh}


def masses(K, Y):
    ev, U = np.linalg.eigh(K)
    Kmh = U @ np.diag(ev ** -0.5) @ U.conj().T
    Yh = Kmh.T @ Y @ Kmh
    Uu, s, Vh = np.linalg.svd(Yh)
    order = np.argsort(s)
    s = s[order]; V = Vh.conj().T[:, order]
    comps = []
    for k in range(3):
        c = Kmh @ V[:, k]
        comps.append([float(abs(c[j]) ** 2 * K[j, j].real) for j in range(3)])
    return {"m": s.tolist(), "m2/m3": float(s[1] / s[2]), "m1/m3": float(s[0] / s[2]), "m1/m2": float(s[0] / s[1]),
            "K eigenvalues": ev.tolist(), "weights on (F_i, F+, F-) per state (light to heavy)": comps}


words = [w for w in lyndon(5) if len(w) >= 2]
res96 = {w: thread_integrals(w, 96) for w in words}
res192 = {w: thread_integrals(w, 192) for w in words}
conv = max(max(float(np.max(np.abs(res96[w][X] - res192[w][X])) / np.max(np.abs(res192[w][X]))) for X in ("K", "Y"))
           for w in words)
print("threads integrated", round(time.time() - t0, 1), file=sys.stderr, flush=True)
out["Q0"] = {"h first coefficients vs W72 (max abs dev)": q0a, "invariance worst relative": inv_worst,
             "invariance tests": ntests, "trapezoid N=96 vs 192 worst relative": conv,
             "holds": bool(q0a < 1e-25 and inv_worst < 1e-9 and conv < 1e-9)}

per = {}
for w in words:
    r = res192[w]
    mm = masses(r["K"], r["Y"])
    per[w] = {k: r[k] for k in ("rotation", "M", "trace", "period", "y_max")}
    per[w].update(mm)
    per[w]["K"] = [[[z.real, z.imag] for z in row] for row in r["K"]]
    per[w]["Y"] = [[[z.real, z.imag] for z in row] for row in r["Y"]]
    per[w]["Kh"] = r["Kh"]
root = per["LR"]
Kroot = res192["LR"]["K"]
out["TF1"] = {"m1/m3": root["m1/m3"], "K eigenvalues": root["K eigenvalues"],
              "holds": bool(root["m1/m3"] > 1e-8 and min(root["K eigenvalues"]) > 0)}
out["TF2"] = {"m2/m3": root["m2/m3"], "m1/m2": root["m1/m2"], "m1/m3": root["m1/m3"],
              "holds": bool(root["m2/m3"] < 0.2 and root["m1/m2"] < 0.2)}
wF = root["weights on (F_i, F+, F-) per state (light to heavy)"][0][1]
out["TF3"] = {"lightest state's weight on F+": wF, "holds": bool(wF > 0.9)}
mir = lambda w: w.translate(str.maketrans("LR", "RL"))
canon = lambda w: min(w[k:] + w[:k] for k in range(len(w)))
pairs, tf4 = [], 0.0
for w in words:
    m = canon(mir(w))
    if m != w and m in per and (m, w) not in pairs:
        pairs.append((w, m))
        tf4 = max(tf4, abs(per[w]["m2/m3"] - per[m]["m2/m3"]) / per[w]["m2/m3"],
                  abs(per[w]["m1/m3"] - per[m]["m1/m3"]) / per[w]["m1/m3"])
out["TF4"] = {"mirror pairs": pairs, "worst relative difference": tf4, "holds": bool(tf4 < 1e-8)}
ymax = [per[w]["y_max"] for w in words]; l13 = [math.log(per[w]["m1/m3"]) for w in words]
rho_s = float(spearmanr(ymax, l13).correlation)
out["TF5"] = {"Spearman(y_max, log m1/m3)": rho_s, "holds": bool(rho_s < -0.5)}

# ------------------------------------------------------------------ read-outs
Yb = np.array([[complex(*z) for z in row] for row in banked["X4"]["Y (Y0 = 2.0)"]])
hend = masses(np.diag([1.0, 2.0, 2.0]).astype(complex), Yb)
hybrid = masses(Kroot, Yb)
hz = json.loads((DOSS / "received" / "HZ2021_running_masses_MZ.json").read_text())["masses_GeV"]["value"]
data = {"up": (hz["u"] / hz["t"], hz["c"] / hz["t"]), "down": (hz["d"] / hz["b"], hz["s"] / hz["b"]),
        "lepton": (hz["e"] / hz["tau"], hz["mu"] / hz["tau"])}
dl = {sec_: {"log(m2/m3 / datum)": math.log(root["m2/m3"] / d21), "log(m1/m3 / datum)": math.log(root["m1/m3"] / d31)}
      for sec_, (d31, d21) in data.items()}
scal = {w: {"log|q| at y_max": -2 * math.pi * per[w]["y_max"], "log m2/m3": math.log(per[w]["m2/m3"]),
            "log m1/m3": math.log(per[w]["m1/m3"])} for w in words}
out["readouts"] = {"per thread": per, "H-end control (W73's 0.01938, 3.87e-4)": {k: hend[k] for k in ("m2/m3", "m1/m3")},
                   "hybrid: W72's Y with the root's K": hybrid, "data line (root vs HZ2021 at M_Z)": dl,
                   "data": data, "scaling": scal, "seconds": round(time.time() - t0, 1)}
out["cells"] = {k: out[k]["holds"] for k in ("Q0", "TF1", "TF2", "TF3", "TF4", "TF5")}
(HERE / "thread_frame.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
print(json.dumps({k: out[k] for k in ("Q0", "TF1", "TF2", "TF3", "TF4", "TF5")}, indent=1, default=str))
print("H-end control", out["readouts"]["H-end control (W73's 0.01938, 3.87e-4)"])
print("hybrid", {k: hybrid[k] for k in ("m2/m3", "m1/m3")})
for w in words:
    p = per[w]
    print(f"{w:6s} y_max {p['y_max']:.4f}  m2/m3 {p['m2/m3']:.4e}  m1/m3 {p['m1/m3']:.4e}  lightest on F+ "
          f"{p['weights on (F_i, F+, F-) per state (light to heavy)'][0][1]:.3f}")
print("data line", json.dumps(dl, indent=1))
print(json.dumps(out["cells"], indent=1)); print("seconds", out["readouts"]["seconds"])
