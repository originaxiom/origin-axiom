#!/usr/bin/env python3
"""per-class rung-2 driver with real timeouts (macOS has no GNU timeout)."""
import json, subprocess, sys
import os, shutil
SAGE = os.environ.get("SAGE_BIN") or shutil.which("sage") or "sage"
d = json.load(open('ptolemy_systems.json'))
for nm in ['L6a4', 's776']:
    for ci in range(len(d[nm]['3'])):
        try:
            r = subprocess.run([SAGE, 'rung2_perclass.sage', nm, str(ci)],
                               capture_output=True, text=True, timeout=1200)
            out = (r.stdout or '').strip().splitlines()
            print(out[-1] if out else f"{nm} class {ci}: NO OUTPUT rc={r.returncode}", flush=True)
        except subprocess.TimeoutExpired:
            print(f"{nm} class {ci}: TIMEOUT(20min) — recorded per ladder", flush=True)
print("RUNG2 SWEEP COMPLETE", flush=True)
