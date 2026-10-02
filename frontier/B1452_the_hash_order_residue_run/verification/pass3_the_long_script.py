#!/usr/bin/env python3
"""Re-run every banked verification script carrying an unsorted order-sensitive site under several PYTHONHASHSEED
values, in a scratch checkout, and compare what each run prints and writes."""
import json, os, subprocess, hashlib, sys, pathlib, time
WT = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); SEEDS = [int(os.environ["E83_SEED"])]
sweep = json.load(open(WT / "frontier/B1425_the_flaky_lock_and_the_hollow_green/verification/order_sensitivity_sweep.json"))
files = []
for s in sweep["unsorted_sites"]:
    if not s["file"].startswith("tests/") and s["file"] not in files: files.append(s["file"])
only = sys.argv[3:] or files
def git(*a): return subprocess.run(["git", "-C", str(WT)] + list(a), capture_output=True, text=True).stdout
def reset(): git("checkout", "--", "."); git("clean", "-fdq")
def state():
    out = {}
    for line in git("status", "--porcelain").splitlines():
        p = line[3:]
        f = WT / p
        if "cloud_handoff" in p: continue
        if f.is_file(): out[p] = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
        elif f.is_dir():
            for g in sorted(f.rglob("*")):
                if g.is_file() and "__pycache__" not in str(g): out[str(g.relative_to(WT))] = hashlib.sha256(g.read_bytes()).hexdigest()[:16]
    return out
res = {}
for f in files:
    if f not in only: continue
    runs = []
    for seed in SEEDS:
        reset(); t0 = time.time()
        link = (WT / f).parent / "cloud_handoff"
        CERTDIR = pathlib.Path(sys.argv[2]).parent / "e83_cert"
        if not link.exists(): os.symlink(str(CERTDIR), str(link))
        cert = str(CERTDIR / "certificates" / "twisted_double.py")
        env = dict(os.environ, PYTHONHASHSEED=str(seed), PYTHONDONTWRITEBYTECODE="1", MPLBACKEND="Agg", B1087_CERT_PATH=cert, B1098_CERT_PATH=cert)
        try:
            r = subprocess.run([sys.executable, os.path.basename(f)], cwd=str((WT / f).parent), capture_output=True, text=True, timeout=14400, env=env)
            code, so, se = r.returncode, r.stdout, r.stderr
        except subprocess.TimeoutExpired as e:
            code, so, se = "TIMEOUT", (e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or ""), ""
        import re
        norm = re.sub(r"\d+\.\d+ ?s\b", "<t>s", so); norm = re.sub(r"\[\s*<t>s\]", "[<t>s]", norm)
        norm = "\n".join(l for l in norm.splitlines() if not re.search(r"(?i)elapsed|wall|seconds|took ", l))
        runs.append(dict(seed=seed, exit=code, seconds=round(time.time() - t0, 1), stdout_sha=hashlib.sha256(norm.encode()).hexdigest()[:16],
                         stdout_lines=len(so.splitlines()), stderr_tail=se[-300:], written=state()))
        (OUT / (f.replace("/", "__") + ".seed%d.out" % seed)).write_text(so)
        print(f, "seed", seed, "exit", code, "sec", runs[-1]["seconds"], "stdout", runs[-1]["stdout_sha"], "files", len(runs[-1]["written"]), flush=True)
        if code == "TIMEOUT": break
    res[f] = dict(runs=runs, same_exit=len({r["exit"] for r in runs}) == 1, same_stdout=len({r["stdout_sha"] for r in runs}) == 1,
                  same_files=len({json.dumps(r["written"], sort_keys=True) for r in runs}) == 1)
    json.dump(res, open(OUT / ("e83_runs_b1098_seed%s.json" % os.environ["E83_SEED"]), "w"), indent=1)
reset()
