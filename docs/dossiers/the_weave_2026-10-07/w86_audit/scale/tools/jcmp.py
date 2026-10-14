"""Compare two JSON files: ints/strings/bools exactly; floats to rel 1e-8 (abs 1e-12 floor for near-zero noise).
Ignores keys whose name contains 'second' (timing). Prints every difference with its path."""
import json, sys, math
RTOL, AFLOOR = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-8, 1e-12
diffs, maxrel = [], [0.0, None]
def cmp(a, b, path):
    if isinstance(a, dict) and isinstance(b, dict):
        ka, kb = set(a), set(b)
        for k in sorted(ka - kb): diffs.append((path + "/" + str(k), "only in committed"))
        for k in sorted(kb - ka): diffs.append((path + "/" + str(k), "only in rerun"))
        for k in sorted(ka & kb, key=str):
            if "second" in str(k): continue
            cmp(a[k], b[k], path + "/" + str(k))
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): diffs.append((path, f"length {len(a)} vs {len(b)}")); return
        for i, (x, y) in enumerate(zip(a, b)): cmp(x, y, f"{path}[{i}]")
    elif isinstance(a, bool) or isinstance(b, bool) or isinstance(a, str) or isinstance(b, str) or a is None or b is None:
        if a != b or type(a) != type(b): diffs.append((path, f"{a!r} vs {b!r}"))
    elif isinstance(a, int) and isinstance(b, int):
        if a != b: diffs.append((path, f"{a} vs {b}"))
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        d = abs(a - b); s = max(abs(a), abs(b))
        if s < AFLOOR and d < AFLOOR: return
        rel = d / s if s > 0 else 0.0
        if rel > maxrel[0]: maxrel[0], maxrel[1] = rel, path
        if rel > RTOL and d > AFLOOR: diffs.append((path, f"{a!r} vs {b!r} (rel {rel:.2e})"))
    else:
        diffs.append((path, f"type {type(a).__name__} vs {type(b).__name__}: {a!r} vs {b!r}"))
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2]))
cmp(A, B, "")
print(f"compare {sys.argv[1].split('/')[-1]} vs {sys.argv[2].split('/')[-1]}: {len(diffs)} differences beyond rel {RTOL}; max rel float diff {maxrel[0]:.2e} at {maxrel[1]}")
for p, m in diffs[:60]: print("  ", p, ":", m)
