#!/usr/bin/env python3
"""Read-outs, not cells (committed before the census output was read; they test nothing): on the sealed census's rows
under the sealed rule (S~ for every sector, Clebsch 3 on the leptons), the ten best rows (six and nine) with their J,
the Im tau profile of the best (its line, Re tau and horocycle), and which line orders the best rows come from.  Model
values from two_ingredients_census.jsonl; the targets as in two_ingredients_compare.py (the record's pinned files at
main's 3412bf09d).
    python3 -B two_ingredients_after.py      # writes two_ingredients_after.json and _run.txt"""
import hashlib, json, math, subprocess, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
REV = "3412bf09d"


def git(path):
    return subprocess.run(["git", "show", f"{REV}:{path}"], cwd=ROOT, capture_output=True, check=True).stdout


bd = git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
bc = git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
assert hashlib.sha256(bd).hexdigest() == "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
assert hashlib.sha256(bc).hexdigest() == "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
v = json.loads(bd)["masses_GeV"]["value"]; C = json.loads(bc)["ckm_abs"]["value"]
T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
T9 = np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])


def _lines(lo, hi):                                   # B1713's list, as in two_ingredients_census.py
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
                seen.add(key); out.append(("N=%d" % N, key[0], key[1]))
    return out


LINES = _lines(1, 7) + _lines(8, 12)
rows = [json.loads(l) for l in (HERE / "two_ingredients_census.jsonl").read_text().splitlines() if l.strip()]
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)


recs = []
for r in rows:
    for hor in ("L_max", "L_2"):
        vals = r[f"up|{hor}|St"] + r[f"down|{hor}|St"] + r[f"lep|{hor}|St"] + r[f"ckm|{hor}|St|St"][:3]
        a = np.log(np.maximum(np.array(vals, dtype=float), 1e-300)); a[4] += math.log(3); a[5] -= math.log(3)
        recs.append({"line": r["line"], "Re": r["Re_tau"], "Im": r["Im_tau"], "hor": hor,
                     "w6": float(np.exp(np.max(np.abs(a[:6] - T6)))), "w9": float(np.exp(np.max(np.abs(a - T9)))),
                     "J": r[f"ckm|{hor}|St|St"][3], "mm9": np.exp(a - T9).tolist()})
OUT = {}
for key in ("w6", "w9"):
    best = sorted(recs, key=lambda x: x[key])[:10]
    OUT[f"ten_best_{key}"] = [{k: val for k, val in b.items()} | {"line_value": [LINES[b["line"]][0], str(LINES[b["line"]][1]), str(LINES[b["line"]][2])]} for b in best]
    say(f"ten best by {key}:")
    for b in best:
        tag, a_, b_ = LINES[b["line"]]
        say(f"  {b[key]:.3f}  {tag} ({a_}, {b_})  tau ({b['Re']}, {b['Im']})  {b['hor']}  J {b['J']:.2e}")
    b0 = best[0]
    prof = sorted([x for x in recs if x["line"] == b0["line"] and x["Re"] == b0["Re"] and x["hor"] == b0["hor"]], key=lambda x: x["Im"])
    OUT[f"profile_{key}"] = [[x["Im"], x[key]] for x in prof]
    say(f"  Im tau profile of the best ({key}):", " ".join(f"{x['Im']:.1f}:{x[key]:.2f}" for x in prof))
    say(f"  model/measured at the best ({key}):", [round(val, 3) for val in b0["mm9"]])
orders = {}
for x in sorted(recs, key=lambda x: x["w6"])[:100]:
    orders[LINES[x["line"]][0]] = orders.get(LINES[x["line"]][0], 0) + 1
OUT["orders_of_the_100_best_six"] = orders
say("line orders among the 100 best six-rows:", orders)
(HERE / "two_ingredients_after.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "two_ingredients_after_run.txt").write_text("\n".join(LOG) + "\n")
