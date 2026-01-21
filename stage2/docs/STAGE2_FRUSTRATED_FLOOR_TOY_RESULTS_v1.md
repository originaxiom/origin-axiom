# Stage 2 – frustrated floor toy results (v1)

Status: obstruction-program-v1, O5.1–O5.2  
Scope: 0D toy tests of a constrained complex amplitude with a hard floor |ψ| ≥ ε, with and without a simple driving term.

This memo records what we actually see in the first ψ + floor toys and how that informs the obstruction program. It is descriptive only and makes no claims about real cosmology or quantum fields.

## 1. Model recap (from design doc)

We work with a single complex amplitude ψ(τ) evolving under:

- a relaxation term that tries to drive ψ toward zero, and
- a hard floor |ψ| ≥ ε implemented as a projection whenever the norm would fall below ε.

In the driven case we add a simple periodic “stirring” term so ψ does not simply collapse and stick to the floor.

The parameters in the current snapshot are:

- ε = 0.05
- γ = 1.0
- time step h = 0.01
- n_steps = 2000
- n_ics = 256 random initial conditions in a disk of radius ≲ 2
- driven toy only: ω = 1.0, drive amplitude = 0.15

All numbers below are taken from the CSV outputs in
`stage2/obstruction_toy_models/outputs/tables`.

## 2. Undriven ψ + floor toy (minimal_psi_floor_toy_v1)

Input and output file:

- Code: `stage2/obstruction_toy_models/src/minimal_psi_floor_toy_v1.py`
- Output: `stage2_minimal_psi_floor_toy_trajectories_v1.csv`

Basic stats over 256 trajectories:

- Initial radii r0:
  - mean ≈ 1.11
  - min ≈ 0.20, max ≈ 2.00
- Minimum radius r_min:
  - exactly ε = 0.05 for every trajectory (within floating error)
- Final radius r_final:
  - exactly ε = 0.05 for every trajectory
- `ever_on_floor`:
  - True for 256 / 256 trajectories
- `floor_active_fraction` (fraction of steps spent at the floor):
  - mean ≈ 0.85
  - range ≈ 0.82–0.93 across trajectories

Interpretation.

- With pure relaxation plus a hard floor and no driving, the dynamics do what we would expect from a simple gradient flow with a constraint: all trajectories collapse onto the floor and stay there.
- The floor is genuinely “felt”: every trajectory hits |ψ| = ε, and after that almost the entire trajectory is spent at the floor.
- This is a good sanity check that the constrained dynamics is implemented correctly, but it is *too trivial* to resemble the kind of “persistent frustrated cancellation” we are ultimately interested in. There is no ongoing attempt to explore state space once the floor is reached.

Non-claims.

- This toy does *not* represent any realistic field dynamics, and ε here is purely a toy parameter, not a physical vacuum scale.
- No connection is made to FRW, θ\*, or any mechanism amplitudes; this is a bare 0D test of the constraint structure.

## 3. Driven ψ + floor toy (minimal_psi_floor_toy_with_drive_v1)

Input and output file:

- Code: `stage2/obstruction_toy_models/src/minimal_psi_floor_toy_with_drive_v1.py`
- Output: `stage2_minimal_psi_floor_toy_with_drive_trajectories_v1.csv`

Basic stats over 256 trajectories:

- Initial radii r0:
  - mean ≈ 1.06
  - min ≈ 0.21, max ≈ 1.99
- Minimum radius r_min:
  - mean ≈ 0.084
  - min ≈ 0.048, max ≈ 0.105
- Maximum radius r_max:
  - matches r0 distribution (∼ 0.21–1.99), as expected for this simple driven relaxation
- Final radius r_final:
  - ≈ 0.106 for all trajectories (the dispersion is ≪ 10⁻⁸)
- `ever_on_floor`:
  - True for 49 / 256 trajectories
  - False for the remaining 207 / 256 trajectories
- `floor_active_fraction`:
  - mean ≈ 0.005
  - median = 0.0
  - max ≈ 0.084

Interpretation.

- The combination of damping, drive, and floor produces a non-trivial steady behaviour:
  - all trajectories converge to a radius ≈ 0.106, which is **above** the floor (ε = 0.05),
  - only a minority of trajectories ever actually touch the floor, and when they do the floor is active only for a small fraction of steps.
- The floor is still present in the dynamics but now acts more like a hard inner exclusion region which some trajectories graze and others orbit around, rather than a final absorbing state.
- This is much closer to the “frustrated” picture: there is a continual attempt to move inward under damping, but the combination of drive and floor stabilises the system at a radius set by the interplay of γ, drive amplitude, ω, ε and the discretisation.

Non-claims.

- We do not claim that the specific steady radius (∼ 0.106) has any physical meaning; it is an artefact of the particular toy parameters chosen here.
- The drive term is deliberately simple and ad hoc; it stands in for “whatever additional dynamics prevents trivial collapse”, not for a realistic microscopic mechanism.
- This toy is not coupled to any FRW or mechanism structure and does not encode a real non-cancellation floor in θ space; it only shows that a constrained, driven system can orbit near but not on a hard floor.

## 4. Lessons for the obstruction program

From these two toys we learn:

1. A bare floor plus simple relaxation degenerates into “everything collapses onto the floor and stays there”, which is not the kind of obstruction we want in the full program.
2. Adding a modest drive term produces a genuinely *frustrated* configuration:
   - the floor is enforced,
   - but the long-time behaviour sits in a band above the floor,
   - with only occasional or partial contact with the constraint.
3. Even in 0D, the long-time radius is set by a balance of damping, drive and the floor; in higher-dimensional or more structured models we should expect similar trade-offs between:
   - internal dynamics that try to cancel,
   - external-style corridors, and
   - whatever imposes the non-cancellation floor.

At this stage these are heuristics only. The next rungs will:

- tidy the toy code and documentation so it is clear how the parameters control the late-time radius and floor contact, and
- explore whether any of these structures can be abstracted into a more general “frustrated projection” picture that is compatible with the Stage 2 obstruction stack.

## 5. Non-claims and status

- No Phase 0–5 contracts, FRW masks, or Stage 2 promotion gates are affected by these toys.
- The ψ-floor dynamics are strictly auxiliary: they do not alter any θ-grid, any mechanism amplitude, or any of the FRW/data-probe corridors.
- No statement is made that a real vacuum field works this way; these are first probes of what an honest “frustrated floor” *could* look like in a minimal setting.

