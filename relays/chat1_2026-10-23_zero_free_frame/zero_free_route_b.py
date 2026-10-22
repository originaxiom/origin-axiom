#!/usr/bin/env python3
"""EXPLORATORY, labelled (route (b) on the zero-free lines, main's P-294; written and committed before the zero-free
census's output is read): a Pati-Salam-type Higgs whose two directions are two zero-free lines of one twisted space.
Why one space: a twist multiplies the coupling by a phase under T and S, so two directions combine covariantly only
when they carry the same chi_eta^r, i.e. a = b (mod 12) (chat1's W133 check).  The spaces with one unit:
  r = 4: a in {-10, 2, 14, 26};   r = 12: a in {-6, 6, 18};   r = 20: a in {-2, 10, 22}.
The model: S_quarks = S(v_a) + kappa S(v_b), S_leptons = S(v_a) + c kappa S(v_b), c = -3 (the B - L Clebsch) or 1 (the
control), for every ordered pair (a, b), b != a, in one space (24 pairs); v_a, v_b the unit directions
(e th2^a, e th4^a, i th3^a) at tau; kappa = rho e^(i phi), log10 rho = -4.0, -3.9, ..., 1.0, phi = 0, 15, ..., 345 deg.
Readings: S~ for every sector, and the split (up S~; down quarks and leptons S).  Both horocycles.
Base points, fixed now, before the census is read: for each a, the ten distinct points among F_a's best six-rows in the
zero-free census with S~ for every sector and the by-hand Clebsch 3 (as route_b_scan chose its points for DR).
Read-out (written by this script): per (reading, c), over all pairs and points, and per first line a:
  the best six and nine, R2 and R1 at the best six-row, the baseline (rho = 1e-4), the best six where D is within
  3 sigma of P-094, the rows with R2 and R1 both in [2, 4.5] and the best six among them, and random as good (main's
  generator, seed 1720) for six and nine.
Controls: T-covariance of one pair's model; a cross-twist pair (a = 2 with b = 6) shown not covariant.
    python3 -B zero_free_route_b.py      # writes zero_free_route_b.json and zero_free_route_b_run.txt"""
import contextlib, hashlib, importlib.util, io, json, math, random, subprocess, sys, pathlib
import numpy as np
from scipy.spatial import cKDTree

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", HERE / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
rbs, B, tic = zfc.rbs, zfc.B, zfc.tic


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
v = json.loads(bd)["masses_GeV"]["value"]; C = json.loads(bc)["ckm_abs"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
P094, SIG = 10.58, 0.11
SPACES = {4: [-10, 2, 14, 26], 12: [-6, 6, 18], 20: [-2, 10, 22]}
PAIRS = [(a, b) for r, aa in SPACES.items() for a in aa for b in aa if b != a]
RHO = [10 ** (-4 + 0.1 * k) for k in range(51)]
PHI = [math.radians(15 * k) for k in range(24)]
READ = ["St-all", "split"]
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


# base points from the census (S~ for every sector, Clebsch 3 by hand)
IDX = json.loads((HERE / "zero_free_census_index.json").read_text())
X = np.load(HERE / "zero_free_census.npz")["data"].astype(np.float64)
TASKS = IDX["tasks"]


def six_stall(d):
    di = IDX["dirs"].index(d); Y = X[:, di]                                  # point, hor, field
    L = np.concatenate([Y[..., 2:4], Y[..., 6:8], Y[..., 10:12]], axis=-1) * math.log(10)   # up St, down St, lep St
    L[..., 4] += math.log(3); L[..., 5] -= math.log(3)
    return np.max(np.abs(L - T6), axis=-1)                                  # point, hor


BASE = {}
for r, aa in SPACES.items():
    for a in aa:
        s = np.min(six_stall(f"F_{a}"), axis=1)
        order = np.argsort(s)[:10]
        BASE[a] = [tuple(TASKS[int(p)]) for p in order]
OUT["base points (line index, Re, Im) per a"] = {str(a): BASE[a] for a in BASE}


def outs(M, hor, Sq, Sl, reading):
    if reading == "St-all":
        su, sd, sl = rbs.St(Sq), rbs.St(Sq), rbs.St(Sl)
    else:
        su, sd, sl = rbs.St(Sq), Sq, Sl
    Yu, Yd, Yl = B.coupling(su, M[("up", hor)]), B.coupling(sd, M[("down", hor)]), B.coupling(sl, M[("lep", hor)])
    o = []
    for Y in (Yu, Yd, Yl):
        s = np.linalg.svd(Y, compute_uv=False); o += [s[1] / s[0], s[2] / s[0]]
    return o + tic.ckm_left(Yu, Yd)


# controls
def cov(a, b, base):
    k, re_t, im_t = base
    la, lb, _ = zfc.LINES[k]
    M0, M1 = rbs.channels(re_t, im_t, la, lb), rbs.channels(re_t + 1, im_t, la, lb - la)
    va0, vb0 = zfc.direction(f"F_{a}", re_t, im_t), zfc.direction(f"F_{b}", re_t, im_t)
    va1, vb1 = zfc.direction(f"F_{a}", re_t + 1, im_t), zfc.direction(f"F_{b}", re_t + 1, im_t)
    kap = 0.05 * np.exp(0.7j); dev = 0.0
    for hor in rbs.HORS:
        for reading in READ:
            o0 = outs(M0, hor, rbs.S_of(va0) + kap * rbs.S_of(vb0), rbs.S_of(va0) - 3 * kap * rbs.S_of(vb0), reading)
            o1 = outs(M1, hor, rbs.S_of(va1) + kap * rbs.S_of(vb1), rbs.S_of(va1) - 3 * kap * rbs.S_of(vb1), reading)
            dev = max(dev, max(abs(math.log(x / y)) for x, y in zip(o0[:9], o1[:9])))
    return dev


OUT["controls"] = {"T-covariance, a = 6 with b = 18 (r = 12)": cov(6, 18, BASE[6][0]),
                   "T-covariance, a = 2 with b = 6 (r = 4 with r = 12, expected to fail)": cov(2, 6, BASE[2][0])}
say(f"controls: {OUT['controls']}")

# the scan
NROW = sum(len(BASE[a]) * (len(SPACES[(2 * a) % 24]) - 1) for a in BASE) * len(RHO) * len(PHI) * len(rbs.HORS)
res = {(rd, c): np.zeros((NROW, 10)) for rd in READ for c in (-3, 1)}   # rows: (a, b, base, rho, phi, hor) -> 10 outputs
meta = []
for a in sorted(BASE):
    r = (2 * a) % 24
    partners = [b for b in SPACES[r] if b != a]
    for base in BASE[a]:
        k, re_t, im_t = base
        la, lb, _ = zfc.LINES[k]
        M = rbs.channels(re_t, im_t, la, lb)
        va = zfc.direction(f"F_{a}", re_t, im_t); Sa = rbs.S_of(va)
        for b in partners:
            Sb = rbs.S_of(zfc.direction(f"F_{b}", re_t, im_t))
            for ir, rho in enumerate(RHO):
                for ip, phi in enumerate(PHI):
                    kap = rho * np.exp(1j * phi)
                    for ih, hor in enumerate(rbs.HORS):
                        n = len(meta); meta.append((a, b, base, ir, ip, ih))
                        for c in (-3, 1):
                            Sq, Sl = Sa + kap * Sb, Sa + c * kap * Sb
                            for rd in READ:
                                res[(rd, c)][n] = outs(M, hor, Sq, Sl, rd)
    say(f"a = {a} done")
rng = random.Random(1720)


def r_masses():
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2:
                break
        tg += [r2, r1]
    return tg


def r_ckm():
    while True:
        a_, b_, c_ = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
        if c_ < b_ < a_:
            return [a_, b_, c_]


d6 = np.log(np.array([r_masses() for _ in range(4000)]))
d9 = np.log(np.array([r_masses() + r_ckm() for _ in range(4000)]))
A_ = np.array([m[0] for m in meta]); RH = np.array([m[3] for m in meta])


def where(i):
    a, b, base, ir, ip, ih = meta[i]
    return {"a": a, "b": b, "line": zfc.LINES[base[0]][2], "tau": [base[1], base[2]], "rho": RHO[ir], "phi_deg": 15 * ip, "hor": rbs.HORS[ih]}


def summ(Xr, mask, label, calibrate):
    L = np.log(np.maximum(Xr[mask, :9], 1e-300)); J = Xr[mask, 9]; idx = np.where(mask)[0]
    six = np.max(np.abs(L[:, :6] - T6), axis=1); nine = np.max(np.abs(L - T9), axis=1)
    R2 = np.exp(L[:, 4] - L[:, 2]); R1 = np.exp(L[:, 3] - L[:, 5]); D = R2 * R1
    base0 = RH[mask] == 0
    out = {}
    for key, arr, m in (("six", six, None), ("nine", nine, None), ("six, D at P-094", six, np.abs(D - P094) <= 3 * SIG),
                        ("six, R2 and R1 in [2, 4.5]", six, (R2 >= 2) & (R2 <= 4.5) & (R1 >= 2) & (R1 <= 4.5)),
                        ("baseline six (rho 1e-4)", six, base0)):
        a2 = np.where(m, arr, np.inf) if m is not None else arr
        i = int(np.argmin(a2))
        out[key] = None if not np.isfinite(a2[i]) else {"value": math.exp(a2[i]), "n_rows": int(m.sum()) if m is not None else int(arr.size),
                                                        "R2": float(R2[i]), "R1": float(R1[i]), "D": float(D[i]), "J": float(J[i]),
                                                        "six": math.exp(six[i]), "nine": math.exp(nine[i]), "where": where(int(idx[i])),
                                                        "model_over_measured": np.exp(L[i] - T9).round(3).tolist()}
    if calibrate:
        q6, _ = cKDTree(L[:, :6]).query(d6, k=1, p=np.inf); q9, _ = cKDTree(L).query(d9, k=1, p=np.inf)
        out["six random as good"] = float(np.mean(q6 <= np.min(six) + 1e-12)); out["nine random as good"] = float(np.mean(q9 <= np.min(nine) + 1e-12))
    s6, s9, sd, sg = out["six"], out["nine"], out["six, D at P-094"], out["six, R2 and R1 in [2, 4.5]"]
    say(f"{label}: six {s6['value']:.3f} (R2 {s6['R2']:.2f}, R1 {s6['R1']:.2f}, D {s6['D']:.2f}; nine there {s6['nine']:.2f}) at {s6['where']}; "
        f"nine {s9['value']:.3f} (J {s9['J']:.1e}); baseline six {out['baseline six (rho 1e-4)']['value']:.3f}; D-matched "
        + (f"{sd['value']:.3f} ({sd['n_rows']} rows; R2 {sd['R2']:.2f}, R1 {sd['R1']:.2f})" if sd else "none")
        + "; GJ-ratio " + (f"{sg['n_rows']} rows, best six {sg['value']:.3f}" if sg else "none")
        + (f"; random as good {out['six random as good']:.4f} / {out['nine random as good']:.4f}" if calibrate else ""))
    return out


OUT["summaries"] = {}
assert len(meta) == NROW
for (rd, c), Xr in res.items():
    OUT["summaries"][f"{rd} c={c} all pairs"] = summ(Xr, np.ones(len(Xr), dtype=bool), f"{rd}, Clebsch {c}, all pairs", True)
    for a in sorted(BASE):
        OUT["summaries"][f"{rd} c={c} a={a}"] = summ(Xr, A_ == a, f"   {rd}, Clebsch {c}, first line a = {a}", False)
(HERE / "zero_free_route_b.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "zero_free_route_b_run.txt").write_text("\n".join(LOG) + "\n")
