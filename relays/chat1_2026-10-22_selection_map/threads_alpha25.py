#!/usr/bin/env python3
"""POST HOC read-out, labelled (after the THREADS comparison was read): which of B1720's thread classes have fixed lines
with alpha = 2/5 (the family where the two ingredients fit, section 6a), and the best six-ratio fit among those rows
under the sealed model (S~ for every sector, Clebsch 3).  Model values from threads_with_ingredients.jsonl.
Second part (added after the referee's third pass): the thread rows on order-10 alpha = 2/5 lines with apex Im tau in
2.55-2.85, moved to 0 <= Re tau < 1 (tau -> tau - n, b -> b + n a), and the sealed model's six at comparable points of
posthoc_scans.json (Re tau 1/2 and 0), to show that the fit is sharp in Re tau and in the line's offset.
    python3 -B threads_alpha25.py      # writes threads_alpha25_run.txt"""
import hashlib, json, math, subprocess, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())


def git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


G = json.loads(git("frontier/B1720_the_thread_fixes_the_point/verification/the_thread_census.json"))
bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
v = json.loads(bd)["masses_GeV"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
A25 = (Fr(2, 5), Fr(3, 5))
cls = [c for c in G["classes"] if any(Fr(a) in A25 for a, _b in c["lines"])]
rows = [json.loads(l) for l in (HERE / "threads_with_ingredients.jsonl").read_text().splitlines() if l.strip()]
best = []
for r in rows:
    c = G["classes"][r["class"]]; a, b = c["lines"][r["line"]]
    if Fr(a) not in A25:
        continue
    for hor in ("L_max", "L_2"):
        x = np.log(np.maximum(np.array(r[f"up|{hor}|St"] + r[f"down|{hor}|St"] + r[f"lep|{hor}|St"], dtype=float), 1e-300))
        x[4] += math.log(3); x[5] -= math.log(3)
        best.append((float(np.exp(np.max(np.abs(x - T6)))), c["word"], c["tau"], [a, b], hor))
best.sort()
LOG = [f"thread classes with an alpha = 2/5 fixed line: {len(cls)} of {len(G['classes'])}",
       f"apex Im tau among them: {min(c['tau'][1] for c in cls):.3f} to {max(c['tau'][1] for c in cls):.3f}",
       "best six under the sealed model among their alpha = 2/5 rows:"]
LOG += [f"  {w:.3f}  {word}  tau ({t[0]:.3f}, {t[1]:.3f})  line ({l[0]}, {l[1]})  {h}" for w, word, t, l, h in best[:6]]
LOG.append("thread rows on order-10 alpha = 2/5 lines with apex Im tau 2.55-2.85 (sealed model, six):")
for r in rows:
    c = G["classes"][r["class"]]; a, b = c["lines"][r["line"]]; A, Bb = Fr(a), Fr(b)
    if A in A25 and math.lcm(A.denominator, Bb.denominator) == 10 and 2.55 <= c["tau"][1] <= 2.85:
        n = math.floor(c["tau"][0] + 1e-9); re0 = c["tau"][0] - n; bb = (Bb + n * A) % 1
        ws = []
        for hor in ("L_max", "L_2"):
            x = np.log(np.maximum(np.array(r[f"up|{hor}|St"] + r[f"down|{hor}|St"] + r[f"lep|{hor}|St"], dtype=float), 1e-300))
            x[4] += math.log(3); x[5] -= math.log(3); ws.append(float(np.exp(np.max(np.abs(x - T6)))))
        LOG.append(f"  {c['word']}  apex ({c['tau'][0]:.3f}, {c['tau'][1]:.3f})  line ({a}, {b})  = ({A}, {bb}) at Re tau {re0:.2f}:"
                   f"  L_max {ws[0]:.2f}, L_2 {ws[1]:.2f}")
P = json.loads((HERE / "posthoc_scans.json").read_text())
LOG.append("posthoc_scans (allst), sealed model, six:")
for re_t, im_t, ln in ((0.5, 2.65, (0.4, 0.1)), (0.5, 2.65, (0.4, 0.5)), (0.0, 2.65, (0.4, 0.5)), (0.0, 2.7, (0.4, 0.5))):
    for r in P["allst_scan"]:
        if abs(r["tau"][0] - re_t) < 1e-9 and abs(r["tau"][1] - im_t) < 1e-9 and abs(r["line"][0] - ln[0]) < 1e-9 and abs(r["line"][1] - ln[1]) < 1e-9:
            ws = []
            for hor in ("L_max", "L_2"):
                x = np.log(np.maximum(np.array(r[f"up|{hor}|St"] + r[f"down|{hor}|St"] + r[f"lep|{hor}|St"], dtype=float), 1e-300))
                x[4] += math.log(3); x[5] -= math.log(3); ws.append(float(np.exp(np.max(np.abs(x - T6)))))
            LOG.append(f"  tau ({re_t}, {im_t}) line {ln}: L_max {ws[0]:.2f}, L_2 {ws[1]:.2f}")
print("\n".join(LOG))
(HERE / "threads_alpha25_run.txt").write_text("\n".join(LOG) + "\n")
