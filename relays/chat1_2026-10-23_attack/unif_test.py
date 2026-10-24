#!/usr/bin/env python3
"""THE UNIFICATION-SCALE TEST (sealed by UNIF_TEST_RULE.md, committed and pushed before this script is committed; this
script is committed before its run on the test grid, its outputs before they are read).  One Higgs direction read S in
every sector (A1), against the nine at the unification scale (arm G: arXiv:2510.01312v1 Table 6, MSSM, tan beta 10, as
transcribed in targets_unification.json) and at M_Z (arm Z: the record's pinned targets), on fresh rows, with a
two-stage search; J and m_b/m_tau as cells.

Instrument: main's fibre frame (B1720's instrument at 3412bf09d, unchanged, through chat1's channel_store.py wrappers)
and B1736's closed form on stored channel weights; PRECISION_BAR's chi2 (sigma^2 = relative error^2 + 0.1^2); c = 3 on
the leptons.

Modes, in this order:
  --c0        data-free checks (no data target of either arm is compared with the model; random and planted targets only).
  --store     C1 at five points, then the channel weights and the record's directions on the grid and the mirror set
              (chunks of 64 points in chunks_unif/, git-ignored); unif_store.npz and its index.
  --c2        the power controls: for each arm 72 rows, a planted direction each (24 near the null conic, 24 near n or
              n-bar, 24 uniform), targets the A1 model's nine there plus Gaussian noise of the arm's sigma, searched by
              the declared two-stage search; the noiseless recovery as a read-out; unif_c2.json.
  --scan      every row: the A1 nine on the direction grid once; for each arm the declared two-stage search (stage A, the
              sealed search of THE HOLOMORPHIC READING TEST; stage B, search_v3, where stage A's minimum is below 150)
              and the read-outs at its optimum; on the calibration grid (every 17th direction of the search grid) each
              arm's minimum for its 10 301 targets (the data's, 300 from main's generator, 10 000 lepton-tied); chunks of
              200 rows (chunks_unif/, atomic, resumable only with the same scripts, data and store); then unif_rows.json
              and unif_calib_best.npz (per arm and target: its best eligible test row by calibration-grid minimum).
  --calib     per arm, only if that arm's H1' holds (and always in the dry mode): for every target the declared two-stage
              search on its best eligible row (the same procedure for the data and every target), each row's group of
              targets written atomically to chunks_unif/calib/ so that a killed run resumes (--arm G or Z runs one arm);
              random as good per set with exact bounds; unif_calib.json when both arms are done.
  --cells     the cells and read-outs from the committed outputs; unif_cells.json.
  --readouts  after the cells: arm G's twenty lowest rows re-searched at tan beta 5, 30 and 50; unif_readouts.json.
Dry mode (UNIF_DRY=1 and UNIF_OUT=<a folder outside the repository>): the ten alpha = 2/5 lines at Re tau 0.0625 (mirror
0.9375), Im tau 2.0 and 2.1 (TWO_HIGGS's points), 10 + 20 random targets, 6 planted rows per arm, chunks of 20 rows; each
arm's data target, J, m_b/m_tau and D windows replaced by stand-ins (random.Random(99) and fixed values), so that no model
value is compared with the data's nine, J, m_b/m_tau or D (set 2's lepton tie and arm G's shift still use the data's factors);
the calibration always runs; every output goes to UNIF_OUT.
    python3 -B unif_test.py --c0 | --store [--workers 2] | --c2 [--workers 2] | --scan [--workers 2] | --calib [--arm G|Z] [--workers 2] | --cells | --readouts"""
import os
for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import contextlib, hashlib, importlib.util, io, json, math, random, sys, time, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
DRY = os.environ.get("UNIF_DRY") == "1"
OUT = pathlib.Path(os.environ["UNIF_OUT"]).resolve() if DRY else HERE
if DRY:
    assert OUT != ROOT and ROOT not in OUT.parents, "the dry run writes outside the repository"
    OUT.mkdir(parents=True, exist_ok=True)


def _load(name, file):
    argv = sys.argv; sys.argv = ["x"]
    spec = importlib.util.spec_from_file_location(name, HERE / file); mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    sys.argv = argv
    return mod


cs = _load("cs", "channel_store.py")
ih = _load("ih", "inverse_higgs.py")
oh = _load("oh", "one_higgs_search.py")
s3 = _load("s3", "search_v3.py")
TU_SHA = "ea6af55b31c979588dbabcd98db6f11ac36a224328f30fde8943e7bae93cd301"
TU = json.loads((HERE / "targets_unification.json").read_text())
TB = TU["GUT"]["tan beta 10"]
ARMS = ("G", "Z")                                          # arm index a: 0 for G, 1 for Z
T_TRUE = {"G": np.log(np.array(TB["nine"])), "Z": ih.T9.copy()}
SIG = {"G": np.sqrt(np.array(TB["relative errors"]) ** 2 + 0.10 ** 2), "Z": ih.SIG.copy()}
SHIFT = T_TRUE["G"] - T_TRUE["Z"]                          # ln(GUT / M_Z) for each of the nine
J_T = {"Z": 3.08e-5, "G": 3.08e-5 * float(np.exp(SHIFT[6:9].sum()))}   # J scaled by the three moduli's running
BTAU_T = {"Z": ih.v["b"] / ih.v["tau"], "G": TB["m_b/m_tau"]}
D_T, D_W = 10.58, 0.33                                     # P-094's D and its 3 sigma
LINES = [(tag, Fr(a), Fr(b)) for (tag, a, b) in cs.tic.LINES]
if DRY:
    LINES = [l for l in LINES if l[1] == Fr(2, 5)]
    J_T = {"Z": 1.0e-4, "G": 1.0e-4}; BTAU_T = {"Z": 2.0, "G": 2.0}; D_T = 7.0     # stand-ins: no measured number
DIRS = cs.DIRS
RE = [0.0625] if DRY else [0.225, 0.275]
IM = [2.0, 2.1] if DRY else [2.275, 2.575, 2.875, 3.175, 3.475]
RE_MIRROR = 0.9375 if DRY else 0.725                       # = 1 - RE[-1], the ten alpha = 2/5 lines only (controls C3, C3')
LOOK_LINES = [(Fr(2, 5), Fr(0)), (Fr(2, 5), Fr(3, 5))]     # the A1 look's lines (left out of the cells' H1', H2' and the calibration)
ORDERS_COPY = (1, 2, 5)                                     # line orders on which the leptons copy the down quarks
CHUNK, ROWCHUNK = 64, (20 if DRY else 200)
BAR9, BAR6, BAR5 = 21.67, 16.75, 15.09
K1, K2 = (10, 20) if DRY else (300, 10000)
NC2 = 6 if DRY else 72
M_ARC, M_WIDE = 10, 21                                     # THE_BAR's Bonferroni counts (the rule lists both)
STAGE_B = 150.0                                            # stage B (search_v3) runs where stage A's minimum is below this
CAL_IDX = np.arange(0, len(oh.HS), 17)                     # the calibration grid: every 17th direction of the search grid
PM = np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)   # R4: h -> PM conj(h) on the mirror row
CD = OUT / "chunks_unif"


def _sha(paths):
    h = hashlib.sha256()
    for p in paths:
        h.update(p.read_bytes())
    return h.hexdigest()


SHA = _sha([HERE / f for f in ("unif_test.py", "search_v3.py", "one_higgs_search.py", "sm_search.py", "inverse_higgs.py",
                               "channel_store.py", "targets_unification.json")])


def grid():
    pts = [(k, r, y) for k in range(len(LINES)) for r in RE for y in IM]
    a25 = [k for k, (_, a, _) in enumerate(LINES) if a == Fr(2, 5)]
    return pts + [(k, RE_MIRROR, y) for k in a25 for y in IM]


def r_masses(rng):
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2:
                break
        tg += [r2, r1]
    return tg


def r_ckm(rng):
    while True:
        a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
        if c < b < a:
            return [a, b, c]


def random_targets(n):
    rng = random.Random(1743)
    return np.log(np.array([r_masses(rng) + r_ckm(rng) for _ in range(n)]))


T = dict(T_TRUE)
if DRY:
    _rr = random.Random(99)
    T["Z"] = np.log(np.array(r_masses(_rr) + r_ckm(_rr))); T["G"] = T["Z"] + SHIFT
TALL = {}
for _arm in ARMS:
    _sh = SHIFT if _arm == "G" else np.zeros(9)
    _r1 = random_targets(K1) + _sh                         # set 1: main's generator, the first K1 draws, run to the arm's scale
    _r2 = random_targets(K2) + _sh                         # set 2: the first K2 draws, leptons tied to their own down ratios
    _r2[:, 4] = _r2[:, 2] + (T_TRUE[_arm][4] - T_TRUE[_arm][2])   # by the arm's data factors (m_mu/m_tau over m_s/m_b, ...)
    _r2[:, 5] = _r2[:, 3] + (T_TRUE[_arm][5] - T_TRUE[_arm][3])
    TALL[_arm] = np.concatenate([T[_arm][None], _r1, _r2])        # column 0 is the data's target
NT = 1 + K1 + K2


def order(line):
    return int(line[0][2:])


def readout(Uh, h, Tt, SG):
    """Everything reported at a direction h: the nine and its parts, |V|, D, J, the inter-sector ratios, h's components."""
    Lh, c9, V = oh.nine_batch(Uh, h[None], Tt, SG, False)
    Uu, su, _ = np.linalg.svd(oh.Ybatch(Uh[0], h[None])[0]); Ud, sd, _ = np.linalg.svd(oh.Ybatch(Uh[1], h[None])[0])
    se = np.linalg.svd(oh.Ybatch(Uh[2], h[None])[0], compute_uv=False)
    Vc = np.conj(Uu[:, ::-1]).T @ Ud[:, ::-1]
    J = float(np.imag(Vc[0, 1] * Vc[1, 2] * np.conj(Vc[0, 2]) * np.conj(Vc[1, 1])))
    c = [np.vdot(oh.F2, h), np.vdot(oh.F3, h), np.vdot(oh.F1, h)]
    return {"chi2_nine": float(c9[0]), "chi2_six there": float(np.sum(((Lh[0, :6] - Tt[:6]) / SG[:6]) ** 2)),
            "chi2 CKM share there": float(np.sum(((Lh[0, 6:] - Tt[6:]) / SG[6:]) ** 2)),
            "model/data": [float(q) for q in np.exp(Lh[0] - Tt)], "|V|": V[0].round(6).tolist(),
            "D": float(math.exp((Lh[0, 4] - Lh[0, 2]) + (Lh[0, 3] - Lh[0, 5]))), "J": J,
            "m_b/m_tau": float(sd[0] / se[0]), "m_t/m_b": float(su[0] / sd[0]), "|h.h|": float(abs(h @ h)),
            "|e1|, |n|, |n-bar|": [float(abs(q)) for q in c], "h": [[float(q.real), float(q.imag)] for q in h]}


def search_row(Uh, extra, Tt, SG, L, seed):
    """The declared two-stage search on one row: stage A, the sealed search of THE HOLOMORPHIC READING TEST
    (one_higgs_search.search, n_extra = 4) on the shared grid; stage B, search_v3's search (all four stages), only where
    stage A's minimum is below STAGE_B; the row's minimum is the lower of the two.
    Returns (the grid's minimum, the minimum, its 6-vector x, stage A's minimum, whether stage B ran)."""
    chis = np.sum(((L - Tt) / SG) ** 2, axis=1)
    gA, (cA, xA) = oh.search(Uh, extra, Tt, SG, False, n_extra=4, chis=chis)
    if not cA < STAGE_B:
        return gA, cA, xA, cA, False
    _, (cB, xB) = s3.search3(Uh, extra, Tt, SG, L=L, seed=seed)
    return (gA, cB, xB, cA, True) if cB < cA else (gA, cA, xA, cA, True)


def cp_upper(k, n):
    """The upper end of the exact (Clopper-Pearson) two-sided 95% interval for k hits in n (as THE_BAR reads it)."""
    from scipy.stats import beta
    return 1.0 if k >= n else float(beta.ppf(0.975, k + 1, n - k))


# ---------------------------------------------------------------- C0
def c0():
    U = np.load(HERE / "channel_store_two_higgs.npz")["U"]; Hs = np.load(HERE / "channel_store_two_higgs.npz")["H"]
    rng = np.random.default_rng(8); w_a1, w_j, w_v = 0.0, 0.0, 0.0
    for p in (0, 333, 777, 1111, 1279):
        for hr in range(2):
            Uh = U[p, :, hr]
            H = rng.normal(size=(100, 3)) + 1j * rng.normal(size=(100, 3)); H /= np.linalg.norm(H, axis=1)[:, None]
            La, Va = oh.model_logs(Uh, H, False)
            for n in range(100):
                L, _, _ = ih.nine(Uh, H[n], H[n])
                w_a1 = max(w_a1, float(np.max(np.abs(L - La[n]))))
            for n in range(10):
                h = H[n]
                Uu, _, _ = np.linalg.svd(oh.Ybatch(Uh[0], h[None])[0]); Ud, _, _ = np.linalg.svd(oh.Ybatch(Uh[1], h[None])[0])
                Vc = np.conj(Uu[:, ::-1]).T @ Ud[:, ::-1]
                J1 = np.imag(Vc[0, 1] * Vc[1, 2] * np.conj(Vc[0, 2]) * np.conj(Vc[1, 1]))
                J2 = np.imag(Vc[0, 0] * Vc[1, 1] * np.conj(Vc[0, 1]) * np.conj(Vc[1, 0]))
                w_j = max(w_j, float(abs(J1 - J2)))
                w_v = max(w_v, float(np.max(np.abs(np.abs(Vc) - Va[n]))))
    wc = 0.0
    for p in (5, 900):
        L = oh.grid_logs(U[p, :, 0], False)
        nk = min(40, NT - 1)
        b, _ = oh.chi2_many(L[CAL_IDX], TALL["G"][1:1 + nk], SIG["G"])
        d = np.array([np.min(np.sum(((L[CAL_IDX] - TALL["G"][1 + k]) / SIG["G"]) ** 2, axis=1)) for k in range(nk)])
        wc = max(wc, float(np.max(np.abs(b - d) / np.maximum(d, 1e-9))))
    tg = np.array(TB["nine"]); rel = np.array(TB["relative errors"])
    tz = np.array(TU["M_Z (the record's pinned targets)"]); relz = np.array(TU["M_Z relative errors"])
    w_t = max(float(np.max(np.abs(np.exp(T_TRUE["G"]) / tg - 1))), float(np.max(np.abs(np.exp(T_TRUE["Z"]) / tz - 1))),
              float(np.max(np.abs(SIG["G"] - np.sqrt(rel ** 2 + 0.01)))), float(np.max(np.abs(SIG["Z"] - np.sqrt(relz ** 2 + 0.01)))),
              float(np.max(np.abs(ih.REL - relz))))
    sha_ok = hashlib.sha256((HERE / "targets_unification.json").read_bytes()).hexdigest() == TU_SHA
    w_s = float(np.max(np.abs((TALL["G"][1:1 + K1] - TALL["Z"][1:1 + K1]) - SHIFT)))
    w_tie = max(max(float(np.max(np.abs(TALL[a][1 + K1:, 4] - TALL[a][1 + K1:, 2] - (T_TRUE[a][4] - T_TRUE[a][2])))),
                    float(np.max(np.abs(TALL[a][1 + K1:, 5] - TALL[a][1 + K1:, 3] - (T_TRUE[a][5] - T_TRUE[a][3]))))) for a in ARMS)
    Uh = U[777, :, 1]; L = s3.grid_logs(Uh)
    r1 = s3.search3(Uh, Hs[777], TALL["G"][5], SIG["G"], L=L, seed=11); r2 = s3.search3(Uh, Hs[777], TALL["G"][5], SIG["G"], L=L, seed=11)
    hp = np.array([0.3 + 0.1j, 0.8, 0.5j]); hp = hp / np.linalg.norm(hp)                   # a planted target, so that stage B runs
    Tpl = oh.nine_batch(Uh, hp[None], np.zeros(9), SIG["Z"], False)[0][0] + 0.5 * SIG["Z"]
    q1 = search_row(Uh, Hs[777], Tpl, SIG["Z"], L, 12); q2 = search_row(Uh, Hs[777], Tpl, SIG["Z"], L, 12)
    same = bool(r1[1][0] == r2[1][0] and np.array_equal(r1[1][1], r2[1][1]) and q1[1] == q2[1] and np.array_equal(q1[2], q2[2]))
    out = {"C0a A1 model against inverse_higgs.nine(h, h): largest |delta ln| (1 000 directions, 10 rows)": w_a1,
           "C0b J from two quartets of the complex CKM: largest difference (100 directions)": w_j,
           "C0c |V| from the complex CKM against model_logs' moduli: largest difference": w_v,
           "C0d chi2_many on the calibration grid against a direct computation, arm G's sigma: largest relative difference (40 random targets, 2 rows)": wc,
           "C0e targets and both arms' sigma against targets_unification.json (and its M_Z copy against inverse_higgs): largest difference": w_t,
           "C0e' targets_unification.json's sha256 is the rule's": sha_ok,
           "C0f set 1 at G minus set 1 at Z against ln(GUT/M_Z): largest difference": w_s,
           "C0g set 2's lepton tie, both lepton ratios, both arms: largest departure": w_tie,
           "C0h search_v3 and the two-stage search repeated with the same seeds: identical minima and directions": same,
           "C0h the two minima (search_v3 on a random target; the two-stage search on a planted one) and whether stage B ran there": [r1[1][0], q1[1], q1[4]],
           "J targets (Z, G)": [J_T["Z"], J_T["G"]], "m_b/m_tau targets (Z, G)": [BTAU_T["Z"], BTAU_T["G"]],
           "C0 holds": bool(w_a1 < 1e-10 and w_j < 1e-12 and w_v < 1e-10 and wc < 1e-8 and w_t < 1e-12 and sha_ok and w_s < 1e-12
                            and w_tie < 1e-12 and same and q1[4])}
    (OUT / "unif_c0.json").write_text(json.dumps(out, indent=1) + "\n")
    print("C0 written")


# ---------------------------------------------------------------- the store
def store_point(task):
    k, re_t, im_t = task
    _, a, b = LINES[k]
    return cs.weights(re_t, im_t, float(a), float(b)), cs.directions(re_t, im_t)


def store(nw):
    tasks = grid()
    picks = [0, 10, 20, 30, len(tasks) - 1] if DRY else [10 * k for k in (0, 40, 100, 180, 260)]
    worst = 0.0
    for task in [tasks[i] for i in picks]:
        k, re_t, im_t = task; _, a, b = LINES[k]
        U, H = store_point(task)
        M = cs.rbs.channels(re_t, im_t, float(a), float(b))
        for d in ("F_6", "dR"):
            h = H[DIRS.index(d)]
            for i_s, sec in enumerate(cs.SECTORS):
                for i_h, hor in enumerate(cs.HORS):
                    Yc = cs.P_BLOCK @ cs.closed(U[i_s, i_h], h) @ cs.P_BLOCK.T
                    Yb = cs.B.coupling(cs.rbs.S_of(h), M[(sec, hor)])
                    worst = max(worst, float(np.max(np.abs(Yc - Yb)) / np.max(np.abs(Yb))))
    ctl = {"C1 largest relative |closed - coupling| at five points of the grid (F_6 and dR, every sector and horocycle)": worst,
           "C1 points": [tasks[i] for i in picks], "C1 holds": worst < 1e-12}
    (OUT / "unif_c1.json").write_text(json.dumps(ctl, indent=1) + "\n")
    if not ctl["C1 holds"]:
        raise SystemExit("C1 fails: the store is not written")
    CD.mkdir(exist_ok=True)
    from multiprocessing import Pool
    t0 = time.time(); nch = (len(tasks) + CHUNK - 1) // CHUNK
    with Pool(nw) as P:
        for c in range(nch):
            f = CD / f"store_{c:04d}.npz"
            if f.exists():
                continue
            res = P.map(store_point, tasks[c * CHUNK:(c + 1) * CHUNK])
            np.savez(CD / f"tmp_store_{c:04d}.npz", U=np.array([r[0] for r in res]), H=np.array([r[1] for r in res]))
            os.replace(CD / f"tmp_store_{c:04d}.npz", f)
            print(f"store chunk {c + 1}/{nch} ({time.time() - t0:.0f} s)", flush=True)
    U = np.concatenate([np.load(CD / f"store_{c:04d}.npz")["U"] for c in range(nch)])
    H = np.concatenate([np.load(CD / f"store_{c:04d}.npz")["H"] for c in range(nch)])
    np.savez_compressed(OUT / "unif_store.npz", U=U, H=H)
    (OUT / "unif_store_index.json").write_text(json.dumps({"tasks": tasks, "lines": [[t, str(a), str(b)] for t, a, b in LINES],
                                                           "sectors": cs.SECTORS, "hors": cs.HORS, "dirs": DIRS}) + "\n")
    print(f"store written ({time.time() - t0:.0f} s)")


G = {}


def _init():
    st = np.load(OUT / "unif_store.npz"); G["U"], G["H"] = st["U"], st["H"]


def n_main():
    return len(LINES) * len(RE) * len(IM)


# ---------------------------------------------------------------- C2
def c2_job(job):
    ai, n, p, hr, Tp, T0 = job
    arm = ARMS[ai]; Uh = G["U"][p, :, hr]
    L = s3.grid_logs(Uh)
    _, chi, _, chiA, ranB = search_row(Uh, G["H"][p], Tp, SIG[arm], L, 5000 + 1000 * ai + n)
    _, chi0, _, chi0A, ranB0 = search_row(Uh, G["H"][p], T0, SIG[arm], L, 5500 + 1000 * ai + n)
    return chi, chiA, ranB, chi0, chi0A, ranB0


def c2(nw):
    _init()
    res = {}
    from multiprocessing import Pool
    for ai, arm in enumerate(ARMS):
        SG = SIG[arm]; rng = np.random.default_rng(2101 + ai); meta, jobs = [], []
        t0 = time.time()
        for n in range(NC2):
            while True:                                    # a degenerate row (a sector's weights all zero) is drawn again
                p = int(rng.integers(0, n_main())); hr = int(rng.integers(0, 2))
                if not any(np.allclose(G["U"][p, s, hr], 0) for s in range(3)):
                    break
            Uh = G["U"][p, :, hr]
            kind = ["near the conic", "near n or n-bar", "uniform"][min(2, (3 * n) // NC2)]
            if kind == "near the conic":
                t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(-4, -1); ph = rng.uniform(0, 2 * math.pi)
                h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0)
                hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
            elif kind == "near n or n-bar":
                lead, other = (oh.F3, oh.F1) if n % 2 == 0 else (oh.F1, oh.F3)
                de = 0.25 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
                ep = 0.03 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
                hp = lead + de * oh.F2 + ep * other
            else:
                z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
            hp = hp / np.linalg.norm(hp)
            T0 = oh.nine_batch(Uh, hp[None], np.zeros(9), SG, False)[0][0]
            Tp = T0 + rng.normal(size=9) * SG
            cp = float(oh.nine_batch(Uh, hp[None], Tp, SG, False)[1][0])
            meta.append({"p": p, "hor": cs.HORS[hr], "kind": kind, "|h.h| planted": float(abs(hp @ hp)), "planted direction's chi2 (noisy targets)": cp})
            jobs.append((ai, n, p, hr, Tp, T0))
        with Pool(nw, initializer=_init) as P:
            found = P.map(c2_job, jobs, chunksize=1)
        out = []
        for m, (chi, chiA, ranB, chi0, chi0A, ranB0) in zip(meta, found):
            out.append({**m, "found (noisy)": chi, "met": bool(chi <= m["planted direction's chi2 (noisy targets)"] + 1e-9),
                        "stage A (noisy), stage B ran": [chiA, ranB], "found (noiseless)": chi0, "stage A (noiseless), stage B ran": [chi0A, ranB0]})
        ok = sum(o["met"] for o in out)
        res[f"C2{arm}"] = {"rows": out, "met (the search's minimum at or below the planted direction's chi2)": ok,
                           "holds": ok >= NC2 - 4,
                           "the per-row miss rate on planted rows: exact two-sided 95% upper end": cp_upper(NC2 - ok, NC2),
                           "read-out: noiseless recovered to chi2 <= 0.1, <= 2.167": [sum(o["found (noiseless)"] <= 0.1 for o in out),
                                                                                      sum(o["found (noiseless)"] <= 2.167 for o in out)],
                           "read-out: the largest stage-A minimum on a planted row (noisy, noiseless); rows where stage B did not run":
                               [max(o["stage A (noisy), stage B ran"][0] for o in out), max(o["stage A (noiseless), stage B ran"][0] for o in out),
                                sum((not o["stage A (noisy), stage B ran"][1]) or (not o["stage A (noiseless), stage B ran"][1]) for o in out)],
                           "seconds": time.time() - t0}
    (OUT / "unif_c2.json").write_text(json.dumps(res, indent=1) + "\n")
    print("C2 written")


# ---------------------------------------------------------------- the scan
def scan_row(job):
    p, hr = job
    Uh = G["U"][p, :, hr]
    if any(np.allclose(Uh[s], 0) for s in range(3)):
        return ({"p": p, "hor": cs.HORS[hr], "degenerate": True}, np.full((2, NT), np.nan, dtype=np.float32),
                np.full((2, NT), -1, dtype=np.int32))
    L = s3.grid_logs(Uh)
    row = {"p": p, "hor": cs.HORS[hr], "degenerate": False}
    mins = np.empty((2, NT), dtype=np.float32); args = np.empty((2, NT), dtype=np.int32)
    for ai, arm in enumerate(ARMS):
        gmin, chi, x, chiA, ranB = search_row(Uh, G["H"][p], T[arm], SIG[arm], L, 7919 * (2 * p + hr) + ai + 1)
        h = oh.vec(x); h = h / np.linalg.norm(h)
        row[arm] = {"grid min chi2_nine": gmin, "stage A minimum": chiA, "stage B ran": ranB, **readout(Uh, h, T[arm], SIG[arm])}
        b, a = oh.chi2_many(L[CAL_IDX], TALL[arm], SIG[arm])
        mins[ai] = b; args[ai] = CAL_IDX[a]
    return row, mins, args


def eligible(tasks, rows):
    LN = [(l[1], l[2]) for l in LINES]
    return np.array([(not r.get("degenerate")) and tasks[r["p"]][1] != RE_MIRROR and LN[tasks[r["p"]][0]] not in LOOK_LINES
                     for r in rows])


def scan(nw):
    tasks = json.loads((OUT / "unif_store_index.json").read_text())["tasks"]
    jobs = [(p, hr) for p in range(len(tasks)) for hr in range(2)]
    CD.mkdir(exist_ok=True)
    man = CD / "manifest.json"
    stamp = {"sha256 (scripts and targets)": SHA, "sha256 (store)": _sha([OUT / "unif_store.npz"])}
    if man.exists():
        assert json.loads(man.read_text()) == stamp, "chunks from other scripts, targets or store: clear chunks_unif/ first"
    else:
        man.write_text(json.dumps(stamp) + "\n")
    from multiprocessing import Pool
    t0 = time.time(); nch = (len(jobs) + ROWCHUNK - 1) // ROWCHUNK
    with Pool(nw, initializer=_init) as P:
        for c in range(nch):
            f = CD / f"rows_{c:04d}.json"
            if f.exists():
                continue
            res = P.map(scan_row, jobs[c * ROWCHUNK:(c + 1) * ROWCHUNK], chunksize=4)
            for nm, arr in (("mins", np.array([r[1] for r in res])), ("args", np.array([r[2] for r in res]))):
                np.save(CD / f"tmp_{nm}_{c:04d}.npy", arr); os.replace(CD / f"tmp_{nm}_{c:04d}.npy", CD / f"{nm}_{c:04d}.npy")
            (CD / f"tmp_rows_{c:04d}.json").write_text(json.dumps([r[0] for r in res]) + "\n"); os.replace(CD / f"tmp_rows_{c:04d}.json", f)
            print(f"row chunk {c + 1}/{nch} ({time.time() - t0:.0f} s)", flush=True)
    rows = sum((json.loads((CD / f"rows_{c:04d}.json").read_text()) for c in range(nch)), [])
    assert [(r["p"], cs.HORS.index(r["hor"])) for r in rows] == jobs
    MN = np.concatenate([np.load(CD / f"mins_{c:04d}.npy") for c in range(nch)]).astype(np.float64)
    AR = np.concatenate([np.load(CD / f"args_{c:04d}.npy") for c in range(nch)])
    assert MN.shape == (len(jobs), 2, NT)
    ok = np.where(eligible(tasks, rows))[0]
    assert np.all(np.isfinite(MN[ok])), "a non-finite calibration-grid minimum on an eligible row"
    best_row = np.empty((2, NT), dtype=np.int64); best_min = np.empty((2, NT)); best_arg = np.empty((2, NT), dtype=np.int64)
    for ai in range(2):
        sub = MN[ok, ai, :]
        i = np.argmin(sub, axis=0)
        best_row[ai] = ok[i]; best_min[ai] = sub[i, np.arange(NT)]; best_arg[ai] = AR[ok[i], ai, np.arange(NT)]
    data_top = {arm: [[int(ok[j]), float(MN[ok[j], ai, 0])] for j in np.argsort(MN[ok, ai, 0])[:10]] for ai, arm in enumerate(ARMS)}
    (OUT / "unif_rows.json").write_text(json.dumps({"tasks": tasks, "rows": rows}) + "\n")
    np.savez_compressed(OUT / "unif_calib_best.npz", best_row=best_row, best_min=best_min, best_arg=best_arg,
                        data_gridmin=MN[:, :, 0].T.copy(), eligible=eligible(tasks, rows))
    (OUT / "unif_calib_best_index.json").write_text(json.dumps({"arms": ARMS, "targets per arm": NT, "eligible rows": int(len(ok)),
                                                                "distinct best rows per arm": [int(len(set(best_row[ai].tolist()))) for ai in range(2)],
                                                                "the data's ten best eligible rows by calibration-grid minimum (row index, minimum)": data_top}) + "\n")
    print(f"rows written ({time.time() - t0:.0f} s)")


# ---------------------------------------------------------------- the calibration
def calib_group(job):
    """One eligible row and the targets whose best row it is: the grid once, then the declared search for each; the
    group's results written atomically to chunks_unif/calib/ (a killed calibration resumes from the completed groups)."""
    ai, i_row, p, hr, ks, fpath = job
    arm = ARMS[ai]; Uh = G["U"][p, :, hr]
    L = s3.grid_logs(Uh)
    out = []
    for k in ks:
        _, chi, x, _, _ = search_row(Uh, G["H"][p], TALL[arm][k], SIG[arm], L, 104729 + NT * ai + k)
        six = None
        if k == 0:
            h = oh.vec(x); h = h / np.linalg.norm(h)
            six = readout(Uh, h, TALL[arm][0], SIG[arm])["chi2_six there"]
        out.append([int(k), float(chi), six])
    tmp = pathlib.Path(str(fpath) + ".tmp"); tmp.write_text(json.dumps(out) + "\n"); os.replace(tmp, fpath)
    return len(ks)


def calib(nw, arms):
    d = json.loads((OUT / "unif_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
    cb = np.load(OUT / "unif_calib_best.npz")
    CC = CD / "calib"; CC.mkdir(parents=True, exist_ok=True)
    stamp = {"sha256 (scripts and targets)": SHA,
             "sha256 (store, rows, calibration summary)": _sha([OUT / "unif_store.npz", OUT / "unif_rows.json", OUT / "unif_calib_best.npz"])}
    man = CC / "manifest.json"
    if man.exists():
        assert json.loads(man.read_text()) == stamp, "calibration chunks from other scripts or inputs: clear chunks_unif/calib/ first"
    else:
        man.write_text(json.dumps(stamp) + "\n")
    away_ok = eligible(tasks, rows)
    from multiprocessing import Pool
    for ai, arm in enumerate(ARMS):
        if arm not in arms:
            continue
        h1p = min(rows[i][arm]["chi2_nine"] for i in np.where(away_ok)[0])
        grid_level = [float(cb["best_min"][ai, 0]), float(np.mean(cb["best_min"][ai, 1:1 + K1] <= cb["best_min"][ai, 0])),
                      float(np.mean(cb["best_min"][ai, 1 + K1:] <= cb["best_min"][ai, 0]))]
        o = {"H1' (lowest chi2_nine on the eligible rows) and whether the calibration runs": [h1p, bool(h1p < BAR9 or DRY)],
             "grid level: the data's best calibration-grid minimum; fractions of set 1 and set 2 at or below it": grid_level}
        if h1p < BAR9 or DRY:
            groups = {}
            for k in range(NT):
                groups.setdefault(int(cb["best_row"][ai, k]), []).append(k)
            jobs = [(ai, i, rows[i]["p"], cs.HORS.index(rows[i]["hor"]), ks, CC / f"{arm}_{i:05d}.json") for i, ks in groups.items()]
            todo = sorted([j for j in jobs if not j[5].exists()], key=lambda j: -len(j[4]))
            t0 = time.time(); done, ntodo = 0, sum(len(j[4]) for j in todo)
            with Pool(nw, initializer=_init) as P:
                for g, n in enumerate(P.imap_unordered(calib_group, todo, chunksize=1)):
                    done += n
                    if g % 50 == 0 or done == ntodo:
                        print(f"calibration {arm}: {done} of {ntodo} targets of this part ({time.time() - t0:.0f} s)", flush=True)
            stat = np.full(NT, np.nan); six0 = None
            for j in jobs:
                for k, chi, six in json.loads(j[5].read_text()):
                    stat[k] = chi
                    if k == 0:
                        six0 = six
            assert np.all(np.isfinite(stat))
            data = float(stat[0]); s1, s2 = stat[1:1 + K1], stat[1 + K1:]
            h1, h2 = int(np.sum(s1 <= data)), int(np.sum(s2 <= data))
            o.update({"the data's statistic (the declared search on its best eligible row by calibration-grid minimum)": data,
                      "chi2_six at the data's statistic's direction": six0,
                      "the data's row (index into unif_rows.json)": int(cb["best_row"][ai, 0]),
                      f"set 1, main's generator ({K1}): hits at or below the data's, fraction, upper end of the exact 95% interval": [h1, h1 / K1, cp_upper(h1, K1)],
                      f"set 2, lepton-tied ({K2}): hits at or below the data's, fraction, upper end of the exact 95% interval": [h2, h2 / K2, cp_upper(h2, K2)],
                      f"THE_BAR: {M_ARC} x set 2's upper end (the arc)": M_ARC * cp_upper(h2, K2),
                      f"THE_BAR: {M_WIDE} x set 2's upper end (the widest count)": M_WIDE * cp_upper(h2, K2),
                      "distinct rows searched": len(jobs), "seconds (the last part)": time.time() - t0,
                      "statistics, set 1": s1.tolist(), "statistics, set 2": s2.tolist()})
        tmp = CC / f"{arm}_result.json.tmp"; tmp.write_text(json.dumps(o, default=float) + "\n"); os.replace(tmp, CC / f"{arm}_result.json")
        print(f"calibration {arm} done", flush=True)
    if all((CC / f"{a}_result.json").exists() for a in ARMS):
        out = {a: json.loads((CC / f"{a}_result.json").read_text()) for a in ARMS}
        (OUT / "unif_calib.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
        print("calibration written")


# ---------------------------------------------------------------- the cells
def cells():
    _init()
    d = json.loads((OUT / "unif_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
    lines = [(t, Fr(a), Fr(b)) for t, a, b in json.loads((OUT / "unif_store_index.json").read_text())["lines"]]
    cal = json.loads((OUT / "unif_calib.json").read_text())
    deg = [r for r in rows if r.get("degenerate")]
    good = [r for r in rows if not r.get("degenerate")]
    main = [r for r in good if tasks[r["p"]][1] != RE_MIRROR]; mir = [r for r in good if tasks[r["p"]][1] == RE_MIRROR]
    away = [r for r in main if (lines[tasks[r["p"]][0]][1], lines[tasks[r["p"]][0]][2]) not in LOOK_LINES]
    other = [r for r in away if order(lines[tasks[r["p"]][0]]) not in ORDERS_COPY]       # the 250 lines of other orders
    copy = [r for r in main if order(lines[tasks[r["p"]][0]]) in ORDERS_COPY]

    def lab(r):
        k = tasks[r["p"]][0]
        return {"line": f"({lines[k][1]}, {lines[k][2]})", "order": lines[k][0], "tau": tasks[r["p"]][1:], "hor": r["hor"]}

    out = {"rows": len(main), "degenerate rows": [lab(r) for r in deg]}
    cb = np.load(OUT / "unif_calib_best.npz")
    elig = cb["eligible"]

    def idx_of(r):
        return 2 * r["p"] + cs.HORS.index(r["hor"])

    for ai, arm in enumerate(ARMS):
        dmin = cb["data_gridmin"][ai]

        def rank(r):
            return int(1 + np.sum(dmin[elig] < dmin[idx_of(r)]))
        A = lambda r: r[arm]
        both = lambda rs: sorted([r for r in rs if A(r)["chi2_nine"] < BAR9 and A(r)["chi2_six there"] < BAR6], key=lambda r: A(r)["chi2_nine"])
        chis = np.array([A(r)["chi2_nine"] for r in main]); chis_away = np.array([A(r)["chi2_nine"] for r in away])
        b_all, b_away, b_other = both(main), both(away), both(other)
        h1row = min(main, key=lambda r: A(r)["chi2_nine"]); h1prow = min(away, key=lambda r: A(r)["chi2_nine"])
        grank = 1 + sum(A(r)["grid min chi2_nine"] < A(h1prow)["grid min chi2_nine"] for r in away)
        ca = cal[arm]
        ran = "chi2_six at the data's statistic's direction" in ca
        k1 = next((v for kk, v in ca.items() if kk.startswith("set 1")), None)
        k2 = next((v for kk, v in ca.items() if kk.startswith("set 2")), None)
        bar = next((v for kk, v in ca.items() if kk.startswith("THE_BAR") and "arc" in kk), None)
        barw = next((v for kk, v in ca.items() if kk.startswith("THE_BAR") and "widest" in kk), None)
        jrow = b_away[0] if b_away else None; brow = b_other[0] if b_other else None
        jr = abs(A(jrow)["J"]) / J_T[arm] if jrow else None; br = A(brow)["m_b/m_tau"] / BTAU_T[arm] if brow else None
        o = {f"H1'{arm} some test row on the 264 lines (other than (2/5, 0) and (2/5, 3/5)) below 21.67": bool(chis_away.min() < BAR9),
             f"H2'{arm} some test row's optimum on the 264 lines below both bars": bool(len(b_away) > 0),
             f"H3{arm} set 1: at most 2 of {K1} at or below the data's statistic (None: not run)": (bool(k1[0] <= 2) if ran else None),
             f"H3'{arm} set 2: fewer than 1% of {K2} at or below it (None: not run)": (bool(k2[0] < 0.01 * K2) if ran else None),
             f"H3'{arm}_BAR {M_ARC} x the upper end of set 2's exact 95% interval below 1% (None: not run)": (bool(bar < 0.01) if ran else None),
             f"H3''{arm}_BAR the same with {M_WIDE} (None: not run)": (bool(barw < 0.01) if ran else None),
             f"H4{arm} some row's optimum below both bars with D within {D_T} +- {D_W} (possible only on the 250 lines)": bool(any(abs(A(r)["D"] - D_T) <= D_W for r in b_all)),
             f"H5{arm} |J| at the lowest row below both bars on the 264 lines within a factor 3 of {J_T[arm]:.3e} (None: no such row)": (bool(1 / 3 <= jr <= 3) if jrow else None),
             f"H6{arm} m_b/m_tau at the lowest row below both bars on the 250 lines of other orders within a factor 1.25 of {BTAU_T[arm]:.4f} (None: no such row)": (bool(1 / 1.25 <= br <= 1.25) if brow else None),
             "read-out H1 and H2 on all 266 lines (near-foreknown at Z on the look's lines)": [bool(chis.min() < BAR9), bool(len(b_all) > 0)],
             "the calibration ran": ran,
             "the calibration (hits, fraction, bound): set 1, set 2; THE_BAR's products (arc, widest)": [k1, k2, bar, barw] if ran else None,
             "the data's calibration statistic, chi2_six at its direction; below both bars?":
                 ([ca["the data's statistic (the declared search on its best eligible row by calibration-grid minimum)"], ca["chi2_six at the data's statistic's direction"],
                   bool(ca["the data's statistic (the declared search on its best eligible row by calibration-grid minimum)"] < BAR9 and ca["chi2_six at the data's statistic's direction"] < BAR6)]
                  if ran else None),
             "grid level (always): the data's best calibration-grid minimum; fractions of set 1 and set 2 at or below it": ca["grid level: the data's best calibration-grid minimum; fractions of set 1 and set 2 at or below it"],
             "H1' row": {**lab(h1prow), "chi2_nine": A(h1prow)["chi2_nine"], "chi2_six there": A(h1prow)["chi2_six there"],
                         "J": A(h1prow)["J"], "m_b/m_tau": A(h1prow)["m_b/m_tau"], "m_t/m_b": A(h1prow)["m_t/m_b"], "D": A(h1prow)["D"],
                         "model/data": [round(q, 3) for q in A(h1prow)["model/data"]], "rank by grid minimum on the 264 lines": grank},
             "H1 row (all lines)": {**lab(h1row), "chi2_nine": A(h1row)["chi2_nine"], "chi2_six there": A(h1row)["chi2_six there"]},
             "H5's row and |J| / target; H6's row and m_b/m_tau / target": [lab(jrow) if jrow else None, jr, lab(brow) if brow else None, br],
             "the priced row against the claim's rows: calibration-grid rank (among eligible rows) of the H1' row and of the lowest H2' row; is the priced row either": [
                 rank(h1prow), (rank(b_away[0]) if b_away else None),
                 bool(cb["best_row"][ai, 0] in [idx_of(h1prow)] + ([idx_of(b_away[0])] if b_away else []))],
             "lowest chi2_nine; on the 264 lines": [float(chis.min()), float(chis_away.min())],
             "quantiles 1%, 5%, 50%": [float(np.quantile(chis, q)) for q in (0.01, 0.05, 0.5)],
             "rows below 15.09 (nine numbers, four fitted), 21.67, 50, 100: all lines; the 264": [[int((chis < c).sum()) for c in (BAR5, BAR9, 50, 100)],
                                                                                              [int((chis_away < c).sum()) for c in (BAR5, BAR9, 50, 100)]],
             "every row below 21.67": [{**lab(r), "chi2_nine": A(r)["chi2_nine"], "chi2_six there": A(r)["chi2_six there"],
                                        "model/data": [round(q, 3) for q in A(r)["model/data"]], "D": A(r)["D"], "J": A(r)["J"],
                                        "m_b/m_tau": A(r)["m_b/m_tau"]} for r in sorted(main, key=lambda r: A(r)["chi2_nine"]) if A(r)["chi2_nine"] < BAR9],
             "D, |J| / target, m_b/m_tau / target at the rows below both bars": [[lab(r)["line"], round(A(r)["D"], 3), abs(A(r)["J"]) / J_T[arm],
                                                                                  A(r)["m_b/m_tau"] / BTAU_T[arm]] for r in b_all],
             "read-out: m_b/m_tau on the 16 lines of order 1, 2, 5 (b-tau equality): largest |m_b/m_tau - 1|; its ratio to the target":
                 [float(max(abs(A(r)["m_b/m_tau"] - 1) for r in copy)) if copy else None, 1.0 / BTAU_T[arm]],
             "rows with chi2_nine above 1e7 (outputs identically zero on their line)": len([r for r in main if A(r)["chi2_nine"] > 1e7]),
             "rows where stage B ran; rows where it lowered the minimum": [sum(bool(A(r)["stage B ran"]) for r in main),
                                                                           sum(A(r)["chi2_nine"] < A(r)["stage A minimum"] - 1e-9 for r in main)]}
        by = {}
        for r in main:
            by.setdefault(lines[tasks[r["p"]][0]][0], []).append(A(r)["chi2_nine"])
        o["lowest chi2_nine by order"] = {k: float(min(v)) for k, v in sorted(by.items(), key=lambda kv: int(kv[0][2:]))}
        o["the twenty lowest rows"] = [{**lab(r), "chi2_nine": A(r)["chi2_nine"], "chi2_six there": A(r)["chi2_six there"],
                                        "model/data": [round(q, 3) for q in A(r)["model/data"]], "|V|": A(r)["|V|"], "D": A(r)["D"],
                                        "J": A(r)["J"], "m_b/m_tau": A(r)["m_b/m_tau"], "|h.h|": A(r)["|h.h|"],
                                        "|e1|, |n|, |n-bar|": A(r)["|e1|, |n|, |n-bar|"], "stage B ran": A(r)["stage B ran"]}
                                       for r in sorted(main, key=lambda r: A(r)["chi2_nine"])[:20]]
        idx = {(t[0], round(t[1], 6), round(t[2], 6)): i for i, t in enumerate(tasks)}
        rmap = {(r["p"], r["hor"]): r for r in good}
        agree, low_pairs, low_agree, one_side, pairs, sym = 0, 0, 0, 0, 0, 0.0
        for r in mir:
            k, re_t, im_t = tasks[r["p"]]; _, a, b = lines[k]
            km = next(i for i, l in enumerate(lines) if l[1] == a and l[2] == (Fr(3, 5) - b) % 1)
            q = idx[(km, round(1 - re_t, 6), round(im_t, 6))]
            if (q, r["hor"]) not in rmap:
                continue
            rq = rmap[(q, r["hor"])]; hr = cs.HORS.index(r["hor"])
            for (pa, ra), pb in (((r["p"], r), q), ((q, rq), r["p"])):
                h = np.array([complex(x, y) for x, y in A(ra)["h"]])
                La = oh.model_logs(G["U"][pa, :, hr], h[None], False)[0][0]
                Lb = oh.model_logs(G["U"][pb, :, hr], (PM @ np.conj(h))[None], False)[0][0]
                sym = max(sym, float(np.max(np.abs(La - Lb))))
            x1, x2 = A(r)["chi2_nine"], A(rq)["chi2_nine"]
            okp = abs(x1 - x2) <= 0.01 * min(x1, x2)
            pairs += 1; agree += okp; one_side += bool(A(r)["stage B ran"]) != bool(A(rq)["stage B ran"])
            if min(x1, x2) < 50:
                low_pairs += 1; low_agree += okp
        o[f"C3{arm} R4 at each pair's two optima: the largest |delta ln| of the nine (h on one row, P conj(h) on its partner)"] = sym
        o[f"C3{arm} holds (every pair present and that largest |delta ln| below 1e-8)"] = bool(pairs == len(mir) and sym < 1e-8)
        o[f"C3'{arm} every mirror pair with a minimum below 50 agrees within 1%: pairs, agreeing, holds"] = [low_pairs, low_agree, bool(low_agree == low_pairs)]
        o["read-out: mirror pairs whose minima agree within 1%; pairs where stage B ran on one side only"] = [[agree, pairs], one_side]
        out[arm] = o
    dg = np.array([r["G"]["chi2_nine"] - r["Z"]["chi2_nine"] for r in away])
    lowm = [r for r in away if min(r["G"]["chi2_nine"], r["Z"]["chi2_nine"]) < 50]
    out["read-out on the 264 lines: chi2_nine at G minus at Z on the same row: quantiles 10/50/90%, rows with G below Z; on rows with either below 50: quantiles, rows with G below Z, rows"] = [
        [float(np.quantile(dg, q)) for q in (0.1, 0.5, 0.9)], int((dg < 0).sum()),
        ([float(np.quantile([r["G"]["chi2_nine"] - r["Z"]["chi2_nine"] for r in lowm], q)) for q in (0.1, 0.5, 0.9)] if lowm else None),
        sum(r["G"]["chi2_nine"] < r["Z"]["chi2_nine"] for r in lowm), len(lowm)]
    (OUT / "unif_cells.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("cells written")


# ---------------------------------------------------------------- read-outs after the cells
def readouts():
    _init()
    d = json.loads((OUT / "unif_rows.json").read_text()); tasks, rows = d["tasks"], d["rows"]
    main = [r for r in rows if not r.get("degenerate") and tasks[r["p"]][1] != RE_MIRROR]
    top = sorted(main, key=lambda r: r["G"]["chi2_nine"])[:20]
    out = {"rows": []}
    for n, r in enumerate(top):
        Uh = G["U"][r["p"], :, cs.HORS.index(r["hor"])]; L = s3.grid_logs(Uh)
        e = {"p": r["p"], "hor": r["hor"], "tau": tasks[r["p"]], "tan beta 10 (the arm)": r["G"]["chi2_nine"]}
        for tb in ("tan beta 5", "tan beta 30", "tan beta 50"):
            Tt = np.log(np.array(TU["GUT"][tb]["nine"])); SG = np.sqrt(np.array(TU["GUT"][tb]["relative errors"]) ** 2 + 0.01)
            if DRY:
                Tt = T["G"] + (Tt - T_TRUE["G"])
            _, chi, x, _, _ = search_row(Uh, G["H"][r["p"]], Tt, SG, L, 31337 + 100 * n + int(tb.split()[-1]))
            h = oh.vec(x); h = h / np.linalg.norm(h)
            e[tb] = {"chi2_nine": chi, "chi2_six there": readout(Uh, h, Tt, SG)["chi2_six there"]}
        out["rows"].append(e)
    (OUT / "unif_readouts.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("read-outs written")


if __name__ == "__main__":
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    if "--c0" in sys.argv:
        c0()
    elif "--store" in sys.argv:
        store(nw)
    elif "--c2" in sys.argv:
        c2(nw)
    elif "--scan" in sys.argv:
        scan(nw)
    elif "--calib" in sys.argv:
        calib(nw, [sys.argv[sys.argv.index("--arm") + 1]] if "--arm" in sys.argv else list(ARMS))
    elif "--cells" in sys.argv:
        cells()
    elif "--readouts" in sys.argv:
        readouts()
