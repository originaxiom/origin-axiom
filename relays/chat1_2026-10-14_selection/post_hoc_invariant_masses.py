"""POST HOC (labelled), after the step-3a pre-seal review found that the thread frame's mass formula is not basis-invariant
where K or Y is complex. Setup copied verbatim from post_hoc_long_words.py (itself lagrange_law.py's construction).

With K_ab = cycle integral of <F_a, F_b> (linear in the first slot), a change of sections F -> U F sends K -> U K U^H and
Y -> U Y U^T, and the invariant masses are the singular values of K^{-1/2} Y (K^{-1/2})^T. The sealed thread frame and
the Lagrange law used (K^{-1/2})^T Y K^{-1/2}. The two agree when K and Y are real, as on every reflection-symmetric
thread (its reversal or its mirror is a rotation of it). This script recomputes, with both forms:
  P1  every Lyndon word of length 2..8 at N = 256 and 384: both forms' ratios, their relative difference, and whether the
      word is reflection-symmetric (the difference must vanish there: a control);
  P2  the Lagrange law's sealed cells LL1-LL5 re-scored with the invariant form (same admission rule, same fits);
  P3  the five long words and the seven reversal words, both forms;
  P4  the least m1/m2 among admitted threads with m2/m3 in [0.002, 0.07] (step 3a's C1 reference), both forms.

Run once:  python3 -B post_hoc_invariant_masses.py > post_hoc_invariant_masses_run.txt 2>&1
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
rev = lambda w: canon(w[::-1])
refl = lambda w: rev(w) == canon(w) or canon(mir(w)) == canon(w)


def masses_inv(K, Y):
    ev, U = np.linalg.eigh(K)
    Kmh = U @ np.diag(ev ** -0.5) @ U.conj().T
    s = np.sort(np.linalg.svd(Kmh @ Y @ Kmh.T, compute_uv=False))
    return {"m2/m3": float(s[1] / s[2]), "m1/m3": float(s[0] / s[2])}


words = [w for w in lyndon(8) if len(w) >= 2]
extra = ["LLRRLRLRLR", "LLRRLRLRLRLRLRLRLR", "LLRLRLRLRLR", "LLRLRLRLRLRLRLRLRLRLRLRLRLR", "LLRRLLRRLR",
         "LLRLRR", "LLRRLR", "LLLRLRR", "LLLRRLR", "LLRRRLR", "LLRLRRR"]
rows = {}
for w in words + [e for e in extra if e not in words]:
    r256, r384 = thread_integrals(w, 256), thread_integrals(w, 384)
    o256, o384 = masses(r256["K"], r256["Y"]), masses(r384["K"], r384["Y"])
    n256, n384 = masses_inv(r256["K"], r256["Y"]), masses_inv(r384["K"], r384["Y"])
    diff = max(abs(n384[k] - o384[k]) / abs(o384[k]) for k in ("m2/m3", "m1/m3"))
    agree_new = max(abs(n256[k] - n384[k]) / abs(n384[k]) for k in ("m2/m3", "m1/m3"))
    rows[w] = {"length": len(w), "reflection-symmetric": refl(w), "y_max": r384["y_max"],
               "old m2/m3": o384["m2/m3"], "old m1/m3": o384["m1/m3"], "new m2/m3": n384["m2/m3"], "new m1/m3": n384["m1/m3"],
               "old vs new, worst relative": diff, "new N256 vs N384": agree_new,
               "admitted (new)": bool(r384["y_max"] <= 3.0 and agree_new <= 1e-5),
               "max|Im K|/|K|": float(np.max(np.abs(r384["K"].imag)) / np.max(np.abs(r384["K"]))),
               "max|Im Y|/|Y|": float(np.max(np.abs(r384["Y"].imag)) / np.max(np.abs(r384["Y"])))}
    print(w, {k: rows[w][k] for k in ("reflection-symmetric", "old vs new, worst relative", "new m2/m3", "admitted (new)")}, flush=True)
out = {"status": "post hoc (labelled), after the step-3a pre-seal review", "rows": rows}
sym = [w for w in rows if rows[w]["reflection-symmetric"]]
out["P1"] = {"reflection-symmetric words": len(sym), "their worst old-vs-new difference": max(rows[w]["old vs new, worst relative"] for w in sym),
             "other words": [w for w in words if not rows[w]["reflection-symmetric"]],
             "their worst old-vs-new difference": max(rows[w]["old vs new, worst relative"] for w in words if not rows[w]["reflection-symmetric"])}
adm = [w for w in words if rows[w]["admitted (new)"]]
new = [w for w in adm if len(w) >= 6]
yv = np.array([rows[w]["y_max"] for w in adm]); l2 = np.log([rows[w]["new m2/m3"] for w in adm])
yn = np.array([rows[w]["y_max"] for w in new]); l2n = np.log([rows[w]["new m2/m3"] for w in new]); l1n = np.log([rows[w]["new m1/m3"] for w in new])
top = max(adm, key=lambda w: rows[w]["new m2/m3"])
low = [w for w in adm if rows[w]["y_max"] < 1.5]; high = [w for w in adm if rows[w]["y_max"] > 2.0]
out["P2"] = {"n admitted": len(adm), "n new admitted": len(new),
             "LL1 Spearman": float(spearmanr(yv, l2).correlation),
             "LL2 RMS": float(np.sqrt(np.mean((l2n - (7.1069 - 7.2941 * yn)) ** 2))),
             "LL3 largest": [top, rows[top]["new m2/m3"]],
             "LL4 violations": [w for w in low if rows[w]["new m2/m3"] <= 0.01] + [w for w in high if rows[w]["new m2/m3"] >= 1e-3],
             "LL5 RMS": float(np.sqrt(np.mean((l1n - (5.9196 - 8.1172 * yn)) ** 2)))}
out["P3"] = {w: rows[w] for w in extra}
band = lambda key2, key1: min(((rows[w][key1] / rows[w][key2], w) for w in adm if 0.002 <= rows[w][key2] <= 0.07), default=None)
out["P4"] = {"old form": band("old m2/m3", "old m1/m3"), "invariant form": band("new m2/m3", "new m1/m3")}
out["seconds"] = round(time.time() - t0, 1)
print(json.dumps({k: out[k] for k in ("P1", "P2", "P4")}, indent=1, default=str))
(HERE / "post_hoc_invariant_masses.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
