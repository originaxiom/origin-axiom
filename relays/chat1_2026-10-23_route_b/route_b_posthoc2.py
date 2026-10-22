#!/usr/bin/env python3
"""POST HOC, labelled (written after route_b_posthoc was read; committed before its own run): two references for
route (b)'s D-matched rows.
  1. The sealed census's rows (two_ingredients_census.jsonl, reading S~ for every sector), with the by-hand Clebsch 3
     and without it: the best six and nine among rows whose D is within 3 sigma of P-094 (10.58 +- 0.11).  The census's
     tau grid is coarse, so few of its rows can land in a 3% band; the number of such rows is printed.
  2. Route (b) (Clebsch -3, reading S~) with kappa continuous and D held within 3 sigma of P-094: from the five best
     distinct (base point, direction, horocycle) triples among the scan's D-matched rows, Nelder-Mead in log10 rho and
     phi on the six plus a penalty 10 |ln(D / 10.58)| outside the band; the result is reported only if it ends in band.
    python3 -B route_b_posthoc2.py      # writes route_b_posthoc2.json and route_b_posthoc2_run.txt"""
import contextlib, hashlib, importlib.util, io, json, math, subprocess, pathlib
import numpy as np
from scipy.optimize import minimize

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
SEL = HERE.parent / "chat1_2026-10-22_selection_map"


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
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


# 1. the census's rows, by-hand Clebsch 3 and none
def _lines(lo, hi):                                   # two_ingredients_census.py's list (B1713's logic), for the labels
    from fractions import Fraction as Fr
    seen, out = set(), []
    for N in range(lo, hi + 1):
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1:
                    continue
                a, b = Fr(j, N), Fr(k, N); na, nb = (-a) % 1, (-b) % 1
                key = min((a, b), (na, nb))
                if key in seen:
                    continue
                seen.add(key); out.append(f"({key[0]}, {key[1]})")
    return out


LINES = _lines(1, 7) + _lines(8, 12)
rows = [json.loads(l) for l in (SEL / "two_ingredients_census.jsonl").read_text().splitlines() if l.strip()]
for c in (3, 1):
    M, lab = [], []
    for r in rows:
        for hor in ("L_max", "L_2"):
            vals = r[f"up|{hor}|St"] + r[f"down|{hor}|St"] + r[f"lep|{hor}|St"] + r[f"ckm|{hor}|St|St"][:3]
            x = np.log(np.maximum(np.array(vals, dtype=float), 1e-300)); x[4] += math.log(c); x[5] -= math.log(c)
            M.append(x); lab.append((r["Re_tau"], r["Im_tau"], LINES[r["line"]], hor))
    M = np.array(M); D = np.exp((M[:, 4] - M[:, 2]) + (M[:, 3] - M[:, 5]))
    w6 = np.exp(np.max(np.abs(M[:, :6] - T6), axis=1)); w9 = np.exp(np.max(np.abs(M - T9), axis=1))
    dm = np.abs(D - P094) <= 3 * SIG
    if dm.any():
        i6 = np.where(dm)[0][np.argmin(w6[dm])]; i9 = np.where(dm)[0][np.argmin(w9[dm])]
        say(f"1. census, S~, Clebsch {c}: {len(M)} rows, {int(dm.sum())} with D within 3 sigma; best six there {w6[i6]:.3f} at {lab[i6]}; "
            f"best nine there {w9[i9]:.3f} at {lab[i9]}")
        OUT[f"census Clebsch {c}"] = {"rows": len(M), "n_D_matched": int(dm.sum()), "best_six": float(w6[i6]), "six_at": lab[i6],
                                      "best_nine": float(w9[i9]), "nine_at": lab[i9]}
    else:
        say(f"1. census, S~, Clebsch {c}: {len(M)} rows, none with D within 3 sigma")
        OUT[f"census Clebsch {c}"] = {"rows": len(M), "n_D_matched": 0}

# 2. route (b) with kappa continuous and D held in band
_spec = importlib.util.spec_from_file_location("rbs", HERE / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)
IDX = json.loads((HERE / "route_b_scan_index.json").read_text())
X = np.load(HERE / "route_b_scan.npz")["data"][..., 0, :]
Lx = np.log(np.maximum(X[..., :9], 1e-300))
six = np.max(np.abs(Lx[..., :6] - T6), axis=-1); Dg = np.exp((Lx[..., 4] - Lx[..., 2]) + (Lx[..., 3] - Lx[..., 5]))
a = np.where(np.abs(Dg - P094) <= 3 * SIG, six, np.inf)
seen = []
for f in np.argsort(a, axis=None):
    i = np.unravel_index(f, a.shape)
    if not np.isfinite(a[i]):
        break
    if (i[0], i[1], i[4]) not in [(s[0], s[1], s[4]) for s in seen]:
        seen.append(i)
    if len(seen) == 5:
        break
OUT["constrained_refinement"] = []
for i in seen:
    re_t, im_t, a_, b_ = IDX["base"][i[0]]
    M = rbs.channels(re_t, im_t, a_, b_)
    v1, v2, v3 = rbs.at(rbs.H1, re_t, im_t), rbs.at(rbs.H2, re_t, im_t), rbs.at(rbs.H3, re_t, im_t)
    u2, u3 = v2 / np.linalg.norm(v2), v3 / np.linalg.norm(v3)
    dirs = {"h2": u2, "h3": u3}
    for ang in (0, 90, 180, 270):
        dirs[f"c{ang}"] = (u2 + np.exp(1j * math.radians(ang)) * u3) / math.sqrt(2)
    S1, n1, Ss, hor = rbs.S_of(v1), np.linalg.norm(v1), rbs.S_of(dirs[IDX["cands"][i[1]]]), IDX["hors"][i[4]]

    def ev(p):
        kap = 10 ** p[0] * np.exp(1j * p[1]) * n1
        o = np.array(rbs.outputs(M, hor, S1 + kap * Ss, S1 - 3 * kap * Ss, "St_all"))
        lo = np.log(np.maximum(o[:9], 1e-300))
        return float(np.max(np.abs(lo[:6] - T6))), float(np.max(np.abs(lo - T9))), math.exp((lo[4] - lo[2]) + (lo[3] - lo[5]))

    def obj(p):
        s6, _, Dv = ev(p)
        return s6 + (0.0 if abs(Dv - P094) <= 3 * SIG else 10 * abs(math.log(Dv / P094)))

    p0 = [math.log10(IDX["rho"][i[2]]), math.radians(IDX["phi_deg"][i[3]])]
    res = minimize(obj, p0, method="Nelder-Mead", options={"xatol": 1e-7, "fatol": 1e-10, "maxiter": 4000})
    s6, s9, Dv = ev(res.x)
    inband = abs(Dv - P094) <= 3 * SIG
    say(f"2. from base {IDX['base'][i[0]]}, {IDX['cands'][i[1]]}, {hor}: grid D-matched six {math.exp(a[i]):.3f} -> continuous "
        f"{math.exp(s6):.3f} (nine {math.exp(s9):.3f}, D {Dv:.2f}, in band {inband}) at rho {10 ** res.x[0]:.4g}, phi {math.degrees(res.x[1]) % 360:.1f}")
    OUT["constrained_refinement"].append({"base": IDX["base"][i[0]], "cand": IDX["cands"][i[1]], "hor": hor, "grid": math.exp(a[i]),
                                          "continuous_six": math.exp(s6), "nine": math.exp(s9), "D": Dv, "in_band": inband,
                                          "rho": 10 ** res.x[0], "phi_deg": math.degrees(res.x[1]) % 360})
(HERE / "route_b_posthoc2.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "route_b_posthoc2_run.txt").write_text("\n".join(LOG) + "\n")
