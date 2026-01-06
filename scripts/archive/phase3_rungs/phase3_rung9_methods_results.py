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

# --- Targets ---
fit_path = root / "phase3/paper/sections/02_fit_pipeline.tex"
inj_path = root / "phase3/paper/sections/03_injection_pipeline.tex"

for p in (fit_path, inj_path):
    if not p.exists():
        print(f"ERROR: {p} not found.")
        sys.exit(1)

# --- Backup originals ---
backup(fit_path)
backup(inj_path)

# --- New 02_fit_pipeline.tex (Methods) ---

fit_tex = r"""\section{Methods: Flavor-sector fit pipeline}
\label{sec:fit_pipeline}

\subsection{Overview}

Phase~3 treats the flavor sector as an external calibration source for the
Origin-Axiom program. Under a fixed, explicitly stated ansatz, and for a frozen
snapshot of CKM and PMNS CP-phase targets, we scan a one-parameter family
\(\theta \in [0,2\pi)\) and extract a best-fit value \(\hat{\theta}\) together
with an uncertainty interval. The output of this pipeline is a schema-stable
\(\theta\)-filter JSON artifact that can be consumed by the Phase~0 corridor
ledger alongside the existing Phase~1 and Phase~2 filters.

This section describes the input targets, the ansatz, the scan and objective,
and the diagnostics that support the Phase~3 fit claim (C3.1).

\subsection{External flavor targets}

We treat the CKM and PMNS sectors as external data. A snapshot of the
relevant CP-sensitive parameters (phases and, where needed, mixing angles) is
encoded in a configuration file
\path{phase3/fit/targets.yaml}. This snapshot is intended to reflect
contemporary global fits (e.g. PDG and NuFIT) at the time of this Phase~3 run;
the precise numerical values and their provenance are recorded in the YAML and
in the paper bundle metadata.

In the present baseline configuration, we:

\begin{itemize}
  \item freeze a set of CKM and PMNS targets at their quoted central values and
        uncertainties;
  \item record all such targets, their assumed uncertainties, and any
        correlations or simplifying assumptions directly in
        \path{phase3/fit/targets.yaml};
  \item treat this snapshot as immutable for the purposes of the Phase~3 run
        documented here, so that future reruns with updated global fits can be
        compared against this fixed baseline.
\end{itemize}

\subsection{One-parameter ansatz and offset hypotheses}

The Phase~3 ansatz is deliberately modest: we posit a one-parameter family of
maps from a single angle \(\theta\) to the CP-sensitive flavor observables. The
intent is not to propose a realistic theory of the CKM or PMNS matrices, but to
define a simple, reproducible test bed that can be integrated into the Phase~0
corridor machinery.

Concretely:

\begin{itemize}
  \item A fixed ansatz family is chosen and registered in
        \path{phase3/fit/ANSATZ_CONTRACT.md}. This contract documents which
        flavor observables are included, how \(\theta\) enters the mapping, and
        which discrete choices (such as offsets) are allowed.
  \item Within this family, we consider a small set of discrete ``offset
        hypotheses'' for the PMNS sector (e.g. different constant shifts
        applied to a CP phase). These hypotheses are enumerated and compared
        via an offset sweep.
  \item For each offset hypothesis, the ansatz defines a predicted set of
        flavor observables as a function of \(\theta\).
\end{itemize}

The discrete model comparison step is summarized in
\path{phase3/outputs/tables/theta_offset_sweep.csv}, with an accompanying
metadata file
\path{phase3/outputs/tables/theta_offset_sweep.meta.json}. The LaTeX
table in Appendix~\ref{app:offset_sweep_table} provides a human-readable view.

In the baseline run documented here, the offset hypothesis labelled
``\(b_{\text{PMNS}} = \pi\)'' minimizes the fit objective among the discrete
candidates and is therefore locked in as the Phase~3 baseline ansatz for the
rest of this paper.

\subsection{Grid scan and fit objective}

For a fixed offset hypothesis, we evaluate the fit quality on a grid of
\(\theta\) values over \([0,2\pi)\). The grid is chosen to be dense enough that
the location and width of the minimum can be resolved to the precision reported
in the tables; the exact grid definition, including step size and domain, is
recorded in the metadata file
\path{phase3/outputs/tables/theta_fit_summary.meta.json}.

The fit quality is measured by a standard quadratic objective,
schematically
\begin{equation}
  \chi^2(\theta)
  \;=\;
  \sum_i
  \left(
    \frac{O_i^{\text{model}}(\theta) - O_i^{\text{target}}}{\sigma_i}
  \right)^2,
\end{equation}
where \(O_i^{\text{model}}(\theta)\) are the ansatz predictions,
\(O_i^{\text{target}}\) are the frozen external targets, and \(\sigma_i\) are
the assumed uncertainties. Correlations, if any, are treated according to the
documented assumptions in \path{phase3/fit/targets.yaml}; no attempt is made
here to reproduce the full machinery of global flavor fits.

For each grid point \(\theta_k\), we evaluate \(\chi^2(\theta_k)\) and record:

\begin{itemize}
  \item the value of \(\theta_k\);
  \item the corresponding \(\chi^2(\theta_k)\);
  \item any auxiliary diagnostics (such as contributions from different
        flavor sectors).
\end{itemize}

The resulting summary is written to
\path{phase3/outputs/tables/theta_fit_summary.csv}, with additional diagnostic
information in \path{phase3/outputs/tables/theta_fit_diagnostics.json}.

\subsection{Best-fit value and uncertainty interval}

From the grid of \(\chi^2(\theta_k)\) values we identify a best-fit point
\(\hat{\theta}\) corresponding to the minimum of the objective, and construct an
uncertainty interval around \(\hat{\theta}\). The present implementation uses a
simple profile-based criterion (e.g. a \(\Delta\chi^2\) threshold suitable for a
single-parameter scan) to define a contiguous interval of \(\theta\) values
around the minimum.

The resulting quantities are:

\begin{itemize}
  \item \(\hat{\theta}\): the best-fit value within the scanned domain;
  \item \([\theta_{\min}, \theta_{\max}]\): an interval of admissible values
        determined by the profile criterion;
  \item derived diagnostics (e.g. goodness-of-fit measures, local curvature)
        recorded in \path{theta_fit_diagnostics.json}.
\end{itemize}

These values are summarized in the canonical table
\path{phase3/outputs/tables/theta_fit_summary.csv}. Figure~\ref{fig:theta_fit}
(\path{phase3/outputs/figures/fig1_theta_fit_diagnostics.pdf}) provides a
visual overview of the objective landscape and the selected interval.

\subsection{Offset sweep model comparison}

To choose the baseline offset hypothesis, we repeat the grid scan for each
candidate offset and compare their minimum \(\chi^2\) values. The sweep is
summarized in \path{theta_offset_sweep.csv} and tabulated in
Appendix~\ref{app:offset_sweep_table}. The selection rule is deliberately
simple:

\begin{itemize}
  \item we select the offset hypothesis with the smallest minimum \(\chi^2\),
        subject to sanity checks on the shape of the profile;
  \item we record the selected hypothesis and its identifier in
        \path{phase3/fit/ANSATZ_CONTRACT.md} and in the metadata of
        \path{theta_fit_summary.meta.json}.
\end{itemize}

The present paper reports only results for the selected baseline hypothesis
(\(b_{\text{PMNS}} = \pi\)). Alternative hypotheses remain in the sweep table
for transparency and for potential future comparison.

\subsection{Exporting the \texorpdfstring{\(\theta\)}{theta}-filter artifact}

Finally, we convert the best-fit interval into a corridor-style
\(\theta\)-filter artifact that is compatible with the Phase~0 ledger
interface. The artifact is written to
\path{phase3/outputs/theta_filter/phase_03_theta_filter.json} and conforms
to the schema defined in the Phase~0 contracts:

\begin{itemize}
  \item it declares a domain \([0,2\pi)\);
  \item it encodes the admissible region as a union of intervals and as a
        grid+pass-mask representation;
  \item it includes provenance fields (e.g. configuration hashes) sufficient
        to tie the artifact back to a specific fit run.
\end{itemize}

This artifact underpins the Phase~3 fit claim (C3.1) and is the only object
seen by the Phase~0 corridor ledger; the internal ansatz machinery remains
encapsulated within the Phase~3 implementation.
"""

fit_path.write_text(fit_tex.lstrip(), encoding="utf-8")
print("[02_fit_pipeline.tex] Rewritten as structured Methods section.")

# --- New 03_injection_pipeline.tex (Results / Diagnostics) ---

inj_tex = r"""\section{Results: Injection into Phase 2 vacuum residue}
\label{sec:injection}

\subsection{Motivation and scope}

Phase~2 implements a vacuum-residue mechanism in a cosmology-inspired setting.
Phase~3 does not attempt to alter that mechanism; instead, it treats Phase~2 as
a downstream diagnostic: we inject the fitted \(\theta\) (and, where useful, a
neighbourhood of values) into the Phase~2 machinery and observe how the vacuum
residue responds.

The goal of this section is narrow:

\begin{itemize}
  \item to define a diagnostic curve \(\Delta\rho_{\mathrm{vac}}(\theta)\)
        derived from Phase~2;
  \item to show how the Phase~3 fit interval sits on this curve;
  \item to record the outcome in a way that the Phase~0 ledger can later
        combine with other filters.
\end{itemize}

No new cosmological claims are made here; the Phase~2 approximations and
limitations continue to be governed by the Phase~2 contracts.

\subsection{Injection hook into Phase 2}

At the implementation level, the injection proceeds by routing a set of
\(\theta\) values through the same numerical pipeline that Phase~2 uses for its
own scans, with the following constraints:

\begin{itemize}
  \item we treat Phase~2 as a black box that accepts \(\theta\) as a control
        parameter and returns a vacuum-residue diagnostic;
  \item we do not modify the Phase~2 equations, approximations, or
        configuration beyond supplying \(\theta\);
  \item we log the configuration and commit hashes so that the exact
        injection context is reproducible.
\end{itemize}

In practice, we evaluate the diagnostic on a grid of \(\theta\) values that
covers at least the Phase~3 fit interval \([\theta_{\min}, \theta_{\max}]\) and
extends beyond it for context. The grid definition and numerical settings are
recorded in the metadata associated with the diagnostic outputs.

\subsection{Definition of the diagnostic curve}

We define \(\Delta\rho_{\mathrm{vac}}(\theta)\) as a difference between a
Phase~2 vacuum-residue quantity evaluated at \(\theta\) and an appropriate
baseline. Schematically,
\begin{equation}
  \Delta\rho_{\mathrm{vac}}(\theta)
  \;=\;
  \rho_{\mathrm{vac}}(\theta) - \rho_{\mathrm{vac}}^{\text{baseline}},
\end{equation}
where \(\rho_{\mathrm{vac}}(\theta)\) is the residue-like quantity produced
by the Phase~2 machinery, and
\(\rho_{\mathrm{vac}}^{\text{baseline}}\) is a reference level (for example,
the value at a distinguished point in the corridor, or another conventional
choice documented in the Phase~2 contracts).

The precise definition of the baseline is recorded alongside the numerical
results so that future reruns can adopt compatible choices or deliberately
change them.

The evaluated curve is stored as a table
\path{phase3/outputs/tables/theta_delta_rho_vac_table.*} (CSV and metadata)
and visualized in Figure~\ref{fig:delta_rho_vac_theta}
(\path{phase3/outputs/figures/fig2_delta_rho_vac_vs_theta.pdf} with an
accompanying metadata file
\path{phase3/outputs/figures/fig2_delta_rho_vac_vs_theta.meta.json}).

\subsection{Position of the Phase 3 fit interval}

On top of the diagnostic curve we highlight the Phase~3 fit interval
\([\theta_{\min}, \theta_{\max}]\) obtained in
Section~\ref{sec:fit_pipeline}. The figure is constructed so that:

\begin{itemize}
  \item the best-fit value \(\hat{\theta}\) is visually distinguished
        (e.g. by a marker);
  \item the interval \([\theta_{\min}, \theta_{\max}]\) is indicated as a
        band along the \(\theta\)-axis;
  \item the overall shape of \(\Delta\rho_{\mathrm{vac}}(\theta)\), including
        any local features, can be inspected at a glance.
\end{itemize}

This overlay is a diagnostic only: it shows how the flavor-calibrated \(\theta\)
region interacts with the Phase~2 vacuum-residue mechanism under the current
approximations. It is not used directly as a corridor filter; that role is
reserved for the explicit \(\theta\)-filter artifact described in
Section~\ref{sec:fit_pipeline} and Appendix~\ref{sec:theta_filter_artifact}.

\subsection{Interpretation and limitations}

The injection results support the Phase~3 injection claim (C3.2) in the
following limited sense:

\begin{itemize}
  \item given a \(\theta\) extracted from the flavor-sector fit, the
        Phase~2 machinery can be evaluated at that \(\theta\) to produce a
        reproducible \(\Delta\rho_{\mathrm{vac}}(\theta)\) curve;
  \item the numerical implementation and its outputs are tied to specific
        configuration and commit hashes, so that the mapping can be re-run
        and audited;
  \item the resulting curve is incorporated into the Phase~3 paper bundle as
        a first-class artifact (tables and figure).
\end{itemize}

We do \emph{not} claim that:

\begin{itemize}
  \item the present \(\Delta\rho_{\mathrm{vac}}(\theta)\) curve captures all
        physically relevant effects;
  \item the observed pattern is robust to changes in the Phase~2
        approximations or external cosmological inputs;
  \item any specific cosmological observable is explained or predicted by
        the combination of Phase~2 and Phase~3.
\end{itemize}

Instead, the injection should be read as a structured, reproducible
\emph{experiment}: it records how one particular flavor-calibrated \(\theta\)
region interacts with one particular implementation of the vacuum-residue
mechanism. Future phases may revisit both ingredients.
"""

inj_path.write_text(inj_tex.lstrip(), encoding="utf-8")
print("[03_injection_pipeline.tex] Rewritten as structured Results/Diagnostics section.")

# --- Progress log entry ---

log_path = root / "phase3/PROGRESS_LOG.md"
if log_path.exists():
    log_text = log_path.read_text(encoding="utf-8")
else:
    log_text = "# Phase 3 Progress Log\n"

entry_header = "## 2026-01-06 - Rung 9: Phase 3 methods + injection results rewrite"
if entry_header in log_text:
    print("[PROGRESS_LOG] Rung 9 entry already present; no changes made.")
else:
    entry = f"""\n\n{entry_header}

- Rewrote `phase3/paper/sections/02_fit_pipeline.tex` as a structured Methods
  section for the flavor-sector fit, covering external targets, ansatz and
  offset hypotheses, grid scan and objective, uncertainty interval, offset
  sweep, and export of the ledger-facing `phase_03_theta_filter.json` artifact.
- Rewrote `phase3/paper/sections/03_injection_pipeline.tex` as a structured
  Results/Diagnostics section for the injection of the fitted \\(\\theta\\) into
  the Phase 2 vacuum-residue mechanism, including a clear definition of the
  diagnostic curve \\(\\Delta\\rho_{{\\mathrm{{vac}}}}(\\theta)\\) and the role
  of the Phase 3 fit interval.
- Kept claim IDs (C3.1–C3.3), numerical artifacts, and gate workflow unchanged;
  this rung tightens the scientific narrative without altering the underlying
  computations.
"""
    log_path.write_text(log_text + entry, encoding="utf-8")
    print("[PROGRESS_LOG] Appended Rung 9 entry.")

print("Rung 9 patcher completed.")
