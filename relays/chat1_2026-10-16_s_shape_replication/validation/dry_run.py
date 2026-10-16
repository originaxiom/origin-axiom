"""Dry run of s_shape_seal.py at excluded orders only (N = 8 and 10; no N = 9, 11 or 12 quantity is computed).

Exercises every code path of the sealed script on fresh-type configurations (Lyndon words of length 13 and 14 at
height <= 3) at N = 8 and 10:
  - the excluded-order controls;
  - two class representatives per order;
  - the class control (every other member of a four-member class: the mirror, the reversal and both);
  - a sign control (negated nulls);
  - the symmetry checks;
  - the scorer.
For the scorer only, the records are relabelled N = 11 (N = 10's) and N = 9 (N = 8's), so that its code paths run.
The unit-orbit read-out's within-orbit check is meaningful only at the true order, so under the false labels it is
printed, not required. The scores printed are those of excluded-order masses under false labels and mean nothing; only that
they run is checked. Timing is reported for the cost estimate.
Usage: python3 -B validation/dry_run.py <forms.pkl> > validation/dry_run_run.txt
"""
import json, os, pickle, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
SEAL = os.path.dirname(HERE)
sys.path.insert(0, SEAL)
import s_shape_seal as S
from enumerate_fresh import configs
from classes import orbit

P = pickle.load(open(sys.argv[1], "rb"))
t0 = time.time()
ctl = S.controls(P)
print("controls:", {k: v["holds"] for k, v in ctl.items()}, f"{time.time() - t0:.0f} s", flush=True)
jobs = []
for N in (8, 10):
    rows = configs(N)
    cls = {}
    for w, h, key, eps in rows:
        cls.setdefault(orbit(w, key, N), []).append((w, key))
    reps = sorted((sorted(m) for m in cls.values()), key=lambda m: m[0])
    print(f"N = {N}: {len(rows)} configurations in {len(reps)} classes", flush=True)
    two = [m for m in reps if len(m) == 4][:2]
    for ci, m in enumerate(two):
        jobs.append({"kind": "class", "N": N, "class": ci, "word": m[0][0], "line": tuple(m[0][1])})
    for mi in (1, 2, 3):
        jobs.append({"kind": "class-control", "N": N, "class": 0, "member": mi, "word": two[0][mi][0],
                     "line": tuple(two[0][mi][1])})
    jobs.append({"kind": "sign-control", "N": N, "class": 0, "member": 0, "word": two[0][0][0],
                 "line": tuple(two[0][0][1])})
for i, j in enumerate(jobs):
    j["index"] = i
records = []
for j in jobs:
    t1 = time.time()
    rec = S.one_configuration_safe((j, P))
    print(f"job {j['index']} {j['kind']} N={j['N']} {j['word']} {tuple(j['line'])}: error {rec.get('error')}; "
          f"max closure {max(rec['closure'].values()):.1e}; {time.time() - t1:.0f} s", flush=True)
    records.append(rec)
ok, sym = S.symmetry_controls(records)
print("symmetry controls hold:", ok, json.dumps(sym, default=str))
for r in records:
    r["N"] = {8: 9, 10: 11}[r["N"]]
sc = S.score(records)
print("scorer ran; class-cells per assignment:", sc["class-cells per assignment"], "; claims' keys:", list(sc["claims"]),
      "; report keys:", list(sc["report only"]), "; within-orbit spreads (must be 0 where computed):",
      {k: v.get("largest count spread within an orbit (must be 0)") for k, v in sc["report only"].items()},
      "; acceptance failures (number of keys):", len(sc["acceptance failures (class-cells, counted as not passing)"]))
print(f"total {time.time() - t0:.0f} s")
