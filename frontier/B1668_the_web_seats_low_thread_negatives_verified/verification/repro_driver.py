"""Re-execute sealed one_configuration() for given configuration indices; compare to stored output records."""
import sys, os, json, pickle, random, math, time
HERE = os.path.abspath("tu"); sys.path.insert(0, HERE)
forms, idx = sys.argv[1], int(sys.argv[2])
sys.argv = ["twisted_units_seal.py", forms]
import twisted_units_seal as S
cfg = json.load(open(f"{HERE}/tlow_configurations.json"))
jobs = []
for N in ("9", "11", "12"):
    for w, h, key, eps in cfg[N]:
        jobs.append((len(jobs), int(N), w, tuple(key), pickle.load(open(forms, "rb")) if not jobs else None))
P = pickle.load(open(forms, "rb"))
job = list(jobs[idx]); job[4] = P
t0 = time.time(); new = S.one_configuration(tuple(job)); dt = time.time() - t0
old = json.load(open(f"stored_rec_{idx}.json"))
def cmp(a, b, path, acc):
    if isinstance(a, dict):
        assert set(a) == set(b), path
        for k in a: cmp(a[k], b[k], path + "/" + str(k), acc)
    elif isinstance(a, list):
        assert len(a) == len(b), path
        for i, (x, y) in enumerate(zip(a, b)): cmp(x, y, path, acc)
    elif a is None or b is None: acc["none"] += (a is not b)
    elif isinstance(a, (int, float)) and not isinstance(a, bool):
        acc["n"] += 1
        if a != b:
            acc["diff"] += 1; rel = abs(a - b) / max(abs(a), abs(b), 1e-300); acc["maxrel"] = max(acc["maxrel"], rel)
            if path.endswith("closure") or "closure" in path: acc["clos_diff"] = max(acc["clos_diff"], abs(a - b))
    else: acc["str"] += (a != b)
acc = dict(n=0, diff=0, maxrel=0.0, none=0, str=0, clos_diff=0.0)
newj = json.loads(json.dumps(new, default=str))
for k in ("N", "word", "line", "rotation", "line_in_rotation", "height", "bits", "Npts", "closure", "plan", "cells"):
    cmp(newj[k], old[k], k, acc)
# also check s-values separately: max rel diff on singular values
mx = 0.0
for k, e in old["cells"].items():
    n = newj["cells"][k]
    if e is None: assert n is None; continue
    for x, y in zip(e["s"], n["s"]): mx = max(mx, abs(x - y) / abs(x))
print(f"idx {idx} N={old['N']} word={old['word']} line={old['line']} time {dt:.0f}s (stored {old['seconds']}s)")
print("  numbers compared", acc["n"], "differing", acc["diff"], "max rel diff (any)", acc["maxrel"], "max rel diff singular values", mx, "max abs closure diff", acc["clos_diff"], "str/none diffs", acc["str"], acc["none"])
