#!/usr/bin/env python3
"""
phase3_rung9_methods_sections.py — Rung 9:
Give Sections 2 and 3 a methods-style structure
(fit pipeline + injection pipeline), without changing
any numerical results or claims.

- Rewrites:
  - phase3/paper/sections/02_fit_pipeline.tex
  - phase3/paper/sections/03_injection_pipeline.tex

- Appends a Rung 9 entry to phase3/PROGRESS_LOG.md.
"""

from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECTIONS_DIR = ROOT / "phase3" / "paper" / "sections"
LOG_PATH = ROOT / "phase3" / "PROGRESS_LOG.md"


FIT_PATH = SECTIONS_DIR / "02_fit_pipeline.tex"
INJ_PATH = SECTIONS_DIR / "03_injection_pipeline.tex"


FIT_CONTENT = r"""\section{Flavor-phase fit pipeline}
\label{sec:phase3-fit}

This section describes the Phase~3 ``methods'' in the narrow, empirical sense:
how we turn frozen external flavor targets into a one-parameter scan over
$\theta$ and a machine-readable $\theta$-filter.

\subsection{External targets and ansatz}

The fit is anchored to a snapshot of CKM and PMNS CP-phase information, encoded
in \path{phase3/fit/targets.yaml}. For the present run we treat this file as
fixed input: it records the numerical values taken from standard references
(PDG and NuFIT) and tags them with a simple ``ansatz label'' identifying the
mapping family used in Phase~3.

We do not attempt to explore a large model space. Instead we fix a single,
explicit ansatz that maps the Origin-Axiom phase parameter $\theta$ to the
relevant flavor-sector phases. The choice is pragmatic and clearly versioned in
\path{phase3/fit/ANSATZ_CONTRACT.md}; it is not claimed to be unique or
fundamental.

\subsection{Objective function and scan}

Given a candidate value of $\theta$, the ansatz produces predicted flavor
phases. We compare these to the external targets using a simple
$\chi^2(\theta)$ objective. The present implementation evaluates $\chi^2$ on
a regular grid in $\theta \in [0,2\pi)$ and records, for each grid point,
\begin{itemize}
  \item the value of $\theta$,
  \item the corresponding $\chi^2(\theta)$, and
  \item any auxiliary diagnostics used in the paper figures.
\end{itemize}

From this grid we extract a best-fit value $\hat{\theta}$ (the minimum of
$\chi^2$) together with an uncertainty interval defined by a simple
$\Delta\chi^2$ criterion. The details of the grid and the criterion are
recorded in the metadata files accompanying the fit tables.

\subsection{Fit artifacts}

The primary artifacts of this section are:
\begin{itemize}
  \item the summary table \path{phase3/outputs/tables/theta_fit_summary.csv};
  \item the diagnostics table \path{phase3/outputs/tables/theta_fit_diagnostics.json};
  \item the figure \path{phase3/outputs/figures/fig1_theta_fit_diagnostics.pdf}; and
  \item the ledger-facing $\theta$-filter
        \path{phase3/outputs/theta_filter/phase_03_theta_filter.json}.
\end{itemize}
These are the objects that Phase~0 and the other phases are allowed to depend
on; the internal fit code is treated as an implementation detail, provided it
reproduces the same artifacts under the gate described in the reproducibility
appendix.
"""


INJ_CONTENT = r"""\section{Injection into the Phase 2 vacuum-residue mechanism}
\label{sec:phase3-injection}

This section explains how the Phase~3 best-fit phase $\hat{\theta}$ is used
as an input to the Phase~2 vacuum-residue machinery, and what the resulting
diagnostics mean.

\subsection{One-way injection hook}

Phase~2 implements a vacuum-residue mechanism and exposes a one-parameter
injection hook for a phase-like parameter. In Phase~3 we treat this as an
opportunity to test whether the empirically fitted flavor phase is at least
compatible with the vacuum-side construction.

Operationally, we:
\begin{enumerate}
  \item take the same $\theta$ grid used in the fit;
  \item pass each $\theta$ value through the Phase~2 injection hook, keeping
        all other Phase~2 settings fixed at their baseline values; and
  \item record the resulting residue metric
        $\Delta\rho_{\mathrm{vac}}(\theta)$.
\end{enumerate}
The injection is strictly one-way: the Phase~2 outputs are not fed back into
the flavor fit, and no attempt is made to re-optimise $\theta$ on the basis
of vacuum-side information.

\subsection{Diagnostic curve and interpretation}

The resulting curve $\Delta\rho_{\mathrm{vac}}(\theta)$ is plotted in
\path{phase3/outputs/figures/fig2_delta_rho_vac_vs_theta.pdf}, with metadata
in \path{phase3/outputs/figures/fig2_delta_rho_vac_vs_theta.meta.json}. In
this paper we use the curve purely as a qualitative diagnostic: it shows how
the Phase~2 residue responds as $\theta$ is moved through the corridor defined
by the flavor fit, but we do not claim any quantitative prediction for
cosmological observables.

The only downstream interface that is allowed to act on Phase~3 is the
ledger-facing $\theta$-filter described in Appendix~D, which compares the
Phase~3 admissible region with the existing Phase~0--2 corridor. The injection
described in this section is therefore a ``sanity check'' and a source of
intuition, not a binding constraint.
"""


def backup_and_write(path: Path, new_text: str, ts: str) -> None:
    if not path.exists():
        raise SystemExit(f"ERROR: Expected file not found: {path}")
    original = path.read_text(encoding="utf-8")
    if original == new_text:
        print(f"[SKIP] {path} already matches desired content.")
        return
    backup = path.with_name(path.name + f".bak.{ts}")
    shutil.copy2(path, backup)
    path.write_text(new_text, encoding="utf-8")
    print(f"[OK] Rewrote {path} (backup at {backup})")


def update_progress_log(ts: str) -> None:
    if LOG_PATH.exists():
        text = LOG_PATH.read_text(encoding="utf-8")
    else:
        text = "# Phase 3 Progress Log\n"

    header = "## 2026-01-06 - Rung 9: Phase 3 methods-style fit and injection sections"
    if header in text:
        print("[PROGRESS_LOG] Rung 9 entry already present; no changes made.")
        return

    entry = f"""\n\n{header}

- Rewrote `phase3/paper/sections/02_fit_pipeline.tex` as a structured
  methods-style description of the flavor-phase fit: external targets and
  ansatz, objective function and scan, and the resulting fit artifacts
  (tables, diagnostics figure, and the ledger-facing θ-filter).
- Rewrote `phase3/paper/sections/03_injection_pipeline.tex` as a structured
  description of the one-way injection of θ into the Phase 2 vacuum-residue
  mechanism and the interpretation of the resulting
  Δρ_{{\\mathrm{{vac}}}}(θ) diagnostic curve.
- No changes to the numerical results, fit configuration, or claim IDs;
  this rung only improves the clarity and conventional ``Methods'' feel of
  the core Phase 3 sections.
"""
    LOG_PATH.write_text(text + entry, encoding="utf-8")
    print("[PROGRESS_LOG] Appended Rung 9 entry.")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_and_write(FIT_PATH, FIT_CONTENT, ts)
    backup_and_write(INJ_PATH, INJ_CONTENT, ts)
    update_progress_log(ts)
    print("Rung 9 patcher completed.")


if __name__ == "__main__":
    main()