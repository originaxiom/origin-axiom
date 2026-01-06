#!/usr/bin/env python3
"""
phase3_rung12_crossref_cleanup.py

Rung 12: fix Phase 3 cross-references:
- Replace "Section ??" with "Section~\\ref{sec:phase3-fit}" in 05_limitations.tex
- Replace "Appendix ??" with "Appendix~\\ref{app:offset_sweep_table}" in 05_limitations.tex
- Replace "Appendix D" with "Appendix~\\ref{sec:theta_filter_artifact}" in 03_injection_pipeline.tex
- Append a Rung 12 entry to phase3/PROGRESS_LOG.md

Each file is only modified if the expected needle is present and the new text
is not already there. Backups are created as *.bak.TIMESTAMP next to originals.
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime
import shutil
import sys


def backup_and_write(path: Path, text: str) -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = path.with_name(path.name + f".bak.{ts}")
    shutil.copy2(path, backup_path)
    path.write_text(text, encoding="utf-8")
    print(f"[backup] {path} -> {backup_path}")
    print(f"[write]  {path} updated.")


def patch_file(path: Path, replacements: list[tuple[str, str]]) -> None:
    if not path.exists():
        print(f"[WARN] {path} does not exist; skipping.")
        return

    text = path.read_text(encoding="utf-8")
    original = text
    modified = False

    for old, new in replacements:
        if new in text:
            # Already patched for this pattern
            print(f"[SKIP] {path.name}: target '{new}' already present; '{old}' replacement not needed.")
            continue
        if old not in text:
            print(f"[WARN] {path.name}: expected pattern '{old}' not found; no replacement.")
            continue

        print(f"[PATCH] {path.name}: replacing '{old}' -> '{new}'")
        text = text.replace(old, new, 1)
        modified = True

    if modified and text != original:
        backup_and_write(path, text)
    else:
        if not modified:
            print(f"[INFO] {path.name}: no changes applied (already in desired state?).")


def patch_crossrefs(root: Path) -> None:
    # 05_limitations.tex: Section ??, Appendix ??
    lim_path = root / "phase3/paper/sections/05_limitations.tex"
    lim_replacements = [
        ("Section ??", "Section~\\ref{sec:phase3-fit}"),
        ("Appendix ??", "Appendix~\\ref{app:offset_sweep_table}"),
    ]
    patch_file(lim_path, lim_replacements)

    # 03_injection_pipeline.tex: Appendix D -> Appendix~\ref{sec:theta_filter_artifact}
    inj_path = root / "phase3/paper/sections/03_injection_pipeline.tex"
    inj_replacements = [
        ("Appendix D", "Appendix~\\ref{sec:theta_filter_artifact}"),
    ]
    patch_file(inj_path, inj_replacements)


def patch_progress_log(root: Path) -> None:
    log_path = root / "phase3/PROGRESS_LOG.md"
    if not log_path.exists():
        print(f"[WARN] {log_path} missing; cannot append Rung 12 entry.")
        return

    text = log_path.read_text(encoding="utf-8")
    entry_header = "## 2026-01-06 - Rung 12: Phase 3 cross-reference cleanup"

    if entry_header in text:
        print("[PROGRESS_LOG] Rung 12 entry already present; no changes made.")
        return

    entry = (
        f"\n\n{entry_header}\n\n"
        "- Replaced the placeholder cross-reference `Section ??` in "
        "`phase3/paper/sections/05_limitations.tex` with "
        "`Section~\\\\ref{{sec:phase3-fit}}` so the Discussion points to the\n"
        "  Phase 3 flavor-phase fit Methods section.\n"
        "- Replaced the placeholder `Appendix ??` in "
        "`phase3/paper/sections/05_limitations.tex` with "
        "`Appendix~\\\\ref{{app:offset_sweep_table}}`, tying the discussion of\n"
        "  fixed-offset choices to the labeled offset-sweep appendix.\n"
        "- Updated `phase3/paper/sections/03_injection_pipeline.tex` so the\n"
        "  reference to the Phase 3 θ-filter appendix uses "
        "`Appendix~\\\\ref{{sec:theta_filter_artifact}}` instead of a hard-coded\n"
        "  letter, keeping the cross-reference robust under appendix reordering.\n"
        "- No changes to claim IDs, numerical artifacts, or gate workflow; this\n"
        "  rung only cleans up LaTeX cross-references for a more stable and\n"
        "  readable Phase 3 paper.\n"
    )

    backup_and_write(log_path, text + entry)
    print("[PROGRESS_LOG] Appended Rung 12 entry.")


def main() -> None:
    # Assume script lives in scripts/ under repo root
    root = Path(__file__).resolve().parent.parent
    print(f"[INFO] Repo root inferred as: {root}")

    patch_crossrefs(root)
    patch_progress_log(root)
    print("Rung 12 cross-reference cleanup completed.")


if __name__ == "__main__":
    main()
