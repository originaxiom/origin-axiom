"""LIFT (sealed: PREREGISTRATION_LIFT.md), chat1, 2026-10-15: does main's boundary-class lift (B1654) survive in the
thread frame's rank-two cells, and how large is it?

B1654 (main, PROVED): under the canonical end condition P4 the residue triplet of B1644's coupling becomes
u_r = sqrt(2 pi L + c_r(tau)) R_r, L = log(1/eps), with c_r the finite part of the channel-r boundary class's norm; under
C0's P4' (equal framed data) u = R and the zero stays. Here R -> u in the thread frame's coupling,
G(X, Y; v) = (v.Y)X + (v.X)Y - (X.Y)v, evaluated pointwise along each thread's closed geodesic:
  - c~_r = c_r - pi log Im tau (the cutoff in the unit-area coordinate; modular covariant: S and T permute the channels,
    and the common shift drops); c_r by main's own route-A code, read from main at 1d2dac43d, on a Chebyshev grid;
  - W72's R is -2 pi times B1654's (units i, j, k <-> channels th2, th4, th3), so delta = c~ o R in W72's basis with
    c~ ordered (c~_2, c~_4, c~_3);
  - u / sqrt(2 pi L) = R + eps delta + O(eps^2), eps = 1/(4 pi L), so the first-order lift of a rank-two cell is
    kappa = |u0^H (A Y_delta B^T) v0| / sigma_max(A Y_R B^T), u0 and v0 the null pair of A Y_R B^T; and m1/m3 -> eps kappa.
Cells: C1 = (3/2, 3/2) h 5/2; C2 = (3/2, 7/2) h 9/2 and C3 = (-1/2, 7/2) h 5/2 under the completions E4.F (c = 0),
theta^2 (c = beta) and H-ORTH; every Lyndon word of length 2..8; masses K_L^-1/2 Y (K_R^-1/2)^T.

Run once:  python3 -B lift_cells.py > lift_cells_run.txt 2>&1   (writes lift_cells.json beside itself)
"""
import importlib.util, io, json, math, os, pathlib, subprocess, sys, tarfile, tempfile, time
from fractions import Fraction
import numpy as np
import mpmath as mp
from numpy.polynomial import chebyshev as Ch
from scipy.stats import spearmanr

t0 = time.time()
HERE = pathlib.Path("<repo>/relays/chat1_2026-10-14_step3")
OUTDIR = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
SMC = "87cf7f55111ec1f4019f302ffaa578376a9143e6"
MAIN = "1d2dac43d443538769fbf04ea393079623346f65"
TMP = pathlib.Path(tempfile.mkdtemp(prefix="lift_sm_"))
blob = subprocess.run(["git", "-C", str(REPO), "archive", SMC, "docs/dossiers/the_weave_2026-10-07", "frontier"],
                      check=True, capture_output=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP, filter="data")
# main's B1654 route A (thetas, cA, R_A), unchanged, read from main and loaded as a module
src = subprocess.run(["git", "-C", str(REPO), "show",
                      f"{MAIN}:frontier/B1654_the_norm_of_the_boundary_class/verification/the_norm_of_the_boundary_class.py"],
                     check=True, capture_output=True, text=True).stdout
(TMP / "b1654_routeA.py").write_text(src[:src.index("# ---------------------------------------------------------------- route B")])
spec = importlib.util.spec_from_file_location("b1654_routeA", TMP / "b1654_routeA.py")
BA = importlib.util.module_from_spec(spec); spec.loader.exec_module(BA)
DOSS = TMP / "docs" / "dossiers" / "the_weave_2026-10-07"
sys.path.insert(0, str(DOSS))
os.chdir(DOSS)
import the_surface_yukawa as SY  # noqa: E402
SU, RC = SY.SU, SY.RC
mp.mp.dps = 40
out = {"sm_seat_commit": SMC, "main_commit": MAIN, "status": "LIFT, sealed (PREREGISTRATION_LIFT.md); one run"}
print("modules loaded", round(time.time() - t0, 1), file=sys.stderr, flush=True)
K32, K72, KM12 = Fraction(3, 2), Fraction(7, 2), Fraction(-1, 2)
UNIT8 = {l: SY.E8[l] - 8 for l in SY.LINES}


def save():
    (OUTDIR / "glue3.json").write_text(json.dumps(out, indent=1, default=lambda z: [z.real, z.imag]
                                                     if isinstance(z, complex) else str(z)) + "\n")


# ------------------------------------------------------------------ the forms (as theta2_completion.py builds them)
resid = {}
F32, FM12 = [], []
for name, u in SY.MATTER:
    terms, r, line = SY.best_section(u, K32); F32.append(SY.to_series(terms, SY.E8)); resid[f"{name} 3/2"] = r
    terms, r, line = SY.best_section(u, KM12); FM12.append(SY.to_series(terms, SY.E8)); resid[f"{name} -1/2"] = r
terms, r, line = SY.best_section((0, 1, 0), KM12); Rser = SY.to_series(terms, SY.E8); resid["R"] = r
fbest = None
for line in SY.LINES:
    terms, r = RC.solve((0, 0, 0), K72, line)
    if fbest is None or r < fbest[1]: fbest = (terms, r, line)
fser = SY.to_series(fbest[0], SY.E8); resid["f 7/2"] = fbest[1]
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

CAP = SY.CAP8 // 8
sig = lambda m, p: sum(d ** p for d in range(1, m + 1) if m % d == 0)
E4 = {0: mp.mpf(1)}; E4.update({8 * m: mp.mpf(240 * sig(m, 3)) for m in range(1, CAP + 1)})
E2 = {0: mp.mpf(1)}; E2.update({8 * m: mp.mpf(-24 * sig(m, 1)) for m in range(1, CAP + 1)})


def serre(X, k):
    D = {key: (mp.mpf(key[1]) / 8) * a for key, a in X.items()}
    return SY.add((1, D), (-mp.mpf(k.numerator) / (12 * k.denominator), SY.scal_vec(E2, X)))


EI = ("e_i", 1)
E4F = [SY.scal_vec(E4, F) for F in FM12]
beta, beta_mp = [], []
for j, l in enumerate(("e_i", "v+", "v-")):
    th2 = serre(serre(FM12[j], KM12), K32)
    u2 = th2.get((l, UNIT8[l]))
    th2 = {k: v / u2 for k, v in th2.items()}
    b_mp = (th2.get(EI, 0) - E4F[j].get(EI, 0)) / fser.get(EI)
    beta_mp.append(b_mp); beta.append(complex(b_mp))
out["Q(d) beta (theta^2 = E4 F + beta f)"] = beta
q_beta = float(max(abs(b - t) / abs(t) for b, t in zip(beta_mp, (-224, -4, -112))))   # compared in mpmath

ev = SY.np_eval
F32n, FM12n, RBn = [ev(s) for s in F32], [ev(s) for s in FM12], [ev(s) for s in E4F + [fser]]
Rn, h5n, h9n = ev(Rser), ev(h5), ev(h9)
print("series ready", round(time.time() - t0, 1), file=sys.stderr, flush=True)

# ------------------------------------------------------------------ c~ on a Chebyshev grid, by main's route A
X0, X1, Y0, Y1 = -0.5, 0.5, 0.86, 4.5
NX, NY = 20, 32


def ctil_direct(tau):
    """(c~_2, c~_4, c~_3): channels th2, th4, th3 = units i, j, k; c~ = c - pi log Im tau"""
    return np.array([0.3 + 0.1 * tau.real, -0.2 + 0.05 * tau.imag, 0.5])  # GLUE3 STUB: chat1's fake, non-covariant, unrelated to c


def cnodes(n, a, b):
    x = np.cos(np.pi * (np.arange(n) + 0.5) / n)
    return 0.5 * (b - a) * x + 0.5 * (b + a), x


xs, ux = cnodes(NX, X0, X1); ys, uy = cnodes(NY, Y0, Y1)
V = np.array([[ctil_direct(complex(x, y)) for y in ys] for x in xs])               # (NX, NY, 3)
Tx, Ty = Ch.chebvander(ux, NX - 1), Ch.chebvander(uy, NY - 1)
Acoef = np.linalg.solve(Tx, V.reshape(NX, -1)).reshape(NX, NY, 3)
CF = np.linalg.solve(Ty, Acoef.transpose(1, 0, 2).reshape(NY, -1)).reshape(NY, NX, 3).transpose(1, 0, 2)
print("c~ grid built", round(time.time() - t0, 1), file=sys.stderr, flush=True)


def ctil(T):
    T = np.asarray(T)
    if np.any(T.real < X0 - 1e-12) or np.any(T.real > X1 + 1e-12) or np.any(T.imag < Y0) or np.any(T.imag > Y1):
        raise ValueError("outside the c~ grid")
    tx = Ch.chebvander((2 * T.real - (X1 + X0)) / (X1 - X0), NX - 1)
    ty = Ch.chebvander((2 * T.imag - (Y1 + Y0)) / (Y1 - Y0), NY - 1)
    return np.einsum("na,nb,abc->nc", tx, ty, CF)                                   # (N, 3)


rng0 = np.random.default_rng(1654)
qa = 0.0
for _ in range(20):
    x = rng0.uniform(-0.5, 0.5); y = rng0.uniform(math.sqrt(1 - x * x), 4.4); tau = complex(x, y)
    qa = max(qa, float(np.max(np.abs(ctil_direct(tau) - ctil(np.array([tau]))[0]))))
out["Q(a) c~ interpolation, worst absolute error at 20 random points of F"] = qa
save()


# ------------------------------------------------------------------ pointwise coupling and integrands
def dot(X, Y):
    return np.sum(X * Y, axis=1)


def Gp(X, Y, v):
    return dot(v, Y)[:, None] * X + dot(v, X)[:, None] * Y - dot(X, Y)[:, None] * v


LS = (10.0, 100.0, 1000.0, 1.0e7)
VKEYS = ("R", "delta", "delta+R", "delta+e3") + tuple(f"L{int(L)}" for L in LS)
E3 = np.array([0.0, 0.0, 1.0])                                  # channel th3 (unit k) shifted by 1: a channel-dependent control
PAIRS = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]


def vectors(T, c):
    Rv = Rn(T)
    vs = {"R": Rv, "delta": c * Rv, "delta+R": (c + 1.0) * Rv, "delta+e3": (c + E3) * Rv}
    for L in LS:
        vs[f"L{int(L)}"] = np.sqrt(1 + c / (2 * math.pi * L)) * Rv
    return vs


def integrands(T, c):
    y = T.imag
    a32 = [f(T) for f in F32n]; am = [f(T) for f in FM12n]; ar = [f(T) for f in RBn]
    v5, v9 = np.conj(h5n(T)), np.conj(h9n(T))
    vs = vectors(T, c)
    res = {}
    for i in range(3):
        for j in range(3):
            res[("K32", i, j)] = dot(a32[i], np.conj(a32[j])) * y ** 1.5
            res[("KM12", i, j)] = dot(am[i], np.conj(am[j])) * y ** -0.5
    for i in range(4):
        for j in range(4):
            res[("K72", i, j)] = dot(ar[i], np.conj(ar[j])) * y ** 3.5
    for vk, v in vs.items():
        for p in PAIRS:
            res[("Y1", vk) + p] = dot(Gp(a32[p[0]], a32[p[1]], v), v5) * y ** 2.5
        for a in range(3):
            for b in range(4):
                res[("Y2", vk, a, b)] = dot(Gp(a32[a], ar[b], v), v9) * y ** 4.5
                res[("Y3", vk, a, b)] = dot(Gp(am[a], ar[b], v), v5) * y ** 2.5
    return res


# Q(e): the pointwise coupling against the series coupling (v = R)
PTS = np.array([0.2 + 1.0j, 1j, -0.3 + 1.2j, 0.45 + 1.6j, 2j])
def scale(X, Y, v):
    return np.linalg.norm(X, axis=1) * np.linalg.norm(Y, axis=1) * np.linalg.norm(v, axis=1)


qe = 0.0
for (A_, B_) in ((F32[0], F32[1]), (FM12[0], E4F[2]), (FM12[2], fser), (F32[2], fser)):
    Xp, Yp, Rp = ev(A_)(PTS), ev(B_)(PTS), Rn(PTS)
    gs = ev(SY.G_series(A_, B_, Rser))(PTS)
    gp = Gp(Xp, Yp, Rp)
    qe = max(qe, float(np.max(np.linalg.norm(gs - gp, axis=1) / scale(Xp, Yp, Rp))))
out["Q(e) pointwise G against the series G, relative to |X||Y||R|"] = qe
Xp, Yp, Rp = ev(FM12[1])(PTS), ev(E4F[0])(PTS), Rn(PTS)
out["Q(e') the zero pair G(R, E4 F_i; R) pointwise, relative to |X||Y||R| (an identity, reported)"] = float(
    np.max(np.linalg.norm(Gp(Xp, Yp, Rp), axis=1) / scale(Xp, Yp, Rp)))


def reduce(t):
    for _ in range(10000):
        t = t - round(t.real)
        if abs(t) < 1 - 1e-14:
            t = -1 / t
        else:
            return t
    raise RuntimeError("reduction did not terminate")


# Q(b): invariance of every integrand (all v) under 20 random moves, with c~ computed directly at both points
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
    A = integrands(np.array([t]), ctil_direct(t)[None, :])
    B = integrands(np.array([tg]), ctil_direct(tg)[None, :])
    fam_of = lambda k: k[0] if k[0].startswith("K") else f"{k[0]} {k[1]}"
    famscale = {}
    for k in A:
        famscale[fam_of(k)] = max(famscale.get(fam_of(k), 0.0), abs(A[k][0]), abs(B[k][0]))
    for k in A:                                  # each entry's deviation relative to its family's largest entry here
        dev = float(abs(A[k][0] - B[k][0]) / famscale[fam_of(k)])
        inv_by[fam_of(k)] = max(inv_by.get(fam_of(k), 0.0), dev)
    ntests += 1
out["Q(b) invariance by family"] = inv_by
save()
print("controls done", round(time.time() - t0, 1), file=sys.stderr, flush=True)

# ------------------------------------------------------------------ threads
Lm = np.array([[1, 0], [1, 1]]); Rm_ = np.array([[1, 1], [0, 1]])


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
        M = M @ (Lm if ch == "L" else Rm_)
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
    vals = integrands(Tr, ctil(Tr))
    w = P / N
    S = lambda key: w * np.sum(vals[key])
    r = {"y_max": float(np.max(Tr.imag)),
         "K32": np.array([[S(("K32", i, j)) for j in range(3)] for i in range(3)]),
         "KM12": np.array([[S(("KM12", i, j)) for j in range(3)] for i in range(3)]),
         "K72": np.array([[S(("K72", i, j)) for j in range(4)] for i in range(4)])}
    for vk in VKEYS:
        Y1 = np.zeros((3, 3), dtype=complex)
        for p in PAIRS:
            Y1[p[0], p[1]] = Y1[p[1], p[0]] = S(("Y1", vk) + p)
        r[f"Y1 {vk}"] = Y1
        r[f"Y2x {vk}"] = np.array([[S(("Y2", vk, a_, b_)) for b_ in range(4)] for a_ in range(3)])
        r[f"Y3x {vk}"] = np.array([[S(("Y3", vk, a_, b_)) for b_ in range(4)] for a_ in range(3)])
    return r


def inv_sqrt(K):
    ev_, U = np.linalg.eigh(K)
    if not np.all(np.isfinite(ev_)) or ev_.min() <= 0:
        return None
    return U @ np.diag(ev_ ** -0.5) @ U.conj().T


def cell_mats(r, cell, comp, vk):
    """(K_L, Y, K_R) for a cell, a completion and a coupling vector"""
    if cell == "C1":
        return r["K32"], r[f"Y1 {vk}"], r["K32"]
    K = r["K72"]
    c = {"E4": np.zeros(3, dtype=complex), "THETA2": np.array(beta, dtype=complex), "ORTH": -K[:3, 3] / K[3, 3]}[comp]
    P3 = np.hstack([np.eye(3), c.reshape(3, 1)])
    KR = P3 @ K @ P3.conj().T
    if cell == "C2":
        return r["K32"], r[f"Y2x {vk}"] @ P3.T, KR
    return r["KM12"], r[f"Y3x {vk}"] @ P3.T, KR


CELLS = [("C1", None), ("C2", "E4"), ("C2", "THETA2"), ("C2", "ORTH"), ("C3", "E4"), ("C3", "THETA2"), ("C3", "ORTH")]
R2CELLS = ("C2/E4", "C3/E4", "C3/THETA2", "C3/ORTH")


def analyse(r):
    res = {}
    for cell, comp in CELLS:
        name = cell if comp is None else f"{cell}/{comp}"
        KL, YR, KR = cell_mats(r, cell, comp, "R")
        A, B = inv_sqrt(KL), inv_sqrt(KR)
        if A is None or B is None:
            res[name] = {"pd": False}; continue
        MR = A @ YR @ B.T
        U, s, Vh = np.linalg.svd(MR)
        o = np.argsort(s); s3 = s[o[2]]
        row = {"pd": True, "m2/m3": float(s[o[1]] / s3), "m1/m3": float(s[o[0]] / s3)}
        row["rank 2"] = bool(row["m1/m3"] < 1e-10)
        u0, v0 = U[:, o[0]], Vh[o[0], :].conj()
        if name in R2CELLS:                      # the first-order lift of a null pair; meaningless at rank three
            for vk, key in (("delta", "kappa"), ("delta+R", "kappa (delta + R)"), ("delta+e3", "kappa (delta + e3)")):
                Md = A @ cell_mats(r, cell, comp, vk)[1] @ B.T
                row[key] = float(abs(u0.conj() @ Md @ v0) / s3)
        for L in LS:
            sl = np.sort(np.linalg.svd(A @ cell_mats(r, cell, comp, f"L{int(L)}")[1] @ B.T, compute_uv=False))
            row[f"L={int(L)}: m1/m3"] = float(sl[0] / sl[2]); row[f"L={int(L)}: m2/m3"] = float(sl[1] / sl[2])
            row[f"L={int(L)}: 4 pi L m1/m3"] = float(4 * math.pi * L * sl[0] / sl[2])
        res[name] = row
    return res


words = ["LR", "LLR"]  # GLUE3: two threads only
per = {}
for w in words:
    r256, r384 = raw(w, 256), raw(w, 384)
    a256, a384 = analyse(r256), analyse(r384)
    row = {"y_max": r384["y_max"]}
    for name in a384:
        x, z = a384[name], a256[name]
        if not (x["pd"] and z["pd"]):
            row[name] = dict(x, admitted=False); continue
        keys = ["m2/m3"] + (["kappa"] if name in R2CELLS else ["m1/m3"])
        agree = max(abs(x[k] - z[k]) / max(abs(x[k]), 1e-300) for k in keys)
        row[name] = dict(x, **{"N256 vs N384": agree, "admitted": bool(r384["y_max"] <= 3.0 and agree <= 1e-5)})
    per[w] = row
    print(w, {n: (round(row[n].get("m2/m3", float("nan")), 5), row[n].get("rank 2"), "%.4g" % (row[n].get("kappa") or float("nan")))
              for n in row if n != "y_max"}, flush=True)
out["per thread"] = per
save()

# ------------------------------------------------------------------ Q(c): the unlifted cells against the earlier runs
t2 = json.loads((HERE / "theta2_completion.json").read_text())["per thread"]
wc = json.loads((HERE / "weights_cells.json").read_text())["per thread"]
MAP = {"C2/E4": "H-E4 C2", "C2/THETA2": "H-THETA2 C2", "C2/ORTH": "H-ORTH C2",
       "C3/E4": "H-E4 C3", "C3/THETA2": "H-THETA2 C3", "C3/ORTH": "H-ORTH C3"}
qc = 0.0
for w in words:
    if wc[w]["C1"]["admitted"]:
        for k in ("m2/m3", "m1/m3"):
            d = abs(per[w]["C1"][k] - wc[w]["C1"][k])
            qc = max(qc, min(d / abs(wc[w]["C1"][k]) / 1e-5, d / 1e-10))
    for name, key in MAP.items():
        if t2[w][key]["admitted"]:
            ks = ("m2/m3",) if t2[w][key]["rank 2"] else ("m2/m3", "m1/m3")
            for k in ks:
                d = abs(per[w][name][k] - t2[w][key][k])
                qc = max(qc, min(d / abs(t2[w][key][k]) / 1e-5, d / 1e-10))
out["Q(c) unlifted cells against the earlier runs: worst of min(rel/1e-5, abs/1e-10); holds below 1"] = qc
out["Q"] = {"(a)": qa, "(b) worst": max(inv_by.values()), "(c)": qc, "(d)": q_beta, "(e)": qe,
            "holds": bool(qa < 1e-8 and max(inv_by.values()) < 1e-8 and qc < 1 and q_beta < 1e-20 and qe < 1e-12)}
save()

# ------------------------------------------------------------------ the cells
adm = lambda name: [w for w in words if per[w][name].get("admitted")]
l1 = {n: [w for w in adm(n) if not per[w][n]["rank 2"]] for n in R2CELLS}
out["L1"] = {"threads in a rank-2 cell that are not rank 2 under P4'": l1, "admitted": {n: len(adm(n)) for n in R2CELLS},
             "largest P4' m1/m3 over admitted": {n: max((per[w][n]["m1/m3"] for w in adm(n)), default=None) for n in R2CELLS},
             "holds": bool(all(adm(n) for n in R2CELLS) and not any(l1.values()))}
l2 = {n: [w for w in adm(n) if not per[w][n]["kappa"] > 1e-6] for n in R2CELLS}
out["L2"] = {"threads with kappa <= 1e-6": l2, "least kappa": {n: min(((per[w][n]["kappa"], w) for w in adm(n)), default=None)
                                                              for n in R2CELLS},
             "holds": bool(all(adm(n) for n in R2CELLS) and not any(l2.values()))}
dev3 = {n: max(((abs(per[w][n]["L=10000000: 4 pi L m1/m3"] - per[w][n]["kappa"]) / per[w][n]["kappa"], w) for w in adm(n)
                if per[w][n]["kappa"] > 0), default=None) for n in R2CELLS}
out["L3"] = {"worst |4 pi L m1/m3 - kappa| / kappa at L = 1e7": dev3,
             "read-out: the same at L = 1000": {n: max(((abs(per[w][n]["L=1000: 4 pi L m1/m3"] - per[w][n]["kappa"])
                                                         / per[w][n]["kappa"], w) for w in adm(n) if per[w][n]["kappa"] > 0),
                                                       default=None) for n in R2CELLS},
             "holds": bool(all(d is not None and d[0] < 0.01 for d in dev3.values()))}
root = {n: per["LR"][n].get("kappa") for n in R2CELLS}
out["L4"] = {"the root's kappa": root, "holds": bool(all(per["LR"][n].get("admitted") and 0.01 <= root[n] <= 10 for n in R2CELLS))}
rootrows = [per["LR"][n] for n in R2CELLS]
out["Q(f) controls at the root: a common shift leaves kappa (identity); a channel shift changes it"] = {
    "common shift, worst relative change": max(abs(x["kappa (delta + R)"] - x["kappa"]) / x["kappa"] for x in rootrows),
    "channel shift, least relative change": min(abs(x["kappa (delta + e3)"] - x["kappa"]) / x["kappa"] for x in rootrows)}
out["cells"] = {k: out[k]["holds"] for k in ("Q", "L1", "L2", "L3", "L4")}
save()

# ------------------------------------------------------------------ read-outs (no prior)
ro = {}
TARGET = {"up m_u/m_c": 0.00123 / 0.62, "lepton m_e/m_mu": 0.00048307 / 0.101766, "down m_d/m_s": 0.00267 / 0.05316}
for n in R2CELLS:
    ws = adm(n)
    ro[f"{n}: kappa range over admitted"] = [min(per[w][n]["kappa"] for w in ws), max(per[w][n]["kappa"] for w in ws)] if ws else None
    if len(ws) > 3:
        ro[f"{n}: Spearman(y_max, ln kappa)"] = float(spearmanr([per[w]["y_max"] for w in ws],
                                                                [math.log(max(per[w][n]["kappa"], 1e-300)) for w in ws]).correlation)
    rr = per["LR"][n]
    ro[f"{n}: the root"] = {k: rr[k] for k in rr if k in ("m2/m3", "kappa", "L=10: 4 pi L m1/m3", "L=100: 4 pi L m1/m3",
                                                         "L=1000: 4 pi L m1/m3", "L=10000000: 4 pi L m1/m3", "admitted")}
    ro[f"{n}: the L the root would need for m1/m2 (no prior; data HZ2021 at M_Z)"] = {
        s: rr["kappa"] / (4 * math.pi * t * rr["m2/m3"]) for s, t in TARGET.items()}
ro["the root's L-free kappa ratios"] = {f"{a} / {b}": root[a] / root[b] for a in R2CELLS for b in R2CELLS
                                       if a < b and root[a] and root[b]}
for n in ("C1", "C2/THETA2", "C2/ORTH"):
    rr = per["LR"][n]
    ro[f"{n} (rank 3): the root's m1/m3 unlifted and at L = 10, 100"] = [rr["m1/m3"], rr["L=10: m1/m3"], rr["L=100: m1/m3"]]
out["readouts"] = ro
out["seconds"] = round(time.time() - t0, 1)
print(json.dumps({k: out[k] for k in ("Q", "L1", "L2", "L3", "L4", "readouts")}, indent=1, default=str))
save()
