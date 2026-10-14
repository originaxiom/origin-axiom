"""Step 3a: the thread frame's weights cells (PREREGISTRATION_WEIGHTS.md, sealed at 641ef8d94, sha256 c332b494...; see the commit
that adds this script). Run ONCE, and only after main banks THE FRAME TRIBUNAL (P-136), unless the owner says otherwise.

The construction is thread_frame.py's (copied from lagrange_law.py, which copied it verbatim): the SM seat's W72 forms at
87cf7f551 through git archive, B1644's coupling G_ab = (R.F_b)F_a + (R.F_a)F_b - (F_a.F_b)R, cycle integrals along the
thread's closed geodesic at the image of each point in the standard fundamental domain, the trapezoid rule.

New here (the seal states them; nothing below was run before the seal except the disclosed plumbing):
  - matter at -1/2: W68's unique one-unit sections in rho_R (best_section(u, -1/2)); its F+ is R itself;
  - matter at 7/2: f, the unique holomorphic section (no unit), and one particular one-unit section per line, made
    unique by setting its (e_i, exponent 1/8) coefficient to zero (that is f's normalised coefficient), then
    H-ORTH on each thread: F~_b = F_b - c_b f with c_b = <F_b, f>_W / <f, f>_W, the weight-7/2 cycle inner product;
  - the Higgs's holomorphic mode at 9/2 in rho' (solve_twisted(9/2, line), the line of least residual).
Cells: C1 = (3/2, 3/2) with h at 5/2 (the sealed thread frame's), C2 = (3/2, 7/2) with h at 9/2, C3 = (-1/2, 7/2) with
h at 5/2. Masses: singular values of K_L^{-1/2} Y (K_R^{-1/2})^T, with K_ab = cycle integral of <F_a, F_b> (linear in
the first slot). This is the basis-invariant form (the pre-seal review's blocker); it equals thread_frame.py's
(K^{-1/2})^T Y K^{-1/2} whenever K and Y are real, as on every reflection-symmetric thread.

Run once:  python3 -B weights_cells.py > weights_cells_run.txt 2>&1   (writes weights_cells.json beside itself)
"""
import io, json, math, os, pathlib, subprocess, sys, tarfile, tempfile, time
from fractions import Fraction
import numpy as np
import mpmath as mp
from scipy.stats import spearmanr

t0 = time.time()
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
SEL = HERE.parent / "chat1_2026-10-14_selection"
SMC = "87cf7f55111ec1f4019f302ffaa578376a9143e6"
TMP = pathlib.Path(tempfile.mkdtemp(prefix="weights_cells_sm_"))
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
out = {"sm_seat_commit": SMC, "status": "step 3a, the weights cells (sealed; one run)"}
print("modules loaded", round(time.time() - t0, 1), file=sys.stderr, flush=True)

K32, K72, KM12 = Fraction(3, 2), Fraction(7, 2), Fraction(-1, 2)


def solve72(units, norm_line, excl=("e_i", 0), N=30, M=120):
    """RC.solve (W68's collocation) copied, with one more column removed: the coefficient at excl is set to zero"""
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


# ------------------------------------------------------------------ the forms
resid = {}
F32, FM12, F72 = [], [], []
for name, u in SY.MATTER:
    terms, r, line = SY.best_section(u, K32); F32.append(SY.to_series(terms, SY.E8)); resid[f"F{name} 3/2"] = r
    terms, r, line = SY.best_section(u, KM12); FM12.append(SY.to_series(terms, SY.E8)); resid[f"F{name} -1/2"] = r
terms, r, line = SY.best_section((0, 1, 0), KM12); Rser = SY.to_series(terms, SY.E8); resid["R"] = r
fbest = None
for line in SY.LINES:
    terms, r = RC.solve((0, 0, 0), K72, line)
    if fbest is None or r < fbest[1]: fbest = (terms, r, line)
fser = SY.to_series(fbest[0], SY.E8); resid["f 7/2"] = fbest[1]; out["f normalised on"] = fbest[2]
F72ALT = []
for (name, u), line in zip(SY.MATTER, ("e_i", "v+", "v-")):
    terms, r = solve72(u, line); F72.append(SY.to_series(terms, SY.E8)); resid[f"F{name} 7/2 (particular)"] = r
    terms, r = solve72(u, line, excl=("v-", 0)); F72ALT.append(SY.to_series(terms, SY.E8))
    resid[f"F{name} 7/2 (second particular, (v-, 3/8) set to zero)"] = r
hb5 = hb9 = None
for line in ("v+", "e_i", "v-"):
    terms, r = SY.solve_twisted(Fraction(5, 2), line)
    if hb5 is None or r < hb5[1]: hb5 = (terms, r, line)
    terms, r = SY.solve_twisted(Fraction(9, 2), line)
    if hb9 is None or r < hb9[1]: hb9 = (terms, r, line)
h5, h9 = SY.to_series(hb5[0], SY.E8P), SY.to_series(hb9[0], SY.E8P)
resid["h 5/2"], resid["h 9/2"] = hb5[1], hb9[1]
print("forms built", round(time.time() - t0, 1), file=sys.stderr, flush=True)
banked = json.loads((DOSS / "the_surface_yukawa.json").read_text())
bh = banked["read-outs"]["h's first coefficients"]
mine = {f"{l}:{Fraction(n8, 8)}": complex(a) for (l, n8), a in h5.items() if n8 < 24}
q0h = max(abs(complex(*bh[k]) - mine[k]) for k in bh)
rdev = max(abs(complex(Rser.get(k, 0)) - complex(FM12[1].get(k, 0))) for k in set(Rser) | set(FM12[1]))  # an identity

# G series. C1: symmetric pairs; C2, C3: left a (3) x right b (3) plus the right f (H-orth)
PAIRS = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
G1 = {p: SY.G_series(F32[p[0]], F32[p[1]], Rser) for p in PAIRS}
RIGHT = F72 + [fser]                                   # index 3 is f
G2 = {(a, b): SY.G_series(F32[a], RIGHT[b], Rser) for a in range(3) for b in range(4)}
G3 = {(a, b): SY.G_series(FM12[a], RIGHT[b], Rser) for a in range(3) for b in range(4)}
RIGHTALT = F72ALT + [fser]
G2ALT = {(a, b): SY.G_series(F32[a], RIGHTALT[b], Rser) for a in range(3) for b in range(3)}
G3ALT = {(a, b): SY.G_series(FM12[a], RIGHTALT[b], Rser) for a in range(3) for b in range(3)}
ev = SY.np_eval
F32n, FM12n, RIGHTn = [ev(s) for s in F32], [ev(s) for s in FM12], [ev(s) for s in RIGHT]
G1n = {k: ev(v) for k, v in G1.items()}; G2n = {k: ev(v) for k, v in G2.items()}; G3n = {k: ev(v) for k, v in G3.items()}
RIGHTALTn = [ev(s_) for s_ in RIGHTALT]
G2ALTn = {k: ev(v) for k, v in G2ALT.items()}; G3ALTn = {k: ev(v) for k, v in G3ALT.items()}
h5n, h9n = ev(h5), ev(h9)
print("series ready", round(time.time() - t0, 1), file=sys.stderr, flush=True)


def integrands(T, alt=False):
    y = T.imag
    a32 = [f(T) for f in F32n]; am = [f(T) for f in FM12n]
    ar = [f(T) for f in (RIGHTALTn if alt else RIGHTn)]
    g2 = {k: (G2ALTn[k] if (alt and k[1] < 3) else G2n[k]) for k in G2n}
    g3 = {k: (G3ALTn[k] if (alt and k[1] < 3) else G3n[k]) for k in G3n}
    v5, v9 = h5n(T), h9n(T)
    res = {}
    for i in range(3):
        for j in range(3):
            res[("K32", i, j)] = np.sum(a32[i] * np.conj(a32[j]), axis=1) * y ** 1.5
            res[("KM12", i, j)] = np.sum(am[i] * np.conj(am[j]), axis=1) * y ** -0.5
    for i in range(4):
        for j in range(4):
            res[("K72", i, j)] = np.sum(ar[i] * np.conj(ar[j]), axis=1) * y ** 3.5
    for p in PAIRS:
        res[("Y1",) + p] = np.sum(G1n[p](T) * np.conj(v5), axis=1) * y ** 2.5
    for a in range(3):
        for b in range(4):
            res[("Y2", a, b)] = np.sum(g2[(a, b)](T) * np.conj(v9), axis=1) * y ** 4.5
            res[("Y3", a, b)] = np.sum(g3[(a, b)](T) * np.conj(v5), axis=1) * y ** 2.5
    return res


def reduce(t):
    for _ in range(10000):
        t = t - round(t.real)
        if abs(t) < 1 - 1e-14:
            t = -1 / t
        else:
            return t
    raise RuntimeError("reduction did not terminate")


# ------------------------------------------------------------------ Q0(c): invariance (thread_frame.py's test)
rng = np.random.default_rng(20261014)
S_ = np.array([[0, -1], [1, 0]]); T_ = np.array([[1, 1], [0, 1]]); Ti = np.array([[1, -1], [0, 1]])
GAMMAS = [S_, T_ @ S_, S_ @ T_, Ti @ S_, S_ @ Ti, T_ @ S_ @ T_]
mob = lambda g, t: (g[0, 0] * t + g[0, 1]) / (g[1, 0] * t + g[1, 1])
inv_worst, ntests = 0.0, 0
inv_by = {}                                           # worst relative deviation per integrand family
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
        inv_worst = max(inv_worst, dev)
        inv_by[k[0]] = max(inv_by.get(k[0], 0.0), dev)
    ntests += 1
VOID = {"C2": max(inv_by["K32"], inv_by["K72"], inv_by["Y2"]) >= 1e-9,
        "C3": max(inv_by["KM12"], inv_by["K72"], inv_by["Y3"]) >= 1e-9}

# ------------------------------------------------------------------ threads (verbatim from thread_frame.py)
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


def thread_mats(word, N, alt=False):
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
    vals = integrands(Tr, alt)
    w = P / N
    S = lambda key: w * np.sum(vals[key])
    K32m = np.array([[S(("K32", i, j)) for j in range(3)] for i in range(3)])
    KM12m = np.array([[S(("KM12", i, j)) for j in range(3)] for i in range(3)])
    K72x = np.array([[S(("K72", i, j)) for j in range(4)] for i in range(4)])
    Y1 = np.zeros((3, 3), dtype=complex)
    for p in PAIRS:
        Y1[p[0], p[1]] = Y1[p[1], p[0]] = S(("Y1",) + p)
    Y2x = np.array([[S(("Y2", a_, b_)) for b_ in range(4)] for a_ in range(3)])
    Y3x = np.array([[S(("Y3", a_, b_)) for b_ in range(4)] for a_ in range(3)])
    # H-ORTH: F~_b = F_b - c_b f, c_b = <F_b, f> / <f, f>
    cvec = K72x[:3, 3] / K72x[3, 3]
    P3 = np.hstack([np.eye(3), -cvec.reshape(3, 1)])
    KR = P3 @ K72x @ P3.conj().T
    orth = float(max(abs((P3 @ K72x[:, 3])[b_]) / math.sqrt(abs(KR[b_, b_].real * K72x[3, 3].real)) for b_ in range(3)))
    Y2 = Y2x @ P3.T; Y3 = Y3x @ P3.T
    return {"rotation": rot, "trace": tr, "y_max": float(np.max(Tr.imag)), "K32": K32m, "KM12": KM12m, "KR": KR,
            "Y1": Y1, "Y2": Y2, "Y3": Y3, "c": cvec, "orth": orth}


def inv_sqrt(K):
    ev, U = np.linalg.eigh(K)
    if not np.all(np.isfinite(ev)) or ev.min() <= 0:
        return None, ev
    return U @ np.diag(ev ** -0.5) @ U.conj().T, ev


def masses(KL, Y, KR):
    A, evL = inv_sqrt(KL); B, evR = inv_sqrt(KR)
    if A is None or B is None:                        # the seal: a K not numerically positive definite is not admitted
        nan = float("nan")
        return {"m": [nan] * 3, "m2/m3": nan, "m1/m3": nan, "m1/m2": nan, "K positive definite": False,
                "KL condition": None, "KR condition": None}
    s = np.sort(np.linalg.svd(A @ Y @ B.T, compute_uv=False))
    return {"m": s.tolist(), "m2/m3": float(s[1] / s[2]), "m1/m3": float(s[0] / s[2]),
            "m1/m2": float(s[0] / s[1]) if s[1] > 0 else None, "K positive definite": True,
            "KL condition": float(evL.max() / evL.min()), "KR condition": float(evR.max() / evR.min())}


def mats_json(KL, Y, KR):
    cz = lambda M: [[[float(z.real), float(z.imag)] for z in row] for row in M]
    im = lambda M: float(np.max(np.abs(M.imag)) / np.max(np.abs(M)))
    return {"K_L": cz(KL), "K_R": cz(KR), "Y": cz(Y), "max|Im K_L|/|K_L|": im(KL), "max|Im K_R|/|K_R|": im(KR),
            "max|Im Y|/|Y|": im(Y)}


CELLMATS = {"C1": ("K32", "Y1", "K32"), "C2": ("K32", "Y2", "KR"), "C3": ("KM12", "Y3", "KR")}


def cells(r):
    return {c: masses(r[a], r[b], r[d]) for c, (a, b, d) in CELLMATS.items()}


words = [w for w in lyndon(8) if len(w) >= 2]
per = {}
for w in words:
    r256, r384 = thread_mats(w, 256), thread_mats(w, 384)
    c256, c384 = cells(r256), cells(r384)
    row = {"y_max": r384["y_max"], "trace": r384["trace"], "H-orth residual": r384["orth"],
           "|c_b|": [float(abs(z)) for z in r384["c"]]}
    for cell in ("C1", "C2", "C3"):
        keys = ("m2/m3",) if cell == "C3" else ("m2/m3", "m1/m3")
        agree = max(abs(c256[cell][k] - c384[cell][k]) / abs(c384[cell][k]) for k in keys)
        row[cell] = dict(c384[cell], **{"N256 vs N384": agree,
                                        "admitted": bool(r384["y_max"] <= 3.0 and agree <= 1e-5
                                                         and c384[cell]["K positive definite"]
                                                         and c256[cell]["K positive definite"])})
        a_, b_, d_ = CELLMATS[cell]
        row[cell]["matrices (N = 384)"] = mats_json(r384[a_], r384[b_], r384[d_])
    per[w] = row
    print(w, {c: (round(row[c]["m2/m3"], 6), row[c]["m1/m3"], row[c]["admitted"]) for c in ("C1", "C2", "C3")},
          flush=True)
out["per thread"] = per

# ------------------------------------------------------------------ Q0
ll = json.loads((SEL / "lagrange_law.json").read_text())["readouts"]["per thread"]
rA, rB = thread_mats("LR", 384), thread_mats("LR", 384, alt=True)
q0d = max(float(np.max(np.abs(rA[k] - rB[k])) / np.max(np.abs(rA[k]))) for k in ("KR", "Y2", "Y3"))
rng2 = np.random.default_rng(20261015)
rr = thread_mats("LLRLRR", 384)
q0e = 0.0
for _ in range(5):
    for cell, (a_, b_, d_) in CELLMATS.items():
        U = np.diag(np.exp(1j * rng2.uniform(0, 2 * np.pi, 3))) @ np.linalg.qr(rng2.normal(size=(3, 3)) + 1j * rng2.normal(size=(3, 3)))[0]
        V = U if cell == "C1" else np.diag(np.exp(1j * rng2.uniform(0, 2 * np.pi, 3)))
        m0 = masses(rr[a_], rr[b_], rr[d_])["m"]
        m1 = masses(U @ rr[a_] @ U.conj().T, U @ rr[b_] @ V.T, V @ rr[d_] @ V.conj().T)["m"]
        dev = max(abs(x - y_) / abs(m0[2]) for x, y_ in zip(m0, m1))
        q0e = float("inf") if not np.isfinite(dev) else max(q0e, dev)
q0a = max(abs(per[w]["C1"][k] - ll[w][k]) / abs(ll[w][k]) for w in ("LR", "LLR", "LLRR", "LLRLR", "LLLR")
          for k in ("m2/m3", "m1/m3"))
out["Q0"] = {"(a) C1 against lagrange_law.json, worst relative": q0a,
             "(b) residuals": resid, "(b) h 5/2 first coefficients vs W72": q0h, "(b) R = F+ at -1/2, max dev": rdev,
             "(c) invariance worst relative": inv_worst, "(c) by family": inv_by, "(c) tests": ntests,
             "void cells (the seal's clause)": [c for c, v in VOID.items() if v],
             "(d) the completion does not depend on the particular solution (root, KR, Y2, Y3), worst relative": q0d,
             "(d') H-orth arithmetic consistency on the root (an identity)": per["LR"]["H-orth residual"],
             "(e) masses unchanged under a change of mode basis on LLRLRR, worst relative to m3": q0e,
             "holds": bool(q0a < 1e-6 and max(resid.values()) < 1e-20 and q0h < 1e-25
                           and inv_worst < 1e-9 and q0d < 1e-10 and q0e < 1e-8)}

adm = lambda cell: [w for w in words if per[w][cell]["admitted"]]
band = lambda cell: [w for w in adm(cell) if 0.002 <= per[w][cell]["m2/m3"] <= 0.07]
s1_bad = [w for w in adm("C3") if not per[w]["C3"]["m1/m3"] < 1e-10]
out["S1"] = {"C3 admitted": len(adm("C3")), "threads with m1/m3 >= 1e-10": s1_bad[:10], "holds": bool(adm("C3") and not s1_bad)}
s2_hits = [w for w in band("C2") if per[w]["C2"]["m1/m2"] <= 0.005]
out["S2"] = {"C2 admitted": len(adm("C2")), "C2 admitted in the band": len(band("C2")), "hits": s2_hits,
             "holds": bool(s2_hits)}
c2min = min((per[w]["C2"]["m1/m2"] for w in band("C2")), default=None)
out["S3"] = {"C2's least m1/m2 in the band": c2min, "C1's (sealed reference)": 0.0515,
             "holds": bool(c2min is not None and c2min < 0.0515)}
out["S4"] = {"C3 admitted in the band": band("C3"), "holds": bool(band("C3"))}
c2a = adm("C2")
top = max(c2a, key=lambda w: per[w]["C2"]["m2/m3"]) if c2a else None
out["S5"] = {"C2's largest m2/m3": [top, per[top]["C2"]["m2/m3"]] if top else None, "holds": bool(top == "LR")}

# ------------------------------------------------------------------ read-outs (no prior)
ro = {}
for cell in ("C1", "C2", "C3"):
    ws = adm(cell)
    if len(ws) > 3:
        ro[f"{cell}: Spearman(y_max, ln m2/m3)"] = float(spearmanr([per[w]["y_max"] for w in ws],
                                                                   [math.log(per[w][cell]["m2/m3"]) for w in ws]).correlation)
    ro[f"{cell}: the root"] = per["LR"][cell]
    ro[f"{cell}: in the band"] = [[w, per[w][cell]["m2/m3"], per[w][cell]["m1/m3"]] for w in band(cell)]
hz = json.loads((DOSS / "received" / "HZ2021_running_masses_MZ.json").read_text())["masses_GeV"]["value"]
data = {"up": (hz["c"] / hz["t"], hz["u"] / hz["t"]), "down": (hz["s"] / hz["b"], hz["d"] / hz["b"]),
        "lepton": (hz["mu"] / hz["tau"], hz["e"] / hz["tau"])}
ro["C1 under the invariant formula: least m1/m2 in the band"] = min(
    ((per[w]["C1"]["m1/m2"], w) for w in band("C1")), default=None)
ro["nearest admitted (thread, cell) per sector, in (ln m2/m3, ln m1/m3) distance (read-out only)"] = {
    sec: min(((math.hypot(math.log(per[w][c]["m2/m3"] / d2), math.log(max(per[w][c]["m1/m3"], 1e-300) / d1)), w, c)
              for c in ("C1", "C2") for w in adm(c)), default=None)
    for sec, (d2, d1) in data.items()}
ro["seconds"] = round(time.time() - t0, 1)
out["readouts"] = ro
for key, cell in (("S1", "C3"), ("S2", "C2"), ("S3", "C2"), ("S4", "C3"), ("S5", "C2")):
    if VOID[cell]:
        out[key]["holds"] = "VOID (the cell's invariance failed; reported, not scored)"
out["cells"] = {k: out[k]["holds"] for k in ("Q0", "S1", "S2", "S3", "S4", "S5")}
print(json.dumps({k: out[k] for k in ("Q0", "S1", "S2", "S3", "S4", "S5")}, indent=1, default=str))
(HERE / "weights_cells.json").write_text(json.dumps(out, indent=1, default=lambda z: [z.real, z.imag]
                                                     if isinstance(z, complex) else str(z)) + "\n")
