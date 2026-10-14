"""Compare two JSON files recursively.
ints/strings/bools exactly; floats to rel 1e-8 (or abs 1e-12 when both are tiny noise-level residuals).
Usage: python3 -I jcmp.py committed.json rerun.json [ignore_key ...]
"""
import json, sys, math

REL = 1e-8
NOISE = 1e-12   # both |a|,|b| below this: a machine-precision residual, reported separately

def walk(a, b, path, out, ignore):
    if isinstance(a, dict) and isinstance(b, dict):
        ka, kb = set(a), set(b)
        for k in sorted(ka - kb): out["struct"].append(f"{path}/{k}: only in committed")
        for k in sorted(kb - ka): out["struct"].append(f"{path}/{k}: only in rerun")
        for k in sorted(ka & kb):
            if k in ignore: continue
            walk(a[k], b[k], f"{path}/{k}", out, ignore)
        return
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out["struct"].append(f"{path}: list length {len(a)} vs {len(b)}")
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, f"{path}[{i}]", out, ignore)
        return
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(a, str) or isinstance(b, str) or a is None or b is None:
        if a != b: out["exact"].append(f"{path}: {a!r} vs {b!r}")
        out["n"] += 1
        return
    if isinstance(a, int) and isinstance(b, int):
        if a != b: out["exact"].append(f"{path}: {a} vs {b}")
        out["n"] += 1
        return
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        out["n"] += 1
        a, b = float(a), float(b)
        if a == b: return
        if math.isnan(a) and math.isnan(b): return
        if abs(a) < NOISE and abs(b) < NOISE:
            out["noise"].append((path, a, b)); return
        rel = abs(a - b) / max(abs(a), abs(b))
        if rel > REL: out["float"].append((path, a, b, rel))
        else: out["small"].append((path, a, b, rel))
        return
    out["struct"].append(f"{path}: type {type(a).__name__} vs {type(b).__name__}")

def main():
    A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2])); ignore = set(sys.argv[3:])
    out = {"exact": [], "float": [], "small": [], "noise": [], "struct": [], "n": 0}
    walk(A, B, "", out, ignore)
    print(f"leaves compared: {out['n']}")
    print(f"structural diffs: {len(out['struct'])}")
    for s in out["struct"][:40]: print("  ", s)
    print(f"exact (int/str/bool) diffs: {len(out['exact'])}")
    for s in out["exact"][:40]: print("  ", s)
    print(f"float diffs > {REL} rel (non-noise): {len(out['float'])}")
    for p, a, b, r in out["float"][:60]: print(f"   {p}: {a!r} vs {b!r} rel {r:.3g}")
    print(f"float diffs <= {REL} rel: {len(out['small'])}; max rel {max([x[3] for x in out['small']], default=0):.3g}")
    print(f"noise-level (<{NOISE}) residual diffs: {len(out['noise'])}")
    for p, a, b in out["noise"][:20]: print(f"   {p}: {a!r} vs {b!r}")

if __name__ == "__main__":
    main()
