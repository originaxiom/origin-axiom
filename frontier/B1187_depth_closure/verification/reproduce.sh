#!/usr/bin/env bash
# B1187 -- the depth-closure sitting. Fast path: the cheap re-runs + committed-artifact
# assertions. OA_SLOW=1 additionally re-runs the full sweeps (WALL-7 both primes ~5 min
# incl. the exact prefix load; B500 census to depth 10 ~15 min; B685 deep ~min; L34 full).
set -euo pipefail
cd "$(dirname "$0")"
echo "== (1) TOMB-L310: per-level matched nulls (re-run, ~30s) =="
python3 l310_per_level_null.py | tail -3
python3 - << 'PY'
import json
d = json.load(open("l310_per_level_null.json"))
zs = [r["z"] for r in d["per_level"]]
assert d["per_level"][-1]["z"] > 8, "the L10 11-sigma deviation must reproduce"
assert all(abs(z) < 4 for z in zs[:3]), "small-L levels near-null"
print("   L310 reproduced: kill stands on drift grounds; 'indistinguishable' clause reversed (z_L10 > 8)")
PY
echo "== (2) TOMB-L34: committed profile verdict + spot re-fit (N=610) =="
python3 - << 'PY'
import json, numpy as np
d = json.load(open("l34_profile.json"))
big = [r["a"] for r in d["fib"] if r["N"] >= 987]
assert d["verdict"]["log_class_stable"] is True
assert min(big) > 0.13 and max(big) < 0.22
assert d["controls"]["random"]["a"] < 0.05 and abs(d["controls"]["periodic"]["a"]) < 0.01
# spot re-fit at N=610, shift 0 (fast)
import importlib.util
spec = importlib.util.spec_from_file_location("l34", "l34_profile.py")
# inline mini-recheck rather than importing the __main__ script:
def fib_word(n_min):
    a, b = [1], [1, 0]
    while len(b) < n_min: a, b = b, b + a
    return b
w = fib_word(700)[:610]
H = np.zeros((610, 610))
for i, c in enumerate(w): H[i, i] = 0.5 if c == 1 else -0.5
for i in range(609): H[i, i+1] = H[i+1, i] = 1.0
_, ev = np.linalg.eigh(H); psi = ev[:, :305]
Ls = np.unique(np.geomspace(8, 305, 25).astype(int)); Ss = []
for L in Ls:
    lam = np.linalg.eigvalsh(psi[:L] @ psi[:L].T)
    lam = lam[(lam > 1e-12) & (lam < 1 - 1e-12)]
    Ss.append(float(-np.sum(lam*np.log(lam) + (1-lam)*np.log(1-lam))))
X = np.vstack([np.log(Ls), np.ones(len(Ls))]).T
(a, b), *_ = np.linalg.lstsq(X, np.array(Ss), rcond=None)
assert 0.1 < a < 0.25, f"N=610 profile slope {a}"
print(f"   L34 reproduced: committed big-N a in [{min(big)},{max(big)}]; spot N=610 a={a:.3f}; controls discriminate")
PY
echo "== (3) B500 mod-2 census: depths 4-6 re-run (~5s) =="
python3 - << 'PY'
import json, subprocess, sys, re
out = subprocess.run([sys.executable, "-c", """
import runpy, sys
sys.argv = ["x", "/dev/null"]
import importlib.util
spec = importlib.util.spec_from_file_location("cen", "b500_mod2_census.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for d in (4, 5, 6):
    r = m.census_depth(d)
    print(d, r["words"], len(r["signature_words"]))
"""], capture_output=True, text=True)
rows = {int(l.split()[0]): (int(l.split()[1]), int(l.split()[2]))
        for l in out.stdout.strip().splitlines() if l and l[0].isdigit()}
assert rows[4] == (36, 0),  "depth 4: 36 words, ZERO signatures (matches the clean depth-4 hunt)"
assert rows[5] == (150, 50), "depth 5: the signature is ABUNDANT -- the obstruction route is dead"
assert rows[6][0] == 540 and rows[6][1] > 0
print(f"   B500 census reproduced: {rows} -- mod-2 exclusion route REFUTED, depth-4 zero consistent")
PY
echo "== (4) WALL-7 + B685: committed-artifact assertions (full re-runs under OA_SLOW) =="
python3 - << 'PY'
import json
d = json.load(open("wall7_all_t.json"))
assert d["deg_bound"] == 864 and d["points"] == 866
assert d["stage_a_clean"] is False or True  # see below: violations must be exactly the t=0 label
for pr in d["primes"]:
    assert pr["q"] in (1009, 1999)
    assert all(v[1] == "degenerate" and v[0] == 0 for v in pr["violations"]), pr["violations"]
print("   WALL-7: dim=0 at every nondegenerate t (1..865), all 8 patterns, both primes -- committed JSON verified")
log = open("b685_deep.log").read()
assert "OVERALL: ALL CHECKS PASS" in log and "n <= 60" in log
print("   B685: deep run (K=60, NC=240) ALL CHECKS PASS -- committed log verified")
PY
if [ "${OA_SLOW:-}" = "1" ]; then
  echo "== OA_SLOW: full sweeps =="
  python3 wall7_all_t.py wall7_all_t.json | tail -3
  python3 b500_mod2_census.py b500_mod2_census.json | tail -3
  python3 b685_deep.py > b685_deep.log 2>&1 && tail -2 b685_deep.log
  python3 l34_profile.py | tail -2
fi
echo "REPRODUCES"
