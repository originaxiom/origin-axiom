"""Independent checks of chat1's first-row claims (auditor's code).
Main's group matrices are loaded read-only from the extraction of main at 60c5470ae that first_row.py's rerun made in
the auditor's scratch (argv[1] = that frontier directory). Everything else is the auditor's own code."""
import sys, os, json, math, itertools, importlib.util, pathlib
import numpy as np
from scipy.optimize import minimize

out = {}
rng = np.random.default_rng(2026)

def R_np(t, K=60):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])

# ---------------------------------------------------------------- 1. the bound, in C^2, C^3, C^5
def sig(w): return abs(w @ w) / np.vdot(w, w).real
def ov(u, v): return abs(np.vdot(u, v)) ** 2 / (np.vdot(u, u).real * np.vdot(v, v).real)
def bound(su, sv): return 0.5 * (1 + su * sv + math.sqrt(max(0, 1 - su * su) * max(0, 1 - sv * sv)))
worst = {}
for n in (2, 3, 5):
    w = -1
    for _ in range(40000):
        u = rng.normal(size=n) + 1j * rng.normal(size=n); v = rng.normal(size=n) + 1j * rng.normal(size=n)
        if rng.random() < 0.5:   # bias towards structured pairs: isotropic-ish against real-ish
            x, y = np.linalg.qr(rng.normal(size=(n, n)))[0][:, :2].T
            u = (x + 1j * y) / math.sqrt(2) + 10 ** rng.uniform(-6, 0) * u
            v = rng.normal(size=n) + 10 ** rng.uniform(-6, 0) * v
        w = max(w, ov(u, v) - bound(sig(u), sig(v)))
    def neg(p):
        u = p[:n] + 1j * p[n:2 * n]; v = p[2 * n:3 * n] + 1j * p[3 * n:]
        if np.vdot(u, u).real < 1e-12 or np.vdot(v, v).real < 1e-12: return 0.0
        return -(ov(u, v) - bound(sig(u), sig(v)))
    adv = max(-minimize(neg, rng.normal(size=4 * n), method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-12, "fatol": 1e-15}).fun for _ in range(60))
    worst[f"C{n}"] = {"random_max_excess": float(w), "adversarial_max_excess": float(adv)}
out["bound"] = worst

# ---------------------------------------------------------------- 2. T-NORM: weight kappa on the k mode, against e_k
p = (1 - 0.3092) * (1 - 0.02248)
tn = {}
for t in (1j, 2j, 0.7j):
    R = R_np(t); ek = np.array([0, 0, 1.0])
    for kap in (1.0, 2.0, p / (1 - p)):
        G = np.diag([1, 1, kap])
        val = abs(R.conj() @ G @ ek) ** 2 / ((R.conj() @ G @ R).real * (ek @ G @ ek))
        tn[f"tau={t} kappa={kap:.4f}"] = [float(val), kap / (1 + kap)]
out["TNORM_kappa_over_1_plus_kappa"] = tn
out["TNORM_kappa_for_0.6753"] = p / (1 - p)
# the cap in a non-compatible metric: max over real v of the G-normalised overlap with R, at tau = i, kappa = 2.08
R = R_np(1j); G = np.diag([1, 1, p / (1 - p)])
best = 0
for _ in range(20000):
    v = rng.normal(size=3); best = max(best, abs(R.conj() @ G @ v) ** 2 / ((R.conj() @ G @ R).real * (v @ G @ v)))
out["cap_in_weighted_metric_tau_i_max_real_overlap"] = float(best)

# ---------------------------------------------------------------- 3. F5's logic on B1649's closed form, and the convention
def cross(R): return np.array([[0, -R[2], R[1]], [R[2], 0, -R[0]], [-R[1], R[0], 0]])
def Yc(s, R):
    a = np.array(s[1:]); return np.outer(a, R) + np.outer(R, a) - (a @ R) * np.eye(3) + s[0] * cross(R)
def null_right(M):
    W, s, Vh = np.linalg.svd(M); return Vh.conj()[-1], s
def null_left(M):
    W, s, Vh = np.linalg.svd(M); return W[:, -1], s
res = {"two_sided_kernel_max": 0.0, "Ue1_right_right_dev": 0.0, "Ue1_left(e)_right(nu)": 0.0, "Ue1_left_left_dev": 0.0}
for t in (1j, 0.3 + 1.1j, -0.5 + math.sqrt(3) / 2 * 1j):
    R = R_np(t); Rh = R / np.linalg.norm(R)
    for _ in range(10):
        c = lambda n: rng.normal(size=n) + 1j * rng.normal(size=n)
        Ye = Yc(c(4), R); YD = Yc(c(4), R); Mr = c(9).reshape(3, 3); Mr = Mr + Mr.T + 4 * np.eye(3)
        Mn = Yc(np.r_[0, c(3)], R) - YD.T @ np.linalg.inv(Mr) @ YD; Mn = (Mn + Mn.T) / 2
        res["two_sided_kernel_max"] = max(res["two_sided_kernel_max"], np.linalg.norm(Ye @ R) / np.linalg.norm(Ye), np.linalg.norm(R @ Ye) / np.linalg.norm(Ye))
        ve_r, _ = null_right(Ye); vn_r, _ = null_right(Mn); ve_l, _ = null_left(Ye); vn_l, _ = null_left(Mn)
        res["Ue1_right_right_dev"] = max(res["Ue1_right_right_dev"], abs(abs(np.vdot(ve_r, vn_r)) - 1))
        res["Ue1_left_left_dev"] = max(res["Ue1_left_left_dev"], abs(abs(np.vdot(ve_l, vn_l)) - 1))
        res["Ue1_left(e)_right(nu)"] = max(res["Ue1_left(e)_right(nu)"], abs(np.vdot(ve_l, vn_r)))
out["F5_logic"] = {k: float(v) for k, v in res.items()}

# ---------------------------------------------------------------- 4. main's group: frames, the post hoc sign classes, the cap's reach
FRONT = pathlib.Path(sys.argv[1]); os.environ["OA_FRONTIER"] = str(FRONT)
spec = importlib.util.spec_from_file_location("cp", FRONT / "B1611_is_cp_violation_forced_on_the_weave" / "verification" / "cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
TB = cp.TB
AL = cp.restrict(cp.W.ML, TB); AR = cp.restrict(cp.W.MR, TB); ARL = cp.restrict(cp.W.MR @ cp.W.ML, TB)
ARRL = cp.restrict(cp.W.MR @ cp.W.MR @ cp.W.ML, TB)
G = cp.Group([cp.W.ML, cp.W.MR]); GT = [cp.restrict(M, TB) for M in G.els]
out["group_order"] = len(GT)
def axis(A):
    mu, V = np.linalg.eig(A)
    for k in range(3):
        o = [j for j in range(3) if j != k]
        r = sorted([mu[o[0]] / mu[k], mu[o[1]] / mu[k]], key=lambda c: c.imag)
        if abs(r[0] + 1j) < 1e-8 and abs(r[1] - 1j) < 1e-8: return V[:, k], mu[k]
    raise RuntimeError("not a quarter-turn")
fL, muL = axis(AL); fR, muR = axis(AR)
# the invariant symmetric form: A^T B A = mu_axis^2 B for both generators (6 unknowns, linear)
basis = []
for a in range(3):
    for b in range(a, 3):
        E = np.zeros((3, 3), complex); E[a, b] = 1; E[b, a] = 1; basis.append(E)
rows = []
for A, mu in ((AL, muL), (AR, muR)):
    rows.append(np.array([(A.T @ E @ A - mu ** 2 * E).flatten() for E in basis]).T)
Mx = np.vstack(rows); _, s, Vh = np.linalg.svd(Mx)
out["form_nullity_singular_values_tail"] = [float(x) for x in s[-2:]]
B = sum(c * E for c, E in zip(Vh[-1].conj(), basis)); B = B / np.linalg.svd(B, compute_uv=False)[0]
out["form_unitary_dev"] = float(np.abs(np.linalg.svd(B, compute_uv=False) - 1).max())
out["form_invariant_all_96"] = float(max(np.linalg.norm(A.T @ B @ A - (A.T @ B @ A)[0, 0] / B[0, 0] * B) for A in GT))
f3 = np.linalg.svd(np.vstack([fL.conj(), fR.conj()]))[2][-1].conj()
frames = [f / np.sqrt(f @ B @ f) for f in (fL, fR, f3)]
out["frame_hermitian_orthonormal_dev"] = float(np.abs(np.array([[np.vdot(x, y) for y in frames] for x in frames]) - np.eye(3)).max())
ARLn = ARL / abs(np.linalg.det(ARL)) ** (1 / 3)
def RB(t, sg, pm=(0, 1, 2)):
    R = R_np(t); v = sum(sg[u] * R[u] * frames[pm[u]] for u in range(3)); return v / np.linalg.norm(v)
def eig_defect(t, sg): v = RB(t, sg); return 1 - abs(np.vdot(v, ARLn @ v))
signs = [(1, s2, s3) for s2 in (1, -1) for s3 in (1, -1)]
ph = {}
w = complex(-0.5, math.sqrt(3) / 2)
for sg in signs:
    best = (9, None)
    for x0 in np.linspace(-1.9, 1.9, 39):
        for y0 in (0.35, 0.6, 0.9, 1.3, 2.0, 3.0):
            f = lambda p: eig_defect(complex(p[0], max(p[1], 0.05)), sg)
            r = minimize(f, [x0, y0], method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-16, "maxiter": 3000})
            if r.fun < best[0]: best = (r.fun, complex(r.x[0], max(r.x[1], 0.05)))
    ph[str(sg)] = {"min_defect": float(best[0]), "argmin_tau": [best[1].real, best[1].imag],
                   "defect_at_omega": float(eig_defect(w, sg)), "defect_at_omega+1": float(eig_defect(w + 1, sg)),
                   "defect_at_omega-1": float(eig_defect(w - 1, sg))}
out["posthoc_RL_eigenline_search"] = ph
# RL's eigenvalue ratios (elliptic/order-3?) and W68 G2: R(omega) in the units' basis against (-omega, 1, omega^2)
ell = np.array([-w, 1, w * w]); Rw = R_np(w)
out["R(omega)_vs_W68_l_omega_projdist"] = float(np.linalg.norm(np.cross(Rw, ell)) / (np.linalg.norm(Rw) * np.linalg.norm(ell)))
# the cap's reach over the 13 real axes, per sign class and labelling, on first_row's grid
GRID = {"i": 1j, "1.5i": 1.5j, "2i": 2j, "4i": 4j, "omega": w, "0.3+1.1i": 0.3 + 1.1j, "-0.2+0.9i": -0.2 + 0.9j, "0.45+2.5i": 0.45 + 2.5j}
axes = []
for A in GT:
    mu, V = np.linalg.eig(A)
    for k in range(3):
        vv = V[:, k] / np.linalg.norm(V[:, k])
        if sum(abs(mu[j] - mu[k]) < 1e-7 for j in range(3)) == 1 and abs(abs(vv @ B @ vv) - 1) < 1e-9:
            if all(abs(abs(np.vdot(vv, a)) - 1) > 1e-8 for a in axes): axes.append(vv)
out["n_real_axes"] = len(axes)
reach = {}
for pm in itertools.permutations(range(3)):
    for sg in signs:
        reach[f"{pm}{sg}"] = sum(1 for t in GRID.values() if abs(max(ov(RB(t, sg, pm), a) for a in axes) - 0.5) < 1e-9)
out["cap_reached_count_per_frame_(of_8_tau)"] = reach
print(json.dumps(out, indent=1, default=str))
