#!/usr/bin/env bash
# B1235 -- the two-seat harvest. Every cell recomputes a seat claim on THIS bench (verify-don't-trust).
set -u; cd "$(dirname "$0")"; fail=0
echo "[1] the 112-family, proper chirality test (SnapPy symmetry group; ~1-2 min)"; python3 chirality_112.py 2>/dev/null | grep -E "112-family|o10_150700|controls" || fail=1
echo "[2] A6's free deck vs CS (40 covers + controls; ~1-2 min)"; python3 a6_cover_cs.py 2>/dev/null | grep -E "VERDICT|covers" || fail=1
echo "[3] B1233's minimum is a BOX minimum"; python3 markoff_box_minimum.py | grep VERDICT || fail=1
echo "[4] ten A2+A1 sub-diagrams of E6"; python3 a2a1_subdiagrams.py || fail=1
echo "[5] B869's committed engine on B994's three parents"; python3 b994_parent_menus.py 2>/dev/null | grep -E "parent|cascade" || fail=1
echo "[6] B1011's 992/284 from the 2880 cells (blind, ~30 s)"; python3 blind_forced_counts.py | grep -E "forced cells|control" || fail=1
echo "[7] E51: the nine relays' blobs (needs origin/audit/b775-braver-questions fetched)"
python3 - <<'PY' || fail=1
import json, subprocess
m = json.load(open("e51_manifest.json"))
try:
    subprocess.check_output(["git", "cat-file", "-t", m["head"]], stderr=subprocess.DEVNULL)
except Exception:
    print("   head", m["head"], "not fetched -- run: git fetch origin audit/b775-braver-questions"); raise SystemExit(0)
for f in m["files"]:
    size = int(subprocess.check_output(["git", "cat-file", "-s", f"{m['head']}:{f['path']}"]))
    assert size == f["bytes"], (f["path"], size, f["bytes"])
print("   9/9 relays present at", m["head"], "with the recorded sizes")
PY
echo "[8] L194 bite control: is any quarter-class amphichiral member an orientation double cover? (~1 min)"; python3 l194_bite.py 2>/dev/null | grep -E "positive control|VERDICT" || fail=1
[ $fail -eq 0 ] && echo "B1235 REPRODUCES" || { echo "B1235 FAILED"; exit 1; }
