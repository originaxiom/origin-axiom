#!/usr/bin/env python3
"""EXPLORATORY read-out, labelled (committed before route_b_scan.npz was read): what a Georgi-Jarlskog-type Higgs from
the record's own weight-3/2 space does in main's frame, with no by-hand factor.
For every base point, second direction s and reading model, over the kappa grid and both horocycles:
  - the six-ratio and nine-target worst factors, and the double ratio D there;
  - the baseline at the smallest kappa (rho = 1e-4);
  - the best six among rows with D within 3 sigma of P-094 (10.58 +- 0.11);
  - the rows whose two Georgi-Jarlskog ratios R2, R1 both lie in [2, 4.5], and the best six among them;
and the overall bests.  The reference is the sealed census's by-hand result: six 1.51, nine 2.09 at its best rows.
Targets: Huang-Zhou 2021 at M_Z and PDG 2025's three moduli, from the record's pinned files at main's 3412bf09d.
    python3 -B route_b_readout.py      # writes route_b_readout.json and route_b_readout_run.txt"""
import hashlib, json, math, subprocess, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())


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
IDX = json.loads((HERE / "route_b_scan_index.json").read_text())
X = np.load(HERE / "route_b_scan.npz")["data"]            # base, cand, rho, phi, hor, model, field
L = np.log(np.maximum(X[..., :9], 1e-300))
six = np.exp(np.max(np.abs(L[..., :6] - T6), axis=-1))
nine = np.exp(np.max(np.abs(L - T9), axis=-1))
R2 = np.exp(L[..., 4] - L[..., 2]); R1 = np.exp(L[..., 3] - L[..., 5]); D = R2 * R1
LOG, OUT = [], {"by_base": []}


def say(s):
    LOG.append(s); print(s)


def where(i):
    b, c, r, p, h, m = i
    return {"base": IDX["base"][b], "cand": IDX["cands"][c], "rho": IDX["rho"][r], "phi_deg": IDX["phi_deg"][p],
            "hor": IDX["hors"][h], "model": IDX["models"][m]}


def best(mask=None, arr=six):
    a = np.where(mask, arr, np.inf) if mask is not None else arr
    i = np.unravel_index(np.argmin(a), a.shape)
    return float(a[i]), tuple(int(k) for k in i)


say(f"grid: {X.shape[0]} base points x {X.shape[1]} directions x {X.shape[2]} rho x {X.shape[3]} phi x 2 horocycles x 2 readings")
for mi, model in enumerate(IDX["models"]):
    sub = np.zeros_like(six, dtype=bool); sub[..., mi] = True
    w6, i6 = best(sub); w9, i9 = best(sub, nine)
    dm = sub & (np.abs(D - P094) <= 3 * SIG); gj = sub & (R2 >= 2) & (R2 <= 4.5) & (R1 >= 2) & (R1 <= 4.5)
    say(f"== reading {model}")
    say(f"   overall best six {w6:.3f} at {where(i6)}; D there {D[i6]:.2f}, R2 {R2[i6]:.2f}, R1 {R1[i6]:.2f}")
    say(f"   overall best nine {w9:.3f} at {where(i9)}; D there {D[i9]:.2f}, J {X[i9][9]:.1e}")
    if dm.any():
        wd, idd = best(dm)
        say(f"   D within 3 sigma of P-094 on {int(dm.sum())} rows; best six there {wd:.3f} at {where(idd)} (nine {nine[idd]:.2f})")
    else:
        say("   no row with D within 3 sigma of P-094")
    if gj.any():
        wg, ig = best(gj)
        say(f"   R2 and R1 both in [2, 4.5] on {int(gj.sum())} rows; best six there {wg:.3f} at {where(ig)} (D {D[ig]:.2f})")
    else:
        say("   no row with R2 and R1 both in [2, 4.5]")
    OUT[model] = {"best_six": [w6, where(i6), float(D[i6])], "best_nine": [w9, where(i9), float(D[i9])],
                  "n_D_matched": int(dm.sum()), "best_six_D_matched": (lambda t: [t[0], where(t[1])])(best(dm)) if dm.any() else None,
                  "n_GJ_rows": int(gj.sum()), "best_six_GJ_rows": (lambda t: [t[0], where(t[1]), float(D[t[1]])])(best(gj)) if gj.any() else None}
say("== per base point (reading S~ for every sector): baseline six at rho = 1e-4, best six over kappa and directions (D), best D-matched six")
for b, base in enumerate(IDX["base"]):
    sub = np.zeros_like(six, dtype=bool); sub[b, ..., 0] = True
    b0 = float(np.min(six[b, :, 0, :, :, 0])); w6, i6 = best(sub)
    dm = sub & (np.abs(D - P094) <= 3 * SIG)
    wd = best(dm)[0] if dm.any() else None
    say(f"   {base}: baseline {b0:.2f}; best {w6:.2f} ({IDX['cands'][i6[1]]}, rho {IDX['rho'][i6[2]]:.1e}, D {D[i6]:.2f}); "
        f"D-matched best {('%.2f' % wd) if wd is not None else 'none'}")
    OUT["by_base"].append({"base": base, "baseline_six": b0, "best_six": w6, "best_where": where(i6), "D_at_best": float(D[i6]), "best_six_D_matched": wd})
(HERE / "route_b_readout.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "route_b_readout_run.txt").write_text("\n".join(LOG) + "\n")
