# W172 — THE RIDDLE, horn 1 at the counted line: the mirror lemma, how firmly the frame's own potential holds Re τ, whether any variation of the content breaks CP there, and the price of the data's Re τ (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **THE RIDDLE** (NOTE, "Reading: THE RIDDLE"; relay §316), program item 1. Horn 1 says that what the frame's own
  dynamics selects keeps a residual symmetry, so it conserves CP. The owner asked that the riddle be probed to the end.
- **Horn 1's mechanism has two parts:**
  - the potentials see only the mirror-invariant spectrum;
  - invariant functions are stationary on the mirror's fixed loci.
- **The record's strongest instance is W169.** At the counted line the potential picks X = 1, the mirror's fixed point,
  at every one of the 38 rows' heights, and W170 found J = 0 exactly there.
- **The question here is how strong that selection is.** If it is strong, horn 1 binds. If it is weak, the frame does
  not really decide Re τ, and CP is settled by effects the frame does not contain.

## The mirror lemma (by hand; checked in P0)

- The one-loop kernel is k(ψ; τ) = −Σ_p Σ′ cos 2π(m(p₁ + ψ₁) + n(p₂ + ψ₂)) y^s/∣m + nτ∣^{2s} (W59, at s = 3).
- Under τ ↦ −τ̄, ∣m − nτ̄∣ = ∣m − nτ∣. Relabelling n ↦ −n (the parities are invariant) gives
  k(ψ₁, ψ₂; −τ̄) = k(ψ₁, −ψ₂; τ).
- So every content's potential obeys V(−τ̄; ψ₁, −ψ₂) = V(τ; ψ₁, ψ₂). In main's line convention, ψ = (−a, b), that is
  (τ, a, b) ↦ (−τ̄, a, −b): the mirror.
- It holds for every content, chiral or not, because the potential sees only ∣m + nτ + q w∣.

## The computation (fixed now)

- **The line and its orbit.** The line (2/5, 1/10), on its T-orbit X = Re τ ∈ [0, 5), exactly as W169 (whose functions
  are reused). Its mirror fixed points are X = 1 and 3.5.
- **The heights.** The 38 rows' heights of W158 (read from W167's row lists, as W169 read them).
- **The content.** The frame's fields (W167's FIELDS), at s = 3, N = 48 (W59, W167, W169).
- **The variations, for P2:**
  - the bosons' weight β ∈ {0.5, 1, 2, 5, 10, 20};
  - the kernel at s = 4 (N = 48; its truncation is smaller than at s = 3);
  - each sector's fields alone: the quarks (Q, u^c, d^c), the leptons (L, e^c), the Higgs pair;
  - in every combination of β and s with the full content, and the sector subsets at β = 1 and s = 3.
  - s = 2 is left out: at N = 48 its truncation error is comparable to the signal measured in P1.
- **The minimum over X.** A grid of 5 000 points on [0, 5) and a bounded refinement around the grid's least (W169's
  method).

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| P0 | **The mirror lemma, numerically.** V(−τ̄; ψ₁, −ψ₂) = V(τ; ψ₁, ψ₂) at 24 random points (\|Re τ\| < 1, Im τ ∈ [1, 4], ψ random), for the frame's content at s = 3 and s = 4, to 10⁻¹² relative. Control: the same with ψ₂ not reversed fails by more than 10⁻⁶ at most points | 99% |
| P1 | **How firmly Re τ is held.** At every one of the 38 heights the X-amplitude of V over the orbit (max − min) is below 10⁻³ of \|V*\|, and the X-curvature at the minimum is below 10⁻³ of the y-curvature | 95% |
| P2 | **No variation breaks CP at one loop.** In every variation and at every height, the global X-minimum lies at a mirror fixed point (1 or 3.5) within 10⁻⁴ | 75% |
| P3 | **The price of the data's Re τ.** At every row, the least sup-norm of a CP-even change of V that makes the row's X a global minimum, bounded below by (V(X_row) − V*)/2, is below 10⁻⁴ of \|V*\| | 85% |
| R | **Read-outs** (no predictions): the X-profile's leading Fourier coefficients (period 5) per height; the s = 3 and s = 4 profiles compared; any off-point minimum's X and its distance from the rows | — |

## What the outcomes mean (fixed now)

- **P1 and P3 hold (the expected outcome).**
  - The frame's one-loop potential holds Re τ by about one part in 10⁴ to 10⁵. Its CP-conserving selection is real but
    very weak.
  - So at the counted line Re τ is in effect a flat direction. Whether CP is conserved at the true state is decided by
    effects the frame does not compute: higher loops, non-perturbative terms, the Higgs's vacuum.
  - Horn 1 then sharpens. The frame's dynamics does not decide Re τ, and the data's Re τ is a choice that nothing
    forced resolves.
- **P2 holds:** no variation on record breaks CP at one loop at this line.
- **P2 fails:** some variation pitchforks off the fixed point, which is spontaneous CP violation at one loop.
  - Its X is compared with the rows' X (a read-out).
  - A variation that lands at X_row would be a lead for its own sealed arc. It is not a result here, since the
    variations are not all forced.
- **P1 fails:** Re τ is held firmly, and horn 1 binds at full strength.

## Weave or thread

- A frame result at a counted line. The line's class is counted (W167), and the contents are the frame's with stated
  variations. The lemma (P0) holds for every content and every line.

## What stays out

- s = 2, other lines' classes, two loops, the Higgs's vacuum.
- Any data comparison beyond reading the rows' X. No target file is read.

## Looks

- None. The rows' X are read as positions, with no χ.

## Seen before the rule (disclosed)

- W169's output. At the 38 heights V(X_row) − V* lies between 0.017 and 0.091, against V* between 1 083 and 1 266, and
  the X-curvature is (3.4–4.1) × 10⁻⁴ of the y-curvature. Bosons ×2 and ×5 do not move X*.
- So P1 and P3 at β = 1 and s = 3 are known in substance. The arc adds the lemma's check, the variations and the price
  at every row.
- Not computed: s = 4, β ≠ 1, 2, 5, and the sector subsets.

## Discipline

- This rule is committed and pushed before the script exists.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
