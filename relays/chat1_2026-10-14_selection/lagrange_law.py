"""The Lagrange law (PREREGISTRATION_LAGRANGE_LAW.md, sealed at 3887230a7, sha256 91bfe0f8...).

In the thread frame (thread_frame.py's construction, copied verbatim below: the SM seat's W72 forms at 87cf7f551,
B1644's coupling, cycle integrals at the image in the fundamental domain), every Lyndon word of length 2..8.
Admission: y_max <= 3.0 and both ratios agree between N = 256 and N = 384 to 1e-5 relative.

  Q0  the 12 old threads reproduce thread_frame.json's ratios to 1e-6
  LL1 Spearman(y_max, ln m2/m3) < -0.9 over all admitted threads
  LL2 the sealed fit 7.1069 - 7.2941 y predicts ln m2/m3 on the new admitted threads with RMS < 1.0
  LL3 the golden root LR has the largest m2/m3 of all admitted threads
  LL4 admitted y < 1.5 => m2/m3 > 0.01; admitted y > 2 => m2/m3 < 1e-3
  LL5 the sealed fit 5.9196 - 8.1172 y predicts ln m1/m3 on the new admitted threads with RMS < 1.5

Run once:  python3 -B lagrange_law.py > lagrange_law_run.txt 2>&1    (writes lagrange_law.json beside itself)
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
out = {"sm_seat_commit": SMC, "status": "the Lagrange law (sealed 3887230a7; one run)"}
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


# ---- threads (verbatim from thread_frame.py)

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



mir = lambda w: w.translate(str.maketrans("LR", "RL"))
canon = lambda w: min(w[k:] + w[:k] for k in range(len(w)))

words = [w for w in lyndon(8) if len(w) >= 2]
old = json.loads((HERE / "thread_frame.json").read_text())["readouts"]["per thread"]
thr = json.loads((HERE.parent / "chat1_2026-10-14_the_scale" / "t_root_threads.json").read_text())
rows = {}
for w in words:
    r256, r384 = thread_integrals(w, 256), thread_integrals(w, 384)
    m256, m384 = masses(r256["K"], r256["Y"]), masses(r384["K"], r384["Y"])
    agree = max(abs(m256[k] - m384[k]) / abs(m384[k]) for k in ("m2/m3", "m1/m3"))
    heavy = m384["weights on (F_i, F+, F-) per state (light to heavy)"][2]
    syl = sum(1 for i in range(len(w)) if w[i] != w[i - 1])
    rows[w] = {"length": len(w), "y_max": r384["y_max"], "m2/m3": m384["m2/m3"], "m1/m3": m384["m1/m3"],
               "N256 vs N384 worst relative": agree, "heaviest state's weights (F_i, F+, F-)": heavy,
               "Vol": thr[w][0], "CS": thr[w][1], "syllables": syl, "K condition": float(m384["K eigenvalues"][2] / m384["K eigenvalues"][0]),
               "admitted": bool(r384["y_max"] <= 3.0 and agree <= 1e-5)}
    print(f"{w:9s} y {r384['y_max']:.4f} m2/m3 {m384['m2/m3']:.4e} m1/m3 {m384['m1/m3']:.4e} agree {agree:.1e} adm {rows[w]['admitted']}", file=sys.stderr, flush=True)
adm = [w for w in words if rows[w]["admitted"]]
new = [w for w in adm if len(w) >= 6]
q0 = max(abs(rows[w][k] - old[w][k]) / old[w][k] for w in old for k in ("m2/m3", "m1/m3"))
out["Q0"] = {"old threads reproduced, worst relative": q0, "holds": bool(q0 < 1e-6)}
y = np.array([rows[w]["y_max"] for w in adm]); l2 = np.log([rows[w]["m2/m3"] for w in adm]); l1 = np.log([rows[w]["m1/m3"] for w in adm])
rho = float(spearmanr(y, l2).correlation)
out["LL1"] = {"Spearman": rho, "n admitted": len(adm), "holds": bool(rho < -0.9)}
yn = np.array([rows[w]["y_max"] for w in new]); l2n = np.log([rows[w]["m2/m3"] for w in new]); l1n = np.log([rows[w]["m1/m3"] for w in new])
rms2 = float(np.sqrt(np.mean((l2n - (7.1069 - 7.2941 * yn)) ** 2))) if len(new) else float("nan")
out["LL2"] = {"RMS residual (new admitted)": rms2, "n new admitted": len(new), "holds": bool(len(new) > 0 and rms2 < 1.0)}
top = max(adm, key=lambda w: rows[w]["m2/m3"])
out["LL3"] = {"largest m2/m3": top, "value": rows[top]["m2/m3"], "holds": bool(top == "LR")}
low = [w for w in adm if rows[w]["y_max"] < 1.5]; high = [w for w in adm if rows[w]["y_max"] > 2.0]
ok4 = all(rows[w]["m2/m3"] > 0.01 for w in low) and all(rows[w]["m2/m3"] < 1e-3 for w in high)
out["LL4"] = {"Markov threads (y < 1.5)": {w: [rows[w]["y_max"], rows[w]["m2/m3"]] for w in low},
              "violations": [w for w in low if rows[w]["m2/m3"] <= 0.01] + [w for w in high if rows[w]["m2/m3"] >= 1e-3],
              "n high": len(high), "holds": bool(ok4)}
rms1 = float(np.sqrt(np.mean((l1n - (5.9196 - 8.1172 * yn)) ** 2))) if len(new) else float("nan")
out["LL5"] = {"RMS residual (new admitted)": rms1, "holds": bool(len(new) > 0 and rms1 < 1.5)}
A = np.vstack([np.ones_like(y), y]).T
c2 = np.linalg.lstsq(A, l2, rcond=None)[0]; c1 = np.linalg.lstsq(A, l1, rcond=None)[0]
res2 = l2 - A @ c2
feat = {"length": [rows[w]["length"] for w in adm], "syllables": [rows[w]["syllables"] for w in adm],
        "|CS|": [abs(rows[w]["CS"]) for w in adm], "amphichiral": [int(abs(rows[w]["CS"]) < 1e-6) for w in adm],
        "Vol": [rows[w]["Vol"] for w in adm]}
corr = {k: float(spearmanr(v, res2).correlation) for k, v in feat.items()}
eq = []
for i, a in enumerate(adm):
    for b in adm[i + 1:]:
        if abs(rows[a]["y_max"] - rows[b]["y_max"]) < 1e-6 and canon(mir(a)) != b:
            eq.append([a, b, rows[a]["y_max"], rows[a]["m2/m3"], rows[b]["m2/m3"]])
out["readouts"] = {"per thread": rows, "fit all admitted: ln m2/m3": c2.tolist(), "fit all admitted: ln m1/m3": c1.tolist(),
                   "RMS of the all-admitted fit (m2/m3)": float(np.sqrt(np.mean(res2 ** 2))),
                   "residual correlations (Spearman)": corr, "equal-height pairs (not mirrors)": eq,
                   "excluded": [w for w in words if not rows[w]["admitted"]], "seconds": round(time.time() - t0, 1)}
out["cells"] = {k: out[k]["holds"] for k in ("Q0", "LL1", "LL2", "LL3", "LL4", "LL5")}
(HERE / "lagrange_law.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
print(json.dumps({k: out[k] for k in ("Q0", "LL1", "LL2", "LL3", "LL4", "LL5")}, indent=1, default=str))
print("fit all admitted:", c2.tolist(), c1.tolist(), "rms", out["readouts"]["RMS of the all-admitted fit (m2/m3)"])
print("residual correlations", corr); print("equal-height pairs", eq); print("excluded", out["readouts"]["excluded"])
print(json.dumps(out["cells"], indent=1)); print("seconds", out["readouts"]["seconds"])
