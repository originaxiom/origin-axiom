#!/usr/bin/env python3
r"""
phase3_rung11_format_alignment.py

Rung 11: Align Phase 3 paper formatting with Phase 1 (documentclass + geometry-style
preamble bits), so page size and margins are consistent across the program.

Strategy:
- Read phase1/paper/main.tex and extract:
  * the \documentclass line
  * any \usepackage{geometry} (or similar) lines
- Patch phase3/paper/main.tex:
  * replace its \documentclass line with Phase 1's
  * ensure any geometry lines from Phase 1 are present (inserted after \documentclass)
- Append a Rung 11 entry to phase3/PROGRESS_LOG.md.
"""

from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path


def find_documentclass_line(lines):
    for i, line in enumerate(lines):
        if line.strip().startswith(r"\documentclass"):
            return i, line
    return None, None


def extract_geometry_lines(lines):
    geom = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(r"\usepackage") and "geometry" in stripped:
            geom.append(line)
    return geom


def patch_phase3_main(root: Path) -> bool:
    p1_main = root / "phase1" / "paper" / "main.tex"
    p3_main = root / "phase3" / "paper" / "main.tex"

    if not p1_main.is_file():
        print(f"[ERROR] Missing Phase 1 main.tex at {p1_main}")
        return False
    if not p3_main.is_file():
        print(f"[ERROR] Missing Phase 3 main.tex at {p3_main}")
        return False

    p1_text = p1_main.read_text(encoding="utf-8")
    p3_text = p3_main.read_text(encoding="utf-8")

    p1_lines = p1_text.splitlines()
    p3_lines = p3_text.splitlines()

    # 1. Extract Phase 1 documentclass + geometry lines
    p1_doc_idx, p1_doc_line = find_documentclass_line(p1_lines)
    if p1_doc_line is None:
        print("[ERROR] Could not find \\documentclass in Phase 1 main.tex")
        return False

    p1_geom_lines = extract_geometry_lines(p1_lines)

    # 2. Patch Phase 3 documentclass
    p3_doc_idx, p3_doc_line = find_documentclass_line(p3_lines)
    if p3_doc_line is None:
        print("[ERROR] Could not find \\documentclass in Phase 3 main.tex")
        return False

    modified = False

    if p3_doc_line != p1_doc_line:
        print(f"[main.tex] Replacing Phase 3 documentclass:\n  OLD: {p3_doc_line}\n  NEW: {p1_doc_line}")
        p3_lines[p3_doc_idx] = p1_doc_line
        modified = True
    else:
        print("[main.tex] Documentclass already matches Phase 1; no change.")

    # 3. Ensure Phase 1 geometry lines are present in Phase 3
    p3_has_geom = any("geometry" in line for line in p3_lines)
    if p1_geom_lines and not p3_has_geom:
        insert_idx = p3_doc_idx + 1
        print("[main.tex] Inserting Phase 1 geometry-related lines after \\documentclass:")
        for g in p1_geom_lines:
            print(f"  + {g}")
        p3_lines[insert_idx:insert_idx] = p1_geom_lines
        modified = True
    elif p1_geom_lines and p3_has_geom:
        print("[main.tex] Both Phase 1 and Phase 3 have geometry lines; leaving Phase 3 as-is.")
    else:
        print("[main.tex] Phase 1 has no geometry lines; nothing to sync here.")

    if not modified:
        print("[main.tex] No formatting changes were necessary.")
        return False

    # 4. Backup and write Phase 3 main.tex
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = p3_main.with_name(p3_main.name + f".bak.{ts}")
    shutil.copy2(p3_main, backup_path)
    p3_main.write_text("\n".join(p3_lines) + "\n", encoding="utf-8")
    print(f"[main.tex] Updated Phase 3 main.tex and created backup {backup_path}")
    return True


def append_progress_log(root: Path, changed: bool) -> None:
    log_path = root / "phase3" / "PROGRESS_LOG.md"
    if not log_path.exists():
        text = "# Phase 3 Progress Log\n"
    else:
        text = log_path.read_text(encoding="utf-8")

    entry_header = "## 2026-01-06 - Rung 11: Phase 3 formatting alignment with Phase 1"

    if entry_header in text:
        print("[PROGRESS_LOG] Rung 11 entry already present; no changes made.")
        return

    if not changed:
        note = "- Checked Phase 3 main.tex against Phase 1; documentclass and geometry-style preamble already aligned.\n"
    else:
        note = (
            "- Replaced the Phase 3 \\documentclass line with the one from Phase 1 and\n"
            "  synchronized Phase 1's geometry-style preamble (if present) into\n"
            "  `phase3/paper/main.tex` so that page size and margins match across phases.\n"
        )

    entry = f\"\"\"\n\n{entry_header}\n\n{note}- No changes to claim IDs or numerical artifacts; this rung only aligns LaTeX\n  formatting so that the Phase 3 paper visually matches the established Phase 1\n  (and Phase 2) layout.\n\"\"\"
    log_path.write_text(text + entry, encoding="utf-8")
    print("[PROGRESS_LOG] Appended Rung 11 entry.")


def main():
    root = Path(__file__).resolve().parents[1]
    changed = patch_phase3_main(root)
    append_progress_log(root, changed)
    print("Rung 11 patcher completed.")


if __name__ == "__main__":
    main()
