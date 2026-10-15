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
REPO = pathlib.Path("/home/claude/origin-axiom")
SMC = "87cf7f55111ec1f4019f302ffaa578376a9143e6"
TMP = pathlib.Path(tempfile.mkdtemp(prefix="audit_sm_", dir="/tmp/claude-0/-home-claude-origin-axiom/6cd20217-7806-5dd6-9098-8054245c567d/scratchpad/audit_D"))
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




# ---------------- AUDIT (scratch only): the sealed fit on Lyndon words of length 9..12
def masses_inv(K, Y):
    ev, U = np.linalg.eigh(K)
    if not np.all(np.isfinite(ev)) or ev.min() <= 0: return None
    A = U @ np.diag(ev ** -0.5) @ U.conj().T
    try:
        s = np.sort(np.linalg.svd(A @ Y @ A.T, compute_uv=False))
    except np.linalg.LinAlgError:
        return None
    return s
ctrl = {}
for w in ("LR", "LLRLRLR", "LLRR"):
    r = thread_integrals(w, 384); s = masses_inv(r["K"], r["Y"]); ctrl[w] = [s[1] / s[2], s[0] / s[2]]
rows = {}
for w in (w for w in lyndon(12) if 9 <= len(w) <= 12):
    r256, r384 = thread_integrals(w, 256), thread_integrals(w, 384)
    s256, s384 = masses_inv(r256["K"], r256["Y"]), masses_inv(r384["K"], r384["Y"])
    if s256 is None or s384 is None:
        rows[w] = {"len": len(w), "y": r384["y_max"], "adm": False, "note": "K not positive definite or SVD failed"}
        continue
    rat = lambda s: (s[1] / s[2], s[0] / s[2])
    a, b = rat(s256), rat(s384)
    agree = max(abs(a[i] - b[i]) / abs(b[i]) for i in (0, 1))
    rows[w] = {"len": len(w), "y": r384["y_max"], "m23": b[0], "m13": b[1], "agree": agree,
               "adm": bool(r384["y_max"] <= 3.0 and agree <= 1e-5)}
json.dump({"control": ctrl, "rows": rows}, open("/tmp/claude-0/-home-claude-origin-axiom/6cd20217-7806-5dd6-9098-8054245c567d/scratchpad/audit_D/len9_12.json", "w"), indent=0)
print("done", round(time.time() - t0, 1), file=sys.stderr, flush=True)
