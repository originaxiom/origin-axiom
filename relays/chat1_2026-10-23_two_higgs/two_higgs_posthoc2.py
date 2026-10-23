#!/usr/bin/env python3
"""POST HOC read-outs, labelled (TWO_HIGGS: written after the referee's report on the draft result note; committed before
its own run).  None is a cell.  They check, before the note states them, the referee's points:
  Q1  d = e: D over every row of the ten lines for each pair, with c = 3;
  Q2  what c = 3 builds in: the share of random six-target sets (seeds 1720-1739, main's generator, the six-targets
      only) whose lepton ratios lie within the best row's worst factor w = 1.0985 of three times and a third of their own
      down ratios (both, at w and at w^2);
  Q3  the four quark ratios alone: the off-diagonal rows' best worst factor over m_c/m_t, m_u/m_t, m_s/m_b, m_d/m_b and the
      share of random four-target sets (the same streams' first four entries) fitted as well; the same in chi-square at the
      data's own errors and with the 10% allowance (the share whose minimum over the rows is at or below the observed one;
      seeds 1720-1724);
  Q4  at the best six-row, each of the six ratios' pull at the measurement's own error, and the quarks' chi-square;
  Q5  the two directions at the best six-row: |<F_6|F_22>|, each one's distance from the isotropic v0 = (0, 1, i)/sqrt2
      (phase-aligned), the ratio of the departures' sizes and the cosine between them; |V_tb| there (main's frame);
  Q6  the matched comparison: random six-target sets fitted within the diagonal pairs' best worst factor (1.466) by the
      off-diagonal rows and by the diagonal rows; and the largest |J| over the 14 rows below the six's bar.
    python3 -B two_higgs_posthoc2.py      # writes two_higgs_posthoc2.json"""
import contextlib, hashlib, importlib.util, io, json, math, random, subprocess, sys, pathlib
import numpy as np
from scipy.spatial import cKDTree

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
m = json.loads(bd)["masses_GeV"]; v, s = m["value"], m["sigma"]; ck = json.loads(bc)["ckm_abs"]; C = ck["value"]
PAIRS6 = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T6 = np.log(np.array([v[a] / v[b] for a, b in PAIRS6]))
REL6 = np.array([math.hypot(s[a] / v[a], s[b] / v[b]) for a, b in PAIRS6])
SIG6 = np.sqrt(REL6 ** 2 + 0.10 ** 2)
IDX = json.loads((HERE / "two_higgs_index.json").read_text())
X = np.load(HERE / "two_higgs.npz")["data"].astype(np.float64)               # point, hor, model, field
TASKS, LINES, MODELS, HORS = IDX["tasks"], IDX["lines"], IDX["models"], IDX["hors"]
PAIRS = [tuple(p) for p in IDX["pairs"]]
OFF = [i for i, (u, d) in enumerate(PAIRS) if u != d]
DIAG = [i for i, (u, d) in enumerate(PAIRS) if u == d]
OUT = {}


def six_rows(models, c=3.0):
    L = X[:, :, models, 0:6] * math.log(10)
    L[..., 4] += math.log(c); L[..., 5] -= math.log(c)
    return L.reshape(-1, 6)


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


TG6 = []
for sd in range(1720, 1740):
    rng = random.Random(sd)
    d6 = np.log(np.array([r_masses(rng) for _ in range(4000)]))
    _d9 = [r_masses(rng) + r_ckm(rng) for _ in range(4000)]          # keep the stream as the comparison draws it
    TG6.append(d6)
TG6 = np.concatenate(TG6)                                            # 80 000 six-target sets

# Q1 d = e
Q1 = {}
for i, (u, d) in enumerate(PAIRS):
    L = six_rows([i])
    lnD = (L[:, 4] - L[:, 2]) + (L[:, 3] - L[:, 5])
    Q1[MODELS[i]] = {"max |ln D - ln 9|": float(np.max(np.abs(lnD - math.log(9)))), "D range": [float(np.exp(lnD.min())), float(np.exp(lnD.max()))]}
OUT["Q1 D over every row, c = 3"] = Q1

# Q2 the Georgi-Jarlskog window in random targets
w = math.log(1.0985198890573848)
g1 = np.abs(TG6[:, 4] - (TG6[:, 2] + math.log(3))); g2 = np.abs(TG6[:, 5] - (TG6[:, 3] - math.log(3)))
OUT["Q2 random six-target sets with leptons within w of 3x and x/3 their down ratios"] = {
    "w": 1.0985198890573848, "share within w (both)": float(np.mean((g1 <= w) & (g2 <= w))),
    "share within w^2 (both)": float(np.mean((g1 <= 2 * w) & (g2 <= 2 * w))), "of": int(len(TG6)),
    "the data": {"m_mu/m_tau over 3 m_s/m_b": float(math.exp(T6[4] - T6[2] - math.log(3))),
                 "m_e/m_tau over m_d/(3 m_b)": float(math.exp(T6[5] - T6[3] + math.log(3)))}}

# Q3 the four quark ratios alone
L4 = six_rows(OFF)[:, :4]
q = np.max(np.abs(L4 - T6[:4]), axis=1); w4 = float(q.min())
tree = cKDTree(L4)
d4, _ = tree.query(TG6[:, :4], k=1, p=np.inf)
Q3 = {"best worst factor over the four quark ratios": math.exp(w4), "share of random four-target sets fitted as well": float(np.mean(d4 <= w4 + 1e-12)), "of": int(len(TG6))}
for lab, sig in (("chi2 at the data's errors", REL6[:4]), ("chi2 with the 10% allowance", SIG6[:4])):
    obs = float(np.min(np.sum(((L4 - T6[:4]) / sig) ** 2, axis=1)))
    hits = 0; n = 0
    for sd in range(5):
        tg = TG6[sd * 4000:(sd + 1) * 4000, :4]
        for j in range(0, 4000, 25):
            d2 = (((L4[None, :, :] - tg[j:j + 25, None, :]) / sig[None, None, :]) ** 2).sum(axis=2)
            hits += int((d2.min(axis=1) <= obs).sum()); n += len(tg[j:j + 25])
    Q3[lab] = {"observed minimum": obs, "share of random four-target sets as good (seeds 1720-1724)": hits / n, "of": n}
OUT["Q3 the four quark ratios alone (off-diagonal rows)"] = Q3

# Q4 pulls at the best six-row
L6 = six_rows(OFF); chi = np.sum(((L6 - T6) / SIG6) ** 2, axis=1); ib = int(np.argmin(chi))
pull = (L6[ib] - T6) / REL6
OUT["Q4 pulls at the best six-row (measurement errors, no allowance)"] = {
    "order": ["m_c/m_t", "m_u/m_t", "m_s/m_b", "m_d/m_b", "m_mu/m_tau", "m_e/m_tau"], "pulls": pull.round(2).tolist(),
    "relative errors": REL6.round(5).tolist(), "chi2 of the four quark ratios": float(np.sum(pull[:4] ** 2))}

# Q6 the matched comparison and |J|
wd = math.log(1.4658539508461745)
res = {}
for lab, mods in (("off-diagonal rows", OFF), ("diagonal rows", DIAG)):
    Ls = six_rows(mods); tr = cKDTree(Ls); dd, _ = tr.query(TG6, k=1, p=np.inf)
    res[lab] = float(np.mean(dd <= wd + 1e-12))
OUT["Q6 random six-target sets fitted within 1.466 (the diagonal pairs' best six)"] = res
Jo = X[:, :, OFF, 9].reshape(-1)
OUT["Q6 largest |J| over the off-diagonal rows below the six's bar"] = float(np.abs(Jo[chi < 16.75]).max())

# Q5 the directions at the best six-row, and |V_tb|
p_idx, rest = divmod(ib, X.shape[1] * len(OFF)); h_idx, m_idx = divmod(rest, len(OFF))
k, re_t, im_t = TASKS[p_idx]
sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("tht", HERE / "two_higgs_test.py")
tht = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(tht)
u, d = PAIRS[OFF[m_idx]]
vu = tht.zfc.direction(u, re_t, im_t); vd = tht.zfc.direction(d, re_t, im_t)
v0 = np.array([0, 1, 1j]) / math.sqrt(2)


def aligned(x):
    ph = np.vdot(v0, x); return x * np.conj(ph) / abs(ph)


au, ad = aligned(vu), aligned(vd); du, dd_ = au - v0, ad - v0
a, b = tht.LINES[k]
M = tht.rbs.channels(re_t, im_t, float(a), float(b))
Yu = tht.B.coupling(tht.rbs.S_of(vu), M[("up", HORS[h_idx])]); Yd = tht.B.coupling(tht.rbs.S_of(vd), M[("down", HORS[h_idx])])
Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
OUT["Q5 the directions at the best six-row"] = {
    "row": {"pair": f"{u} | {d}", "tau": [re_t, im_t], "line": LINES[k], "hor": HORS[h_idx]},
    "|<v_u|v_d>|": float(abs(np.vdot(vu, vd))), "|v_u - v0| (phase-aligned)": float(np.linalg.norm(du)),
    "|v_d - v0| (phase-aligned)": float(np.linalg.norm(dd_)), "ratio |v_d - v0| / |v_u - v0|": float(np.linalg.norm(dd_) / np.linalg.norm(du)),
    "cosine between the departures": float(abs(np.vdot(du, dd_)) / (np.linalg.norm(du) * np.linalg.norm(dd_))),
    "|V| (rows u, c, t; columns d, s, b)": np.abs(V).round(4).tolist()}
(HERE / "two_higgs_posthoc2.json").write_text(json.dumps(OUT, indent=1) + "\n")
print("written")
