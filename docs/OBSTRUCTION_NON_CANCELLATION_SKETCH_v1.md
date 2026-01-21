# Obstruction program – non-cancellation sketch (v1)

Status: design-level memo, not a claim. This file does not change any Phase 0–5 contracts or Stage 2 promotion gates.

## 1. Context: what we actually have in hand

The obstruction program is built on top of the locked Stage I stack (Phase 0–5) and the Stage 2 belts. In the current snapshot:

- Phase 3 provides mechanism amplitudes over a 2048-point θ-grid:
  - `mech_baseline_A0`, `mech_baseline_A_floor`, `mech_baseline_bound`,
  - `mech_binding_A0`, `mech_binding_A`, `mech_binding_bound`.
- Phase 4 provides FRW-style masks and scalars:
  - `E_vac`, `omega_lambda`, `age_Gyr`,
  - FRW viability flags (`frw_viable`, `lcdm_like`, toy corridor flags),
  - data-probe flags (with `frw_data_ok` currently empty).
- Stage 2 builds:
  - a pre-data FRW kernel (1016 / 2048 grid points) where the FRW background is structurally sane,
  - FRW corridor diagnostics (families F1–F5 and their robustness tests),
  - a joint mech–FRW θ-grid with strong correlations between FRW scalars and mechanism amplitudes,
  - obstruction-specific helpers:
    - static kernel table,
    - toy and external-style late-time corridors,
    - external-style age and expansion corridors,
    - structure-proxy flags,
    - and a summary table of how the Phase 3 amplitudes behave inside these families.

The obstruction program is an interpretive overlay on this stack: it does not redefine the phases, but asks whether the existing machinery naturally supports a “forbidden full cancellation” picture.

## 2. Informal picture: forbidden full cancellation

Informally, the obstruction story says:

- The vacuum sector behaves as if reality is trying to cancel to zero but fails.
- There is a non-cancelling component that cannot be tuned away, and its bookkeeping shows up as FRW backgrounds and structure-friendly universes.
- The θ-grid and the associated amplitudes are a way of scanning this failure to cancel and checking whether the residual behaves like a stable “floor” rather than a tunable accident.

The goal of this memo is to translate that informal picture into mathematical objects that can sit inside the Phase 0–5 scheme and be tested by Stage 2.

## 3. Objects and notation

We work with:

- A discrete θ-grid: \\(\\{\\theta_i\\}_{i=1}^{N}\\) with \\(N = 2048\\) in the current snapshot.
- FRW scalars:
  - \\(E_\\mathrm{vac}(\\theta_i)\\),
  - \\(\\omega_\\Lambda(\\theta_i)\\),
  - \\(\\mathrm{age}(\\theta_i)\\).
- Mechanism amplitudes:
  - baseline set \\(A_\\mathrm{base}^{(k)}(\\theta_i)\\) for \\(k \\in \\{0, \\mathrm{floor}, \\mathrm{bound}\\}\\),
  - binding set \\(A_\\mathrm{bind}^{(k)}(\\theta_i)\\) for \\(k \\in \\{0, A, \\mathrm{bound}\\}\\),
  - instantiated in code as the six columns `mech_baseline_*`, `mech_binding_*`.
- Kernel and corridors:
  - FRW pre-data kernel \\(K\\subseteq\\{1,\\dots,N\\}\\) (size 1016),
  - FRW corridors and LCDM-like sets from Stage 2,
  - external-style corridors \\(C_j\\subseteq\\{1,\\dots,N\\}\\) defined by:
    - age bands,
    - late-time expansion bands,
    - basic structure proxies,
  - “sweet subsets” given by intersections such as:
    - \\(S_{\\mathrm{age+LCDM+toy}}\\): the 40-point set surviving kernel, LCDM-like, toy corridor and external-age-\\(v2\\).

All of these are realized concretely in CSV tables under `phase4/outputs/tables/` and `stage2/obstruction_tests/outputs/tables/`.

## 4. What “forbidden full cancellation” would need to mean

A strong obstruction-style claim would have to say something like:

1. **Non-vanishing floor on a kernel.**  
   There exists at least one mechanism amplitude \\(A(\\theta)\\) and a non-empty kernel \\(K\\) such that
   \\[
     \\inf_{i \\in K} A(\\theta_i) \\ge A_\\ast > 0
   \\]
   for some \\(A_\\ast\\) that is not an artefact of discretization or of a trivial reparameterisation of FRW scalars.

2. **Stability under reasonable external corridors.**  
   If we intersect \\(K\\) with a small family of external-style corridors \\(C_j\\) that encode:
   - age-compatible universes,
   - acceptable late-time expansion behaviour,
   - basic structure-friendly conditions,
   then the surviving set \\(K' = K \\cap C_1 \\cap \\dots \\cap C_m\\) is:
   - non-empty,
   - and the same lower bound \\(A_\\ast\\) applies (up to controlled slack).

3. **Non-triviality.**  
   The lower bound is not a tautology of the construction (e.g. not forced by a hard-coded cutoff in the definition of \\(A\\)) and not equivalent to a simple bound on FRW scalars that could have been imposed directly.

4. **Continuum or refinement behaviour.**  
   Under reasonable refinements of the θ-grid or the underlying ansatz, the statement
   \\[
     A(\\theta) \\ge A_\\ast
   \\]
   on a suitably defined kernel persists, suggesting that the non-cancelling floor has a genuine structural origin rather than being a one-off feature of a particular toy scan.

This is the level at which a “forbidden full cancellation” result would start to look like a real obstruction claim, rather than a handful of coincidentally non-zero values.

## 5. What the current O1–O2 results already tell us

From the O1–O2 obstruction rungs we already know:

- The FRW pre-data kernel is non-empty and sizable (1016 / 2048 grid points) and survives basic sanity checks (matter era, smooth \\(H^2\\), late acceleration).
- Toy and external-style corridors (age bands, LCDM-derived late-time boxes, basic structure proxies) can carve out:
  - a 40-point sweet subset `KERNEL_LCDM_TOY_AND_EXTERNAL_AGE_V2` inside the kernel,
  - a 51-point tight subset `KERNEL_AGE_TIGHT_EXP_STRUCT_TIGHT`,
  while still leaving non-empty surviving sets.
- The Phase 3 amplitudes over these sets:
  - remain strictly positive on the kernel and on the tighter subsets,
  - exhibit narrower ranges and means on the tighter subsets than on the full grid,
  - but are strongly correlated with FRW scalars, so they behave more like smooth reparameterisations of \\(E_\\mathrm{vac}\\) and \\(\\omega_\\Lambda\\) than like an independently motivated measure.

In other words, the current obstruction stack demonstrates that it is easy to define **non-empty, reasonably constrained kernels and corridors** in which the mechanism amplitudes never hit zero, but:

- this does **not yet** amount to a theorem-level lower bound \\(A_\\ast > 0\\),
- and it does **not yet** isolate a mechanism quantity that clearly deserves to be called “the” non-cancelling floor.

## 6. How this feeds into a future claim

This design memo suggests the following direction for future rungs:

1. **Candidate amplitude selection.**  
   Use the Stage 2 mech/measure analysis to select one or two amplitudes that are:
   - monotonic or at least well-behaved over the kernel,
   - structurally tied to the non-cancellation principle (e.g. `A_floor`-type quantities),
   - and not trivially equivalent to FRW scalars.

2. **Robust kernel and corridor definition.**  
   Stabilise a small set of external-style corridors (age, expansion, simple structure proxies) and define:
   - a canonical kernel \\(K\\),
   - a small family of canonical corridors \\(C_j\\),
   such that the resulting sweet subset \\(K'\\) is:
   - numerically stable,
   - and not tuned to a single special grid point.

3. **Empirical lower-bound statement (Stage 2-level).**  
   Formulate and test a Stage 2 statement of the form:
   - “On the current θ-grid and for the current ansatz, we observe
     \\(A(\\theta_i) \\ge A_\\ast > 0\\) for all \\(i \\in K'\\), with specified \\(A_\\ast\\) and variance.”
   This would be an **explicitly provisional** non-cancellation floor statement, clearly marked as a toy-grid observation rather than a continuum claim.

4. **Path to a Phase-level claim.**  
   If such a pattern persists under modest refinements and alternative ansätze, a later phase (likely a dedicated obstruction phase or an extended Phase 4/5) could promote a carefully worded version of the statement into a claims table, with:
   - explicit references to the Stage 2 artifacts,
   - a clear corridor definition,
   - and a spelled-out list of non-claims.

## 7. Non-claims

This memo does **not** assert:

- that a non-cancelling floor \\(A_\\ast > 0\\) has already been demonstrated,
- that any particular amplitude is the right candidate for \\(A\\),
- that the current 40-point or 51-point subsets are physically preferred,
- or that the current θ-grid and ansatz are sufficient for a final obstruction theorem.

It only clarifies what “forbidden full cancellation” would need to mean in the language of the existing stack, and how the current O1–O2 results can be used as a scaffold for a more rigorous claim later.
