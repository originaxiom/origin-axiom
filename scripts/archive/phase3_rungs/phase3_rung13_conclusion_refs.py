#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


def get_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def patch_limitations(path: Path) -> bool:
    """Append a Conclusion and outlook subsection to 05_limitations.tex if missing."""
    if not path.exists():
        print(f"[WARN] Limitations file not found at {path}; skipping conclusion/outlook.")
        return False

    text = path.read_text(encoding="utf-8")
    if "Conclusion and outlook" in text:
        print("[05_limitations.tex] Conclusion/outlook subsection already present; skipping.")
        return False

    lines = [
        r"\subsection{Conclusion and outlook}",
        "",
        r"Phase~3, in its present configuration, should be read as a focused calibration rung",
        r"rather than a discovery claim. We demonstrate that, under a frozen CKM/PMNS target",
        r"snapshot and a fixed ansatz, one can extract a well-defined flavor-phase interval",
        r"and export it as a ledger-compatible $\theta$-filter, and that injecting this",
        r"interval into the Phase~2 vacuum-residue mechanism currently yields an empty global",
        r"corridor once all filters are combined.",
        "",
        r"This negative outcome is scientifically useful: it ties the failure to a specific,",
        r"versioned ansatz/target choice and makes it reproducible in the Phase~0 ledger.",
        r"Future Phase~3 iterations can revisit either component — updating external flavor",
        r"data or relaxing/replacing the ansatz family — and compare their corridor behavior",
        r"directly against the baseline reported here. A Phase~4+ program would only be",
        r"warranted in configurations where a non-empty corridor emerges and remains stable",
        r"under such revisions.",
        "",
    ]
    conclusion_block = "\n".join(lines)

    new_text = text.rstrip() + "\n\n" + conclusion_block + "\n"
    if new_text == text:
        print("[05_limitations.tex] No changes applied (text unchanged).")
        return False

    path.write_text(new_text, encoding="utf-8")
    print("[05_limitations.tex] Appended Conclusion and outlook subsection.")
    return True


def collect_bib_keys(bib_path: Path) -> set[str]:
    """Parse Reference.bib and return a set of entry keys."""
    if not bib_path.exists():
        print(f"[WARN] Reference.bib not found at {bib_path}; skipping reference hooks.")
        return set()

    bib_text = bib_path.read_text(encoding="utf-8")
    keys: set[str] = set()
    # Match things like: @article{pdg2024,  or @misc{nufit2024,
    for m in re.finditer(r"@\w+\s*\{\s*([^,]+),", bib_text):
        keys.add(m.group(1).strip())
    print(f"[Reference.bib] Found {len(keys)} keys: {', '.join(sorted(keys))}")
    return keys


def patch_fit_section(path: Path, bib_keys: set[str]) -> bool:
    """Add PDG/NuFIT citation to the fit Methods section if possible."""
    if not path.exists():
        print(f"[WARN] Fit pipeline file not found at {path}; skipping reference insertion.")
        return False

    text = path.read_text(encoding="utf-8")
    anchor = "standard references (PDG and NuFIT snapshots)"

    if anchor not in text:
        print("[02_fit_pipeline.tex] Anchor text for PDG/NuFIT not found; skipping reference insertion.")
        return False

    # If there is already a \cite near that phrase, do nothing
    if "PDG and NuFIT snapshots\\cite" in text or "PDG and NuFIT snapshots \\cite" in text:
        print("[02_fit_pipeline.tex] PDG/NuFIT citation already present; skipping.")
        return False

    cite_keys: list[str] = []

    if "pdg2024" in bib_keys:
        cite_keys.append("pdg2024")

    # Pick a NuFIT-like key if any
    nufit_key = next((k for k in bib_keys if k.lower().startswith("nufit")), None)
    if nufit_key:
        cite_keys.append(nufit_key)

    if not cite_keys:
        print("[02_fit_pipeline.tex] No PDG/NuFIT-like keys found in Reference.bib; skipping reference insertion.")
        return False

    cite_str = " \\cite{" + ",".join(cite_keys) + "}"
    new_text = text.replace(anchor, anchor + cite_str, 1)

    if new_text == text:
        print("[02_fit_pipeline.tex] Replacement produced no change; skipping.")
        return False

    path.write_text(new_text, encoding="utf-8")
    print(f"[02_fit_pipeline.tex] Added PDG/NuFIT citation using keys: {', '.join(cite_keys)}.")
    return True


def patch_progress_log(path: Path, did_lim: bool, did_refs: bool) -> bool:
    if not path.exists():
        print(f"[WARN] PROGRESS_LOG not found at {path}; no log entry written.")
        return False

    text = path.read_text(encoding="utf-8")
    header = "## 2026-01-06 - Rung 13: Conclusion/outlook + reference hooks"

    if header in text:
        print("[PROGRESS_LOG] Rung 13 entry already present; skipping.")
        return False

    lines: list[str] = [header, ""]

    if did_lim:
        lines.append(
            "- Added a `Conclusion and outlook` subsection to "
            "`phase3/paper/sections/05_limitations.tex` to summarise the "
            "negative-corridor result and frame Phase 3 as a calibration rung "
            "with an explicit failure mode."
        )
    if did_refs:
        lines.append(
            "- Inserted PDG/NuFIT citation hooks in "
            "`phase3/paper/sections/02_fit_pipeline.tex`, conditioned on the "
            "presence of corresponding keys in `phase3/paper/Reference.bib`, "
            "to anchor the external flavor targets to standard data releases."
        )

    if did_lim or did_refs:
        lines.append(
            "- No changes to claim IDs (C3.1–C3.3), numerical artifacts, or gate "
            "workflow; this rung only improves narrative closure and reference hygiene."
        )
    else:
        lines.append(
            "- No textual changes were required by this rung (files were already in "
            "the desired state); this entry documents that the cross-check was performed."
        )

    entry = "\n".join(lines) + "\n"
    path.write_text(text.rstrip() + "\n\n" + entry, encoding="utf-8")
    print("[PROGRESS_LOG] Appended Rung 13 entry.")
    return True


def main() -> None:
    root = get_repo_root()
    phase3 = root / "phase3"
    lim_path = phase3 / "paper" / "sections" / "05_limitations.tex"
    fit_path = phase3 / "paper" / "sections" / "02_fit_pipeline.tex"
    bib_path = phase3 / "paper" / "Reference.bib"
    log_path = phase3 / "PROGRESS_LOG.md"

    print(f"[INFO] Repo root inferred as: {root}")

    did_lim = patch_limitations(lim_path)
    bib_keys = collect_bib_keys(bib_path)
    did_refs = False
    if bib_keys:
        did_refs = patch_fit_section(fit_path, bib_keys)

    patch_progress_log(log_path, did_lim, did_refs)

    if did_lim or did_refs:
        print("Rung 13 completed: one or more Phase 3 paper files were updated.")
    else:
        print("Rung 13 completed: no LaTeX content changes were necessary (already in desired state).")


if __name__ == "__main__":
    main()
