#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

apply_one () {
  local path="$1"
  local label="$2"
  local claim_id="$3"

  if [ ! -f "$path" ]; then
    echo "ERROR: missing file: $path"
    exit 1
  fi

  python3 - <<PY
from pathlib import Path
import re

p = Path(r"$path")
label = r"$label"
claim_id = r"$claim_id"

s = p.read_text(encoding="utf-8")

checklist = (
    "% === P2-S4b CLAIM STRUCTURE CHECKLIST (keep; delete only after Phase 2 lock) ===\n"
    f"% File: {p.as_posix()}\n"
    f"% Must contain: (i) \\\\paragraph{{Claim ({claim_id}).}} with a single-sentence claim,\n"
    "% (ii) explicit figure pointer(s) (e.g. Fig.~A / Figs.~B--D / Fig.~E),\n"
    "% (iii) explicit pointer to Appendix run manifest (Appendix~\\\\ref{app:run_manifest}),\n"
    "% (iv) explicit non-claims boundary sentence.\n"
    "% No new physics claims; structure/clarity only.\n"
    "% === END CHECKLIST ===\n\n"
)

# 1) Ensure checklist exists at top
if not s.lstrip().startswith("% === P2-S4b CLAIM STRUCTURE CHECKLIST"):
    s = checklist + s

# 2) Ensure label exists somewhere; if missing, insert right after first \\section{...}
if f"\\\\label{{{label}}}" not in s:
    sec_pat = re.compile(r"(\\\\section\\{[^}]*\\}\\s*\\n)", re.M)
    m = sec_pat.search(s)
    if not m:
        raise SystemExit(f"ERROR: no \\\\section{{...}} found in {p}")
    insert_at = m.end()
    s = s[:insert_at] + f"\\\\label{{{label}}}\\n" + s[insert_at:]

p.write_text(s, encoding="utf-8")
print(f"OK: hardened structure: {p}")
PY
}

# Apply to the 3 claim sections
apply_one "phase2/paper/sections/03_claim_C2_1_existence.tex"    "sec:claim_c21" "C2.1"
apply_one "phase2/paper/sections/04_claim_C2_2_robustness.tex"   "sec:claim_c22" "C2.2"
apply_one "phase2/paper/sections/05_claim_C2_3_frw_viability.tex" "sec:claim_c23" "C2.3"

echo
echo "== Phase 2 Claim Structure Scan =="

scan_one () {
  local path="$1"
  local label="$2"
  local claim_id="$3"

  echo
  echo "--- $path ---"
  rg -n -F "\\label{$label}" "$path" || echo "WARN: missing label $label"
  rg -n -F "\\paragraph{Claim ($claim_id).}" "$path" || echo "WARN: missing Claim paragraph"
  rg -n "Fig\\.|Figs\\." "$path" || echo "WARN: no Fig reference found"
  rg -n -F "Appendix~\\ref{app:run_manifest}" "$path" || echo "WARN: no run-manifest pointer found"
  rg -n -i "non-claims|nonclaims|scope|not a prediction|not interpret|limitations" "$path" || echo "WARN: no obvious non-claims boundary found"
}

scan_one "phase2/paper/sections/03_claim_C2_1_existence.tex"     "sec:claim_c21" "C2.1"
scan_one "phase2/paper/sections/04_claim_C2_2_robustness.tex"    "sec:claim_c22" "C2.2"
scan_one "phase2/paper/sections/05_claim_C2_3_frw_viability.tex" "sec:claim_c23" "C2.3"

echo
echo "Done."
