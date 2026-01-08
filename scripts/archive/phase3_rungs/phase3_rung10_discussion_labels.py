#!/usr/bin/env python3
from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

root = Path(__file__).resolve().parents[1]

def backup(path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = path.with_name(path.name + f".bak.{ts}")
    shutil.copy2(path, backup_path)
    print(f"[backup] {path} -> {backup_path}")
    return backup_path

# --- Targets ---
claims_path = root / "phase3/paper/appendix/A_claims_table.tex"
offs_path   = root / "phase3/paper/appendix/C_offset_sweep_table.tex"
theta_path  = root / "phase3/paper/appendix/D_theta_filter.tex"
lim_path    = root / "phase3/paper/sections/05_limitations.tex"
log_path    = root / "phase3/PROGRESS_LOG.md"

for p in (claims_path, offs_path, theta_path, lim_path):
    if not p.exists():
        print(f"ERROR: {p} not found.")
        raise SystemExit(1)

# --- Backup originals ---
backup(claims_path)
backup(offs_path)
backup(theta_path)
backup(lim_path)

# --- Label patch: A_claims_table.tex ---
claims_text = claims_path.read_text(encoding="utf-8")
if "\\label{app:phase3_claims_table}" in claims_text:
    print("[A_claims_table] Label already present.")
else:
    needle = r"\section{Claims Table (Phase 3)}"
    if needle in claims_text:
        claims_text = claims_text.replace(
            needle,
            needle + "\n\\label{app:phase3_claims_table}",
            1,
        )
        claims_path.write_text(claims_text, encoding="utf-8")
        print("[A_claims_table] Inserted \\label{app:phase3_claims_table}.")
    else:
        print("[WARN] A_claims_table: could not find section header to label.")

# --- Label patch: C_offset_sweep_table.tex ---
offs_text = offs_path.read_text(encoding="utf-8")
if "\\label{app:offset_sweep_table}" in offs_text:
    print("[C_offset_sweep_table] Label already present.")
else:
    needle = r"\section{Offset sweep table}"
    if needle in offs_text:
        offs_text = offs_text.replace(
            needle,
            needle + "\n\\label{app:offset_sweep_table}",
            1,
        )
        offs_path.write_text(offs_text, encoding="utf-8")
        print("[C_offset_sweep_table] Inserted \\label{app:offset_sweep_table}.")
    else:
        print("[WARN] C_offset_sweep_table: could not find section header to label.")

# --- Label patch: D_theta_filter.tex ---
theta_text = theta_path.read_text(encoding="utf-8")
if "\\label{sec:theta_filter_artifact}" in theta_text:
    print("[D_theta_filter] Label already present.")
else:
    needle = r"\section{Phase 3 $\theta$-filter artifact (Phase 0 ledger interface)}"
    if needle in theta_text:
        theta_text = theta_text.replace(
            needle,
            needle + "\n\\label{sec:theta_filter_artifact}",
            1,
        )
        theta_path.write_text(theta_text, encoding="utf-8")
        print("[D_theta_filter] Inserted \\label{sec:theta_filter_artifact}.")
    else:
        print("[WARN] D_theta_filter: could not find section header to label.")

# --- Rewrite 05_limitations.tex as Discussion+Limitations ---

lim_tex = r"""\section{Discussion and Limitations}
\label{sec:limitations}

\subsection{Summary of the Phase 3 outcome}

Phase~3 is designed as an exploratory, ledger-compatible calibration step: it
uses external flavor-sector information (CKM and PMNS CP-phase data) to extract
a one-parameter fit for \(\theta\), exports the resulting interval as a
ledger-facing \(\theta\)-filter artifact, and then probes the Phase~2
vacuum-residue mechanism at and around that interval.

In the baseline configuration documented here, the Phase~3 fit pipeline
(Section~\ref{sec:fit_pipeline}) produces a best-fit value
\(\hat{\theta}\) and an associated uncertainty interval derived from a
one-parameter scan under a fixed ansatz and frozen target snapshot. This
interval is encoded in the artifact
\path{phase3/outputs/theta_filter/phase_03_theta_filter.json}, which conforms
to the Phase~0 corridor interface and underpins claim C3.1.

When this artifact is injected into the Phase~0 corridor ledger alongside the
Phase~0--2 filters, the resulting combined corridor is empty: no \(\theta\)
survives the simultaneous application of all filters. This is the central
negative result of the present Phase~3 run. By construction, we interpret this
as evidence against the locked Phase~3 ansatz/target combination (and, to a
lesser extent, against the present alignment between Phases~2 and~3), not as a
global falsification of the Origin-Axiom hypothesis.

\subsection{Dependence on external flavor data}

The Phase~3 extraction is conditional on a frozen snapshot of external flavor
data:

\begin{itemize}
  \item The targets and their uncertainties are encoded in
        \path{phase3/fit/targets.yaml}, with provenance ties to
        contemporary global fits (PDG, NuFIT, etc.).
  \item The present paper treats this snapshot as immutable for the purposes of
        the reported run; any update to the external data requires a new Phase~3
        run with a new bundle and potentially a different outcome.
  \item Correlation structures, hierarchy assumptions, and other simplifications
        are explicitly documented in the configuration and should be revisited
        as global flavor analyses evolve.
\end{itemize}

In particular, the existence and location of \(\hat{\theta}\) and its interval
are sensitive to target updates. One of the explicit failure conditions in
Section~\ref{sec:falsifiability} is a ``target drift collapse,'' in which
future data remove or significantly displace the minimum relative to the
Phase~1/2 corridor. Users of the Phase~3 filter must therefore treat the
present corridor intersection (or its absence) as provisional, tied to this
one external snapshot.

\subsection{Ansatz fragility and model incompleteness}

The ansatz used in Phase~3 is intentionally modest: it is a one-parameter
family that maps \(\theta\) into a handful of CP-sensitive flavor observables,
with a small discrete set of offset hypotheses. This serves the goal of
defining a clean, reproducible test bed, but it also imposes strong
limitations:

\begin{itemize}
  \item The ansatz is not a realistic model of the CKM/PMNS matrices and does
        not attempt to reproduce the full structure of modern flavor fits.
  \item The discrete offset family is very restricted; we presently select
        \(b_{\text{PMNS}} = \pi\) as the baseline because it minimizes the
        fit objective among the candidates listed in
        Appendix~\ref{app:offset_sweep_table}, but a richer ansatz space could
        easily produce different minima.
  \item Small, controlled modifications within the declared ansatz class may
        destroy the stability of the minimum or significantly change the
        extracted interval. This fragility is explicitly listed as a
        falsifiability condition in Section~\ref{sec:falsifiability}.
\end{itemize}

For these reasons, the negative corridor result should not be over-interpreted:
it says that one particular slice through flavor-parameter space, under a very
specific ansatz, is difficult to reconcile with the present Phase~1/2 corridor.
It does not rule out other ansatz choices, other ways of embedding flavor
information, or revisions to the Phase~2 mechanism itself.

\subsection{Corridor-level interpretation}

The Phase~0 corridor ledger provides a technical framework for combining
\(\theta\)-filters across phases. Within this framework, the Phase~3 result
plays three roles:

\begin{itemize}
  \item It supplies a filter that is structurally comparable to the Phase~1 and
        Phase~2 filters, enabling a clean intersection test.
  \item It provides an explicit example of a configuration in which the
        combined corridor becomes empty, illustrating that the ledger can record
        negative results as first-class outcomes.
  \item It anchors the procedural falsifiability claim (C3.3): an empty
        corridor under the locked ansatz/target combination is treated as
        evidence against that configuration, and any future Phase~3-like
        attempt must state in advance how such outcomes will be interpreted.
\end{itemize}

From a programmatic point of view, the empty corridor is useful even if it is
disappointing: it identifies a concrete mismatch between one tractable
flavor-encoding and the current residue-based corridor. That mismatch can then
be targeted by future work.

\subsection{Outlook}

The present Phase~3 run is not intended to be the final word on flavor-sector
integration. Instead, it establishes a reproducible template for how such
attempts should be structured and recorded:

\begin{itemize}
  \item \textbf{Upgrading the ansatz.} Future iterations can enlarge the
        ansatz family, add more realistic parameterizations, or explore
        different ways of coupling \(\theta\) into the CKM/PMNS structures.
        Each such change should be documented in an updated
        \path{ANSATZ_CONTRACT.md} and produce a new, clearly labelled
        Phase~3 bundle.
  \item \textbf{Updating external data.} As global flavor fits evolve,
        new snapshots can be encoded in \path{targets.yaml} and used to
        rerun the Phase~3 pipeline. Comparison across snapshots may reveal
        trends in how the Phase~3 corridor constraint moves relative to
        Phase~1/2.
  \item \textbf{Refining downstream diagnostics.} The present injection into
        Phase~2 uses a single diagnostic curve
        \(\Delta\rho_{\mathrm{vac}}(\theta)\). Future work may add more
        refined diagnostics, or connect the injected \(\theta\) region to
        Phase~2 observables in different ways.
  \item \textbf{Exploring Phase~4 and beyond.} If the Origin-Axiom program
        develops additional phases (for example, more direct observational
        tests), the Phase~3 template provides a blueprint for how to expose
        their filters to the corridor ledger and how to declare their claims
        and non-claims.
\end{itemize}

In short, the Phase~3 paper should be read as an explicit, negative but
constructive experiment: it shows how one plausible attempt to connect a
flavor-calibrated \(\theta\) to the existing corridor fails, and it records
enough detail that the attempt can be repeated, modified, or superseded in a
controlled way.
"""

lim_path.write_text(lim_tex.lstrip(), encoding="utf-8")
print("[05_limitations.tex] Rewritten as Discussion and Limitations section.")

# --- Progress log entry ---
if log_path.exists():
    log_text = log_path.read_text(encoding="utf-8")
else:
    log_text = "# Phase 3 Progress Log\n"

entry_header = "## 2026-01-06 - Rung 10: Discussion/limitations + appendix labels"
if entry_header in log_text:
    print("[PROGRESS_LOG] Rung 10 entry already present; no changes made.")
else:
    entry = f"""\n\n{entry_header}

- Added explicit LaTeX labels for the Phase 3 claims table
  (`app:phase3_claims_table`), offset sweep table (`app:offset_sweep_table`),
  and theta-filter appendix (`sec:theta_filter_artifact`) so that cross-references
  from the Methods and Results sections remain stable.
- Rewrote `phase3/paper/sections/05_limitations.tex` as a structured Discussion
  and Limitations section, summarizing the negative corridor outcome, clarifying
  dependence on external flavor data and ansatz choices, and providing an outlook
  for future Phase 3 iterations and potential Phase 4+ extensions.
- Kept claim IDs (C3.1–C3.3), numerical artifacts, and the Phase 3 gate workflow
  unchanged; this rung improves scientific narrative and cross-reference hygiene
  without altering computations.
"""
    log_path.write_text(log_text + entry, encoding="utf-8")
    print("[PROGRESS_LOG] Appended Rung 10 entry.")

print("Rung 10 patcher completed.")
