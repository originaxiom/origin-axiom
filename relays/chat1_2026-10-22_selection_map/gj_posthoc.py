#!/usr/bin/env python3
"""POST HOC, labelled (every number here was computed after the Georgi-Jarlskog wall's cells were read, and the
Clebsch 3 was chosen knowing the data's R2 = 3.14).  Reads main's committed census outputs (B1712, B1713, B1720 at
main's 3412bf09d) and reports:
  1. where the frame fits the down and lepton hierarchies (each of the four ratios within a factor F of the data),
     the range of R2 = (m_mu/m_tau)/(m_s/m_b) it gives (data 3.14);
  2. the six-ratio worst factor when a Clebsch c is put on the leptons' middle generation, det kept
     (m_mu/m_tau x c, m_e/m_tau / c), for c in a set; the best rows at c = 3;
  3. main's own calibration (B1720 compare.py's prior and seed 1720, 4000 draws) for c = 3 fixed, and with the
     Clebsch look-elsewhere (each random target also takes its best c in the set);
  4. the nine (six ratios and |V_us|, |V_cb|, |V_ub|) with c = 1 and c = 3.
The model values are main's, unchanged; nothing in the frame is recomputed.
    python3 -B gj_posthoc.py      # writes gj_posthoc.json and gj_posthoc_run.txt"""
import json, math, random, subprocess, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
REV = "3412bf09d"
SRC = {"B1712": "frontier/B1712_the_weave_census_of_lines/verification/the_line_census_masses.json",
       "B1713": "frontier/B1713_the_complement_and_the_mixing/verification/the_complement_and_mixing.json",
       "B1720": "frontier/B1720_the_thread_fixes_the_point/verification/the_thread_census.json"}
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)


def load(name):
    return json.loads(subprocess.run(["git", "show", f"{REV}:{SRC[name]}"], cwd=ROOT, capture_output=True,
                                     check=True).stdout)


v = {"u": 0.00123, "c": 0.620, "t": 168.26, "d": 0.00267, "s": 0.05316, "b": 2.839,
     "e": 0.00048307, "mu": 0.101766, "tau": 1.72856}                           # HZ2021 at M_Z, the record's file
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"],
                      v["mu"] / v["tau"], v["e"] / v["tau"]]))
T3 = np.log(np.array([0.22500, 0.04182, 0.00369]))                              # PDG 2025 |V_us|, |V_cb|, |V_ub|
CSET = [1 / 3, 1 / 2, 2 / 3, 1, 3 / 2, 2, 3, 4, 5]


def rows(G, with_ckm=False):
    lab, A = [], []
    for p in G["rows"]:
        for hor in ("L_max", "L_2"):
            for rd in ("S", "St", "conjS"):
                ku = "up|%s|%s" % (hor, rd)
                if ku not in p:
                    continue
                vals = p[ku] + p["down|%s|S" % hor] + p["lep|%s|S" % hor]
                if with_ckm:
                    ck = p.get("ckm|%s|%s" % (hor, rd))
                    if ck is None:
                        continue
                    vals = vals + ck[:3]
                A.append([math.log(max(z, 1e-300)) for z in vals])
                lab.append({k: p[k] for k in p if not isinstance(p[k], list)} | {"horocycle": hor, "up_reading": rd})
    return lab, np.array(A)


def clebsch(A, c):
    B = A.copy(); B[:, 4] += math.log(c); B[:, 5] -= math.log(c); return B


def best(M, t):
    w = np.exp(np.max(np.abs(M - t), axis=1)); i = int(np.argmin(w)); return float(w[i]), i


def r_masses(rng):
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2:
                break
        tg += [r2, r1]
    return tg


OUT = {"note": "POST HOC, labelled; the Clebsch 3 was chosen knowing the data", "rev": REV, "by_census": {}}
for name in ("B1712", "B1713", "B1720"):
    G = load(name)
    lab, A = rows(G)
    res = {"rows": int(len(A))}
    # 1. the good-hierarchy region (reading S rows only, to count each (point, horocycle) once)
    sel = np.array([l["up_reading"] == "S" for l in lab])
    f4 = np.max(np.abs(A[:, 2:6] - T6[2:6]), axis=1)
    reg = {}
    for F in (3.0, 2.5, 2.0):
        m = sel & (f4 < math.log(F))
        R2 = np.exp(A[m, 4] - A[m, 2])
        reg[str(F)] = {"n": int(m.sum()), "R2_min": float(R2.min()) if m.any() else None,
                       "R2_max": float(R2.max()) if m.any() else None}
    res["good_region_R2"] = reg
    # 2. the Clebsch scan
    scan = {}
    for c in CSET:
        w, i = best(clebsch(A, c), T6)
        scan[f"{c:.4g}"] = {"best": w, "row": lab[i], "model_over_measured": np.exp(clebsch(A, c)[i] - T6).tolist()}
    res["clebsch_scan"] = scan
    say(f"{name}: rows {len(A)}; best six-ratio factor by Clebsch c:",
        ", ".join(f"{k}: {x['best']:.3f}" for k, x in scan.items()))
    say(f"   good region (four down/lepton ratios within 2.0): n = {reg['2.0']['n']}, R2 from "
        f"{reg['2.0']['R2_min']} to {reg['2.0']['R2_max']}")
    B3 = clebsch(A, 3); w3 = np.exp(np.max(np.abs(B3 - T6), axis=1)); top = np.argsort(w3)[:10]
    res["best_rows_c3"] = [{"factor": float(w3[i]), "row": lab[i]} for i in top]
    # 3. calibration, main's prior and seed
    if name in ("B1713", "B1720"):
        W = {c: best(clebsch(A, c), T6)[0] for c in CSET}
        wb = min(W.values())
        rng = random.Random(1720); h1 = h3 = hall = 0; N = 4000
        mats = {c: clebsch(A, c) for c in CSET}
        for _ in range(N):
            tg = np.log(np.array(r_masses(rng)))
            b = {c: best(mats[c], tg)[0] for c in CSET}
            h1 += b[1] <= W[1] + 1e-12; h3 += b[3] <= W[3] + 1e-12; hall += min(b.values()) <= wb + 1e-12
        res["calibration"] = {"N": N, "c1_as_computed": h1 / N, "c3_fixed": h3 / N, "best_of_set": hall / N,
                              "data_best_of_set": wb}
        say(f"   calibration (main's prior, seed 1720): c = 1 {h1/N:.4f}; c = 3 fixed {h3/N:.4f}; "
            f"best of the set for every target {hall/N:.4f}")
    # 4. the nine
    lab9, A9 = rows(G, with_ckm=True)
    if len(A9):
        t9 = np.concatenate([T6, T3]); nine = {}
        for c in (1, 3):
            w, i = best(clebsch(A9, c), t9)
            nine[str(c)] = {"best": w, "row": lab9[i], "model_over_measured": np.exp(clebsch(A9, c)[i] - t9).tolist()}
        res["nine"] = nine
        say(f"   nine (with CKM moduli): c = 1 {nine['1']['best']:.3f}; c = 3 {nine['3']['best']:.3f}")
    OUT["by_census"][name] = res

(HERE / "gj_posthoc.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "gj_posthoc_run.txt").write_text("\n".join(LOG) + "\n")
