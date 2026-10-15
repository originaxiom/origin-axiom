"""POST HOC (labelled), 2026-10-15, after the owner's question at 01:36 ("are you sure about your math on all your
negatives? what are you doing wrong?") and four read-only audits. No prediction is scored; nothing here re-grades step
3a's sealed cells.

The question: is step 3a's negative (S2, S3: the (3/2, 7/2) cell keeps the light pair together) a property of the
cell, or of the completion H-ORTH that chat1 chose? The 7/2 one-unit space on each line is two-dimensional (W68), and
it contains E4 F_l, where F_l is the unique one-unit -1/2 section (E4 = 1 + 240 q + ... has weight 4 and leaves the
unit's coefficient at 1). So every completion is E4 F_l + alpha_l f, with f the unique holomorphic 7/2 section. Since
F_+ at -1/2 is R itself and R.R = 0, E4 R is isotropic and G(X, E4 R, R) = E4 (R.R) X = 0: under the ring completion
alpha = 0 the + column of both 7/2 cells vanishes.

  I1  the Serre derivative of each -1/2 section is proportional to the 3/2 section W72 uses (theta_k = q d/dq - k/12 E2)
  I2  step 3a's particular 7/2 section minus E4 F_l is proportional to f (alpha_l)
  I3  theta^2 F_l, normalised at its unit, minus E4 F_l is proportional to f (beta_l)
  Q   controls: the new integrands' invariance under 20 random moves (thread_frame.py's test); H-ORTH computed from the
      E4 basis reproduces weights_cells.json (it must, since H-ORTH does not depend on the representative)
  C   the cells C2 = (3/2, 7/2) with h at 9/2 and C3 = (-1/2, 7/2) with h at 5/2 under four completions:
        H-ORTH (step 3a's), H-E4 (alpha = 0), H-PART (step 3a's particular sections, uncompleted), H-THETA2 (theta^2 F)
      on every Lyndon word of length 2..8, with step 3a's admission rule and mass formula (K_L^-1/2 Y (K_R^-1/2)^T).

Run once:  python3 -B post_hoc_completions.py > post_hoc_completions_run.txt 2>&1   (writes post_hoc_completions.json)
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
TMP = pathlib.Path(tempfile.mkdtemp(prefix="completions_sm_"))
blob = subprocess.run(["git", "-C", str(REPO), "archive", SMC, "docs/dossiers/the_weave_2026-10-07", "frontier"],
                      check=True, capture_output=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP, filter="data")
DOSS = TMP / "docs" / "dossiers" / "the_weave_2026-10-07"
sys.path.insert(0, str(DOSS))
os.chdir(DOSS)
import the_surface_yukawa as SY  # noqa: E402
SU, RC = SY.SU, SY.RC
mp.mp.dps = 40
I = mp.mpc(0, 1)
out = {"sm_seat_commit": SMC, "status": "post hoc (labelled), after the owner's question of 2026-10-15 01:36; no prediction"}
print("modules loaded", round(time.time() - t0, 1), file=sys.stderr, flush=True)
K32, K72, KM12 = Fraction(3, 2), Fraction(7, 2), Fraction(-1, 2)
UNIT8 = {l: SY.E8[l] - 8 for l in SY.LINES}             # the one-unit exponent, in eighths


def solve72(units, norm_line, excl=("e_i", 0), N=30, M=120):
    """weights_cells.py's solve72, verbatim"""
    u = dict(zip(SY.LINES, units))
    n0 = -u[norm_line]
    cols = [(l, n) for l in SY.LINES for n in range(-u[l], N) if not (l == norm_line and n == n0) and (l, n) != excl]
    thetas = [mp.pi / 3 + mp.mpf("0.02") + j * (mp.pi / 3 - mp.mpf("0.04")) / (M - 1) for j in range(M)]
    A = mp.matrix(3 * M, len(cols))
    b = mp.matrix(3 * M, 1)
    kk = mp.mpf(K72.numerator) / K72.denominator
    for r, th in enumerate(thetas):
        t = mp.exp(I * th)
        ts, tk = -1 / t, mp.power(t, kk)
        for c, (l, n) in enumerate(cols):
            e = n + SU.LAM[l]
            sc = mp.exp(2 * mp.pi * e * SU.H0)
            v2 = SU.matvec(SU.RS, SU.B[l])
            for q in range(3):
                A[3 * r + q, c] = (SU.B[l][q] * SU.qp(e, ts) - tk * v2[q] * SU.qp(e, t)) * sc
        e = n0 + SU.LAM[norm_line]
        v2 = SU.matvec(SU.RS, SU.B[norm_line])
        for q in range(3):
            b[3 * r + q] = -(SU.B[norm_line][q] * SU.qp(e, ts) - tk * v2[q] * SU.qp(e, t))
    Q, Rm = mp.qr(A, mode="skinny")
    x = mp.lu_solve(Rm, Q.H * b)
    res = mp.norm(A * x - b) / mp.norm(b)
    terms = [(norm_line, n0 + SU.LAM[norm_line], mp.mpf(1))] + [
        (l, n + SU.LAM[l], x[c] * mp.exp(2 * mp.pi * (n + SU.LAM[l]) * SU.H0)) for c, (l, n) in enumerate(cols)]
    return terms, float(res)


# ------------------------------------------------------------------ the forms (as weights_cells.py builds them)
resid = {}
F32, FM12, F72P = [], [], []
for name, u in SY.MATTER:
    terms, r, line = SY.best_section(u, K32); F32.append(SY.to_series(terms, SY.E8)); resid[f"{name} 3/2"] = r
    terms, r, line = SY.best_section(u, KM12); FM12.append(SY.to_series(terms, SY.E8)); resid[f"{name} -1/2"] = r
terms, r, line = SY.best_section((0, 1, 0), KM12); Rser = SY.to_series(terms, SY.E8); resid["R"] = r
fbest = None
for line in SY.LINES:
    terms, r = RC.solve((0, 0, 0), K72, line)
    if fbest is None or r < fbest[1]: fbest = (terms, r, line)
fser = SY.to_series(fbest[0], SY.E8); resid["f 7/2"] = fbest[1]
for (name, u), line in zip(SY.MATTER, ("e_i", "v+", "v-")):
    terms, r = solve72(u, line); F72P.append(SY.to_series(terms, SY.E8)); resid[f"{name} 7/2 (particular)"] = r
hb5 = hb9 = None
for line in ("v+", "e_i", "v-"):
    terms, r = SY.solve_twisted(Fraction(5, 2), line)
    if hb5 is None or r < hb5[1]: hb5 = (terms, r, line)
    terms, r = SY.solve_twisted(Fraction(9, 2), line)
    if hb9 is None or r < hb9[1]: hb9 = (terms, r, line)
h5, h9 = SY.to_series(hb5[0], SY.E8P), SY.to_series(hb9[0], SY.E8P)
resid["h 5/2"], resid["h 9/2"] = hb5[1], hb9[1]
out["residuals"] = resid
print("forms built", round(time.time() - t0, 1), file=sys.stderr, flush=True)

# ------------------------------------------------------------------ E4, E2, the Serre derivative
CAP = SY.CAP8 // 8
sig = lambda m, p: sum(d ** p for d in range(1, m + 1) if m % d == 0)
E4 = {0: mp.mpf(1)}; E4.update({8 * m: mp.mpf(240 * sig(m, 3)) for m in range(1, CAP + 1)})
E2 = {0: mp.mpf(1)}; E2.update({8 * m: mp.mpf(-24 * sig(m, 1)) for m in range(1, CAP + 1)})


def serre(X, k):
    D = {key: (mp.mpf(key[1]) / 8) * a for key, a in X.items()}
    return SY.add((1, D), (-mp.mpf(k.numerator) / (12 * k.denominator), SY.scal_vec(E2, X)))


def unit_coeff(X, l):
    return X.get((l, UNIT8[l]), mp.mpc(0))


TOP8 = 8 * 22                                           # compare coefficients up to exponent 22 (truncation-safe)


PTS = np.array([0.1 + 0.9j, 1j, -0.3 + 1.2j, 0.45 + 1.6j, 2j])


def prop_fit(X, Y):
    """fit X = s Y on the coefficients with exponent <= 22; return s, the worst coefficient residual relative to the
    largest coefficient, and the worst value residual at five points of the fundamental domain relative to |X|"""
    keys = [k for k in set(X) | set(Y) if k[1] <= TOP8]
    num = sum(X.get(k, 0) * mp.conj(Y.get(k, 0)) for k in keys)
    den = sum(abs(Y.get(k, 0)) ** 2 for k in keys)
    s = num / den
    big = max(abs(X.get(k, 0)) for k in keys)
    rc = float(max(abs(X.get(k, 0) - s * Y.get(k, 0)) for k in keys) / big)
    xv, yv = SY.np_eval(X)(PTS), SY.np_eval(Y)(PTS)
    rv = float(np.max(np.abs(xv - complex(s) * yv)) / np.max(np.abs(xv)))
    return s, rc, rv


E4F = [SY.scal_vec(E4, F) for F in FM12]
ident = {"I1 theta(F_l at -1/2) = s F_l at 3/2": {}, "I2 particular 7/2 - E4 F_l = alpha f": {},
         "I3 theta^2 F_l (normalised) - E4 F_l = beta f": {}}
alpha, beta = [], []
for j, ((name, u), l) in enumerate(zip(SY.MATTER, ("e_i", "v+", "v-"))):
    th1 = serre(FM12[j], KM12)
    s1, r1c, r1v = prop_fit(th1, F32[j])
    ident["I1 theta(F_l at -1/2) = s F_l at 3/2"][name] = {"s": complex(s1), "coefficient residual": r1c,
                                                             "value residual": r1v}
    a, r2c, r2v = prop_fit(SY.add((1, F72P[j]), (-1, E4F[j])), fser)
    alpha.append(complex(a))
    ident["I2 particular 7/2 - E4 F_l = alpha f"][name] = {
        "alpha": complex(a), "coefficient residual": r2c, "value residual": r2v,
        "unit coefficients (particular, E4 F)": [complex(unit_coeff(F72P[j], l)), complex(unit_coeff(E4F[j], l))]}
    th2 = serre(th1, K32)
    u2 = unit_coeff(th2, l)
    th2 = {k: v / u2 for k, v in th2.items()}
    b_, r3c, r3v = prop_fit(SY.add((1, th2), (-1, E4F[j])), fser)
    beta.append(complex(b_))
    ident["I3 theta^2 F_l (normalised) - E4 F_l = beta f"][name] = {"beta": complex(b_), "coefficient residual": r3c,
                                                                      "value residual": r3v}
iso = SY.G_series(FM12[0], E4F[1], Rser)
ref = SY.G_series(FM12[0], E4F[0], Rser)
ident["G(F_i, E4 R, R) against G(F_i, E4 F_i, R), largest coefficients (an identity: E4 (R.R) F_i = 0)"] = [
    float(max((abs(v) for v in iso.values()), default=0.0)), float(max(abs(v) for v in ref.values()))]
out["identities"] = ident
print("identities", json.dumps(ident, indent=1, default=str), flush=True)

# ------------------------------------------------------------------ G series and integrands, right basis (E4 F_i, E4 F_+, E4 F_-, f)
RB = E4F + [fser]
G2 = {(a, b): SY.G_series(F32[a], RB[b], Rser) for a in range(3) for b in range(4)}
G3 = {(a, b): SY.G_series(FM12[a], RB[b], Rser) for a in range(3) for b in range(4)}
ev = SY.np_eval
F32n, FM12n, RBn = [ev(s) for s in F32], [ev(s) for s in FM12], [ev(s) for s in RB]
G2n = {k: ev(v) for k, v in G2.items()}; G3n = {k: ev(v) for k, v in G3.items()}
h5n, h9n = ev(h5), ev(h9)
print("series ready", round(time.time() - t0, 1), file=sys.stderr, flush=True)


def integrands(T):
    y = T.imag
    a32 = [f(T) for f in F32n]; am = [f(T) for f in FM12n]; ar = [f(T) for f in RBn]
    v5, v9 = h5n(T), h9n(T)
    res = {}
    for i in range(3):
        for j in range(3):
            res[("K32", i, j)] = np.sum(a32[i] * np.conj(a32[j]), axis=1) * y ** 1.5
            res[("KM12", i, j)] = np.sum(am[i] * np.conj(am[j]), axis=1) * y ** -0.5
    for i in range(4):
        for j in range(4):
            res[("K72", i, j)] = np.sum(ar[i] * np.conj(ar[j]), axis=1) * y ** 3.5
    for a in range(3):
        for b in range(4):
            res[("Y2", a, b)] = np.sum(G2n[(a, b)](T) * np.conj(v9), axis=1) * y ** 4.5
            res[("Y3", a, b)] = np.sum(G3n[(a, b)](T) * np.conj(v5), axis=1) * y ** 2.5
    return res


def reduce(t):
    for _ in range(10000):
        t = t - round(t.real)
        if abs(t) < 1 - 1e-14:
            t = -1 / t
        else:
            return t
    raise RuntimeError("reduction did not terminate")


rng = np.random.default_rng(20261015)
S_ = np.array([[0, -1], [1, 0]]); T_ = np.array([[1, 1], [0, 1]]); Ti = np.array([[1, -1], [0, 1]])
GAMMAS = [S_, T_ @ S_, S_ @ T_, Ti @ S_, S_ @ Ti, T_ @ S_ @ T_]
mob = lambda g, t: (g[0, 0] * t + g[0, 1]) / (g[1, 0] * t + g[1, 1])
inv_by, ntests = {}, 0
while ntests < 20:
    t = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.8, 1.2))
    g = GAMMAS[rng.integers(len(GAMMAS))]
    tg = mob(g, t)
    if tg.imag < 0.75 or t.imag < 0.75:
        continue
    A, B = integrands(np.array([t])), integrands(np.array([tg]))
    floor = 1e-12 * max(abs(A[k][0]) for k in A)
    for k in A:
        dev = float(abs(A[k][0] - B[k][0]) / max(abs(A[k][0]), abs(B[k][0]), floor))
        inv_by[k[0]] = max(inv_by.get(k[0], 0.0), dev)
    ntests += 1
out["Q invariance by family"] = inv_by

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


def raw(word, N):
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
    S = lambda key: w * np.sum(vals[key])
    return {"y_max": float(np.max(Tr.imag)),
            "K32": np.array([[S(("K32", i, j)) for j in range(3)] for i in range(3)]),
            "KM12": np.array([[S(("KM12", i, j)) for j in range(3)] for i in range(3)]),
            "K72": np.array([[S(("K72", i, j)) for j in range(4)] for i in range(4)]),
            "Y2x": np.array([[S(("Y2", a_, b_)) for b_ in range(4)] for a_ in range(3)]),
            "Y3x": np.array([[S(("Y3", a_, b_)) for b_ in range(4)] for a_ in range(3)])}


def inv_sqrt(K):
    ev_, U = np.linalg.eigh(K)
    if not np.all(np.isfinite(ev_)) or ev_.min() <= 0:
        return None
    return U @ np.diag(ev_ ** -0.5) @ U.conj().T


def masses(KL, Y, KR):
    A, B = inv_sqrt(KL), inv_sqrt(KR)
    if A is None or B is None:
        nan = float("nan")
        return {"m2/m3": nan, "m1/m3": nan, "m1/m2": nan, "pd": False}
    s = np.sort(np.linalg.svd(A @ Y @ B.T, compute_uv=False))
    return {"m2/m3": float(s[1] / s[2]), "m1/m3": float(s[0] / s[2]), "m1/m2": float(s[0] / s[1]) if s[1] > 0 else None,
            "pd": True}


def completion(r, name):
    K = r["K72"]
    if name == "H-ORTH":
        c = -K[:3, 3] / K[3, 3]
    elif name == "H-E4":
        c = np.zeros(3, dtype=complex)
    elif name == "H-PART":
        c = np.array(alpha, dtype=complex)
    else:
        c = np.array(beta, dtype=complex)
    P3 = np.hstack([np.eye(3), c.reshape(3, 1)])
    return P3 @ K @ P3.conj().T, r["Y2x"] @ P3.T, r["Y3x"] @ P3.T


COMPS = ("H-ORTH", "H-E4", "H-PART", "H-THETA2")
sealed = json.loads((HERE / "weights_cells.json").read_text())["per thread"]
words = [w for w in lyndon(8) if len(w) >= 2]
per, q_orth = {}, 0.0
for w in words:
    r256, r384 = raw(w, 256), raw(w, 384)
    row = {"y_max": r384["y_max"]}
    for comp in COMPS:
        KR256, Y2_256, Y3_256 = completion(r256, comp)
        KR384, Y2_384, Y3_384 = completion(r384, comp)
        for cell, (KL256, Y256, KL384, Y384) in (("C2", (r256["K32"], Y2_256, r384["K32"], Y2_384)),
                                                  ("C3", (r256["KM12"], Y3_256, r384["KM12"], Y3_384))):
            m256, m384 = masses(KL256, Y256, KR256), masses(KL384, Y384, KR384)
            rank2 = bool(m384["pd"] and m384["m1/m3"] < 1e-10)
            keys = ("m2/m3",) if rank2 else ("m2/m3", "m1/m3")
            agree = max(abs(m256[k] - m384[k]) / abs(m384[k]) for k in keys) if m384["pd"] and m256["pd"] else float("inf")
            row[f"{comp} {cell}"] = dict(m384, **{"rank 2": rank2, "N256 vs N384": agree,
                                                  "admitted": bool(r384["y_max"] <= 3.0 and agree <= 1e-5)})
    for cell in ("C2", "C3"):
        for k in ("m2/m3",) + (("m1/m3",) if cell == "C2" else ()):
            q_orth = max(q_orth, abs(row[f"H-ORTH {cell}"][k] - sealed[w][cell][k]) / abs(sealed[w][cell][k]))
    per[w] = row
    print(w, {f"{c} {cl}": (round(row[f'{c} {cl}']['m2/m3'], 5), row[f'{c} {cl}']['m1/m2'] if not row[f'{c} {cl}']['rank 2'] else 0.0)
              for c in COMPS for cl in ("C2", "C3")}, flush=True)
out["per thread"] = per
out["Q H-ORTH from the E4 basis against weights_cells.json, worst relative"] = q_orth

summary = {}
for comp in COMPS:
    for cell in ("C2", "C3"):
        key = f"{comp} {cell}"
        adm = [w for w in words if per[w][key]["admitted"]]
        band = [w for w in adm if 0.002 <= per[w][key]["m2/m3"] <= 0.07]
        r3band = [w for w in band if not per[w][key]["rank 2"]]
        top = max(adm, key=lambda w: per[w][key]["m2/m3"]) if adm else None
        root_rank = sorted(adm, key=lambda w: -per[w][key]["m2/m3"]).index("LR") + 1 if "LR" in adm else None
        summary[key] = {
            "admitted": len(adm), "rank 2 on": sum(per[w][key]["rank 2"] for w in adm),
            "in the band": len(band),
            "least m1/m2 in the band among rank-3 threads": min(((per[w][key]["m1/m2"], w) for w in r3band), default=None),
            "rank-3 threads in the band with m1/m2 <= 0.005": [w for w in r3band if per[w][key]["m1/m2"] <= 0.005],
            "the root": {k: per["LR"][key][k] for k in ("m2/m3", "m1/m3", "m1/m2", "rank 2", "admitted")},
            "the root's place by m2/m3 (1 = largest)": root_rank,
            "largest m2/m3": [top, per[top][key]["m2/m3"]] if top else None,
            "Spearman(y_max, ln m2/m3)": float(spearmanr([per[w]["y_max"] for w in adm],
                                                         [math.log(per[w][key]["m2/m3"]) for w in adm]).correlation) if len(adm) > 3 else None}
out["summary"] = summary
out["seconds"] = round(time.time() - t0, 1)
print(json.dumps({k: out[k] for k in ("Q invariance by family", "Q H-ORTH from the E4 basis against weights_cells.json, worst relative",
                                      "summary")}, indent=1, default=str))
(HERE / "post_hoc_completions.json").write_text(json.dumps(out, indent=1, default=lambda z: [z.real, z.imag]
                                                           if isinstance(z, complex) else str(z)) + "\n")
