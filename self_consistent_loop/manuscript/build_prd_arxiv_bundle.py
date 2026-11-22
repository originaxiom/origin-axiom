#!/usr/bin/env python3
"""Build and verify a turnkey arXiv + APS Physical Review D submission tarball.

Why this script matters:
  arXiv's AutoTeX engine compiles REVTeX submissions with `pdflatex` ONLY (it does not run `bibtex`),
  so the submission archive MUST include the compiled `main.bbl` alongside `main.tex` and `figures/*.pdf`,
  with zero `.aux`/`.log`/`.out` build residue.

Usage:
  python3 self_consistent_loop/manuscript/build_prd_arxiv_bundle.py [--out /path/to/bundle.tar.gz]
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import tarfile
import tempfile

MANUSCRIPT_DIR = Path(__file__).resolve().parent

FIG_PDFS = (
    "figures/fig5_porti_torsions_and_covers.pdf",
    "figures/fig6_h3_green_and_zss_divergence.pdf",
    "figures/fig7_cy4_signature_and_bp.pdf",
    "figures/fig8_three_seat_bridges.pdf",
)


def _run(cmd: list[str], cwd: Path) -> str:
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(f"Command {' '.join(cmd)} failed ({proc.returncode}):\n{proc.stdout}\n{proc.stderr}")
    return proc.stdout


def build_and_verify_bundle(out_tar_gz: Path) -> dict[str, object]:
    tex_src = MANUSCRIPT_DIR / "main.tex"
    bib_src = MANUSCRIPT_DIR / "references.bib"
    assert tex_src.exists() and bib_src.exists(), "Missing main.tex or references.bib"

    # 1. Stage 1: Full pdflatex + bibtex build to generate clean main.bbl and main.pdf:
    with tempfile.TemporaryDirectory(prefix="prd_stage1_") as tmp1_s:
        tmp1 = Path(tmp1_s)
        shutil.copy2(tex_src, tmp1 / "main.tex")
        shutil.copy2(bib_src, tmp1 / "references.bib")
        (tmp1 / "figures").mkdir()
        for rel_f in FIG_PDFS:
            shutil.copy2(MANUSCRIPT_DIR / rel_f, tmp1 / rel_f)

        _run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], tmp1)
        bib_stdout = _run(["bibtex", "main"], tmp1)
        assert "Warning--" not in bib_stdout, f"BibTeX warnings detected:\n{bib_stdout}"
        _run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], tmp1)
        _run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], tmp1)

        bbl_path = tmp1 / "main.bbl"
        log_txt = (tmp1 / "main.log").read_text(encoding="utf-8", errors="replace")
        assert bbl_path.exists() and bbl_path.stat().st_size > 100, "Failed to generate non-empty main.bbl"
        overfull = re.findall(r"^Overfull \\hbox.*", log_txt, flags=re.M)
        undef = re.findall(r"LaTeX Warning:.*undefined.*", log_txt)
        assert not overfull, f"Overfull hboxes detected: {overfull}"
        assert not undef, f"Undefined references/citations detected: {undef}"

        # Pack exact arXiv/PRD source tarball (main.tex + main.bbl + 4 vector PDF figures):
        out_tar_gz.parent.mkdir(parents=True, exist_ok=True)
        members_added: list[str] = []
        with tarfile.open(out_tar_gz, "w:gz") as tf:
            tf.add(tmp1 / "main.tex", arcname="main.tex")
            members_added.append("main.tex")
            tf.add(bbl_path, arcname="main.bbl")
            members_added.append("main.bbl")
            for rel_f in FIG_PDFS:
                tf.add(tmp1 / rel_f, arcname=rel_f)
                members_added.append(rel_f)

    # 2. Stage 2: Simulate arXiv's AutoTeX server (extract tarball into empty dir, run pdflatex ONLY without bibtex!):
    with tempfile.TemporaryDirectory(prefix="arxiv_autotex_verify_") as tmp2_s:
        tmp2 = Path(tmp2_s)
        with tarfile.open(out_tar_gz, "r:gz") as tf:
            tf.extractall(tmp2, filter="data")
        _run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], tmp2)
        _run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], tmp2)
        log2 = (tmp2 / "main.log").read_text(encoding="utf-8", errors="replace")
        undef2 = re.findall(r"LaTeX Warning:.*undefined.*", log2)
        pages_m = re.search(r"Output written on main\.pdf \((\d+) pages, (\d+) bytes\)", log2)
        assert not undef2 and pages_m is not None, f"Standalone AutoTeX verification failed: {undef2}"
        n_pages, n_bytes = int(pages_m.group(1)), int(pages_m.group(2))

    return {
        "bundle_path": str(out_tar_gz),
        "bundle_bytes": out_tar_gz.stat().st_size,
        "members": members_added,
        "autotex_standalone_pages": n_pages,
        "autotex_pdf_bytes": n_bytes,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build verified arXiv + APS PRD submission tarball.")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("/tmp/arxiv_prd_submission_bundle.tar.gz"),
        help="Output .tar.gz path (defaults outside git working tree so git status stays clean).",
    )
    args = parser.parse_args()
    info = build_and_verify_bundle(args.out.resolve())
    print(f"Verified arXiv/PRD bundle written to: {info['bundle_path']} ({info['bundle_bytes']} bytes)")
    print(f"Standalone AutoTeX check PASSED: {info['autotex_standalone_pages']} pages, 0 undefined citations, members={info['members']}")


if __name__ == "__main__":
    main()
