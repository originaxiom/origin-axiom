# Stage 2 – Frustrated Floor Toy Model (Design v1)

Status: **design note / diagnostic model**. This document specifies a toy model of a “frustrated floor” built purely on top of existing Stage 2 outputs. It does **not** change any Phase 0–5 contracts, FRW masks, or promotion gates and must not be treated as a claims document.

---

## 1. Objective

Define a concrete, reproducible toy model of a “frustrated floor” that:

- uses only existing Stage 2 tables and masks,
- is expressible as algebraic conditions on the θ-grid,
- can be probed numerically with the current obstruction helpers, and
- makes a clear distinction between what is *assumed* (model hypotheses) and what is *measured* (counts, fractions, amplitude ranges).

The model is deliberately modest: it does not attempt to derive the floor from first principles or to explain the observed cosmological constant. It is a structured way of saying “here is what a non-trivial non-cancellation floor would look like in the current snapshot, and here is how we would check whether such a picture is even compatible with the existing kernel and corridors.”

---

## 2. Ingredients

We work on the existing one-dimensional θ-grid with:

- Background and FRW structure from Phase 4:
  - vacuum parameters: \(E_{\mathrm{vac}}(\theta)\), \(\Omega_\Lambda(\theta)\), age \(t_{\mathrm{age}}(\theta)\),
  - FRW masks and corridors (viability, LCDM-like band, shape and data probes),
- Stage 2 obstruction helpers:
  - pre-data kernel flag: \(\mathrm{KERNEL}(\theta) \in \{0,1\}\),
  - toy FRW corridor flag: \(\mathrm{TOY\_CORRIDOR}(\theta) \in \{0,1\}\),
  - external-style corridors:
    - age band v2: \(\mathrm{AGE\_EXT\_V2}(\theta) \in \{0,1\}\),
    - late-time expansion corridor v1: \(\mathrm{LT\_EXT\_V1}(\theta) \in \{0,1\}\),
    - age/expansion/structure proxy bands v1 (broad/tight),
- Mechanism amplitudes from Phase 3:
  - baseline amplitudes: \(\mathrm{A}^{\mathrm{base}}_0(\theta)\), \(\mathrm{A}^{\mathrm{base}}_{\mathrm{floor}}(\theta)\), \(\mathrm{A}^{\mathrm{base}}_{\mathrm{bound}}(\theta)\),
  - binding amplitudes: \(\mathrm{A}^{\mathrm{bind}}_0(\theta)\), \(\mathrm{A}^{\mathrm{bind}}(\theta)\), \(\mathrm{A}^{\mathrm{bind}}_{\mathrm{bound}}(\theta)\).

These quantities already live in:

- `stage2/obstruction_tests/outputs/tables/stage2_obstruction_kernel_with_mech_v1.csv`,
- the various external-corridor tables and summaries documented in the obstruction stack.

---

## 3. Model hypotheses

The toy model introduces three explicit hypotheses, labelled for future reference.

**H1 (background kernel as pre-selection).**  
The pre-data FRW kernel is treated as the minimal background viability filter:

\[
\mathrm{KERNEL}(\theta) = 1
\]

means that θ has a qualitatively acceptable FRW background (matter era, late-time acceleration, smooth H²) before any host-like considerations.

**H2 (external-style host corridors).**  
External-style corridors approximate the requirement that a θ-point can host a universe with broadly acceptable late-time age, expansion, and structure conditions. A minimal “host corridor” can be defined as:

\[
\mathrm{HOST\_EXT}(\theta) = 1 \iff \mathrm{AGE\_EXT\_V2}(\theta) = 1 \ \wedge \ \mathrm{EXP\_TIGHT\_V1}(\theta) = 1 \ \wedge \ \mathrm{STRUCT\_TIGHT\_V1}(\theta) = 1
\]

where the concrete flags correspond to:

- age band compatible with a late-time universe of order 14 Gyr,
- expansion and structure proxies within a narrow band.

This is a model choice, not a claim about real host viability.

**H3 (mechanism amplitude as non-cancellation proxy).**  
One of the Phase 3 binding amplitudes is treated as a proxy for “non-cancellation strength”:

\[
F_{\mathrm{nc}}(\theta) := \mathrm{A}^{\mathrm{bind}}_0(\theta)
\]

and a **toy floor level** \(F_{\mathrm{floor}}\) is introduced as a scalar threshold such that:

\[
\mathrm{FLOOR}(\theta) = 1 \iff F_{\mathrm{nc}}(\theta) \ge F_{\mathrm{floor}}
\]

The choice of \(F_{\mathrm{nc}}\) and \(F_{\mathrm{floor}}\) is part of the toy model and will be tied to the empirical distributions already summarised in `stage2_obstruction_non_cancel_floor_vs_corridors_v1.csv`. At design time, \(F_{\mathrm{floor}}\) is chosen so that:

- a substantial fraction of the kernel satisfies the floor (so the condition is non-vacuous),
- but the floor is still non-trivial (it excludes a controlled subset of kernel points).

In the current snapshot a natural choice is in the range where the KERNEL+FLOOR subset remains well populated (for example the 0.045 threshold explored in the existing helper), but nothing in this model fixes the value uniquely.

---

## 4. Definition of the frustrated-floor toy band

Given H1–H3, we define three nested sets on the θ-grid:

1. **Background kernel**  
   \[
   \mathcal{K} = \{\theta \mid \mathrm{KERNEL}(\theta) = 1\}
   \]

2. **Host-compatible band**  
   \[
   \mathcal{H} = \{\theta \in \mathcal{K} \mid \mathrm{HOST\_EXT}(\theta) = 1\}
   \]

3. **Frustrated-floor band**  
   \[
   \mathcal{F} = \{\theta \in \mathcal{H} \mid \mathrm{FLOOR}(\theta) = 1\}
   \]

In words:

- \(\mathcal{K}\) collects points with acceptable internal FRW behaviour.
- \(\mathcal{H}\) adds a minimal host-style external corridor.
- \(\mathcal{F}\) imposes a non-trivial lower bound on the mechanism amplitude.

The **toy frustrated-floor statement** is then:

> “In the current snapshot, we can realise a non-empty subset \(\mathcal{F}\) of θ that simultaneously satisfies background FRW viability, simple host-like external corridors, and a non-trivial non-cancellation floor on the mechanism amplitude.”

The obstruction helpers already compute the sizes and amplitude ranges of several related families, such as:

- KERNEL + external age v2,
- KERNEL + tight age/expansion/structure proxies,
- KERNEL + sweet-like subsets under external corridors,
- KERNEL + non-cancellation floor.

The purpose of this model is to align these diagnostics into one coherent set definition and to track \(|\mathcal{F}|\) and the behaviour of \(F_{\mathrm{nc}}(\theta)\) within it.

---

## 5. What is being **measured** versus assumed

**Measured (from existing tables)**

From the current Stage 2 outputs we can directly read:

- the counts and fractions for:
  - ALL_GRID, PRE_DATA_KERNEL,
  - external-age and late-time corridors,
  - toy FRW corridor,
  - sweet-like subsets under external corridors,
  - non-cancellation floor families;
- the min, max, and mean values of the mechanism amplitudes in each such family;
- the status of particular θ-values (for example, previously distinguished θ candidates) with respect to all these flags.

These are objective properties of the current snapshot and do not depend on the frustrated-floor narrative.

**Assumed (toy-model structure)**

The toy model additionally assumes that:

- background viability should always be enforced first (H1),
- a simple conjunction of external-style corridors can stand in for “host viability” (H2),
- a single mechanism amplitude component is a reasonable proxy for “non-cancellation strength” (H3),
- and a single scalar floor \(F_{\mathrm{floor}}\) is sufficient to model the floor, rather than a more complicated functional.

These assumptions are precisely the places where future rungs can sharpen or replace the model as understanding improves.

---

## 6. Relation to the obstruction verdict

This model is **subordinate** to the Stage 2 obstruction verdict document:

- The verdict continues to be expressed in terms of:
  - FRW masks and corridors,
  - external-style tests,
  - and mechanism diagnostics,
  - with explicit non-claims about floor existence.
- The frustrated-floor toy band \(\mathcal{F}\) is an **interpretive diagnostic** within that verdict:
  - it asks “how far can we push simultaneous host corridors and amplitude floors before the kernel empties or becomes extremely thin?”,
  - but it does not assert that any such configuration is physically realised.

Any future obstruction verdict statements that reference \(\mathcal{F}\) must:

- explicitly label the toy-model assumptions used,
- refer back to this design note,
- and clearly separate “what this snapshot shows” from “what we conjecture about fundamental dynamics”.

---

## 7. Future directions

To move from this toy model toward something closer to the original frustrated-floor vision, future rungs could:

1. **Sharpen the host corridors.**  
   Replace the current age and expansion proxies with corridors whose thresholds are motivated by explicit cosmological arguments, and track how \(|\mathcal{F}|\) responds.

2. **Refine the non-cancellation measure.**  
   Explore alternative definitions of \(F_{\mathrm{nc}}(\theta)\) (including combinations of amplitudes and penalties) and see whether the existence and thickness of \(\mathcal{F}\) is robust.

3. **Introduce dynamical structure.**  
   Add simple θ-evolution models (for example gradient flows in θ-space) and ask whether trajectories tend to enter and linger in \(\mathcal{F}\) rather than in arbitrary parts of the kernel.

4. **Connect to earlier θ-candidate work.**  
   Systematically compare previously studied θ-values to \(\mathcal{F}\) and related bands to see whether they behave in a qualitatively distinctive way.

Each such direction will require its own design and gate rungs. Until those exist, this document remains a **design-level specification** of how to talk about a frustrated floor honestly within the current Stage 2 snapshot.

