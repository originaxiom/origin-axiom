#!/usr/bin/env python3
"""SM-C24's decisive run in the new card form (fam1-v1-unset-04): relays/sm_c24/run_c24.py run unchanged in a copy of its
folder, with the repo root as main's checkout, then its disclosed split relays/sm_c24/posthoc_split_by_a.py on that
run's own rows; the decisive facts printed as DECISIVE: lines.
    python3 relays/claims/sm_refile/c24_decisive.py
Exit 0 when the run completes and every decisive fact comes out as the card states; 1 otherwise."""
import json, pathlib, shutil, subprocess, sys, tempfile
from collections import Counter
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
tmp = pathlib.Path(tempfile.mkdtemp()) / "sm_c24"
shutil.copytree(ROOT / "relays" / "sm_c24", tmp)
(tmp / "c24_results.json").unlink()
r = subprocess.run([sys.executable, "-B", "run_c24.py", str(ROOT)], cwd=tmp, capture_output=True, text=True)
if r.returncode != 0 or not (tmp / "c24_results.json").is_file():
    print("RUN FAILED"); sys.exit(1)
d = json.loads((tmp / "c24_results.json").read_text())["rows"]
K = ("up_m2m3", "up_m1m3", "down_m2m3", "down_m1m3", "lep_m2m3", "lep_m1m3", "V12", "V23", "V13")
key = lambda x: tuple(None if x[k] is None else round(x[k] * 60) for k in K)
res = lambda x: max(abs(x[k] * 60 - round(x[k] * 60)) / 60 for k in K if x[k] is not None)
hier = lambda x: x["up_m2m3"] >= 0.1 and x["down_m2m3"] >= 0.1 and x["up_m1m3"] >= 0.2 and x["down_m1m3"] >= 0.2
five = [x for x in d if Fr(x["a"]).denominator % 5 == 0]
rest = [x for x in d if Fr(x["a"]).denominator % 5 != 0]
ah = sum(x["r4050"]["diag"] >= 0.9 and hier(x["r4050"]) for x in five)
cl5 = Counter(key(x["r4050"]) for x in five); line = Counter(key(x["r4050"]) for x in d if x["on_line"])
ratios = sorted({cl5[k] / line[k] for k in line})
print("DECISIVE: pairs +-v of exact order 30: %d; with a 5-part in a: %d" % (len(d), len(five)))
print("DECISIVE: with a 5-part: aligned and hierarchical in both quark sectors: %d of %d" % (ah, len(five)))
print("DECISIVE: with a 5-part: every 40-50 rate within 1e-3 of the 1/60 grid: %s" % (max(map(lambda x: res(x["r4050"]), five)) < 1e-3))
print("DECISIVE: with a 5-part: class kept from 30-40 to 40-50: %d of %d" % (sum(key(x["r3040"]) == key(x["r4050"]) for x in five), len(five)))
print("DECISIVE: classes with a 5-part: %d; the same as the act's line's: %s; size ratio to the line: %s"
      % (len(cl5), set(cl5) == set(line), ratios))
print("DECISIVE: without a 5-part (not claimed): %d pairs, class kept %d" % (len(rest), sum(key(x["r3040"]) == key(x["r4050"]) for x in rest)))
ok = len(d) == 288 and len(five) == 240 and ah == 240 and len(cl5) == 12 and set(cl5) == set(line) and ratios == [5.0]
sys.exit(0 if ok else 1)
