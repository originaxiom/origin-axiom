# Forbidden cancellation program (v1)

## 1. Position in the stack

This document sits on top of the locked Stage I phases (0–5), the Stage 2 diagnostic belts, and the obstruction-program memos. Its only job is to spell out what it would mean, in this concrete stack, for a non-cancelling floor to be "forbidden" or "forced" in a way that can be tested and, in principle, falsified.

The statements here are programmatic. They do not change any Phase 0–5 contracts, claims, or non-claims, and they do not promote any Stage 2 object to a phase-level claim. Any promotion would require its own Phase 0 style gate.

## 2. Working ingredients

The forbidden-cancellation program uses the following objects as inputs:

- A one-parameter theta grid, currently a uniform 2048-point grid covering a fixed angle interval.
- A pre-data FRW kernel, built from the Phase 4 viability mask and always-true sanity checks, which currently keeps about half the grid.
- A family of FRW-derived flags on that grid, including:
  - viability, LCDM-like, and toy FRW corridor flags,
  - external-style age corridors,
  - external-style late-time expansion corridors,
  - simple structure proxies built from age and expansion.
- A family of mechanism amplitudes from Phase 3, currently:
  - mech_baseline_A0, mech_baseline_A_floor, mech_baseline_bound,
  - mech_binding_A0, mech_binding_A, mech_binding_bound,
  attached to the FRW kernel via the joint theta grid.
- A small “sweet subset” inside the kernel where several internal and external-style corridors meet (for example the 40-point subset where kernel, LCDM-like, toy corridor, and an external-style age cut all overlap in the current snapshot).
- A reference point theta_star, defined independently of the FRW kernel and corridors, which can be checked for membership in these sets but is not tuned to them.

The obstruction tests you have already implemented are all of the form: start from the kernel, apply one or more internal or external-style corridors, and inspect the surviving fraction and its behaviour in FRW and mechanism space.

## 3. Candidate notions of “forbidden cancellation”

In this stack “forbidden cancellation” is not a single sentence. It is a family of candidate statements about how small the mechanism amplitudes are allowed to be, and how that interacts with FRW viability and external corridors.

Below are three working notions, ordered from weakest to strongest.

### 3.1. Non-vanishing floor on a sweet subset (weak program)

There exists a non-trivial subset S of the theta grid such that:

- S lives inside the pre-data FRW kernel and passes a small number of external-style corridors (for example age and a simple structure proxy).
- On S, all admissible mechanism amplitudes are bounded away from zero by a floor epsilon, in a sense that survives minor variations of the corridors.
- Outside S, the amplitudes are allowed to be small or to cancel, but S itself never collapses under admissible corridor refinements.

In the current snapshot, the 40-point sweet subset is the natural candidate for S: it is small, lives inside the kernel, passes several toy and external-style corridors, and can be tracked in both FRW space and mechanism space.

The weak program asks whether a non-trivial S of this kind can survive under a sharpening ladder of corridors without the mechanism amplitudes on S dropping to arbitrarily small values.

### 3.2. Robust floor on a corridor family (intermediate program)

There exists a corridor family C, built from a small number of internal and external-style filters, such that:

- C contains a non-trivial fraction of the kernel (not just a small sweet subset).
- The mechanism amplitudes on C are bounded away from zero by a floor epsilon that is stable under:
  - moderate changes in the corridor thresholds,
  - extensions of the kernel to nearby FRW snapshots,
  - and mild reparametrisations of the mechanism module.

Here the program is to see whether the static FRW kernel, together with age, expansion, and structure proxies, can support a corridor C that is both:
- non-empty and non-trivial in size, and
- equipped with a mechanism floor that looks stable rather than accidental.

In the current snapshot your tests show that the mechanism amplitudes on the kernel and on the 40-point sweet subset are smooth and non-zero, but you have not yet identified a corridor family C with a demonstrably stable floor.

### 3.3. Global obstruction to exact cancellation (strong program)

The strongest notion would be a statement of the form:

> On any FRW-viable theta grid of this kind, satisfying a given list of external-style corridors and structural sanity checks, there is no way to choose mechanism amplitudes consistent with the Phase 3 module that make the vacuum sector cancel exactly. A non-zero floor is forced by the structure itself.

This is a true obstruction statement: it would show that, once the FRW and mechanism structures are fixed and a small set of external corridors is imposed, the dynamics simply cannot realise an exact cancellation. Any such statement would require:

- a clear mathematical space of admissible mechanism modules and FRW kernels,
- a precise definition of exact cancellation in that space,
- and a proof or rigorous numerical obstruction argument that excludes it.

The current stack is not yet in a position to make such a strong claim; the strong program is recorded here as a long-term goal.

## 4. Near-term targets with the current stack

With the current Stage 2 and obstruction program you can realistically aim for:

- A documented static kernel and sweet subset, with:
  - counts and fractions under multiple external-style corridors,
  - summaries of mechanism amplitudes on the kernel and on the sweet subset.
- A structured sequence of external-style corridors (age, expansion, structure proxies) that:
  - are explicitly recorded and stable under small threshold changes,
  - are not tuned to the sweet subset by construction,
  - and carve the kernel in transparent ways.
- A verdict that says, in this toy setting:
  - whether the sweet subset S survives under this sharpening ladder,
  - whether the mechanism amplitudes on S stay well away from zero,
  - and whether any near-cancellation patterns appear to be accidental or structural.

This belongs to the weak and intermediate programs above. It is already being built under the obstruction-program branch; this document is the place where the programmatic targets are spelled out.

## 5. How this feeds future phases and hosts

In the longer run, a forbidden-cancellation program will need to be tested across multiple hosts and kernels, not just the current Stage I FRW toy. That is the role of Stage II and the host design memos.

From the point of view of this document:

- Stage I and Stage 2 provide a single, fully auditable testbed.
- The obstruction program defines concrete kernels, corridors, and sweet subsets and measures how they behave in FRW and mechanism space.
- The forbidden-cancellation program defines what would count as:
  - a weak positive signal (a small sweet subset with a robust floor),
  - a stronger signal (a corridor family with a floor),
  - or a genuine obstruction (in the strong sense).
- Stage II and beyond are where similar tests would be repeated on multiple hosts, with more realistic kernels and external corridors, to see whether any of these signals persist in a way that is not an artefact of the first toy stack.

## 6. Non-claims

This document does not assert that forbidden cancellation is realised in the current snapshot. It records target statements that the project may eventually be able to support or rule out.

In particular:

- No specific value of theta or theta_star is claimed to be preferred by the current kernels or corridors.
- No mechanism amplitude is promoted to a canonical measure over theta.
- No global obstruction theorem is claimed; the strong program is aspirational.

Any future claim that a particular corridor carries a genuine non-cancellation floor, or that exact cancellation is obstructed in a precise sense, will be made only after separate design rungs, numerical and conceptual checks, and explicit Phase 0 style gates.
