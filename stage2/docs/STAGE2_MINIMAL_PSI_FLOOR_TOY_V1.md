# Stage 2 – Minimal Ψ + floor toy (v1)

**Rung:** obstruction-program-v1 / O3.1  
**File:** `stage2/obstruction_toy_models/src/minimal_psi_floor_toy_v1.py`  
**Outputs:** `stage2/obstruction_toy_models/outputs/tables/stage2_minimal_psi_floor_toy_trajectories_v1.csv`

This note records the first explicit Ψ + floor toy used to make the “frustrated cancellation” idea concrete. It is deliberately simple and deliberately too strong, so that the role of the floor is mathematically transparent.

---

## 1. Definition of the toy

We consider a single complex degree of freedom Ψ evolving under a linear “cancellation” dynamics with a hard floor on its magnitude.

- Phase space: Ψ ∈ ℂ.
- Cancellation dynamics: exponential damping toward zero with rate γ.
- Floor: a fixed ε > 0 such that |Ψ| is never allowed to go below ε.

In the current implementation this is realised as:

- Draw 256 initial conditions uniformly in a disk in ℂ with radii in [0.2, 2.0].
- Evolve for `n_steps = 2000` with step size `h = 0.01` and damping rate `γ = 1.0`.
- At each step:
  - apply the linear damping update (driving Ψ toward 0),
  - if the updated point would satisfy |Ψ| < ε, project it radially back to the circle |Ψ| = ε.

The only “physics” in this toy is:

- an explicit attempt to cancel Ψ to zero, and
- an explicit prohibition encoded as a hard lower bound |Ψ| ≥ ε.

The floor ε is not derived; here it is simply set to ε = 0.05 as a dimensionless toy value.

---

## 2. Outputs and diagnostics

The helper `minimal_psi_floor_toy_v1.py` writes a single table:

- `stage2/obstruction_toy_models/outputs/tables/stage2_minimal_psi_floor_toy_trajectories_v1.csv`

with one row per initial condition and columns:

- `ic_index`: trajectory index.
- `psi0_real`, `psi0_imag`: initial Ψ components.
- `r0`: initial radius |Ψ₀|.
- `ever_on_floor`: boolean, whether the trajectory ever touched the floor.
- `floor_active_fraction`: fraction of time steps where the floor projection was active.
- `r_min`, `r_max`, `r_final`: minimum, maximum and final radii over the trajectory.
- `gamma`, `eps`, `h`, `n_steps`: the numerical parameters.

In the current snapshot:

- `n_ics = 256`.
- All trajectories satisfy `ever_on_floor = True`.
- For every trajectory:
  - `r_min = ε`,
  - `r_final = ε`,
  - `r_max` matches the initial radius `r0`.
- The floor-active fraction has:
  - mean ≈ 0.85,
  - range roughly 0.82–0.93.

So every trajectory:

- starts somewhere in the disk,
- is driven inward by the cancellation dynamics,
- hits the floor |Ψ| = ε,
- then spends most of its subsequent evolution exactly on the floor.

---

## 3. What this toy shows (and what it does not)

What it *does* show:

- A clean, fully reproducible example where:
  - cancellation dynamics by themselves would drive Ψ → 0,
  - a hard lower bound |Ψ| ≥ ε forbids perfect cancellation,
  - and the resulting long-term behaviour is that **all trajectories end up stuck on the floor**.
- This is a mathematically explicit realisation of the slogan “attempt to not-exist, blocked by a floor”.

What it *does not* show:

- It is not a realistic dynamical system:
  - the floor is implemented as a hard projection, not as something derived from an action or a constraint,
  - there are no fluctuations or competing drives; once the floor is hit, there is nothing to pull Ψ away from it.
- It is not yet “frustrated cancellation” in the richer sense of a system that keeps trying to cancel and keeps being blocked:
  - in this toy, the cancelling drive wins quickly in the radial direction,
  - the floor wins globally by forbidding |Ψ| = 0,
  - after a short transient there is no further competition; the trajectory simply sits on the floor.
- The ε value is arbitrary, and there is no connection to any physical scale or to the cosmological constant.

In short:

- v1 is a **floor-dominated toy**, not yet a realistic frustrated process.
- It serves as a didactic baseline: “if you combine pure cancellation + hard floor, you get universal attraction to the floor”.

---

## 4. Role in the obstruction program

Within the obstruction program this object plays a limited but clear role:

- It is the first explicit Ψ + floor toy where:
  - there is a transparent cancellation drive (exponential damping),
  - there is a transparent obstruction (hard |Ψ| ≥ ε),
  - and the outcome is simple enough to summarise quantitatively.
- It gives a concrete benchmark for later toys:
  - more realistic frustrated systems should be compared against this “everything ends up on the floor” limit.
- It is entirely decoupled from the Phase 0–5 stack and from the FRW and mechanism corridors:
  - no Phase contracts, masks, or promotion gates are changed,
  - no claims are made about real cosmology or about the value of any θ-like parameter.

Later rungs will introduce:

- softer or derived floors,
- competing drives or fluctuations that keep “trying to cancel” even after the floor is reached,
- and possible ways of embedding such a degree of freedom into the existing Stage 2 obstruction tables.

This note simply records v1 as the minimal, fully floor-dominated case.

---

## 5. Non-claims

- This toy does **not** explain the cosmological constant or any real vacuum energy.
- It does **not** claim that reality is governed by a single complex Ψ with a hard magnitude floor.
- It does **not** claim that the chosen parameters (γ, ε, h, n_steps) have any physical significance.
- It does **not** connect to the Standard Model, to GR, or to observational data.

It is only a controlled sandbox for one idea: what happens when a pure cancellation dynamics is obstructed by a hard, non-zero floor.

