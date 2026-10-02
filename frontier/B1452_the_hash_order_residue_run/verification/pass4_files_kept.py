#!/usr/bin/env python3
"""fourth pass: b1100_hypercharge needs b1100_exact5.json, which b1100_exact_table writes in the working directory.
That product has one hash on four seeds and is byte-identical to the tracked b1100_exact_table.json, so a copy of the
tracked file is placed in the working directory beforehand (the table is re-run only if it is absent); then the
hypercharge script under four seeds, and b1102_adapted_basis under four seeds, keeping the JSON each writes."""
import json, os, subprocess, hashlib, sys, pathlib, time, re, shutil
WT = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2]); CERTDIR = pathlib.Path(sys.argv[3]); OUT.mkdir(exist_ok=True)
link = WT / "cloud_handoff"
if not link.exists(): os.symlink(str(CERTDIR), str(link))
cert = str(CERTDIR / "certificates" / "twisted_double.py")
def run(f, seed, timeout):
    env = dict(os.environ, PYTHONHASHSEED=str(seed), PYTHONDONTWRITEBYTECODE="1", MPLBACKEND="Agg", B1087_CERT_PATH=cert, B1098_CERT_PATH=cert)
    t0 = time.time(); r = subprocess.run([sys.executable, f], cwd=str(WT), capture_output=True, text=True, timeout=timeout, env=env)
    (OUT / (f.replace("/", "__") + ".seed%d.out" % seed)).write_text(r.stdout); print(f, "seed", seed, "exit", r.returncode, "sec", round(time.time() - t0, 1), (r.stderr.strip().splitlines() or [""])[-1][:150], flush=True)
    return r.returncode
for seed in range(4):
    run("frontier/B1102_exact_hypercharge_solve/b1102_adapted_basis.py", seed, 600)
    shutil.copy(WT / "frontier/B1102_exact_hypercharge_solve/b1102_intermediate.json", OUT / ("b1102_intermediate.seed%d.json" % seed))
    subprocess.run(["git", "-C", str(WT), "checkout", "--", "frontier/B1102_exact_hypercharge_solve"])
if not (WT / "b1100_exact5.json").exists(): run("frontier/B1100_landing_content/b1100_exact_table.py", 0, 14400)
shutil.copy(WT / "b1100_exact5.json", OUT / "b1100_exact5.json")
for seed in range(4):
    run("frontier/B1100_landing_content/b1100_hypercharge.py", seed, 3600)
    for nm in ("b1100_hyper.json",):
        if (WT / nm).exists(): shutil.copy(WT / nm, OUT / (nm + ".seed%d" % seed))
    for g in WT.glob("frontier/B1100_landing_content/*.json"): shutil.copy(g, OUT / (g.name + ".seed%d" % seed))
    subprocess.run(["git", "-C", str(WT), "checkout", "--", "frontier/B1100_landing_content"])
print("DONE", flush=True)
