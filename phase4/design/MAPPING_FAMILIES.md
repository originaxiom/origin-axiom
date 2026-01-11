# Phase 4 mapping families (design note, draft)

Status: DRAFT (non-binding)
Scope: Internal design for how Phase 4 will connect the Phase 3
       global-amplitude mechanism to FRW-like / vacuum-energy-like
       observables.

This note does not define any binding claims. It specifies candidate
families of mappings that Phase 4 may implement and test. Only once a
mapping is actually implemented, documented in the paper, and wired
through a gate will it be eligible to support a binding claim.

## 1. Inputs and outputs

**Inputs (from Phase 3 mechanism):**

- A floor-enforced global amplitude
  \( A(\theta) = \max\{ A_0(\theta), \varepsilon \} \) defined on
  a grid \( \theta \in [0, 2\pi) \).
- Diagnostics from the Phase 3 binding regime, including
  \( \varepsilon \), quantiles of \( A_0(\theta) \), and summary
  statistics for the shift between \( A_0 \) and \( A \).

For Phase 4 we treat these as a canonical toy vacuum observable and
associated metadata. We do **not** modify the Phase 3 mechanism in
this phase; we only define mappings downstream of \( A(\theta) \).

**Outputs (Phase 4-level):**

- One or more FRW-like or vacuum-energy-like observables as functions
  of \( \theta \) and possibly a small number of mapping parameters.
- Optional derived \(\theta\)-filters that can be ingested by the
  Phase 0 ledger if they meet corridor-style criteria (non-empty,
  non-pathological).

## 2. Design principles for mappings

Phase 4 mappings should:

1. Be **explicit and low-dimensional**:
   - Prefer 1–3 free parameters per mapping family.
   - Avoid highly flexible functional forms that can fit anything.

2. Be **normalisation-aware**:
   - Clarify how dimensionless amplitudes \( A(\theta) \) are turned
     into quantities with cosmological units, if at all.
   - Separate "shape" information in \( \theta \) from overall scale.

3. Be **corridor-compatible**:
   - Produce \(\theta\)-dependent quantities in a form that can
     support corridor definitions (e.g. inequality bands, stability
     windows, or qualitative behaviour conditions).

4. Be **honest about physical status**:
   - These are toy mappings, not claimed derivations from first
     principles.
   - The paper must clearly separate "mathematically convenient" from
     "physically motivated".

## 3. Candidate mapping families (draft)

The families below are **candidates**, not yet implemented.

### F1: Amplitude-to-density rescaling

Treat the floor-enforced amplitude \( A(\theta) \) as a dimensionless
proxy for a vacuum-energy-like density:

\[
  \rho_{\mathrm{vac}}(\theta; \kappa, p)
  \;=\; \kappa \, [A(\theta)]^p,
\]

with:

- \( \kappa > 0 \): overall scale (not claimed to match observed
  \( \rho_\Lambda \));
- \( p > 0 \): shape exponent (e.g. \( p = 1 \) or \( p = 2 \)).

**Design intent:**

- Use \( p \) to test how sensitive FRW-like behaviour is to the
  "sharpness" of the map between amplitude and effective density.
- Use \( \kappa \) only as a scale knob, not as a physically claimed
  fit parameter.

### F2: Residue-relative mapping

Use the *difference* between the floor-enforced and unconstrained
amplitudes as a proxy for a vacuum "residue":

\[
  \Delta A(\theta) \;=\; A(\theta) - A_0(\theta),
\]

\[
  \rho_{\mathrm{res}}(\theta; \kappa_{\mathrm{res}})
  \;=\; \kappa_{\mathrm{res}} \, \Delta A(\theta).
\]

**Design intent:**

- Focus on regions where the non-cancellation floor is active
  (binding regime).
- Ask whether the "extra" amplitude enforced by the floor can be
  interpreted as a vacuum-energy-like contribution without producing
  pathological FRW trajectories.

### F3: Normalised amplitude corridor

Define a normalised amplitude,

\[
  \tilde{A}(\theta) \;=\;
  \frac{A(\theta) - A_{\min}}{A_{\max} - A_{\min}},
\]

using Phase 3 diagnostics \( A_{\min}, A_{\max} \). Then define
simple corridor-style conditions such as:

- "Acceptable" \(\theta\) values satisfy
  \( \tilde{A}(\theta) \in [\alpha_{\min}, \alpha_{\max}] \)
  for some fixed bounds \( 0 \le \alpha_{\min} < \alpha_{\max} \le 1 \).
- These inequalities can then be combined with FRW-like diagnostics
  (e.g. stability, sign of acceleration) to define a Phase 4
  \(\theta\)-filter.

**Design intent:**

- Keep the mapping dimensionless and avoid premature physical
  normalisation.
- Provide a simple way to define corridors without pretending to have
  a full cosmological fit.

## 4. Strategy for implementation and testing

Planned implementation sequence:

1. Implement F1 with very simple parameter choices:
   - e.g. \( p = 1 \), a small discrete set of \( \kappa \) values.
   - Couple \( \rho_{\mathrm{vac}}(\theta) \) to a toy FRW module.

2. Define minimal diagnostics:
   - stability of trajectories;
   - monotonicity or boundedness of scale-factor evolution;
   - qualitative behaviour of \(\theta\)-dependence.

3. If F1 yields only pathological or empty corridors, test F2 and F3,
   documenting the failure modes as structured negative results.

4. Only if a mapping produces a non-empty, non-trivial corridor do we
   consider defining a Phase 4 \(\theta\)-filter artifact.

## 5. Non-claims

This note does **not** claim:

- A derivation of cosmological parameters from the Origin Axiom.
- A unique or physically preferred mapping from \( A(\theta) \) to
  FRW observables.
- That any specific mapping family will succeed.

It is a design document to keep Phase 4 constrained, auditable, and
aligned with the Phase 0 corridor and ledger semantics.


---

Doc status: Phase 4 mapping families design note (draft); defines candidate mapping families over FRW scalars and masks; descriptive and non-binding; any promotion into Phase 4/5 claims or figures must pass the FRW promotion gate.
