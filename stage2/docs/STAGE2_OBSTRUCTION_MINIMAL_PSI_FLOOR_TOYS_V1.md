# Stage 2 obstruction: minimal ψ–floor toy experiments (v1)

This note records the first minimal ODE-level experiments with a “floor” constraint on a complex scalar ψ and uses them as a sanity check on the frustrated-cancellation intuition. The goal is not to promote any new claim, but to see, in the simplest possible setting, what a hard floor actually does and does not do.

All experiments are purely 0D ODE toys: there is no spacetime, no FRW background, and no connection to the actual θ-grid or to Phase 3 / Phase 4 numerics. They are conceptual labs only.

## 1. Definitions and setup

We work with ψ(τ) ∈ ℂ and a norm r(τ) = |ψ(τ)|. The floor scale ε > 0 is fixed; in these runs ε = 0.05. We define a projection that enforces r ≥ ε by clamping back to the circle of radius ε whenever dynamics would try to go inside it.

The base dissipative dynamics is:
dψ/dτ = -γ ψ
with γ = 1. In isolation this just drives ψ → 0.

The floor projection acts as:
- if |ψ| ≥ ε, leave ψ unchanged,
- if |ψ| < ε, project back to |ψ| = ε along the radial direction:
  ψ ↦ ε ψ / |ψ|.

This is intentionally crude: it is a hard projector, not a smoothed penalty.

We then consider two toy systems:
1. Pure floor + dissipation (no drive).
2. Floor + dissipation + periodic drive.

For each system we draw 256 random initial conditions ψ0 in a broad annulus in the complex plane and integrate for 2000 steps with step size h = 0.01. For each trajectory we record:
- r0 = |ψ0|,
- r_min, r_max over the trajectory,
- r_final at the final time,
- a Boolean ever_on_floor,
- floor_active_fraction = fraction of time steps where |ψ| was clamped.

## 2. Toy A: dissipation + floor only (no drive)

Dynamics:
dψ/dτ = -γ ψ
with γ = 1 and the floor projection at r = ε applied after each ODE step.

Numerical snapshot (256 trajectories):
- r0 in roughly [0.20, 2.0], mean ≈ 1.11.
- r_min = ε = 0.05 for every trajectory.
- r_max matches r0: the dissipative part only decreases |ψ|.
- r_final = ε for all trajectories.
- ever_on_floor is True for all trajectories.
- floor_active_fraction lies in [0.817, 0.9305], with mean ≈ 0.853.

Interpretation:
- Every trajectory falls onto the floor and then spends most of its life there, being repeatedly clamped.
- In this toy, the floor acts as an absorbing set: once the dynamics arrives at r = ε, nothing pushes it away.
- The “frustration” here is trivial: dissipation wants r → 0; the floor forbids r < ε; the long-time state is a static ring at r = ε.

This is not a model of a living, noisy universe. It is a minimal demonstration that “floor + pure damping” just produces a frozen shell.

## 3. Toy B: dissipation + floor + periodic drive

Dynamics:
dψ/dτ = -γ ψ + i ω ψ + D
with γ = 1, ω = 1, a constant complex drive D of magnitude 0.15, and the same floor projection at r = ε after each step.

Numerical snapshot (256 trajectories):
- r0 in roughly [0.21, 2.0], mean ≈ 1.06.
- r_min in roughly [0.048, 0.105], mean ≈ 0.084.
- r_max tracks the initial amplitudes, similar to Toy A.
- r_final is concentrated near ≈ 0.106, slightly above ε.
- ever_on_floor is True for only about 19% of trajectories; ≈ 81% never hit the floor over the run.
- floor_active_fraction has mean ≈ 0.005 and is zero for most trajectories.

Interpretation:
- The periodic drive plus damping generates a non-trivial attractor near (but not at) the floor.
- The floor is almost never active: it only occasionally clips trajectories that would dip slightly below ε.
- The “shape” of the long-time behaviour is controlled by the balance of damping and drive, not by the floor itself.

In other words, as soon as we add a drive, the floor becomes a guard-rail, not the engine. The engine is the non-zero forcing term.

## 4. Lessons for the obstruction and frustrated-floor intuition

These 0D toys are too simple to be read as cosmology, but they give some honest constraints on the intuition:

1. A floor by itself is not a frustrated dynamics.
   - Pure dissipation + hard floor freezes everything onto the floor.
   - The system is “frustrated” only in a trivial sense: the preferred state |ψ| = 0 is forbidden, so it sits at |ψ| = ε and stops.

2. To get a living, genuinely frustrated process you need at least:
   - a tendency to cancel (dissipation, or something that tries to lower |ψ|),
   - a non-zero drive or forcing that keeps pushing the system away from the floor,
   - the floor as a hard bound that occasionally intervenes.

   In that regime the floor records the fact that “trying to go to zero” sometimes collides with a global bound, but the actual motion is in the competition between drive and damping.

3. The floor should be interpreted as a constraint, not a source of energy.
   - In both toys the energy-like quantity is tied to |dψ/dτ|, which is set by the ODE terms.
   - The floor does not generate energy; it only forbids further cancellation once r reaches ε.
   - Any story in which “the attempt to reach zero” powers the universe has to be carried by the dynamics and the drive terms, not by the existence of the floor alone.

4. Static Θ-corridors vs dynamic frustrated process.
   - The obstruction program in the FRW stack works with static corridors and masks on θ and background scalars (viability, LCDM-likeness, age, etc.).
   - Those corridors are well-defined filters in parameter space, but they are not themselves a dynamic frustrated process; they slice a static grid of models.
   - If we want a genuine “frustrated-cancellation” picture, we would need a θ-dynamics plus something like a drive, with the FRW and external corridors acting as constraints on that dynamics, not as standalone statements.

5. What these toys do and do not justify.
   - They justify talking about a floor as a constraint in a dynamical system and show explicitly that “floor-only” dynamics is not the right picture.
   - They do not justify any specific cosmological claim, any link to the observed Λ, or any identification of θ with a real field.

## 5. Role in the Stage 2 obstruction program

Within the obstruction program these toys play a narrow, explicit role:

- They provide a concrete example where:
  - a floor-only system collapses and freezes,
  - a driven system lives in a region near the floor, with the floor rarely active.
- They support treating the “frustrated floor” idea as:
  - a dynamical story about competition between drive, damping, and constraints,
  - not as a claim that “a static floor by itself explains the universe”.

At this point, the FRW-side obstruction stack remains a static analysis on a fixed θ-grid. Any attempt to promote a dynamic Ψ + floor model toward the phases will require separate, tightly scoped design rungs, explicit equations, and clear separation between:
- what is a toy ODE picture,
- what is a serious proposal for θ-dynamics,
- and what, if anything, is being claimed about the real universe.

## 6. Non-claims

This note does not:
- Propose that the minimal ODEs used here are physically fundamental.
- Identify ψ with any real field or observable.
- Claim any preferred θ-value or θ-dynamics.
- Modify any Phase 0–5 contracts or Stage 2 promotion gates.

It is an interpretive, internal record of what the first ψ + floor toy experiments showed when we actually ran them.
