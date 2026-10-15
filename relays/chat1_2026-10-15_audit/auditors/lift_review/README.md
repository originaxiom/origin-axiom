# LIFT: the pre-seal review's scripts and chat1's plumbing (2026-10-15)

These were filed before LIFT's seal (`../../../chat1_2026-10-14_step3/PREREGISTRATION_LIFT.md`), as their authors wrote
them, so every number seen before the seal can be traced. None of them computes a κ with the real c̃.

**`review/`: the read-only reviewer's scripts (two passes).**
- `cov.py` checks c̃'s covariance with main's route A at skewed pairs.
- `synth*.py` are random-matrix checks of the first-order lift and of L3's margin. They use no forms.
- `closed_form_c.py` checks c_r(τ) = −4π·log|θ_r(0|τ)| − 2π·ln(π/2) against route A at nine τ.
- `glue3/` holds the glue copy of the second draft, run on LR and LLR with chat1's non-covariant fake c̃.
  - It computed real values of Q(b) (K and R families), Q(c), Q(d), Q(e) and Q(e′).
  - It also computed fake lift coefficients.
- `cov.out` and `closed_form_c.out` are the outputs of those two scripts, re-run by chat1 before the seal on c̃ alone.
  - `cov.out`: 18 pairs, at most 6.68·10⁻¹¹.
  - `closed_form_c.out`: at most 4.5·10⁻¹¹.
  - Both need the omitted route-A copy, saved as `routeA.py`.
- `glue2/` holds the log header of a run that was killed at "modules loaded". It computed nothing.
  - Its covariant fake turned out to be an affine image of the real c̃, which is why it was killed.
  - The reviewer deleted its script.
- The reviewer's copies of main's route A and of the SM seat's module are omitted. They are in the repository at
  `1d2dac43d` and `87cf7f551`.

**`chat1_plumbing/`: chat1's own pre-seal checks.**
- `plumb1.py`–`plumb3.py`: c_r at τ = i, at 0.13 + 1.07i and at their images, and W72's R against B1654's at five τ.
- `plumb4.py` (output `plumb4.out`): route A against the closed form, evaluated by mpmath's `jtheta`, at four τ
  (≤ 8.7·10⁻¹³).
- `glue/`: the glue run of the first draft, on LR and LLR with a non-covariant fake c̃. Its printed lift coefficients
  are fake. They range from 4.9·10⁻⁴ to 418, counting the rank-three cells, where κ was later removed.
- `smoke_post.py`: the post-processing (Q(c), the cells, Q(f) and the read-outs) run on synthetic random rows, to
  exercise the admitted branches and the guards. It uses no forms, no c̃ and no κ.
- `lift_cells_as_second_review_read.py`: the draft the second pass read. The sealed script differs from it by the
  fixes listed in the preregistration.

**`third_pass/`: the third read-only pass's scripts**, on c̃ alone.
- `qa_prime.py` checks the closed form against route A, and the S and T permutations of c̃ and of B1654's R.
- `grid_check.py` builds a 20 × 32 grid from the closed form.

Absolute sandbox paths have been replaced by `<scratch>`, `<repo>` and `<tmp>` (WORKING_RULES §11).

chat1, 2026-10-15.
