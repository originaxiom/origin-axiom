#!/usr/bin/env python3
"""second pass: the scripts that address their inputs relative to the repository root, run from the root"""
import json, os, subprocess, hashlib, sys, pathlib, time, re
WT = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); CERTDIR = pathlib.Path(sys.argv[3]); SEEDS = [int(os.environ["E83_SEED"])]
FILES = sys.argv[4:]
def git(*a): return subprocess.run(["git", "-C", str(WT)] + list(a), capture_output=True, text=True).stdout
def reset(): git("checkout", "--", "."); git("clean", "-fdq")
def state():
    out = {}
    for line in git("status", "--porcelain").splitlines():
        p = line[3:]
        if "cloud_handoff" in p: continue
        f = WT / p
        if f.is_file(): out[p] = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
        elif f.is_dir():
            for g in sorted(f.rglob("*")):
                if g.is_file() and "__pycache__" not in str(g): out[str(g.relative_to(WT))] = hashlib.sha256(g.read_bytes()).hexdigest()[:16]
    return out
def norm(so):
    so = re.sub(r"\d+\.\d+ ?s\b", "<t>s", so); so = re.sub(r"\[\s*\d+s\]", "[<t>s]", so); so = re.sub(r"\[\s*<t>s\]", "[<t>s]", so)
    return "\n".join(l for l in so.splitlines() if not re.search(r"(?i)elapsed|wall|seconds|took ", l))
res = {}
for f in FILES:
    runs = []
    for seed in SEEDS:
        reset(); link = WT / "cloud_handoff"
        if not link.exists(): os.symlink(str(CERTDIR), str(link))
        cert = str(CERTDIR / "certificates" / "twisted_double.py")
        env = dict(os.environ, PYTHONHASHSEED=str(seed), PYTHONDONTWRITEBYTECODE="1", MPLBACKEND="Agg", B1087_CERT_PATH=cert, B1098_CERT_PATH=cert)
        t0 = time.time()
        try:
            r = subprocess.run([sys.executable, f], cwd=str(WT), capture_output=True, text=True, timeout=9000, env=env); code, so, se = r.returncode, r.stdout, r.stderr
        except subprocess.TimeoutExpired: code, so, se = "TIMEOUT", "", ""
        n = norm(so)
        runs.append(dict(seed=seed, exit=code, seconds=round(time.time() - t0, 1), stdout_sha=hashlib.sha256(n.encode()).hexdigest()[:16], stdout_lines=len(so.splitlines()), stderr_tail=se[-300:], written=state()))
        (OUT / (f.replace("/", "__") + ".rootclean.seed%d.out" % seed)).write_text(so)
        print(f, "seed", seed, "exit", code, "sec", runs[-1]["seconds"], "stdout", runs[-1]["stdout_sha"], "files", len(runs[-1]["written"]), flush=True)
    res[f] = dict(runs=runs, same_exit=len({r["exit"] for r in runs}) == 1, same_stdout=len({r["stdout_sha"] for r in runs}) == 1, same_files=len({json.dumps(r["written"], sort_keys=True) for r in runs}) == 1)
    json.dump(res, open(OUT / ("e83_runs_root_clean_seed%s.json" % os.environ["E83_SEED"]), "w"), indent=1)
reset()
