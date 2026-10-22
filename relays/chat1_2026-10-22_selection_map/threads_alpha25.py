#!/usr/bin/env python3
"""POST HOC read-out, labelled (after the THREADS comparison was read): which of B1720's thread classes have fixed lines
with alpha = 2/5 (the family where the two ingredients fit, section 6a), and the best six-ratio fit among those rows
under the sealed model (S~ for every sector, Clebsch 3).  Model values from threads_with_ingredients.jsonl.
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
print("\n".join(LOG))
(HERE / "threads_alpha25_run.txt").write_text("\n".join(LOG) + "\n")
