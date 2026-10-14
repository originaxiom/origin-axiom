#!/usr/bin/env python3
"""The first-row check (chat1, 2026-10-14; PREREGISTRATION.md, sealed at 53b7f3f88, sha256 81ca4a63...).

Can the lepton obstacle (B1649 §3: a trivial PMNS first row at leading order) be escaped at leading order?

  Q0  controls: B1612's TM1 column; R isotropic; the units' frame in B1612's coordinates
  F1  the bound |<u,v>|^2/(|u|^2|v|^2) <= (1 + s_u s_v + sqrt((1-s_u^2)(1-s_v^2)))/2, s = |w.w|/|w|^2
  F2  the invariant symmetric form B on T (unique, unitary up to scale)
  F3  TM1's neutrino line real; RL's basis (real, isotropic, isotropic); the 2/3 on the real one
  F4  the cap: max over real v of |<R^, v>|^2 = 1/2; TM1's line against R^ <= 1/2 in all 24 frames
  F5  one fibre, every neutrino operator built on the puncture's couplings: |U_e1| = 1
  F6  Reading B (conditional): nu_1 = e_t, |U_e1|^2 = |R_t|^2/|R|^2 <= 1/2; both sectors: |U_e1| = 1

Main's banked modules are read-only, extracted by `git archive` from main at the pinned commit into a temporary
directory. Run once:   python3 -B first_row.py > run.txt 2>&1     (writes first_row.json beside itself)
"""
import io, itertools, json, math, os, pathlib, subprocess, sys, tarfile, tempfile, time, importlib.util
import numpy as np
import mpmath as mp
from scipy.optimize import minimize

t0 = time.time()
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
MAIN = "60c5470ae1747e5bd31a1a889ce38739791e0af3"
ARCS = ["frontier/B1600_the_weave_verified", "frontier/B1610_the_hands_on_the_founding_torsor",
        "frontier/B1611_is_cp_violation_forced_on_the_weave", "frontier/B1612_the_mixing_patterns_the_weave_fixes",
        "frontier/B1642_the_golden_coupling_as_the_zero_modes_residue", "frontier/B1649_the_kernel_at_the_puncture"]
TMP = pathlib.Path(tempfile.mkdtemp(prefix="first_row_main_"))
blob = subprocess.run(["git", "-C", str(REPO), "archive", MAIN] + ARCS, check=True, capture_output=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP)
FRONTIER = TMP / "frontier"
os.environ["OA_FRONTIER"] = str(FRONTIER)
out = {"main_commit": MAIN, "arcs": ARCS}
rng = np.random.default_rng(20261014)

# ------------------------------------------------------------------ main's modules
spec = importlib.util.spec_from_file_location("cp", FRONTIER / "B1611_is_cp_violation_forced_on_the_weave" / "verification" / "cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
TB = cp.TB
AL = cp.restrict(cp.W.ML, TB); AR = cp.restrict(cp.W.MR, TB)
A_RL = cp.restrict(cp.W.MR @ cp.W.ML, TB)                    # B1612's word order: "RL" = MR @ ML
A_RRL = cp.restrict(cp.W.MR @ cp.W.MR @ cp.W.ML, TB)
G = cp.Group([cp.W.ML, cp.W.MR]); GT = [cp.restrict(M, TB) for M in G.els]

B1642 = FRONTIER / "B1642_the_golden_coupling_as_the_zero_modes_residue" / "verification" / "residue_coupling.py"
ns = {"__file__": str(B1642)}
exec(compile(open(B1642).read().split("rng = np.random.default_rng(1642)")[0], "residue_coupling_defs", "exec"), ns)
src49 = (FRONTIER / "B1649_the_kernel_at_the_puncture" / "verification" / "the_kernel_at_the_puncture.py").read_text()


def grab(src, name):
    i = src.index(f"def {name}(")
    j = src.index("\ndef ", i + 1)
    return src[i:j]


ns["ONE"] = mp.eye(2); ns["BLOCK_OF_UNIT"] = [1, 0, 2]
exec(grab(src49, "Y_of"), ns); exec(grab(src49, "R_of"), ns)      # B1649's Y_of and R_of, verbatim
Y_of, R_of = ns["Y_of"], ns["R_of"]
mp.mp.dps = 30


def R_np(t, K=40):                                                # B1645's closed form (numpy series)
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])


def Y_formula(a, R):                                              # B1645: Y(a) = a R^T + R a^T - (a.R) 1
    return np.outer(a, R) + np.outer(R, a) - np.dot(a, R) * np.eye(3)


def to_np(Y):
    return np.array([[complex(Y[a, b]) for b in range(3)] for a in range(3)])


GRID = [1j, 1.5j, 2j, 4j, complex(-0.5, math.sqrt(3) / 2), 0.3 + 1.1j, -0.2 + 0.9j, 0.45 + 2.5j]
GRID_NAMES = ["i", "1.5i", "2i", "4i", "omega", "0.3+1.1i", "-0.2+0.9i", "0.45+2.5i"]
UNITS = ["i", "j", "k"]


def sig(w, Bf=None):
    """sigma = |w.w|/|w|^2 (Bf: the bilinear form's matrix; identity in the units' basis)"""
    w = np.asarray(w, dtype=complex)
    bb = w @ w if Bf is None else w @ Bf @ w
    return float(abs(bb) / np.vdot(w, w).real)


def bound(su, sv):
    return 0.5 * (1 + su * sv + math.sqrt(max(0.0, 1 - su * su) * max(0.0, 1 - sv * sv)))


def ratio(u, v):
    return float(abs(np.vdot(u, v)) ** 2 / (np.vdot(u, u).real * np.vdot(v, v).real))


def eig_groups(A, tol=1e-7):
    ev, V = np.linalg.eig(A); groups = []
    for e, v in zip(ev, V.T):
        for g in groups:
            if abs(g[0] - e) < tol: g[1].append(v); break
        else:
            groups.append([e, [v]])
    return [(e, np.linalg.qr(np.array(vs).T)[0]) for e, vs in groups]


def nondegenerate_line(A):
    gs = eig_groups(A)
    lines = [Wv[:, 0] for e, Wv in gs if Wv.shape[1] == 1]
    return lines[0] if len(gs) == 2 and len(lines) == 1 else None


def cyclic_basis(A):
    gs = eig_groups(A)
    return np.hstack([Wv for e, Wv in gs]) if len(gs) == 3 else None


# ------------------------------------------------------------------ F2: the invariant symmetric form on T
SYM = []
for a in range(3):
    for b in range(a, 3):
        E = np.zeros((3, 3), dtype=complex); E[a, b] = 1; E[b, a] = 1; SYM.append(E)
SYMM = np.array([E.flatten() for E in SYM]).T                      # 9 x 6


def phi(A):
    """the map B -> A^T B A on symmetric matrices, in the basis SYM (least squares back-projection, exact here)"""
    cols = [np.linalg.lstsq(SYMM, (A.T @ E @ A).flatten(), rcond=None)[0] for E in SYM]
    return np.array(cols).T


PL, PR = phi(AL), phi(AR)
sols = []
for lL in np.linalg.eigvals(PL):
    for lR in np.linalg.eigvals(PR):
        Mst = np.vstack([PL - lL * np.eye(6), PR - lR * np.eye(6)])
        _, s, Vh = np.linalg.svd(Mst)
        for k in range(6):
            if s[5 - k] < 1e-9:
                c = Vh[5 - k].conj(); Bm = sum(ci * E for ci, E in zip(c, SYM)); Bm = Bm / np.linalg.norm(Bm)
                if all(abs(np.vdot(Bm.flatten(), S0.flatten())) < 1 - 1e-8 for S0 in sols):
                    sols.append(Bm)
F2 = {"n_solutions": len(sols)}
Bf = None
if sols:
    sv = np.linalg.svd(sols[0], compute_uv=False)
    F2["singular_values"] = [float(x) for x in sv]
    Bf = sols[0] / sv[0]
    F2["max_dev_from_unitary"] = float(np.abs(np.linalg.svd(Bf, compute_uv=False) - 1).max())
    F2["invariance_residual"] = float(max(np.linalg.norm(A.T @ Bf @ A - (A.T @ Bf @ A)[0, 0] / Bf[0, 0] * Bf)
                                          for A in GT) if abs(Bf[0, 0]) > 1e-6 else -1)
F2["holds"] = bool(len(sols) == 1 and F2.get("max_dev_from_unitary", 1) < 1e-9)
out["F2"] = F2

# ------------------------------------------------------------------ Q0 and F3
U_RL = cyclic_basis(A_RL); nu_TM1 = nondegenerate_line(A_RRL)
col = np.abs(U_RL.conj().T @ nu_TM1) ** 2
Q0 = {"TM1_column_sorted": sorted(float(x) for x in col),
      "TM1_column_err": float(np.abs(np.sort(col) - np.array([1 / 6, 1 / 6, 2 / 3])).max())}
Q0["R_isotropy_numpy_max"] = float(max(abs(np.dot(R_np(t), R_np(t))) / np.vdot(R_np(t), R_np(t)).real for t in GRID))
iso_mp = []
for t in GRID[:3]:
    Rm = R_of(mp.mpc(t.real, t.imag))
    iso_mp.append(float(abs(sum(x * x for x in Rm)) / sum(abs(x) ** 2 for x in Rm)))
Q0["R_isotropy_mpmath_3tau"] = iso_mp

F3 = {}
if Bf is not None:
    F3["sigma_TM1_line"] = sig(nu_TM1, Bf)
    sRL = [sig(U_RL[:, k], Bf) for k in range(3)]
    F3["sigma_RL_basis"] = sRL
    k_real = int(np.argmax(sRL))
    F3["column_entry_on_real_vector"] = float(col[k_real])
    F3["holds"] = bool(abs(F3["sigma_TM1_line"] - 1) < 1e-9 and abs(sorted(sRL)[2] - 1) < 1e-9
                       and sorted(sRL)[1] < 1e-9 and abs(col[k_real] - 2 / 3) < 1e-9)
out["F3"] = F3


# the units' frame in B1612's coordinates
def axis_of(A):
    """the sigma_B = 1 eigenline of a quarter-turn's matrix"""
    gs = eig_groups(A); best = None
    for e, Wv in gs:
        for c in range(Wv.shape[1]):
            v = Wv[:, c]; s = sig(v, Bf)
            if best is None or s > best[0]: best = (s, v)
    return best


sL, fL = axis_of(AL); sR, fR = axis_of(AR)
_, _, Vh3 = np.linalg.svd(np.vstack([fL.conj(), fR.conj()])); f3 = Vh3[-1].conj()


def phased(f):
    return f / np.sqrt(f @ Bf @ f)


fL, fR, f3 = phased(fL), phased(fR), phased(f3)
Q0["sigma_axes"] = [sL, sR, sig(f3, Bf)]
Q0["fL_dot_fR_hermitian"] = float(abs(np.vdot(fL, fR)))
Q0["frame_B_orthonormal_err"] = float(np.abs(np.array([[x @ Bf @ y for y in (fL, fR, f3)] for x in (fL, fR, f3)]) - np.eye(3)).max())
Fm = np.column_stack([fL, fR, f3])
real_struct = []
for A in (AL, AR, A_RL, A_RRL):
    Af = np.linalg.inv(Fm) @ A @ Fm
    X = Af @ np.linalg.inv(Af.conj())
    real_struct.append(float(np.abs(X - X[0, 0] * np.eye(3)).max()))
Q0["generators_real_up_to_scalar_in_frame"] = real_struct
Q0["holds"] = bool(Q0["TM1_column_err"] < 1e-9 and Q0["R_isotropy_numpy_max"] < 1e-12 and max(iso_mp) < 1e-25
                   and Q0["fL_dot_fR_hermitian"] < 1e-9 and abs(Q0["sigma_axes"][2] - 1) < 1e-9)
out["Q0"] = Q0
print("Q0, F2, F3 done", round(time.time() - t0, 1), "s", file=sys.stderr, flush=True)

# ------------------------------------------------------------------ F1: the bound
def rand_c(n=3): return rng.normal(size=n) + 1j * rng.normal(size=n)
def rand_on(n=3):
    Q, _ = np.linalg.qr(rng.normal(size=(n, n))); return Q[:, 0], Q[:, 1]


worst = -1.0; counts = {}
fams = {"gaussian": 0, "isotropic_vs_real": 0, "near_iso_vs_near_real": 0, "sharp_perturbed": 0}
for fam in fams:
    for _ in range(50000):
        if fam == "gaussian":
            u, v = rand_c(), rand_c()
        elif fam == "isotropic_vs_real":
            x, y = rand_on(); u = (x + 1j * y) / math.sqrt(2); v = rng.normal(size=3) * np.exp(2j * math.pi * rng.random())
        elif fam == "near_iso_vs_near_real":
            x, y = rand_on(); eps = 10 ** rng.uniform(-6, -1)
            u = (x + 1j * y) / math.sqrt(2) + eps * rand_c(); v = rng.normal(size=3) + eps * rand_c()
        else:
            x, y = rand_on(); au, av = rng.uniform(0, math.pi / 4, 2)
            u = math.cos(au) * x + 1j * math.sin(au) * y; v = math.cos(av) * x + 1j * math.sin(av) * y
            v = v + 1e-3 * rand_c()
        d = ratio(u, v) - bound(sig(u), sig(v))
        worst = max(worst, d)
    fams[fam] = worst


def neg_gap(p):
    u = p[0:3] + 1j * p[3:6]; v = p[6:9] + 1j * p[9:12]
    if np.vdot(u, u).real < 1e-12 or np.vdot(v, v).real < 1e-12: return 0.0
    return -(ratio(u, v) - bound(sig(u), sig(v)))


adv = -1.0
for _ in range(200):
    r = minimize(neg_gap, rng.normal(size=12), method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-12, "fatol": 1e-14})
    adv = max(adv, -r.fun)
sharp = 0.0
for su in np.linspace(0, 1, 5):
    for sv in np.linspace(0, 1, 5):
        x, y = rand_on(); au, av = 0.5 * math.acos(su), 0.5 * math.acos(sv)
        u = math.cos(au) * x + 1j * math.sin(au) * y; v = math.cos(av) * x + 1j * math.sin(av) * y
        sharp = max(sharp, abs(ratio(u, v) - bound(sig(u), sig(v))))
F1 = {"max_excess_random_by_family_cumulative": fams, "max_excess_adversarial": adv, "sharp_max_abs_gap": sharp}
F1["holds"] = bool(max(fams.values()) <= 1e-9 and adv <= 1e-9 and sharp <= 1e-12)
out["F1"] = F1
print("F1 done", round(time.time() - t0, 1), "s", file=sys.stderr, flush=True)

# ------------------------------------------------------------------ F4: the cap
F4 = {"max_real_overlap": {}, "tm1_frames_max": {}, "tm1_W49": {}}
perms = list(itertools.permutations([0, 1, 2])); frames = [fL, fR, f3]
signs = [(1, s2, s3) for s2 in (1, -1) for s3 in (1, -1)]
cap_ok = True
for t, name in zip(GRID, GRID_NAMES):
    R = R_np(t); Rh = R / np.linalg.norm(R)
    top = float(np.linalg.eigvalsh(np.real(np.outer(Rh, Rh.conj()))).max())
    F4["max_real_overlap"][name] = top
    vals = []
    for pm in perms:
        for sg in signs:
            RB = sum(sg[u] * R[u] * frames[pm[u]] for u in range(3))
            vals.append(ratio(RB, nu_TM1))
            if pm == (0, 1, 2):
                F4["tm1_W49"].setdefault(name, []).append(ratio(RB, nu_TM1))
    F4["tm1_frames_max"][name] = [min(vals), max(vals)]
    cap_ok = cap_ok and abs(top - 0.5) < 1e-12 and max(vals) <= 0.5 + 1e-12
F4["holds"] = bool(cap_ok)
out["F4"] = F4

# ------------------------------------------------------------------ F5: one fibre, every neutrino operator (residues)
def lightest_states(M):
    """columns = right singular vectors in ascending order of the singular values (the kernel vector first)"""
    W, s, Vh = np.linalg.svd(M); order = np.argsort(s)
    return Vh.conj().T[:, order], s[order]


F5 = {"cases": []}; f5_ok = True
for t in GRID[:6]:
    tm = mp.mpc(t.real, t.imag)
    for d in range(3):
        se = rand_c(4); Ye = to_np(Y_of([complex(x) for x in se], tm))
        a = rand_c(3); Ya = to_np(Y_of([0j] + [complex(x) for x in a], tm))
        sD = rand_c(4); YD = to_np(Y_of([complex(x) for x in sD], tm))
        Mr = rand_c(9).reshape(3, 3); Mr = Mr + Mr.T + 4 * np.eye(3)
        ops = {"weinberg_Y(a)": Ya, "typeI_-YDt_MRinv_YD": -YD.T @ np.linalg.inv(Mr) @ YD}
        ops["typeI_plus_II"] = ops["weinberg_Y(a)"] + ops["typeI_-YDt_MRinv_YD"]
        Ve, se_ = lightest_states(Ye)
        for k, Mn in ops.items():
            Mn = (Mn + Mn.T) / 2
            Vn, sn = lightest_states(Mn)
            U = Ve.conj().T @ Vn
            c = {"tau": str(t), "draw": d, "op": k, "abs_Ue1": float(abs(U[0, 0])), "abs_Ue2": float(abs(U[0, 1])),
                 "abs_Ue3": float(abs(U[0, 2])), "me_over_mtau": float(se_[0] / se_[2]), "m1_over_m3": float(sn[0] / sn[2])}
            F5["cases"].append(c)
            f5_ok = f5_ok and abs(c["abs_Ue1"] - 1) < 1e-10 and c["abs_Ue2"] < 1e-10 and c["abs_Ue3"] < 1e-10 \
                and c["me_over_mtau"] < 1e-10 and c["m1_over_m3"] < 1e-10
    print("F5 tau", t, round(time.time() - t0, 1), "s", file=sys.stderr, flush=True)
F5["worst"] = {k: (max(abs(c[k] - 1) for c in F5["cases"]) if k == "abs_Ue1" else max(c[k] for c in F5["cases"]))
               for k in ("abs_Ue1", "abs_Ue2", "abs_Ue3", "me_over_mtau", "m1_over_m3")}
F5["holds"] = bool(f5_ok)
out["F5"] = {"worst": F5["worst"], "holds": F5["holds"], "n_cases": len(F5["cases"]), "cases": F5["cases"]}

# ------------------------------------------------------------------ F6: Reading B (conditional)
def Eij(r, s):
    E = np.zeros((3, 3), dtype=complex); E[r, s] = 1; return E


F6 = {"cases": [], "both_sectors": [], "Rt2_over_R2": {}}; f6_ok = True
for ti, tname in enumerate(UNITS):
    r, s = [x for x in range(3) if x != ti]
    et = np.zeros(3, dtype=complex); et[ti] = 1
    for t, name in zip(GRID, GRID_NAMES):
        R = R_np(t); Rh = R / np.linalg.norm(R)
        F6["Rt2_over_R2"].setdefault(tname, {})[name] = float(abs(R[ti]) ** 2 / np.vdot(R, R).real)
        for d in range(3):
            al, be = rand_c(2), rand_c(2)
            A = al[0] * Eij(r, s) + al[1] * Eij(s, r); B = be[0] * Eij(r, s) + be[1] * Eij(s, r)
            M = A.T @ Y_formula(rand_c(3), R) @ B; M = (M + M.T) / 2
            Vn, sn = lightest_states(M)
            c = {"t": tname, "tau": name, "m1_over_m3": float(sn[0] / sn[2]), "m2_over_m3": float(sn[1] / sn[2]),
                 "overlap_null_et": float(abs(np.vdot(et, Vn[:, 0]))), "Ue1_sq": ratio(Rh, Vn[:, 0])}
            F6["cases"].append(c)
            f6_ok = f6_ok and c["m1_over_m3"] < 1e-12 and c["m2_over_m3"] > 1e-6 and abs(c["overlap_null_et"] - 1) < 1e-10 \
                and c["Ue1_sq"] <= 0.5 + 1e-12
    # both sectors (residue couplings at three tau): the charged leptons' Dirac matrix A' Y(S_e) B'
    for t in GRID[:3]:
        tm = mp.mpc(t.real, t.imag)
        Ye = to_np(Y_of([complex(x) for x in rand_c(4)], tm))
        al, be = rand_c(2), rand_c(2)
        Ap = al[0] * Eij(r, s) + al[1] * Eij(s, r); Bp = be[0] * Eij(r, s) + be[1] * Eij(s, r)
        Ve, se_ = lightest_states(Ap.T @ Ye @ Bp)
        al, be = rand_c(2), rand_c(2)
        A = al[0] * Eij(r, s) + al[1] * Eij(s, r); B = be[0] * Eij(r, s) + be[1] * Eij(s, r)
        M = A.T @ to_np(Y_of([0j] + [complex(x) for x in rand_c(3)], tm)) @ B; M = (M + M.T) / 2
        Vn, sn = lightest_states(M)
        c = {"t": tname, "tau": str(t), "abs_Ue1": float(abs(np.vdot(Ve[:, 0], Vn[:, 0]))),
             "me_over_mtau": float(se_[0] / se_[2]), "m1_over_m3": float(sn[0] / sn[2])}
        F6["both_sectors"].append(c)
        f6_ok = f6_ok and abs(c["abs_Ue1"] - 1) < 1e-10
    print("F6 t =", tname, round(time.time() - t0, 1), "s", file=sys.stderr, flush=True)
F6["worst"] = {"m1_over_m3": max(c["m1_over_m3"] for c in F6["cases"]), "min_m2_over_m3": min(c["m2_over_m3"] for c in F6["cases"]),
               "max_dev_overlap_null_et": max(abs(c["overlap_null_et"] - 1) for c in F6["cases"]),
               "max_Ue1_sq": max(c["Ue1_sq"] for c in F6["cases"]),
               "both_sectors_max_dev_Ue1": max(abs(c["abs_Ue1"] - 1) for c in F6["both_sectors"])}
F6["holds"] = bool(f6_ok)
out["F6"] = F6

# ------------------------------------------------------------------ read-outs
ro = {}
ys = np.linspace(0.6, 6.0, 28)
ro["imag_axis_y"] = [float(y) for y in ys]
ro["tm1_W49_imag_axis"] = []
ro["Rt2_over_R2_imag_axis"] = {u: [] for u in UNITS}
ro["hand_value_(th3^4+th4^4)/(4 th3^4)"] = []
for y in ys:
    t = 1j * y; R = R_np(t)
    ro["tm1_W49_imag_axis"].append([ratio(sum(sg[u] * R[u] * frames[u] for u in range(3)), nu_TM1) for sg in signs])
    for ui, u in enumerate(UNITS):
        ro["Rt2_over_R2_imag_axis"][u].append(float(abs(R[ui]) ** 2 / np.vdot(R, R).real))
    n = np.arange(-40, 41); q = lambda x: np.exp(1j * np.pi * t * x)
    th3, th4 = np.sum(q(n * n)).real, np.sum((-1.0) ** n * q(n * n)).real
    ro["hand_value_(th3^4+th4^4)/(4 th3^4)"].append(float((th3 ** 4 + th4 ** 4) / (4 * th3 ** 4)))
# both condensates on one leg: sym(Y(a) A B)
one_leg = []
for ti in range(3):
    r, s = [x for x in range(3) if x != ti]
    for t in GRID:
        R = R_np(t); al, be = rand_c(2), rand_c(2)
        A = al[0] * Eij(r, s) + al[1] * Eij(s, r); B = be[0] * Eij(r, s) + be[1] * Eij(s, r)
        M = Y_formula(rand_c(3), R) @ A @ B; M = (M + M.T) / 2
        sv = np.linalg.svd(M, compute_uv=False)
        one_leg.append(float(sv.min() / sv.max()))
ro["one_leg_min_sv_ratio_range"] = [min(one_leg), max(one_leg)]
# every real eigenline of the group against R^ (W49's frame, signs +++)
real_lines = []
for A in GT:
    for e, Wv in eig_groups(A):
        if Wv.shape[1] == 1 and abs(sig(Wv[:, 0], Bf) - 1) < 1e-9:
            v = Wv[:, 0]
            if all(abs(abs(np.vdot(v, w)) - 1) > 1e-8 for w in real_lines): real_lines.append(v)
ro["n_real_eigenlines"] = len(real_lines)
ro["max_overlap_real_eigenline_vs_R"] = {}
for t, name in zip(GRID, GRID_NAMES):
    R = R_np(t); RB = sum(R[u] * frames[u] for u in range(3))
    ro["max_overlap_real_eigenline_vs_R"][name] = max(ratio(RB, v) for v in real_lines)
p = (1 - 0.3092) * (1 - 0.02248); dp = 0.0087 * (1 - 0.02248)
ro["data"] = {"Ue1_sq": p, "err": dp, "sigma_from_half": (p - 0.5) / dp, "sigma_from_one": (1 - p) / dp,
              "sigma_nu_max_data": 2 * math.sqrt(p * (1 - p)), "sigma_nu_max_TM1": 2 * math.sqrt(2 / 9),
              "electron_min_turn_deg_data": 45 - math.degrees(0.5 * math.acos(2 * p - 1)),
              "electron_min_turn_deg_TM1": 45 - math.degrees(0.5 * math.acos(1 / 3))}
ro["sigma_R_in_frame"] = {name: sig(sum(R_np(t)[u] * frames[u] for u in range(3)), Bf) for t, name in zip(GRID, GRID_NAMES)}
out["readouts"] = ro

out["cells"] = {k: out[k]["holds"] for k in ("Q0", "F1", "F2", "F3", "F4", "F5", "F6")}
out["seconds"] = round(time.time() - t0, 1)
(HERE / "first_row.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
summary = {k: {kk: vv for kk, vv in out[k].items() if kk not in ("cases", "both_sectors")} for k in ("Q0", "F1", "F2", "F3", "F4", "F5", "F6")}
print(json.dumps(summary, indent=1, default=str))
print(json.dumps({k: v for k, v in ro.items() if k not in ("imag_axis_y",)}, indent=1, default=str))
print(json.dumps(out["cells"], indent=1)); print("seconds", out["seconds"])
