"""POST HOC (labelled), after the referee and before the relay: is CP in the thread frame word reversal? Setup copied
verbatim from post_hoc_long_words.py (itself lagrange_law.py's, sealed at 3887230a7): the SM seat's W72 forms at
87cf7f551, B1644's coupling, cycle integrals at the image in the fundamental domain, N = 256 and 384.

The reading under test (THE_SELECTION_PRINCIPLE.md section 4, by hand): the modular surface's reflection tau -> -conj(tau)
carries a thread's geodesic onto its reversed word's, so if the forms' coefficients are real up to fixed phases, the
couplings of W and of reverse(W) are complex conjugates, and a word that is its own reverse has real couplings.
No prediction is scored; the read-outs are recorded as they come:
  - for each word: the largest |Im| of K and of Y relative to the largest entry; the mass ratios;
  - for (W, reverse W) and (W, mirror W): K' against conj(K) and against K, and Y' against conj(Y) and against Y.
Words: LLR (its own reverse, a control); LLRLRR and LLRRLR (a reverse pair, Markov 5, CS = 0); LLLRLRR with its reverse
LLLRRLR, its mirror LLRRRLR and its mirror-reverse LLRLRRR (chiral).

Run once:  python3 -B post_hoc_reversal.py > post_hoc_reversal_run.txt 2>&1   (writes post_hoc_reversal.json)
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



mir = lambda w: w.translate(str.maketrans("LR", "RL"))
canon = lambda w: min(w[k:] + w[:k] for k in range(len(w)))
rev = lambda w: canon(w[::-1])
mirr = lambda w: canon(mir(w))

words = ["LLR", "LLRLRR", "LLRRLR", "LLLRLRR", "LLLRRLR", "LLRRRLR", "LLRLRRR"]
res, outp = {}, {"words": {}, "pairs": {}}
for w in words:
    r256, r384 = thread_integrals(w, 256), thread_integrals(w, 384)
    m256, m384 = masses(r256["K"], r256["Y"]), masses(r384["K"], r384["Y"])
    K, Y = r384["K"], r384["Y"]
    res[w] = (K, Y)
    outp["words"][w] = {"reverse": rev(w), "mirror": mirr(w), "y_max": r384["y_max"],
                        "Im K / max|K|": float(np.max(np.abs(K.imag)) / np.max(np.abs(K))),
                        "Im Y / max|Y|": float(np.max(np.abs(Y.imag)) / np.max(np.abs(Y))),
                        "m2/m3": m384["m2/m3"], "m1/m3": m384["m1/m3"],
                        "N256 vs N384": max(abs(m256[k] - m384[k]) / abs(m384[k]) for k in ("m2/m3", "m1/m3")),
                        "K": [[[z.real, z.imag] for z in row] for row in K],
                        "Y": [[[z.real, z.imag] for z in row] for row in Y]}
    print(w, {k: v for k, v in outp["words"][w].items() if k not in ("K", "Y")}, flush=True)


def rel(A, B):
    return float(np.max(np.abs(A - B)) / np.max(np.abs(B)))


for w in words:
    for kind, f in (("reverse", rev), ("mirror", mirr)):
        p = f(w)
        if p in res and p != w and (p, w, kind) not in [(a, b, k) for (a, b, k) in outp["pairs"].get("_seen", [])]:
            (K1, Y1), (K2, Y2) = res[w], res[p]
            outp["pairs"][f"{w} | {kind} {p}"] = {"K' vs conj K": rel(K2, np.conj(K1)), "K' vs K": rel(K2, K1),
                                                  "Y' vs conj Y": rel(Y2, np.conj(Y1)), "Y' vs Y": rel(Y2, Y1)}
            outp["pairs"].setdefault("_seen", []).append((w, p, kind))
            print(f"{w} | {kind} {p}", outp["pairs"][f"{w} | {kind} {p}"], flush=True)
outp["pairs"].pop("_seen", None)
outp["seconds"] = round(time.time() - t0, 1)
(HERE / "post_hoc_reversal.json").write_text(json.dumps(outp, indent=1) + "\n")
print("seconds", outp["seconds"])
