#!/usr/bin/env python3
"""chat1, 2026-10-21 -- the leptons at the quark-fixed tau under PF1-W.  The rule is LEPTON_TEST_RULE.md (2c1e16790), committed
and pushed before this script.  One run; its output (lepton_test.json, lepton_test_run.txt) is committed before it is
read.

The SM seat's code is imported unchanged (the_strong_angle.py, the_tuned_fit.py at c9f001d9d, hash-checked), as in
zero_free_checks.py.  Pre-run: this script was only compiled (py_compile); no part of it was run before the run.

Stages: Q (the quark-fixed tau of W114's assignments 11, 13, 14); L (the ten lepton pairs at each tau*); cells L0-L5.
"""
import hashlib
import json
import math
import subprocess
import sys
import tempfile
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import mpmath as mp
from scipy.stats import chi2 as CHI2

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
COMMIT = "c9f001d9ded23c059fae7d4475c98231404fec45"
SRC = "docs/dossiers/the_weave_2026-10-07/"
PINS = {"the_strong_angle.py": "a9c4b15b82739289b4698a388da117d4c517380826fcacfc16c6065221028622",
        "the_tuned_fit.py": "21f979beccd96c5470109d91579eff17af289c6951ed7485822a84e2149c713b",
        "received/HZ2021_running_masses_MZ.json": None, "received/B1612_data.json": None}
T0 = time.time()
OUT = {"rule": "LEPTON_TEST_RULE.md", "script": "lepton_test.py", "sm_commit": COMMIT}


def log(*a):
    print(f"[{time.time() - T0:8.1f}s]", *a, flush=True)


TMP = Path(tempfile.mkdtemp(prefix="lt_sm_"))
for name, pin in PINS.items():
    blob = subprocess.check_output(["git", "-C", str(REPO), "show", f"{COMMIT}:{SRC}{name}"])
    h = hashlib.sha256(blob).hexdigest()
    if pin is not None and h != pin:
        raise SystemExit(f"hash mismatch for {name}: {h}")
    (TMP / name).parent.mkdir(parents=True, exist_ok=True)
    (TMP / name).write_bytes(blob)
    OUT.setdefault("sha256", {})[name] = h
sys.path.insert(0, str(TMP))
import the_strong_angle as SA  # noqa: E402
import the_tuned_fit as TF  # noqa: E402

mp.mp.dps = 30
A_ALLOW = 0.10
P_, M_ = 1, -1
TT, BB, MQT, MQB = (P_, P_), (M_, M_), (P_, M_), (M_, P_)
QUARK = {11: (MQB, 4, BB, 7), 13: (BB, 7, MQB, 4), 14: (BB, 3, BB, 7)}

# ------------------------------------------------------------------------------------------- data
HZ = json.loads((TMP / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
MV, MS = HZ["masses_GeV"]["value"], HZ["masses_GeV"]["sigma"]
CH_OBS = [MV["e"] / MV["mu"], MV["mu"] / MV["tau"]]
CH_REL = [float(np.hypot(MS["e"] / MV["e"], MS["mu"] / MV["mu"])), float(np.hypot(MS["mu"] / MV["mu"], MS["tau"] / MV["tau"]))]
NU = {"NO": {"s12": (0.308, 0.0115), "s13": (0.02215, 0.00057), "s23": (0.470, 0.015), "d21": (7.49e-5, 0.19e-5),
             "d3l": (2.513e-3, 0.020e-3), "pen": 0.0},
      "IO": {"s12": (0.308, 0.0115), "s13": (0.02231, 0.00056), "s23": (0.550, 0.0135), "d21": (7.49e-5, 0.19e-5),
             "d3l": (2.484e-3, 0.020e-3), "pen": 6.1}}
DATA = {}
for o, d in NU.items():
    r = d["d21"][0] / d["d3l"][0]
    rr = float(np.hypot(d["d21"][1] / d["d21"][0], d["d3l"][1] / d["d3l"][0]))
    obs = CH_OBS + [d["s12"][0], d["s13"][0], d["s23"][0], r]
    rel = CH_REL + [d["s12"][1] / d["s12"][0], d["s13"][1] / d["s13"][0], d["s23"][1] / d["s23"][0], rr]
    DATA[o] = (np.log(np.array(obs)), np.array(rel), d["pen"])
OUT["data"] = {o: {"obs": np.exp(v[0]).tolist(), "rel": v[1].tolist(), "IO penalty": v[2]} for o, v in DATA.items()}
LAB = ["m_e/m_mu", "m_mu/m_tau", "s12^2", "s13^2", "s23^2", "r"]


# ------------------------------------------------------------------------------------------- the Weinberg sector (symmetric part)
def sym_basis(rb, d):
    from sympy import Matrix, Rational
    mons = SA.normal_monomials(d)
    idx = {mon: n for n, mon in enumerate(mons)}
    nm_ = len(mons)
    cols = []
    for B in rb:
        v = [Rational(0)] * (9 * nm_)
        for i in range(3):
            for j in range(3):
                for mon, x in B[i][j].items():
                    v[(3 * i + j) * nm_ + idx[mon]] += Rational(x.numerator, x.denominator)
                for mon, x in B[j][i].items():
                    v[(3 * i + j) * nm_ + idx[mon]] -= Rational(x.numerator, x.denominator)
        cols.append(v)
    ns = Matrix(cols).T.nullspace()
    return np.array([[float(Fraction(int(z.p), int(z.q))) for z in vec] for vec in ns]).T   # n x s


class SymParam:
    """the symmetric part of a (s, s) sector, with PF1-W's variety at w = 12"""

    def __init__(self, typ, k, rng):
        self.base = TF.SectorParam(typ, k, rng)
        basis, d = SA.space(typ[0], typ[1], k)
        _, rb = SA.real_basis(basis, d)
        self.Bm = sym_basis(rb, d)
        self.s = self.Bm.shape[1]
        self.tuned = self.base.tuned
        self.S = self.base.S
        self.label = "sym " + self.base.label
        self.nfree = 0 if self.s == 1 else self.s
        self.p = self.s - 1 - int(self.tuned)
        if self.tuned:
            self.As = np.einsum("ijk,ia,jb,kc->abc", self.base.As, self.Bm, self.Bm, self.Bm)
            scale = float(np.max(np.abs(self.As)))
            while True:
                e = rng.normal(size=self.s)
                e /= np.linalg.norm(e)
                if abs(np.einsum("abc,a,b,c->", self.As, e, e, e)) > 1e-3 * scale:
                    break
            self.e = e

    def coeffs(self, v):
        if self.s == 1:
            return self.Bm[:, 0] / np.linalg.norm(self.Bm[:, 0])
        v = np.asarray(v, dtype=float)
        if not self.tuned:
            c = v
        else:
            A, e = self.As, self.e
            co = [np.einsum("abc,a,b,c->", A, e, e, e), 3 * np.einsum("abc,a,b,c->", A, v, e, e),
                  3 * np.einsum("abc,a,b,c->", A, v, v, e), np.einsum("abc,a,b,c->", A, v, v, v)]
            r = np.roots(co)
            sc = max(1.0, float(np.max(np.abs(r)))) if r.size else 1.0
            real = [x.real for x in r if abs(x.imag) <= 1e-9 * sc]
            if not real:
                return None
            c = v + min(real, key=abs) * e
        full = self.Bm @ c
        n = np.linalg.norm(full)
        return full / n if n > 1e-12 else None


class ChargedParam:
    def __init__(self, typ, k, rng):
        self.base = TF.SectorParam(typ, k, rng)
        self.S, self.tuned, self.label = self.base.S, self.base.tuned, self.base.label
        self.nfree = self.base.nfree
        self.p = self.base.dim - 1 - int(self.tuned)

    def coeffs(self, v):
        return self.base.coeffs(v)


# ------------------------------------------------------------------------------------------- lepton observables
def lepton_obs(Ye, Yn):
    Ue, se, _ = np.linalg.svd(Ye)
    Ue, se = Ue[:, ::-1], se[::-1]            # ascending: e, mu, tau
    Un, sn, _ = np.linalg.svd(Yn)
    Un, sn = Un[:, ::-1], sn[::-1]            # ascending n0 < n1 < n2
    P = np.conj(Ue.T) @ Un
    n0, n1, n2 = sn ** 2
    if n1 - n0 < n2 - n1:
        order, cols, r = "NO", [0, 1, 2], (n1 - n0) / (n2 - n0)
    else:
        order, cols, r = "IO", [1, 2, 0], (n2 - n1) / (n2 - n0)
    P = P[:, cols]
    s13 = abs(P[0, 2]) ** 2
    s12 = abs(P[0, 1]) ** 2 / (1 - s13)
    s23 = abs(P[1, 2]) ** 2 / (1 - s13)
    obs = np.array([se[0] / se[1], se[1] / se[2], s12, s13, s23, r])
    return obs, order, P, sn[cols], Ue


def chi2_of(obs, order, a=A_ALLOW, data=None):
    logd, rel, pen = (data or DATA)[order]
    if not np.all(np.isfinite(obs)) or np.any(obs < 1e-12):
        return math.inf
    z = (np.log(obs) - logd) / np.hypot(rel, a)
    return float(np.sum(z * z) + pen)


class Pair:
    def __init__(self, ch, wb):
        self.ch, self.wb = ch, wb
        self.p = ch.p + wb.p
        self.dof = 6 - self.p
        self.label = f"{ch.label} | {wb.label}"

    def mats(self, v, U, E):
        ce = self.ch.coeffs(v[:self.ch.nfree]) if self.ch.nfree else np.array([1.0])
        cn = self.wb.coeffs(v[self.ch.nfree:])
        if ce is None or cn is None:
            return None
        return self.ch.S.Y(U, E, ce)[0], self.wb.S.Y(U, E, cn)[0]

    def evaluate(self, v, U, E):
        m = self.mats(v, U, E)
        if m is None:
            return None
        return lepton_obs(*m)

    def chi2(self, v, U, E, a=A_ALLOW, data=None):
        r = self.evaluate(v, U, E)
        if r is None:
            return 1e30
        c = chi2_of(r[0], r[1], a, data)
        return c if np.isfinite(c) else 1e30


def fit_pair(pair, U, E, rng, a=A_ALLOW, data=None, n1=4000, n2=20, n3=3, maxfev=4000):
    nv = pair.ch.nfree + pair.wb.nfree
    if nv == 0:
        return np.zeros(0), pair.chi2(np.zeros(0), U, E, a, data)
    V = rng.normal(size=(n1, nv))
    vals = np.array([pair.chi2(v, U, E, a, data) for v in V])
    order = np.argsort(vals)
    f = lambda v: pair.chi2(v, U, E, a, data)  # noqa: E731
    s2 = sorted((TF.nm(f, V[i], maxfev) for i in order[:n2]), key=lambda t: t[1])
    s3 = sorted((TF.nm(f, p, maxfev) for p, _ in s2[:n3]), key=lambda t: t[1])
    return s3[0]


def readout(pair, v, U, E, taus_check):
    obs, order, P, sn, Ue = pair.evaluate(v, U, E)
    s12, s13, s23 = obs[2], obs[3], obs[4]
    c12, c13, c23 = math.sqrt(1 - s12), math.sqrt(1 - s13), math.sqrt(1 - s23)
    J = float((P[0, 0] * P[1, 1] * np.conj(P[0, 1]) * np.conj(P[1, 0])).imag)
    denom = math.sqrt(s12 * s23 * s13) * c12 * c23 * c13 ** 2
    sind = J / denom if denom > 0 else float("nan")
    cosd = ((abs(P[1, 0]) ** 2) - s12 * c23 ** 2 - c12 ** 2 * s23 * s13) / (2 * math.sqrt(s12 * s23 * s13) * c12 * c23) \
        if denom > 0 else float("nan")
    delta = math.degrees(math.atan2(sind, cosd)) % 360
    # the scale from |Delta m^2_3l|
    m2 = sn ** 2
    d3l = NU[order]["d3l"][0]
    scale2 = d3l / (abs(m2[2] - m2[0]) if order == "NO" else abs(m2[1] - m2[2]))
    masses = np.sqrt(m2 * scale2)
    ce = pair.ch.coeffs(v[:pair.ch.nfree]) if pair.ch.nfree else np.array([1.0])
    cn = pair.wb.coeffs(v[pair.ch.nfree:])
    Yn = pair.wb.S.Y(U, E, cn)[0]
    Mn = Yn * math.sqrt(scale2)
    # m_bb in the charged-lepton mass basis (W = conj(Ue), rows L): |(Ue^dagger M_nu conj(Ue))_ee|
    mbb = float(abs((np.conj(Ue.T) @ Mn @ np.conj(Ue))[0, 0]))
    # PF1-W at the best point: det / eta^(6k) constant across three tau
    dets = []
    for t in taus_check:
        Ut, Et = SA.u_eta_np(np.array([t]))
        Ye_t, Yn_t = pair.ch.S.Y(Ut, Et, ce)[0], pair.wb.S.Y(Ut, Et, cn)[0]
        dets.append((np.linalg.det(Ye_t) / Et[0] ** (6 * pair.ch.base.k), np.linalg.det(Yn_t) / Et[0] ** (6 * pair.wb.base.k)))
    spread_e = max(abs(d[0] - dets[0][0]) for d in dets) / abs(dets[0][0])
    spread_n = max(abs(d[1] - dets[0][1]) for d in dets) / abs(dets[0][1])
    return {"order": order, "observables": dict(zip(LAB, obs.tolist())), "J (convention: P = Ue^dagger U_nu)": J,
            "delta_deg (same convention)": delta, "m_lightest/m_heaviest": float(min(masses) / max(masses)),
            "masses_eV (nu1, nu2, nu3)": masses.tolist(), "sum_m_nu_eV": float(np.sum(masses)), "m_bb_eV": mbb,
            "PF1-W: det Y_e/eta^(6k) spread": float(spread_e), "PF1-W: det Y_nu/eta^(6k) spread": float(spread_n),
            "L2 holds here": bool(spread_e < 1e-8 and spread_n < 1e-8 and min(masses) > 0)}


# ------------------------------------------------------------------------------------------- stage Q
log("stage Q")
secs = {}


def sec(typ, k, rng):
    if (typ, k) not in secs:
        secs[(typ, k)] = TF.SectorParam(typ, k, rng)
    return secs[(typ, k)]


rngQ = np.random.default_rng(2110)
QOUT, TAUS = {}, []
for num, (ut, uk, dt, dk) in QUARK.items():
    t = time.time()
    model = TF.Model(sec(ut, uk, rngQ), sec(dt, dk, rngQ))
    rng = np.random.default_rng(2110 + num)
    P1 = TF.random_starts(model, rng, 40000)
    v1 = TF.stage1(model, P1, SA.LOGD, A_ALLOW)
    order = np.argsort(v1)
    f = lambda p, model=model: model.chi2(p, SA.LOGD, A_ALLOW)  # noqa: E731
    ends = []
    for i in order[:200]:
        p, v = TF.nm(f, P1[i], 6000)
        p, v = TF.nm(f, p, 6000)
        ends.append((p, v))
    kept = [(p, v) for p, v in ends if v <= 3.84]
    found = []
    for p, v in sorted(kept, key=lambda t: t[1]):
        tf = SA.to_fd(complex(p[0], p[1]))
        key = complex(abs(tf.real), tf.imag)
        if all(abs(key - q["key"]) > 1e-3 for q in found):
            found.append({"key": key, "tau": [tf.real, tf.imag], "chi2": v})
    QOUT[str(num)] = {"endpoints": len(ends), "kept (chi2 <= 3.84)": len(kept), "best chi2": min(v for _, v in ends),
                      "distinct tau*": [{"tau": q["tau"], "chi2": q["chi2"]} for q in found], "seconds": time.time() - t}
    for q in found:
        TAUS.append({"assignment": num, "tau": complex(q["tau"][0], q["tau"][1]), "chi2_q": q["chi2"]})
    log(f"assignment {num}", QOUT[str(num)]["kept (chi2 <= 3.84)"], "kept;", len(found), "distinct tau*;",
        "best", QOUT[str(num)]["best chi2"])
L1 = (QOUT["11"]["best chi2"] <= 1e-6 and QOUT["13"]["best chi2"] <= 1e-6 and QOUT["14"]["best chi2"] <= 3.84)
OUT["stage Q"] = QOUT
OUT["L1"] = {"holds": bool(L1), "distinct tau* (all assignments)": len(TAUS)}

# ------------------------------------------------------------------------------------------- the ten pairs
rngL = np.random.default_rng(2111)
CH = {+1: [(TT, 5), (MQT, 4)], -1: [(BB, 3), (BB, 7), (MQB, 4)]}
WB = {+1: [(TT, 1), (TT, 5)], -1: [(BB, 3), (BB, 7)]}
PAIRS = []
for sL in (+1, -1):
    for ct, ck in CH[sL]:
        for wt, wk in WB[sL]:
            ch = ChargedParam(ct, ck, rngL)
            ch.base.k = ck
            wb = SymParam(wt, wk, rngL)
            wb.base.k = wk
            PAIRS.append(Pair(ch, wb))
OUT["pairs"] = [{"pair": p.label, "free": p.p, "dof": p.dof} for p in PAIRS]
log("pairs", [(p.label, p.p, p.dof) for p in PAIRS])

# ------------------------------------------------------------------------------------------- L0 the control
log("L0")
ctrl = next(p for p in PAIRS if p.ch.label == "Tbar(x)Tbar k=3" and p.wb.label == "sym Tbar(x)Tbar k=3")
U0, E0 = SA.u_eta_np(np.array([TAUS[0]["tau"]]))
rc = np.random.default_rng(2112)
synth = None
for _ in range(2000):
    v = rc.normal(size=ctrl.ch.nfree + ctrl.wb.nfree)
    r = ctrl.evaluate(v, U0, E0)
    if r is not None and np.all(r[0] > 1e-6) and np.all(r[0] < 0.99):
        synth = (v, r)
        break
sdata = dict(DATA)
sdata[synth[1][1]] = (np.log(synth[1][0]), DATA[synth[1][1]][1], 0.0)
other = "IO" if synth[1][1] == "NO" else "NO"
sdata[other] = (DATA[other][0], DATA[other][1], 1e6)
pb, vb = fit_pair(ctrl, U0, E0, np.random.default_rng(2113), data=sdata)
OUT["L0"] = {"synthetic observables": synth[1][0].tolist(), "order": synth[1][1], "chi2_min": vb, "holds": bool(vb <= 0.01)}
log("L0", vb)

# ------------------------------------------------------------------------------------------- stage L
log("stage L")
rows = []
CHECK = [complex(0.137, 1.291), complex(-0.284, 2.173), complex(0.41, 0.95)]
for ti, T in enumerate(TAUS):
    U, E = SA.u_eta_np(np.array([T["tau"]]))
    for pi_, pair in enumerate(PAIRS):
        rng = np.random.default_rng(3000 + 100 * ti + pi_)
        pbest, vbest = fit_pair(pair, U, E, rng)
        rec = {"assignment": T["assignment"], "tau*": [T["tau"].real, T["tau"].imag], "pair": pair.label,
               "free": pair.p, "dof": pair.dof, "chi2_min (a = 0.10)": vbest}
        for a2 in (0.05, 0.20):
            rec[f"chi2_min (a = {a2})"] = fit_pair(pair, U, E, np.random.default_rng(5000 + 100 * ti + pi_), a=a2,
                                                   n1=2000, n2=10, n3=2)[1]
        if vbest < 1e29:
            rec["best point"] = readout(pair, pbest, U, E, CHECK)
            rec["params"] = pbest.tolist()
        if pair.dof >= 1:
            rec["pass mark"] = float(CHI2.ppf(0.95, pair.dof))
            rec["passes"] = bool(vbest <= rec["pass mark"])
        else:
            rec["pass mark"] = "3.84 (compatibility only)"
            rec["compatible"] = bool(vbest <= 3.84)
        rows.append(rec)
        log(f"tau* {ti} ({T['assignment']})", pair.label, "dof", pair.dof, "chi2", round(vbest, 3),
            "pass" if rec.get("passes") else ("compat" if rec.get("compatible") else "-"))
OUT["stage L"] = rows
tested = [r for r in rows if r["dof"] >= 1]
passes = [r for r in tested if r["passes"]]
L2 = all(r.get("best point", {}).get("L2 holds here", False) for r in rows if "best point" in r)
OUT["L2"] = {"holds": bool(L2)}
OUT["L3"] = {"tests with dof >= 1": len(tested), "passes": len(passes), "holds": bool(len(passes) == 0),
             "compatible at dof 0": sum(1 for r in rows if r.get("compatible"))}

# ------------------------------------------------------------------------------------------- L5 the random-target control
log("L5")
L5 = []
for r in passes:
    pair = next(p for p in PAIRS if p.label == r["pair"])
    T = complex(*r["tau*"])
    U, E = SA.u_eta_np(np.array([T]))
    rt = np.random.default_rng(7000 + len(L5))
    better, n = 0, 0
    while n < 200:
        tg = {}
        for o in ("NO", "IO"):
            logd = DATA[o][0] + rt.uniform(-math.log(10) / 2, math.log(10) / 2, size=6)
            tg[o] = logd
        if any(np.any(np.exp(tg[o][2:5]) > 0.99) for o in tg):
            continue
        td = {o: (tg[o], DATA[o][1], DATA[o][2]) for o in tg}
        _, v = fit_pair(pair, U, E, np.random.default_rng(8000 + n), data=td, n1=1000, n2=5, n3=1)
        better += int(v <= r["chi2_min (a = 0.10)"])
        n += 1
    L5.append({"pair": r["pair"], "tau*": r["tau*"], "f": better / n})
    log("L5", r["pair"], r["tau*"], better / n)
OUT["L5"] = L5
OUT["cells"] = {"L0": OUT["L0"]["holds"], "L1": OUT["L1"]["holds"], "L2": OUT["L2"]["holds"], "L3": OUT["L3"]["holds"]}
OUT["seconds"] = time.time() - T0
(HERE / "lepton_test.json").write_text(json.dumps(OUT, indent=1, default=str))
log("cells", OUT["cells"], "L3", OUT["L3"])
log("written lepton_test.json")
