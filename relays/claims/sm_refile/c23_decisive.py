#!/usr/bin/env python3
"""SM-C23's decisive run in the new card form (fam1-v1-unset-04): relays/sm_c23/run_c23.py run unchanged, in a copy of its
folder, with the repo root as main's checkout; its rows read back and the decisive facts printed as DECISIVE: lines.
    python3 relays/claims/sm_refile/c23_decisive.py
Exit 0 when the run completes and every decisive fact comes out as the card states; 1 otherwise."""
import json, pathlib, shutil, subprocess, sys, tempfile
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
tmp = pathlib.Path(tempfile.mkdtemp()) / "sm_c23"
shutil.copytree(ROOT / "relays" / "sm_c23", tmp)
r = subprocess.run([sys.executable, "-B", "run_c23.py", str(ROOT)], cwd=tmp, capture_output=True, text=True)
if r.returncode != 0:
    print("RUN FAILED"); sys.exit(1)
rows = json.loads((tmp / "c23_results.json").read_text())["rows"]
ok = True
for g in ("T", "S", "ACT"):
    c1 = [x for x in rows if x["g"] == g and x["cand"].startswith("C1")]
    held = len(c1) == 3 and all(x["masses"] < 1e-15 and x["mixing"] < 1e-15 for x in c1)
    others = [x for x in rows if x["g"] == g and x["cand"].startswith(("C2", "C3", "C4", "C5"))]
    print("DECISIVE: %s joint, point as (a, b)g^-1, all three moduli: masses and |V| equal below 1e-15: %s" % (g, held))
    ok &= held
    if g == "T":
        print("DECISIVE: T, every other declared action fails by more than 1e-3: %s"
              % all(x["masses"] > 1e-3 for x in others))
plants = [x for x in rows if x["g"] == "plant"]
pf = len(plants) == 6 and all(x["masses"] > 1e-3 for x in plants)
print("DECISIVE: both plants (point unmoved; end unshifted) fail by more than 1e-3 at all three moduli: %s" % pf)
ok &= pf
sys.exit(0 if ok else 1)
