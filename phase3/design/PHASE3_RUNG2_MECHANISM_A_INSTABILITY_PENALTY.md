# Phase 3 – Rung 2
## Mechanism Family A: Instability-Penalised Toy Configurations

**Document role.** This note specifies a *candidate* Phase 3 Rung-2
mechanism family built on top of the Rung-1 toy ensemble and the
diagnostics introduced in `measure_v1` and `instability_penalty_v1`.
It is a *design document*, not a binding claim: it defines what we
would implement and measure, and what such a mechanism would and would
not mean.

This document is intended to sit *under* the broader roadmap in
`PHASE3_NEXT_RUNG.md` as the first concrete mechanism family to be
explored.

---

## 0. Rung position and dependencies

- **Upstream requirements**
  - Phase 0: corridor + claims ledger (conceptual backbone).
  - Phase 1: locked θ-space mapping playground.
  - Phase 2: locked FRW corridor machinery.
  - Phase 3 Rung 1:
    - Toy mechanism \(z_k(\theta)\), \(A_0(\theta)\), and floor
      \(A(\theta) = \max(A_0(\theta), \varepsilon)\).
    - Baseline binding experiment and binding fraction.
    - Diagnostics:
      - `measure_v1.py` → histogram and quantiles of \(A_0\).
      - `instability_penalty_v1.py` → scalar instability penalty
        aggregating how much time the ensemble spends near deep
        cancellation.

- **Rung 2 scope**
  - Work entirely within the toy ensemble family (same \(z_k(\theta)\)
    structure or controlled variations of it).
  - Use diagnostics to define and explore *candidate structural
    mechanisms* for maintaining a non-zero floor.
  - Make no physical identification with the real vacuum and no claim
    that nature actually optimises the chosen objective.

---

## 1. Intuition and goals

Rung 1 shows that, for the present toy ensemble,

- deep cancellation (very small \(A_0\)) occupies a limited fraction of
  the grid; and
- imposing an explicit floor \(A(\theta) = \max(A_0(\theta), \varepsilon)\)
  produces a non-trivial binding regime.

However, Rung 1 treats \(\varepsilon\) as an *external choice*. Rung 2
aims to explore toy mechanisms where something like a floor is
encouraged or stabilised by an **internal constraint** on the toy
configuration, e.g. “do not spend *too much* time in extremely deep
cancellation,” subject to other structural requirements.

**Goal for Mechanism Family A.**

Define a class of toy configurations and an associated objective
functional
\[
  \mathcal{J}[\text{config}] = 
    \mathcal{P}_{\text{inst}}[\text{config}; \{\varepsilon_i\}]
    + \text{(constraint terms)},
\]
such that:

- \(\mathcal{P}_{\text{inst}}\) is built directly from the existing
  diagnostics (fractions of grid points with \(A_0 < \varepsilon_i\));
- minimising \(\mathcal{J}\) favours configurations that *avoid*
  spending excessive measure near \(A_0 \approx 0\), but do **not**
  collapse to a trivial “always-large \(A_0\)” regime; and
- we can explore this family numerically without making any physical
  claim beyond: “here is a structurally consistent way to favour
  non-cancellation in the current toy space.”

---

## 2. Baseline objects and notation

We keep the Rung-1 ensemble structure:

- Modes:
  \[
    z_k(\theta) = \exp\bigl(i(\alpha_k + \sigma_k \theta)\bigr),
  \]
  with:
  - \(k = 1,\dots,N\);
  - \(\alpha_k \in [0,2\pi)\) fixed phase offsets;
  - \(\sigma_k\) drawn from a small set of winding numbers
    \(\{1,2,3,4\}\) in the baseline configuration.

- Global amplitude:
  \[
    A_0(\theta) = \left| \frac{1}{N} \sum_{k=1}^N z_k(\theta) \right|
  \]
  sampled over a fixed grid \(\theta_j\).

- Rung-1 diagnostics:
  - \(A_0\) samples stored in `mech_baseline_scan.csv`.
  - Quantiles and fractions below thresholds \(\varepsilon_i\) stored
    in `phase3_measure_v1_stats.json`.
  - Aggregate instability penalty
    `total_penalty` in `phase3_instability_penalty_v1.json`.

At Rung 2 we *reuse* these definitions; we do not change the meaning
of \(A_0\) or the baseline diagnosis of how often it approaches deep
cancellation.

---

## 3. Mechanism Family A: Instability-penalised ensembles

### 3.1. Abstract definition

We consider a space of toy configurations \(\mathcal{C}\), each
configuration `config` specifying a finite set of modes with parameters
\(\{\alpha_k, \sigma_k\}_{k=1}^N\) and any additional discrete
structure we choose to introduce (e.g. sector labels or weights).

For each configuration:

1. We define \(A_0(\theta)\) exactly as in Rung 1.
2. We run a *measure probe* analogous to `measure_v1` to obtain:
   - the empirical CDF of \(A_0\);
   - fractions \(f_i(\text{config}) = \Pr[A_0 < \varepsilon_i]\) over a
     small, fixed set of \(\varepsilon_i\) values.

3. We define an **instability penalty**
   \[
     \mathcal{P}_{\text{inst}}[\text{config}] =
       \sum_i w_i \, g\!\bigl(f_i(\text{config})\bigr),
   \]
   where:
   - \(\varepsilon_i\) and weights \(w_i\) are fixed hyperparameters;
   - \(g\) is a convex, increasing function (e.g. quadratic) that
     heavily penalises large fractions of the grid in deep cancellation
     basins.

4. We optionally include *soft constraints* to avoid trivialising the
   ensemble, e.g. terms penalising:
   - vanishing variance of \(A_0(\theta)\);
   - excessively large mean amplitude (to avoid “always-large” regimes).

The full objective for a configuration is then:
\[
  \mathcal{J}[\text{config}] =
    \mathcal{P}_{\text{inst}}[\text{config}] +
    \lambda_{\text{var}} \, \mathcal{C}_{\text{var}}[\text{config}] +
    \lambda_{\text{mean}} \, \mathcal{C}_{\text{mean}}[\text{config}],
\]
with \(\lambda_{\text{var}}\) and \(\lambda_{\text{mean}}\) fixed as
part of the toy design.

### 3.2. Intended exploration (non-binding)

Within this family we **do not** claim that nature performs any such
optimisation. Instead, Rung 2 uses \(\mathcal{J}\) to:

- compare the *baseline* Rung-1 configuration to nearby configurations
  in \(\mathcal{C}\);
- explore whether there exist configurations that:
  - maintain non-trivial variation in \(A_0(\theta)\);
  - preserve some binding fraction behaviour; yet
  - significantly reduce the instability penalty \(\mathcal{P}_{\text{inst}}\).

The outcomes would be purely toy-model statements, e.g.:

> “In this restricted ensemble, there exist configurations that
>  reduce the time spent in deep cancellation while retaining
>  non-trivial amplitude structure.”

Any such statement would be logged as a **non-binding toy claim** in
the Phase-3 claims table until a much stronger conceptual or physical
motivation is established.

---

## 4. Proposed code artefacts (non-implemented at this rung)

This Rung-2 family is intended to produce *new* scripts and outputs, in
addition to the existing Rung-1 diagnostics. Tentative names:

- **Configuration generator / explorer**
  - `phase3/src/phase3_mech/mechA_generate_configs_v1.py`
  - Responsibilities:
    - define a parameterisation of configurations in \(\mathcal{C}\)
      (e.g. distributions over \(\alpha_k\), \(\sigma_k\), optional
      sector labels);
    - generate a small library of candidate configs (baseline + simple
      variations);
    - write them to a JSON or YAML registry under
      `phase3/inputs/mechA_configs_v1/`.

- **Objective evaluator**
  - `phase3/src/phase3_mech/mechA_evaluate_v1.py`
  - Responsibilities:
    - for each config in the registry:
      - compute the \(A_0(\theta)\) curve;
      - reuse the `measure_v1` machinery (or a refactored helper) to
        compute \(f_i(\text{config})\) and the derived penalty;
      - compute constraint terms (variance, mean) and assemble
        \(\mathcal{J}[\text{config}]\);
    - write a per-configuration diagnostics table:
      `phase3/outputs/tables/mechA_rung2_diagnostics.csv` and a JSON
      summary.

- **Optional visualisation**
  - `phase3/src/phase3_mech/mechA_plot_profiles_v1.py`
  - Responsibilities:
    - plot a small subset of \(A_0(\theta)\) profiles and penalties for
      representative configs, to be referenced (non-binding) in later
      paper rungs.

At this stage, no code is yet implemented; this document serves as the
spec that future scripts must adhere to.

---

## 5. Claim boundaries

At Phase 3 Rung 2, Mechanism Family A is strictly **exploratory**.

### 5.1. Possible future *toy* claims (if supported by artefacts)

If and only if the above scripts and diagnostics are implemented and
checked, examples of *toy-level*, non-binding claims might include:

- **M3.A-toy-1 (non-binding).**  
  Within the Rung-1 toy ensemble class, there exist configurations
  that reduce the instability penalty \(\mathcal{P}_{\text{inst}}\)
  relative to the baseline while preserving non-trivial variation in
  \(A_0(\theta)\).

- **M3.A-toy-2 (non-binding).**  
  For certain hyperparameter choices \((\varepsilon_i, w_i,
  \lambda_{\text{var}}, \lambda_{\text{mean}})\), the distribution of
  \(A_0(\theta)\) in low-penalty configurations exhibits a “soft
  floor” in the sense that very small amplitudes occur less frequently
  than in the baseline ensemble.

These would be explicitly logged as **toy-mechanism diagnostics** and
kept separate from any physical or cosmological claims.

### 5.2. Explicit non-claims

Mechanism Family A, even if fully implemented, **does not** claim:

- that the real vacuum is described by this ensemble;
- that nature extremises \(\mathcal{J}\) or any similar functional;
- that any emergent “soft floor” scale corresponds to the cosmological
  constant or any other observed quantity;
- that this mechanism is unique, preferred, or stable under changes in
  the toy ensemble definition.

Any step toward those directions would require a higher rung with
substantially stronger conceptual and empirical backing.

---

## 6. Interfaces to other phases

- **To Phase 0.**  
  If a later rung converts any Mechanism-A output into a corridor or
  filter on \(\theta\), that filter must be:
  - encoded as a *non-binding* Phase-0 corridor at first; and
  - clearly marked as derived from a toy-mechanism family.

- **To Phase 4.**  
  Optionally, one can feed Mechanism-A configurations (or their
  derived amplitude curves) into the Phase-4 mapping family F1 and its
  FRW diagnostics. This would remain a *diagnostic cross-check*:
  - “What do FRW-like probes see if we move within Mechanism-A’s toy
    configuration space?”

No Phase-4 claim becomes binding without independent justification.

---

## 7. Next actions (for future work)

This document is intentionally one rung *ahead* of current
implementation. The next concrete actions, when we decide to take
them, would be:

1. **Refactor shared diagnostics.**  
   Factor out the `A_0` histogram / quantile logic from `measure_v1`
   into a small reusable helper so Mechanism-A scripts can call it.

2. **Implement minimal config registry.**  
   Define a very small, explicit registry of configurations in
   `phase3/inputs/mechA_configs_v1/` including:
   - the current baseline;
   - a few hand-tuned variants probing more / less cancellation.

3. **Implement `mechA_evaluate_v1.py`.**  
   Compute \(\mathcal{P}_{\text{inst}}\) and constraint terms for each
   config and write a diagnostics table.

4. **Decide whether any toy-level statements are worth logging.**  
   Only after we have clear artefacts and figures should we consider
   adding non-binding toy claims to the Phase-3 claims table.

Until these are done, Mechanism Family A remains a **design sketch**
with no scientific weight beyond defining a clear, reproducible target
for future work.


---

Doc status: Rung-level Phase 3 design note documenting the mechanism-A instability-penalty refinement; historical and explanatory; it guides interpretation of specific Phase 3 runs but is not a standalone claims register.
