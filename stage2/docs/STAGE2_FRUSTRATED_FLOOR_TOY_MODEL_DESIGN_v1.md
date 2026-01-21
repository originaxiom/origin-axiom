# Stage 2 – Frustrated Floor Toy Model (Design v1)

Status: **DRAFT – design only.** This note defines a minimal, finite-dimensional toy model for a “frustrated floor” dynamics. It is a Stage 2 obstruction/diagnostic helper, not a Phase 0–5 claim and not a physical theory.

The aim is to:
- make the “perpetual attempt to cancel + non-zero floor” idea precise in a small, analyzable system, and
- provide a clean object we can actually compute with on the existing θ-grid and kernel.

It deliberately **does not**:
- derive the floor from holography/topology/information,
- couple to the Standard Model or full GR,
- make any statement that the toy model describes the real universe.

It is infrastructure for obstruction-style tests.

---

## 1. Minimal finite-dimensional setup

We work on the existing discrete θ-grid used in Phase 3/4 and Stage 2:

- Let \( \theta_k \), \( k = 0, \dots, N-1 \) be the grid points (currently \( N = 2048 \)).
- Let \( \psi_k(\tau) \in \mathbb{R} \) (or \(\mathbb{C}\)) be a single scalar “cancellation amplitude” attached to each grid point.
- Collect them into a vector \( \psi(\tau) \in \mathbb{R}^N \).

### 1.1 “Attempt to cancel”

The simplest “attempt to cancel everything” is a gradient-flow toward zero:

\[
\left.\frac{d\psi}{d\tau}\right|_{\text{cancel}} = -\gamma \psi, \quad \gamma > 0.
\]

If this were the only term, every component would decay exponentially to zero and we would have complete cancellation.

### 1.2 Background preference vector

We also allow a “background preference” vector \( a \in \mathbb{R}^N \) which reflects structure inherited from the existing stack (FRW masks, mechanism amplitudes, etc). For the design we keep it abstract:

- \( a_k \) encodes “where the system would like to sit” if there were no floor, e.g. informed by Phase 3 mechanism amplitudes or FRW viability.

A simple unconstrained relaxation toward this background is:

\[
\left.\frac{d\psi}{d\tau}\right|_{\text{relax}} = -\gamma (\psi - a).
\]

Unconstrained fixed point: \( \psi^\star = a \).

Later, when we connect to data, a natural choice will be:
- let \( a_k \) be a rescaled version of a Stage 3 amplitude such as `mech_binding_A0(θ_k)` on the pre-data kernel (and 0 elsewhere).

### 1.3 Global floor constraint

We now impose a **global floor** on the norm of \( \psi \):

\[
\|\psi(\tau)\|_2 \equiv \left( \sum_k \psi_k(\tau)^2 \right)^{1/2} \ge \varepsilon > 0.
\]

Interpretation:
- the system “tries” to cancel towards zero under the relaxation dynamics,
- but there is a hard lower bound on how close the global configuration can get to perfect cancellation.

There are two equivalent ways to encode this:

1. **Continuous constrained dynamics** with a Lagrange multiplier \( \lambda(\tau) \):

   \[
   \frac{d\psi}{d\tau} = -\gamma (\psi - a) + \lambda(\tau) \frac{\psi}{\|\psi\|_2},
   \]
   with \( \lambda(\tau) \) chosen so that \( \|\psi(\tau)\|_2 \ge \varepsilon \) for all \(\tau\).

2. **Discrete relax-then-project** scheme (simpler for numerics):
   - starting from \( \psi \), take a small unconstrained step towards \( a \):
     \[
     \tilde{\psi} = \psi - \eta (\psi - a)
     \]
     for some small step \( \eta > 0 \),
   - then apply a **floor projection**:
     - if \( \|\tilde{\psi}\|_2 \ge \varepsilon \), keep it: \( \psi_{\text{new}} = \tilde{\psi} \),
     - if \( \|\tilde{\psi}\|_2 < \varepsilon \) and \( \tilde{\psi} \neq 0 \), rescale:
       \[
       \psi_{\text{new}} = \varepsilon \, \tilde{\psi} / \|\tilde{\psi}\|_2,
       \]
     - if \( \tilde{\psi} = 0 \), fall back to the direction of \( a \) (e.g. \( \psi_{\text{new}} = \varepsilon \, a/\|a\|_2 \) if \( a \neq 0 \)).

For small steps, the discrete relax-then-project scheme approximates the continuous constrained flow and is straightforward to implement.

---

## 2. Stationary behaviour of the toy model

The unconstrained fixed point is \( \psi^\star = a \). Two regimes:

1. **Floor inactive** (uninteresting regime for our purposes):

   If \( \|a\|_2 \ge \varepsilon \), then the constrained and unconstrained problems agree: the relaxation dynamics converges to \( \psi^\star = a \) and the floor never binds.

2. **Floor active** (the genuinely “frustrated” regime):

   If \( \|a\|_2 < \varepsilon \), the system **cannot** reach its unconstrained fixed point without violating the floor. In the relax-then-project picture:

   - unconstrained relaxation tries to push \( \psi \) toward \( a \),
   - once you get sufficiently close that \( \|\psi\|_2 < \varepsilon \), the projection lifts you back to the sphere \( \|\psi\|_2 = \varepsilon \),
   - in the long-time limit, the configuration sits on the floor sphere, aligned with the “preferred” direction \( a \):
     \[
     \psi^\star_{\text{floor}} = \varepsilon \, a / \|a\|_2.
     \]

In other words, the floor replaces a small-norm target \( a \) by a **rescaled** configuration \( \psi^\star_{\text{floor}} \) that has the same direction but a **minimum overall amplitude**. This is the simplest possible way to encode:

- “the system tries to cancel”
- “it would prefer to land at \( a \)”
- “but exact (or near-exact) cancellation is forbidden, so a minimum global amplitude survives.”

---

## 3. Connecting to the existing Stage 2 stack

In this design, we keep the mapping abstract, but the intended use with the actual repo is:

1. **Grid and kernel:**
   - use the existing θ-grid (N = 2048) and the pre-data FRW kernel flag from `stage2_obstruction_static_frw_kernel_v1.csv`,
   - take ψ-components only on the kernel, or weight non-kernel points appropriately.

2. **Choice of background vector a:**
   - base option: let \( a_k \) be a rescaled version of `mech_binding_A0(θ_k)` or a simple combination of the Phase 3 mechanism amplitudes, possibly zeroed outside the pre-data kernel,
   - normalize a so that \( \|a\|_2 \) is explicitly known and can be compared to a chosen floor ε.

3. **Choice of floor ε:**
   - pick ε so that the floor is **actually active** (i.e. \( \|a\|_2 < \varepsilon \)), otherwise the toy model degenerates to unconstrained relaxation,
   - explore a small family of ε values (e.g. just above \( \|a\|_2 \), and a bit larger) to see how sensitive the configuration is.

4. **Observables we care about:**
   - the final configuration \( \psi^\star_{\text{floor}} \) on the pre-data kernel,
   - how its components compare to \( a_k \) (ratio \( \psi^\star_k / a_k \) where defined),
   - how the resulting distribution looks when restricted to:
     - the 40-point “sweet” subset,
     - external-corridor-tight subsets (age/expansion/structure),
     - and to special single points such as the current θ\* candidate.

The *same* finite-dimensional mechanism can be applied regardless of which subset we then look at; the constrained dynamics is defined on the full θ-grid.

---

## 4. Role in the obstruction program

This toy model is intended to answer narrow, technical questions such as:

- If you impose a **global non-cancellation floor** on top of the mechanism-informed background \( a \), does the floor:
  - essentially leave the pattern unchanged (just rescale everything), or
  - privilege a smaller subset of θ-values in a non-trivial way?

- How does the presence of the floor interact with:
  - the pre-data kernel structure,
  - the external-style corridors (age bands, late-time expansion boxes, structure proxies),
  - the non-cancellation floor on `mech_binding_A0` we already explored as a *diagnostic cut*?

In particular, once we implement the toy model on the real θ-grid, we can:

- compute \( \psi^\star_{\text{floor}} \) for a given (a, ε),
- overlay the existing external corridor flags,
- and see whether the intersection “kernel + corridors + frustrated-floor configuration” still looks like a broad patch, a small island, or something pathologically tuned.

At this stage, the toy model is there to **organise thinking and tests** about global floors. It is not a proposal for the actual microphysics of vacuum.

---

## 5. Non-claims and next steps

Non-claims:

- This toy model is **not** a derivation of the floor from holography, topology, or information theory.
- It does **not** define a preferred θ\*, and it does not claim that the current θ\* candidate is selected by the floor.
- It does **not** modify any Phase 0–5 contracts, FRW masks, or Stage 2 promotion gates.

Next steps (rungs, O4.x):

1. Implement a small Stage 2 helper (e.g. `stage2/obstruction_tests/src/apply_frustrated_floor_projection_v1.py`) that:
   - reads `stage2_obstruction_kernel_with_mech_v1.csv`,
   - constructs a background vector a from chosen mechanism amplitudes on the kernel,
   - applies the relax-then-project scheme for one or many steps until convergence,
   - writes out the final \( \psi^\star_{\text{floor}} \) on the θ-grid.

2. Extend the existing obstruction summaries to:
   - compare \( \psi^\star_{\text{floor}} \) against a and the corridor flags,
   - compute simple statistics for the sweet subset, external-corridor-tight subsets, and candidate θ\* neighbourhood.

Only after those rungs are in place would we consider any higher-level “verdict” about how a floor interacts with the current stack.

