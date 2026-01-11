# Phase 4 hard-novelty roadmap (F1 + FRW)

_Status note (2026-01-11)._ This document is a **Phase 4 design / planning
note**, kept for context and roadmap purposes. It is **draft and
non-binding** and does not override or extend the Phase 4 scope or claims.

For the current Phase 4 contract, see:

- `phase4/SCOPE.md` for the Phase 4 scope definition,
- `phase4/CLAIMS.md` and `phase4/NON_CLAIMS.md` for claims and guardrails,
- `phase4/REPRODUCIBILITY.md` for reproducibility, and
- `phase4/design/FRW_TOY_DESIGN.md`, `phase4/design/FRW_DATA_DESIGN.md`, and
  `phase4/design/FRW_SYNTHESIS.md` for detailed FRW-facing design.

Any future promotion of ideas from this document into Phase 4/5 text or
figures must pass through the FRW promotion gate
`docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md` and the Phase 4 promotion design
in `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md`, and be reflected in
the Phase 4 scope/claims documents.


This note sketches concrete directions for turning the current Phase 4
infrastructure into harder scientific novelty, while staying honest about what
is and is not yet demonstrated. It is meant as a design document, not as a
claims vehicle.

## 1. Where we stand

As of the current baseline:

- Phase 3 delivers a mechanism and a diagnostic scalar
  \(E_{\mathrm{vac}}(\theta)\) with documented behaviour on a fixed grid.
- Phase 4 builds an F1 mapping on top of that scalar and exposes it to:
  - shape diagnostics and toy corridors;
  - FRW toy sanity checks on \(H^2(a; \theta)\);
  - FRW viability scans (matter era, late acceleration, broad age window);
  - FRW viability corridors in \(\theta\);
  - a \(\Lambda\)CDM-like probe (age/\(\Omega_\Lambda\) box cuts);
  - overlaps between F1-shape corridors and FRW-facing corridors;
  - a scaffold for data-facing FRW probes.

The **novelty so far** is structural and infrastructural:
- a fully logged, reproducible pipeline from the Phase 3 scalar to FRW-based
  viability and corridor structure; and
- explicit quantification of how much of the \(\theta\)-grid survives each
  successive diagnostic.

It is **not yet** hard-physics novelty in the sense of:
- fitting real data,
- deriving new constraints, or
- proving that the mapping does something that conventional models cannot.

The roadmap below outlines how Phase 4 (and successors) could move in that
direction.

## 2. Direction I — From box cuts to simple likelihoods

Current status:
- FRW viability and \(\Lambda\)CDM-like probes use box-shaped cuts in age and
  \(\Omega_\Lambda\), under hand-fixed \((\Omega_m, \Omega_r, H_0)\).
- `phase4/src/phase4/run_f1_frw_data_probe.py` provides a hook to compare FRW
  histories against a binned distance–redshift dataset at
  `phase4/data/external/frw_distance_binned.csv`, but the repository does not
  ship any such file; the baseline logs `data_available = false`.

Natural next step:
1. Choose a simple, public distance–redshift dataset (e.g. SNe Ia or BAO) and
   export a *binned*, *lightweight* version into
   `phase4/data/external/frw_distance_binned.csv` (or a similar, documented
   path) with columns such as
   \[
     z_i,\ D_L^{\mathrm{obs}}(z_i),\ \sigma_i.
   \]

2. Extend or complement `run_f1_frw_data_probe.py` with a minimal FRW
   calculator for:
   - \(H(z; \theta)\),
   - the comoving distance,
   - the luminosity distance \(D_L(z; \theta)\)
   for each \(\theta\) on the grid.

3. Define a simple \(\chi^2\)-like statistic
   \[
     \chi^2(\theta) = \sum_i
       \frac{\bigl(D_L^{\mathrm{model}}(z_i; \theta) -
                   D_L^{\mathrm{obs}}(z_i)\bigr)^2}{\sigma_i^2},
   \]
   and record per-\(\theta\) \(\chi^2\) and an associated “data-OK” mask
   using a transparent threshold on \(\chi^2/\mathrm{dof}\).

4. Treat the result as a **diagnostic overlay** on top of the FRW-viable
   corridor:
   - What fraction of FRW-viable points are also data-OK?
   - Does the data-OK set lie in a compact \(\theta\)-interval or fragment
     into islands?

Claim discipline:
- At first, this should be framed as “compatibility checks” with a chosen
  dataset, *not* as a competitive cosmological fit.
- All thresholds and approximations must be spelled out in the code and
  documented in Phase 4 notes.

## 3. Direction II — Hyperparameter scans in FRW space

Current status:
- FRW layers fix \(\Omega_m = 0.3\), \(\Omega_r = 0\), and \(H_0 =
  70\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) by hand.
- All reported fractions (FRW-viable, \(\Lambda\)CDM-like, overlaps) are tied
  to this single background choice.

Natural next step:
1. Introduce a compact grid of background parameters, e.g.
   \[
     \Omega_m \in [0.25, 0.35],\quad
     H_0 \in [65, 75]\,\mathrm{km\,s^{-1}\,Mpc^{-1}},
   \]
   with a small number of sampling points.

2. For each point in this hyperparameter grid:
   - re-run the FRW viability scan;
   - re-run the \(\Lambda\)CDM-like probe (with appropriately updated target
     windows if needed);
   - record the resulting fractions and \(\theta\)-intervals.

3. Build a small, structured summary (JSON + tables) of how:
   - the FRW-viable fraction,
   - the \(\Lambda\)CDM-like fraction,
   - and key overlap fractions
   move when \((\Omega_m, H_0)\) are varied inside observationally reasonable
   ranges.

Questions this can answer:
- Are FRW-viable corridors robust under modest changes in background
  parameters, or do they appear only for finely tuned values?
- Do \(\Lambda\)CDM-like subsets disappear, split, or remain contiguous under
  such scans?

Claim discipline:
- All of these would still be framed as **structural robustness tests** of the
  mapping, not as hard constraints on \(\Omega_m\) or \(H_0\).

## 4. Direction III — Making the axiom link explicit

Current status:
- The FRW layers are built on top of the F1 scalar and Phase 3 diagnostics,
  but the paper only loosely gestures at how this ties back to the origin
  axiom and Phase 1–2 conceptual work.

Natural next step:
1. Trace explicitly which properties of \(E_{\mathrm{vac}}(\theta)\) that
   enter the FRW-facing pipeline are:
   - inherited from the axiom and Phase 1–3 construction, e.g. specific
     non-cancellation or quantile behaviour; versus
   - introduced ad hoc in Phase 4, e.g. choices of normalisation,
     scaling, or thresholds.

2. Identify **invariants** of the F1 mapping that are robust under changes in
   resolution and minor implementation details (e.g. conserved ordering,
   persistent features in the shape of \(E_{\mathrm{vac}}(\theta)\)) and ask
   whether any FRW-facing statement can be phrased purely in terms of such
   invariants.

3. Use this analysis to separate:
   - claims that would still hold for any mapping with the same structural
     properties (and thus are not specific to the axiom); from
   - claims that are genuinely rooted in the origin-axiom machinery.

Outcome:
- A clearer map of where “axiom-driven” structure ends and where “Phase 4
  engineering” begins, which is essential for a future, harder-novelty
  paper.

## 5. Direction IV — Phase 4 freeze vs extensions

Given the current state, a pragmatic strategy is:

1. **Phase 4 freeze (minimal):**
   - Declare the existing F1 + FRW infrastructure, together with its
     diagnostics and limitations, as the completed scope of Phase 4.
   - Keep new, more aggressive physics work in separate modules and design
     notes, marked as “Phase 4+” or “Phase 5”.

2. **Phase 4 extensions (optional, carefully scoped):**
   - If a simple FRW data check or a small hyperparameter scan yields a
     result that is both interesting and robust, consider adding it as a new
     rung with very tightly worded claims.
   - Otherwise, treat Phase 4 as a *staging ground* for future phases
     specialising in cosmology, data, or field theory.

This roadmap is deliberately conservative: it focuses first on structural and
robustness questions that are natural given the existing machinery, and only
then on potential data contacts. It should be updated as new rungs are added
or as the scope of Phase 4 is formally frozen.

---

Doc status: Phase 4 hard-novelty roadmap design note; outlines potential FRW-facing novelty paths but is not a binding roadmap or claims source; subject to the same promotion design and gating as other Phase 4 design docs.
