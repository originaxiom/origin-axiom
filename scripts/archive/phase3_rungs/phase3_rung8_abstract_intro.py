#!/usr/bin/env python3
from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]

def backup(path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = path.with_name(path.name + f".bak.{ts}")
    shutil.copy2(path, backup_path)
    print(f"[backup] {path} -> {backup_path}")
    return backup_path

# --- Patch 1: Replace abstract in main.tex ---

main_path = root / "phase3/paper/main.tex"
if not main_path.exists():
    print(f"ERROR: {main_path} not found.")
    sys.exit(1)

backup(main_path)
text = main_path.read_text(encoding="utf-8")

start = text.find(r"\begin{abstract}")
end = text.find(r"\end{abstract}", start)

if start == -1 or end == -1:
    print("ERROR: Could not find \\begin{abstract}...\\end{abstract} in main.tex")
    sys.exit(1)

end += len(r"\end{abstract}")

new_abstract = r"""\begin{abstract}
Phase~3 of the Origin-Axiom program is a ledger-compatible flavor-sector calibration add-on.
Under a fixed, explicitly stated ansatz, and for a frozen snapshot of CKM and PMNS CP-phase
targets, we scan a one-parameter family $\theta \in [0,2\pi)$ to extract a best-fit
$\hat{\theta}$ and an uncertainty interval. We expose this fit as a schema-stable
$\theta$-filter JSON artifact, designed to be consumed by the Phase~0 corridor ledger
alongside the existing Phase~1 and Phase~2 filters. We then inject the fitted $\theta$
into the Phase~2 vacuum-residue mechanism to compute a diagnostic
$\Delta\rho_{\mathrm{vac}}(\theta)$ curve, keeping the injection strictly one-way
(no feedback of Phase~2 into the flavor fit). In the baseline configuration documented
here, the Phase~0 ledger reports that the combined corridor is empty once the Phase~3
filter is applied. We interpret this as a negative test for the locked Phase~3
ansatz/target combination, not as a proof that no Origin-Axiom-compatible corridor
exists. The purpose of this paper is to make this calibration step and its failure
mode reproducible, auditable, and upgradeable as flavor data and ansatz choices evolve.
\end{abstract}
"""

new_text = text[:start] + new_abstract + text[end:]

if new_text == text:
    print("WARN: main.tex abstract appears unchanged; no modifications applied.")
else:
    main_path.write_text(new_text, encoding="utf-8")
    print("[main.tex] Replaced abstract block.")

# --- Patch 2: Rename Scope section to Introduction ---

scope_path = root / "phase3/paper/sections/01_scope_and_nonclaims.tex"
if not scope_path.exists():
    print(f"ERROR: {scope_path} not found.")
    sys.exit(1)

backup(scope_path)
scope_text = scope_path.read_text(encoding="utf-8")
original_scope_text = scope_text

scope_text = scope_text.replace(
    r"\section{Scope and Non-Claims}",
    r"\section{Introduction}",
    1,
)
scope_text = scope_text.replace(
    r"\label{sec:scope}",
    r"\label{sec:introduction}",
    1,
)

if scope_text == original_scope_text:
    print("WARN: 01_scope_and_nonclaims.tex was not modified (section or label not found).")
else:
    scope_path.write_text(scope_text, encoding="utf-8")
    print("[01_scope_and_nonclaims.tex] Renamed section to Introduction and updated label.")

# --- Patch 3: Progress log entry ---

log_path = root / "phase3/PROGRESS_LOG.md"
if log_path.exists():
    log_text = log_path.read_text(encoding="utf-8")
else:
    log_text = "# Phase 3 Progress Log\n"

entry_header = "## 2026-01-06 - Rung 8: Phase 3 abstract + introduction upgrade"
if entry_header in log_text:
    print("[PROGRESS_LOG] Rung 8 entry already present; no changes made.")
else:
    entry = f"""\n\n{entry_header}

- Replaced the Phase 3 abstract with a structured summary that states the ansatz,
  external flavor targets, grid scan, injection into Phase 2, and the ledger outcome
  (empty combined corridor in the baseline configuration).
- Renamed `\\\\section{{Scope and Non-Claims}}` to `\\\\section{{Introduction}}` and
  updated the label to `sec:introduction` so the Phase 3 paper front matter reads
  like a conventional introduction while preserving the existing scope / non-claims content.
- No changes to claim IDs (C3.1–C3.3), filters, or numerical results; this rung only
  improves the narrative structure of the front section.
"""
    log_path.write_text(log_text + entry, encoding="utf-8")
    print("[PROGRESS_LOG] Appended Rung 8 entry.")

print("Rung 8 patcher completed.")
