#!/usr/bin/env python3
"""EXPLORATORY, labelled (no cell, no seal): the SM seat's W129 test (i) in main's frame, a first look. The Higgs is
taken flavour-blind, S = 1 (the identity channel, which the moves fix), in place of the end-data Higgs DR's parity
components; every other piece is main's B1720 instrument at 3412bf09d, unchanged (through two_ingredients_census, whose
import extracts and hash-checks it). With S = 1 all three readings coincide (eps 1* eps^T = 1), so the up and down
sectors read the Higgs alike. Grid: chat1's allst lines (10 lines with alpha in {0, 1/5, 2/5}), Re tau in {0, 1/4, 1/2},
Im tau 2.30-3.50 (step 0.05), both horocycles. Read-outs against Huang-Zhou at M_Z and PDG's moduli: the best six
(no Clebsch, and with the Clebsch 3), the best nine, and the CKM moduli there.
    python3 -B flavour_blind_scan.py      # writes flavour_blind_scan.json and flavour_blind_scan_run.txt"""
import hashlib, importlib.util, json, math, subprocess, pathlib, sys
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SEL = HERE.parent / "chat1_2026-10-22_selection_map"
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
_spec = importlib.util.spec_from_file_location("tic", SEL / "two_ingredients_census.py")
tic = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(tic)
B, TC = tic.B, tic.TC


def evaluate_blind(re_t, im_t, a, b):
    t = complex(re_t, im_t); w = a * t + b
    S = np.eye(2, dtype=complex)
    res, Y = {}, {}
    for sec, (lf, rf) in TC.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for which in ("L_max", "L_2"):
            L = TC.L_of(t.imag, which)
            u = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
            Ym = B.coupling(S, B.weighted_M(u)); Y[(sec, which)] = Ym
            sv = np.linalg.svd(Ym, compute_uv=False)
            res[f"{sec}|{which}"] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    for which in ("L_max", "L_2"):
        res[f"ckm|{which}"] = tic.ckm_left(Y[("up", which)], Y[("down", which)])
    return res


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


if __name__ == "__main__":
    bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
    bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
    assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
    assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
    v = json.loads(bd)["masses_GeV"]["value"]; C = json.loads(bc)["ckm_abs"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])
    lines = [(2/5, 1/5), (2/5, 2/5), (2/5, 3/5), (2/5, 4/5), (2/5, 1/2), (2/5, 1/10), (1/5, 2/5), (1/5, 3/5), (0, 1/5), (0, 2/5)]
    tasks = [(r, round(2.30 + 0.05 * j, 2), a, b) for (a, b) in lines for r in (0.0, 0.25, 0.5) for j in range(25)]
    rows = []
    for k, (r, y, a, b) in enumerate(tasks):
        res = evaluate_blind(r, y, a, b); res.update({"tau": [r, y], "line": [a, b]}); rows.append(res)
    recs = []
    for res in rows:
        for hor in ("L_max", "L_2"):
            x = np.log(np.maximum(np.array(res[f"up|{hor}"] + res[f"down|{hor}"] + res[f"lep|{hor}"] + res[f"ckm|{hor}"][:3]), 1e-300))
            xc = x.copy(); xc[4] += math.log(3); xc[5] -= math.log(3)
            recs.append({"tau": res["tau"], "line": res["line"], "hor": hor,
                         "six": float(np.exp(np.max(np.abs(x[:6] - T6)))), "six_clebsch": float(np.exp(np.max(np.abs(xc[:6] - T6)))),
                         "nine_clebsch": float(np.exp(np.max(np.abs(xc - T9)))), "ckm": res[f"ckm|{hor}"],
                         "model_over_measured_clebsch": np.exp(xc - T9).tolist()})
    LOG = [f"flavour-blind Higgs S = 1 in main's frame: {len(tasks)} points, {len(recs)} rows (exploratory, labelled)"]
    for key in ("six", "six_clebsch", "nine_clebsch"):
        b0 = min(recs, key=lambda q: q[key])
        LOG.append(f"best {key}: {b0[key]:.3f} at tau {b0['tau']}, line {[round(z, 3) for z in b0['line']]}, {b0['hor']}; "
                   f"|V_us|, |V_cb|, |V_ub| = {[round(z, 4) for z in b0['ckm'][:3]]}; J = {b0['ckm'][3]:.2e}; "
                   f"model/measured (Clebsch) {[round(z, 2) for z in b0['model_over_measured_clebsch']]}")
    vus = [q["ckm"][0] for q in recs]
    LOG.append(f"|V_us| over all rows: median {np.median(vus):.3f}, range {min(vus):.3f}-{max(vus):.3f}")
    print("\n".join(LOG))
    (HERE / "flavour_blind_scan.json").write_text(json.dumps({"note": "EXPLORATORY; model values and read-outs", "rows": recs}) + "\n")
    (HERE / "flavour_blind_scan_run.txt").write_text("\n".join(LOG) + "\n")
