"""compare two JSON files: ints/str/bool exactly, floats to rtol (with abs floor), ignore timing keys"""
import json, sys, math
a, b = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
rtol = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-8
IGN = ("seconds",)
stats = {"floats": 0, "exact": 0, "float_bad": [], "exact_bad": [], "struct": [], "maxrel": (0.0, None)}
def rel(x, y):
    if x == y: return 0.0
    return abs(x - y) / max(abs(x), abs(y), 1e-300)
def walk(x, y, path):
    if isinstance(x, dict) and isinstance(y, dict):
        if set(x) != set(y): stats["struct"].append((path, sorted(set(x) ^ set(y))[:5]))
        for k in x:
            if k in y and not any(t in k for t in IGN): walk(x[k], y[k], path + "/" + k)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y): stats["struct"].append((path, f"len {len(x)} vs {len(y)}")); return
        for i, (u, v) in enumerate(zip(x, y)): walk(u, v, f"{path}[{i}]")
    elif isinstance(x, bool) or isinstance(y, bool) or isinstance(x, str) or isinstance(y, str) or x is None or y is None:
        stats["exact"] += 1
        if x != y: stats["exact_bad"].append((path, x, y))
    elif isinstance(x, int) and isinstance(y, int):
        stats["exact"] += 1
        if x != y: stats["exact_bad"].append((path, x, y))
    else:
        stats["floats"] += 1
        x, y = float(x), float(y)
        if math.isnan(x) and math.isnan(y): return
        r = rel(x, y)
        if r > stats["maxrel"][0]: stats["maxrel"] = (r, path, x, y)
        if r > rtol: stats["float_bad"].append((path, x, y, r))
walk(a, b, "")
print(f"exact compared {stats['exact']}, mismatches {len(stats['exact_bad'])}; floats compared {stats['floats']}, beyond rtol {rtol}: {len(stats['float_bad'])}; max rel diff {stats['maxrel']}")
for e in stats["exact_bad"][:20]: print("  EXACT MISMATCH", e)
for e in sorted(stats["float_bad"], key=lambda t: -t[3])[:15]: print("  FLOAT", e)
for e in stats["struct"][:10]: print("  STRUCT", e)
