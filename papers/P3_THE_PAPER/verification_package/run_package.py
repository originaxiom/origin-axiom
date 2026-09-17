#!/usr/bin/env python3
"""THE VERIFICATION PACKAGE of THE PAPER -- run it.

    python3 run_package.py --seals     # every seal in the manifest matches the file it sealed (seconds)
    python3 run_package.py --locks     # run every test lock the manifest names, through pytest (a few minutes)
    python3 run_package.py --scripts   # re-run every record's verification/reproduce.sh where one is shipped (slow; optional)
    python3 run_package.py             # --seals then --locks

Writes REPORT.md beside this file. Exit code 0 only if every step that ran passed. Run from anywhere inside a clone of the
repository; the manifest must be current (python3 build_manifest.py) or the report says so.
"""
import datetime, hashlib, json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]

def check_seals(man):
    rows = []; ok = True
    for c in man["claims"]:
        for r in c["records"]:
            for s in r.get("seals", []):
                target = ROOT / s["sealed_file"] if s["sealed_file"] else None
                cur = hashlib.sha256(target.read_bytes()).hexdigest() if target and target.exists() else None
                good = bool(cur) and any(cur in line for line in s["recorded"])
                ok &= good; rows.append((r["arc"], s["seal_file"], "ok" if good else "MISMATCH"))
    return ok, rows

def run_locks(man):
    tests = sorted({l for c in man["claims"] for r in c["records"] for l in r.get("locks", [])})
    if not tests: return False, ["no locks in the manifest"]
    # -rf makes pytest print a short summary naming every failure. Added 2026-09-17 (B1424) after an
    # outside referee ran this package, got "FAIL", and could not tell from the report WHICH lock failed
    # -- a report that says a check failed without naming it cannot be acted on, which defeats the point
    # of shipping the package at all. --durations surfaces the slow subprocess locks whose timeouts are
    # the usual cause of a run-to-run difference.
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-rf", "--durations=5", "--color=no", *tests],
                       capture_output=True, text=True, cwd=ROOT)
    # pytest colours its summary, so the markers do not start the line as written; strip them before
    # parsing (2026-09-17: the first version of this patch matched nothing for exactly this reason).
    out = [re.sub(r"\x1b\[[0-9;]*m", "", l) for l in r.stdout.strip().splitlines()]
    tail = out[-1] if out else r.stderr[-500:]
    named = [l.strip() for l in out if l.strip().startswith("FAILED")]
    slow = [l.strip() for l in out if " call " in l and l.strip().endswith(("s call", "s"))][:5]
    rows = [f"{len(tests)} lock files: {tail}"]
    if named:
        rows += ["", "**Failures, named:**"] + [f"  - `{x}`" for x in named]
    if slow:
        rows += ["", "**Slowest locks (a timeout here is the usual cause of a run-to-run difference):**"] + [f"  - {x}" for x in slow]
    return r.returncode == 0, rows

def run_scripts(man):
    rows = []; ok = True
    for c in man["claims"]:
        for r in c["records"]:
            if not r.get("reproduce_sh"): continue
            sh = ROOT / r["dir"] / "verification" / "reproduce.sh"
            p = subprocess.run(["bash", str(sh)], capture_output=True, text=True, cwd=sh.parent)
            ok &= (p.returncode == 0); rows.append((r["arc"], str(sh.relative_to(ROOT)), p.returncode))
    return ok, rows

def main(argv):
    man = json.loads((HERE / "MANIFEST.json").read_text(encoding="utf-8"))
    do = {a for a in argv if a.startswith("--")} or {"--seals", "--locks"}
    report = [f"# THE VERIFICATION PACKAGE — report ({datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')})", "",
              f"Manifest built {man['built']} at commit `{man['environment'].get('git_head')}`; {man['totals']}.", ""]
    all_ok = True
    if "--seals" in do:
        ok, rows = check_seals(man); all_ok &= ok
        report += [f"## Seals — {'PASS' if ok else 'FAIL'} ({sum(1 for r in rows if r[2]=='ok')}/{len(rows)} match)", ""] + [f"- `{a}` {f}: {v}" for a, f, v in rows] + [""]
        print("seals:", "PASS" if ok else "FAIL", f"{sum(1 for r in rows if r[2]=='ok')}/{len(rows)}")
    if "--locks" in do:
        ok, rows = run_locks(man); all_ok &= ok
        report += [f"## Test locks — {'PASS' if ok else 'FAIL'}", ""] + [f"- {x}" for x in rows] + [""]
        print("locks:", "PASS" if ok else "FAIL", rows[0])
    if "--scripts" in do:
        ok, rows = run_scripts(man); all_ok &= ok
        report += [f"## Shipped reproduce.sh scripts — {'PASS' if ok else 'FAIL'}", ""] + [f"- `{a}` {s}: rc={rc}" for a, s, rc in rows] + [""]
        print("scripts:", "PASS" if ok else "FAIL", len(rows))
    report.append(f"**Overall: {'PASS' if all_ok else 'FAIL'}.** All verification is internal to the repository's own re-runnable pipelines; no external review is claimed.")
    # --out <dir>, the convention build_manifest.py already uses: write the report elsewhere so
    # a test run leaves no tracked file modified (2026-09-16). Default unchanged.
    _dest = pathlib.Path(argv[argv.index("--out") + 1]) if "--out" in argv else HERE
    (_dest / "REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
