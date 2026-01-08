# Origin–Axiom Phase 3 – Next-Rung Design

## 1. Status recap (Phase 3 and Phase 4 as they stand)

### Phase 3 (toy non-cancellation mechanism)

- Defines a finite ensemble of complex modes
  \(z_k(\theta) = \exp[i(\alpha_k + \sigma_k \theta)]\) with fixed
  phases \(\alpha_k\) and integer windings \(\sigma_k\).
- Global amplitude observable:
  \[
    A_0(\theta) =
    \left|\frac{1}{N}\sum_{k=1}^{N} z_k(\theta)\right|.
  \]
- Non-cancellation floor enforced by
  \(A(\theta) = \max(A_0(\theta), \varepsilon)\) with \(\varepsilon\)
  chosen as a low quantile (e.g. 25th percentile) of the baseline
  amplitude distribution across the \(\theta\)-grid.
- Baseline run demonstrates a genuine binding regime:
  - the floor is active on a non-trivial fraction of the grid
    \(0 < f_{\mathrm{bind}} < 1\);
  - the floor produces a measurable global effect (mean shift, L\(^2\)
    distance) between \(A_0\) and \(A\).
- All of this is implemented and reproducible via explicit scripts
  under `phase3/src/` and a binding-profile figure under
  `phase3/outputs/figures/`.

**Deliberate limitations at this rung**

- The toy vacuum has no spatial structure, no dynamics in time, and
  no relation to a Hamiltonian or Lagrangian.
- The floor scale \(\varepsilon\) is picked by a distributional rule
  (a quantile of \(A_0\)), not derived from deeper principles.
- Phase 3 does not yet produce a binding \(\theta\)-filter artifact
  for the Phase 0 ledger.

### Phase 4 (FRW-facing diagnostic stack on top of Phase 3)

- Introduces a structural mapping family F1,
  \(E_{\mathrm{vac}}(\theta) = \alpha\, A(\theta)^\beta\), with
  baseline \((\alpha,\beta) = (1,4)\), treated explicitly as a toy
  choice rather than a physical law.
- Builds a layered FRW-inspired diagnostic stack:
  - F1 sanity curve and shape diagnostics;
  - FRW toy sanity check;
  - FRW viability scan (age window, matter era, late-time acceleration);
  - extraction of contiguous \(\theta\)-corridors;
  - broad \(\Lambda\)CDM-like probe around
    \((\Omega_\Lambda, t_0) \sim (0.7, 13.8\,\mathrm{Gyr})\);
  - joint shape/FRW probes;
  - an explicit data-probe stub that records a structured negative
    result if no external data are present.
- All Phase 4 scripts live under `phase4/src/phase4/` and write
  JSON/CSV diagnostics into `phase4/outputs/tables/`.

**Deliberate limitations at this rung**

- F1 is explicitly arbitrary and toy-level: it is not calibrated to
  any physical scale.
- The FRW layer is a consistency/sanity check; it does not attempt a
  data-driven cosmology fit.
- No binding \(\theta\)-filter is produced; all FRW-facing probes are
  non-binding diagnostics.

---

## 2. Core scientific debt: origin and status of the floor

The central Phase 3 question that remains open is:

> Why should a non-cancellation floor \(|A| \ge \varepsilon > 0\) exist at all?

At the current rung we have shown that:

- a floor *can be implemented* in a toy ensemble;
- the floor can be non-trivial (genuine binding regime);
- the floor can be handled in a numerically robust and reproducible way.

We have **not** shown that:

- the floor follows from any deeper principle (topological, dynamical,
  information-theoretic, etc.);
- the scale or structure of \(\varepsilon\) is related to any physical
  observable;
- the floor is uniquely or even naturally realised by the chosen toy
  ensemble.

This is the main “scientific debt” carried into the next rung of
Phase 3 and into any future Phase 5.

---

## 3. Design goals for Phase 3 – Next Rung

The next rung of Phase 3 should move from “demonstrating that a floor
can be imposed” towards “proposing candidate reasons why a floor
might arise”.  The goals are:

1. **Mechanism enrichment.** Introduce at least one concrete mechanism
   candidate where the non-cancellation floor is tied to a structural
   feature (e.g. topology, instability, or consistency condition),
   rather than being purely imposed by hand.

2. **Structured comparison.** Preserve the existing simple ensemble as
   a baseline, and treat richer mechanisms as side-by-side candidates
   that can be compared via the same diagnostic language.

3. **Explicit failure / negative results.** If a mechanism family
   fails (e.g. collapses back towards perfect cancellation, or
   produces pathological behaviour), this should be recorded as an
   explicit negative result rather than silently abandoned.

4. **Interface stability.** Any new mechanism candidate should still
   present a clean \(\theta \mapsto A(\theta)\) interface so that
   Phase 4 and later FRW-facing layers can be reused without major
   surgery.

The next rung is not required to “solve cosmology” or to match any
observed scale.  Its role is to propose and explore plausible
\emph{structural} paths from axiom to mechanism.

---

## 4. Candidate mechanism directions (non-binding menu)

The following directions are candidates for subsequent Phase 3
experiments.  They are listed as a menu rather than a commitment.

### 4.1 Topological / geometric obstructions

Idea: interpret the amplitude zero set \(A_0(\theta) = 0\) as a locus
that is difficult or impossible to cross, because doing so would
require passing through a singular or ill-defined configuration.

Sketch options:

- Construct ensembles where \(A_0(\theta)\) can be written as a
  product of factors whose individual zeros correspond to distinct
  “defects”, and explore whether certain paths in \(\theta\)-space
  are effectively excluded.
- Introduce a penalty functional that increases sharply as
  \(A_0(\theta) \to 0\), and interpret the floor as the effective
  outcome of avoiding those regions.

At this rung, such constructions would remain toy-level but can be
used to assess whether “topological obstruction to perfect
cancellation” is a viable story to pursue.

### 4.2 Consistency / instability-based floors

Idea: require that configurations with \(|A_0|\) below some threshold
are dynamically unstable, inconsistent, or fail to satisfy a
self-consistency condition, so that the effective dynamics of the
ensemble never realise \(|A| \approx 0\).

Sketch options:

- Couple the ensemble to an auxiliary “consistency monitor” that
  fails (e.g. diverges or becomes undefined) when \(|A_0|\) drops
  below a threshold, thereby excluding those trajectories.
- Explore discrete dynamics on the mode phases or windings where
  transitions across the \(|A_0| = 0\) region are disallowed or
  always redirected.

Here, the floor is less a parameter and more a derived “zone of
avoidance” in configuration space.

### 4.3 Measure / selection effects

Idea: argue that the set of configurations with \(|A_0| < \varepsilon\)
has very small measure compared to those with \(|A_0| \gtrsim
\varepsilon\), so that typical configurations sampled from a natural
measure almost never realise very small amplitudes.

Sketch options:

- Analyse the distribution of \(A_0(\theta)\) for large ensembles of
  modes and investigate whether the probability weight near zero is
  sharply suppressed for certain structural choices of \(\sigma_k\)
  and \(\alpha_k\).
- Treat \(\varepsilon\) as an emergent scale associated with, e.g.,
  a concentration-of-measure phenomenon in high-dimensional phase
  space.

This direction would lean more heavily on analytic or numerical
statistics than on dynamics.

---

## 5. Concrete next steps – experiment stubs

Rather than committing to a single story prematurely, the next rung
can introduce a small number of concrete experiment families, each
with its own source directory and outputs:

- `phase3/src/phase3_mech/topology_*` – toy constructions that
  explore obstruction-like behaviour for the amplitude zero set.

- `phase3/src/phase3_mech/consistency_*` – dynamics where attempts to
  drive \(|A_0| \to 0\) trigger instability or inconsistency flags.

- `phase3/src/phase3_mech/measure_*` – statistical studies of the
  amplitude distribution across large ensembles and parameter
  families.

Each experiment family should:

1. Produce a well-defined \(\theta \mapsto A(\theta)\) (or multiple
   candidates) so that Phase 4 can, in principle, be reused.
2. Emit JSON/CSV diagnostics summarising:
   - the fraction of the grid in which the floor is active;
   - basic distributional properties of \(A_0\) and \(A\);
   - any structural indicators of the mechanism (e.g. instability
     flags or topological indices, if defined).
3. Be wired into a clear claims table entry, with explicit binding
   status (most likely non-binding at first).

Negative results (e.g. “this mechanism collapses to trivial
behaviour”) are considered valuable and should be logged as such.

---

## 6. Phase 5 – provisional interface

While Phase 5 is not yet implemented, the design of the next Phase 3
rung should anticipate plausible Phase 5 roles, such as:

- taking one or more mechanism candidates that survive Phase 3
  scrutiny and exploring how they might be embedded into richer
  structures (e.g. multiple sectors, hierarchies of scales, or links
  to field-theoretic or cosmology-facing models);
- deepening the connection between any candidate floor mechanism and
  the FRW-facing diagnostics of Phase 4, possibly adding new mapping
  families beyond F1;
- beginning to explore whether any mechanism candidates can naturally
  produce hierarchies or scales that are at least qualitatively
  reminiscent of observed vacuum-energy scales, without overclaiming.

At this point, Phase 5 should be treated as a **placeholder for
future structure**, not as a binding commitment.  The priority is to
ensure that the next Phase 3 rung is documented and structured well
enough that a future Phase 5 has a clear, well-defined set of inputs
and questions to work with.

