#!/usr/bin/env python3
"""The negatives audit, reproducibility half (the owner's instruction of 2026-10-09: "make sure the negatives are not result
of bugs on scripts, misinformed or integrity of computations").  Copies frontier/ to a scratch directory, re-runs every
instrument of the window B1609..B1630 there (OA_FRONTIER pointing at the copy, so the banked files are never touched), and
compares every JSON each run writes against the banked file of the same path: identical, equal within 1e-6 relative, or
DIFFERENT (with the first differing paths).  Writes audit_sweep.json beside this script."""
import json, os, pathlib, shutil, subprocess, sys, time, math
HERE = pathlib.Path(__file__).resolve().parent; REPO = HERE.parents[2]
COPY = pathlib.Path(os.environ.get("OA_AUDIT_COPY", "/tmp/oa_audit_frontier_copy"))
ARCS = [f"B{n}" for n in range(1609, 1631)]
SKIP = {"r62_5_apply.py"}                                                     # B1626's ledger edit (not an instrument)


def walk(a, b, path="", out=None, tol=1e-6):
    out = [] if out is None else out
    if len(out) > 6: return out
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b: out.append(f"{path}/{k}: key only in {'copy' if k in a else 'banked'}"); continue
            walk(a[k], b[k], f"{path}/{k}", out, tol)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): out.append(f"{path}: length {len(a)} vs {len(b)}"); return out
        for i, (x, y) in enumerate(zip(a, b)): walk(x, y, f"{path}[{i}]", out, tol)
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)) and not isinstance(a, bool) and not isinstance(b, bool):
        if not (a == b or (math.isfinite(a) and math.isfinite(b) and abs(a - b) <= tol * max(1.0, abs(a), abs(b)))):
            out.append(f"{path}: {a} vs {b}")
    elif a != b:
        out.append(f"{path}: {str(a)[:60]} vs {str(b)[:60]}")
    return out


def main():
    if COPY.exists(): shutil.rmtree(COPY)
    shutil.copytree(REPO / "frontier", COPY, ignore=shutil.ignore_patterns("__pycache__"))
    env = dict(os.environ, OA_FRONTIER=str(COPY), PYTHONHASHSEED="0")
    report = []
    for arc in ARCS:
        for d in sorted(COPY.glob(arc + "_*")):
            ver = d / "verification"
            if not ver.is_dir(): continue
            scripts = sorted(p for p in ver.glob("*.py") if not p.name.startswith("test_") and p.name not in SKIP)
            for s in scripts:
                before = {p: p.stat().st_mtime for p in ver.rglob("*.json")}
                t0 = time.time()
                try:
                    r = subprocess.run([sys.executable, s.name], cwd=ver, env=env, capture_output=True, text=True, timeout=2400)
                    rc = r.returncode; err = (r.stderr or "")[-300:]
                except subprocess.TimeoutExpired:
                    rc = "TIMEOUT"; err = ""
                written = [p for p in ver.rglob("*.json") if p not in before or p.stat().st_mtime > before[p]]
                comps = []
                for p in written:
                    rel = p.relative_to(COPY); banked = REPO / "frontier" / rel
                    if not banked.exists(): comps.append({"json": str(rel), "status": "NEW (no banked file)"}); continue
                    try:
                        A, B = json.load(open(p)), json.load(open(banked))
                    except Exception as e:
                        comps.append({"json": str(rel), "status": f"UNREADABLE {e}"}); continue
                    if A == B: comps.append({"json": str(rel), "status": "IDENTICAL"}); continue
                    diffs = walk(A, B)
                    comps.append({"json": str(rel), "status": "EQUAL within 1e-6" if not diffs else "DIFFERENT", "first_diffs": diffs[:6]})
                report.append({"arc": d.name, "script": s.name, "rc": rc, "seconds": round(time.time() - t0, 1), "stderr_tail": err if rc not in (0,) else "", "outputs": comps})
                print(d.name, s.name, rc, [c["status"] for c in comps], flush=True)
                json.dump(report, open(HERE / "audit_sweep.json", "w"), indent=1)


if __name__ == "__main__":
    main()
