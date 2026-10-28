# W167 — the plan's stage 2, is the line's condition forced? The one-loop potential of the hypercharge line w = aτ + b on the shared fibre, from the frame's own fields, minimised over the torus at W158's 38 strip rows; B1761's points ranked among the census's 266 lines; a census over contents (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The plan's stage 2** (`THE_NINETEEN_PLAN_2026-10-27.md`, adopted by the owner; the owner's "agreed continue do them
  all"). Is B1761's condition forced? If so, the line follows for every line at once, a weave result. If not, the line
  is one choice, counted.
- **What the line is.** In the frame each sector sees the line through (q_L ± q_R)·w, with q the 6Y charges of
  W93's SIXY (Q 1, u −4, d 2, L −3, e 6, H 3). This is W160's 5w, −w and −9w, together with the ∓3w of the 3 Re w
  recurrence. So w is the hypercharge's flat connection on the fibre, and a field of charge q sees q·w.
- **What fixes a flat connection is its one-loop potential.** This is the Hosotani route. THE WEAVE's
  spontaneous-breaking clause admits it: a state chosen by minimising the joint action's own effective potential, with
  the domain and budget fixed first.
- **The record's kernel exists.** W59 computed the one-loop potential on the fibre for a charged field over all three
  parities. A charged boson goes to 2- and 3-torsion points, a fermion to 0. W59 never evaluated it at the strip or
  with the frame's whole content.

## The potential (fixed now)

- **The kernel.** W59's joint-parity kernel at s = 3, unchanged (`the_one_loop_potential_on_the_fibre.py`, class
  `Joint`, N = 48):
  K_σ(ψ; τ) = −σ Σ_p Σ'_{(m,n)} cos 2π(m(p₁ + ψ₁) + n(p₂ + ψ₂)) · y³/|m + nτ|⁶, where p runs over (½, 0), (0, ½) and
  (½, ½), and σ = +1 for a boson, −1 for a fermion.
- **The line's coordinates.** For w = aτ + b in main's convention, the Kronecker character is χ(m + nτ) =
  e^{2πi(nb − ma)}, so ψ = (−a, b) for unit charge, and q·ψ for charge q.
  - V is even, so ψ and −ψ agree.
  - The kernel obeys V(ψ₁, ψ₂; τ) = V(ψ₁, ψ₂ + ψ₁; τ + 1), with the three parities permuted. With ψ = (−a, b) that is
    the frame's own T-law, (τ, b) ~ (τ + 1, b − a), which fixes the sign convention. It is control L0. On the
    truncated box the map m → m + n moves the edge, so the check holds to the truncation, 10⁻⁶.
- **The content: the frame's own fields, no others.** Three generations of fermions, plus the two doublets of W158's
  and W166's type II route as bosons. Each field is weighted by its number of complex components:

  | field | charge q | weight | statistics |
  | --- | --- | --- | --- |
  | Q | 1 | 3 × 6 | fermion |
  | u | −4 | 3 × 3 | fermion |
  | d | 2 | 3 × 3 | fermion |
  | L | −3 | 3 × 2 | fermion |
  | e | 6 | 3 × 1 | fermion |
  | H_u, H_d | ∓3 | 2 + 2 | boson |

  The gauge fields are neutral and add a constant.
- **V(w; τ) = Σ_f n_f K_{σ_f}(q_f ψ; τ).** The weight per complex component is the same for both statistics. That is a
  normalisation, counted, and varied in L3.
- **The domain:** the whole torus of w at each of the 38 rows' τ (the strip, W158's rows), and the census's 266 lines
  of order 1–12 as a discrete check.
- **The budget:** one loop, the kernel above, nothing else. It is fixed before any value is computed.
- **The minimiser:** V on a 192 × 192 grid of the torus (vectorised, exact at the grid points), then Newton with
  W59's gradient and Hessian from each of the grid's ten lowest local minima; the global minimum is the least
  converged point. W59's `stationary` (72 × 72 starts) is too slow for 38 rows and is not used.

## Weave or thread

- **The potential is weave-type:** all three parities at once and every field of the frame, with none hand-picked.
- **The τ's are the strip's,** chosen by the data's six. So L1–L3 are frame results at data-chosen rows.
- **What would be a weave result:** a minimum on B1761's set at every row, from the content above with no free number.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| L0 | **The kernel.** At three strip rows, W59's `Joint` with N = 48 agrees with N = 64 to 10⁻⁶ relative (the lattice tail beyond 48 is about 10⁻⁷ of V), and the content's minimum moves by less than 10⁻⁶. V(ψ) = V(−ψ) to 10⁻¹². The T-law V(ψ₁, ψ₂; τ) = V(ψ₁, ψ₂ + ψ₁; τ + 1) holds to 10⁻⁶ at ten random ψ per row | 95% |
| L1 | **The minimum at the strip.** With the content above, the global minimum over the torus lies at a = 0 at every one of the 38 rows. No row's minimum is on B1761's set (a ∈ {1, 2, 3, 4}/5, b odd/10) | 90% |
| L2 | **B1761's points ranked.** At every row, every one of B1761's 20 points lies above the 10th percentile of V over the 266 census lines. That is, none is among the lowest tenth | 85% |
| L3 | **The boson weight.** With the bosons' weight multiplied by 2, 5 or 10, the global minimum stays at a = 0 at every row | 75% |
| R | **Read-outs** (no predictions): each row's minimum (a, b) and value; the depth of the 2/5 class's best point above the minimum; the boson multiplier at which a ≠ 0 first wins, if any up to 50. **The census over contents:** at each row, a linear programme maximises the margin t by which the line (2/5, 1/10), ψ = (−2/5, 1/10), is the strict global minimum over a 96 × 96 grid, outside a 0.02 neighbourhood of its ± images, with weights c_q ∈ [−1, 1] for each \|q\| ∈ {1, 2, 3, 4, 6}. It reports t* and the sign pattern of c when t* > 0 | — |

## What the outcomes mean (fixed now)

- **L1 and L2 hold:** the one-loop potential of the frame's own fields does not force B1761's condition. Its minimum
  is the line a = 0, which W162 found fails the six at every height. Stage 2 ends as the plan expected: **the line
  is one choice, counted** against the 19, and this potential cannot remove it.
- **L1 fails with the minimum on B1761's set at every row:** a forced line from the frame's own content, the record's
  first weave candidate for the line. It is checked again at fresh τ before any claim.
- **L1 fails otherwise:** the minimum's location is reported, and the line stays a choice.
- **The census:**
  - If t* > 0 at some row, a content selects the line. Its sign pattern says which charges must be bosonic, and the
    line's choice moves to GENESIS FK11's content, as a stated map.
  - If t* ≤ 0 at every row, no content of these charges selects it at one loop.

## Pre-mortem

The likeliest surprise is the boson-fermion balance. If the kernel's fermion sign at the strip favours a half-period
in a rather than 0, the minimum moves to a = ½: still not B1761's set, but L1 would fail as worded.

## What stays out

- The nine, the six and any target. No target file is read.
- Any other loop order, kernel or content.
- τ's dependence (stage 4) and the Higgs (stage 3).

## Looks

None at any target. The census over contents is a look at the frame only.

## Seen before the rule (disclosed)

- **W59's results:** the kernel, the torsion-point minima, and that a fermion goes to 0.
- **W160's, W162's and B1761's lines,** and that a = 0 lines fail the six (W162).
- **Reasoning, not computation.** The character formula and the T-law's action on the parities were worked by hand.
  So was the shell picture: at Im τ ≈ 3 the n = 0 shell dominates, so the potential mainly fixes q·a, and a
  fermion-dominated content pins a = 0. That is L1's prediction.
- **A sign corrected in the draft, by hand.** The draft first took ψ = (a, b). The kernel identity under τ → τ + 1
  showed that only ψ = (−a, b) carries the frame's T-law. This was settled before anything was computed.
- **Not computed:** no value of V at any strip τ. No script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read. A failed part is a failed launch, kept and disclosed.
- Any later check is labelled post hoc.

0 of 19.
