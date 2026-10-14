"""W69: the weighted census. W66's parameter-free census extended to every pair of W68's seven parameter-free sections
(E, R, R' at weight -1/2; F_i, F+, F- at 3/2; G at 7/2): 28 pairs, 28^3 assignments to the up, down and lepton sectors,
each fitted at one tau with W66's observables, data, tolerance and pass mark. The rule (W69_RULE.md) was committed
before this script.

  J1  the instrument: double precision against 40 digits at W65's sample, for all seven sections
  J2  W66 inside W69: W66's best assignment refined here reaches W66's 308.6 within 1%
  J3  the verdict: no assignment passes at a = 0.10
  plus the read-outs: the ten best, the unfitted values at the best, a = 0.05 and 0.20, the best by weight

Run: python3 the_weighted_census.py  ->  the_weighted_census.json beside it.
"""
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_second_unit as SU  # noqa: E402  (W65: the 40-digit evaluation and the sample)
import the_parameter_free_census as PF  # noqa: E402  (W66: the data, the domain map, the grid)
import the_residual_charges_at_omega as RC  # noqa: E402  (W68: the collocation at any weight)

OUT = HERE / "the_weighted_census.json"
mp.mp.dps = 40
SECTIONS = [("E", Fraction(-1, 2), (1, 0, 0)), ("R", Fraction(-1, 2), (0, 1, 0)), ("R'", Fraction(-1, 2), (0, 0, 1)),
            ("F_i", Fraction(3, 2), (1, 0, 0)), ("F+", Fraction(3, 2), (0, 1, 0)), ("F-", Fraction(3, 2), (0, 0, 1)),
            ("G", Fraction(7, 2), (0, 0, 0))]
NAMES = [n for n, _, _ in SECTIONS]
WEIGHT = {n: k for n, k, _ in SECTIONS}
PAIRS = list(itertools.combinations_with_replacement(NAMES, 2))
PNAME = [f"{a}{b}" for a, b in PAIRS]
PASS = 7.81
OMEGA = complex(-0.5, np.sqrt(3) / 2)
W66_BEST = [(("E", "R'"), ("E", "R"), ("E", "E")), (("E", "R"), ("E", "R'"), ("E", "E"))]


def solve_all():
    sec, S = {}, {}
    for name, k, u in SECTIONS:
        order = [l for l, on in zip(SU.LINES, u) if on] + [l for l, on in zip(SU.LINES, u) if not on]
        best = None
        for line in order:
            terms, res = RC.solve(u, k, line)
            if best is None or res < best[1]:
                best = (terms, res)
            if res < 1e-20:
                break
        sec[name] = (lambda tm: (lambda t: SU.evaluate(tm, t)))(best[0])
        S[name] = PF.to_numpy(best[0])
    return sec, S


def values_on(S, ts):
    out = {}
    for n in NAMES:
        vec, ex = S[n]
        out[n] = np.exp(2j * np.pi * np.outer(ts, ex)) @ vec           # (len(ts), 3)
    return out


def pair_arrays(vals):
    R2, U = [], []
    for a, b in PAIRS:
        va, vb = vals[a], vals[b]
        Y = va[:, :, None] * vb[:, None, :] + vb[:, :, None] * va[:, None, :]
        Y -= np.einsum("ti,ti->t", va, vb)[:, None, None] * np.eye(3)[None]
        u, s, _ = np.linalg.svd(Y)
        s, u = s[:, ::-1], u[:, :, ::-1]                               # ascending
        R2.append(s[:, 1] / s[:, 2])
        U.append(u)
    return np.array(R2), np.array(U)                                    # (28, T), (28, T, 3, 3)


def zterm(x, i, a):
    with np.errstate(divide="ignore", invalid="ignore"):
        z = ((np.log(np.maximum(x, 1e-300)) - PF.LOGD[i]) / np.hypot(PF.REL[i], a)) ** 2
    return np.where((x < 1e-12) | ~np.isfinite(z), np.inf, z)      # a zero or undefined value scores infinity


def grid_tables(R2, U, a):
    zm = [zterm(R2, s, a) for s in range(3)]                             # each (28, T)
    zckm = np.empty((len(PAIRS), len(PAIRS), R2.shape[1]))
    for pu in range(len(PAIRS)):
        V = np.einsum("tji,qtjk->qtik", U[pu].conj(), U)                 # (28, T, 3, 3)
        zckm[pu] = zterm(np.abs(V[:, :, 0, 1]), 3, a) + zterm(np.abs(V[:, :, 1, 2]), 4, a)
    return zm, zckm


def chi_over_grid(zm, zckm, pu, pd, pe):
    return zm[0][pu] + zm[1][pd] + zm[2][pe] + zckm[pu, pd]


def observables(S, assign, t):
    names = sorted({n for pr in assign for n in PAIRS[pr]})
    vals = {n: PF.ev_np(S[n], t) for n in names}
    out = []
    for pr in assign:
        a, b = PAIRS[pr]
        Y = np.outer(vals[a], vals[b]) + np.outer(vals[b], vals[a]) - (vals[a] @ vals[b]) * np.eye(3)
        u, s, _ = np.linalg.svd(Y)
        out.append((s[::-1], u[:, ::-1]))
    V = out[0][1].conj().T @ out[1][1]
    obs = np.array([o[0][1] / o[0][2] for o in out] + [abs(V[0, 1]), abs(V[1, 2])])
    extra = {"m1/m3 per sector": [float(o[0][0] / o[0][2]) for o in out],
             "|V_ub|": float(abs(V[0, 2])), "|V_td|": float(abs(V[2, 0]))}
    return obs, extra


def chi2(obs, a):
    if np.any(obs < 1e-12):
        return np.inf
    return float(np.sum(((np.log(obs) - PF.LOGD) / np.hypot(PF.REL, a)) ** 2))


def refine(S, assign, starts, a):
    def f(xy):
        t = PF.to_fd(complex(xy[0], xy[1]))
        if t.imag > 6:
            return 1e12
        c = chi2(observables(S, assign, t)[0], a)
        return c if np.isfinite(c) else 1e12
    finals = []
    for t0 in starts:
        r = minimize(f, [t0.real, t0.imag], method="Nelder-Mead",
                     options={"xatol": 1e-9, "fatol": 1e-10, "maxiter": 4000})
        finals.append((float(r.fun), PF.to_fd(complex(*r.x))))
    cmin, tmin = min(finals, key=lambda z: z[0])
    return cmin, tmin, sum(1 for c, _ in finals if c - cmin < 0.1)


def census(S, pts, R2, U, a):
    zm, zckm = grid_tables(R2, U, a)
    n = len(PAIRS)
    gridmin = np.empty((n, n, n))
    for pu in range(n):
        arr = zm[0][pu][None, None, :] + zm[1][:, None, :] + zm[2][None, :, :] + zckm[pu][:, None, :]
        gridmin[pu] = arr.min(axis=2)
    flat = sorted(((gridmin[idx], idx) for idx in np.ndindex(gridmin.shape)), key=lambda z: z[0])
    chosen = {idx for _, idx in flat[:50]} | {idx for v, idx in flat if v < 3 * PASS}
    chosen |= {tuple(PAIRS.index(tuple(sorted(p, key=NAMES.index))) for p in asg) for asg in W66_BEST}
    refined = {}
    for idx in chosen:
        if not np.isfinite(gridmin[idx]):
            refined[idx] = (np.inf, None, 0)
            continue
        chis = chi_over_grid(zm, zckm, *idx)
        starts = [pts[k] for k in np.argsort(chis)[:10]]
        c, t, nr = refine(S, idx, starts, a)
        refined[idx] = (min(c, float(gridmin[idx])), t, nr)
    return gridmin, refined


def label(idx):
    return " / ".join(PNAME[p] for p in idx)


def main():
    sec, S = solve_all()
    worst = 0.0
    for t in SU.SAMPLE:
        for n in NAMES:
            hi = np.array([complex(x) for x in sec[n](t)])
            lo = PF.ev_np(S[n], complex(t))
            worst = max(worst, float(np.linalg.norm(lo - hi) / np.linalg.norm(hi)))
    j1 = {"largest relative difference": worst, "holds": bool(worst < 1e-10)}
    pts = PF.grid()
    vals = values_on(S, np.array(pts))
    R2, U = pair_arrays(vals)
    results = {a: census(S, pts, R2, U, a) for a in (0.10, 0.05, 0.20)}
    gridmin, refined = results[0.10]
    w66 = tuple(PAIRS.index(tuple(sorted(p, key=NAMES.index))) for p in W66_BEST[0])
    j2_val = refined[w66][0]
    j2 = {"W66's best (ER' / ER / EE) refined here": j2_val, "W66's value": 308.6316042400572,
          "holds": bool(abs(j2_val - 308.6316042400572) / 308.6316042400572 < 0.01)}
    best_refined = min(v[0] for v in refined.values())
    unrefined_min = min(float(gridmin[idx]) for idx in np.ndindex(gridmin.shape) if idx not in refined)
    j3 = {"the smallest refined chi2_min": best_refined, "the smallest unrefined grid minimum": unrefined_min,
          "assignments refined": len(refined),
          "holds": bool(best_refined > PASS and unrefined_min > 3 * PASS)}
    top = sorted(refined.items(), key=lambda kv: kv[1][0])[:10]
    ten = []
    for idx, (c, t, nr) in top:
        row = {"assignment (up / down / lepton)": label(idx), "chi2_min": c, "reached by (of 10)": nr,
               "weights": sorted({str(WEIGHT[n]) for p in idx for n in PAIRS[p]})}
        if t is not None:
            obs, extra = observables(S, idx, t)
            row.update({"tau_min": [t.real, t.imag], "distance from omega": float(min(abs(t - OMEGA),
                                                                                        abs(t - OMEGA - 1))),
                        "observables": dict(zip(PF.LABELS, map(float, obs))),
                        "z": dict(zip(PF.LABELS, [float((np.log(o) - PF.LOGD[i]) / np.hypot(PF.REL[i], 0.10))
                                                  for i, o in enumerate(obs)])),
                        "unfitted": extra})
        ten.append(row)
    by_weight = {}
    for cls, test in (("only weight -1/2", lambda ns: all(WEIGHT[n] == Fraction(-1, 2) for n in ns)),
                      ("with a weight 3/2 section", lambda ns: any(WEIGHT[n] == Fraction(3, 2) for n in ns)),
                      ("with the weight 7/2 section", lambda ns: any(WEIGHT[n] == Fraction(7, 2) for n in ns))):
        vals_c = [refined[idx][0] if idx in refined else float(gridmin[idx])
                  for idx in np.ndindex(gridmin.shape) if test({n for p in idx for n in PAIRS[p]})]
        by_weight[cls] = float(min(vals_c))
    other = {}
    for a in (0.05, 0.20):
        gm, rf = results[a]
        other[str(a)] = {"best chi2_min": float(min(v[0] for v in rf.values())),
                         "assignments passing": sum(1 for v in rf.values() if v[0] <= PASS),
                         "best assignment": label(min(rf.items(), key=lambda kv: kv[1][0])[0])}
    out = {"status": "W69: the weighted census (the rule W69_RULE.md first; one run)", "J1": j1, "J2": j2, "J3": j3}
    out["cells"] = {k: out[k]["holds"] for k in ("J1", "J2", "J3")}
    out["read-outs"] = {"the ten best at a = 0.10": ten,
                        "assignments passing at a = 0.10": sum(1 for v in refined.values() if v[0] <= PASS),
                        "a = 0.05 and 0.20": other, "the best chi2_min by weight (a = 0.10)": by_weight,
                        "pairs": PNAME, "assignments": len(PAIRS) ** 3, "grid points": len(pts)}
    OUT.write_text(json.dumps(out, indent=1, default=lambda x: float(x) if isinstance(x, (np.floating, mp.mpf))
                              else [x.real, x.imag] if isinstance(x, complex) else str(x)) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
