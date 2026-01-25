# Stage 2 dynamic-θ and floor status (v1, internal note)

**Status:** Internal interpretive note for the obstruction program and dynamic-θ / frustrated-floor explorations.  
**Branch:** `obstruction-program-v1`  
**Scope:** Stage 2 obstruction diagnostics and toy mechanisms only. No Phase 0–5 contracts, FRW masks, or promotion gates are altered by this document.

---

## 1. Purpose and scope

This note fixes the current status of:

- the **static FRW kernel + sweet subset** used in the obstruction program,
- the **θ\*** candidate and related dynamic-θ ideas,
- the **non-cancellation floor** as tested so far,
- the **ψ-floor toy ODEs** and their “with drive / without drive” variants,
- and how we treat external AI campaigns and off-repo calculations.

It is deliberately **interpretive** and **internal**. It does not:

- introduce new claims at Phase-paper level,
- change any Phase 0 governance rules,
- or promote any of the toy dynamics to a physical mechanism.

Future rungs (D2, D3, …) will have to reference this note explicitly when refining dynamic-θ work.

---

## 2. Trusted numerical backbone (what we stand on)

Within Stage 2 and the obstruction program, we treat the following as **trusted internal artefacts**, because they are:

- produced by scripts in the repo,
- run locally in a controlled environment, and
- recorded in the obstruction branch with clear provenance.

### 2.1 Static FRW kernel and sweet subset

From the existing Stage 2 and Phase 4 outputs:

- A 2048-point θ-grid underlies the scalar FRW toy.
- The **pre-data kernel** contains 1016 points which pass the Phase 4 FRW viability masks.
- A **40-point sweet subset** survives a combination of:
  - FRW viability,
  - LCDM-like scalar box,
  - toy FRW “shape” / corridor masks,
  - and simple external-style age / expansion proxies.

We treat the kernel and the 40-point sweet subset as:

- a **real numerical structure** the repo has actually built, and
- the primary testbed for any θ\*- or floor-related story.

They are not, yet, a physical claim. They are structured toy universes that happen to survive the current internal filters.

### 2.2 θ\* as a candidate, not a winner

The θ\* candidate (derived from φ^φ) has been checked against the obstruction stack:

- It lies **inside** the pre-data kernel.
- It is **not uniquely singled out** by the current corridors:
  - It behaves like a healthy, non-pathological point, one among a structured set.
  - The current toy external corridors and proxies do not elevate it to a unique optimum.

We therefore adopt the following stance:

- θ\* is allowed as a **distinguished candidate** for further exploration.
- It is **not** promoted to a preferred or “true” value by Stage I / Stage 2.
- Any future promotion would require:
  - sharper external corridors,
  - a dynamic mechanism that actually picks it out, and
  - explicit Phase 0–style gates.

### 2.3 Mechanism amplitudes and floor statistics

From the Stage 2 obstruction helpers which attach Phase 3 amplitudes to the kernel and build corridor families:

- The **pre-data kernel** supports a wide range of mechanism amplitudes.
- With a simple non-cancellation floor (e.g. a threshold on `mech_binding_A0`):
  - A large fraction of the kernel remains above the floor.
  - Restricting simultaneously to sweet-like, age-tuned, expansion- and structure-tuned families yields small but non-empty subsets.
- Summary tables (kernel vs external corridors, kernel vs non-cancellation floor) show:
  - the floor can be implemented **without killing** the kernel,
  - the sweet-like subset remains compatible with a modest floor.

We treat these as:

- **evidence of robustness** of the obstruction picture in the toy FRW + mechanism space,
- **not** as evidence that any particular amplitude or floor value is physically realised.

---

## 3. ψ-floor toy ODEs: what they actually showed

We introduced toy ODEs for a single complex ψ with a floor ε, in two basic versions:

1. **No-drive toy:** damping + floor only.  
2. **Driven toy:** damping + periodic drive + floor.

They are designed as **mechanism analogies**, not as candidate fundamental equations.

### 3.1 No-drive toy: “everything collapses to the floor”

Numerical behaviour:

- Initial amplitudes span some range above ε.
- Under pure damping with a hard floor, every trajectory:
  - eventually hits the floor,
  - spends most of the integration time glued to it,
  - and ends with `|ψ| ≈ ε`.

Interpretation:

- This model **does implement** a frustrated cancellation floor in a literal sense (no trajectory can fall below ε).
- But dynamically it is **too trivial**:
  - the late-time attractor is a static floor state,
  - there is no ongoing “stirring” or structure once transients die,
  - time evolution degenerates into simple exponential decay plus a hard clip.

We keep this as:

- a sanity-check that a floor can be made mathematically consistent,
- an example of what we **do not** want physically: a universe that just dies onto the floor.

### 3.2 Driven toy: floor plus external forcing

Numerical behaviour:

- With a periodic drive plus damping and a floor:
  - trajectories explore a band above the floor,
  - the floor is hit occasionally but is not the only attractor,
  - late-time amplitudes settle into a narrow band **above** ε.

Interpretation:

- The drive provides a **non-trivial steady state**:
  - the system neither cancels away nor collapses into a static floor,
  - the floor acts as a “hard core” while the drive keeps things alive.
- But conceptually:
  - the drive is **put in by hand**,
  - nothing in the model explains why the drive exists or how it relates to θ, FRW, or quantum fields.

We keep this as:

- a demonstration that “floor + ongoing dynamics” is easy to realise once you admit an external driver,
- a warning that we must **not** smuggle the whole mechanism into an unexplained forcing term.

### 3.3 Overall lesson from the ψ toys

What the ψ toys taught us:

- A floor **by itself** is dynamically too weak: without drive, everything collapses to ε.
- A floor **plus arbitrary drive** is dynamically rich but conceptually cheap: the physics hides in the drive.
- A credible mechanism must therefore:

  1. make the floor **structurally necessary** (topological, informational, or constraint-based), and  
  2. make the ongoing “drive” **emerge** from the same structure that defines θ and the vacuum, not from a hand-tuned forcing term.

The ψ toys are therefore recorded as:

- **useful diagnostics of what not to over-claim**, and
- an existence proof that a non-trivial frustrated floor is compatible with simple ODE dynamics.

They are **not** to be cited as physical evidence for the origin-axiom mechanism.

---

## 4. External AI campaigns and off-repo analyses

In addition to the repo-native code, there have been external AI analyses and campaigns (e.g. separate agents, remote notebooks, and batch rungs) that:

- re-analysed Planck corridors,
- explored dynamic θ variants,
- proposed alternative mechanisms or combinations,
- produced PDFs and zip bundles with extended calculations.

Policy for Stage I and obstruction:

- These are treated as **exploratory scratch work**, not as part of the Stage I record.
- They may inspire future rungs, but:
  - no claim or numerical result is accepted into the ladder until it is:
    - re-implemented as a script in this repo,
    - run locally with recorded commands,
    - and tied into Phase 0–style gates and non-claims.

Concretely:

- The obstruction program’s **trusted numerical spine** is the set of CSVs, scripts, and docs under:
  - `phase4/outputs/…`,
  - `stage2/obstruction_tests/…`,
  - `stage2/obstruction_toy_models/…`,
  - and the obstruction docs under `docs/` and `stage2/docs/`.
- External AI artefacts (zips, PDFs, off-repo notebooks) are **not binding** unless and until they are imported into the repo through explicit rungs.

---

## 5. Where this leaves the non-cancellation principle

Given the current evidence, we adopt the following **honest internal position**:

1. The **obstruction picture** (reality as a near-cancelling system forbidden from reaching exact zero) is:
   - conceptually coherent,
   - compatible with the toy FRW kernel and sweet subset,
   - and survives non-trivial internal corridors and simple external-style age / expansion filters.

2. The **non-cancellation floor** is:
   - clearly implementable in the toy mechanisms,
   - compatible with preserving structured subsets of the kernel,
   - but not yet derived from any deeper principle (topological, holographic, or informational).

3. The **dynamic-θ / ψ mechanisms**:
   - have demonstrated that a frustrated floor can be modelled in simple ODEs,
   - have not yet produced a mechanism that:
     - is structurally self-contained,
     - couples cleanly to FRW and the Stage 2 kernel,
     - and yields a non-trivial, testable prediction.

4. The **θ\*** candidate:
   - remains an interesting target,
   - is neither selected nor ruled out by the current obstruction stack,
   - and must earn any special status through future, sharper rungs.

---

## 6. Implications for future rungs (D2, D3, …)

This note imposes the following constraints on future work:

- **No more floor-only stories.** Any further mechanism work must treat the floor as part of a structured constraint, not a lone parameter.
- **No hand-wavy drivers.** If a drive term is introduced, its origin must be tied to:
  - θ and the vacuum architecture, or
  - a clearly defined external structure (e.g. boundary / dual, topological sector).
- **Repo or it didn’t happen.** Any dynamic-θ or Planck-corridor claims must be realised as:
  - scripts under `stage2/` (or an appropriate phase),
  - with CSV outputs and doc rungs,
  - and explicit non-claims.

In particular, future D2/D3 style rungs should:

1. Treat the existing 2048-point kernel and 40-point sweet subset as the **baseline** object to be confronted with sharper external-style corridors (Planck-like age and expansion, improved structure proxies).
2. Use the ψ toys and previous external campaigns only as **inspiration** for better-designed mechanisms, not as evidence.
3. Record any new dynamic-θ mechanism as:
   - a well-specified ODE or field equation,
   - a clear pipeline from parameters to observables,
   - and a precise list of where it fails or remains speculative.

---

## 7. Non-claims

This note does **not** claim that:

- the obstruction picture is realised in nature,
- the non-cancellation floor explains the observed vacuum energy,
- θ\* is the true value of any physical parameter,
- the ψ toys are in any way fundamental,
- or any dynamic-θ mechanism explored so far is predictive.

It is a status report on the internal numerical and conceptual situation of the obstruction program, intended to keep future work honest and reproducible.


### D3 – Gap to a Planck-like FRW band

The helper `apply_planck_like_frw_corridor_v1.py` attaches a narrow, Planck-inspired band in the `(age_Gyr, omega_lambda)` plane to the static FRW kernel. In the current snapshot this band is empty: no grid point in the 2048-point θ grid, and no point in the pre-data kernel or 40-point sweet subset, lies inside the toy Planck-like box.

To make this more quantitative we introduced `analyze_planck_like_gap_v1.py`, which reports how the kernel and sweet subset sit relative to that box and writes a small summary table (`stage2_obstruction_planck_like_gap_summary_v1.csv`) with the closest points in FRW space. The result is that the present kernel lives near but outside a realistic Planck-like band; the emptiness of `in_planck_like_corridor_v1` is therefore interpreted as a diagnostic of the current FRW toy pipeline rather than as a final obstruction verdict.

In other words, a realistic late-time corridor tied to Planck central values already pushes us into a regime where the static kernel as currently constructed misses the band entirely. This is one of the motivations for the “dynamic θ and frustrated floor” strand: rather than forcing a static θ to hit a Planck-like box, we will explore whether an evolving θ(t) plus a non-cancellation floor can generate compatible late-time effective parameters while remaining faithful to the obstruction picture.
