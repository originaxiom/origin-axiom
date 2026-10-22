#!/usr/bin/env python3
"""POST HOC, labelled (written after route_b_split_control was read; committed before its own run): route (b) in the
two readings not yet scanned, to see whether the Georgi-Jarlskog behaviour and the mixing can live in one reading.
  So far: in the split reading (up S~; down and leptons S, the Standard Model's H~/H assignment if B1656's 2x2 index
  is SU(2)_L) the -3 acts as Georgi-Jarlskog (best six 1.74 with R2 2.28, R1 3.26; the Clebsch-1 control 1.83 with
  R2 1.00) but the mixing fails (nine 22.9); with S~ for every sector the mixing works (nine 2.47) but the -3 does not
  act (R2 1.04 at the best six).
  Here: (i) S for every sector; (ii) the flipped split (up S; down and leptons S~).  Each with the Clebsch -3 and the
  Clebsch-1 control, on route (b)'s grid; summaries as before (best six with D, R2, R1 there; best nine; D-matched and
  Georgi-Jarlskog-ratio rows; calibration with main's generator).  As a reference, the sealed census's rows in the
  same readings, with the by-hand Clebsch 3 and without.
    python3 -B route_b_readings.py      # writes route_b_readings.json and route_b_readings_run.txt"""
import contextlib, hashlib, importlib.util, io, json, math, random, subprocess, pathlib
import numpy as np
from scipy.spatial import cKDTree

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
SEL = HERE.parent / "chat1_2026-10-22_selection_map"
_spec = importlib.util.spec_from_file_location("rbs", HERE / "route_b_scan.py")
rbs = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(rbs)
B, tic = rbs.B, rbs.tic


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
READINGS = {"S for every sector": ("S", "S", "S"), "flipped split (up S; down, leptons S~)": ("S", "St", "St")}
LOG, OUT = [], {"route_b": {}, "census": {}}


def say(s):
    LOG.append(s); print(s, flush=True)


def rd(S, r):
    return rbs.St(S) if r == "St" else S


def outs(M, which, Sq, Sl, reading):
    ru, rdn, rl = reading
    Yu = B.coupling(rd(Sq, ru), M[("up", which)]); Yd = B.coupling(rd(Sq, rdn), M[("down", which)]); Yl = B.coupling(rd(Sl, rl), M[("lep", which)])
    o = []
    for Y in (Yu, Yd, Yl):
        s = np.linalg.svd(Y, compute_uv=False); o += [s[1] / s[0], s[2] / s[0]]
    return o + tic.ckm_left(Yu, Yd)


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
        a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
        if c < b < a:
            return [a, b, c]


d6 = np.log(np.array([r_masses() for _ in range(4000)]))
d9 = np.log(np.array([r_masses() + r_ckm() for _ in range(4000)]))


def summarise(L, label, where, store):
    six = np.max(np.abs(L[..., :6] - T6), axis=-1); nine = np.max(np.abs(L - T9), axis=-1)
    R2 = np.exp(L[..., 4] - L[..., 2]); R1 = np.exp(L[..., 3] - L[..., 5]); D = R2 * R1
    res = {}
    for key, arr, mask in (("best six", six, None), ("best nine", nine, None), ("D-matched best six", six, np.abs(D - P094) <= 3 * SIG),
                           ("GJ-ratio best six", six, (R2 >= 2) & (R2 <= 4.5) & (R1 >= 2) & (R1 <= 4.5))):
        a_ = np.where(mask, arr, np.inf) if mask is not None else arr
        i = np.unravel_index(np.argmin(a_), a_.shape)
        n = int(mask.sum()) if mask is not None else int(arr.size)
        res[key] = None if not np.isfinite(a_[i]) else {"value": math.exp(a_[i]), "rows": n, "where": where(i), "D": float(D[i]),
                                                        "R2": float(R2[i]), "R1": float(R1[i]), "nine": math.exp(nine[i]), "six": math.exp(six[i])}
    rows = L.reshape(-1, 9)
    q6, _ = cKDTree(rows[:, :6]).query(d6, k=1, p=np.inf); q9, _ = cKDTree(rows).query(d9, k=1, p=np.inf)
    res["six_random_as_good"] = float(np.mean(q6 <= np.min(six) + 1e-12)); res["nine_random_as_good"] = float(np.mean(q9 <= np.min(nine) + 1e-12))
    b6, b9, dm, gj = res["best six"], res["best nine"], res["D-matched best six"], res["GJ-ratio best six"]
    say(f"{label}: best six {b6['value']:.3f} (R2 {b6['R2']:.2f}, R1 {b6['R1']:.2f}, D {b6['D']:.2f}; nine there {b6['nine']:.2f}) at {b6['where']}; "
        f"best nine {b9['value']:.3f} (D {b9['D']:.2f}); D-matched " + (f"{dm['rows']} rows, best six {dm['value']:.3f} (nine {dm['nine']:.2f})" if dm else "none")
        + "; GJ-ratio " + (f"{gj['rows']} rows, best six {gj['value']:.3f} (nine {gj['nine']:.2f})" if gj else "none")
        + f"; random as good six {res['six_random_as_good']:.4f}, nine {res['nine_random_as_good']:.4f}")
    store[label] = res


# the sealed census's rows in the same readings
def _lines(lo, hi):
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
crow = [json.loads(l) for l in (SEL / "two_ingredients_census.jsonl").read_text().splitlines() if l.strip()]
for rname, (ru, rdn, rl) in READINGS.items():
    for c in (3, 1):
        Lc, lab = [], []
        for r in crow:
            for hor in ("L_max", "L_2"):
                vals = r[f"up|{hor}|{ru}"] + r[f"down|{hor}|{rdn}"] + r[f"lep|{hor}|{rl}"] + r[f"ckm|{hor}|{ru}|{rdn}"][:3]
                x = np.log(np.maximum(np.array(vals, dtype=float), 1e-300)); x[4] += math.log(c); x[5] -= math.log(c)
                Lc.append(x); lab.append((r["Re_tau"], r["Im_tau"], LINES[r["line"]], hor))
        summarise(np.array(Lc), f"census, {rname}, Clebsch {c} by hand", lambda i, lab=lab: lab[i[0]], OUT["census"])

# route (b) in the same readings
data = {(rn, c): np.zeros((len(rbs.BASE), len(rbs.CANDS), len(rbs.RHO), len(rbs.PHI), len(rbs.HORS), 10)) for rn in READINGS for c in (-3, 1)}
for ib, (re_t, im_t, a, b) in enumerate(rbs.BASE):
    M = rbs.channels(re_t, im_t, a, b)
    v1, v2, v3 = rbs.at(rbs.H1, re_t, im_t), rbs.at(rbs.H2, re_t, im_t), rbs.at(rbs.H3, re_t, im_t)
    n1 = np.linalg.norm(v1)
    u2, u3 = v2 / np.linalg.norm(v2), v3 / np.linalg.norm(v3)
    dirs = {"h2": u2, "h3": u3}
    for ang in (0, 90, 180, 270):
        dirs[f"c{ang}"] = (u2 + np.exp(1j * math.radians(ang)) * u3) / math.sqrt(2)
    S1 = rbs.S_of(v1)
    for ic, cn in enumerate(rbs.CANDS):
        Ss = rbs.S_of(dirs[cn])
        for ir, rho in enumerate(rbs.RHO):
            for ip, phi in enumerate(rbs.PHI):
                kap = rho * np.exp(1j * phi) * n1
                for c in (-3, 1):
                    Sq, Sl = S1 + kap * Ss, S1 + c * kap * Ss
                    for ih, which in enumerate(rbs.HORS):
                        for rn, reading in READINGS.items():
                            data[(rn, c)][ib, ic, ir, ip, ih] = outs(M, which, Sq, Sl, reading)


def where_b(i):
    b, c, r, p, h = i
    return {"base": rbs.BASE[b], "cand": rbs.CANDS[c], "rho": rbs.RHO[r], "phi_deg": 15 * int(p), "hor": rbs.HORS[h]}


for (rn, c), X in data.items():
    summarise(np.log(np.maximum(X[..., :9], 1e-300)), f"route (b), {rn}, second direction Clebsch {c}", where_b, OUT["route_b"])
(HERE / "route_b_readings.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "route_b_readings_run.txt").write_text("\n".join(LOG) + "\n")
