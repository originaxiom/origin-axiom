"""W66: the parameter-free census. B1644's Yukawa form Y(a; c) = a c^T + c a^T - (a.c) 1 with the Higgs a and the
coupling c among W65's one-unit sections E, R and R' (each unique up to scale), so every sector's Yukawa is a function
of tau alone. Every assignment of the six pairs to the up, down and charged-lepton sectors is fitted at one tau. The
rule (W66_RULE.md) was committed before this script.

  C1  the rank of each pair, at 40 digits at W65's sample (away from omega and from E's cone points)
  C2  the live assignments: only the six permutations of (EE, ER, ER') can pass
  C3  the verdict: no assignment passes (chi^2_min > 7.81 at a = 0.10)
  plus the read-outs: each permutation's minimum, the first-generation read-outs, a = 0.05 and 0.20, two at a time

Fixed here, before the run:
- E's cone points are tau_0 (W65's JSON) and its mirror -conj(tau_0), which has the same real j = 1280. C1 excludes
  sample points within 0.05 of either, and of omega.
- An assignment whose grid chi^2 is infinite everywhere (a zero mass or a zero |V| at every grid point) is recorded as
  infinite without a refinement; the refinement from the 10 best grid points runs for every other assignment.
- A ratio m2/m3 or a |V| below 10^-12 counts as zero (chi^2 = infinity). Points with y > 6 after mapping into the
  fundamental domain score infinity.

Run: python3 the_parameter_free_census.py  ->  the_parameter_free_census.json beside it.
"""
import itertools
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_second_unit as SU  # noqa: E402  (W65: the collocation, the sample, the 40-digit sections)

OUT = HERE / "the_parameter_free_census.json"
mp.mp.dps = 40
PAIRS = {"EE": ("E", "E"), "ER": ("E", "R"), "ER'": ("E", "R'"), "RR": ("R", "R"), "RR'": ("R", "R'"),
         "R'R'": ("R'", "R'")}
SECTORS = ("up", "down", "lepton")
ASSIGN = list(itertools.product(PAIRS, repeat=3))
LIVE = {p for p in itertools.permutations(("EE", "ER", "ER'"))}
ZERO = 1e-12
PASS = 7.81


# ----------------------------------------------------------------------------------------------------------- data
def load_data():
    hz = json.loads((HERE / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    ckm = json.loads((HERE / "received" / "B1612_data.json").read_text(encoding="utf-8"))["ckm_abs"]
    mv, ms = hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]
    obs, rel = [], []
    for two, three in (("c", "t"), ("s", "b"), ("mu", "tau")):
        obs.append(mv[two] / mv[three])
        rel.append(float(np.hypot(ms[two] / mv[two], ms[three] / mv[three])))
    for i, j in ((0, 1), (1, 2)):
        obs.append(ckm["value"][i][j])
        rel.append(ckm["sigma"][i][j] / ckm["value"][i][j])
    return np.log(obs), np.array(rel)


LOGD, REL = load_data()
LABELS = ["m_c/m_t", "m_s/m_b", "m_mu/m_tau", "|V_us|", "|V_cb|"]


# ----------------------------------------------------------------------------------------------------------- sections
def to_numpy(terms):
    vec = np.array([[complex(a * SU.B[l][c]) for c in range(3)] for l, e, a in terms])
    ex = np.array([float(e) for l, e, a in terms])
    return vec, ex


def ev_np(S, t):
    vec, ex = S
    return np.exp(2j * np.pi * ex * t) @ vec


def to_fd(t):
    for _ in range(100):
        t = complex(t.real - np.round(t.real), t.imag)
        if abs(t) < 1 - 1e-15:
            t = -1 / t
        else:
            break
    return t


def pair_data(t, S):
    v = {k: ev_np(S[k], t) for k in ("E", "R", "R'")}
    out = {}
    for name, (a, c) in PAIRS.items():
        Y = np.outer(v[a], v[c]) + np.outer(v[c], v[a]) - (v[a] @ v[c]) * np.eye(3)
        U, s, _ = np.linalg.svd(Y)
        out[name] = (s[::-1], U[:, ::-1])                    # ascending: m1, m2, m3 and their left states
    return out


def observables(assign, pd):
    vals = []
    for p in assign:
        s = pd[p][0]
        vals.append(s[1] / s[2])
    V = pd[assign[0]][1].conj().T @ pd[assign[1]][1]
    vals += [abs(V[0, 1]), abs(V[1, 2])]
    extra = {"|V_ub|": float(abs(V[0, 2])), "|V_td|": float(abs(V[2, 0])),
             "m1/m3 per sector": [float(pd[p][0][0] / pd[p][0][2]) for p in assign]}
    return np.array(vals), extra


def chi2_of(vals, a, which=None):
    idx = range(5) if which is None else which
    if any(vals[i] < ZERO for i in idx):
        return np.inf
    z = [(np.log(vals[i]) - LOGD[i]) / np.hypot(REL[i], a) for i in idx]
    return float(np.sum(np.square(z)))


# ----------------------------------------------------------------------------------------------------------- C1
def C1(sec, taus_excl):
    rows, ok = {}, True
    for t in SU.SAMPLE:
        if min(abs(t - u) for u in taus_excl) < 0.05:
            continue
        v = {k: sec[k](t) for k in ("E", "R", "R'")}
        row = {}
        for name, (a, c) in PAIRS.items():
            Y = SU.Yuk(v[a], v[c])
            U, S, Vh = mp.svd_c(Y)
            m1, m2 = S[2] / S[0], S[1] / S[0]
            null = [mp.conj(Vh[2, k]) for k in range(3)]
            entry = {"m1/m3": float(m1), "m2/m3": float(m2)}
            if name in ("RR", "RR'", "R'R'"):
                ok &= m2 < 1e-12
            elif name in ("ER", "ER'"):
                iso = v["R"] if name == "ER" else v["R'"]
                sn = SU.sine(null, iso)
                entry["sine of the null vector to the isotropic section"] = float(sn)
                ok &= m1 < 1e-12 and sn < 1e-10 and m2 > 1e-9
            else:
                dev = abs(S[2] * S[0] / S[1] ** 2 - 1)
                entry["|m1 m3 / m2^2 - 1|"] = float(dev)
                ok &= dev < 1e-10
            row[name] = entry
        rows[mp.nstr(t, 4)] = row
    return {"per sample point": rows, "holds": bool(ok)}


# ----------------------------------------------------------------------------------------------------------- the census
def grid():
    pts = []
    for x in np.linspace(-0.5, 0.5, 41):
        for y in np.geomspace(0.87, 6, 40):
            if abs(complex(x, y)) >= 1:
                pts.append(complex(x, y))
    return pts


def census(S, a_values):
    pts = grid()
    pds = [pair_data(t, S) for t in pts]
    table = {}
    for a in a_values:
        res = {}
        for assign in ASSIGN:
            chis = np.array([chi2_of(observables(assign, pd)[0], a) for pd in pds])
            best_grid = float(np.min(chis))
            if not np.isfinite(best_grid):
                res[assign] = {"chi2_min": np.inf, "refined": False}
                continue
            order = np.argsort(chis)[:10]

            def f(xy, assign=assign, a=a):
                t = to_fd(complex(xy[0], xy[1]))
                if t.imag > 6:
                    return 1e12
                c = chi2_of(observables(assign, pair_data(t, S))[0], a)
                return c if np.isfinite(c) else 1e12
            finals = []
            for k in order:
                r = minimize(f, [pts[k].real, pts[k].imag], method="Nelder-Mead",
                             options={"xatol": 1e-9, "fatol": 1e-10, "maxiter": 4000})
                finals.append((float(r.fun), to_fd(complex(*r.x))))
            cmin, tmin = min(finals, key=lambda z: z[0])
            cmin = min(cmin, best_grid)
            n_reach = sum(1 for c, _ in finals if c - cmin < 0.1)
            res[assign] = {"chi2_min": cmin, "tau_min": tmin, "reached by": n_reach, "refined": True}
        table[a] = res
    return table, pts, pds


def two_at_a_time(S, pts, pds):
    out = {}
    for assign in LIVE:
        if assign[0] != "ER":
            continue
        chis = np.array([chi2_of(observables(assign, pd)[0], 0.10, which=(0, 3)) for pd in pds])
        order = np.argsort(chis)[:10]

        def f(xy, assign=assign):
            t = to_fd(complex(xy[0], xy[1]))
            if t.imag > 6:
                return 1e12
            c = chi2_of(observables(assign, pair_data(t, S))[0], 0.10, which=(0, 3))
            return c if np.isfinite(c) else 1e12
        best = min((minimize(f, [pts[k].real, pts[k].imag], method="Nelder-Mead",
                             options={"xatol": 1e-9, "fatol": 1e-10, "maxiter": 4000}) for k in order),
                   key=lambda r: r.fun)
        t = to_fd(complex(*best.x))
        vals, _ = observables(assign, pair_data(t, S))
        out[" / ".join(assign)] = {"smallest z(m_c/m_t)^2 + z(V_us)^2": float(best.fun),
                                   "at tau": [t.real, t.imag], "m_c/m_t there": float(vals[0]),
                                   "|V_us| there": float(vals[3])}
    return out


# ----------------------------------------------------------------------------------------------------------- main
def main():
    w65 = json.loads((HERE / "the_second_unit.json").read_text(encoding="utf-8"))
    t0 = complex(*w65["read-outs"]["tau_0 (E on the cone)"])
    excl = [SU.OMEGA, mp.mpc(t0.real, t0.imag), mp.mpc(-t0.real, t0.imag)]
    sec, S = {}, {}
    for name, units, lead in (("E", (1, 0, 0), "e_i"), ("R'", (0, 0, 1), "v-"), ("R", (0, 1, 0), "v+")):
        terms, res = SU.solve_section(units, lead)
        sec[name] = (lambda tm: (lambda t: SU.evaluate(tm, t)))(terms)
        S[name] = to_numpy(terms)
    worst = 0.0
    for t in SU.SAMPLE:
        for k in ("E", "R", "R'"):
            hi = np.array([complex(x) for x in sec[k](t)])
            lo = ev_np(S[k], complex(t))
            worst = max(worst, float(np.linalg.norm(lo - hi) / np.linalg.norm(hi)))
    c1 = C1(sec, excl)
    table, pts, pds = census(S, (0.10, 0.05, 0.20))
    main_t = table[0.10]
    dead_ok = all(r["chi2_min"] > PASS for asg, r in main_t.items() if asg not in LIVE)
    none_pass = all(r["chi2_min"] > PASS for r in main_t.values())
    perms = {}
    for asg in sorted(LIVE):
        r = main_t[asg]
        row = {"chi2_min": r["chi2_min"], "reached by (of 10)": r.get("reached by")}
        if r.get("refined"):
            t = r["tau_min"]
            vals, extra = observables(asg, pair_data(t, S))
            row.update({"tau_min": [t.real, t.imag],
                        "observables": dict(zip(LABELS, map(float, vals))),
                        "z": dict(zip(LABELS, [float((np.log(v) - LOGD[i]) / np.hypot(REL[i], 0.10))
                                               for i, v in enumerate(vals)])),
                        "read-outs": extra})
        perms[" / ".join(asg)] = row
    counts = {a: sum(1 for r in table[a].values() if r["chi2_min"] <= PASS) for a in table}
    out = {"status": "W66: the parameter-free census (the rule W66_RULE.md first; one run)",
           "instrument: double precision against 40 digits at W65's sample (largest relative difference)": worst,
           "instrument holds (10^-10)": bool(worst < 1e-10),
           "data (log values, relative errors)": {"labels": LABELS, "log data": LOGD.tolist(),
                                                  "relative": REL.tolist()},
           "C1": c1,
           "C2": {"every non-permutation assignment above 7.81 at a = 0.10": bool(dead_ok),
                  "the smallest chi2_min among them": float(min(r["chi2_min"] for asg, r in main_t.items()
                                                                if asg not in LIVE)),
                  "holds": bool(dead_ok)},
           "C3": {"no assignment passes at a = 0.10": bool(none_pass),
                  "the smallest chi2_min of all 216": float(min(r["chi2_min"] for r in main_t.values())),
                  "holds": bool(none_pass)}}
    out["cells"] = {k: out[k]["holds"] for k in ("C1", "C2", "C3")}
    out["read-outs"] = {
        "the six permutations at a = 0.10": perms,
        "assignments passing (chi2_min <= 7.81) at a = 0.10, 0.05, 0.20": {str(a): counts[a] for a in counts},
        "the smallest chi2_min at a = 0.05 and 0.20": {str(a): float(min(r["chi2_min"] for r in table[a].values()))
                                                       for a in (0.05, 0.20)},
        "two at a time (up = ER)": two_at_a_time(S, pts, pds),
        "assignments refined at a = 0.10": sum(1 for r in main_t.values() if r["refined"]),
        "grid points": len(pts)}
    OUT.write_text(json.dumps(out, indent=1, default=lambda x: float(x) if isinstance(x, (np.floating, mp.mpf))
                              else [x.real, x.imag] if isinstance(x, complex) else str(x)) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
