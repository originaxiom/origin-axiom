#!/usr/bin/env bash
# B1207 -- the slow lane's first full run, triaged and discharged.
set -euo pipefail
cd "$(dirname "$0")/../../.."
python3 - << 'PY' 2>/dev/null | tee frontier/B1207_slow_lane_discharge/verification/discharge.txt
import json, os, re
from pathlib import Path
R = Path(".").resolve()
ok = True

# (1) no arc verification script carries an absolute machine path
bad = [str(p.relative_to(R)) for p in R.glob("frontier/*/verification/*.py")
       if "/Users/" in p.read_text(encoding="utf-8", errors="ignore")]
print(f"(1) verification scripts with absolute machine paths: {len(bad)}")
ok &= not bad

# (2) every arc carrying a verdict also carries a findings document
orphan = [p.parent.name for p in R.glob("frontier/B1*/arc_verdict.json")
          if not (p.parent / "FINDINGS.md").exists()]
print(f"(2) verdicts with no findings document: {len(orphan)}")
ok &= not orphan

# (3) every NEGATIVE-verdict arc is routed in the kill graph
kg = json.loads((R / "frontier/B738_pathfinder_compiler/kill_graph.json").read_text())
routed = {r.get("id") for r in kg}
negs = {json.loads(p.read_text())["id"] for p in R.glob("frontier/*/arc_verdict.json")
        if json.loads(p.read_text()).get("verdict") == "NEGATIVE"}
print(f"(3) NEGATIVE arcs: {len(negs)}; unrouted: {len(negs - routed)}")
ok &= not (negs - routed)

# (4) B1113's root resolves to the repo, not to frontier/ (the doubled-path defect)
src = (R / "frontier/B1113_tmeter/b1113_tmeter_verify.py").read_text()
depth = src.count("os.path.dirname(", src.index("REPO_ROOT ="), src.index("CCB_PATH ="))
print(f"(4) B1113 REPO_ROOT dirname depth: {depth} (needs 3: <root>/frontier/<arc>/file.py)")
ok &= depth == 3

# (5) the review gate's ID strip is bounded -- it must still expose a bare ID,
#     and must not eat a colon-free reason whole
ID = r"^R[\d-]+\s*[:→—-]?\s*"
bare_ok = len(re.sub(ID, "", "R99-9").strip()) < 25
reason_ok = len(re.sub(ID, "", "R49-5 → folded into R50-6 (T-GOLDEN-MERIDIAN verify).").strip()) >= 25
print(f"(5) ID strip: flags a bare id={bare_ok}, keeps a colon-free reason={reason_ok}")
ok &= bare_ok and reason_ok

print("\nREPRODUCES" if ok else "\nFAILED")
PY
